"""This module provides a base class for representing structural foundations
within the BNSM layer and for building and exporting their OpenSees
representations.
"""
# Imports from installed packages
from abc import ABC
from typing import List
import openseespy.opensees as ops

# Imports from bnsm library
from .node import Node

# Imports from bdim base library
from ...bdim.baselib.joint import JointBase as JointDesign


class FoundationBase(ABC):
    """Abstract Base Class for foundation implementations in BNSM layer.
    It provides methods to define a foundation in the OpenSees domain and to
    export equivalent Python and Tcl commands.

    The foundation is defined using a single node, which carries the lumped
    mass and is fully constrained in all degrees of freedom. To model
    soil-structure interaction, this class needs to be extended.

    Attributes
    ----------
    foundation_node : Node
        Foundation node.
    design : JointDesign
        Instance of support joint design information model.
    """
    foundation_node: Node
    design: JointDesign

    def __init__(self, design: JointDesign, mass: float):
        """Initialize the Foundation object.

        Parameters
        ----------
        design : ~simdesign.rcmrf.bnsm.baselib.joint.JointBase
            Reference design information of support joint.
        mass : float
            Total mass assigned to support joint.
        """
        # Save the reference design information of joint
        self.design = design
        # Initialize the foundation (support) node
        self._initialize_foundation_node(mass)

    def _initialize_foundation_node(self, mass):
        """Initialize the foundation node.

        Parameters
        ----------
        mass : float
            Total mass assigned to support joint.
        """
        tag = self.design.elastic_node.tag + 70000
        coordinates = self.design.elastic_node.coordinates
        masses = [mass, mass, mass, 0.0, 0.0, 0.0]
        self.foundation_node = Node(tag, coordinates, masses)

    def add_to_ops(self) -> None:
        """Adds all the objects that are necessary for defining foundation
        into the OpenSees domain.
        """
        self.foundation_node.add_to_ops()
        ops.fix(self.foundation_node.tag, 1, 1, 1, 1, 1, 1)

    def to_py(self) -> List[str]:
        """Gets the Python commands to define all the objects that are
        necessary for defining foundation in the OpenSees domain.

        Returns
        -------
        List[str]
            List of Python commands for constructing the components of
            foundation in OpenSees.
        """
        col = self.design.top_column.line.tag
        content = [f'# Foundation or support under the column {col}']
        content.append(self.foundation_node.to_py())
        content.append(
            f"ops.fix({self.foundation_node.tag}, 1, 1, 1, 1, 1, 1)"
        )

        return content

    def to_tcl(self) -> List[str]:
        """Gets the Tcl commands to define all the objects that are
        necessary for defining foundation in the OpenSees domain.

        Returns
        -------
        List[str]
            List of Tcl commands for constructing the components of
            foundation in OpenSees.
        """
        col = self.design.top_column.line.tag
        content = [f'# Foundation or support under the column {col}']
        content.append(self.foundation_node.to_tcl())
        content.append(f"fix {self.foundation_node.tag} 1 1 1 1 1 1")

        return content
