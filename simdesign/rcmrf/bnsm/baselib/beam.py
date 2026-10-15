"""This module provides a base class for representing beams
within the BNSM layer and for building and exporting their OpenSees
representations.
"""
# Imports from installed packages
from abc import ABC
import numpy as np
import openseespy.opensees as ops
from typing import List, Literal, Dict, Tuple, Optional

# Imports from bnsm library
from .node import Node
from .constants import RIGID_MAT

# Imports from bdim base library
from ...bdim.baselib.beam import BeamBase as BeamDesign
from ...bdim.baselib.beam import Array3

# Imports from utils library
from ....utils.units import MPa
from ....utils.misc import PRECISION, round_list
from ....utils import rcsection as rc
from ....utils.tags import sub_tag


PINCHX = 0.8
"""Pinching factor for strain (or deformation) during reloading"""
PINCHY = 0.2
"""Pinching factor for stress (or force) during reloading"""
DAMAGE1 = 0.0  # no degradation (default)
"""Damage due to ductility: D1(mu-1)"""
DAMAGE2 = 0.0  # no degradation (default)
"""Damage due to energy: D2(Eii/Eult)"""
BETA = 0.85  # from Dolšek and Fajfar 2005
"""Power used to determine the degraded unloading stiffness based on
ductility, mu-beta (optional, default=0.0)"""
HYSTERETIC_PARAMETERS = [PINCHX, PINCHY, DAMAGE1, DAMAGE2, BETA]
"""Hysteretic parameters"""


class BeamBase(ABC):
    """Abstract Base Class for beam implementations in BNSM layer.

    This class defines the common interface and core behaviour required to:
    (1) define a beam member in the OpenSees domain, and
    (2) export equivalent Python and Tcl commands.

    The member is modelled using a force-based beam-column element
    (``forceBeamColumn``) with a plastic-hinge integration scheme
    (e.g., ``HingeRadau``). Nonlinear behaviour is concentrated within
    finite hinge lengths at the element ends.

    Hinge behaviour is defined through phenomenological moment-rotation
    relationships implemented using uniaxial materials and section
    aggregators. The interior region is represented by an elastic section,
    with optional use of cracked-section (effective) stiffness properties.

    A bond-slip modification factor is applied when determining hinge
    properties (i.e., rotation capacities). Uniformly distributed
    gravity loads are assigned to the beam element.

    Many section-level quantities are stored as ``Array3`` values,
    corresponding to the (i, mid, j) sections.

    Attributes
    ----------
    design : ~simdesign.rcmrf.bdim.baselib.beam.BeamBase
        Instance of beam design information model.
    bondslip_factor : float
        Bondslip factor.
    ele_node_i : Node
        Element node at the start of beam.
    ele_node_j : Node
        Element node at the end of beam.
    ele_load : float
        Uniformly distributed gravity load along the beam.
    load_type : Literal['uniform', 'point']
        How the gravity load is applied: 'uniform' as a uniformly distributed
        element load, 'point' as equivalent point loads at the element ends
        (as in O'Reilly and Sullivan, 2019).
    jnt_offsets : List[float]
        Rigid joint offset values (dx_i, dy_i, dz_i, dx_j, dy_j, dz_j),
        specified with respect to the global coordinate system.
    cracked : None | bool | float
        Cracked-section (effective) flexural properties of the elastic
        sections: True for ``EIeff = My / phi_y`` with the yield moment and
        curvature of the plastic hinges computed with the empirical or
        analytical approach (see `yield_mom_curv`), or a float as the ratio
        of effective to gross flexural stiffness. If None or False,
        gross-section properties are used.
        The class attribute is the method used for the BNSM option
        ``'auto'`` (see the model classes).
    yield_mom_curv : Literal['empirical', 'analytical']
        Method to compute yield moment and curvature of the plastic hinges:
        ``'empirical'`` (Panagiotakos and Fardis, 2001) or
        ``'analytical'`` (simplified section analysis).
    cyclic_model : bool
        If True, the model parameters will be adjusted for cyclic analysis.
    _Iz_eff : float
        Effective beam moment of inertia around local-z.

    Notes
    -----
    Section view of beams along X direction:

    .. code-block:: text

        Z (3)
        |__Y (2)
            --------------    ----
            |     y      |    |
            |     |      |    |
            |  z--+      |    h
            |            |    |
            |            |    |
            --------------    ----
            |---- b -----|

        Vectors defining the local axes in Global Coordinate System:
            vx = np.array([1.0, 0.0, 0.0])
            vy = np.array([0.0, 0.0, 1.0])
            vz = np.array([0.0, -1.0, 0.0])
            vecxz = np.array([0.0, -1.0, 0.0])
        Compatibility check:
            np.allclose(vy, np.cross(vecxz, vx))
            np.allclose(vz, np.cross(vx,vy))

    Section view of beams along Y direction:

    .. code-block:: text

        Z (3)
        |__X (1)
            --------------    ----
            |     y      |    |
            |     |      |    |
            |     +--z   |    h
            |            |    |
            |            |    |
            --------------    ----
            |---- b -----|

        Vectors defining the local axes in Global Coordinate System:
            vx = np.array([0.0, 1.0, 0.0])
            vy = np.array([0.0, 0.0, 1.0])
            vz = np.array([1.0, 0.0, 0.0])
            vecxz = np.array([1.0, 0.0, 0.0])
        Compatibility check:
            np.allclose(vy, np.cross(vecxz, vx))
            np.allclose(vz, np.cross(vx,vy))
    """
    design: BeamDesign
    bondslip_factor: float
    ele_node_i: Node
    ele_node_j: Node
    ele_load: float
    load_type: Literal['uniform', 'point']
    jnt_offsets: List[float]
    cracked: Optional[bool | float] = None
    yield_mom_curv: Literal['empirical', 'analytical']
    cyclic_model: bool
    _Iz_eff: float

    @property
    def ele_tag(self) -> int:
        """
        Returns
        -------
        int
            Tag of beam-column element representing the beam.
        """
        return self.design.line.tag

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
    def rhoh_z_q(self) -> Array3[np.float64]:
        """
        Returns
        -------
        Array3[np.float64]
            In situ (quality adjusted) transverse reinforcement ratio in
            local-z.
        """
        Ash = self.design.nbh_b_q * np.pi * self.design.dbh_q**2 / 4
        return Ash / (self.design.h * self.design.sbh_q)

    @property
    def rhoh_y_q(self) -> Array3[np.float64]:
        """
        Returns
        -------
        Array3[np.float64]
            In situ (quality adjusted) transverse reinforcement ratio in
            local-y.
        """
        Ash = self.design.nbh_h_q * np.pi * self.design.dbh_q**2 / 4
        return Ash / (self.design.b * self.design.sbh_q)

    @property
    def rhol_top_q(self) -> Array3[np.float64]:
        """
        Returns
        -------
        Array3[np.float64]
            In situ (quality adjusted) top longitudinal reinforcement ratio.
        """
        Acor = self.design.nbl_t1_q * (np.pi * self.design.dbl_t1_q**2 / 4)
        Aint = self.design.nbl_t2_q * (np.pi * self.design.dbl_t2_q**2 / 4)

        return (Acor + Aint) / self.design.Ag

    @property
    def rhol_bot_q(self) -> Array3[np.float64]:
        """
        Returns
        -------
        Array3[np.float64]
            In situ (quality adjusted) bottom longitudinal reinforcement ratio.
        """
        Acor = self.design.nbl_b1_q * (np.pi * self.design.dbl_b1_q**2 / 4)
        Aint = self.design.nbl_b2_q * (np.pi * self.design.dbl_b2_q**2 / 4)

        return (Acor + Aint) / self.design.Ag

    @property
    def rhol_q(self) -> Array3[np.float64]:
        """
        Returns
        -------
        Array3[np.float64]
            In situ (quality adjusted) total longitudinal reinforcement ratio.
        """
        return self.rhol_top_q + self.rhol_bot_q

    @property
    def rhoh_z_q_(self) -> Array3[np.float64]:
        """
        Returns
        -------
        Array3[np.float64]
            In situ (quality adjusted) transverse reinforcement ratio in
            local-z. Computed using confined concrete dimensions.
        """
        # Total transverse reinforcement area
        Av = self.design.nbh_b_q * (np.pi * self.design.dbh_q**2) / 4
        # Transverse reinforcement spacing
        s = self.design.sbh_q
        # Core diameter
        dc = self.design.h - 2 * (self.design.cover_q + self.design.dbh_q / 2)
        return Av / (s * dc)

    @property
    def rhoh_y_q_(self) -> Array3[np.float64]:
        """
        Returns
        -------
        Array3[np.float64]
            In situ (quality adjusted) transverse reinforcement ratio in
            local-y. Computed using confined concrete dimensions.
        """
        # Total transverse reinforcement area
        Av = self.design.nbh_h_q * (np.pi * self.design.dbh_q**2) / 4
        # Transverse reinforcement spacing
        s = self.design.sbh_q
        # Core diameter
        dc = self.design.b - 2 * (self.design.cover_q + self.design.dbh_q / 2)
        return Av / (s * dc)

    @property
    def rhol_top_q_(self) -> Array3[np.float64]:
        """
        Returns
        -------
        Array3[np.float64]
            In situ (quality adjusted) top longitudinal reinforcement ratio.
            Computed using confined concrete dimensions.
        """
        Acor = self.design.nbl_t1_q * (np.pi * self.design.dbl_t1_q**2 / 4)
        Aint = self.design.nbl_t2_q * (np.pi * self.design.dbl_t2_q**2 / 4)
        bc = self.design.b - 2 * (self.design.cover_q + self.design.dbh_q / 2)
        hc = self.design.h - 2 * (self.design.cover_q + self.design.dbh_q / 2)

        return (Acor + Aint) / (hc * bc)

    @property
    def rhol_bot_q_(self) -> Array3[np.float64]:
        """
        Returns
        -------
        Array3[np.float64]
            In situ (quality adjusted) bottom longitudinal reinforcement ratio.
            Computed using confined concrete dimensions.
        """
        Acor = self.design.nbl_b1_q * (np.pi * self.design.dbl_b1_q**2 / 4)
        Aint = self.design.nbl_b2_q * (np.pi * self.design.dbl_b2_q**2 / 4)
        bc = self.design.b - 2 * (self.design.cover_q + self.design.dbh_q / 2)
        hc = self.design.h - 2 * (self.design.cover_q + self.design.dbh_q / 2)

        return (Acor + Aint) / (hc * bc)

    @property
    def rhol_q_(self) -> Array3[np.float64]:
        """
        Returns
        -------
        Array3[np.float64]
            In situ (quality adjusted) total longitudinal reinforcement ratio.
            Computed using confined concrete dimensions.
        """
        return self.rhol_top_q_ + self.rhol_bot_q_

    @property
    def vecxz(self) -> List[float]:
        """Local x-z plane vector in global coordinates for OpenSees
        geometric transformation.

        Returns
        -------
        List[float]
            (X, Y, Z) components of ``vecxz`` used by ``ops.geomTransf`` to
            define the local element axes.

        Notes
        -----
        - For beams along global X (1): [0, -1, 0]
        - For beams along global Y (2): [1, 0, 0]
        """
        if self.design.direction == 'x':
            return [0, -1, 0]
        elif self.design.direction == 'y':
            return [1, 0, 0]

    @property
    def mz_i_mat_tag(self) -> int:
        """Material tag for the *i-end* flexural hinge about local-z (Mz)."""
        return sub_tag(self.design.line.tag, 90)

    @property
    def mz_j_mat_tag(self) -> int:
        """Material tag for the *j-end* flexural hinge about local-z (Mz)."""
        return sub_tag(self.design.line.tag, 91)

    @property
    def p_mat_tag(self) -> int:
        """Elastic material tag for the axial response (P) of the hinges."""
        return sub_tag(self.design.line.tag, 94)

    @property
    def my_mat_tag(self) -> int:
        """Elastic material tag for the flexural response about local-y (My)
        of the hinges."""
        return sub_tag(self.design.line.tag, 95)

    @property
    def t_mat_tag(self) -> int:
        """Elastic material tag for the torsional response (T) of the
        hinges."""
        return sub_tag(self.design.line.tag, 96)

    @property
    def elastic_sec_tag(self) -> int:
        """Section tag for the elastic (interior) section."""
        return sub_tag(self.design.line.tag, 90)

    @property
    def inelastic_sec_i_tag(self) -> int:
        """Section tag for the inelastic (hinge) section at i-end."""
        return sub_tag(self.design.line.tag, 91)

    @property
    def inelastic_sec_j_tag(self) -> int:
        """Section tag for the inelastic (hinge) section at j-end."""
        return sub_tag(self.design.line.tag, 92)

    @property
    def int_tag(self) -> int:
        """Beam integration tag used by OpenSees."""
        return self.design.line.tag

    @property
    def geo_transf_tag(self) -> int:
        """Geometric transformation tag used by OpenSees."""
        return self.design.line.tag

    @property
    def clear_length(self) -> float:
        """Length of the deformable element, without the rigid joint
        offsets."""
        start = np.array(self.ele_node_i.coordinates) + self.jnt_offsets[:3]
        end = np.array(self.ele_node_j.coordinates) + self.jnt_offsets[3:]
        return float(np.linalg.norm(end - start))

    def __init__(
        self, design: BeamDesign, bondslip_factor: float,
        load_factors: Dict[Literal['G', 'Q'], float],
        cyclic_model: bool = False,
        cracked_section: None | bool | float = None,
        load_type: Literal['uniform', 'point'] = 'point',
        yield_mom_curv: Literal['empirical', 'analytical'] = 'empirical'
    ) -> None:
        """Initialize the Beam object.

        Parameters
        ----------
        design : ~simdesign.rcmrf.bdim.baselib.beam.BeamBase
            Instance of beam design information model.
        bondslip_factor : float
            Bondslip factor considered while defining plastic hinges.
        load_factors : Dict[Literal['G', 'Q'], float]
            Load factors used to compute uniformly distributed gravity load on
            the beam.
        cyclic_model : bool, optional
            If True, the model parameters will be adjusted for cyclic analysis.
            By default False.
        cracked_section : None | bool | float, optional
            Cracked-section (effective) flexural properties of the elastic
            sections: True for My / phi_y of the plastic hinges (see
            `yield_mom_curv`), or a float as the ratio of effective to gross
            flexural stiffness. If None or False, gross-section properties
            are used. By default None.
        load_type : Literal['uniform', 'point'], optional
            How the gravity load is applied: 'uniform' as a uniformly
            distributed element load, 'point' as equivalent point loads at the
            element ends. By default 'point'.
        yield_mom_curv : Literal['empirical', 'analytical'], optional
            Yield moment and curvature of the plastic hinges: 'empirical'
            from the expressions of Panagiotakos and Fardis (2001),
            'analytical' from a moment-curvature section analysis.
            By default 'empirical'.
        """
        self.design = design
        self.bondslip_factor = bondslip_factor
        self.cyclic_model = cyclic_model
        self.cracked = cracked_section
        self.load_type = load_type
        self.yield_mom_curv = yield_mom_curv
        # Set the gravity loading based on load factors
        self.ele_load = round(
            float(design.wg_total * load_factors['G']
                  + design.wq_total * load_factors['Q']),
            PRECISION)
        # Initailize joint offsets
        self.jnt_offsets = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        # Set cracked section properties
        self._set_cracked_properties()

    def add_to_ops(self) -> None:
        """Adds beam components to the OpenSees domain
        (i.e, elastic beam element and nodes).
        """
        # Define geometric transformation
        ops.geomTransf(*self._get_geo_transf_inputs())

        # Create the section materials
        mat_inputs_i, mat_inputs_j = self._get_mz_mat_inputs()
        ops.uniaxialMaterial(*mat_inputs_i)
        ops.uniaxialMaterial(*mat_inputs_j)

        # Create element sections
        ops.section(*self._get_elastic_sec_inputs())
        ops.section(*self._get_inelastic_sec_i_inputs())
        ops.section(*self._get_inelastic_sec_j_inputs())

        # Create beam integration
        ops.beamIntegration(*self._get_int_inputs())

        # Create the element
        ops.element(*self._get_ele_inputs())

    def to_py(self) -> List[str]:
        """Gets the Python commands to construct beam components in OpenSees
        domain (i.e, beam element and nodes).

        Returns
        -------
        List[str]
            List of Python commands for constructing the components of beam
            object in OpenSees.
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
        mz_mat_inputs_i, mz_mat_inputs_j = self._get_mz_mat_inputs()
        mz_mat_inputs_i = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in mz_mat_inputs_i
        )
        mz_mat_inputs_j = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in mz_mat_inputs_j
        )
        content.append(f"ops.uniaxialMaterial({mz_mat_inputs_i})")
        content.append(f"ops.uniaxialMaterial({mz_mat_inputs_j})")

        # Create sections
        content.append('# Create element sections')
        elastic_sec_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_elastic_sec_inputs()
        )
        inelastic_sec_i_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_inelastic_sec_i_inputs()
        )
        inelastic_sec_j_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_inelastic_sec_j_inputs()
        )
        content.append(f"ops.section({elastic_sec_inputs})")
        content.append(f"ops.section({inelastic_sec_i_inputs})")
        content.append(f"ops.section({inelastic_sec_j_inputs})")

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
        """Gets the Tcl commands to construct beam components in OpenSees
        domain (i.e, beam element and nodes).

        Returns
        -------
        List[str]
            List of Tcl commands for constructing the components of beam
            object in OpenSees.
        """
        # Define geometric transformation
        content = ['# Create geometric transformation']
        transf_inputs = ' '.join(f"{item}" for item in
                                 self._get_geo_transf_inputs())
        content.append(f"geomTransf {transf_inputs}")

        # Create the section materials
        content.append('# Create uniaxial materials')
        mz_mat_inputs_i, mz_mat_inputs_j = self._get_mz_mat_inputs()
        mz_mat_inputs_i = ' '.join(f"{item}" for item in mz_mat_inputs_i)
        mz_mat_inputs_j = ' '.join(f"{item}" for item in mz_mat_inputs_j)
        content.append(f"uniaxialMaterial {mz_mat_inputs_i}")
        content.append(f"uniaxialMaterial {mz_mat_inputs_j}")

        # Create sections
        content.append('# Create element sections')
        elastic_sec_inputs = ' '.join(
            f"{item}" for item in self._get_elastic_sec_inputs())
        inelastic_sec_i_inputs = ' '.join(
            f"{item}" for item in self._get_inelastic_sec_i_inputs())
        inelastic_sec_j_inputs = ' '.join(
            f"{item}" for item in self._get_inelastic_sec_j_inputs())
        content.append(f"section {elastic_sec_inputs}")
        content.append(f"section {inelastic_sec_i_inputs}")
        content.append(f"section {inelastic_sec_j_inputs}")

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

    @property
    def end_gaps(self) -> Tuple[float, float]:
        """Lengths of the beam line at the i and j ends that are not part of
        the deformable element (rigid joint offsets or links).

        Returns
        -------
        Tuple[float, float]
            Gap lengths at the i and j ends.
        """
        start = np.array(self.ele_node_i.coordinates) + self.jnt_offsets[:3]
        end = np.array(self.ele_node_j.coordinates) + self.jnt_offsets[3:]
        points = [np.array(point.coordinates)
                  for point in self.design.line.points]
        gap_i = min(float(np.linalg.norm(start - x)) for x in points)
        gap_j = min(float(np.linalg.norm(end - x)) for x in points)
        return gap_i, gap_j

    def _get_grav_point_loads(self) -> Tuple[float, float]:
        """Vertical point loads at the element end nodes.

        For ``load_type='point'``, half of the total beam load, i.e., of the
        load over the beam line length, is applied at each end. For
        ``load_type='uniform'``, the load over the rigid end regions, which
        is not covered by the uniformly distributed element load, is
        applied at the corresponding end.

        Returns
        -------
        Tuple[float, float]
            Point loads at the i and j ends (positive downwards).
        """
        if self.load_type == 'point':
            load = self.ele_load * self.design.line.length / 2
            return round(load, PRECISION), round(load, PRECISION)
        gap_i, gap_j = self.end_gaps
        return (round(self.ele_load * gap_i, PRECISION),
                round(self.ele_load * gap_j, PRECISION))

    def add_grav_loads_to_ops(self) -> None:
        """Adds gravity load objects to the OpenSees domain
        (i.e, uniformly distributed loads, or point loads at both ends).

        Notes
        -----
        Both options apply the total load over the beam line length.
        """
        if self.load_type == 'uniform':
            ops.eleLoad('-ele', self.ele_tag, '-type', '-beamUniform',
                        -self.ele_load, 0.0)
        for node, load in zip((self.ele_node_i, self.ele_node_j),
                              self._get_grav_point_loads()):
            if load:
                ops.load(node.tag, 0.0, 0.0, -load, 0.0, 0.0, 0.0)

    def to_py_grav_loads(self) -> List[str]:
        """Gets the Python commands to construct beam gravity load objects in
        OpenSees domain (i.e, uniformly distributed loads, or point loads at
        both ends).

        Returns
        -------
        List[str]
            List of Python commands for adding beam gravity loads
            to OpenSees.
        """
        content = []
        if self.load_type == 'uniform':
            content.append(
                f"ops.eleLoad('-ele', {self.ele_tag}, '-type', "
                f"'-beamUniform', {-self.ele_load}, 0.0)")
        for node, load in zip((self.ele_node_i, self.ele_node_j),
                              self._get_grav_point_loads()):
            if load:
                content.append(
                    f"ops.load({node.tag}, 0.0, 0.0, {-load}, 0.0, 0.0, 0.0)")
        return content

    def to_tcl_grav_loads(self) -> List[str]:
        """Gets the Tcl commands to construct beam gravity load objects in
        OpenSees domain (i.e, uniformly distributed loads, or point loads at
        both ends).

        Returns
        -------
        List[str]
            List of Tcl commands for adding beam gravity loads to OpenSees.
        """
        content = []
        if self.load_type == 'uniform':
            content.append(
                f"eleLoad -ele {self.ele_tag} -type "
                f"-beamUniform {-self.ele_load} 0.0")
        for node, load in zip((self.ele_node_i, self.ele_node_j),
                              self._get_grav_point_loads()):
            if load:
                content.append(f"load {node.tag} 0.0 0.0 {-load} 0.0 0.0 0.0")
        return content

    def _get_geo_transf_inputs(self) -> List[str | int | float]:
        """Builds the OpenSees ``geomTransf`` command arguments.

        Returns
        -------
        List[str | int | float]
            Inputs for ``ops.geomTransf``, including the transformation type,
            tag, ``vecxz`` definition, and optional joint offsets.
        """
        inputs = ['Linear', self.geo_transf_tag] \
            + self.vecxz + ['-jntOffset'] + self.jnt_offsets
        return inputs

    def _get_ele_inputs(self) -> List[str | int]:
        """Retrieves beam element inputs.

        Returns
        -------
        List[str | int]
            List of beam element inputs.
        """
        ele_inputs = [
            'forceBeamColumn', self.design.line.tag,
            self.ele_node_i.tag, self.ele_node_j.tag,
            self.geo_transf_tag, self.int_tag
        ]

        return ele_inputs

    def _get_elastic_sec_inputs(self) -> List[str | int | float]:
        """Retrieves elastic beam section inputs.

        Returns
        -------
        List[str | int | float]
            List of elastic beam section inputs.
        """
        if self.cracked:
            Iz = self._Iz_eff
        else:
            Iz = self.design.Iz
        sec_inputs = [
            'Elastic', self.elastic_sec_tag, self.Ecm_q, self.design.Ag,
            Iz, self.design.Iy, self.Gcm_q, self.design.J
        ]
        sec_inputs = round_list(sec_inputs)

        return sec_inputs

    def _get_hinge_elastic_mat_inputs(
        self
    ) -> List[List[str | float | int]]:
        """Retrieves the elastic material inputs of the hinge sections.

        Returns
        -------
        List[List[str | float | int]]
            Inputs of the elastic axial (EA), flexural about local-y (EIy) and
            torsional (GJ) materials, i.e., the properties of the elastic
            section in the degrees of freedom without a hinge.
        """
        return [
            round_list(['Elastic', self.p_mat_tag,
                        self.Ecm_q * self.design.Ag]),
            round_list(['Elastic', self.my_mat_tag,
                        self.Ecm_q * self.design.Iy]),
            round_list(['Elastic', self.t_mat_tag,
                        self.Gcm_q * self.design.J])
        ]

    def _get_inelastic_sec_i_inputs(self) -> List[str | int]:
        """Retrieves inputs for inelastic beam section at ith end.

        Returns
        -------
        List[str | int]
            List of inputs for inelastic beam section at ith end.
        """
        sec_inputs = [
            'Aggregator', self.inelastic_sec_i_tag,
            self.mz_i_mat_tag, 'Mz',
            RIGID_MAT, 'Vy',
            RIGID_MAT, 'My',
            RIGID_MAT, 'Vz',
            RIGID_MAT, 'P',
            RIGID_MAT, 'T'
        ]

        return sec_inputs

    def _get_inelastic_sec_j_inputs(self) -> List[str | int]:
        """Retrieves inputs for inelastic beam section at jth end.

        Returns
        -------
        List[str | int]
            List of inputs for inelastic beam section at jth end.
        """
        sec_inputs = [
            'Aggregator', self.inelastic_sec_j_tag,
            self.mz_j_mat_tag, 'Mz',
            RIGID_MAT, 'Vy',
            RIGID_MAT, 'My',
            RIGID_MAT, 'Vz',
            RIGID_MAT, 'P',
            RIGID_MAT, 'T'
        ]

        return sec_inputs

    def _get_int_inputs(self) -> List[str | int | float]:
        """Retrieves beam integration inputs.

        Returns
        -------
        List[str | int | float]
            List of beam integration inputs.

        References
        ----------
        Scott, M. H., & Fenves, G. L. (2006). Plastic Hinge Integration Methods
        for Force-Based Beam-Column Elements. Journal of Structural
        Engineering, 132(2), 244-252.
        https://doi.org/10.1061/(asce)0733-9445(2006)132:2(244)
        """
        Lp = self._get_lp()
        # Beam integration inputs
        int_inputs = [
            'HingeRadau', self.int_tag,
            self.inelastic_sec_i_tag, Lp[0], self.inelastic_sec_j_tag, Lp[-1],
            self.elastic_sec_tag
        ]

        return int_inputs

    def _get_mz_mat_inputs(self) -> Tuple[List[str | float],
                                          List[str | float]]:
        """Retrieves the material inputs defining the flexural behaviour
        around local-z for the plastic hinge of forceBeamColumn element.

        Returns
        -------
        mat_inputs_i : List[str | float]
            Hysteretic material model inputs for hinge at the start section.
        mat_inputs_j : List[str | float]
            Hysteretic material model inputs for hinge at the end section.
        """
        # Backbone of the plastic hinges
        (
            phiy_neg, My_neg, Mc_neg, Mr_neg,
            theta_y_neg, theta_cap_pl_neg, theta_pc_neg,
            phiy_pos, My_pos, Mc_pos, Mr_pos,
            theta_y_pos, theta_cap_pl_pos, theta_pc_pos,
        ) = self._get_rot_hinge_props()

        # Rotation values
        theta_1_neg = theta_y_neg
        theta_2_neg = theta_1_neg + theta_cap_pl_neg
        theta_3_neg = theta_2_neg + theta_pc_neg
        theta_1_pos = theta_y_pos
        theta_2_pos = theta_1_pos + theta_cap_pl_pos
        theta_3_pos = theta_2_pos + theta_pc_pos

        # Curvature values
        # Accounting for all the flexibility sources of the yield rotation
        Lp = self._get_lp()
        phi_1_neg = self._get_phiy_adjusted(My_neg, theta_y_neg, Lp)
        phi_1_pos = self._get_phiy_adjusted(My_pos, theta_y_pos, Lp)
        phi_2_neg = (theta_2_neg - theta_1_neg) / Lp + phi_1_neg
        phi_3_neg = (theta_3_neg - theta_1_neg) / Lp + phi_1_neg
        phi_2_pos = (theta_2_pos - theta_1_pos) / Lp + phi_1_pos
        phi_3_pos = (theta_3_pos - theta_1_pos) / Lp + phi_1_pos

        # Material inputs
        mat_inputs_i = [
            'Hysteretic', self.mz_i_mat_tag,
            My_pos[0], phi_1_pos[0],
            Mc_pos[0], phi_2_pos[0],
            Mr_pos[0], phi_3_pos[0],
            -My_neg[0], -phi_1_neg[0],
            -Mc_neg[0], -phi_2_neg[0],
            -Mr_neg[0], -phi_3_neg[0],
            *HYSTERETIC_PARAMETERS
        ]
        mat_inputs_j = [
            'Hysteretic', self.mz_j_mat_tag,
            My_pos[-1], phi_1_pos[-1],
            Mc_pos[-1], phi_2_pos[-1],
            Mr_pos[-1], phi_3_pos[-1],
            -My_neg[-1], -phi_1_neg[-1],
            -Mc_neg[-1], -phi_2_neg[-1],
            -Mr_neg[-1], -phi_3_neg[-1],
            *HYSTERETIC_PARAMETERS
        ]

        # Rounding to precision
        mat_inputs_i = round_list(mat_inputs_i)
        mat_inputs_j = round_list(mat_inputs_j)

        return mat_inputs_i, mat_inputs_j

    def _get_phiy_adjusted(
        self, My: Array3, theta_y: Array3, Lp: Array3
    ) -> Array3:
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
        My : Array3
            Yield moment of the sections.
        theta_y : Array3
            Yield rotation of the sections.
        Lp : Array3
            Plastic hinge length of the sections.

        Returns
        -------
        phi_y : Array3
            Yield curvature of the hinge sections.
        """
        ls = self.clear_length / 2  # Shear span, as in _get_rot_hinge_props
        EIeff = self.Ecm_q * self._get_elastic_sec_inputs()[4]
        dtheta = np.maximum(theta_y - My * ls / (3 * EIeff), 0.0)
        phiy = My / EIeff + dtheta / Lp
        return phiy

    def _get_lp(self) -> Array3:
        """Computes plastic hinge length for the sections.

        Returns
        -------
        Lp : Array3
            Plastic hinge lengths for the beam sections.

        References
        ----------
        Priestley, M. J. N., Calvi, G. M., & Kowalsky, M. J. (2007).
        *Displacement-based seismic design of structures*. IUSS Press.
        """
        # Shear span, assuming equal to 50% of the free length of the element
        Ls = self.clear_length / 2
        # Smallest diameter of the longitudinal reinforcement
        dbl = np.minimum(
            self.design.dbl_t1_q,
            np.minimum(
                self.design.dbl_t2_q,
                np.minimum(self.design.dbl_b1_q, self.design.dbl_b2_q),
            ),
        )
        return rc.get_lp_priestley_2007(Ls, self.design.fsyl_q, dbl)

    def _get_my_phiy(self, direction: Literal['negative', 'positive']
                     ) -> Tuple[Array3, Array3, Array3]:
        """Computes yield moment and curvatures about local-z axis
        in the given bending direction for beam sections.

        Parameters
        ----------
        direction : Literal['negative', 'positive']
            Bending direction.

        Returns
        -------
        My : Array3
            Yield moment of beam in the specified `direction`.
            Computed for start, mid, end beam sections.
        phiy : Array3
            Yield curvature of beam in the specified `direction`.
            Computed for start, mid, end beam sections.
        cy : Array3
            Neutral axis depth at yield in the specified `direction`.
            Computed for start, mid, end beam sections.

        See Also
        --------
        :meth:`_get_my_phiy_empirical` : Empirical expressions, used if
            ``yield_mom_curv='empirical'``.
        :meth:`_get_my_phiy_analytical` : Section analysis, used if
            ``yield_mom_curv='analytical'``.
        """
        if self.yield_mom_curv == 'analytical':
            return self._get_my_phiy_analytical(direction)
        return self._get_my_phiy_empirical(direction)

    def _get_rot_hinge_props(self) -> List[Array3]:
        """Computes the backbone parameters of the rotational plastic
        hinges about the local-z axis.

        Returns
        -------
        props : List[Array3]
            Ordered list of backbone parameters, for the start, mid and end
            beam sections:

            0. ``phiy_neg`` (Array3) Yield curvature in the negative bending
            direction.
            1. ``My_neg`` (Array3) Yield moment in the negative bending
            direction.
            2. ``Mc_neg`` (Array3) Capping (maximum) moment in the negative
            bending direction.
            3. ``Mr_neg`` (Array3) Residual moment in the negative bending
            direction.
            4. ``theta_y_neg`` (Array3) Yield rotation in the negative bending
            direction.
            5. ``theta_cap_pl_neg`` (Array3) Plastic rotation capacity up to
            capping (negative).
            6. ``theta_pc_neg`` (Array3) Post-capping rotation capacity
            (negative).
            7. ``phiy_pos`` (Array3) Yield curvature in the positive bending
            direction.
            8. ``My_pos`` (Array3) Yield moment in the positive bending
            direction.
            9. ``Mc_pos`` (Array3) Capping (maximum) moment in the positive
            bending direction.
            10. ``Mr_pos`` (Array3) Residual moment in the positive bending
            direction.
            11. ``theta_y_pos`` (Array3) Yield rotation in the positive
            bending direction.
            12. ``theta_cap_pl_pos`` (Array3) Plastic rotation capacity up to
            capping (positive).
            13. ``theta_pc_pos`` (Array3) Post-capping rotation capacity
            (positive).

        References
        ---------
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
        """
        h = self.design.h
        ln = self.clear_length  # Clear length, without the joint offsets
        fc = self.design.fc_q
        fsyl = self.design.fsyl_q
        b = self.design.b
        sbh = self.design.sbh_q
        rhol = self.rhol_q
        rhoh = self.rhoh_y_q

        # Shear span, assuming equal to 50% of the free length of the element
        ls = ln / 2  # NOTE: Could be varied with intensity of loading, but ok.
        niu = 0.0  # Axial load ratio, assuming beams do not have any

        # Compute yield moments in positive and negative directions
        My_neg, phiy_neg, _ = self._get_my_phiy('negative')
        My_pos, phiy_pos, _ = self._get_my_phiy('positive')

        # Tension reinforcement of each bending direction: negative has top
        # rebars in tension, positive has bottom rebars in tension
        As_neg, _, dbl_neg, dd_neg = self._get_rebar_in_direction('negative')
        As_pos, _, dbl_pos, dd_pos = self._get_rebar_in_direction('positive')

        # Yield rotation capacity - EN 1998-3:2004 - Equation A.10b
        # (tension shift factor from the shear cracking resistance - EN 1992-1)
        theta_y_neg = rc.get_yield_rot_eurocode8(
            phiy_neg, h, ls, fc, fsyl, dbl_neg, self.bondslip_factor,
            My=My_neg, b=b, As_tens=As_neg, dd=dd_neg)
        theta_y_pos = rc.get_yield_rot_eurocode8(
            phiy_pos, h, ls, fc, fsyl, dbl_pos, self.bondslip_factor,
            My=My_pos, b=b, As_tens=As_pos, dd=dd_pos)

        # Maximum moment capacity and plastic rotation capacity by
        # Haselton et al. 2016. Negative: top rebar in tension, bottom rebar
        # in compression. Positive: bottom rebar in tension, top rebar in
        # compression. The rotation capacity of the non-symmetric section is
        # adjusted for the bending direction - Equation 7
        # NOTE: This is different than MATLAB implementation
        # (max(0.01, w_compression) / max(0.01, w_tension)) ** 0.225
        Mc_neg, theta_cap_pl_neg = rc.get_capping_mom_plastic_rot_haselton2016(
            My_neg, fc, fsyl, rhol, rhoh, sbh, dbl_neg, niu,
            self.bondslip_factor, rhol_tens=self.rhol_top_q,
            rhol_comp=self.rhol_bot_q, cyclic_model=self.cyclic_model)
        Mc_pos, theta_cap_pl_pos = rc.get_capping_mom_plastic_rot_haselton2016(
            My_pos, fc, fsyl, rhol, rhoh, sbh, dbl_pos, niu,
            self.bondslip_factor, rhol_tens=self.rhol_bot_q,
            rhol_comp=self.rhol_top_q, cyclic_model=self.cyclic_model)

        # Residual moment and post-capping rotation capacity by
        # Haselton et al. 2016
        Mr_neg, theta_pc_neg = (
            rc.get_residual_mom_post_capping_rot_haselton2016(
                Mc_neg, rhoh, niu, cyclic_model=self.cyclic_model))
        Mr_pos, theta_pc_pos = (
            rc.get_residual_mom_post_capping_rot_haselton2016(
                Mc_pos, rhoh, niu, cyclic_model=self.cyclic_model))

        # The negative ones are based on top (compression) reinforcement
        # The positive ones are based on bottom (tension) renforcement
        backbone = [
            phiy_neg, My_neg, Mc_neg, Mr_neg,
            theta_y_neg, theta_cap_pl_neg, theta_pc_neg,
            phiy_pos, My_pos, Mc_pos, Mr_pos,
            theta_y_pos, theta_cap_pl_pos, theta_pc_pos,
        ]

        return backbone

    def _get_rebar_in_direction(
        self, direction: Literal['negative', 'positive']
    ) -> Tuple[Array3, Array3, Array3, Array3]:
        """Gets the longitudinal reinforcement of beam sections which are
        in tension and compression for the given bending direction.

        Parameters
        ----------
        direction : Literal['negative', 'positive']
            Bending direction. Negative: top rebars in tension. Positive:
            bottom rebars in tension.

        Returns
        -------
        As_tens : Array3
            Area of the tension reinforcement.
        As_comp : Array3
            Area of the compression reinforcement.
        dbl_tens : Array3
            Diameter of the (first layer of) tension reinforcement.
        dd : Array3
            Distance from the extreme concrete fiber in compression to the
            centroid of the (first layer of) tension reinforcement.
            Computed for start, mid, end beam sections.
        """
        cover = self.design.cover_q
        dbh = self.design.dbh_q
        # Longitudinal reinforcement area of the bottom and top bars
        As_bot = (self.design.nbl_b1_q * ((0.25 * np.pi)
                                          * self.design.dbl_b1_q**2)
                  + self.design.nbl_b2_q * ((0.25 * np.pi)
                                            * self.design.dbl_b2_q**2))
        As_top = (self.design.nbl_t1_q * ((0.25 * np.pi)
                                          * self.design.dbl_t1_q**2)
                  + self.design.nbl_t2_q * ((0.25 * np.pi)
                                            * self.design.dbl_t2_q**2))

        # Set direction dependent parameters
        if direction == 'positive':  # bottom rebars in tension
            As_tens, As_comp = As_bot, As_top
            dbl_tens = self.design.dbl_b1_q
        elif direction == 'negative':  # top rebars in tension
            As_tens, As_comp = As_top, As_bot
            dbl_tens = self.design.dbl_t1_q
        # Dist. from concrete fiber in compression to the rebars in tension
        dd = self.design.h - cover - dbh - 0.5 * dbl_tens

        return As_tens, As_comp, dbl_tens, dd

    def _get_my_phiy_empirical(
        self, direction: Literal['negative', 'positive']
    ) -> Tuple[Array3, Array3, Array3]:
        """Computes yield moment and curvatures about local-z axis
        in the given bending direction for beam sections by the
        empirical relationship proposed in Panagiotakos and Fardis 2001.

        Parameters
        ----------
        direction : Literal['negative', 'positive']
            Bending direction.

        Returns
        -------
        My : Array3
            Yield moment of beam in the specified `direction`.
            Computed for start, mid, end beam sections.
        phiy : Array3
            Yield curvature of beam in the specified `direction`.
            Computed for start, mid, end beam sections.
        cy : Array3
            Neutral axis depth at yield in the specified `direction`.
            Computed for start, mid, end beam sections.

        See Also
        --------
        :func:`~simdesign.utils.rcsection.get_my_phiy_panagiotakos_fardis2001`

        Notes
        -----
        The axial load and the web reinforcement of beams are neglected.

        References
        ----------
        Panagiotakos, T. B., & Fardis, M. N. (2001).
        Deformations of reinforced concrete members at yielding and ultimate.
        Structural Journal, 98(2), 135-148.
        """
        As_tens, As_comp, _, dd = self._get_rebar_in_direction(direction)

        return rc.get_my_phiy_panagiotakos_fardis2001(
            h=self.design.h, b=self.design.b, fc=self.design.fc_q,
            Ec=self.Ecm_q, Es=self.design.Es, fsyl=self.design.fsyl_q,
            As_tens=As_tens, As_comp=As_comp, dd=dd)

    def _get_my_phiy_analytical(
        self, direction: Literal['negative', 'positive']
    ) -> Tuple[Array3, Array3, Array3]:
        """Computes yield moment and curvatures about local-z axis
        in the given bending direction for beam sections by the
        simplified section analysis.

        Parameters
        ----------
        direction : Literal['negative', 'positive']
            Bending direction: 'positive' for sagging (top in compression),
            'negative' for hogging (bottom in compression).

        Returns
        -------
        My : Array3
            Yield moment for start, mid, end beam sections.
        phi_y : Array3
            Yield curvature for start, mid, end beam sections.
        cy : Array3
            Neutral axis depth at yield in the specified `direction`.
            Computed for start, mid, end beam sections.

        See Also
        --------
        :func:`~simdesign.utils.rcsection.do_simplified_section_analysis`

        Notes
        -----
        The axial load is neglected in the moment-curvature calculation.
        """
        h = self.design.h
        b = self.design.b
        fc = float(self.design.fc_q)
        fsyl = float(self.design.fsyl_q)
        Es = self.design.steel.Es
        Ec = float(self.Ecm_q)
        cv = float(self.design.cover_q)
        My_list, phi_list, cy_list = [], [], []
        for idx in range(3):
            # Diameter of each rebar type and their quantities
            nbl_b1 = float(self.design.nbl_b1_q[idx])
            nbl_b2 = float(self.design.nbl_b2_q[idx])
            dbl_b1 = float(self.design.dbl_b1_q[idx])
            dbl_b2 = float(self.design.dbl_b2_q[idx])
            nbl_t1 = float(self.design.nbl_t1_q[idx])
            nbl_t2 = float(self.design.nbl_t2_q[idx])
            dbl_t1 = float(self.design.dbl_t1_q[idx])
            dbl_t2 = float(self.design.dbl_t2_q[idx])
            dbh = float(self.design.dbh_q[idx])
            # Reinforcement layout (depths from the top fiber)
            yt1 = cv + dbh + dbl_t1 / 2
            yt2 = cv + dbh + dbl_t2 / 2
            yb1 = h - (cv + dbh + dbl_b1 / 2)
            yb2 = h - (cv + dbh + dbl_b2 / 2)
            y_layers = [yt2, yt1, yb1, yb2]
            As_layers = [nbl_t2 * 0.25 * np.pi * dbl_t2**2,
                         nbl_t1 * 0.25 * np.pi * dbl_t1**2,
                         nbl_b1 * 0.25 * np.pi * dbl_b1**2,
                         nbl_b2 * 0.25 * np.pi * dbl_b2**2]
            if direction == 'negative':
                # Hogging: measure the depths from the bottom fiber
                y_layers = [h - y for y in y_layers]
            # Sort the distances in ascending order
            y_layers, As_layers = map(list, zip(
                *sorted(zip(y_layers, As_layers))))
            _, _, _, My, phi_y, cy = rc.do_simplified_section_analysis(
                h=h, b=b, fc=fc, Ec=Ec,
                Pext=0.0, fyL=fsyl, Es=Es,
                As_layers=As_layers,
                y_layers=y_layers,
            )
            My_list.append(float(My))
            phi_list.append(float(phi_y))
            cy_list.append(float(cy))
        return np.array(My_list), np.array(phi_list), np.array(cy_list)

    def _set_cracked_properties(self) -> None:
        """
        Computes and stores cracked-section (effective) flexural properties
        about local z.

        The effective second moment of area ``self._Iz_eff`` is always
        computed, regardless of ``cracked``, as ``EIeff / Ec`` with
        ``EIeff = My / phi_y`` from the yield moment and curvature of the
        plastic hinges (see ``_get_my_phiy``), averaged over both end
        sections and bending directions. If ``cracked`` is a float, it is
        instead the ratio of effective to gross stiffness times ``Iz``.
        ``self._Iz_eff`` is used by the elastic sections only if ``cracked``
        is True or a float; if it is None or False, the gross section is
        used.

        Notes
        -----
        The axial load of beams is neglected in the yield point.

        See Also
        --------
        :meth:`_get_my_phiy` : Yield point of the plastic hinges.
        """
        # EIeff = My/φy. The slope of the section's moment-curvature
        # response up to yield, so flexure only.
        # It follows yield_mom_curv (empirical or analytical)
        My_neg, phiy_neg, _ = self._get_my_phiy('negative')
        My_pos, phiy_pos, _ = self._get_my_phiy('positive')
        EIeffs = [My_neg[k] / phiy_neg[k] for k in (0, -1)] + [
            My_pos[k] / phiy_pos[k] for k in (0, -1)]
        self._Iz_eff = float(np.mean(EIeffs) / self.Ecm_q)
        if isinstance(self.cracked, float):
            # User-defined ratio of effective to gross flexural stiffness
            self._Iz_eff = self.cracked * self.design.Iz
