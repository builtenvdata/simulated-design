"""This module provides the joint class implementations for the ``CP03`` model
in the BNSM layer.
"""
# Imports from installed packages
import openseespy.opensees as ops
from typing import Dict, List, Literal

# Imports from bnsm base library
from ..baselib.joint import StairsJointBase, FloorJointBase, JointDesign
from ..baselib.node import Node
from ..baselib.constants import (
    RIGID_SEC, LINEAR_TRANSF_X, LINEAR_TRANSF_Y, LINEAR_TRANSF_Z
)


class StairsJoint(StairsJointBase):
    """Stairs joint implementation for the ``CP03`` model.

    Represents a beam-column joint located at an intermediate (mid-storey)
    level associated with staircase framing.

    This class extends ``StairsJointBase`` by creating rigid offset nodes
    around the joint center and connecting them to the center joint node using
    rigid-like ``elasticBeamColumn`` elements.

    Offset directions:
    - left/right nodes: along global X (beam offsets)
    - bottom/top nodes: along global Z (column offsets)

    Attributes
    ----------
    left_node : Node | None
        The left offset joint node along global X (created only if the
        corresponding left beam exists).
    right_node : Node | None
        The right offset joint node along global X (created only if the
        corresponding right beam exists).
    bottom_node : Node | None
        The bottom offset joint node along global Z (created only if the
        corresponding vottom beam exists).
    top_node : Node | None
        The top offset joint node along global Z (created only if the
        corresponding top beam exists).
    rigid_ele : list[int]
        Element tags of the rigid-like offset links.

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.baselib.joint.StairsJointBase`
        Base stairs joint definition extended by this class.
    """
    left_node: Node | None
    right_node: Node | None
    bottom_node: Node | None
    top_node: Node | None
    rigid_ele: List[int]

    def __init__(self, design: JointDesign, mass: float) -> None:
        """Initialize StairsJoint object.

        Parameters
        ----------
        design : JointDesign
            Reference design information of joint.
        mass : float
            Total mass assigned to joint.
        """
        # Store rigid-like element tags
        self.rigid_ele = []
        # Save reference design information of joint
        self.design = design
        # Set reference node properties
        ref_point = self.design.elastic_node
        ref_tag = ref_point.tag
        ref_coords = ref_point.coordinates
        # Initialize center node
        masses = [mass, mass, mass, 0.0, 0.0, 0.0]
        self.center_node = Node(ref_tag, ref_coords, masses)
        # Initialize rigid offsets nodes
        if self.design.bottom_column:  # bottom
            coords = ref_coords.copy()
            coords[2] -= self.h / 2
            self.bottom_node = Node(ref_tag + 20000, coords)
        else:
            self.bottom_node = None
        if self.design.right_beam:  # right
            coords = ref_coords.copy()
            coords[0] += self.bx / 2
            self.right_node = Node(ref_tag + 30000, coords)
        else:
            self.right_node = None
        if self.design.left_beam:  # left
            coords = ref_coords.copy()
            coords[0] -= self.bx / 2
            self.left_node = Node(ref_tag + 50000, coords)
        else:
            self.left_node = None
        if self.design.top_column:  # top
            coords = ref_coords.copy()
            coords[2] += self.h / 2
            self.top_node = Node(ref_tag + 70000, coords)
        else:
            self.top_node = None

    def add_to_ops(self) -> None:
        """Adds stairs joint model objects to the OpenSees domain (i.e,
        rigid joint offsets elements and nodes).
        """
        # Central joint node
        self.center_node.add_to_ops()
        # Rigid-joint offset elements
        if self.left_node:
            self.left_node.add_to_ops()
            ele_nodes = [self.left_node.tag, self.center_node.tag]
            ele_tag = self.left_node.tag
            ops.element('elasticBeamColumn', ele_tag, *ele_nodes,
                        RIGID_SEC, LINEAR_TRANSF_X)
            self.rigid_ele.append(ele_tag)
        if self.right_node:
            self.right_node.add_to_ops()
            ele_nodes = [self.center_node.tag, self.right_node.tag]
            ele_tag = self.right_node.tag
            ops.element('elasticBeamColumn', ele_tag, *ele_nodes,
                        RIGID_SEC, LINEAR_TRANSF_X)
            self.rigid_ele.append(ele_tag)
        if self.bottom_node:
            self.bottom_node.add_to_ops()
            ele_nodes = [self.bottom_node.tag, self.center_node.tag]
            ele_tag = self.bottom_node.tag
            ops.element('elasticBeamColumn', ele_tag, *ele_nodes,
                        RIGID_SEC, LINEAR_TRANSF_Z)
            self.rigid_ele.append(ele_tag)
        if self.top_node:
            self.top_node.add_to_ops()
            ele_nodes = [self.center_node.tag, self.top_node.tag]
            ele_tag = self.top_node.tag
            ops.element('elasticBeamColumn', ele_tag, *ele_nodes,
                        RIGID_SEC, LINEAR_TRANSF_Z)
            self.rigid_ele.append(ele_tag)

    def to_py(self) -> List[str]:
        """Gets the Python commands to define stairs joint model objects in
        the OpenSees domain (i.e, rigid joint offsets elements and nodes).

        Returns
        -------
        list[str]
            List of Python commands for constructing the components of stairs
            joint in OpenSees.
        """
        grids = ', '.join([f"{i}" for i in self.design.elastic_node.grid_ids])
        content = [f'# Joint grid ids (x, y, z): ({grids})']
        content.append("# Central joint node")
        content.append(self.center_node.to_py())
        content.append("# Rigid-joint offset elements")
        if self.left_node:
            content.append(self.left_node.to_py())
            ele_nodes = f"{self.left_node.tag}, {self.center_node.tag}"
            ele_tag = self.left_node.tag
            content.append(
                f"ops.element('elasticBeamColumn', {ele_tag}, {ele_nodes}, "
                f"{RIGID_SEC}, {LINEAR_TRANSF_X})"
            )
        if self.right_node:
            content.append(self.right_node.to_py())
            ele_nodes = f"{self.center_node.tag}, {self.right_node.tag}"
            ele_tag = self.right_node.tag
            content.append(
                f"ops.element('elasticBeamColumn', {ele_tag}, {ele_nodes}, "
                f"{RIGID_SEC}, {LINEAR_TRANSF_X})"
            )
        if self.bottom_node:
            content.append(self.bottom_node.to_py())
            ele_nodes = f"{self.bottom_node.tag}, {self.center_node.tag}"
            ele_tag = self.bottom_node.tag
            content.append(
                f"ops.element('elasticBeamColumn', {ele_tag}, {ele_nodes}, "
                f"{RIGID_SEC}, {LINEAR_TRANSF_Z})"
            )
        if self.top_node:
            content.append(self.top_node.to_py())
            ele_nodes = f"{self.center_node.tag}, {self.top_node.tag}"
            ele_tag = self.top_node.tag
            content.append(
                f"ops.element('elasticBeamColumn', {ele_tag}, {ele_nodes}, "
                f"{RIGID_SEC}, {LINEAR_TRANSF_Z})"
            )

        return content

    def to_tcl(self) -> List[str]:
        """Gets the Tcl commands to define stairs joint model objects in
        the OpenSees domain (i.e, rigid joint offsets elements and nodes).

        Returns
        -------
        list[str]
            List of Tcl commands for constructing the components of stairs
            joint in OpenSees.
        """
        grids = ', '.join([f"{i}" for i in self.design.elastic_node.grid_ids])
        content = [f'# Joint grid ids (x, y, z): ({grids})']
        content.append("# Central joint node")
        content.append(self.center_node.to_tcl())
        content.append("# Rigid-joint offset elements")
        if self.left_node:
            content.append(self.left_node.to_tcl())
            ele_nodes = f"{self.left_node.tag} {self.center_node.tag}"
            ele_tag = self.left_node.tag
            content.append(
                f"element elasticBeamColumn {ele_tag} {ele_nodes} "
                f"{RIGID_SEC} {LINEAR_TRANSF_X}"
            )
        if self.right_node:
            content.append(self.right_node.to_tcl())
            ele_nodes = f"{self.center_node.tag} {self.right_node.tag}"
            ele_tag = self.right_node.tag
            content.append(
                f"element elasticBeamColumn {ele_tag} {ele_nodes} "
                f"{RIGID_SEC} {LINEAR_TRANSF_X}"
            )
        if self.bottom_node:
            content.append(self.bottom_node.to_tcl())
            ele_nodes = f"{self.bottom_node.tag} {self.center_node.tag}"
            ele_tag = self.bottom_node.tag
            content.append(
                f"element elasticBeamColumn {ele_tag} {ele_nodes} "
                f"{RIGID_SEC} {LINEAR_TRANSF_Z}"
            )
        if self.top_node:
            content.append(self.top_node.to_tcl())
            ele_nodes = f"{self.center_node.tag} {self.top_node.tag}"
            ele_tag = self.top_node.tag
            content.append(
                f"element elasticBeamColumn {ele_tag} {ele_nodes} "
                f"{RIGID_SEC} {LINEAR_TRANSF_Z}"
            )

        return content


class FloorJoint(FloorJointBase, StairsJoint):
    """Floor joint implementation for the ``CP03`` model.

    Represents a beam-column joint located at a floor level.

    This class combines:

    - rigid offset modelling (center node + rigid-like offset links), and
    - an optional joint-flexibility element (rigid/elastic/inelastic) between
      the joint center node and the floor diaphragm-constrained node.

    In addition to the X- and Z-direction offsets, this class also creates
    front/rear offset nodes along global Y (if the corresponding beams exist)
    and connects them to the joint center node using rigid-like
    ``elasticBeamColumn`` elements.

    Attributes
    ----------
    rear_node : Node | None
        The rear offset joint node along global Y-axis (created only if the
        corresponding rear beam exists).
    front_node : Node | None
        The front offset joint node along global Y-axis (created only if the
        corresponding front beam exists).

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.baselib.joint.FloorJointBase`
        Base floor joint class from which beam-column joint model is inherited.
    :class:`~simdesign.rcmrf.bnsm.cp03.joint.StairsJoint`
        Stairs joint class extended by this class to define rigid offsets.
    """
    rear_node: Node | None
    front_node: Node | None

    def __init__(self, design: JointDesign, mass: float,
                 model: Literal["inelastic", "elastic", "rigid"],
                 load_factors: Dict[Literal['G', 'Q'], float]) -> None:
        """Initialize FloorJoint object.

        Parameters
        ----------
        design : JointDesign
            Reference design information of joint.
        mass : float
            Total mass assigned to joint.
        model : {"inelastic", "elastic", "rigid"}
            Joint flexibility model.
        load_factors : dict[{'G', 'Q'}, float]
            Load factors used to compute axial load on joint.
        """
        # Save joint flexibility model option
        self.flexibility_model = model
        # Initialize the nodes in stairs joint
        super(FloorJointBase, self).__init__(design, mass)
        # Initialize the floor node to account for joint flexibility
        ref_point = self.design.elastic_node
        # Set the joint node constrained by the floor diaphragm
        if model == 'rigid':
            # There is no need to create additional joint node
            self.floor_node = self.center_node
        else:
            # Initialize the new node to account for joint flexibility
            self.floor_node = Node(ref_point.tag + 10000,
                                   ref_point.coordinates)
        # Initialize rigid offsets (in Y) nodes
        if self.design.front_beam:  # front
            coords = ref_point.coordinates.copy()
            coords[1] += self.by / 2
            self.front_node = Node(ref_point.tag + 40000, coords)
        else:
            self.front_node = None
        if self.design.rear_beam:  # rear
            coords = ref_point.coordinates.copy()
            coords[1] -= self.by / 2
            self.rear_node = Node(ref_point.tag + 60000, coords)
        else:
            self.rear_node = None
        # Axial force on the joint
        if self.design.bottom_column:
            # forces = (
            #     load_factors['G'] *
            #     self.design.bottom_column.forces['G/seismic'] +
            #     load_factors['Q'] *
            #     self.design.bottom_column.forces['Q/seismic']
            # )
            # self.axial_load = -forces.N9
            self.axial_force = (
                load_factors['G'] * self.design.bottom_column.hinge_Ng
                + load_factors['Q'] * self.design.bottom_column.hinge_Nq
            )
        else:
            raise ValueError(
                "Bottom column is missing, joint model won't work here.")

    def add_to_ops(self) -> None:
        """Adds floor joint model objects to the OpenSees domain (i.e, rigid
        joint offsets elements, nodes and joint flexibility element).
        """
        super(FloorJointBase, self).add_to_ops()
        # Rigid-joint offset elements along Y
        if self.rear_node:
            self.rear_node.add_to_ops()
            ele_nodes = [self.rear_node.tag, self.center_node.tag]
            ele_tag = self.rear_node.tag
            ops.element('elasticBeamColumn', ele_tag, *ele_nodes,
                        RIGID_SEC, LINEAR_TRANSF_Y)
            self.rigid_ele.append(ele_tag)
        if self.front_node:
            self.front_node.add_to_ops()
            ele_nodes = [self.center_node.tag, self.front_node.tag]
            ele_tag = self.front_node.tag
            ops.element('elasticBeamColumn', ele_tag, *ele_nodes,
                        RIGID_SEC, LINEAR_TRANSF_Y)
            self.rigid_ele.append(ele_tag)

        # Add joint flexibility element for no-rigid joint cases
        if self.flexibility_model != 'rigid':
            # Add floor joint node constrained by the floor diaphragm
            self.floor_node.add_to_ops()
            # Materials defining flexible rotation behaviour
            ops.uniaxialMaterial(*self._get_mat_inputs('X'))
            ops.uniaxialMaterial(*self._get_mat_inputs('Y'))
            # Create the new section with flexible rotation behaviour
            ops.section(*self._get_agg_sec_inputs())
            # Create the joint flexibility element
            ops.element(*self._get_ele_inputs())

    def to_py(self) -> List[str]:
        """Gets the Python commands to define floor joint model objects in
        the OpenSees domain (i.e, rigid joint offsets elements, nodes and joint
        flexibility element).

        Returns
        -------
        list[str]
            List of Python commands for constructing the components of floor
            joint in OpenSees.
        """
        content = super(FloorJointBase, self).to_py()
        # Rigid-joint offset elements along Y
        if self.rear_node:
            content.append(self.rear_node.to_py())
            ele_nodes = f"{self.rear_node.tag}, {self.center_node.tag}"
            ele_tag = self.rear_node.tag
            content.append(
                f"ops.element('elasticBeamColumn', {ele_tag}, {ele_nodes}, "
                f"{RIGID_SEC}, {LINEAR_TRANSF_Y})"
            )
        if self.front_node:
            content.append(self.front_node.to_py())
            ele_nodes = f"{self.center_node.tag}, {self.front_node.tag}"
            ele_tag = self.front_node.tag
            content.append(
                f"ops.element('elasticBeamColumn', {ele_tag}, {ele_nodes}, "
                f"{RIGID_SEC}, {LINEAR_TRANSF_Y})"
            )

        content.append(f"# Joint flexibility model: {self.flexibility_model}")
        # Add joint flexibility element for no-rigid joint cases
        if self.flexibility_model != 'rigid':
            # Add floor joint node constrained by the floor diaphragm
            note = ' # Constrained floor node'
            content.append(self.floor_node.to_py() + note)
            # Materials defining flexible rotation behaviour
            mz_mat_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in self._get_mat_inputs('X')
            )
            my_mat_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in self._get_mat_inputs('Y')
            )
            content.append(f"ops.uniaxialMaterial({mz_mat_inputs})")
            content.append(f"ops.uniaxialMaterial({my_mat_inputs})")
            # Create the new section with flexible rotation behaviour
            sec_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in self._get_agg_sec_inputs()
            )
            content.append(f"ops.section({sec_inputs})")
            # Create the joint flexibility element
            ele_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in self._get_ele_inputs()
            )
            content.append(f"ops.element({ele_inputs})")

        return content

    def to_tcl(self) -> List[str]:
        """Gets the Tcl commands to define floor joint model objects in
        the OpenSees domain (i.e, rigid joint offsets elements, nodes and joint
        flexibility element).

        Returns
        -------
        list[str]
            List of Tcl commands for constructing the components of floor
            joint in OpenSees.
        """
        content = super(FloorJointBase, self).to_tcl()
        # Rigid-joint offset elements along Y
        if self.rear_node:
            content.append(self.rear_node.to_tcl())
            ele_nodes = f"{self.rear_node.tag} {self.center_node.tag}"
            ele_tag = self.rear_node.tag
            content.append(
                f"element elasticBeamColumn {ele_tag} {ele_nodes} "
                f"{RIGID_SEC} {LINEAR_TRANSF_Y}"
            )
        if self.front_node:
            content.append(self.front_node.to_tcl())
            ele_nodes = f"{self.center_node.tag} {self.front_node.tag}"
            ele_tag = self.front_node.tag
            content.append(
                f"element elasticBeamColumn {ele_tag} {ele_nodes} "
                f"{RIGID_SEC} {LINEAR_TRANSF_Y}"
            )

        content.append(f"# Joint flexibility model: {self.flexibility_model}")
        # Add joint flexibility element for no-rigid joint cases
        if self.flexibility_model != 'rigid':
            # Add floor joint node constrained by the floor diaphragm
            note = ' # Constrained floor node'
            content.append(self.floor_node.to_tcl() + note)
            # Materials defining flexible rotation behaviour
            mz_mat_inputs = ' '.join(
                f'{item}' for item in self._get_mat_inputs('X')
            )
            my_mat_inputs = ' '.join(
                f'{item}' for item in self._get_mat_inputs('Y')
            )
            content.append(f"uniaxialMaterial {mz_mat_inputs}")
            content.append(f"uniaxialMaterial {my_mat_inputs}")
            # Create the new section with flexible rotation behaviour
            sec_inputs = ' '.join(
                f'{item}' for item in self._get_agg_sec_inputs()
            )
            content.append(f"section {sec_inputs}")
            # Create the joint flexibility element
            ele_inputs = ' '.join(
                f'{item}' for item in self._get_ele_inputs()
            )
            content.append(f"element {ele_inputs} ")

        return content
