"""This module provides the base class for representing slabs in the BDIM
layer.
"""
# Imports from installed packages
import numpy as np
from abc import ABC
from scipy.interpolate import interp1d
from typing import Literal, List, Optional

# Imports from bdim base library
from .loads import PermanentBase, VariableBase

# Imports from geometry library
from ...geometry.base import Rectangle

# Imports from utils library
from ....utils.misc import PRECISION


class SlabBase(ABC):
    """
    Abstract base class for floor slab elements.

    It provides geometry definition, thickness estimation, load transfer,
    and load assignment behaviour. It must be inherited by design-class-
    specific slab implementations.

    Attributes
    ----------
    rectangle : ~simdesign.rcmrf.geometry.base.Rectangle
        Geometric mesh representation of the slab (tag, points, lines).
    typology : Literal[1, 2, 3]
        Slab typology.
            1: Solid two-way cast-in-situ slabs (SS2).
            2: Solid one-way cast-in-situ slabs (SS1).
            3: One-way composite slab with ceramic blocks and RC joists or
            pre-stressed beams (HS).
    gamma_rc : float
        Unit weight of reinforced concrete [kN/m^3].
    pg : float
        Total permanent load per unit area [kN/m^2].
        Set via ``set_loads``.
    pq : float
        Variable load per unit area [kN/m^2].
        Set via ``set_loads``.
    roof : bool
        Whether the slab is located at roof level.

    MAX_THICKNESS : float
        Maximum allowable slab thickness, by default 0.85 m.

    _thickness : float | None
        Default floor slab thickness. If None, thickness is estimated
        from span length when accessed via ``t``.
    _orientation : Literal[1, 2, 3] | None
        Default floor slab load-transfer orientation. If None, orientation is
        inferred from typology and span ratio when accessed via
        ``orientation``.

    Notes
    -----
    Plan view of mesh objects (rectangle) representing slabs::

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
    typology: Literal[1, 2, 3]
    gamma_rc: float
    pg: float
    pq: float
    roof: bool
    MAX_THICKNESS: float = 0.85
    _orientation: Optional[Literal[1, 2, 3]]
    _thickness: Optional[float]

    def __init__(
        self, rectangle: Rectangle, typology: Literal[1, 2, 3],
        thickness: Optional[float] = None,
        orientation: Optional[Literal[1, 2, 3]] = None
    ) -> None:
        """Initialize the Slab object.

        Parameters
        ----------
        rectangle : ~simdesign.rcmrf.geometry.base.Rectangle
            Geometric mesh representation of the slab (tag, points, lines).
        typology : Literal[1, 2, 3]
            Slab typology.
            1: Solid two-way cast-in-situ slabs (SS2).
            2: Solid one-way cast-in-situ slabs (SS1).
            3: One-way composite slab with ceramic blocks and RC joists or
            pre-stressed beams (HS).
        thickness : float, optional
            Slab thickness (depth), by default None.
            If None, thickness is estimated from span length; see :attr:`t`.
        orientation : Literal[1, 2, 3], optional
            Orientation of slab load transfer to beams, by default None.
            1: Load is transferred to beams along the X direction.
            2: Load is transferred to beams along the Y direction.
            3: Load is transferred to beams along both directions.
            If None, orientation is inferred from typology and span ratio;
            see :attr:`orientation`.
        """
        self.rectangle = rectangle
        self.typology = typology
        self._thickness = thickness
        self._orientation = orientation

    @property
    def lx(self) -> float:
        """Slab length along the global X-axis.

        This corresponds to the length of ``rectangle.lines[1]``.

        Returns
        -------
        float
            Slab length along the global X-axis [m].
        """
        return self.rectangle.lines[1].length

    @property
    def ly(self) -> float:
        """Slab length along the global Y-axis.

        This corresponds to the length of ``rectangle.lines[0]``.

        Returns
        -------
        float
            Slab length along the global Y-axis [m].
        """
        return self.rectangle.lines[0].length

    @property
    def area(self) -> float:
        """Slab plan area.

        This corresponds to ``rectangle.area``.

        Returns
        -------
        float
            Slab plan area [m^2].
        """
        return self.rectangle.area

    @property
    def pself(self) -> float:
        """
        Slab self-weight per unit area.

        Returns
        -------
        float
            Slab self-weight per unit area [kN/m^2].

        Notes
        -----
        For solid cast-in-situ slabs (typology 1 or 2), self-weight is
        computed as:

            pself = gamma_rc * t

        For composite slabs with pre-fabricated joists and ceramic blocks
        (typology 3), a logarithmic regression fit to manufacturer data is
        used:

            pself = 2.20 * ln(t) + 6.50

        where t is the slab thickness in metres.

        References
        ----------
        https://presdouro.pt/wp-content/themes/presdouro/images/DT_PD2016_VALIDADO.pdf
        https://lajes.pavimir.pt/pdfs/DA%2060%20-%20Pavimentos%20Aligeirados.pdf
        """
        # Solid cast-in-situ slab
        if self.typology == 1 or self.typology == 2:
            return self.gamma_rc * self.t
        # Composite slab with pre-fabricated joists and ceramic blocks
        elif self.typology == 3:
            return 2.20 * np.log(self.t) + 6.50

    @property
    def beam_alpha_coeffs(self) -> List[float]:
        """
        Alpha coefficients for the four beams surrounding the slab.

        Alpha coefficients convert triangular or trapezoidal slab loads into
        equivalent uniformly distributed loads on each beam; see
        :meth:`_get_alpha`. For one-way orientations, all coefficients are 1.0.

        Returns
        -------
        list[float]
            Alpha coefficients of four beams surrounding the slab,
            ordered [l1, l2, l3, l4] following the plan-view convention.
        """
        if self.orientation == 3:
            long = max(self.lx, self.ly)
            short = min(self.lx, self.ly)
            ratio = float(short / long)
            alpha_l = self._get_alpha(ratio)
            alpha_s = self._get_alpha(1.0)
            if self.lx > self.ly:
                # Long span is along x
                return [alpha_s, alpha_l, alpha_s, alpha_l]
            else:
                # Long span is along y
                return [alpha_l, alpha_s, alpha_l, alpha_s]
        else:
            return [1.0, 1.0, 1.0, 1.0]

    @property
    def orientation(self) -> Literal[1, 2, 3]:
        """
        Slab load-transfer orientation.

        Returns
        -------
        Literal[1, 2, 3]
            Slab load-transfer orientation.
            1: Load is transferred to beams along the X direction.
            2: Load is transferred to beams along the Y direction.
            3: Load is transferred to beams along both directions.

        Notes
        -----
        When orientation is not explicitly set, it is inferred as follows:
        For two-way slabs (typology 1) ``orientation = 3``. For one-way slabs,
        load transfer is oriented along the longer span axis:
        ``orientation = 1`` if lx > ly, ``orientation = 2`` otherwise.
        """
        if self._orientation is None:
            if self.typology == 1:
                return 3
            elif self.lx / self.ly > 1.0:
                return 1
            else:
                return 2
        return self._orientation

    @orientation.setter
    def orientation(self, value: Optional[Literal[1, 2, 3]] = None) -> None:
        """Setter for orientation.

        If ``value`` is None, the orientation will be inferred from typology
        and span ratio when next accessed; see :attr:`orientation`.
        """
        self._orientation = value

    @property
    def t(self) -> float:
        """
        Slab thickness (depth).

        Returns
        -------
        float
            Slab thickness (depth) [m].

        Notes
        -----
        When thickness is not explicitly set, it is estimated from the shorter
        span length ``min(lx, ly)``.

        For solid cast-in-situ slabs (typology 1 or 2), a span-to-depth ratio
        of 30 is assumed:

            t = round(min_span / 30, 2)

        For composite slabs with pre-fabricated joists and ceramic blocks
        (typology 3), a linear regression fit to manufacturer data is used:

            t = round(0.032 * min_span + 0.065, 2)

        In both cases the result is capped at :attr:`MAX_THICKNESS`.

        References
        ----------
        https://presdouro.pt/wp-content/themes/presdouro/images/DT_PD2016_VALIDADO.pdf
        https://lajes.pavimir.pt/pdfs/DA%2060%20-%20Pavimentos%20Aligeirados.pdf
        """
        if self._thickness is None:
            min_span_length = min(self.lx, self.ly)
            if self.typology == 1 or self.typology == 2:
                return min(
                    round(100 * min_span_length / 30) / 100,
                    self.MAX_THICKNESS)
            elif self.typology == 3:
                return min(
                    round(100 * (0.032 * min_span_length + 0.065)) / 100,
                    self.MAX_THICKNESS)
        return self._thickness

    @t.setter
    def t(self, value: Optional[float] = None) -> None:
        """Setter for slab thickness (depth).

        If ``value`` is None, thickness will be estimated from span length
        when next accessed; see :attr:`t`.
        """
        self._thickness = value

    @property
    def beam_tributary_areas(self) -> List[float]:
        """
        Tributary areas assigned to the surrounding beams.

        Returns
        -------
        list[float]
            Tributary areas [m^2] for the four beams surrounding the slab,
            ordered [l1, l2, l3, l4] following the plan-view convention.

        Notes
        -----
        For one-way orientations (1 or 2), one pair of parallel beams carries
        the full half-area each and the perpendicular pair carries nothing.
        For two-way orientation (3), loads are distributed as triangular areas
        to beams along the shorter span and trapezoidal areas to beams along
        the longer span.
        """
        # Loading along beam in x
        if self.orientation == 1:
            ax = self.lx * self.ly / 2
            ay = 0
        # Loading along beam in y
        elif self.orientation == 2:
            ax = 0
            ay = self.lx * self.ly / 2
        # Loading along beams on both sides
        elif self.orientation == 3:
            if self.lx > self.ly:
                # Trapezoid area
                ax = (((self.lx - self.ly) + self.lx) * self.ly) / 2
                # Triangle area
                ay = ((self.ly / 2) * self.ly) / 2
            else:
                # Triangle area
                ax = ((self.lx / 2) * self.lx) / 2
                # Trapezoid area
                ay = (((self.ly - self.lx) + self.ly) * self.lx) / 2

        ax = round(ax, PRECISION)
        ay = round(ay, PRECISION)
        return [ay, ax, ay, ax]

    def set_loads(
        self, permanent_loads: PermanentBase, variable_loads: VariableBase
    ) -> None:
        """Assign permanent and variable loads to the slab.

        Sets :attr:`gamma_rc`, :attr:`pg` (self-weight + superimposed dead
        load), and :attr:`pq` from the provided load objects. Load values
        depend on whether the slab is at roof or floor level (:attr:`roof`).

        Parameters
        ----------
        permanent_loads : PermanentBase
            Permanent loads.
        variable_loads : VariableBase
            Variable loads.
        """
        self.gamma_rc = permanent_loads.gamma_rc
        if self.roof:
            self.pg = self.pself + permanent_loads.roof
            self.pq = variable_loads.roof
        else:
            self.pg = self.pself + permanent_loads.floor
            self.pq = variable_loads.floor

    def _get_alpha(self, ratio: float) -> float:
        """
        Compute correction factor for equivalent uniformly distributed load.

        The load transferred from the slab to a beam may be triangular or
        trapezoidal. The correction factor ``alpha`` converts this load to an
        equivalent uniformly distributed load that produces the same maximum
        bending moment.

        Parameters
        ----------
        ratio : float
            Ratio of shorter to longer slab dimension, in the range (0, 1].

        Returns
        -------
        float
            Correction factor for equivalent uniformly distributed load,
            in the range [2/3, 1.0].

        Notes
        -----
        The input ratio is halved internally before interpolation to align
        with the reference table, which is defined over half-span ratios.

        In the mid-span of a beam with length L, a triangular load with peak
        value wtr results in a maximum moment of:

            Mmax = (L**2 * wtr) / 12

        A uniform load we over the same beam produces:

            Mmax = (L**2 * we) / 8

        Equating both expressions yields alpha = 2/3 for triangular loading.
        For trapezoidal loads, alpha varies between 2/3 and 1.0 depending on
        the aspect ratio.
        """
        # Reference table for alpha values
        ratio_ref = np.arange(0, 0.55, 0.05)
        alpha_ref = np.array([1.000, 0.9967, 0.9867, 0.97, 0.9467, 0.9167,
                              0.88, 0.8367, 0.7867, 0.73, 0.6667])

        # Ratio is halved and clipped for compatibility with the table.
        ratio = np.clip(ratio / 2, 0.0, 0.5)
        alpha = float(interp1d(ratio_ref, alpha_ref)(ratio))

        return alpha
