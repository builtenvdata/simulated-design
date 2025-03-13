"""
Specific routines for defining and designing tr_7599 columns.

References
----------
TBEC-1975(TR)-Specification for Structures to be Built in Disaster Areas
TS500-1984(TR)-Design and Construction Rules for Reinfoced Concrete Buildings
"""

# Imports from installed packages
import json
from math import ceil
import numpy as np
import numpy.typing as npt
from pathlib import Path
from typing import Tuple, Dict
from scipy.interpolate import RegularGridInterpolator

# Imports from the design class (tr_7599) library
from .materials import Steel, Concrete

# Imports from bdim base library
from ..baselib.column import ColumnBase

# Imports from utils library
from ....utils.units import MPa, N, m, mm


class DesignTableTR:
    """
    Design table class for Turkish design practice.

    It is used for longitudinal reinforcement area calculation in
    reinforced concrete rectangular column sections.

    Attributes
    ----------
    data : Dict[str, Dict[str, npt.NDArray[np.float64]]]
        Dictionary containing reinforcement for varying steel grades
        and axial load ratios.

    References
    ----------
    Aydin, M. R., Akgün, Ö. R., Topçu, A. Betonarme Kolon Tablolari,
    Eskisehir, 1991.
    """

    data: Dict[str, Dict[str, npt.NDArray[np.float64]]]
    """Dictionary containing reinforcement for varying steel grades
    and axial load ratios."""

    def __init__(self):
        """Initialize reinforcement area calculator."""
        # Load json file
        json_path = Path(__file__).parent / "data/design_tables.json"
        with open(json_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
        # Convert "values" field into NumPy arrays
        for key in data:
            data[key]["mx"] = np.array(data[key]["mx"])
            data[key]["my"] = np.array(data[key]["my"])
            data[key]["omega"] = np.array(data[key]["omega"])
        # Save as attribute
        self.data = data

    def _find_num_bars(self, b: float, h: float) -> Tuple[int, int, int]:
        """Finds the number of bars placed on each side of the section.

        Parameters
        ----------
        b : float
            Section width (m).
        h : float
            Section height (m).

        Returns
        -------
        Tuple[int, int, int]
            Number of internal bars along width,
            Number of internal bars along height,
            Total number of bars.
        """

        cover_b = 0.1 * b  # clear cover + stirrup diam. + 0.5*long.diam.
        cover_h = 0.1 * h  # clear cover + stirrup diam. + 0.5*long.diam.

        # Finds short and long side lengths for between outermost rebars
        shortside, longside = min(b - 2 * cover_b, h - 2 * cover_h), max(
            b - 2 * cover_b, h - 2 * cover_h
        )

        # Finds the index of the closest spacing to 100 mm (assumption).
        possible_spacings = shortside / np.arange(1, 10)  # Possible spacings
        closest_idx = np.argmin(np.abs(possible_spacings - 100))

        if shortside == b - 2 * cover_b:
            num_bars_int_b = closest_idx
            num_bars_int_h = int(
                np.floor(longside / possible_spacings[closest_idx]) - 1
            )
        else:
            num_bars_int_h = closest_idx
            num_bars_int_b = int(
                np.floor(longside / possible_spacings[closest_idx]) - 1
            )

        num_bars = 2 * (num_bars_int_b + num_bars_int_h) + 4

        return num_bars_int_b, num_bars_int_h, num_bars

    def _interpolate(
        self, table: Dict[str, npt.NDArray[np.float64]], mx: float, my: float
    ) -> float:
        """Performs bilinear interpolation to estimate reinforcement area.

        Parameters
        ----------
        data : Dict[str, npt.NDArray[np.float64]]
            Design table data.
        mx : float
            Normalised moment in X.
        my : float
            Normalised moment in Y.

        Returns
        -------
        float
            Interpolated omega coefficient based on the design table and
            sectional forces.
        """
        # NOTE: The values outside the domain are extrapolated
        interpolator = RegularGridInterpolator(
            (table['mx'], table['my']), table['omega'],
            method='linear', bounds_error=False, fill_value=None
        )
        w = interpolator([[my, mx]])[0]
        return w

    def get_reinforcement(
        self, Nd: float, Mxd: float, Myd: float, fcd: float,
        fsyd: float, fsyk: float, bx: float, by: float
    ) -> Tuple[float, float]:
        """Retrieves reinforcement area from design
        tables with interpolation.

        Parameters
        ----------
        Nd : float
            Axial load on the RC column (kN).
        Mxd : float
            Bending moment on the RC column in the X direction (kNm).
        Myd : float
            Bending moment on the RC column in the Y direction (kNm).
        fcd : float
            Design value of concrete strength (kPa).
        fsyd : float
            Design value of steel strength (kPa).
        fsyk : float
            Characteristic value of steel strength (kPa).
        bx : float
            Breadth (width) along global X (m).
        by : float
            Breadth (width) along global Y (m).

        Returns
        -------
        Tuple[float, float]
            Required longitudinal reinforcement area of bars
            distributed along -x and -y on each side.

        Notes
        -----
        The design tables are created assuming rebars are evenly spaced.
        """
        # Convert units to N, mm
        Nd = Nd / N
        Mxd, Myd = Mxd / (N*mm), Myd / (N*mm)
        fcd, fsyd = fcd / MPa, fsyd / MPa
        bx, by = bx / mm, by / mm

        # Compute normalized parameters
        n = Nd / (fcd * bx * by)
        mx = 100 * Mxd / (fcd * (bx * by**2))
        my = 100 * Myd / (fcd * (by * bx**2))

        # Retrieve w and calculate areas
        n_values = np.arange(0.0, 1, 0.1)
        if n in n_values:  # Exact match
            key = f"S{fsyk:.0f}_n={n:.1f}"
            w = self._interpolate(self.data[key], mx, my)
            Asl = w * (fcd / fsyd) * bx * by / 100
            Asl = Asl * (mm**2)  # Convert mm2 to m2
            num_bars_int_b, num_bars_int_h, num_bars = self._find_num_bars(
                bx, by)
            rebar_area = Asl / num_bars
            Asl_x = (2 + num_bars_int_b) * rebar_area
            Asl_y = (2 + num_bars_int_h) * rebar_area
        else:
            n_lower_idx = np.searchsorted(n_values, n, side='right') - 1
            n_upper_idx = n_lower_idx + 1
            n_lower, n_upper = n_values[n_lower_idx], n_values[n_upper_idx]

            # Read closest tables
            key_lower = f"S{fsyk:.0f}_n={n_lower:.1f}"
            key_upper = f"S{fsyk:.0f}_n={n_upper:.1f}"

            # Perform bilinear interpolation
            w_lower = self._interpolate(self.data[key_lower], mx, my)
            w_upper = self._interpolate(self.data[key_upper], mx, my)

            # Interpolate between n_lower and n_upper
            w = np.interp(n, [n_lower, n_upper], [w_lower, w_upper])
            Asl = w * (fcd / fsyd) * bx * by / 100
            Asl = Asl * (mm**2)  # Convert mm2 to m2

            # Calculate areas in x and y direction of section
            num_bars_int_b, num_bars_int_h, num_bars = self._find_num_bars(
                bx, by)
            rebar_area = Asl / num_bars
            Asl_x = (2 + num_bars_int_b) * rebar_area
            Asl_y = (2 + num_bars_int_h) * rebar_area

        return Asl_x, Asl_y


ECONOMIC_MU: float = 0.25
"""Maximum mu value considered for the economic column design."""
MAX_NIU = 0.60
"""Maximum allowed value of axial load ratio. Section-8.2.6 in TS500-1984"""
table = DesignTableTR()
"""Design table data class used for computing required reinforcement area."""


class Column(ColumnBase):
    """Column object for design class: tr_7599."""

    steel: Steel
    """Steel material."""
    concrete: Concrete
    """Concrete material."""
    MIN_B_SQUARE: float = 0.25 * m
    """The default minimum square column dimension."""
    MIN_B_RECTANGLE: float = 0.25 * m
    """The default minimum rectangular column dimension."""

    @property
    def fctk(self) -> float:
        """
        Reference
        ---------
        Section 3.3.2 in T5500-1984

        Returns
        -------
        float
            Characteristic value of tensional concrete strength
            (in base units).
        """
        return (0.35 * (self.concrete.fck) ** (1 / 2)) * MPa

    @property
    def fctd(self) -> float:
        """
        Returns
        -------
        float
            Design value of tensional concrete strength (in base units).
        """
        return self.fctk / self.concrete.PARTIAL_FACTOR

    @property
    def rhol_max(self) -> float:
        """
        References
        ----------
        # Section 12.3.2 in TS500-1984

        Returns
        -------
        float
            Maximum allowed longitudinal reinforcement ratio.
        """
        return 0.04

    @property
    def rhol_min(self) -> float:
        """
        Reference
        ---------
        #Section 6.6 in TBEC-1975

        Returns
        -------
        float
            Minimum longitudinal reinforcement ratio.
        """

        return 0.01

    @property
    def rhoh_min(self) -> float:
        """
        Reference
        ---------
        Equation 6.1 in TBEC-1975

        Returns
        -------
        float
            Minimum transverse reinforcement ratio.
        """
        return max(0.12 * self.fck / self.fsyk, 0.01)

    def predesign_section_dimensions(self) -> None:
        """Does preliminary design of column.

        This method makes initial guess for section dimensions.
        """
        # Initial guess for column concrete area
        min_area = self.pre_Nd / (MAX_NIU * self.fck)
        # Determine initial dimensions
        if self.section == 1:  # Square section
            self.bx = min_area**0.5
            self.by = min_area**0.5
        elif self.section == 2:  # Rectangular section
            if self.orient == "x":  # Longer dimension is bx
                self.bx = (2 * min_area) ** 0.5
                self.by = 0.50 * self.bx
            elif self.orient == "y":  # Longer dimension is by
                self.by = (2 * min_area) ** 0.5
                self.bx = 0.50 * self.by
        # Check against minimum dimensions
        self.bx = max(ceil(20 * self.bx) / 20, self.min_b)
        self.by = max(ceil(20 * self.by) / 20, self.min_b)

    def verify_section_adequacy(self) -> None:
        """Verifies the column section dimensions for design forces."""
        # Maximum axial load ratio
        max_niu = max(
            self.envelope_forces.N1_pos,
            self.envelope_forces.N9_pos,
            abs(self.envelope_forces.N1_neg),
            abs(self.envelope_forces.N9_neg),
        ) / (self.Ag * self.fck)

        # Maximum moment ratio
        max_mu_x = max(
            self.envelope_forces.Mx1_pos,
            self.envelope_forces.Mx9_pos,
            abs(self.envelope_forces.Mx1_neg),
            abs(self.envelope_forces.Mx9_neg),
        ) / ((self.bx * self.by**2) * self.fcd)
        max_mu_y = max(
            self.envelope_forces.My1_pos,
            self.envelope_forces.My9_pos,
            abs(self.envelope_forces.My1_neg),
            abs(self.envelope_forces.My9_neg),
        ) / ((self.by * self.bx**2) * self.fcd)

        # Maximum shear force
        max_Vx = max(self.envelope_forces.Vx1, self.envelope_forces.Vx9)
        max_Vy = max(self.envelope_forces.Vy1, self.envelope_forces.Vy9)

        # Distance from extreme compression fiber to centroid of longitudinal
        # reinforcement.
        dx = 0.90 * self.bx
        dy = 0.90 * self.by

        # Maximum acceptable shear force # Eq. 8.49 in TS500-1984
        Vrdx = 0.25 * self.fcd * self.by * dx
        Vrdy = 0.25 * self.fcd * self.bx * dy

        if max_mu_y > ECONOMIC_MU or max_Vx > Vrdx:
            # Need to increase dimension parallel to global-x
            self.ok_x = False
        else:
            self.ok_x = True
        if max_mu_x > ECONOMIC_MU or max_Vy > Vrdy:
            # Need to increase dimension parallel to global-y
            self.ok_y = False
        else:
            self.ok_y = True
        if max_niu > MAX_NIU and self.ok_x and self.ok_y:
            # May increase both dimensions or random one?
            self.ok_x = False
            self.ok_y = False

    def compute_required_longitudinal_reinforcement(self) -> None:
        """Computes the required reinforcement area for design forces."""
        Asl_x = 2 * np.pi * 0.25 * ((0.014 * m) ** 2)
        Asl_y = 2 * np.pi * 0.25 * ((0.014 * m) ** 2)
        for force in self.design_forces:
            # Determine the required longitudinal reinforcement ratio
            N1d = 0 if force.N1 > 0 else abs(force.N1)
            N9d = 0 if force.N9 > 0 else abs(force.N9)

            ex = 0.1 * self.bx  # min. eccentr. in the x direct., TS500-1984
            ey = 0.1 * self.by  # min. eccentr. in the y direct., TS500-1984

            Mx1d_ecc = N1d * ex
            Mx9d_ecc = N9d * ex
            My1d_ecc = N1d * ey
            My9d_ecc = N9d * ey

            Mx1d = max(abs(force.Mx1), Mx1d_ecc)
            Mx9d = max(abs(force.Mx9), Mx9d_ecc)
            My1d = max(abs(force.My1), My1d_ecc)
            My9d = max(abs(force.My9), My9d_ecc)

            Asl_1_x, Asl_1_y = table.get_reinforcement(
                N1d, Mx1d, My1d, self.fcd, self.fsyd, self.steel.fsyk,
                self.bx, self.by
                )
            Asl_9_x, Asl_9_y = table.get_reinforcement(
                N9d, Mx9d, My9d, self.fcd, self.fsyd, self.steel.fsyk,
                self.bx, self.by
                )
            Asl_x = max(Asl_x, max(Asl_1_x, Asl_9_x))
            Asl_y = max(Asl_y, max(Asl_1_y, Asl_9_y))

        # Save the required longitudinal reinforcement values
        self.Aslx_req = Asl_x
        self.Asly_req = Asl_y

    def compute_required_transverse_reinforcement(self) -> None:
        """Computes the required transverse reinforcement for design forces."""
        # Distance of long. bars in tens. to extreme conc. fibers in compr.
        dx = (self.bx - 2 * self.cover - 0.008)
        dy = (self.by - 2 * self.cover - 0.008)

        # Minimum transverse reinforcement area to spacing ratio
        Ash_sh_min = self.rhoh_min * dy * dx
        Ashx_sh_min = Ash_sh_min * dx / (dx + dy)
        Ashy_sh_min = Ash_sh_min * dy / (dx + dy)

        # Design shear forces
        Vd_x = max(self.envelope_forces.Vx1, self.envelope_forces.Vx9)
        Vd_y = max(self.envelope_forces.Vy1, self.envelope_forces.Vy9)
        Nd = min(abs(self.envelope_forces.N1_neg),
                 abs(self.envelope_forces.N9_neg))

        # Transverse reinforcement computation, Section 8.3 in TS500-1984
        Vcr_x = 0.65 * (self.fctd / MPa) * (self.by / mm) * (dx / mm) * \
            (1 + 0.07 * (Nd / N) / (self.Ag / (mm**2))) / 1000
        Vc_x = 0.8 * Vcr_x
        Vcr_y = 0.65 * (self.fctd / MPa) * (self.bx / mm) * (dy / mm) * \
            (1 + 0.07 * (Nd / N) / (self.Ag / (mm**2))) / 1000
        Vc_y = 0.8 * Vcr_y

        # Transverse reinforcement computation
        if Vd_x <= Vcr_x:
            Ashx_sh = Ashx_sh_min
        else:
            Vw = Vd_x - Vc_x
            Ashx_sh = Vw / (self.fsyd * dx)

        if Vd_y <= Vcr_y:
            Ashy_sh = Ashy_sh_min
        else:
            Vw = Vd_y - Vc_y
            Ashy_sh = Vw / (self.fsyd * dy)

        # Save the required transverse reinforcement area to spacing ratio
        self.Ashx_sbh_req = max(Ashx_sh_min, Ashx_sh)
        self.Ashy_sbh_req = max(Ashy_sh_min, Ashy_sh)
