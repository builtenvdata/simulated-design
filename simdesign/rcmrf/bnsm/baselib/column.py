"""This module provides a base class for representing columns
within the BNSM layer and for building and exporting their OpenSees
representations.
"""
# Imports from installed packages
from abc import ABC
import numpy as np
import openseespy.opensees as ops
from typing import Dict, Literal, List, Tuple, Optional

# Imports from bnsm library
from .node import Node
from .constants import RIGID_MAT

# Imports from bdim base library
from ...bdim.baselib.column import ColumnBase as ColumnDesign

# Imports from utils library
from ....utils.units import MPa
from ....utils.misc import PRECISION, round_list
from ....utils import rcsection as rc
from ....utils.tags import sub_tag

PINCHX = 1.0
"""Pinching factor for strain (or deformation) during reloading"""
PINCHY = 1.0
"""Pinching factor for stress (or force) during reloading"""
DAMAGE1 = 0.0  # no degradation (default)
"""Damage due to ductility: D1(mu-1)"""
DAMAGE2 = 0.0  # no degradation (default)
"""Damage due to energy: D2(Eii/Eult)"""
BETA = 0.0  # from Dolšek and Fajfar 2005
"""Power used to determine the degraded unloading stiffness based on
ductility, mu-beta (optional, default=0.0)"""
HYSTERETIC_PARAMETERS = [PINCHX, PINCHY, DAMAGE1, DAMAGE2, BETA]
"""Hysteretic parameters"""


class ColumnBase(ABC):
    """Abstract Base Class for column implementations in BNSM layer.

    This class defines the common interface and core behaviour required to:
    (1) define a column member in the OpenSees domain, and
    (2) export equivalent Python and Tcl commands.

    The column is modelled using a force-based beam-column formulation
    (``forceBeamColumn``) with a plastic-hinge integration scheme
    (e.g., ``HingeRadau``). Geometric nonlinearity is accounted for through
    a P-Delta transformation (``geomTransf('PDelta', ...)``).

    Nonlinear behaviour is concentrated within finite plastic-hinge regions
    at the element ends, while the interior region remains elastic.

    Flexural response about the local axes (My and Mz) is represented by
    phenomenological moment-curvature relationships implemented using
    uniaxial ``Hysteretic`` materials and assembled into an aggregated
    hinge section.

    When ``capacity_design`` is False, shear behaviour is additionally
    modelled through ``Pinching4`` materials (for Vy and Vz), wrapped with
    ``MinMax`` limiters to enforce strength and deformation bounds. These
    shear components are included in the same aggregated hinge section.

    The interior region is represented by an elastic section, with optional
    use of cracked-section (effective) stiffness properties derived from the
    yield moment and curvature of the plastic hinges.

    Attributes
    ----------
    design : ~simdesign.rcmrf.bnsm.baselib.column.ColumnBase
        Instance of column design information model.
    capacity_design : bool
        Flag to check whether capacity shear design is followed or not.
    bondslip_factor : float
        Bondslip factor.
    axial_force: float
        Considered axial force on column.
    ele_node_i : Node
        Element node at the start of column.
    ele_node_j : Node
        Element node at the end of column.
    ele_load: float
        Uniformly distributed gravity load along the column.
    jnt_offsets : List[float]
        Rigid joint offset values (dx_i, dy_i, dz_i, dx_j, dy_j, dz_j),
        specified with respect to the global coordinate system.
    cracked : None | bool | float
        Cracked-section (effective) flexural properties of the elastic
        sections: True for ``EIeff = My / phi_y`` with the yield moment and
        curvature of the plastic hinges (see `yield_mom_curv`), or a float
        as the ratio of effective to gross flexural stiffness. If None or
        False, gross-section properties are used.
    cyclic_model : bool
        If True, the model parameters will be adjusted for cyclic analysis.
    _cy : float
        Neutral axis depth for shear hinge calculations in local-y.
    _cx : float
        Neutral axis depth for shear hinge calculations in local-x.
    _Iy_eff : float
        Effective column moment of inertia around local-y.
    _Ix_eff : float
        Effective column moment of inertia around local-x.
    yield_mom_curv : Literal['empirical', 'analytical']
        Yield moment and curvature of the plastic hinges: ``'empirical'``
        (Panagiotakos and Fardis, 2001) or ``'analytical'`` (section
        analysis).

    Notes
    -----
    Section view:

    .. code-block:: text

        Y (2)
        |__X (1)
            --------------    ----
            |     y      |    |
            |     |      |    |
            |  z--+      |    by
            |            |    |
            |            |    |
            --------------    ----
            |---- bx ----|

        Vectors defining the local axes in Global Coordinate System:
            vx = np.array([0.0, 0.0, 1.0])
            vy = np.array([0.0, 1.0, 0.0])
            vz = np.array([-1.0, 0.0, 0.0])
            vecxz = np.array([-1.0, 0.0, 0.0])
        Compatibility check:
            np.allclose(vy, np.cross(vecxz, vx))
            np.allclose(vz, np.cross(vx,vy))
    """
    design: ColumnDesign
    capacity_design: bool
    bondslip_factor: float
    axial_force: float
    ele_node_i: Node
    ele_node_j: Node
    ele_load: float
    jnt_offsets: List[float]
    cracked: Optional[bool | float] = None
    cyclic_model: bool
    yield_mom_curv: Literal['empirical', 'analytical']
    _cy: float
    _cx: float
    _Iy_eff: float
    _Ix_eff: float

    @property
    def ele_tag(self) -> int:
        """
        Returns
        -------
        int
            Tag of beam-column element representing the column.
        """
        return self.design.line.tag

    @property
    def vecxz(self) -> List[float]:
        """
        Returns
        -------
        List[float]
            X, Y, and Z components of vecxz for column elements along Z (3).
        """
        return [-1, 0, 0]

    @property
    def Ecm_q(self) -> float:
        """
        Returns
        -------
        float
            Elastic young's modulus of concrete (in base units).

        Note
        ----
        Based on quality adjusted concrete strength.
        """
        # Use quality adjusted elastic youngs modulus
        fc_mpa = self.design.fc_q / MPa  # convert to MPa
        return (22000 * (fc_mpa / 10)**0.3) * MPa

    @property
    def Gcm_q(self) -> float:
        """
        Returns
        -------
        float
            Elastic shear modulus of concrete (in base units).

        Note
        ----
        Based on quality adjusted concrete strength.
        """
        return self.Ecm_q / (2 * (1 + self.design.concrete.POISSONS_RATIO))

    @property
    def Acc(self) -> float:
        """
        Returns
        -------
        float
            Confined concrete area.
        """
        bx = self.design.bx - 2 * (self.design.cover_q + self.design.dbh_q / 2)
        by = self.design.by - 2 * (self.design.cover_q + self.design.dbh_q / 2)
        return float(bx * by)

    @property
    def rhol_q(self) -> float:
        """
        Returns
        -------
        float
            In situ (quality adjusted) longitudinal reinforcement area ratio.
        """
        Abl_cor = (np.pi * self.design.dbl_cor_q**2) / 4
        Abl_int = (np.pi * self.design.dbl_int_q**2) / 4
        nbl_int = 2 * (self.design.nbly_int_q + self.design.nblx_int_q)
        nbl_cor = 4
        return (nbl_cor * Abl_cor + nbl_int * Abl_int) / self.design.Ag

    @property
    def rhol_q_(self) -> float:
        """
        Returns
        -------
        float
            In situ (quality adjusted) longitudinal reinforcement area ratio.
            Computed using confined concrete dimensions.
        """
        Abl_cor = (np.pi * self.design.dbl_cor_q**2) / 4
        Abl_int = (np.pi * self.design.dbl_int_q**2) / 4
        nbl_int = 2 * (self.design.nbly_int_q + self.design.nblx_int_q)
        nbl_cor = 4

        return (nbl_cor * Abl_cor + nbl_int * Abl_int) / self.Acc

    @property
    def rhoh_x_q(self) -> float:
        """
        Returns
        -------
        float
            In situ (quality adjusted) transverse reinforcement area (in x)
            ratio.
        """
        Abh_x = self.design.nbh_x_q * (np.pi * self.design.dbh_q**2) / 4
        return Abh_x / (self.design.sbh_q * self.design.by)

    @property
    def rhoh_y_q(self) -> float:
        """
        Returns
        -------
        float
            In situ (quality adjusted) transverse reinforcement area (in y)
            ratio.
        """
        Abh_y = self.design.nbh_y_q * (np.pi * self.design.dbh_q**2) / 4
        return Abh_y / (self.design.sbh_q * self.design.bx)

    @property
    def rhoh_x_q_(self) -> float:
        """
        Returns
        -------
        float
            In situ (quality adjusted) transverse reinforcement area (in x)
            ratio. Computed using confined concrete dimensions.
        """
        # Total transverse reinforcement area
        Av = self.design.nbh_x_q * (np.pi * self.design.dbh_q**2) / 4
        # Transverse reinforcement spacing
        s = self.design.sbh_q
        # Core diameter
        dc = self.design.by - 2 * (self.design.cover_q + self.design.dbh_q / 2)
        return Av / (s * dc)

    @property
    def rhoh_y_q_(self) -> float:
        """
        Returns
        -------
        float
            In situ (quality adjusted) transverse reinforcement area (in y)
            ratio. Computed using confined concrete dimensions.
        """
        # Total transverse reinforcement area
        Av = self.design.nbh_y_q * (np.pi * self.design.dbh_q**2) / 4
        # Transverse reinforcement spacing
        s = self.design.sbh_q
        # Core diameter
        dc = self.design.bx - 2 * (self.design.cover_q + self.design.dbh_q / 2)
        return Av / (s * dc)

    @property
    def mz_mat_tag(self) -> int:
        """Uniaxial material tag for the flexural hinge about local-z (Mz)."""
        return sub_tag(self.design.line.tag, 91)

    @property
    def my_mat_tag(self) -> int:
        """Uniaxial material tag for the flexural hinge about local-y (My)."""
        return sub_tag(self.design.line.tag, 93)

    @property
    def vy_mat_tag_(self) -> int:
        """Pinching4 material tag for the shear hinge in local-y (Vy)."""
        return sub_tag(self.design.line.tag, 94)

    @property
    def vy_mat_tag(self) -> int:
        """MinMax material tag for the shear hinge in local-y (Vy)."""
        return sub_tag(self.design.line.tag, 95)

    @property
    def vz_mat_tag_(self) -> int:
        """Pinching4 material tag for the shear hinge in local-z (Vz)."""
        return sub_tag(self.design.line.tag, 96)

    @property
    def vz_mat_tag(self) -> int:
        """MinMax material tag for the shear hinge in local-z (Vz)."""
        return sub_tag(self.design.line.tag, 97)

    @property
    def elastic_sec_tag(self) -> int:
        """Section tag for the elastic (interior) section."""
        return sub_tag(self.design.line.tag, 90)

    @property
    def inelastic_sec_tag(self) -> int:
        """Section tag for the inelastic aggregated section."""
        return sub_tag(self.design.line.tag, 92)

    @property
    def interior_sec_tag(self) -> int:
        """Section tag for the interior section with shear springs."""
        return sub_tag(self.design.line.tag, 93)

    @property
    def int_tag(self) -> int:
        """Beam integration tag used by OpenSees."""
        return self.design.line.tag

    @property
    def geo_transf_tag(self) -> int:
        """Geometric transformation tag used by OpenSees."""
        return self.design.line.tag

    def __init__(
        self, design: ColumnDesign, bondslip_factor: float,
        capacity_design: bool, load_factors: Dict[Literal['G', 'Q'], float],
        cyclic_model: bool = False,
        cracked: Optional[bool | float] = None,
        yield_mom_curv: Literal['empirical', 'analytical'] = 'empirical'
    ) -> None:
        """Initialize the Column object.

        Parameters
        ----------
        design : ~simdesign.rcmrf.bnsm.baselib.column.ColumnBase
            Instance of column design information model.
        bondslip_factor : float
            Bondslip factor considered while defining plastic hinges.
        capacity_design : bool
            Flag to check whether capacity shear design is followed or not.
        load_factors : Dict[Literal['G', 'Q'], float]
            Load factors used to compute gravity loads/forces on the column.
        cyclic_model : bool, optional
            If True, the model parameters will be adjusted for cyclic analysis.
            By default False.
        cracked : None | bool | float, optional
            Cracked-section (effective) flexural properties of the elastic
            sections: True for My / phi_y of the plastic hinges (see
            `yield_mom_curv`), or a float as the ratio of effective to gross
            flexural stiffness. If None or False, gross-section properties
            are used. By default None.
        yield_mom_curv : Literal['empirical', 'analytical'], optional
            Yield moment and curvature of the plastic hinges: 'empirical'
            from the expressions of Panagiotakos and Fardis (2001),
            'analytical' from a moment-curvature section analysis.
            By default 'empirical'.
        """
        self.design = design
        self.bondslip_factor = bondslip_factor
        self.capacity_design = capacity_design
        self.cyclic_model = cyclic_model
        self.cracked = cracked
        self.yield_mom_curv = yield_mom_curv
        self.axial_force = -(load_factors['G'] * design.hinge_Ng
                             + load_factors['Q'] * design.hinge_Nq)
        self.ele_load = float(design.self_wg * load_factors['G'])
        self.jnt_offsets = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        # Set cracked section properties
        self._set_cracked_properties()

    def add_to_ops(self) -> None:
        """Adds column components to the OpenSees domain
        (i.e, column element and nodes).

        Notes
        -----
        Same hinge materials are used at both ends.
        """
        # Define geometric transformation
        ops.geomTransf(*self._get_geo_transf_inputs())

        # Create the section materials
        ops.uniaxialMaterial(*self._get_rot_hinge_mat_inputs('x'))
        ops.uniaxialMaterial(*self._get_rot_hinge_mat_inputs('y'))
        if not self.capacity_design:
            vy_mat, minmax_vy = self._get_shear_hinge_mat_inputs('y')
            vz_mat, minmax_vz = self._get_shear_hinge_mat_inputs('x')
            ops.uniaxialMaterial(*vy_mat)
            ops.uniaxialMaterial(*vz_mat)
            ops.uniaxialMaterial(*minmax_vy)
            ops.uniaxialMaterial(*minmax_vz)

        # Create element sections
        ops.section(*self._get_elastic_sec_inputs())
        ops.section(*self._get_inelastic_sec_inputs())
        if not self.capacity_design:  # Interior section with shear springs
            ops.section(*self._get_interior_sec_inputs())

        # Create beam integration
        ops.beamIntegration(*self._get_int_inputs())

        # Create the element
        ops.element(*self._get_ele_inputs())

    def to_py(self) -> List[str]:
        """Gets the Python commands to construct column components in OpenSees
        domain (i.e, column element and nodes).

        Returns
        -------
        List[str]
            List of Python commands for constructing the components of column
            object in OpenSees.

        Notes
        -----
        Same hinge materials are used at both ends.
        """
        # Define geometric transformation
        content = ['# Create geometric transformation']
        transf_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_geo_transf_inputs()
        )
        content.append(f"ops.geomTransf({transf_inputs})")

        # Create the section materials
        content.append('# Create uniaxial materials')
        mz_mat_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_rot_hinge_mat_inputs('x')
        )
        my_mat_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_rot_hinge_mat_inputs('y')
        )
        content.append(f"ops.uniaxialMaterial({mz_mat_inputs})")
        content.append(f"ops.uniaxialMaterial({my_mat_inputs})")

        if not self.capacity_design:
            vy_mat, minmax_vy = self._get_shear_hinge_mat_inputs('y')
            vz_mat, minmax_vz = self._get_shear_hinge_mat_inputs('x')
            vy_mat_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in vy_mat
            )
            vz_mat_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in vz_mat
            )
            minmax_vy_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in minmax_vy
            )
            minmax_vz_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in minmax_vz
            )
            content.append(f"ops.uniaxialMaterial({vy_mat_inputs})")
            content.append(f"ops.uniaxialMaterial({minmax_vy_inputs})")
            content.append(f"ops.uniaxialMaterial({vz_mat_inputs})")
            content.append(f"ops.uniaxialMaterial({minmax_vz_inputs})")

        # Create sections
        content.append('# Create element sections')
        elastic_sec_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_elastic_sec_inputs()
        )
        inelastic_sec_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_inelastic_sec_inputs()
        )
        content.append(f"ops.section({elastic_sec_inputs})")
        content.append(f"ops.section({inelastic_sec_inputs})")
        if not self.capacity_design:  # Interior section with shear springs
            interior_sec_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in self._get_interior_sec_inputs()
            )
            content.append(f"ops.section({interior_sec_inputs})")

        # Create beam integration
        content.append('# Create integration scheme')
        int_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_int_inputs()
        )
        content.append(f"ops.beamIntegration({int_inputs})")

        # Create column element
        content.append('# Create element')
        ele_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_ele_inputs()
        )
        content.append(f"ops.element({ele_inputs})")

        return content

    def to_tcl(self) -> List[str]:
        """Gets the Tcl commands to construct column components in OpenSees
        domain (i.e, column element and nodes).

        Returns
        -------
        List[str]
            List of Tcl commands for constructing the components of column
            object in OpenSees.

        Notes
        -----
        Same hinge materials are used at both ends.
        """
        # Define geometric transformation
        content = ['# Create geometric transformation']
        transf_inputs = ' '.join(f"{item}" for item in
                                 self._get_geo_transf_inputs())
        content.append(f"geomTransf {transf_inputs}")

        # Create the section materials
        content.append('# Create uniaxial materials')
        mz_mat_inputs = ' '.join(
            f"{item}" for item in self._get_rot_hinge_mat_inputs('x'))
        my_mat_inputs = ' '.join(
            f"{item}" for item in self._get_rot_hinge_mat_inputs('y'))
        content.append(f"uniaxialMaterial {mz_mat_inputs}")
        content.append(f"uniaxialMaterial {my_mat_inputs}")

        if not self.capacity_design:
            vy_mat, minmax_vy = self._get_shear_hinge_mat_inputs('y')
            vz_mat, minmax_vz = self._get_shear_hinge_mat_inputs('x')
            vy_mat_inputs = ' '.join(f"{item}" for item in vy_mat)
            vz_mat_inputs = ' '.join(f"{item}" for item in vz_mat)
            minmax_vy_inputs = ' '.join(f"{item}" for item in minmax_vy)
            minmax_vz_inputs = ' '.join(f"{item}" for item in minmax_vz)
            content.append(f"uniaxialMaterial {vy_mat_inputs}")
            content.append(f"uniaxialMaterial {minmax_vy_inputs}")
            content.append(f"uniaxialMaterial {vz_mat_inputs}")
            content.append(f"uniaxialMaterial {minmax_vz_inputs}")

        # Create sections
        content.append('# Create element sections')
        elastic_sec_inputs = ' '.join(
            f"{item}" for item in self._get_elastic_sec_inputs())
        inelastic_sec_inputs = ' '.join(
            f"{item}" for item in self._get_inelastic_sec_inputs())
        content.append(f"section {elastic_sec_inputs}")
        content.append(f"section {inelastic_sec_inputs}")
        if not self.capacity_design:  # Interior section with shear springs
            interior_sec_inputs = ' '.join(
                f"{item}" for item in self._get_interior_sec_inputs())
            content.append(f"section {interior_sec_inputs}")

        # Create beam integration
        content.append('# Create integration scheme')
        int_inputs = ' '.join(
            f"{item}" for item in self._get_int_inputs())
        content.append(f"beamIntegration {int_inputs}")

        # Create column element
        content.append('# Create element')
        ele_inputs = ' '.join(
            f"{item}" for item in self._get_ele_inputs())
        content.append(f"element {ele_inputs}")

        return content

    def add_grav_loads_to_ops(self) -> None:
        """Adds gravity load objects to the OpenSees domain
        (i.e, point loads at both ends).
        """
        point_load = round(self.ele_load * self.design.H / 2, PRECISION)
        load_values = [0.0, 0.0, -point_load, 0.0, 0.0, 0.0]
        ops.load(self.ele_node_i.tag, *load_values)
        ops.load(self.ele_node_j.tag, *load_values)

    def to_py_grav_loads(self) -> List[str]:
        """Gets the Python commands to construct column gravity load object in
        OpenSees domain (i.e, point loads at both ends).

        Returns
        -------
        List[str]
            List of Python commands for adding column gravity loads
            to OpenSees.
        """
        point_load = round(self.ele_load * self.design.H / 2, PRECISION)
        load_values = f"0.0, 0.0, {-point_load}, 0.0, 0.0, 0.0"
        return [
            f"ops.load({self.ele_node_i.tag}, {load_values})",
            f"ops.load({self.ele_node_j.tag}, {load_values})"
        ]

    def to_tcl_grav_loads(self) -> List[str]:
        """Gets the Tcl commands to construct column gravity load object in
        OpenSees domain (i.e, point loads at both ends).

        Returns
        -------
        List[str]
            List of Tcl commands for adding column gravity loads to OpenSees.
        """
        point_load = round(self.ele_load * self.design.H / 2, PRECISION)
        load_values = f"0.0 0.0 {-point_load} 0.0 0.0 0.0"
        return [
            f"load {self.ele_node_i.tag} {load_values}",
            f"load {self.ele_node_j.tag} {load_values}"
        ]

    def _get_geo_transf_inputs(self) -> List[str | float]:
        """Builds the OpenSees ``geomTransf`` command arguments.

        Returns
        -------
        List[str | float | int]
            Inputs for ``ops.geomTransf``, including the transformation type,
            tag, ``vecxz`` definition, and optional joint offsets.
        """
        inputs = ['PDelta', self.geo_transf_tag] \
            + self.vecxz + ['-jntOffset'] + self.jnt_offsets
        return inputs

    def _get_ele_inputs(self) -> List[str | int]:
        """Retrieves column element inputs.

        Returns
        -------
        List[str | int]
            List of column element inputs.
        """
        ele_inputs = [
            'forceBeamColumn', self.design.line.tag,
            self.ele_node_i.tag, self.ele_node_j.tag,
            self.geo_transf_tag, self.int_tag
        ]

        return ele_inputs

    def _get_elastic_sec_inputs(self) -> List[str | float | int]:
        """Retrieves elastic column section inputs.

        Returns
        -------
        List[str | float | int]
            List of elastic column section inputs.
        """
        # Cracked section properties
        if self.cracked:
            Iz = self._Ix_eff
            Iy = self._Iy_eff
        else:
            Iz = self.design.Ix
            Iy = self.design.Iy
        # Set the inputs
        sec_inputs = round_list([
            'Elastic', self.elastic_sec_tag, self.Ecm_q, self.design.Ag,
            Iz, Iy, self.Gcm_q, self.design.J
        ])

        return sec_inputs

    def _get_inelastic_sec_inputs(self) -> List[str | int]:
        """Retrieves inputs for inelastic aggregated column section.

        Returns
        -------
        List[str | int]
            List of inputs for inelastic aggregated column section.
        """
        sec_inputs = [
            'Aggregator', self.inelastic_sec_tag,
            RIGID_MAT, 'P',
            self.mz_mat_tag, 'Mz',
            self.vy_mat_tag, 'Vy',
            self.my_mat_tag, 'My',
            self.vz_mat_tag, 'Vz',
            RIGID_MAT, 'T'
        ]
        if self.capacity_design:
            sec_inputs[6], sec_inputs[10] = RIGID_MAT, RIGID_MAT

        return sec_inputs

    def _get_interior_sec_inputs(self) -> List[str | int]:
        """Retrieves inputs for the interior section with shear springs.

        Returns
        -------
        List[str | int]
            List of inputs for the aggregated interior section, i.e., the
            elastic section aggregated with the shear force - shear strain
            materials (Vy and Vz).

        Notes
        -----
        The shear materials define shear force vs. average shear strain of
        the member (Mergos and Kappos, 2012; Zimos et al., 2015). Including
        them in the interior section integrates the shear strains along the
        whole member length rather than only over the plastic hinge lengths.
        """
        sec_inputs = [
            'Aggregator', self.interior_sec_tag,
            self.vy_mat_tag, 'Vy',
            self.vz_mat_tag, 'Vz',
            '-section', self.elastic_sec_tag
        ]

        return sec_inputs

    def _get_int_inputs(self) -> List[str | float | int]:
        """Retrieves column integration inputs.

        Returns
        -------
        List[str | float | int]
            List of column integration inputs.

        References
        ----------
        Scott, M. H., & Fenves, G. L. (2006). Plastic Hinge Integration Methods
        for Force-Based Beam-Column Elements. Journal of Structural
        Engineering, 132(2), 244-252.
        https://doi.org/10.1061/(asce)0733-9445(2006)132:2(244)
        """
        # Plastic hinge length based on Priestley et al. 2007
        Lp = self._get_lp()
        # Beam integration inputs
        # Interior section, including the shear springs if they are used
        if self.capacity_design:
            interior_sec_tag = self.elastic_sec_tag
        else:
            interior_sec_tag = self.interior_sec_tag
        int_inputs = [
            'HingeRadau', self.int_tag,
            self.inelastic_sec_tag, Lp, self.inelastic_sec_tag, Lp,
            interior_sec_tag
        ]

        return int_inputs

    def _get_shear_hinge_mat_inputs(self, axis: Literal['x', 'y']
                                    ) -> Tuple[List[float], List[float]]:
        """Gets inputs the shear plastic hinge materials for given axis.

        The model is based on Zimos et al. (2015).

        Parameters
        ----------
        axis : Literal['x', 'y']
            The local axis considered for the calculations.

        Returns
        -------
        shear_mat_inputs : List[float]
            Pinching4 material model inputs for the plastic hinge describing
            shear behaviour in `axis`.
        minmax_mat_inputs : List[float]
            Inputs for MinMax uniaxialMaterial describing the axial failure
            in `axis`.

        References
        ----------
        Zimos, D. K., Mergos, P. E., & Kappos, A. J. (2015). Shear hysteresis
        model for reinforced concrete elements including the post-peak range.
        Proceedings of the COMPDYN. https://doi.org/10.7712/120115.3565.1184

        Sezen, H. and Moehle, J.P. (2004). Shear Strength Model for Lightly
        Reinforced Concrete Columns. J Struct Eng 130:1692-1703.
        https://doi.org/10.1061/(asce)0733-9445(2004)130:11(1692)

        Priestley, M. N., Verma, R., & Xiao, Y. (1994). Seismic shear strength
        of reinforced concrete columns. Journal of structural engineering,
        120(8), 2310-2329.
        https://doi.org/10.1061/(ASCE)0733-9445(1994)120:8(2310)

        Mergos, P. E., & Kappos, A. J. (2012). A gradual spread inelasticity
        model for R/C beam-columns, accounting for flexure, shear and
        anchorage slip. Engineering Structures, 44, 94-106.
        https://doi.org/10.1016/j.engstruct.2012.05.035

        O'Reilly, G. J. (2016). Performance-based seismic assessment and
        retrofit of existing RC frame buildings in Italy (Doctoral
        dissertation, IUSS Pavia).
        """
        if axis == 'y':
            # Section height
            h = self.design.by  # along y
            # Section width
            b = self.design.bx  # along x
            # Number of horizontal bars (stirrup legs)
            nbh = self.design.nbh_y_q
            # Transverse reinforcement area ratio
            rhoh = self.rhoh_y_q
            # Neutral axis depth (NOTE: the same value from M-Phi analysis)
            c = self._cy  # An approximate conservative value
            # The integer tag for the MinMax uniaxial material defining failure
            minmax_mat_tag = self.vy_mat_tag
            # The integer tag for the material describing shear behaviour in
            # local -y (corresponds to y in ops)
            shear_mat_tag = self.vy_mat_tag_
        elif axis == 'x':
            # Section height
            h = self.design.bx  # along x
            # Section width
            b = self.design.by  # along y
            # Number of horizontal bars (stirrup legs)
            nbh = self.design.nbh_x_q
            # Transverse reinforcement area ratio
            rhoh = self.rhoh_x_q
            # Neutral axis depth (NOTE: the same value from M-Phi analysis)
            c = self._cx  # An approximate conservative value
            # The integer tag for the MinMax uniaxial material defining failure
            minmax_mat_tag = self.vz_mat_tag
            # The integer tag for the material describing shear behaviour in
            # local -x (corresponds to z in ops)
            shear_mat_tag = self.vz_mat_tag_

        # Gross corss-section area
        Ag = self.design.Ag
        # Concrete compressive strength
        fc = self.design.fc_q  # in base units
        # Concrete elastic modulus
        Ec = self.Ecm_q
        # Concrete shear modulus
        Gc = self.Gcm_q
        # Transverse reinforcement yield strength
        fsyh = self.design.fsyh_q  # in base units
        # Steel shear modulus
        Es = self.design.steel.Es
        # Diameter of internal reinforcement
        dbl_int = self.design.dbl_int_q
        # Longitudinal reinforcement ratio
        rhol = self.rhol_q
        # Longitudinal reinforcement area
        Asl = rhol * Ag
        # Average long. reinf. bar diameter
        nbl_int = 2 * (self.design.nbly_int_q + self.design.nblx_int_q)
        nbl_cor = 4
        dbl_ave = np.sqrt(4 * Asl / (nbl_int + nbl_cor) / np.pi)

        # Longitudinal reinforcement yield strength
        fsyl = self.design.fsyl_q  # in base units
        # Concrete cover
        cover = self.design.cover_q
        # Stirrup spacing
        sbh = self.design.sbh_q
        # Horizontal (stirrup) reinforcement diameter
        dbh = self.design.dbh_q
        # Core height measured to centerline of transverse reinforcement
        hc = h - 2*(cover + dbh/2)
        # Core width measured to centerline of transverse reinforcement
        bc = b - 2*(cover + dbh/2)
        # Transverse reinforcement area
        Av = nbh * np.pi * (dbh**2) / 4
        # Distance between top concrete fiber and bottom tension steel
        d = h - (cover + dbh + dbl_int/2)
        # Nominal length of column
        Ln = self.design.H
        # Shear span, assuming equal to 50% of the free length of the element
        Ls = Ln / 2  # NOTE: Could be varied with intensity of loading, but ok.
        # Compressive axial load (+) - Positive in compression
        P = max(-self.axial_force, 0)
        # Normalized axial load ratio (dimensionless)
        nu = P / (self.design.Ag * fc)

        # Onset of cracking - Sezen and Moehle (2004), with the concrete
        # tensile strength of Collins and Mitchell (1997)
        V1, gamm_1 = rc.get_shear_cracking_sezen_moehle2004(
            fc, Gc, Ag, d, Ls, P)

        # Onset of maximum shear force - Priestley et al. (1994)
        Vc, Vp, Vs = rc.get_shear_strength_priestley1994(
            fc, Ag, h, c, Ls, Av, fsyh, hc, sbh, P)
        # Maximum shear strength
        Vmax = Vc + Vp + Vs
        V2 = Vmax

        # NOTE: V1 cannot be greater than V2, this is a superficial adjustment.
        if V1 > V2:  # This may happen even though, rare!
            V1 = 0.8 * V2  # Assume V1 is 80% of V2
            gamm_1 = V1 / (Gc * (0.8 * Ag))  # Adjust gamm_1 accordingly

        # Cracked shear stiffness, shear strains at the maximum shear force
        # and at the onset of shear failure - Mergos and Kappos (2012)
        _, gamm_2, gamm_3 = rc.get_shear_strains_mergos_kappos2012(
            V1, gamm_1, V2, Es, Ec, b, hc, rhoh, fsyh, fc, Ls, h, nu)
        V3 = Vmax

        # NOTE: Followings are superficial adjustments for numerical purposes
        if gamm_3 > gamm_2:  # 2nd and 3rd points are not the same
            # OpenSees may complain due to zero shear stiffness
            V2 = 0.9 * V2  # To avoid 0 stiffness between 2nd & 3rd points
        elif gamm_3 == gamm_2:  # 2nd and 3rd points are the same
            gamm_2 = gamm_2 - 0.1 * (gamm_2 - gamm_1)
            V2 = V2 - 0.1 * (V2 - V1)

        # Onset of axial failure - Zimos et al. (2015)
        Spp, gamm_tpp = rc.get_shear_post_peak_zimos2015(
            Vmax, P, b, d, Ag, hc * bc, rhol, rhoh, fc, fsyl, fsyh, sbh,
            dbl_ave, nu)
        # Residual shear force, at least 10% of the maximum - Eqn. 3
        V4, gamm_tpp = rc.get_shear_residual_zimos2015(V3, Spp, gamm_tpp)
        # Residual shear strain
        gamm_4 = gamm_3 + gamm_tpp

        # Pinching4 material backbone parameters
        ePf1, ePf2, ePf3, ePf4 = V1, V2, V3, V4
        ePd1, ePd2, ePd3, ePd4 = gamm_1, gamm_2, gamm_3, gamm_4
        eNf1, eNf2, eNf3, eNf4 = -V1, -V2, -V3, -V4
        eNd1, eNd2, eNd3, eNd4 = -gamm_1, -gamm_2, -gamm_3, -gamm_4

        # Pinching4 material Unloading/Reloading parameters
        # Ratio of maximum deformation at which reloading begins
        rDispP, rDispN = 0.4, 0.4  # from Table 2.3. in O'Reilly 2016
        # Ratio of envelope force at which reloading begins
        rForceP, rForceN = 0.2, 0.2  # from Table 2.3. in O'Reilly 2016
        # Ratio of monotonic strength developed upon unloading
        uForceP, uForceN = 0.0, 0.0  # from Table 2.3. in O'Reilly 2016
        # Coefficients for Unloading Stiffness degradation
        gK1, gK2, gK3, gK4, gKLim = 0.0, 0.0, 0.0, 0.0, 0.0  # No degredation
        # Coefficients for Reloading Stiffness degradation
        gD1, gD2, gD3, gD4, gDLim = 0.0, 0.0, 0.0, 0.0, 0.0  # No degredation
        # Coefficients for Strength degradation
        gF1, gF2, gF3, gF4, gFLim = 0.0, 0.0, 0.0, 0.0, 0.0  # No degredation
        # Cyclic energy dissipation factor (E_cyclic=gE*E_monotonic)
        gE = 0.0  # No degredation
        # Damage type
        dmgType = "energy"
        shear_mat_inputs = [
            'Pinching4', shear_mat_tag,
            ePf1, ePd1, ePf2, ePd2, ePf3, ePd3, ePf4, ePd4,
            eNf1, eNd1, eNf2, eNd2, eNf3, eNd3, eNf4, eNd4,
            rDispP, rForceP, uForceP,
            rDispN, rForceN, uForceN,
            gK1, gK2, gK3, gK4, gKLim,
            gD1, gD2, gD3, gD4, gDLim,
            gF1, gF2, gF3, gF4, gFLim,
            gE, dmgType
        ]

        # MinMax material inputs
        minmax_mat_inputs = [
            'MinMax', minmax_mat_tag, shear_mat_tag,
            '-min', -gamm_4, '-max', gamm_4
        ]

        # Rounding to precision
        minmax_mat_inputs = round_list(minmax_mat_inputs)
        shear_mat_inputs = round_list(shear_mat_inputs)

        return shear_mat_inputs, minmax_mat_inputs

    def _get_rot_hinge_mat_inputs(self, axis: Literal['x', 'y']
                                  ) -> List[float | str]:
        """Gets the plastic hinge material properties for given axis.

        Parameters
        ----------
        axis : Literal['x', 'y']
            The local axis considered for the calculations.

        Returns
        -------
        rot_mat_inputs : List[float | str]
            Hysteretic material model inputs for the plastic hinge describing
            behaviour in flexure around `axis`. The curvatures are adjusted so
            that the member yields at the yield rotation (see
            ``_get_phiy_adjusted``), and the plastic rotations are spread over
            the plastic hinge length.
        """
        if axis == 'x':
            # The integer tag for the material describing flexure behaviour
            # around local -x (corresponds to z in ops)
            flex_mat_tag = self.mz_mat_tag

        elif axis == 'y':
            # The integer tag for the material describing flexure behaviour
            # around local -y axis (corresponds to y in ops)
            flex_mat_tag = self.my_mat_tag

        # Backbone of the plastic hinges
        (
            _, My, Mc, Mr, theta_y, theta_cap_pl, theta_pc,
         ) = self._get_rot_hinge_props(axis)

        # Rotation values
        theta_1 = theta_y
        theta_2 = theta_1 + theta_cap_pl
        theta_3 = theta_2 + theta_pc

        # Curvature values
        # Accounting for all the flexibility sources of the yield rotation
        Lp = self._get_lp()
        phi_1 = self._get_phiy_adjusted(My, theta_y, Lp, axis)
        phi_2 = (theta_2 - theta_1) / Lp + phi_1
        phi_3 = (theta_3 - theta_1) / Lp + phi_1

        # Material inputs
        rot_mat_inputs = [
            'Hysteretic', flex_mat_tag,
            My, phi_1, Mc, phi_2, Mr, phi_3,
            -My, -phi_1, -Mc, -phi_2, -Mr, -phi_3,
            *HYSTERETIC_PARAMETERS
        ]

        # Rounding to precision
        rot_mat_inputs = round_list(rot_mat_inputs)

        return rot_mat_inputs

    def _get_rot_hinge_props(self, axis: Literal['x', 'y']) -> List[float]:
        """Computes the backbone parameters of the rotational plastic hinge
        about the specified local axis.

        Parameters
        ----------
        axis : Literal['x', 'y']
            Local bending axis considered for the calculations.

        Returns
        -------
        props : List[float]
            Ordered list of backbone parameters for the specified axis:

            0. ``phi_y`` Yield curvature.
            1. ``My`` Yield moment.
            2. ``Mc`` Capping (maximum) moment.
            3. ``Mr`` Residual moment.
            4. ``theta_y`` Yield rotation.
            5. ``theta_cap_pl`` Plastic rotation capacity up to capping.
            6. ``theta_pc`` Post-capping rotation capacity.

        Notes
        -----
        The yield rotation follows EN 1998-3 Eq. A.10b. Its shear distortion
        term is left out if the shear deformations are modelled with shear
        springs, i.e., if ``capacity_design`` is False.

        References
        ----------
        Haselton, C. B., Liel, A. B., Lange, S. T., & Deierlein, G. G. (2008).
        Beam-column element model calibrated for predicting flexural response
        leading to global collapse of RC frame buildings. Pacific Earthquake
        Engineering Research Center, University of California, Berkeley, CA.

        Haselton, C. B., Liel, A. B., Taylor-Lange, S. C., & Deierlein, G. G.
        (2016). Calibration of model to simulate response of reinforced
        concrete beam-columns to collapse. ACI Structural Journal, 113(6).

        CEN (2005) Eurocode 8: Design of structures for earthquake resistance -
        Part 3: Assessment and retrofitting of existing buildings.
        Brussels, Belgium

        Panagiotakos, T. B., & Fardis, M. N. (2001).
        Deformations of reinforced concrete members at yielding and ultimate.
        Structural Journal, 98(2), 135-148.

        ACI CODE 318-25. (2025). Building Code for Structural Concrete-Code
        Requirements and Commentary. American Concrete Institute.
        """
        if axis == 'x':
            # Section height and width
            h, b = self.design.by, self.design.bx  # along y, along x
            # Transverse reinforcement ratio
            rhoh = self.rhoh_y_q  # Stirrups are along -y axis

        elif axis == 'y':
            # Section height and width
            h, b = self.design.bx, self.design.by  # along x, along y
            # Transverse reinforcement ratio
            rhoh = self.rhoh_x_q  # Stirrups are along -x axis

        # Diameter of corner reinforcement
        dbl_cor = self.design.dbl_cor_q
        # Concrete compressive strength in base units
        fc = self.design.fc_q
        # Longitudinal steel yield strength in base units
        fsyl = self.design.fsyl_q
        # Nominal length of column
        Ln = self.design.H
        # Stirrup spacing
        sbh = self.design.sbh_q
        # Longitudinal reinforcement ratio
        rhol = self.rhol_q
        # Compressive axial load (+)
        Nu = max(-self.axial_force, 0)

        # Compute yield moment and curvature
        My, phi_y, _ = self._get_my_phiy(axis)

        # Shear span, assuming equal to 50% of the free length of the element
        Ls = Ln / 2  # NOTE: Could be varied with intensity of loading, but ok.
        # Axial load ratio
        niu = Nu / (self.design.Ag * fc)

        # Yield rotation capacity - EN 1998-3:2004 - Equation A.10b
        # (tension shift factor from the shear cracking resistance - EN 1992-1)
        As_tens, dd = self._get_tension_rebar(axis)
        if self.capacity_design:
            include_shear = True
        else:
            include_shear = False
        theta_y = rc.get_yield_rot_eurocode8(
            phi_y, h, Ls, fc, fsyl, dbl_cor, self.bondslip_factor,
            My=My, b=b, As_tens=As_tens, dd=dd, Nu=Nu,
            include_shear=include_shear)

        # Maximum moment capacity and plastic rotation capacity by
        # Haselton et al. 2016
        Mc, theta_cap_pl = rc.get_capping_mom_plastic_rot_haselton2016(
            My, fc, fsyl, rhol, rhoh, sbh, dbl_cor, niu,
            self.bondslip_factor, cyclic_model=self.cyclic_model)
        # Residual moment and post-capping rotation capacity by
        # Haselton et al. 2016
        Mr, theta_pc = rc.get_residual_mom_post_capping_rot_haselton2016(
            Mc, rhoh, niu, cyclic_model=self.cyclic_model)

        # Save to list
        props = [
            float(phi_y), float(My), float(Mc), float(Mr),
            float(theta_y), float(theta_cap_pl), float(theta_pc),
        ]

        return props

    def _get_phiy_adjusted(self, My: float, theta_y: float, Lp: float,
                           axis: Literal['x', 'y']) -> float:
        """Computes the yield curvature of the plastic hinge sections
        based on yield rotation capacity.

        The hinges account for all the flexibility sources of the yield
        rotation ``theta_y`` (EN 1998-3 Eq. A.10b: tension shift, shear
        distortion and bond-slip). The elastic interior gives the flexural
        yield rotation ``My·Ls/(3·EI)``, and the hinge carries the rest of
        ``theta_y`` over ``Lp``, so that the member reaches ``theta_y`` when
        the hinge yields.

        Parameters
        ----------
        My : float
            Yield moment.
        theta_y : float
            Yield rotation.
        Lp : float
            Plastic hinge length.
        axis : Literal['x', 'y']
            The local axis considered for the calculations.

        Returns
        -------
        float
            Yield curvature of the plastic hinge sections.
        """
        sec_inputs = self._get_elastic_sec_inputs()
        ls = self.design.H / 2  # Shear span, as in _get_backbone
        EIeff = self.Ecm_q * (sec_inputs[4] if axis == 'x' else sec_inputs[5])
        dtheta = max(theta_y - My * ls / (3 * EIeff), 0.0)
        phi_y = My / EIeff + dtheta / Lp
        return phi_y

    def _get_lp(self) -> float:
        """Computes the plastic hinge length of the column.

        Returns
        -------
        Lp : float
            Plastic hinge length.

        References
        ----------
        Priestley, M. J. N., Calvi, G. M., & Kowalsky, M. J. (2007).
        *Displacement-based seismic design of structures*. IUSS Press.
        """
        # Shear span, assuming equal to 50% of the free length of the element
        Ls = self.design.line.length / 2
        return rc.get_lp_priestley_2007(
            Ls, self.design.fsyl_q, self.design.dbl_int_q)

    def _get_my_phiy(
        self, axis: Literal['x', 'y']
    ) -> Tuple[float, float, float]:
        """Computes the yield moment and curvature of the column section for
        bending around `axis`.

        Parameters
        ----------
        axis : Literal['x', 'y']
            The local axis considered for the calculations.

        Returns
        -------
        My : float
            Yield moment.
        phi_y : float
            Yield curvature.
        cy : float
            Neutral axis depth at yield.

        See Also
        --------
        :meth:`_get_my_phiy_empirical` : Empirical expressions, used if
            ``yield_mom_curv='empirical'``.
        :meth:`_get_my_phiy_analytical` : Section analysis, used if
            ``yield_mom_curv='analytical'``.
        """
        if self.yield_mom_curv == 'analytical':
            return self._get_my_phiy_analytical(axis)
        return self._get_my_phiy_empirical(axis)

    def _get_tension_rebar(
        self, axis: Literal['x', 'y']
    ) -> Tuple[float, float]:
        """Gets the longitudinal reinforcement on a single side of the column
        section for bending around `axis`.

        Parameters
        ----------
        axis : Literal['x', 'y']
            The local axis considered for the calculations.

        Returns
        -------
        As_tens : float
            Area of the corner and internal reinforcement on a single side.
        dd : float
            Distance from the compression fiber to the centroid of the
            reinforcement on the tension side.
        """
        if axis == 'x':
            h = self.design.by  # Section height, along y
            nbl_int = self.design.nblx_int_q
        elif axis == 'y':
            h = self.design.bx  # Section height, along x
            nbl_int = self.design.nbly_int_q
        # Number of corner reinforcement (on a single side)
        nbl_cor = 2
        # Diameter of corner reinforcement
        dbl_cor = self.design.dbl_cor_q
        # Diameter of internal reinforcement
        dbl_int = self.design.dbl_int_q
        As_tens = (nbl_cor * ((0.25 * np.pi) * dbl_cor**2)
                   + nbl_int * ((0.25 * np.pi) * dbl_int**2))
        dd = (h - self.design.cover_q - self.design.dbh_q - 0.5 * dbl_cor)
        return As_tens, dd

    def _get_my_phiy_empirical(
        self, axis: Literal['x', 'y']
    ) -> Tuple[float, float, float]:
        """Computes the yield moment and curvature of the column section for
        bending around `axis` with the empirical expressions of
        Panagiotakos and Fardis (2001).

        Parameters
        ----------
        axis : Literal['x', 'y']
            The local axis considered for the calculations.

        Returns
        -------
        My : float
            Yield moment.
        phi_y : float
            Yield curvature.
        cy : float
            Neutral axis depth at yield.

        See Also
        --------
        :func:`~simdesign.utils.rcsection.get_my_phiy_panagiotakos_fardis2001`

        References
        ----------
        Panagiotakos, T. B., & Fardis, M. N. (2001).
        Deformations of reinforced concrete members at yielding and ultimate.
        Structural Journal, 98(2), 135-148.
        """
        if axis == 'x':
            # Section height
            h = self.design.by  # along y
            # Section width
            b = self.design.bx  # along x
            # Number of internal web reinforcement (intermediate)
            nbl_v = self.design.nbly_int_q
        elif axis == 'y':
            # Section height
            h = self.design.bx  # along x
            # Section width
            b = self.design.by  # along y
            # Number of internal web reinforcement (intermediate)
            nbl_v = self.design.nblx_int_q
        # Diameter of internal reinforcement
        dbl_int = self.design.dbl_int_q
        # Tension and compression reinforcement (equal on both sides), and
        # distance from the compression fiber to the tension rebars
        As_tens, dd = self._get_tension_rebar(axis)
        As_comp = As_tens
        # Web reinforcement (intermediate)
        As_int = 2 * nbl_v * (0.25 * np.pi * dbl_int**2)
        # Compressive axial load (+)
        Nu = max(-self.axial_force, 0)

        return rc.get_my_phiy_panagiotakos_fardis2001(
            h=h, b=b, fc=self.design.fc_q, Ec=self.Ecm_q,
            Es=self.design.Es, fsyl=self.design.fsyl_q,
            As_tens=As_tens, As_comp=As_comp, dd=dd, As_int=As_int, Nu=Nu)

    def _get_my_phiy_analytical(self, axis: Literal['x', 'y']
                                ) -> Tuple[float, float, float]:
        """Computes the yield moment and curvature of the column section for
        bending around `axis` by the simplified section analysis.

        Parameters
        ----------
        axis : Literal['x', 'y']
            The local axis considered for the calculations.

        Returns
        -------
        My : float
            Yield moment.
        phi_y : float
            Yield curvature.
        cy : float
            Neutral axis depth at yield.

        See Also
        --------
        :func:`~simdesign.utils.rcsection.do_simplified_section_analysis`
        """
        if axis == 'x':
            # Section height
            h = self.design.by  # along y
            # Section width
            b = self.design.bx  # along x
            # Number of internal web reinforcement (intermediate)
            nbl_v = np.array(self.design.nbly_int_q, dtype=int)
            # Number of internal reinforcement (on a single side)
            nbl_int = np.array(self.design.nblx_int_q, dtype=int)
        elif axis == 'y':
            # Section height
            h = self.design.bx  # along x
            # Section width
            b = self.design.by  # along y
            # Number of internal web reinforcement (intermediate)
            nbl_v = np.array(self.design.nblx_int_q, dtype=int)
            # Number of internal reinforcement (on a single side)
            nbl_int = np.array(self.design.nbly_int_q, dtype=int)
        # Number of corner reinforcement (on a single side)
        nbl_cor = 2
        # Diameter of corner reinforcement
        dbl_cor = self.design.dbl_cor_q
        # Diameter of internal reinforcement
        dbl_int = self.design.dbl_int_q
        # Concrete compressive strength in base units
        fc = self.design.fc_q
        # Longitudinal steel yield strength in base units
        fsyl = self.design.fsyl_q
        # Concrete cover
        cover = self.design.cover_q
        # Horizontal (stirrup) reinforcement diameter
        dbh = self.design.dbh_q
        # Compressive axial load (+)
        Nu = max(-self.axial_force, 0)
        # Concrete modulus of elasticity
        Ec = self.Ecm_q
        # Steel modulus of elasticity
        Es = self.design.Es

        # Reinforcement layout (top to bottom)
        y_ct = cover + dbh + dbl_cor / 2
        y_it = cover + dbh + dbl_int / 2
        y_cb = h - (cover + dbh + dbl_cor / 2)
        y_ib = h - (cover + dbh + dbl_int / 2)
        dv = (y_cb - y_ct) / (nbl_v + 1)
        y_layers = [y_it, y_ct] + [y_ct + (i + 1) * dv for i in range(nbl_v)
                                   ] + [y_cb, y_ib]
        # Reinforcement area per layer (top to bottom)
        Ab_c = 0.25*np.pi*dbl_cor**2
        Ab_i = 0.25*np.pi*dbl_int**2
        As_c = nbl_cor * Ab_c
        As_i = nbl_int * Ab_i
        As_web = 2 * Ab_i  # on both sides
        As_layers = [As_i, As_c] + [As_web for _ in range(nbl_v)
                                    ] + [As_c, As_i]
        # Cracking and yield moments
        _, _, _, My, phi_y, cy = rc.do_simplified_section_analysis(
            h=h, b=b, fc=fc, Ec=Ec,
            Pext=Nu, fyL=fsyl, Es=Es,
            As_layers=As_layers,
            y_layers=y_layers,
        )

        return My, phi_y, cy

    def _set_cracked_properties(self) -> None:
        """Computes and stores the cracked-section (effective) flexural
        properties of the column about the local x and y axes.

        The effective second moment of area is always computed, regardless
        of ``cracked``, as ``Ieff = EIeff / Ec`` with ``EIeff = My / phi_y``
        from the yield moment and curvature of the plastic hinges (see
        ``_get_my_phiy``). If ``cracked`` is a float, it is instead the ratio
        of effective to gross stiffness times the gross moment of inertia.
        The elastic sections use ``Ieff`` only if ``cracked`` is True or a
        float; if it is None or False, the gross section is used.

        The results are stored on the object for later use:

        - ``self._Ix_eff`` and ``self._cy`` (bending around local x), and
        - ``self._Iy_eff`` and ``self._cx`` (bending around local y),

        where ``_cy`` and ``_cx`` are the neutral axis depths at yield used
        by the shear hinges.

        See Also
        --------
        :meth:`_get_my_phiy` : Yield point of the plastic hinges.

        References
        ----------
        Panagiotakos, T. B., & Fardis, M. N. (2001).
        Deformations of reinforced concrete members at yielding and ultimate.
        Structural Journal, 98(2), 135-148.

        Priestley, M. J. N., Calvi, G. M., & Kowalsky, M. J. (2007).
        *Displacement-based seismic design of structures*. IUSS Press.
        """
        for axis in ['x', 'y']:
            My, phiy, cy = self._get_my_phiy(axis)
            Ieff = (My / phiy) / self.Ecm_q

            if isinstance(self.cracked, float):
                # User-defined ratio of effective to gross flexural stiffness
                Ig = self.design.Ix if axis == 'x' else self.design.Iy
                Ieff = self.cracked * Ig

            # Save also the neutral axis depth for shear hinge calculations
            if axis == 'x':
                self._Ix_eff = Ieff
                self._cy = cy
            elif axis == 'y':
                self._Iy_eff = Ieff
                self._cx = cy
