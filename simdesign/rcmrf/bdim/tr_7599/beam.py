"""This module provides the beam class implementation for the ``tr_7599``
design class in the BDIM layer.
"""
# Imports from installed packages
import numpy as np
from typing import Tuple

# Imports from the design class (tr_7599) library
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


class Beam(BeamBase):
    """Beam implementation for design class ``tr_7599``.

    This class extends ``BeamBase`` by narrowing the attribute types
    and overriding design methods per TBEC-1975 and TS500-1984.

    Attributes
    ----------
    steel : ~simdesign.rcmrf.bdim.tr_7599.materials.Steel
        Steel material assigned to the beam.
    concrete : ~simdesign.rcmrf.bdim.tr_7599.materials.Concrete
        Concrete material assigned to the beam.
    MIN_B_EB: float
        The default minimum breadth (width) of emergent beams.
    MIN_H_EB: float
        The default minimum height (depth) of emergent beams.

    See Also
    --------
    :class:`~bdim.baselib.beam.BeamBase`
        Base class defining the core behaviour and configuration.

    References
    ----------
    TBEC (1975). *Afet Bölgelerinde Yapılacak Yapılar Hakkında Yönetmelik*.
    Resmi Gazete, Ankara, Türkiye.

    TS500 (1984). *Requirements for Design and Construction of Reinforced
    Concrete Structures*. Turkish Standards Institution (TSE), Ankara, Türkiye.
    """
    steel: Steel
    concrete: Concrete
    MIN_B_EB: float = 0.20 * m
    MIN_H_EB: float = 0.30 * m

    @property
    def fctk(self) -> float:
        """
        Returns
        -------
        float
            Characteristic value of tensional concrete strength
            (in base units).

        Notes
        -----
        Based on Section 3.3.2 in T5500-1984.
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
    def rhol_min_tens(self) -> float:
        """
        Returns
        -------
        float
            Minimum longitudinal reinforcement ratio in tension zone.

        Notes
        -----
        Based on Section 6.9 in TBEC-1975.
        """
        if self.steel.grade == "S220":
            return 0.005
        elif self.steel.grade == "S420":
            return 0.003

    @property
    def rhoh_min(self) -> float:
        """
        Returns
        -------
        float
            Minimum transverse reinforcement ratio.

        Notes
        -----
        Based on Equation 12.3 in TS500-1984.
        """
        return 0.15 * (self.fctd) / (self.fsyd)

    def verify_section_adequacy(self) -> None:
        """Verify the beam section dimensions for design forces.
        """
        # Economic mu values (dimensionless)
        if self.typology == 1:
            mu_economic = ECONOMIC_MU_WB
        elif self.typology == 2:
            mu_economic = ECONOMIC_MU_EB

        # Distance from extreme compression fiber to centroid of longitudinal
        # tension reinforcement.
        d = 0.90 * self.h

        # Maximum of envelope forces
        max_shear = max(
            self.envelope_forces.V1, self.envelope_forces.V5,
            self.envelope_forces.V9)
        max_moment = max(
            self.envelope_forces.M1_pos,
            self.envelope_forces.M5_pos,
            self.envelope_forces.M9_pos,
            abs(self.envelope_forces.M1_neg),
            abs(self.envelope_forces.M5_neg),
            abs(self.envelope_forces.M9_neg)
        )

        # Verify the adequacy of the section dimensions
        Vrd_max = 0.25 * self.fcd * self.b * d  # Eq. 8.49 in TS500-1984
        mu = max_moment / (self.fcd * self.b * d**2)

        if mu < mu_economic and max_shear < Vrd_max:
            self.ok = True  # Ok
        else:
            self.ok = False  # Not ok

    def _get_long_area(self, Md: Array3
                       ) -> Tuple[Array3[np.float64], Array3[np.float64]]:
        """Get longitudinal reinforcement area given bending moment.

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
        """Compute the required longitudinal reinforcement for design forces.

        Notes
        -----
        - Top reinforcement is calculated as the maximum of required
          reinforcement in tension for maximum of negative bending moments
          and required reinforcement in compression for maximum of positive
          bending moments.

        - Bottom reinforcement is calculated as the maximum of required
          reinforcement in compression for maximum of negative bending moments
          and required reinforcement in tension for maximum of positive
          bending moments.

        - Required reinforcement is computed at three different sections:
          start, middle, end.
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

        # Required area for positive moment envelope (+)
        Asl_pos_bot, Asl_pos_top = self._get_long_area(moment_pos)

        # Required area for negative moment envelope (-)
        Asl_neg_top, Asl_neg_bot = self._get_long_area(moment_neg)

        # Determine required reinforcement at top and bottom
        Asl_bot = np.maximum(Asl_pos_bot, Asl_neg_bot)
        Asl_top = np.maximum(Asl_neg_top, Asl_pos_top)

        # Check against minimum longitudinal reinforcement area
        Asl_min_tens = self.rhol_min_tens * self.b * (0.9 * self.h)
        Asl_top = np.maximum(Asl_top, Asl_min_tens)
        Asl_bot = np.maximum(Asl_bot, Asl_min_tens)

        # Compression to tension reinf. ratio must be greater than 0.333
        mask = Asl_top / Asl_bot < (1 / 3)
        if np.any(mask):
            Asl_top[mask] = (1 / 3) * Asl_bot[mask]
        mask = Asl_bot / Asl_top < (1 / 3)
        if np.any(mask):
            Asl_bot[mask] = (1 / 3) * Asl_top[mask]

        # Save required longitudinal steel area
        self.Asl_top_req = Asl_top
        self.Asl_bot_req = Asl_bot

    def compute_required_transverse_reinforcement(self) -> None:
        """Compute the required transverse reinforcement for design forces.

        Notes
        -----
        Reinforcement is computed at three sections: start, mid, and end.
        """
        # Design shear force
        Vd = np.array(
            [self.envelope_forces.V1, self.envelope_forces.V5,
             self.envelope_forces.V9]
        )

        # Transverse reinforcement computation, Section 8.3 in TBEC-1984
        Vcr = 0.65 * self.fctd * self.b * (0.9 * self.h)
        Ash_sbh = np.zeros(len(Vd))
        Ash_sbh_min = self.rhoh_min * self.b
        mask = Vd <= Vcr
        Ash_sbh[mask] = Ash_sbh_min
        Ash_sbh[~mask] = Vd[~mask] / (self.fsyd * (0.9 * self.h))
        Ash_sbh = np.maximum(Ash_sbh, Ash_sbh_min)

        # Save required transverse reinforcement area to spacing ratio
        self.Ash_sbh_req = Ash_sbh
