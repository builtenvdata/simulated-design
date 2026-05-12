"""This module provides the base class for representing masonry infill walls
within the BDIM layer.
"""
# Imports from installed packages
from abc import ABC
import numpy as np
from typing import List, Optional, Literal

# Imports from bdim base library
from .beam import BeamBase
from .column import ColumnBase

# Imports from geometry library
from ... geometry.base import Rectangle

# Imports from utils library
from ....utils.units import kN, m, mm
from ....utils.misc import PRECISION


# Infill property mapper (Parameters from Hak et al. 2012)
INFILL_PROPERTIES = {
    "Weak": {
        "tw": 80.0,     # Wall thickness [mm]
        "W": 6.87,      # Unit weight [kN/m3]
    },
    "Medium": {
        "tw": 240.0,    # Wall thickness [mm]
        "W": 6.87,      # Unit weight [kN/m3]
    },
    "Strong": {
        "tw": 300.0,    # Wall thickness [mm]
        "W": 7.36,      # Unit weight [kN/m3]
    },
}
"""
The weak masonry infill consists of a 8.0 cm thick single-leaf masonry wall
constructed of horizontally hollowed brick units (volumetric percentage of
holes ≈60%) with a 1.0-cm thick plaster on each face, while the medium
typology consists of two 12.0-cm thick leaves, each constructed of
horizontally hollowed brick units (volumetric percentage of holes ≈60%),
divided by an intermediate 5.0-cm cavity and covered with a 1.0-cm thick
plaster placed at the external sides of the walls. The typology representing
strong infill walls is constituted by a single 30-cm thick leaf built with
vertically hollowed brick units (volumetric percentage of holes ≈50%).

TODO: Verify the weights if they make sense.
"""


class InfillBase(ABC):
    """
    Abstract base class for infills.

    Must be inherited by design-class-specific infills.

    Attributes
    ----------
    rectangle : ~simdesign.rcmrf.geometry.base.Rectangle
        Geometric mesh representation of the infill (tag, points, lines).
    beams : List[Optional[~simdesign.rcmrf.bdim.baselib.beam.BeamBase]]
        List of beams corresponding to the rectangle lines with indices
        1 and 3.
    columns : List[~simdesign.rcmrf.bdim.baselib.column.ColumnBase \
        | List[~simdesign.rcmrf.bdim.baselib.column.ColumnBase]]
        List of columns corresponding to the rectangle lines with indices
        0 and 2.
    loc : Literal['exterior', 'interior']
        Location of the infill wall : 'exterior' or 'interior'.
    """
    rectangle: Rectangle
    beams: List[Optional[BeamBase]]
    columns: List[ColumnBase | List[ColumnBase]]
    loc: Literal['exterior', 'interior']

    def __init__(
        self,
        rectangle: Rectangle,
        beams: List[Optional[BeamBase]],
        columns: List[ColumnBase | List[ColumnBase]],
        loc: Literal['exterior', 'interior']
    ):
        """
        Initialize a new instance of InfillBase.

        Parameters
        ----------
        rectangle : ~simdesign.rcmrf.geometry.base.Rectangle
            Geometric rectangle representing the infill panel.
        beams : List[Optional[~simdesign.rcmrf.bdim.baselib.beam.BeamBase]]
            Beams associated with the rectangle's 1st and 3rd edges (lines).
        columns : List[~simdesign.rcmrf.bdim.baselib.column.ColumnBase \
            | List[~simdesign.rcmrf.bdim.baselib.column.ColumnBase]]
            Columns associated with the rectangle's 0th and 2nd edges (lines).
        loc : Literal['exterior', 'interior']
            Location type of the infill wall which determines thickness.
        """
        self.rectangle = rectangle
        self.beams = beams
        self.columns = columns
        self.loc = loc

    @property
    def typology(self) -> Literal['Weak', 'Medium', 'Strong']:
        """
        Return the infill wall typology (strength) based on assignment.

        Returns
        -------
        Literal['Weak', 'Medium', 'Strong']
            Type of the infill wall.

        Raises
        ------
        KeyError
            If ``loc`` is not set to 'interior' or 'exterior' and strength
            is not defined.
        """
        if self.rectangle.typology:
            return self.rectangle.typology
        elif self.loc == 'interior':
            return 'Weak'  # Default typology for interior frame infills
        elif self.loc == 'exterior':
            return 'Medium'  # Default typology for exterior frame infills
        else:
            raise KeyError('Infill location is not set or not valid')

    @property
    def thickness(self) -> float:
        """
        Return the infill wall thickness based on its typology.

        Returns
        -------
        float
            Thickness of the infill wall.
        """
        return INFILL_PROPERTIES[self.typology]['tw'] * mm

    @property
    def unit_weight(self) -> float:
        """
        Return the infill wall unit weight based on its typology.

        Returns
        -------
        float
            Unit weight of the infill wall.
        """
        return INFILL_PROPERTIES[self.typology]['W'] * kN/m**3

    @property
    def height(self) -> float:
        """
        Compute the infill height from its rectangle points (z-extent).

        Returns
        -------
        float
            Height of infill wall.
        """
        zs = [p.coordinates[2] for p in self.rectangle.points]
        height = max(zs) - min(zs)
        return round(height, PRECISION)

    @property
    def length(self) -> float:
        """
        Compute the infill length along its in-plane horizontal axis.

        Returns
        -------
        float
            Length of wall along y (if YZ plane) or along x (if XZ plane).

        Raises
        ------
        ValueError
            If the rectangle is not axis-aligned in YZ or XZ planes.
        """
        plane = self.plane
        if plane == 'YZ':
            ys = [p.coordinates[1] for p in self.rectangle.points]
            length = max(ys) - min(ys)
        elif plane == 'XZ':
            xs = [p.coordinates[0] for p in self.rectangle.points]
            length = max(xs) - min(xs)
        else:
            raise ValueError("Rectangle not aligned with YZ or XZ plane")

        return round(length, PRECISION)

    @property
    def plane(self) -> Literal['XZ', 'YZ']:
        """
        Detect whether the rectangle lies in the YZ or XZ plane and return
        the corresponding in-plane name.

        Returns
        -------
        Literal['XZ', 'YZ']
            The plane name which is parallel to the infill.

        Raises
        ------
        ValueError
            If the rectangle is not axis-aligned in YZ or XZ planes.
        """
        u_norm = self.rectangle.unit_normal_vector
        if np.allclose(u_norm, [0.0, 1.0, 0.0]):
            return 'XZ'   # XZ (ccw)
        elif np.allclose(u_norm, [-1.0, 0.0, 0.0]):
            return 'YZ'   # YZ (ccw)
        else:
            raise ValueError("Rectangle not aligned with YZ or XZ plane")

    @property
    def weight(self) -> float:
        """
        Compute the total weight of the infill panel.

        Returns
        -------
        float
            Total weight of infill wall.
        """
        weight = self.length * self.height * self.thickness * self.unit_weight
        return round(weight, PRECISION)

    @property
    def wg(self) -> float:
        """
        Return the distributed load (line load) on the supporting beam.

        Returns
        -------
        float
            Distributed weight of infill wall along its length.
        """
        return round(self.weight / self.length, PRECISION)

    def set_beam_infill_load(self) -> None:
        """
        Assign the infill's distributed load to the supporting beam.

        Notes
        -----
        If supporting beam exists (except ground floors), sets its
        ``infill_wg`` attribute to ``self.wg``.
        """
        if self.beams[1]:  # Bottom (supporting) beam
            self.beams[1].infill_wg = self.wg
