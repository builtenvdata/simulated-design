"""This module provides a base class for representing beams
within the BNSM layer and for building and exporting their OpenSees
representations.
"""
# Imports from installed packages
from abc import ABC
import numpy as np
import openseespy.opensees as ops
from typing import List, Literal, Dict, Tuple

# Imports from bnsm library
from .node import Node
from .constants import RIGID_MAT

# Imports from bdim base library
from ...bdim.baselib.beam import BeamBase as BeamDesign
from ...bdim.baselib.beam import Array3

# Imports from utils library
from ....utils.units import MPa, mm
from ....utils.misc import PRECISION, round_list
from ....utils.rcsection import get_moments


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
    jnt_offsets : List[float]
        Rigid joint offset values (dx_i, dy_i, dz_i, dx_j, dy_j, dz_j),
        specified with respect to the global coordinate system.
    cyclic_model : bool
        If True, the model parameters will be adjusted for cyclic analysis.
    cracked_section : bool
        If True, the elastic sections uses cracked-section
        (effective) flexural properties. If False, gross-section
        properties are used.
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
    jnt_offsets: List[float]
    cracked_section: bool
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
        return int(str(self.design.line.tag) + '990')

    @property
    def mz_j_mat_tag(self) -> int:
        """Material tag for the *j-end* flexural hinge about local-z (Mz)."""
        return int(str(self.design.line.tag) + '991')

    @property
    def elastic_sec_tag(self) -> int:
        """Section tag for the elastic (interior) section."""
        return int(str(self.design.line.tag) + '990')

    @property
    def inelastic_sec_i_tag(self) -> int:
        """Section tag for the inelastic (hinge) section at i-end."""
        return int(str(self.design.line.tag) + '991')

    @property
    def inelastic_sec_j_tag(self) -> int:
        """Section tag for the inelastic (hinge) section at j-end."""
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
        self, design: BeamDesign, bondslip_factor: float,
        load_factors: Dict[Literal['G', 'Q'], float],
        cyclic_model: bool = False, cracked_section: bool = False
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
        cracked_section : bool, optional
            If True, the elastic sections uses cracked-section
            (effective) flexural properties. If False, gross-section
            properties are used. By default False.
        """
        self.design = design
        self.bondslip_factor = bondslip_factor
        self.cyclic_model = cyclic_model
        self.cracked_section = cracked_section
        # Set the gravity loading based on load factors
        self.ele_load = round(
            float(design.wg_total * load_factors['G']
                  + design.wq_total * load_factors['Q']),
            PRECISION)
        # Initailize joint offsets
        self.jnt_offsets = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        # Set cracked section properties
        self._set_cracked_section_properties()

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

    def add_grav_loads_to_ops(self) -> None:
        """Adds gravity load objects to the OpenSees domain
        (i.e, uniformly distrubted loads).
        """
        ops.eleLoad('-ele', self.ele_tag, '-type', '-beamUniform',
                    -self.ele_load, 0.0)

    def to_py_grav_loads(self) -> str:
        """Gets the Python commands to construct beam gravity load object in
        OpenSees domain (i.e, uniformly distrubted loads).

        Returns
        -------
        str
            Python command for constructing beam gravity load object
            in OpenSees.
        """
        return (
            f"ops.eleLoad('-ele', {self.ele_tag}, '-type', "
            f"'-beamUniform', {-self.ele_load}, 0.0)"
        )

    def to_tcl_grav_loads(self) -> str:
        """Gets the Tcl commands to construct beam gravity load object in
        OpenSees domain (i.e, uniformly distrubted loads).

        Returns
        -------
        str
            Tcl command for constructing beam gravity load object
            in OpenSees.
        """
        return (
            f"eleLoad -ele {self.ele_tag} -type "
            f"-beamUniform {-self.ele_load} 0.0"
        )

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
        if self.cracked_section:
            Iz = self._Iz_eff
        else:
            Iz = self.design.Iz
        sec_inputs = [
            'Elastic', self.elastic_sec_tag, self.Ecm_q, self.design.Ag,
            Iz, self.design.Iy, self.Gcm_q, self.design.J
        ]
        sec_inputs = round_list(sec_inputs)

        return sec_inputs

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
        Lp = self._get_plastic_hinge_length()
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
        # Plastic hinge properties
        (
            phiy_neg, My_neg, Mc_neg, Mr_neg,
            theta_y_neg, theta_cap_pl_neg, theta_pc_neg,
            phiy_pos, My_pos, Mc_pos, Mr_pos,
            theta_y_pos, theta_cap_pl_pos, theta_pc_pos,
            pinchx, pinchy, damage1, damage2, beta,
        ) = self._get_rot_hinge_props()

        # Rotation values for monotonic loading
        theta_1_neg = theta_y_neg
        theta_2_neg = theta_y_neg + theta_cap_pl_neg
        theta_3_neg = theta_y_neg + theta_cap_pl_neg + theta_pc_neg
        theta_1_pos = theta_y_pos
        theta_2_pos = theta_y_pos + theta_cap_pl_pos
        theta_3_pos = theta_y_pos + theta_cap_pl_pos + theta_pc_pos
        # NOTE: rotation values needs to be adjusted for cyclic loading
        # theta_cap_pl needs to be factored by 0.7
        # theta_pc needs to be factored by 0.5

        # Curvature values for monotonic loading
        Lp = self._get_plastic_hinge_length()
        phi_1_neg = phiy_neg
        phi_2_neg = (theta_2_neg - theta_1_neg) / Lp + phiy_neg
        phi_3_neg = (theta_3_neg - theta_1_neg) / Lp + phiy_neg
        phi_1_pos = phiy_pos
        phi_2_pos = (theta_2_pos - theta_1_pos) / Lp + phiy_pos
        phi_3_pos = (theta_3_pos - theta_1_pos) / Lp + phiy_pos

        # Material inputs
        mat_inputs_i = [
            'Hysteretic', self.mz_i_mat_tag,
            My_pos[0], phi_1_pos[0],
            Mc_pos[0], phi_2_pos[0],
            Mr_pos[0], phi_3_pos[0],
            -My_neg[0], -phi_1_neg[0],
            -Mc_neg[0], -phi_2_neg[0],
            -Mr_neg[0], -phi_3_neg[0],
            pinchx, pinchy, damage1, damage2, beta
        ]
        mat_inputs_j = [
            'Hysteretic', self.mz_j_mat_tag,
            My_pos[-1], phi_1_pos[-1],
            Mc_pos[-1], phi_2_pos[-1],
            Mr_pos[-1], phi_3_pos[-1],
            -My_neg[-1], -phi_1_neg[-1],
            -Mc_neg[-1], -phi_2_neg[-1],
            -Mr_neg[-1], -phi_3_neg[-1],
            pinchx, pinchy, damage1, damage2, beta
        ]

        # Rounding to precision
        mat_inputs_i = round_list(mat_inputs_i)
        mat_inputs_j = round_list(mat_inputs_j)

        return mat_inputs_i, mat_inputs_j

    def _get_plastic_hinge_length(self) -> Array3:
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
        Ls = self.design.line.length / 2 / mm  # in mm
        # Diameter of internal reinforcement
        dbl = (
            np.minimum(
                self.design.dbl_t1,
                np.minimum(
                    self.design.dbl_t2,
                    np.minimum(self.design.dbl_b1, self.design.dbl_b2),
                ),
            )
            / mm
        )  # mm
        # Longitudinal steel yield strength in base units
        fsyl = self.design.fsyl_q / MPa  # in MPa
        # Plastic hinge length based on Priestley et al. 2007
        Lp = np.round(0.08 * Ls + 0.022 * fsyl * dbl, PRECISION) * mm

        return Lp

    def _compute_yield_point(self, direction: Literal['negative', 'positive']
                             ) -> Tuple[Array3, Array3]:
        """
        Computes yield moment and curvatures about local-z axis
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
        fiy : Array3
            Yield curvature of beam in the specified `direction`.
            Computed for start, mid, end beam sections.

        References
        ----------
        Panagiotakos, T. B., & Fardis, M. N. (2001).
        Deformations of reinforced concrete members at yielding and ultimate.
        Structural Journal, 98(2), 135-148.
        """
        h = self.design.h
        b = self.design.b
        fc = self.design.fc_q
        fsyl = self.design.fsyl_q
        cover = self.design.cover_q
        nbl_b1 = self.design.nbl_b1_q
        nbl_b2 = self.design.nbl_b2_q
        dbl_b1 = self.design.dbl_b1_q
        dbl_b2 = self.design.dbl_b2_q
        nbl_t1 = self.design.nbl_t1_q
        nbl_t2 = self.design.nbl_t2_q
        dbl_t1 = self.design.dbl_t1_q
        dbl_t2 = self.design.dbl_t2_q
        dbh = self.design.dbh_q

        # Set direction dependent parameters
        if direction == 'positive':  # positive direction case
            # Longitudinal reinforcement area under tension
            As_tens = (nbl_b1 * ((0.25 * np.pi) * dbl_b1**2)
                       + nbl_b2 * ((0.25 * np.pi) * dbl_b2**2))
            # Longitudinal reinforcement area under compression
            As_comp = (nbl_t1 * ((0.25 * np.pi) * dbl_t1**2)
                       + nbl_t2 * ((0.25 * np.pi) * dbl_t2**2))
            # Dist. from concrete fiber in compression to the rebars in tension
            dd = h - cover - dbh - 0.5 * dbl_b1
        elif direction == 'negative':  # negative direction case
            # Longitudinal reinforcement area under tension
            As_tens = (nbl_t1 * ((0.25 * np.pi) * dbl_t1**2)
                       + nbl_t2 * ((0.25 * np.pi) * dbl_t2**2))
            # Longitudinal reinforcement area under compression
            As_comp = (nbl_b1 * ((0.25 * np.pi) * dbl_b1**2)
                       + nbl_b2 * ((0.25 * np.pi) * dbl_b2**2))
            # Dist. from concrete fiber in compression to the rebars in tension
            dd = h - cover - dbh - 0.5 * dbl_t1

        # Concrete crushing strain used for computing section capacity
        EPS_CU = 0.0035
        # Stress-block coefficient used to compute section capacity
        # Table 22.2.2.4.3 of ACI 318-25
        if fc < 27.6 * MPa:
            betac = 0.85
        elif fc > 55.17 * MPa:
            betac = 0.65
        else:
            betac = 1.05 - 0.05 * fc / (6.9 * MPa)
        # Concrete modulus of elasticity
        Ec = self.Ecm_q
        # Steel modulus of elasticity
        Es = self.design.Es
        nyoung = Es / Ec
        # Yield strain of steel bars
        esy = fsyl / Es
        # Distance from ext. concrete fiber (comp.) to the rebars (comp.)
        dd_prime = h - dd
        # Balanced c value: dist. to neutral axis from ext. conc. fiber (comp.)
        cb = (EPS_CU * dd) / (EPS_CU + esy)
        # Tension and compression longitudinal reinforcement ratio values
        rhol_tens = As_tens / (b * dd)
        rhol_comp = As_comp / (b * dd)
        # Compute distance to neutral axis with outer faces (simplification)
        c = (As_tens * fsyl - As_comp * fsyl) / (0.85 * fc * b * betac)
        # Decide whether yielding is controlled by tension or compression zone
        # Panagiotakos and Fardis 2001 - Equation 4 & 5
        Acomp_cntrl = rhol_tens + rhol_comp
        Atens_cntrl = rhol_tens + rhol_comp
        Bcomp_cntrl = rhol_tens + rhol_comp * (dd_prime / dd)
        Btens_cntrl = rhol_tens + rhol_comp * (dd_prime / dd)
        # Yielding is controlled by the tension steel
        control = np.ones_like(dd)
        A_to_use = Atens_cntrl
        B_to_use = Btens_cntrl
        # Yielding is controlled by the compression zone
        control[c >= cb] = 0
        A_to_use[c >= cb] = Acomp_cntrl[c >= cb]
        B_to_use[c >= cb] = Bcomp_cntrl[c >= cb]
        # The compression zone depth: Panagiotakos and Fardis 2001 - Equation 3
        ky = (
            (nyoung**2) * (A_to_use**2) + (2 * nyoung * B_to_use)
        ) ** 0.5 - nyoung * A_to_use
        # Panagiotakos and Fardis 2001 - Equation 1
        fiy1 = fsyl / (Es * (1 - ky) * dd)
        # Panagiotakos and Fardis 2001 - Equation 2
        fiy2 = (1.8 * (fc) / (Ec * ky * dd))
        # Yield curvature
        fiy = fiy1
        fiy[control == 0] = fiy2[control == 0]
        # Yield Moment: Panagiotakos and Fardis 2001 - Equation 6
        rhol_int = 0.0  # Beams do not have web-reinforcement
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
        My = (b * (dd**3)) * fiy * (term1 + term2)

        return My, fiy

    def _get_rot_hinge_props(self) -> List[Array3 | float]:
        """Compute backbone and cyclic degradation parameters defining the
        behaviour of the rotational plastic hinge about the local-z axis.

        Returns
        -------
        props : List[Array3 | float]
            Ordered list of hinge properties:

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
            14. ``pinchx`` (float) Pinching factor for deformation during
            reloading.
            15. ``pinchy`` (float) Pinching factor for force during reloading.
            16. ``damage1`` (float) Ductility-based damage parameter.
            17. ``damage2`` (float) Energy-based damage parameter.
            18. ``beta`` (float) Unloading stiffness degradation exponent.

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

        Dolšek, M. and Fajfar, P. (2005). Post-test analyses of the SPEAR test
        building. University of Ljubljana.
        """
        h = self.design.h
        ln = self.design.L
        fc_mpa = self.design.fc_q / MPa
        fsyl_mpa = self.design.fsyl_q / MPa
        dbl_t1 = self.design.dbl_t1_q
        sbh = self.design.sbh_q
        rhol = self.rhol_q
        rhoh = self.rhoh_y_q

        # Shear span, assuming equal to 50% of the free length of the element
        ls = ln / 2  # NOTE: Could be varied with intensity of loading, but ok.
        niu = 0.0  # Axial load ratio, assuming beams do not have any
        # Post-yield hardening stiffness - Haselton et al. 2008 - Equation 3.17
        Mc_My = 1.25 * (0.89**niu) * (0.91 ** (0.01 * fc_mpa))
        #  Residual strength to capping strength ratio - assumed
        Mr_Mc = 0.1  # 10%
        # Reinforcing bar buckling coefficient, by Dhakal and Maekawa 2002
        sn = (sbh[0] / dbl_t1) * (fsyl_mpa / 100) ** 0.5
        # Shear cracking is expected to precede flexural yield EC8-3 pp 41
        av = 1.0
        z = 0.9 * (0.9 * h)  # lever arm
        # NOTE: av.z is the tension shift of the bending diagram see:
        # EN 1992-1-1: 2004, 9.2.1.3(2)

        # Compute yield moments in positive and negative directions at both
        # end sections of the beam (i and j) - Panagiotakos and Fardis (2001)
        My_neg, phiy_neg = self._compute_yield_point('negative')
        My_pos, phiy_pos = self._compute_yield_point('positive')
        # Maximum moment capacity
        Mc_neg = Mc_My * My_neg
        Mc_pos = Mc_My * My_pos
        # Residual moment capacity
        Mr_neg = Mr_Mc * Mc_neg
        Mr_pos = Mr_Mc * Mc_pos

        # Plastic Rotation capacity by Haselton et al. 2016 - Equation 5
        c_u = 1.0  # Unit conversion coefficient 1.0 for MPa, 6.9 for ksi
        theta_cap_pl_pos = (
            0.12
            * (1 + 0.55 * self.bondslip_factor)
            * (0.16**niu)
            * ((0.02 + 40 * rhoh) ** 0.43)
            * (0.54 ** (0.01 * c_u * fc_mpa))
            * (0.66 ** (0.1 * sn))
            * (2.27 ** (10.0 * rhol))
        )
        # Non-symmetric beam section - Equation 7
        # NOTE: This is different than MATLAB implementation
        ratio_pos_neg = (
            np.maximum(0.01, fsyl_mpa * self.rhol_top_q / fc_mpa)
            / np.maximum(0.01, fsyl_mpa * self.rhol_bot_q / fc_mpa)
        ) ** 0.225
        theta_cap_pl_neg = ratio_pos_neg * theta_cap_pl_pos
        # Post-capping rotation capacity by Haselton et al. 2016 - Equation 8
        theta_pc_neg = 0.76 * (0.031**niu) * ((0.02 + 40 * rhoh) ** 1.02)
        theta_pc_neg[theta_pc_neg >= 0.10] = 0.10
        theta_pc_pos = 0.76 * (0.031**niu) * ((0.02 + 40 * rhoh) ** 1.02)
        theta_pc_pos[theta_pc_pos >= 0.10] = 0.10

        # Yield rotation capacity - EN 1998-3:2004 - Equation A.10b
        theta_y1_neg = phiy_neg * ((ls + (av * z)) / 3)
        theta_y1_pos = phiy_pos * ((ls + (av * z)) / 3)
        theta_y2 = 0.0014 * (1 + 1.5 * h / ls)
        theta_y3_neg = 0.125 * phiy_neg * dbl_t1 * (fsyl_mpa / (fc_mpa**0.50))
        theta_y3_pos = 0.125 * phiy_pos * dbl_t1 * (fsyl_mpa / (fc_mpa**0.50))
        theta_y_neg = (
            theta_y1_neg + theta_y2 + self.bondslip_factor * theta_y3_neg
        )
        theta_y_pos = (
            theta_y1_pos + theta_y2 + self.bondslip_factor * theta_y3_pos
        )

        # Rotation values needs to be adjusted for cyclic loading
        if self.cyclic_model:  # Haselton et al. 2016
            theta_cap_pl_pos = 0.7 * theta_cap_pl_pos  # Equation (12)
            theta_cap_pl_neg = 0.7 * theta_cap_pl_neg  # Equation (12)
            theta_pc_pos = 0.5 * theta_pc_pos  # Equation (13)
            theta_pc_neg = 0.5 * theta_pc_neg  # Equation (13)

        # Pinching factor for strain (or deformation) during reloading
        pinchx = 0.8  # no pinching (default)
        # Pinching factor for stress (or force) during reloading
        pinchy = 0.2  # no pinching (default)
        # Damage due to ductility: D1(mu-1)
        damage1 = 0.0  # no degradation (default)
        # Damage due to energy: D2(Eii/Eult)
        damage2 = 0.0  # no degradation (default)
        # Power used to determine the degraded unloading stiffness based on
        # ductility, mu-beta (optional, default=0.0)
        beta = 0.85  # from Dolšek and Fajfar 2005

        # The negative ones are based on top (compression) reinforcement
        # The positive ones are based on bottom (tension) renforcement
        props = [
            phiy_neg, My_neg, Mc_neg, Mr_neg,
            theta_y_neg, theta_cap_pl_neg, theta_pc_neg,
            phiy_pos, My_pos, Mc_pos, Mr_pos,
            theta_y_pos, theta_cap_pl_pos, theta_pc_pos,
            pinchx, pinchy, damage1, damage2, beta,
        ]

        return props

    def _set_cracked_section_properties(self) -> None:
        """
        Compute and store cracked-section (effective) flexural properties
        about local z.

        The method assembles a layered longitudinal-reinforcement model for
        the (i-end) rectangular section using the detailing stored in
        ``self.design`` (cover, stirrup diameter, bar diameters and counts).
        It then calls ``get_moments`` to obtain the yield moment ``My`` and
        yield curvature ``phi_y`` for bending about the local z-axis under
        zero external axial load (``Pext = 0.0``). From these, it computes the
        effective flexural rigidity ``EIeff = My / phi_y`` and the
        corresponding effective second moment of area ``Ieff = EIeff / Ec``.

        The computed effective inertia is stored as ``self._Iz_eff`` for later
        use.

        Notes
        -----
        - Reinforcement layers are created from the top and bottom bar groups
          (t2, t1, b1, b2) and sorted by depth from the top fiber.
        - This implementation currently uses only the i-end section
        - Axial load is neglected in the moment-curvature calculation.

        See Also
        --------
        `get_moments`: Computes cracking/yield moments and associated curvature
        quantities for a layered reinforced-concrete section.
        """
        # Section properties
        h = self.design.h
        b = self.design.b
        fc = float(self.design.fc_q)
        fsyl = float(self.design.fsyl_q)
        Es = self.design.steel.Es
        Ec = float(self.Ecm_q)
        cv = float(self.design.cover_q)

        # Effective moment of inertia values for end sections
        Ieffs = []
        for idx in [0, 2]:
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

            # Reinforcement layout (top to bottom)
            yt1 = cv + dbh + dbl_t1 / 2
            yt2 = cv + dbh + dbl_t2 / 2
            yb1 = h - (cv + dbh + dbl_b1 / 2)
            yb2 = h - (cv + dbh + dbl_b2 / 2)
            # Reinforcement area per layer (top to bottom)
            Ab_t1 = 0.25*np.pi*dbl_t1**2
            Ab_t2 = 0.25*np.pi*dbl_t2**2
            As_t1 = nbl_t1 * Ab_t1
            As_t2 = nbl_t2 * Ab_t2
            Ab_b1 = 0.25*np.pi*dbl_b1**2
            Ab_b2 = 0.25*np.pi*dbl_b2**2
            As_b1 = nbl_b1 * Ab_b1
            As_b2 = nbl_b2 * Ab_b2
            # Set the layer distances and total areas
            y_layers = [yt2, yt1, yb1, yb2]
            As_layers = [As_t2, As_t1, As_b1, As_b2]
            # Sort the distances in ascending order
            y_layers, As_layers = map(list, zip(
                *sorted(zip(y_layers, As_layers))))
            # Cracking and yield moments (positive direction)
            _, _, _, My, phi_y, _ = get_moments(
                h=h, b=b, fc=fc, Ec=Ec,
                Pext=0.0, fyL=fsyl, Es=Es,
                As_layers=As_layers,
                y_layers=y_layers,
            )
            # Save effective moment inertia for elastic section
            Ieffs.append(float(My / (phi_y * Ec)))

        # Compute the average from two ends
        self._Iz_eff = sum(Ieffs) / len(Ieffs)
