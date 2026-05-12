"""This module provides the class used to represent any structural node
within the BNSM layer. Unlike other classes in baselib, this class does not
require abstraction.
"""
# Imports from installed packages
import openseespy.opensees as ops
from typing import Optional, List

# Imports from utils library
from ....utils.misc import round_list


class Node:
    """Structural node representation in the BNSM layer. It provides
    methods to define the node in the OpenSees domain and to export
    equivalent Python and Tcl commands.

    Attributes
    ----------
    tag : int
        Unique identifier of the node.
    coordinates : List[float]
        Node coordinates [x, y, z].
    masses : List[float]
        Nodal masses associated with each degree of freedom:
        [Mx, My, Mz, RMx, RMy, RMz].
    nodal_mass : bool, default=True
        If True, masses are assigned directly to the node in OpenSees.
    """
    tag: int
    coordinates: List[float]
    masses: List[float]
    nodal_mass: bool = True

    def __init__(self, tag: int, coordinates: List[float],
                 masses: Optional[List[float]] = None) -> None:
        """Initialize a Node object.

        Parameters
        ----------
        tag : int
            Unique identifier of the node.
        coordinates : List[float]
            Node coordinates [x, y, z].
        masses : List[float] | None, optional
            Nodal masses [Mx, My, Mz, RMx, RMy, RMz]. If not provided,
            masses are initialized to zero.
        """
        self.tag = tag
        self.coordinates = round_list(coordinates)
        if masses is None:
            masses = [0.0] * 6
        elif len(masses) != 6:
            raise ValueError(
                "masses must have 6 components [Mx, My, Mz, RMx, RMy, RMz]"
            )
        self.masses = masses

    def add_to_ops(self) -> None:
        """Adds the node object to OpenSees domain.

        The node is created using the ``ops.node`` command. If ``nodal_mass``
        is True and at least one mass component is non-zero, nodal masses are
        assigned using the ``-mass`` option.
        """
        if self.nodal_mass and any(self.masses):
            ops.node(self.tag, *self.coordinates, '-mass', *self.masses)
        else:
            ops.node(self.tag, *self.coordinates)

    def to_py(self) -> str:
        """Gets the python command to construct the node object in OpenSees.

        Returns
        -------
        str
            Python command for constructing the node object in OpenSees.
        """
        coordinates = ', '.join(map(str, self.coordinates))
        if self.nodal_mass and any(self.masses):
            masses = ', '.join(map(str, self.masses))
            return f"ops.node({self.tag}, {coordinates}, '-mass', {masses})"
        else:
            return f"ops.node({self.tag}, {coordinates})"

    def to_tcl(self) -> str:
        """Gets the Tcl command to construct the node object in OpenSees.

        Returns
        -------
        str
            Tcl command for constructing the node object in OpenSees.
        """
        coordinates = ' '.join(map(str, self.coordinates))
        if self.nodal_mass and any(self.masses):
            masses = ' '.join(map(str, self.masses))
            return f"node {self.tag} {coordinates} -mass {masses}"
        else:
            return f"node {self.tag} {coordinates}"
