"""
Specific routines for defining and designing tr_0018_dch beams.

References
----------
TBEC-1998(TR)-Specification for Structures to be Built in Disaster Areas
TBEC-2007(TR)-Specification for Structures to be Built in Disaster Areas
TS500-2000(TR)-Design and Construction Rules for Reinforced Concrete Buildings
"""

# Imports from installed packages
from math import ceil
import numpy as np
from typing import Tuple, Optional

# Imports from the design class (tr_0018_dch) library
from .materials import Steel, Concrete

# Imports from bdim base library
from ..baselib.beam import BeamBase, Array3

# Imports from units library
from ....utils.units import MPa, m

# Constants
ECONOMIC_MU_EB: float = 0.25
"""Maximum mu value considered for the economic emergent beam design."""
ECONOMIC_MU_WB: float = 0.25
"""Maximum mu value considered for the economic wide beam design."""
EPS_CU = 0.003
"""Concrete crushing strain used for computing section capacity."""


class Beam(BeamBase):
    """Beam object for design class: tr_0018_dch."""

    steel: Steel
    """Steel material."""
    concrete: Concrete
    """Concrete material."""
    MIN_B_EB: float = 0.25 * m
    """The default minimum breadth (width) of emergent beams.TBEC-1998"""
    MIN_H_EB: float = 0.30 * m
    """The default minimum breadth (width) of emergent beams.TBEC-1998"""
    Ve1: Optional[float] = None
    """Beam capacity design shear force at 1st gaussian point"""
    Ve9: Optional[float] = None
    """Beam capacity design shear force at 9st gaussian point"""

    @property
    def max_b(self) -> float:
        """
        Reference
        ---------
        Section 7.4.1 in TBEC-1998
        Section 3.4.1 in TBEC-2007

        Returns
        -------
        float
            Computed maximum allowed section breadth (width).
        """
        if self.direction == "x":  # Beam is along x
            bc = max(col.by for col in self.columns if col)
        elif self.direction == "y":  # Beam is along y
            bc = max(col.bx for col in self.columns if col)
        b_max_code = bc + self.h
        # Masks for finding emergent beams
        bool1 = self.typology == 2
        bool2 = self.exterior
        bool3 = self.stairs_wg != 0.0
        if bool1 or bool2 or bool3:
            return min(b_max_code, self.MAX_B_EB)
        else:
            return min(b_max_code, self.MAX_B_WB)

    @property
    def max_h(self) -> float:
        """
        Reference
        ---------
        Section 7.4.1 in TBEC-1998
        Section 3.4.1 in TBEC-2007

        Returns
        -------
        float
            Computed maximum allowed section height (depth).
        """
        # Masks for finding emergent beams
        bool1 = self.typology == 2  # Emergent by default
        bool2 = self.exterior  # Forces exterior beams to emergent
        bool3 = self.stairs_wg != 0.0  # Forces stairs beams to be emergent

        if bool3:
            return self.MAX_H_EB
        else:
            if self.direction == 'x':  # Beam is along x
                bxmax = max(col.bx for col in self.columns if col)
                bxmin = min(col.bx for col in self.columns if col)
                Lnet = self.L - (bxmax + bxmin) / 2
            elif self.direction == 'y':  # Beam is along y
                bymax = max(col.by for col in self.columns if col)
                bymin = min(col.by for col in self.columns if col)
                Lnet = self.L - (bymax + bymin) / 2

            h_max_code = min(3.5 * self.b, Lnet / 4)
            if bool1 or bool2:
                return min(self.MAX_H_EB, h_max_code)
            else:
                return min(self.MAX_H_WB, h_max_code)

    @property
    def fctk(self) -> float:
        """
        Reference
        ---------
        Equation 3.1 in T5500-2000

        Returns
        -------
        float
            Characteristic tensional strength of concrete (in base units).
        """
        return (0.35 * (self.concrete.fck) ** (1 / 2)) * MPa

    @property
    def fctd(self) -> float:
        """
        Returns
        -------
        float
            Design value for characteristic tensional strength of concrete (in
            base units).
        """
        return self.fctk / self.concrete.PARTIAL_FACTOR

    @property
    def rhol_min_tens(self) -> float:
        """
        Reference
        ----------
        Equation 3.8 in TBEC-2007

        Returns
        -------
        float
            Minimum longitudinal reinforcement ratio in tension zone
        """
        return 0.8 * (self.fctd / self.fsyd)

    @property
    def rhol_max_tens(self) -> float:
        """
        Reference
        ----------
        Equation 7.5 in T5500-2000

        Returns
        -------
        float
            Maximum longitudinal reinforcement ratio in tens. and comp. zones
        """
        return 0.02

    @property
    def rhoh_min(self) -> float:
        """
        Reference
        ----------
        Equation 8.6 in T5500-2000

        Returns
        -------
        float
            Minimum transverse reinforcement ratio
        """
        return 0.3 * (self.fctd) / (self.fsyd)

    def predesign_section_dimensions(self, slab_h: float) -> None:
        """Does preliminary design of beam.

        This method makes initial guess for section dimensions.

        Parameters
        ----------
        slab_h : float
            Slab thickness.
        """
        # Unit conversions
        Md = self.pre_Md
        # Emergent beam cases
        bool1 = self.typology == 2
        bool2 = self.exterior
        bool3 = self.stairs_wg != 0.0
        if bool1 or bool2 or bool3:
            # Set section breadth to minimum
            self.b = self.min_b
            # Compute height for economic section, assuming d = 0.1h
            mu_h = ((Md / (ECONOMIC_MU_EB * self.fcd * self.b)) ** 0.5) / 0.9
            # Compute height to control deformations
            if self.stairs_wg != 0.0 or sum(self.slab_wg) != 0.0:
                # The beam carries a slab (stairs or floor slab)
                def_h = self.L / 12
            else:  # The beam is secondary gravity beam
                def_h = self.L / (0.9 * 18)
            # Compute height to provide support condition for slabs
            bh_s = 3 * slab_h  # Section 7.4.1 in TBEC-1998
            # Get the maximum slab computed from all
            self.h = max(self.min_h, bh_s, mu_h, def_h)
            # Iterate for aspect ratio consideration
            while self.h / self.b > self.MAX_ASPECT_RATIO_EB:
                # Increase breadth
                self.b += self.B_INCR_EB
                # Compute height for economic section, assuming d = 0.1h
                mu_h = ((Md / (ECONOMIC_MU_EB * self.fcd * self.b))
                        ** 0.5) / 0.9
                # Compute height to control deformations
                if self.stairs_wg != 0.0 or sum(self.slab_wg) != 0.0:
                    # The beam carries a slab (stairs or floor slab)
                    def_h = self.L / 12
                else:  # The beam is secondary gravity beam
                    def_h = self.L / (0.9 * 18)
                # Get the maximum slab computed from all
                self.h = max(self.min_h, bh_s, mu_h, def_h)
        # Wide beam cases
        else:
            # Set section height (slab thickness or minimum)
            self.h = max(slab_h, self.min_h)
            # Section widths
            if sum(self.slab_wg) == 0.0:  # Secondary gravity beams
                self.b = self.min_b  # Use minimum dimension
            else:  # Primary gravity beams
                # Set width based on economic mu value and minimum allowed
                self.b = max(
                    self.min_b,
                    (Md / (ECONOMIC_MU_WB * self.fcd * (0.9 * self.h) ** 2)),
                )
                while (
                    self.b > self.max_b
                    or self.b / self.h > self.MAX_ASPECT_RATIO_WB
                ):
                    self.h += self.H_INCR_WB
                    self.b = Md / (
                        ECONOMIC_MU_WB * self.fcd * (0.9 * self.h) ** 2
                    )
        # Round
        self.h = ceil(20 * self.h) / 20
        self.b = ceil(20 * self.b) / 20

    def verify_section_adequacy(self) -> None:
        """Verifies the beam section dimensions for design forces."""
        # mu values (dimensionless) for economic section (eng. practice)
        if self.typology == 1:
            mu_economic = ECONOMIC_MU_WB
        elif self.typology == 2:
            mu_economic = ECONOMIC_MU_EB

        # Distance from extreme compression fiber to centroid of longitudinal
        # tension reinforcement.
        d = 0.90 * self.h

        # Maximum of envelope forces
        if self.Ve1 is not None and self.Ve9 is not None:
            Vmax = max(self.Ve1, self.Ve9)
        else:
            Vmax = max(
                self.envelope_forces.V1,
                self.envelope_forces.V5,
                self.envelope_forces.V9,
            )

        Mmax = max(
            self.envelope_forces.M1_pos,
            self.envelope_forces.M5_pos,
            self.envelope_forces.M9_pos,
            abs(self.envelope_forces.M1_neg),
            abs(self.envelope_forces.M5_neg),
            abs(self.envelope_forces.M9_neg),
        )

        # Verify the adequacy of the section dimensions
        mu = Mmax / (self.fcd * self.b * d**2)
        Vrd_max = 0.22 * self.b * d * self.fcd  # Equation 8.7 in TS500-2000

        if mu < mu_economic and Vmax < Vrd_max:
            self.ok = True  # Ok
        else:
            self.ok = False  # Not ok

    def _get_long_area(self, Md: Array3
                       ) -> Tuple[Array3[np.float64], Array3[np.float64]]:
        """Beam design method to be used in compute_required_reinforcement
        method.

        Parameters
        ----------
        Md : np.ndarray
            Moment value to be used for beam design.

        Returns
        -------
        As_required : np.ndarray
            Required tension steel area.
        Asprime_required : np.ndarray
            Required compression steel area.
        """
        # Initial material and geometrical definitions
        fcd = self.fcd
        fyd = self.fsyd
        Es = self.Es
        bw = self.b
        dprime = 0.1 * self.h
        d = self.h - dprime

        # Definition of k1 and k3
        k1 = min(1 - 0.006 * self.fck / MPa, 0.85)
        k3 = 0.85

        # Bending moment calculation for the choice between single
        # and double reinforcement.
        Mr1 = 0.235 * fcd * bw * (d**2) * (1 - 0.1175 / k3)

        As_required = np.zeros(len(Md))
        Asprime_required = np.zeros(len(Md))
        mask = Md < Mr1
        if np.any(mask):  # Single reinforcement
            K = Md[mask] / (bw * d**2)
            rho = k3 * (fcd / fyd) * (1 - (1 - (2 * K) / (k3 * fcd)) ** 0.5)
            As_required[mask] = rho * bw * d
            Asprime_required[mask] = 0
        else:  # Double reinforcement
            As1 = 0.235 * (fcd / fyd) * bw * d
            Mr2 = Md[~mask] - Mr1
            As2 = Mr2 / (fyd * (d - dprime))
            epss_prime = 0.003 * (1 - (k1 * k3 / 0.235) * (dprime / d))
            sigmas_prime = epss_prime * Es

            if sigmas_prime >= fyd:
                sigmas_prime = fyd
            else:
                sigmas_prime = sigmas_prime

            As_required[~mask] = As1 + As2
            Asprime_required[~mask] = As2 * fyd / sigmas_prime

        return As_required, Asprime_required

    def compute_required_longitudinal_reinforcement(self) -> None:
        """Computes the required reinforcement area for design forces.

        Notes
        -----
        1. Top reinforcement is calculated as the maximum of required
        reinforcement in tension for maximum of negative bending moments
        and required reinforcement in compression for maximum of positive
        bending moments.
        2. Bottom reinforcement is calculated as the maximum of required
        reinforcement in compression for maximum of negative bending moments
        and required reinforcement in tension for maximum of positive
        bending moments.
        3. Required reinforcement is computed at different sections:
        start, mid, end.
        """

        # Design forces
        moment_pos = np.array(
            [
                self.envelope_forces.M1_pos,
                self.envelope_forces.M5_pos,
                self.envelope_forces.M9_pos,
            ]
        )
        moment_neg = np.array(
            [
                self.envelope_forces.M1_neg,
                self.envelope_forces.M5_neg,
                self.envelope_forces.M9_neg,
            ]
        )
        moment_neg = np.abs(moment_neg)

        # Longitudinal reinforcement computation
        # ...........................................................................

        # For positive moment envelope (+)
        Asl_pos_bot, Asl_pos_top = self._get_long_area(moment_pos)

        # For negative moment envelope (-)
        Asl_neg_top, Asl_neg_bot = self._get_long_area(moment_neg)

        # Determine required reinforcement at top and bottom
        Asl_bot = np.maximum(Asl_pos_bot, Asl_neg_bot)
        Asl_top = np.maximum(Asl_neg_top, Asl_pos_top)

        # Check against minimum longitudinal reinforcement area
        Asl_min_tens = self.rhol_min_tens * self.b * (0.9 * self.h)
        Asl_top = np.maximum(Asl_top, Asl_min_tens)
        Asl_bot = np.maximum(Asl_bot, Asl_min_tens)

        # Compression to tension reinf. ratio must be greater than 0.5
        # for 1st and 2nd seismic zones
        mask = Asl_top / Asl_bot < 0.5
        if any(mask):
            Asl_top[mask] = 0.5 * Asl_bot[mask]
        mask = Asl_bot / Asl_top < 0.5
        if any(mask):
            Asl_bot[mask] = 0.5 * Asl_top[mask]

        # Save required longitudinal steel area at top and bottom
        self.Asl_top_req = Asl_top
        self.Asl_bot_req = Asl_bot

    def compute_required_transverse_reinforcement(self) -> None:
        """Computes the required transverse reinforcement for design forces.

        Notes
        -----
        1. Required reinforcement is computed at different sections:
        start, mid, end.
        """
        # Shear forces due to gravity and earthquake loads
        Vd = np.array(
            [self.envelope_forces.V1, self.envelope_forces.V5,
             self.envelope_forces.V9]
        )

        # Design shear force (Ve1 and Ve9 are calculated in building.py)
        Ve = np.array([self.Ve1, self.envelope_forces.V5, self.Ve9])

        # Shear force due to gravity loads
        grav_forces = self.forces["G/seismic"] + self.forces["Q/seismic"]
        Vd_gravity = np.array([abs(grav_forces.V1), abs(grav_forces.V5),
                               abs(grav_forces.V9)])

        # Shear force resisted by concrete, Eq.8.1 in TS500-2000
        Vcr = 0.65 * self.fctd * self.b * (0.9 * self.h)
        Vc = 0.8 * Vcr

        # Transverse reinforcement computation,
        # Section 7.4.5 in TBEC-1998 and Section 3.4.5 in TBEC-2007
        Ash_sbh = np.zeros(len(Ve))

        # Ve <= Vcr case
        mask = Ve <= Vcr
        Ash_sbh[mask] = self.rhoh_min * self.b

        # Ve > Vcr case
        shear_force_for_reinforcement = np.where((Vd - Vd_gravity) >= 0.5 * Vd,
                                                 Ve, Ve - Vc)
        Ash_sbh[~mask] = shear_force_for_reinforcement[~mask] / \
            (self.fsyd * (0.9 * self.h))

        # Save required transverse reinforcement area to spacing ratio
        Ash_sbh_min = self.rhoh_min * self.b  # Min. transverse reinforcement
        self.Ash_sbh_req = np.maximum(Ash_sbh, Ash_sbh_min)
