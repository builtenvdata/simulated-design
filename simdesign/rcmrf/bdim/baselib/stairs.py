"""This module provides the base class for representing stairs in the BDIM
layer.
"""
# Imports from installed packages
from abc import ABC

# Imports from bdim base library
from .loads import PermanentBase, VariableBase

# Imports from geometry library
from ...geometry.base import Rectangle


class StairsBase(ABC):
    """
    Abstract base class for stair slab elements.

    It provides geometry definition, self-weight calculation, load transfer,
    and load assignment behaviour. It must be inherited by design-class-
    specific stair implementations.

    Attributes
    ----------
    rectangle : ~simdesign.rcmrf.geometry.base.Rectangle
        Geometric mesh representation of the stairs (tag, points, lines).
    gamma_rc : float
        Unit weight of reinforced concrete [kN/m^3].
    pg : float
        Total permanent load per unit area of stairs slab [kN/m^2].
        Set via ``set_loads``.
    pq : float
        Variable (live) load per unit area of stairs slab [kN/m^2].
        Set via ``set_loads``.
    roof : bool
        Whether the stairs slab is located at roof level.

    _thickness : float
        Default stairs slab thickness [m], used as fallback when no
        thickness is provided at instantiation. Default is 0.15.

    Notes
    -----
    Plan view of mesh objects (rectangle) representing stairs::

        y
        |__x
                      l2(p2,p3)
         p2(x2,y2,z2) o------>o p3(x3,y3,z3)
                      ^       ^
            l1(p1,p2) |       | l3(p4,p3)
                      |       |
         p1(x1,y1,z1) o------>o p4(x4,y4,z4)
                      l4(p1,p4)

    pi is the i-th ``Point`` representing a corner point.

    li is the i-th surrounding ``Line``.

    xi, yi, and zi are the coordinates of the i-th ``Point``.
    """
    rectangle: Rectangle
    gamma_rc: float
    pg: float
    pq: float
    roof: bool
    _thickness: float = 0.15

    def __init__(self, rectangle: Rectangle, thickness: float = None) -> None:
        """Initialize the StairsBase object.

        Parameters
        ----------
        rectangle : ~simdesign.rcmrf.geometry.base.Rectangle
            Geometric mesh representation of the stairs (tag, points, lines).
        thickness : float, optional
            Stairs slab thickness (depth) in metres, by default None.
            If None, the class-level default (:attr:`_thickness` = 0.15 m)
            is used.
        """
        self.rectangle = rectangle
        self.t = thickness

    @property
    def t(self) -> float:
        """Stairs slab thickness (depth).

        Returns
        -------
        float
            Stairs slab thickness (depth) [m].
        """
        return self._thickness

    @t.setter
    def t(self, value: float | None = None) -> None:
        """Setter for stairs slab thickness (depth).

        If value is None or falsy, the class-level default is retained.
        """
        self._thickness = value or self._thickness

    @property
    def lx(self) -> float:
        """Stairs slab length along the global X-axis.

        This corresponds to the length of ``rectangle.lines[1]``.

        Returns
        -------
        float
            Stairs slab length along the global X-axis [m].
        """
        return self.rectangle.lines[1].length

    @property
    def ly(self) -> float:
        """Stairs slab length along the global Y-axis.

        This corresponds to the length of ``rectangle.lines[0]``.

        Returns
        -------
        float
            Stairs slab length along the global Y-axis [m].
        """
        return self.rectangle.lines[0].length

    @property
    def area(self) -> float:
        """Plan area of the stairs slab.

        This corresponds to ``rectangle.area``.

        Returns
        -------
        float
            Stairs slab area [m^2].
        """
        return self.rectangle.area

    @property
    def pself(self) -> float:
        """Self-weight of the stairs slab per unit plan area.

        Returns
        -------
        float
            Self-weight per unit area [kN/m^2].
        """
        return self.gamma_rc * self.t

    @property
    def beam_influence_areas(self) -> float:
        """Tributary area assigned to each of the two supporting beams.

        Both beams run along the X-direction: one at mid-storey level and one
        at floor level. Each beam is assigned half the total slab area.

        Returns
        -------
        float
            Tributary area per supporting beam [m^2].
        """
        return self.lx * (self.ly / 2)

    def set_loads(
        self, permanent_loads: PermanentBase, variable_loads: VariableBase
    ) -> None:
        """Assign permanent and variable loads to the stairs slab.

        Sets :attr:`gamma_rc`, :attr:`pg` (self-weight plus superimposed dead
        load), and :attr:`pq` (variable load) from the provided load objects.

        Parameters
        ----------
        permanent_loads : PermanentBase
            Permanent load data, including unit weight of reinforced concrete
            [kN/m^3] and superimposed staircase dead load.
        variable_loads : VariableBase
            Variable load data, including staircase live load [kN/m^2].
        """
        self.gamma_rc = permanent_loads.gamma_rc
        self.pg = self.pself + permanent_loads.staircase
        self.pq = variable_loads.staircase
