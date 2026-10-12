"""This module provides the beam class implementation for the ``DP05`` model in
the BNSM layer.
"""
# Imports from installed packages
import openseespy.opensees as ops
from typing import List, Optional

# Imports from bnsm library
from ..dp03.beam import Beam as BeamDP03
from ..baselib.node import Node
from ..baselib.constants import RIGID_MAT

# Imports from utils library
from ....utils.tags import node_tag, TYPE_UNIT


class Beam(BeamDP03):
    """Beam implementation for the ``DP05`` model.

    This class extends the ``DP03`` beam (fiber end sections) with an axial
    release at the end section (*j-end*). The beam element frames into an
    auxiliary node, ``ele_node_j``, which is connected to the beam-side joint
    node, ``release_node``, by a ``zeroLength`` element. The release is free
    along the beam axis and rigid in the transverse translations and in the
    rotations, so the beam can elongate as its fiber sections crack and
    yield, although the joint nodes are constrained by the rigid floor
    diaphragm. The beam then carries no axial force.

    The mid-storey stairs beams have no release (see
    :meth:`~simdesign.rcmrf.bnsm.dp05.building.Building._initialize_beams`).

    Attributes
    ----------
    release_node : Node | None
        Beam-side joint node at the *j-end*, constrained by the floor
        diaphragm. None if the beam has no release.

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.dp03.beam.Beam`
        Beam definition extended by this class.
    """

    release_node: Optional[Node] = None

    @property
    def release_ele_tag(self) -> int:
        """
        Returns
        -------
        int
            Tag of the ``zeroLength`` element of the axial release, equal to
            the tag of the auxiliary node.
        """
        return self.ele_node_j.tag

    def set_axial_release(self) -> None:
        """Moves the *j-end* of the beam element to an auxiliary node at the
        location of the joint node, which becomes the ``release_node``.

        The auxiliary node takes the tag of the beam-side node of the joint,
        i.e., ``left`` for beams along x and ``rear`` for beams along y,
        which is unique for each beam end.
        """
        self.release_node = self.ele_node_j
        point = self.release_node.tag % TYPE_UNIT
        side = 'left' if self.design.direction == 'x' else 'rear'
        self.ele_node_j = Node(node_tag(point, side),
                               self.release_node.coordinates.copy())

    def add_to_ops(self) -> None:
        """Adds beam components to the OpenSees domain (i.e, auxiliary node,
        axial release, fiber sections and beam element).
        """
        if self.release_node is not None:
            self.ele_node_j.add_to_ops()
            ops.element(*self._get_release_ele_inputs())
        super().add_to_ops()

    def to_py(self) -> List[str]:
        """Gets the Python commands to construct beam components in OpenSees
        domain (i.e, auxiliary node, axial release, fiber sections and beam
        element).

        Returns
        -------
        List[str]
            List of Python commands for constructing the components of beam
            object in OpenSees.
        """
        if self.release_node is None:
            return super().to_py()
        release_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_release_ele_inputs()
        )
        content = ['# Create the auxiliary node and the axial release']
        content.append(self.ele_node_j.to_py())
        content.append(f"ops.element({release_inputs})")
        return content + super().to_py()

    def to_tcl(self) -> List[str]:
        """Gets the Tcl commands to construct beam components in OpenSees
        domain (i.e, auxiliary node, axial release, fiber sections and beam
        element).

        Returns
        -------
        List[str]
            List of Tcl commands for constructing the components of beam
            object in OpenSees.
        """
        if self.release_node is None:
            return super().to_tcl()
        release_inputs = ' '.join(
            f'{item}' for item in self._get_release_ele_inputs())
        content = ['# Create the auxiliary node and the axial release']
        content.append(self.ele_node_j.to_tcl())
        content.append(f"element {release_inputs}")
        return content + super().to_tcl()

    def _get_release_ele_inputs(self) -> List[str | float | int]:
        """Retrieves the inputs of the axial release (zero-length element).

        Returns
        -------
        List[str | float | int]
            Inputs of the ``zeroLength`` element between the joint node and
            the auxiliary node. No material is assigned along the beam axis
            (local direction 1), and rigid materials are assigned to the
            transverse translations and the rotations (directions 2-6).
        """
        nodes = [self.release_node.tag, self.ele_node_j.tag]
        if self.design.direction == 'x':
            vecx = [1.0, 0.0, 0.0]
            vecyp = [0.0, -1.0, 0.0]
        elif self.design.direction == 'y':
            vecx = [0.0, 1.0, 0.0]
            vecyp = [1.0, 0.0, 0.0]
        return [
            'zeroLength', self.release_ele_tag, *nodes,
            '-mat', *[RIGID_MAT] * 5, '-dir', 2, 3, 4, 5, 6,
            '-orient', *vecx, *vecyp
        ]
