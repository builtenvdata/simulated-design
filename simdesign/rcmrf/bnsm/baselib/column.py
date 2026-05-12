"""This module provides a base class for representing columns
within the BNSM layer and for building and exporting their OpenSees
representations.
"""
# Imports from installed packages
from abc import ABC
import numpy as np
import openseespy.opensees as ops
from typing import Dict, Literal, List, Tuple

# Imports from bnsm library
from .node import Node
from .constants import RIGID_MAT

# Imports from bdim base library
from ...bdim.baselib.column import ColumnBase as ColumnDesign

# Imports from utils library
from ....utils.units import MPa, mm
from ....utils.misc import PRECISION, round_list
from ....utils.rcsection import get_moments


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
    use of cracked-section (effective) stiffness properties derived from
    moment-curvature analysis.

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
    cracked_section : bool
        If True, the elastic sections uses cracked-section
        (effective) flexural properties. If False, gross-section
        properties are used.
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
    cracked_section: bool
    cyclic_model: bool
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
        return int(str(self.design.line.tag) + '991')

    @property
    def my_mat_tag(self) -> int:
        """Uniaxial material tag for the flexural hinge about local-y (My)."""
        return int(str(self.design.line.tag) + '993')

    @property
    def vy_mat_tag_(self) -> int:
        """Pinching4 material tag for the shear hinge in local-y (Vy)."""
        return int(str(self.design.line.tag) + '994')

    @property
    def vy_mat_tag(self) -> int:
        """MinMax material tag for the shear hinge in local-y (Vy)."""
        return int(str(self.design.line.tag) + '995')

    @property
    def vz_mat_tag_(self) -> int:
        """Pinching4 material tag for the shear hinge in local-z (Vz)."""
        return int(str(self.design.line.tag) + '996')

    @property
    def vz_mat_tag(self) -> int:
        """MinMax material tag for the shear hinge in local-z (Vz)."""
        return int(str(self.design.line.tag) + '997')

    @property
    def elastic_sec_tag(self) -> int:
        """Section tag for the elastic (interior) section."""
        return int(str(self.design.line.tag) + '990')

    @property
    def inelastic_sec_tag(self) -> int:
        """Section tag for the inelastic aggregated section."""
        return int(str(self.design.line.tag) + '992')

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
        cyclic_model: bool = False, cracked_section: bool = False
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
        cracked_section : bool, optional
            If True, the elastic sections uses cracked-section
            (effective) flexural properties. If False, gross-section
            properties are used. By default False.
        """
        self.design = design
        self.bondslip_factor = bondslip_factor
        self.capacity_design = capacity_design
        self.cyclic_model = cyclic_model
        self.cracked_section = cracked_section
        self.axial_force = -(load_factors['G'] * design.hinge_Ng
                             + load_factors['Q'] * design.hinge_Nq)
        self.ele_load = float(design.self_wg * load_factors['G'])
        self.jnt_offsets = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        # Set cracked section properties
        self._set_cracked_section_properties('x')
        self._set_cracked_section_properties('y')

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
        if self.cracked_section:
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
        Lp = self._get_plastic_hinge_length()
        # Beam integration inputs
        int_inputs = [
            'HingeRadau', self.int_tag,
            self.inelastic_sec_tag, Lp, self.inelastic_sec_tag, Lp,
            self.elastic_sec_tag
        ]

        return int_inputs

    def _set_cracked_section_properties(self, axis: Literal['x', 'y']) -> None:
        """
        Compute and store cracked-section (effective) flexural properties
        about a local axis.

        This method builds a layered longitudinal-reinforcement layout from
        the section geometry and detailing stored in ``self.design``, then
        calls ``get_moments`` to obtain the yield moment ``My``, yield
        curvature ``phi_y``, and neutral axis depth at yield ``cy``. From
        these, it computes the effective flexural rigidity
        ``EIeff = My / phi_y`` and the corresponding effective second moment
        of area ``Ieff = EIeff / Ec``.

        The results are stored on the object for later use:
        - For ``axis='x'``: ``self._cy`` and ``self._Ix_eff``
        - For ``axis='y'``: ``self._cx`` and ``self._Iy_eff``

        Parameters
        ----------
        axis : Literal['x', 'y']
            Local bending axis for the calculations

        Returns
        -------
        None
            This method does not return values; it updates internal attributes
            with neutral-axis depth at yield and effective inertia.

        See Also
        --------
        get_moments : Computes cracking/yield moments and associated
            curvature/neutral-axis quantities for a layered RC section.

        References
        ----------
        Priestley, M. J. N., Calvi, G. M., & Kowalsky, M. J. (2007).
        *Displacement-based seismic design of structures*. IUSS Press.

        Collins, M. P., & Mitchell, D. (1997).
        *Prestressed concrete structures*. Prentice Hall.
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
        _, _, _, My, phi_y, cy = get_moments(
            h=h, b=b, fc=fc, Ec=Ec,
            Pext=Nu, fyL=fsyl, Es=Es,
            As_layers=As_layers,
            y_layers=y_layers,
        )

        # Save neutral axis depth for shear hinge calculations
        if axis == 'x':
            self._cy = cy
        elif axis == 'y':
            self._cx = cy

        # Save effective moment inertia for elastic section
        EIeff = My / phi_y
        Ieff = EIeff / Ec
        if axis == 'x':
            self._Ix_eff = Ieff
        elif axis == 'y':
            self._Iy_eff = Ieff

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
            # Transverse reinforcement ratio
            rhoh = self.rhoh_y_q_
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
            # Transverse reinforcement ratio
            rhoh = self.rhoh_x_q_
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
        fc_mpa = fc / MPa  # in MPa
        # Concrete elastic modulus
        Ec = self.Ecm_q
        # Concrete shear modulus
        Gc = self.Gcm_q
        # Transverse reinforcement yield strength
        fsyh = self.design.fsyh_q  # in base units
        fsyh_mpa = fsyh / MPa  # in MPa
        # Steel shear modulus
        Es = self.design.steel.Es
        # Diameter of internal reinforcement
        dbl_int = self.design.dbl_int_q
        # Longitudinal reinforcement ratio
        rhol = self.rhol_q
        # Longitudinal reinforcement area
        Asl = rhol * Ag
        # Average long. reinf. bar area
        nbl_int = 2 * (self.design.nbly_int_q + self.design.nblx_int_q)
        nbl_cor = 4
        dbl_ave = Asl / (nbl_int + nbl_cor)

        # Longitudinal reinforcement yield strength
        fsyl = self.design.fsyl_q  # in base units
        fsyl_mpa = fsyl / MPa  # in MPa
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
        # The volumetric ratio of transverse reinforcement
        rhoh = Av / (sbh * hc)
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

        # Onset of cracking terms
        Ae = 0.8 * Ag  # Effective shear area for rectangular columns
        GA0 = Gc * Ae  # Uncracked shear stiffness
        # Concrete tensile strength Collins & Mitchell (1997) - Eqn. 3-16
        fct = ((fc_mpa**0.5) / 3.0) * MPa  # (kN)
        # Cracking Shear as per Sezen & Moehle (2004) - Eqn. 11
        # Note: Only difference is fct, from Collins & Mitchell 1997.
        V1 = fct * d / Ls * np.sqrt(1 + P / (fct * Ag)) * Ae  # (kN)
        # Cracking shear strain per Zimos et al. (2015) - Fig. 7
        gamm_1 = V1 / GA0

        # Onset of maximum shear force attainment terms
        # Concrete component based on Priestley et al. (1994)
        k = 0.29  # Assuming low ductility based on Fig. 7
        Vc = k * ((fc_mpa**0.5) * MPa) * Ae  # Eqn. 27
        # Axial-load component based on Priestley et al. (1994)
        Vp = P * (h - c) / (2 * Ls)  # Eqn. 28
        # Truss-mechanism componentbased on Priestley et al. (1994)
        theta = 45.0  # Assumed based on observations from Zimos et al. 2015
        cot_th = 1 / np.tan(np.deg2rad(theta))
        Vs = (Av * fsyh * hc / sbh) * cot_th  # Eqn. 29
        # Maximum shear strength
        Vmax = Vc + Vp + Vs
        V2 = Vmax

        # NOTE: V1 cannot be greater than V2, this is a superficial adjustment.
        if V1 > V2:  # This may happen even though, rare!
            V1 = 0.8 * V2  # Assume V1 is 80% of V2
            gamm_1 = V1 / GA0  # Adjust gamm_1 accordingly

        # Cracked shear stiffness from Mergos and Kappos 2012
        # NOTE: Instead of d-d', the core diameter by Priestley is used.
        sin4_th = np.sin(np.deg2rad(theta))**4
        cot2_th = cot_th**2
        eta = Es / Ec  # Modular ratio
        GA1 = (Es * b * hc * rhoh * sin4_th * cot2_th  # Eqn. 7
               ) / (sin4_th + eta * rhoh)
        # Cracking strain from truss analogy
        gamma_truss = gamm_1 + (V2 - V1) / GA1
        # Corrections on cracking strain
        # NOTE: In Eqn.8, nu is clipped by 0.6 based on Table 1
        kappa = 1 - 1.07 * min(nu, 0.6)  # Eqn. 8
        lambda_ = 5.37 - 1.59 * min(Ls / h, 2.5)  # Eqn. 9
        gamm_2 = kappa * lambda_ * gamma_truss  # Eqn. 10

        # Onset shear failure terms from Mergos and Kappos 2012
        V3 = Vmax
        omega_k = rhoh * fsyh / fc  # Eqn. 11.5
        lambda_1 = 1 - 2.5 * min(nu, 0.4)  # Eqn. 11.2
        lambda_2 = min(Ls / h, 2.5)**2  # Eqn. 11.3
        lambda_3 = 0.31 + 17.8 * min(omega_k, 0.08)  # Eqn. 11.4
        gamm_3 = max(lambda_1 * lambda_2 * lambda_3, 1) * gamm_2  # Eqn. 11.1

        # NOTE: Followings are superficial adjustments for numerical purposes
        if gamm_3 > gamm_2:  # 2nd and 3rd points are not the same
            # OpenSees may complain due to zero shear stiffness
            V2 = 0.9 * V2  # To avoid 0 stiffness between 2nd & 3rd points
        elif gamm_3 == gamm_2:  # 2nd and 3rd points are the same
            gamm_2 = gamm_2 - 0.1 * (gamm_2 - gamm_1)
            V2 = V2 - 0.1 * (V2 - V1)

        # Onset of axial failure terms based on Zimos et al. 2015
        nu_l = P / (Asl * fsyl)
        tau_ave_max = Vmax / (b * d) / MPa  # in MPa
        Ac = hc * bc  # confined concrete area
        aconf = Ac / Ag  # ratio of confined to gross concrete area
        # Total post-peak shear strain - Eqn. 7
        gamm_tpp = max(
            (0.65 * (rhol / aconf) ** 1.2)
            / (
                (
                    (rhoh * fsyh_mpa)
                    / (nu_l * (sbh / d) * (tau_ave_max / (fc_mpa**0.5)))
                )
                ** 0.5
            ),
            0
        )
        # Descending branch slope - Eqn. 4
        Spp = 7.36 + (0.28 * (nu + 0.02) ** 0.5) / (
            (rhoh + 0.0011)
            * ((fsyl_mpa * rhol / aconf) * (dbl_ave / d) + 0.06)
        )
        # Residual shear force - Eqn. 3
        V4 = V3 * (1 - Spp * gamm_tpp)
        if V4 <= 0:
            V4 = 0.1 * V3
            gamm_tpp = 1 / Spp
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
        rot_mat_inputs : List[float]
            Hysteretic material model inputs for the plastic hinge describing
            behaviour in flexure around `axis`.
        """
        if axis == 'x':
            # The integer tag for the material describing flexure behaviour
            # around local -x (corresponds to z in ops)
            flex_mat_tag = self.mz_mat_tag

        elif axis == 'y':
            # The integer tag for the material describing flexure behaviour
            # around local -y axis (corresponds to y in ops)
            flex_mat_tag = self.my_mat_tag

        # Plastic hinge properties
        (
            phi_y, My, Mc, Mr, theta_y, theta_cap_pl, theta_pc,
            pinchx, pinchy, damage1, damage2, beta
         ) = self._get_rot_hinge_props(axis)

        # Rotation values for monotonic loading
        theta_1 = theta_y
        theta_2 = theta_y + theta_cap_pl
        theta_3 = theta_y + theta_cap_pl + theta_pc

        # Curvature values for monotonic loading
        Lp = self._get_plastic_hinge_length()
        phi_1 = phi_y
        phi_2 = (theta_2 - theta_1) / Lp + phi_1
        phi_3 = (theta_3 - theta_1) / Lp + phi_1

        # Material inputs
        rot_mat_inputs = [
            'Hysteretic', flex_mat_tag,
            My, phi_1, Mc, phi_2, Mr, phi_3,
            -My, -phi_1, -Mc, -phi_2, -Mr, -phi_3,
            pinchx, pinchy, damage1, damage2, beta
        ]

        # Rounding to precision
        rot_mat_inputs = round_list(rot_mat_inputs)

        return rot_mat_inputs

    def _get_plastic_hinge_length(self) -> float:

        """Computes plastic hinge length for the sections.

        Returns
        -------
        Lp : float
            Plastic hinge lengths for the beam sections.

        References
        ----------
        Priestley, M. J. N., Calvi, G. M., & Kowalsky, M. J. (2007).
        *Displacement-based seismic design of structures*. IUSS Press.
        """
        # Longitudinal steel yield strength in base units
        fsyl = self.design.fsyl_q / MPa  # in MPa
        # Shear span, assuming equal to 50% of the free length of the element
        Ls = self.design.line.length / 2 / mm  # in mm
        # Diameter of internal reinforcement
        dbl_int = self.design.dbl_int_q / mm  # in mm
        # Longitudinal steel yield strength in base units
        fsyl = self.design.fsyl_q / MPa  # in MPa
        # Plastic hinge length based on Priestley et al. 2007
        Lp = round(0.08 * Ls + 0.022 * fsyl * dbl_int, PRECISION) * mm

        return Lp

    def _get_rot_hinge_props(self, axis: Literal['x', 'y']) -> List[float]:
        """Compute backbone and cyclic degradation parameters defining the
        behaviour of the rotational plastic hinge about specified local axis.

        Parameters
        ----------
        axis : Literal['x', 'y']
            Local bending axis considered for the calculations.

        Returns
        -------
        props : list of float
            Ordered list of hinge properties for the specified axis:

            0. ``phi_y`` Yield curvature.
            1. ``My`` Yield moment.
            2. ``Mc`` Capping moment.
            3. ``Mr`` Residual moment.
            4. ``theta_y`` Yield rotation.
            5. ``theta_cap_pl`` Plastic rotation capacity.
            6. ``theta_pc`` Post-capping rotation capacity.
            7. ``pinchx`` Pinching factor for deformation.
            8. ``pinchy`` Pinching factor for force.
            9. ``damage1`` Ductility-based damage.
            10. ``damage2`` Energy-based damage.
            11. ``beta`` Unloading stiffness degradation exponent.

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

        ACI CODE 318-25. (2025). Building Code for Structural Concrete-Code
        Requirements and Commentary. American Concrete Institute.
        """
        if axis == 'x':
            # Section height
            h = self.design.by  # along y
            # Section width
            b = self.design.bx  # along x
            # Number of internal web reinforcement (intermediate)
            nbl_v = self.design.nbly_int_q
            # Number of internal reinforcement (on a single side)
            nbl_int = self.design.nblx_int_q
            # Transverse reinforcement ratio
            rhoh = self.rhoh_y_q  # Stirrups are along -y axis

        elif axis == 'y':
            # Section height
            h = self.design.bx  # along x
            # Section width
            b = self.design.by  # along y
            # Number of internal web reinforcement (intermediate)
            nbl_v = self.design.nblx_int_q
            # Number of internal reinforcement (on a single side)
            nbl_int = self.design.nbly_int_q
            # Transverse reinforcement ratio
            rhoh = self.rhoh_x_q  # Stirrups are along -x axis

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
        # Concrete compressive strength in MPa
        fc_mpa = self.design.fc_q / MPa  # convert to MPa
        # Longitudinal steel yield strength in MPa
        fsyl_mpa = self.design.fsyl_q / MPa  # convert to MPa
        # Nominal length of column
        Ln = self.design.H
        # Stirrup spacing
        sbh = self.design.sbh_q
        # Longitudinal reinforcement ratio
        rhol = self.rhol_q
        # Concrete crushing strain used for computing section capacity
        eps_cu = 0.0035
        # Compressive axial load (+)
        Nu = max(-self.axial_force, 0)

        """PART 1: YIELD MOMENT AND CURVATURE CALCULATIONS
        MAIN REFERENCE: Panagiotakos and Fardis (2001)
        """
        # Stress-block coefficient used to compute section capacity
        # Table 22.2.2.4.3 of ACI 318-25
        if fc < 27.6 * MPa:
            betac = 0.85
        elif fc > 55.17 * MPa:
            betac = 0.65
        else:
            betac = 1.05 - 0.05 * fc_mpa / 6.9
        # Concrete modulus of elasticity
        Ec = self.Ecm_q
        # Steel modulus of elasticity
        Es = self.design.Es
        # Modular ratio
        nyoung = Es / Ec
        # Yield strain of steel bars
        esy = fsyl / Es
        # Distance from top fiber to bottom rebars
        dd = h - cover - dbh - 0.5 * dbl_cor
        # Distance from top fiber to top rebars
        dd_prime = h - dd
        # Balanced  value of c: distance to neutral axis from top fiber
        cb = (eps_cu * dd) / (eps_cu + esy)  # from compatibility
        # Tension and compression reinforcement
        As_tens = (nbl_cor * ((0.25 * np.pi) * dbl_cor**2)
                   + nbl_int * ((0.25 * np.pi) * dbl_int**2))
        rhol_tens = As_tens / (b * dd)
        As_comp = (nbl_cor * ((0.25 * np.pi) * dbl_cor**2)
                   + nbl_int * ((0.25 * np.pi) * dbl_int**2))
        rhol_comp = As_comp / (b * dd)
        # Web reinforcement (intermediate)
        As_int = 2 * nbl_v * (0.25 * np.pi * dbl_int**2)
        rhol_int = As_int / (b * dd)
        # Compute distance to neutral axis with outer faces (simplification)
        c = (As_tens * fsyl - As_comp * fsyl + Nu) / (
            0.85 * fc * b * betac)
        # Decide whether yielding is controlled by tension or compression zone
        if c < cb:  # Yielding is controlled by the tension steel
            # Panagiotakos and Fardis 2001 - Equation 4
            A_to_use = (
                rhol_tens + rhol_comp + rhol_int + (Nu / (b * dd * fsyl))
            )
            B_to_use = (
                rhol_tens
                + rhol_comp * (dd_prime / dd)
                + 0.5 * rhol_int * (1 + (dd_prime / dd))
                + (Nu / (b * dd * fsyl))
            )
            control = 1
        else:  # Yielding is controlled by the compression zone
            # Panagiotakos and Fardis 2001 - Equation 5
            A_to_use = (
                rhol_tens
                + rhol_comp
                + rhol_int
                - (Nu / (1.8 * nyoung * b * dd * fc))
            )
            B_to_use = (
                rhol_tens
                + rhol_comp * (dd_prime / dd)
                + 0.5 * rhol_int * (1 + (dd_prime / dd))
            )
            control = 0
        # The compression zone depth: Panagiotakos and Fardis 2001 - Equation 3
        ky = (
            (nyoung**2) * (A_to_use**2) + (2 * nyoung * B_to_use)
        ) ** 0.5 - nyoung * A_to_use
        # Yield curvature
        if control == 1:
            # Panagiotakos and Fardis 2001 - Equation 1
            phi_y = fsyl / (Es * (1 - ky) * dd)
        else:
            # Panagiotakos and Fardis 2001 - Equation 2
            phi_y = (1.8 * fc) / (Ec * ky * dd)
        # Yield Moment: Panagiotakos and Fardis 2001 - Equation 6
        term1 = (Ec * (ky**2) / 2) * (
            0.5 * (1 + (dd_prime / dd)) - (ky / 3))
        term2 = (
            (Es / 2)
            * (
                (1 - ky) * rhol_tens
                + (ky - (dd_prime / dd)) * rhol_comp
                + (rhol_int / 6) * (1 - (dd_prime / dd))
            )
            * (1 - (dd_prime / dd))
        )
        My = (b * (dd**3)) * phi_y * (term1 + term2)

        """PART 2: PLASTIC HINGE PROPERTY CALCULATIONS
        MAIN REFERENCE: Haselton et al. (2016)
        """
        # Shear span, assuming equal to 50% of the free length of the element
        Ls = Ln / 2  # NOTE: Could be varied with intensity of loading, but ok.
        # Shear cracking is expected to precede flexural yield EC8-3 pp 41
        av = 1.0
        # Axial load ratio
        niu = Nu / (self.design.Ag * fc)
        # Unit conversion coefficient 1.0 for MPa, 6.9 for ksi (Haselton 2016)
        c_u = 1.0
        # Reinforcing bar buckling coefficient, by Dhakal and Maekawa 2002
        sn = (sbh / dbl_cor) * (fsyl_mpa / 100) ** 0.5
        # Effective depth: dist. between outer comp. fiber and tens. steel
        d = 0.9 * h
        # Level arm: dist. between comp. and tens. forces
        z = 0.9 * d

        # Post-yield hardening stiffness - Haselton et al. 2008 - Equation 3.17
        Mc_My = 1.25 * (0.89**niu) * (0.91 ** (0.01 * fc_mpa))
        #  Residual strength to capping strength ratio - assumed
        Mr_Mc = 0.1  # 10%
        # Maximum moment capacity
        Mc = Mc_My * My
        # Residual moment capacity
        Mr = Mr_Mc * Mc

        # Plastic Rotation capacity by Haselton et al. 2016 - Equation 5
        theta_cap_pl = (
            0.12
            * (1 + 0.55 * self.bondslip_factor)
            * (0.16**niu)
            * ((0.02 + 40 * rhoh) ** 0.43)
            * (0.54 ** (0.01 * c_u * fc_mpa))
            * (0.66 ** (0.1 * sn))
            * (2.27 ** (10.0 * rhol))
        )
        # Post-capping rotation capacity by Haselton et al. 2016 - Equation 8
        theta_pc = min(
            0.10, 0.76 * (0.031**niu) * ((0.02 + 40 * rhoh) ** 1.02)
        )
        # Yield rotation capacity - EN 1998-3:2004 - Equation A.10b
        theta_y1 = phi_y * ((Ls + (av * z)) / 3)
        theta_y2 = 0.0014 * (1 + 1.5 * h / Ls)
        theta_y3 = 0.125 * phi_y * dbl_cor * (fsyl_mpa / (fc_mpa**0.50))
        theta_y = theta_y1 + theta_y2 + (self.bondslip_factor * theta_y3)

        # Rotation values needs to be adjusted for cyclic loading
        if self.cyclic_model:  # Haselton et al. 2016
            theta_cap_pl = 0.7 * theta_cap_pl  # Equation (12)
            theta_pc = 0.5 * theta_pc  # Equation (13)

        # Pinching factor for strain (or deformation) during reloading
        pinchx = 1.0  # no pinching (default)
        # Pinching factor for stress (or force) during reloading
        pinchy = 1.0  # no pinching (default)
        # Damage due to ductility: D1(mu-1)
        damage1 = 0.0  # no degradation (default)
        # Damage due to energy: D2(Eii/Eult)
        damage2 = 0.0  # no degradation (default)
        # Power used to determine the degraded unloading stiffness based on
        # ductility, mu-beta (optional, default=0.0)
        beta = 0.0  # elastic unloading (default)

        # Save to list
        props = [
            float(phi_y), float(My), float(Mc), float(Mr),
            float(theta_y), float(theta_cap_pl), float(theta_pc),
            pinchx, pinchy, damage1, damage2, beta,
        ]

        return props
