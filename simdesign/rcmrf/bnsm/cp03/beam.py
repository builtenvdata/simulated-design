"""This module provides the beam class implementation for the ``CP03`` model in
the BNSM layer.
"""
# Imports from installed packages
import openseespy.opensees as ops
from typing import Tuple, List

# Imports from bnsm base library
from ..baselib.beam import BeamBase, HYSTERETIC_PARAMETERS
from ..baselib.node import Node
from ..baselib.constants import RIGID_MAT, LINEAR_TRANSF_X, LINEAR_TRANSF_Y
from ..cp01.column import STIFF_INTERIOR_FACTOR

# Imports from utils library
from ....utils.misc import round_list
from ....utils.tags import element_end_node_tag


class Beam(BeamBase):
    """Beam implementation for the ``CP03`` model.

    The beam is modeled based on a concentrated plasticity approach.
    An elastic interior member (``elasticBeamColumn``) is connected to
    nonlinear rotational hinges at both ends. Each hinge is implemented
    as a ``zeroLength`` element between the original beam-end node and an
    auxiliary element node.

    The hinge response is defined by a uniaxial ``Hysteretic`` material
    assigned to the rotational degree of freedom about the local z-axis.
    All other translational and rotational degrees of freedom across the
    hinge are constrained to behave rigidly using rigid materials, so the
    hinge represents concentrated flexural nonlinearity.

    The hinge backbone rotations are chord rotations of the whole member
    (the yield rotation includes the elastic deformations), so the elastic
    member is nearly rigid in flexure about local-z
    (``STIFF_INTERIOR_FACTOR``) and the hinges carry the whole flexural
    flexibility.

    Attributes
    ----------
    hinge_node_i : Node
        Auxiliary node at the start of the beam used to define the plastic
        hinge.
    hinge_node_j : Node
        Auxiliary node at the end of the beam used to define the plastic
        hinge.

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.baselib.beam.BeamBase`
        Base beam definition extended by this class.
    """

    hinge_node_i: Node
    hinge_node_j: Node

    @property
    def hinge_i_tag(self) -> int:
        """
        Returns
        -------
        int
            Node tag used as the identifier for the *i-end* hinge
            material/element.
        """
        return self.ele_node_i.tag

    @property
    def hinge_j_tag(self) -> int:
        """
        Returns
        -------
        int
            Node tag used as the identifier for the *j-end* hinge
            material/element.
        """
        return self.ele_node_j.tag

    def set_ele_node_i(self) -> None:
        """Initialize the *i-end* elastic element node.
        """
        coords = self.hinge_node_i.coordinates.copy()
        tag = element_end_node_tag(self.hinge_node_i.tag)
        self.ele_node_i = Node(tag, coords)

    def set_ele_node_j(self) -> None:
        """Initialize the *j-end* elastic element node.
        """
        coords = self.hinge_node_j.coordinates.copy()
        tag = element_end_node_tag(self.hinge_node_j.tag)
        self.ele_node_j = Node(tag, coords)

    def add_to_ops(self) -> None:
        """Adds beam components to the OpenSees domain
        (i.e, plastic hinges, elastic beam element and nodes).
        """
        # Create beam element nodes
        self.ele_node_i.add_to_ops()
        self.ele_node_j.add_to_ops()

        # Create elastic beam element
        elastic_ele_inputs = self._get_elastic_ele_inputs()
        ops.element(*elastic_ele_inputs)

        # Create plastic hinge materials
        hinge_i_mat_inputs, hinge_j_mat_inputs = self._get_mz_mat_inputs()
        ops.uniaxialMaterial(*hinge_i_mat_inputs)
        ops.uniaxialMaterial(*hinge_j_mat_inputs)

        # Create plastic hinge elements
        hinge_i_ele_inputs, hinge_j_ele_inputs = self._get_hinge_ele_inputs()
        ops.element(*hinge_i_ele_inputs)
        ops.element(*hinge_j_ele_inputs)

    def to_py(self) -> List[str]:
        """Gets the Python commands to construct beam components in OpenSees
        domain (i.e, plastic hinges, elastic beam element and nodes).

        Returns
        -------
        List[str]
            List of Python commands for constructing the components of beam
            object in OpenSees.
        """
        # Create beam element nodes
        content = ['# Create elastic beam element nodes']
        content.append(self.ele_node_i.to_py())
        content.append(self.ele_node_j.to_py())

        # Create elastic beam element
        content.append('# Create elastic beam element')
        elastic_ele_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_elastic_ele_inputs()
        )
        content.append(f"ops.element({elastic_ele_inputs})")

        # Create plastic hinge materials
        content.append('# Create plastic hinge materials')
        hinge_i_mat_inputs, hinge_j_mat_inputs = self._get_mz_mat_inputs()
        hinge_i_mat_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in hinge_i_mat_inputs
        )
        hinge_j_mat_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in hinge_j_mat_inputs
        )
        content.append(f"ops.uniaxialMaterial({hinge_i_mat_inputs})")
        content.append(f"ops.uniaxialMaterial({hinge_j_mat_inputs})")

        # Create plastic hinge elements
        content.append('# Create plastic hinge elements')
        hinge_i_ele_inputs, hinge_j_ele_inputs = self._get_hinge_ele_inputs()
        hinge_i_ele_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in hinge_i_ele_inputs
        )
        hinge_j_ele_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in hinge_j_ele_inputs
        )
        content.append(f"ops.element({hinge_i_ele_inputs})")
        content.append(f"ops.element({hinge_j_ele_inputs})")

        return content

    def to_tcl(self) -> List[str]:
        """Gets the Tcl commands to construct beam components in OpenSees
        domain (i.e, plastic hinges, elastic beam element and nodes).

        Returns
        -------
        List[str]
            List of Tcl commands for constructing the components of beam
            object in OpenSees.
        """
        # Create beam element nodes
        content = ['# Create elastic beam element nodes']
        content.append(self.ele_node_i.to_tcl())
        content.append(self.ele_node_j.to_tcl())

        # Create elastic beam element
        content.append('# Create elastic beam element')
        elastic_ele_inputs = ' '.join(
            f'{item}' for item in self._get_elastic_ele_inputs()
        )
        content.append(f"element {elastic_ele_inputs}")

        # Create plastic hinge materials
        content.append('# Create plastic hinge materials')
        hinge_i_mat_inputs, hinge_j_mat_inputs = self._get_mz_mat_inputs()
        hinge_i_mat_inputs = ' '.join(f"{item}" for item in hinge_i_mat_inputs)
        hinge_j_mat_inputs = ' '.join(f"{item}" for item in hinge_j_mat_inputs)
        content.append(f"uniaxialMaterial {hinge_i_mat_inputs}")
        content.append(f"uniaxialMaterial {hinge_j_mat_inputs}")

        # Create plastic hinge elements
        content.append('# Create plastic hinge elements')
        hinge_i_ele_inputs, hinge_j_ele_inputs = self._get_hinge_ele_inputs()
        hinge_i_ele_inputs = ' '.join(f"{item}" for item in hinge_i_ele_inputs)
        hinge_j_ele_inputs = ' '.join(f"{item}" for item in hinge_j_ele_inputs)
        content.append(f"element {hinge_i_ele_inputs}")
        content.append(f"element {hinge_j_ele_inputs}")

        return content

    def _get_hinge_ele_inputs(self) -> Tuple[List[str | float | int],
                                             List[str | float | int]]:
        """Retrieves plastic hinge element inputs (zero-length spring).

        Returns
        -------
        hinge_i_ele_inputs : List[str | float | int]
            Element inputs for the hinge at the start section.
        hinge_j_ele_inputs : List[str | float | int]
            Element inputs for the hinge at the end section.
        """
        # Nodes
        hinge_i_nodes = [self.hinge_node_i.tag, self.ele_node_i.tag]
        hinge_j_nodes = [self.ele_node_j.tag, self.hinge_node_j.tag]
        # Orientation: rotation about local y (dir 5) is positive under
        # sagging (bottom fibres in tension), consistent with the positive
        # branch of the hinge material (My_pos)
        if self.design.direction == 'x':
            vecx = [1.0, 0.0, 0.0]
            vecyp = [0.0, -1.0, 0.0]
            # cross product is vecz = [0, 0, -1]
        elif self.design.direction == 'y':
            vecx = [0.0, 1.0, 0.0]
            vecyp = [1.0, 0.0, 0.0]
            # cross product is vecz = [0, 0, -1]
        orientation = [*vecx, *vecyp]
        # Uniaxial Materials
        hinge_i_mats = [RIGID_MAT, RIGID_MAT, RIGID_MAT,
                        RIGID_MAT, self.mz_i_mat_tag, RIGID_MAT]
        hinge_j_mats = [RIGID_MAT, RIGID_MAT, RIGID_MAT,
                        RIGID_MAT, self.mz_j_mat_tag, RIGID_MAT]
        mat_dirs = [1, 2, 3, 4, 5, 6]
        # Element inputs
        hinge_i_inputs = [
            'zeroLength', self.hinge_i_tag, *hinge_i_nodes,
            '-mat', *hinge_i_mats, '-dir', *mat_dirs,
            '-orient', *orientation
        ]
        hinge_j_inputs = [
            'zeroLength', self.hinge_j_tag, *hinge_j_nodes,
            '-mat', *hinge_j_mats, '-dir', *mat_dirs,
            '-orient', *orientation
        ]
        return hinge_i_inputs, hinge_j_inputs

    def _get_mz_mat_inputs(self) -> Tuple[List[str | float | int],
                                          List[str | float | int]]:
        """Retrieves the material inputs defining the flexural behaviour
        around local-z for the plastic hinge.

        Returns
        -------
        hinge_i_mat_inputs : List[str | float | int]
            Hysteretic material model inputs for hinge at the start section.
        hinge_j_mat_inputs : List[str | float | int]
            Hysteretic material model inputs for hinge at the end section.
        """
        # Backbone of the plastic hinges
        (
            _, My_neg, Mc_neg, Mr_neg,
            theta_y_neg, theta_cap_pl_neg, theta_pc_neg,
            _, My_pos, Mc_pos, Mr_pos,
            theta_y_pos, theta_cap_pl_pos, theta_pc_pos,
        ) = self._get_rot_hinge_props()

        # Rotation values for monotonic loading.
        theta_1_neg = theta_y_neg
        theta_2_neg = theta_1_neg + theta_cap_pl_neg
        theta_3_neg = theta_2_neg + theta_pc_neg
        theta_1_pos = theta_y_pos
        theta_2_pos = theta_1_pos + theta_cap_pl_pos
        theta_3_pos = theta_2_pos + theta_pc_pos

        # Material inputs
        hinge_i_mat_inputs = [
            'Hysteretic', self.mz_i_mat_tag,
            My_pos[0], theta_1_pos[0],
            Mc_pos[0], theta_2_pos[0],
            Mr_pos[0], theta_3_pos[0],
            -My_neg[0], -theta_1_neg[0],
            -Mc_neg[0], -theta_2_neg[0],
            -Mr_neg[0], -theta_3_neg[0],
            *HYSTERETIC_PARAMETERS
        ]
        hinge_j_mat_inputs = [
            'Hysteretic', self.mz_j_mat_tag,
            My_pos[-1], theta_1_pos[-1],
            Mc_pos[-1], theta_2_pos[-1],
            Mr_pos[-1], theta_3_pos[-1],
            -My_neg[-1], -theta_1_neg[-1],
            -Mc_neg[-1], -theta_2_neg[-1],
            -Mr_neg[-1], -theta_3_neg[-1],
            *HYSTERETIC_PARAMETERS
        ]

        # Rounding to precision
        hinge_i_mat_inputs = round_list(hinge_i_mat_inputs)
        hinge_j_mat_inputs = round_list(hinge_j_mat_inputs)

        return hinge_i_mat_inputs, hinge_j_mat_inputs

    def _get_elastic_ele_inputs(self) -> List[str | float | int]:
        """Retrieves elastic beam element inputs.

        Returns
        -------
        List[str | float | int]
            List of elastic beam element inputs.

        Notes
        -----
        The moment of inertia about local-z (Iz) is multiplied by
        ``STIFF_INTERIOR_FACTOR``, since the hinges carry the whole flexural
        flexibility. The weak-axis flexure (Iy) has no hinge and keeps its
        elastic stiffness.
        """
        # Check if cracked section is being used or not
        if self.cracked:
            Iz = self._Iz_eff
        else:
            Iz = self.design.Iz
        # Nearly rigid in flexure about local-z
        Iz = Iz * STIFF_INTERIOR_FACTOR

        # List of elasticBeamColumn element inputs
        ele_inputs = [
            'elasticBeamColumn', self.ele_tag,
            self.ele_node_i.tag, self.ele_node_j.tag,
            self.design.Ag, self.Ecm_q, self.Gcm_q,
            self.design.J, self.design.Iy, Iz
        ]
        # Append geometric transformation
        if self.design.direction == 'x':
            ele_inputs.append(LINEAR_TRANSF_X)
        elif self.design.direction == 'y':
            ele_inputs.append(LINEAR_TRANSF_Y)

        # Rounding to precision
        ele_inputs = round_list(ele_inputs)

        return ele_inputs
