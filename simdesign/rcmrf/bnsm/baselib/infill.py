"""This module provides a base class for representing masonry infill
walls within the BNSM layer.
"""
# Imports from installed packages
from abc import ABC
import numpy as np
import openseespy.opensees as ops
from typing import Tuple, List

# Imports from bnsm library
from .node import Node

# Imports from bdim base library
from ...bdim.baselib.infill import InfillBase as InfillDesign

# Imports from utils library
from ....utils.units import mm, MPa
from ....utils.misc import PRECISION, round_list


# Infill property mapper (Parameters from Hak et al. 2012)
HAKETAL2012_INFILLS = {
    "Weak": {           # Typology: T1
        "fwh": 1.18,    # Horizontal compressive strength [MPa]
        "fwv": 2.02,    # Vertical compressive strength [MPa]
        "fwu": 0.44,    # Sliding shear resistance of mortar joints [MPa]
        "fws": 0.55,    # Shear resistance under diagonal compression [MPa]
        "Ewh": 991.0,   # Horizontal secant modulus [MPa]
        "Ewv": 1873.0,  # Vertical secant modulus [MPa]
        "Gw": 1089.0,   # Shear modulus [MPa]
        "tw": 80.0,     # Wall thickness [mm]
        "sig_v": 0.0,   # Vertical compression due to gravity loading [MPa]
        "v": 0.2,       # Poisson's ratio [-]
        "W": 6.87,      # Unit weight [kN/m3]
    },
    "Medium": {         # Typology: T2
        "fwh": 1.11,    # Horizontal compressive strength [MPa]
        "fwv": 1.50,    # Vertical compressive strength [MPa]
        "fwu": 0.25,    # Sliding shear resistance of mortar joints [MPa]
        "fws": 0.31,    # Shear resistance under diagonal compression [MPa]
        "Ewh": 991.0,   # Horizontal secant modulus [MPa]
        "Ewv": 1873.0,  # Vertical secant modulus [MPa]
        "Gw": 1089.0,   # Shear modulus [MPa]
        "tw": 240.0,    # Wall thickness [mm]
        "sig_v": 0.0,   # Vertical compression due to gravity loading [MPa]
        "v": 0.2,       # Poisson's ratio [-]
        "W": 6.87,      # Unit weight [kN/m3]
    },
    "Strong": {         # Typology: T3
        "fwh": 1.50,    # Horizontal compressive strength [MPa]
        "fwv": 3.51,    # Vertical compressive strength [MPa]
        "fwu": 0.30,    # Sliding shear resistance of mortar joints [MPa]
        "fws": 0.36,    # Shear resistance under diagonal compression [MPa]
        "Ewh": 1050.0,  # Horizontal secant modulus [MPa]
        "Ewv": 3240.0,  # Vertical secant modulus [MPa]
        "Gw": 1296.0,   # Shear modulus [MPa]
        "tw": 300.0,    # Wall thickness [mm]
        "sig_v": 0.0,   # Vertical compression due to gravity loading [MPa]
        "v": 0.2,       # Poisson's ratio [-]
        "W": 7.36,      # Unit weight [kN/m3]
    },
}


class InfillBase(ABC):
    """Abstract Base Class for masonry infill wall implementations in the BNSM
    layer. It provides methods to define an infill in the OpenSees domain and
    to export equivalent Python and Tcl commands.

    The implementation follows a macro-modeling approach, where infill walls
    are represented by two diagonal truss elements with a nonlinear uniaxial
    material model. Infill typology and strut modelling strategy are based on
    Hak et al. (2012).

    Attributes
    ----------
    design : ~simdesign.rcmrf.bdim.baselib.infill.InfillBase
        Instance of infill design information model.
    strut1_nodes : List[Node]
        Element nodes of 1st diagonal strut.
    strut2_nodes : List[Node]
        Element nodes of 2nd diagonal strut.

    References
    ----------
    Hak, S., Morandi, P., Magenes, G., & Sullivan, T. J. (2012). Damage
    control for clay masonry infills in the design of RC frame structures.
    Journal of Earthquake Engineering, 16(sup1), 1-35.
    https://doi.org/10.1080/13632469.2012.670575
    """
    design: InfillDesign
    strut1_nodes: List[Node]
    strut2_nodes: List[Node]

    def __init__(self, design: InfillDesign,
                 strut1_nodes: List[Node],
                 strut2_nodes: List[Node]) -> None:
        """
        Initialize an `Infill` with its design data and diagonal strut nodes.

        Parameters
        ----------
        design : ~simdesign.rcmrf.bdim.baselib.infill.InfillBase
            Infill design information (geometry, tags, typology).
        strut1_nodes : List[Node]
            Nodes defining the first diagonal truss element (e.g., [i, j]).
        strut2_nodes : List[Node]
            Nodes defining the second diagonal truss element (e.g., [i, j]).
        """
        self.design = design
        self.strut1_nodes = strut1_nodes
        self.strut2_nodes = strut2_nodes

    def add_to_ops(self) -> None:
        """Adds infill components to the OpenSees domain
        (i.e, truss elements and uniaxialmaterial).
        """
        # Retrieve element and material inputs
        strut1_inputs, strut2_inputs, mat_inputs = self._get_strut_inputs()

        # Create the material for diagonal struts
        ops.uniaxialMaterial(*mat_inputs)

        # Create the elements for diagonal struts
        ops.element(*strut1_inputs)
        ops.element(*strut2_inputs)

    def to_py(self) -> List[str]:
        """Gets the Python commands to construct infill components in OpenSees
        domain (i.e, truss elements and uniaxialmaterial).

        Returns
        -------
        List[str]
            List of Python commands for constructing the components of infill
            object in OpenSees.
        """
        # Retrieve element and material inputs
        strut1_inputs, strut2_inputs, mat_inputs = self._get_strut_inputs()

        # Create the material for diagonal struts
        content = ['# Create the material for diagonal struts']
        mat_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in mat_inputs
        )
        content.append(f"ops.uniaxialMaterial({mat_inputs})")

        # Create the elements for diagonal struts
        content.append('# Create the elements for diagonal struts')
        strut1_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in strut1_inputs
        )
        strut2_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in strut2_inputs
        )
        content.append(f"ops.element({strut1_inputs})")
        content.append(f"ops.element({strut2_inputs})")

        return content

    def to_tcl(self) -> List[str]:
        """Gets the Tcl commands to construct infill components in OpenSees
        domain (i.e, truss elements and uniaxialmaterial).

        Returns
        -------
        List[str]
            List of Tcl commands for constructing the components of infill
            object in OpenSees.
        """
        # Retrieve element and material inputs
        strut1_inputs, strut2_inputs, mat_inputs = self._get_strut_inputs()

        # Create the material for diagonal struts
        content = ['# Create the material for diagonal struts']
        mat_inputs = ' '.join([f"{item}" for item in mat_inputs])
        content.append(f"uniaxialMaterial {mat_inputs}")

        # Create the elements for diagonal struts
        content.append('# Create the elements for diagonal struts')
        strut1_inputs = ' '.join([f"{item}" for item in strut1_inputs])
        strut2_inputs = ' '.join([f"{item}" for item in strut2_inputs])
        content.append(f"element {strut1_inputs}")
        content.append(f"element {strut2_inputs}")

        return content

    def _get_strut_inputs(self) -> Tuple[List[str | int | float]]:
        """
        Build OpenSees argument lists for the two diagonal strut elements and
        the associated uniaxial material.

        Returns
        -------
        strut1_inputs : List[str | int | float]
            1st strut element argument list.
        strut2_inputs : List[str | int | float]
            2nd strut element argument list.
        mat_inputs : List[str | int | float]
            `uniaxialMaterial` argument list.

        Notes
        -----
        Element tags are derived from the infill `rectangle.tag` and are
        intended to be unique within the model. The material tag is set to
        `rectangle.tag`.
        """
        mat_tag = self.design.rectangle.tag
        mat_inputs, area = self._get_mat_inputs()
        ele1_tag = int(str(self.design.rectangle.tag) + '001')
        ele2_tag = int(str(self.design.rectangle.tag) + '002')
        ele1_nodes = [self.strut1_nodes[0].tag, self.strut1_nodes[1].tag]
        ele2_nodes = [self.strut2_nodes[0].tag, self.strut2_nodes[1].tag]
        strut1_inputs = ['Truss', ele1_tag] + ele1_nodes + [area, mat_tag]
        strut2_inputs = ['Truss', ele2_tag] + ele2_nodes + [area, mat_tag]

        return strut1_inputs, strut2_inputs, mat_inputs

    def _get_mat_inputs(self) -> Tuple[List[str | float | int], float]:
        """
        Compute the uniaxial material definition for the equivalent diagonal
        strut and the corresponding strut cross-sectional area based on
        Hak et al. 2012.

        Returns
        -------
        mat_inputs : List[str | float | int]
            OpenSees `uniaxialMaterial` argument list.
        Aw : float
            Equivalent digaonal strut area (m2).

        References
        ----------
        Hak, S., Morandi, P., Magenes, G., Sullivan, T. (2012). Damage control
        for clay masonry infills in the design of RC frame structures.
        Journal of Earthquake Engineering, 16(sup1), 1-35.
        https://doi.org/10.1080/13632469.2012.670575
        """
        # DETERMINE EQUIVALENT DIAGONAL STRUT GEOMETRY
        # Typology dependent properties
        props = HAKETAL2012_INFILLS.get(self.design.typology)
        # Terms based on Figure 7, Hak et al. 2012
        # Note average values from surrounding members are considered
        plane = self.design.plane
        if plane == "XZ":
            b_attr = "bx"
            I_attr = "Iy"
        elif plane == "YZ":
            b_attr = "by"
            I_attr = "Ix"
        hbs = []
        hcs = []
        Ics = []
        Ecs = []
        for column in self.design.columns:  # Loop through columns
            if isinstance(column, list):
                for column_ in column:
                    if column_:
                        hcs.append(getattr(column_, b_attr))
                        Ics.append(getattr(column_, I_attr))
                        Ecs.append(column_.concrete.Ecm)
            elif column:
                hcs.append(getattr(column, b_attr))
                Ics.append(getattr(column, I_attr))
                Ecs.append(column.concrete.Ecm)
        for beam in self.design.beams:  # Loop through beams
            if beam:
                hbs.append(beam.h)
        hb = sum(hbs) / len(hbs)  # Beam height
        hc = sum(hcs) / len(hcs)  # Column height
        Ic = (sum(Ics) / len(Ics)) / (mm**4)  # Column moment of inertia (mm4)
        Ec = (sum(Ecs) / len(Ecs)) / MPa  # Colum concrete modulus (MPa)
        h = self.design.height / mm  # infill height, between joints (mm)
        L = self.design.length / mm  # infill length, between joints (mm)
        Lw = h - hc  # clear infill length (mm)
        hw = L - hb  # clear infill height (mm)
        theta = np.arctan(hw / Lw)  # inclination of the diagonal strut (rad)
        dw = (Lw**2 + hw**2) ** 0.5  # diagonal length of the infill panel (mm)
        Ewtheta = 1.0 / (  # Equation (3), Hak et al. 2012
            (np.cos(theta) ** 4) / props['Ewh']
            + (np.sin(theta) ** 4) / props['Ewv']
            + (np.cos(theta) ** 2) * (np.sin(theta) ** 2)
            * (1.0 / props['Gw'] - 2.0 * props['v'] / props['Ewv'])
        )
        lambda_h = h * (  # Equation (2), Hak et al. 2012
            Ewtheta * props['tw'] * np.sin(2.0 * theta) / (4.0 * Ec * Ic * hw)
        ) ** 0.25
        # Table 4, Hak et al. 2012
        if lambda_h < 3.14:
            K1, K2 = 1.300, -0.178
        elif 3.14 < lambda_h < 7.85:
            K1, K2 = 0.707, 0.010
        else:
            K1, K2 = 0.470, 0.040
        # Equivalent digaonal strut width (mm)
        bw = dw * (K1 / lambda_h + K2)  # Equation (1), Hak et al. 2012

        # DETERMINE CRITICAL STRESS IN EACH MODE
        # Compression in centre, Equation (4)
        sigw1 = 1.16 * props['fwv'] * np.tan(theta) / (K1 + K2 * lambda_h)
        # Compression at corners, Equation (5)
        sigw2 = (
            (1.12 * props['fwv'] * np.sin(theta) * np.cos(theta))
            / (K1 * (lambda_h**-0.12) + K2 * (lambda_h**0.88))
        )
        # Shear sliding, Equation (6)
        sigw3 = (
            ((1.2 * np.sin(theta) + 0.45 * np.cos(theta)) * props['fwu']
             + 0.3 * props['sig_v']) / (bw / dw)
        )
        # Diagonal tension, Equation (7)
        sigw4 = (0.6 * props['fws'] + 0.3 * props['sig_v']) / (bw / dw)
        # Governing failure mechanism
        sigw = min(sigw1, sigw2, sigw3, sigw4) * MPa  # (kPa)
        # Equivalent digaonal strut area (m2)
        Aw = (bw * props['tw'] * mm**2)

        # Uniaxial material Inputs from Hak et al. 2012.
        fpc = -sigw  # Compressive strength of strut
        fpcu = 0.01 * fpc  # assumed, %1 to avoid numerical issues
        epsc0 = -0.0013  # from Hak et al. 2012, Figure 12b
        epscu = -0.0045  # from Hak et al. 2012, Figure 12b
        mat_inputs = round_list([fpc, epsc0, fpcu, epscu], PRECISION)
        mat_inputs = ['Concrete01', self.design.rectangle.tag] + mat_inputs

        return mat_inputs, Aw
