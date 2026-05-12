"""This module provides the beam class implementation for the ``eu_cdm``
design class in the BDIM layer.
"""
# Imports from installed packages
import numpy as np

# Imports from the design class (eu_cdm) library
from .materials import Steel, Concrete

# Imports from bdim base library
from ..baselib.beam import BeamBase

# Imports from units library
from ....utils.units import MPa, m

# Constants
ECONOMIC_MU_EB: float = 0.25
"""Maximum mu value considered for the economic emergent beam design."""
ECONOMIC_MU_WB: float = 0.25
"""Maximum mu value considered for the economic wide beam design."""
TAU_C_VECT = np.array(
    [0.5, 0.6, 0.65, 0.75, 0.85, 0.90, 1.00, 1.10, 1.15]) * MPa
"""Vector of allowable shear stresses that carried by the concrete or
vector of the design shear strength values of concrete."""
TAU_MAX_VECT = np.array([2.4, 3.2, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]) * MPa
"""Vector of allowable shear stresses that can be carried by
the beam section."""
FCK_VECT = np.array([12, 16, 20, 25, 30, 35, 40, 45, 50]) * MPa
"""Vector of characteristic concrete compressive strength values."""


class Beam(BeamBase):
    """Beam implementation for design class ``eu_cdm``.

    This class extends ``BeamBase`` by narrowing the attribute types
    and overriding design methods per REBAP (1983).

    Attributes
    ----------
    steel : ~simdesign.rcmrf.bdim.eu_cdm.materials.Steel
        Steel material assigned to the beam.
    concrete : ~simdesign.rcmrf.bdim.eu_cdm.materials.Concrete
        Concrete material assigned to the beam.
    MIN_B_EB: float : float
        The default minimum breadth (width) of emergent beams.

    See Also
    --------
    :class:`~bdim.baselib.beam.BeamBase`
        Base class defining the core behaviour and configuration.

    References
    ----------
    REBAP (1983). Regulamento de Estruturas de Betão Armado e Pré-Esforçado.
    Decreto-Lei N.° 349-C/83, Lisbon, Portugal.

    d'Arga e Lima, J., Monteiro, V., Mun, M. (2005).
    Betão armado: esforços normais e de flexão: REBAP-83.
    Laboratório Nacional de Engenharia Civil, Lisboa.
    """
    steel: Steel
    concrete: Concrete
    MIN_B_EB: float = 0.25 * m

    @property
    def rhol_min_tens(self) -> float:
        """
        Returns
        -------
        float
            Minimum longitudinal reinforcement ratio in tension zone.
        """
        # Art 90.1 in REBAP (1983)
        if self.steel.grade == "A500":
            return 0.12 / 100
        elif self.steel.grade == "A400":
            return 0.15 / 100
        elif self.steel.grade == "A235":
            return 0.25 / 100

    @property
    def rhol_max_tens(self) -> float:
        """
        Returns
        -------
        float
            Maximum longitudinal reinforcement ratio in tension
            and compression zones.
        """
        # Art 90.2 in REBAP (1983)
        return 0.04

    @property
    def rhoh_min(self) -> float:
        """
        Returns
        -------
        float
            Minimum transverse reinforcement ratio.
        """
        # Art 94.2 in REBAP (1983)
        if self.steel.grade == "A500":
            return 0.08 / 100
        elif self.steel.grade == "A400":
            return 0.10 / 100
        else:
            return 0.16 / 100

    def verify_section_adequacy(self) -> None:
        """Verify the beam section dimensions for design forces.
        """
        # Dimensionless mu values for economic section from REBAP book
        # This can be considered as an engineering practice
        if self.typology == 1:  # Wide Beam
            mu_max = ECONOMIC_MU_WB
        elif self.typology == 2:  # Emergent Beam
            mu_max = ECONOMIC_MU_EB

        # Allowable shear stress that can be carried by the beam
        tau_max = np.interp(self.concrete.fck, FCK_VECT, TAU_MAX_VECT)
        # Distance from extreme compression fiber to centroid of longitudinal
        # tension reinforcement.
        d = 0.9 * self.h

        # Maximum of envelope forces
        max_shear = max(self.envelope_forces.V1, self.envelope_forces.V5,
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
        tau = max_shear / (self.b * d)  # for max. shear force
        mu = max_moment / (self.fcd * self.b * d**2)  # for max. bending moment
        if mu < mu_max and tau < tau_max:
            self.ok = True  # Ok
        else:
            self.ok = False  # Not ok

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
        # Distance from extreme compression fiber to centroid of longitudinal
        # tension reinforcement.
        d = 0.9 * self.h
        # Dimensionless limit values
        mu_lim = 0.31  # mu limit defined in REBAP-83
        omega_lim = 0.41  # omega limit defined in REBAP-83
        # Design forces
        moment_pos = np.array([self.envelope_forces.M1_pos,
                               self.envelope_forces.M5_pos,
                               self.envelope_forces.M9_pos])
        moment_neg = np.array([abs(self.envelope_forces.M1_neg),
                               abs(self.envelope_forces.M5_neg),
                               abs(self.envelope_forces.M9_neg)])
        # Reinforcement area computation for positive moment envelope (+)
        # REBAP pp. 33
        mu_pos = moment_pos / (self.fcd * self.b * d**2)
        # REBAP pp. 35, eq 11
        omega_pos_prime = (mu_pos - mu_lim) / (1 - (self.cover / (d)))
        # REBAP pp. 35, eq 10
        omega_pos_prime[mu_pos <= mu_lim] = 0
        # REBAP pp. 35, eq 11
        omega_pos = omega_lim + omega_pos_prime
        # REBAP pp. 35, eq 10
        omega_pos[mu_pos <= mu_lim] = (
            mu_pos[mu_pos <= mu_lim] * (1 + mu_pos[mu_pos <= mu_lim]))
        # Reinforcement area computation for negative moment envelope (-)
        # REBAP pp. 33
        mu_neg = moment_neg / (self.fcd * self.b * d**2)
        # REBAP pp. 35, eq 11
        omega_neg_prime = (mu_neg - mu_lim) / (1 - (self.cover / (d)))
        # REBAP pp. 35, eq 10
        omega_neg_prime[mu_neg <= mu_lim] = 0
        # REBAP pp. 35, eq 11
        omega_neg = omega_lim + omega_neg_prime
        # REBAP pp. 35, eq 10
        omega_neg[mu_neg <= mu_lim] = (
            mu_neg[mu_neg <= mu_lim] * (1 + mu_neg[mu_neg <= mu_lim]))
        # Prime is used for compression reinforcement.
        # It can be both at top and bottom due to seismic loading
        omega_pos = np.maximum(omega_pos, omega_neg_prime)
        omega_neg = np.maximum(omega_neg, omega_pos_prime)
        # Determine required reinforcement at top and bottom
        Asl_top = omega_neg * self.b * d * self.fcd / self.fsyd
        Asl_bot = omega_pos * self.b * d * self.fcd / self.fsyd
        # Check against minimum longitudinal reinforcement area
        Asl_min_top = self.rhol_min_tens * self.b * d  # REBAP 90.1
        Asl_min_bot = self.rhol_min_tens * self.b * d  # REBAP 90.1
        Asl_top = np.maximum(Asl_top, Asl_min_top)
        Asl_bot = np.maximum(Asl_bot, Asl_min_bot)
        # Save required longitudinal reinforcement area
        self.Asl_top_req = Asl_top
        self.Asl_bot_req = Asl_bot

    def compute_required_transverse_reinforcement(self) -> None:
        """Compute the required transverse reinforcement for design forces.

        Notes
        -----
        Reinforcement is computed at three sections: start, mid, and end.
        """
        # Allowable shear stress that can be carried by the beam
        tau_c = np.interp(self.concrete.fck, FCK_VECT, TAU_C_VECT)
        # Distance from extreme compression fiber to centroid of longitudinal
        # tension reinforcement.
        d = 0.9 * self.h
        # lever arm, i.e., distance between comp. and tens. forces
        z = 0.9 * d
        # Design forces
        shear = np.array([self.envelope_forces.V1,
                          self.envelope_forces.V5,
                          self.envelope_forces.V9])
        # Calculate the minimum shear reinforcement
        Ash_sbh_min = self.rhoh_min * self.b  # REBAP 1983 - Art 94.2
        # REBAP 1983 - Art 53.1 V < Vcd + Vwd
        Vcd = tau_c * self.b * d  # Article 53.2
        Ash_sbh = (shear - Vcd) / (z * self.fsyd)  # Art 53.3
        Ash_sbh = np.maximum(Ash_sbh, Ash_sbh_min)
        # Save required transverse reinforcement area to spacing ratio
        self.Ash_sbh_req = Ash_sbh
