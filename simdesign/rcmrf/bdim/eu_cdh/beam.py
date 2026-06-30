"""This module provides the beam class implementation for the ``eu_cdh``
design class in the BDIM layer.
"""
# Imports from installed packages
import numpy as np
from typing import Literal

# Imports from the design class (eu_cdh) library
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


class Beam(BeamBase):
    """Beam implementation for design class ``eu_cdh``.

    This class extends ``BeamBase`` by narrowing the attribute types
    and overriding design methods per Eurocodes 2 and 8.

    Attributes
    ----------
    steel : ~simdesign.rcmrf.bdim.eu_cdh.materials.Steel
        Steel material assigned to the beam.
    concrete : ~simdesign.rcmrf.bdim.eu_cdh.materials.Concrete
        Concrete material assigned to the beam.
    MIN_B_EB: float : float
        The default minimum breadth (width) of emergent beams.

    See Also
    --------
    :class:`~simdesign.rcmrf.bdim.baselib.beam.BeamBase`
        Base class defining the core behaviour and configuration.

    References
    ----------
    Comité Européen de Normalisation, CEN (2004). Eurocode 2: Design of
    Concrete Structures — Part 1-1: General Rules and Rules for Buildings.
    European Committee for Standardization, Brussels, Belgium.

    Comité Européen de Normalisation, CEN (2004). Eurocode 8: Design of
    Structures for Earthquake Resistance — Part 1: General Rules,
    Seismic Actions and Rules for Buildings.
    European Committee for Standardization, Brussels, Belgium.

    d'Arga e Lima, J., Monteiro, V., Mun, M. (2005).
    Betão armado: esforços normais e de flexão: REBAP-83.
    Laboratório Nacional de Engenharia Civil, Lisboa.

    Notes
    -----
    - Max aspect ratio indicated in EN 1992-1-1:2004 5.9(3) eqn. 5.40a is
      ignored for now.
    - EC8 5.5.1.2.1(1)P states the minimum width as 200mm, smaller than the
      default 250 mm.
    """
    steel: Steel
    concrete: Concrete
    MIN_B_EB: float = 0.25 * m

    @property
    def Iy_eff(self) -> float:
        """
        Returns
        -------
        float
            Moment of inertia around y-axis of the beam.
        """
        return 0.5 * self.Iy  # EN 1998-1:2004 4.3.1(7)

    @property
    def Iz_eff(self) -> float:
        """
        Returns
        -------
        float
            Moment of inertia around z-axis of the beam.
        """
        return 0.5 * self.Iz  # EN 1998-1:2004 4.3.1(7)

    @property
    def rhol_max_tens(self) -> float:
        """
        Returns
        -------
        float
            Maximum longitudinal reinforcement ratio in tension
            and compression zones.
        """
        # EN 1992-1-1:2004, 9.2.1.1(3)
        return 0.04

    @property
    def rhoh_min(self) -> float:
        """
        Returns
        -------
        float
            Minimum transverse reinforcement ratio.
        """
        # EN 1992-1-1:2004, 9.2.2(5), Eqn. 9.5N
        return 0.08 * ((self.fck / MPa) ** 0.5) / (self.fsyk / MPa)

    def get_rhol_min_tens(self, case: Literal['seismic', 'gravity']) -> float:
        """
        Returns
        -------
        float
            Minimum longitudinal reinforcement ratio in tension zone.
        """
        fctm = (0.3 * (self.fck / MPa) ** (2 / 3)) * MPa
        if case == 'seismic':
            # EN 1998-1:2004, Eqn. 5.12
            return 0.50 * (fctm / self.fsyk)
        else:
            # EN 1992-1-1:2004, Eqn. 9.1N
            return max(0.26 * (fctm / self.fsyk), 0.0013)

    def verify_section_adequacy(self) -> None:
        """Verify the beam section dimensions for design forces.
        """
        # Dimensionless mu values for economic section from REBAP book
        # This can be considered as an engineering practice
        if self.typology == 1:  # Wide Beam
            mu_max = ECONOMIC_MU_WB
        elif self.typology == 2:  # Emergent Beam
            mu_max = ECONOMIC_MU_EB
        # Distance from extreme compression fiber to centroid of longitudinal
        # tension reinforcement.
        d = 0.9 * self.h
        z = 0.9 * d  # lever arm, i.e., distance between comp. and tens. forces
        # Following EC2-1/6.2.3: Members with vertical shear reinforcement
        # Strength reduction factor for concrete cracked in shear
        v = 0.6 * (1 - self.fck / (250 * MPa))  # Eqn 6.6N
        if self.fsyd / self.fsyk >= 0.80:
            v1 = v  # Note 1: Recommended strength reduction factor
        else:  # Note 2: If fsyd is below 80% of fsyk
            if self.fck <= 60 * MPa:
                v1 = 0.6
            else:
                v1 = max(0.6 * (1 - self.fck / (200 * MPa)), 0.5)
        # Coefficient taking account the stress state in the comp. chord
        alpha_cw = 1.0  # assuming no axial force (beams), eqn. 6.11aN
        # Angle between the conc. comp. strut and the beam axis perp. to shear
        theta = 21.80140948635181  # in degrees, based on eqn. 6.7N
        theta = 45  # in degrees, based on eqn. 6.7N
        tan_theta = np.tan(theta * np.pi / 180)  # 0.4 - 1.0
        cot_theta = 1 / tan_theta  # 1.0 - 2.5
        # Assuming vertical shear reinforcement is provided: Eqn. 6.9
        Vrd_max = (alpha_cw * self.b * z * v1 * self.fcd) / (
            cot_theta + tan_theta)
        # Maximum of envelope forces
        Vmax = max(self.envelope_forces.V1, self.envelope_forces.V5,
                   self.envelope_forces.V9)
        Mmax = max(
            self.envelope_forces.M1_pos,
            self.envelope_forces.M5_pos,
            self.envelope_forces.M9_pos,
            abs(self.envelope_forces.M1_neg),
            abs(self.envelope_forces.M5_neg),
            abs(self.envelope_forces.M9_neg)
        )
        # Verify the adequacy of the section dimensions
        mu = Mmax / (self.fcd * self.b * d**2)  # for max. bending moment
        if mu < mu_max and Vmax < Vrd_max:
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
          start, middle, end.rcement is computed at different sections:
          start, mid, end.
        """
        # Distance from extreme compression fiber to centroid of longitudinal
        # tension reinforcement.
        d = 0.9 * self.h
        # Dimensionless limit values
        mu_lim = 0.37  # mu limit defined in REBAP book
        omega_lim = 0.41  # omega limit defined in REBAP book
        combo_types = [forces.case for forces in self.design_forces]
        if "seismic" in combo_types:
            rhol_min_tens = self.get_rhol_min_tens("seismic")
        else:
            rhol_min_tens = self.get_rhol_min_tens("gravity")
        # Design forces
        moment_pos = np.array([self.envelope_forces.M1_pos,
                               self.envelope_forces.M5_pos,
                               self.envelope_forces.M9_pos])
        moment_neg = np.array([abs(self.envelope_forces.M1_neg),
                               abs(self.envelope_forces.M5_neg),
                               abs(self.envelope_forces.M9_neg)])
        # Reinforcement computation for positive moment envelope (+)
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
            mu_pos[mu_pos <= mu_lim] * (1 + 0.75*mu_pos[mu_pos <= mu_lim]))
        # Reinforcement computation for negative moment envelope (-)
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
            mu_neg[mu_neg <= mu_lim] * (1 + 0.75*mu_neg[mu_neg <= mu_lim]))
        # Prime is used for compression reinforcement.
        # It can be both at top and bottom due to seismic loading
        omega_pos = np.maximum(omega_pos, omega_neg_prime)
        omega_neg = np.maximum(omega_neg, omega_pos_prime)
        # Determine required reinforcement at top and bottom
        Asl_top = omega_neg * self.b * d * self.fcd / self.fsyd
        Asl_bot = omega_pos * self.b * d * self.fcd / self.fsyd
        # Check against minimum longitudinal reinforcement area
        Asl_min_tens = rhol_min_tens * self.b * d
        Asl_top = np.maximum(Asl_top, Asl_min_tens)
        Asl_bot = np.maximum(Asl_bot, Asl_min_tens)
        # EC 8-1 / 5.4.3.1.2 (4a) Detailing for local ductility
        # Compression to tension reinf. ratio must be greater than 0.5
        mask1 = Asl_top/Asl_bot < 0.5
        if np.any(mask1):
            Asl_top[mask1] = 0.5*Asl_bot[mask1]
        mask1 = Asl_bot/Asl_top < 0.5
        if np.any(mask1):
            Asl_bot[mask1] = 0.5*Asl_top[mask1]
        # Save required longitudinal steel area at top and bottom
        self.Asl_top_req = Asl_top
        self.Asl_bot_req = Asl_bot

    def compute_required_transverse_reinforcement(self) -> None:
        """Compute the required transverse reinforcement for design forces.

        Notes
        -----
        Reinforcement is computed at three sections: start, mid, and end.
        """
        # Distance from extreme compression fiber to centroid of longitudinal
        # tension reinforcement.
        d = 0.9 * self.h
        # lever arm, i.e., distance between comp. and tens. forces
        z = 0.9 * d
        # Design forces
        Ved = np.array([self.envelope_forces.V1,
                        self.envelope_forces.V5,
                        self.envelope_forces.V9])
        # Transverse reinforcement computation
        cot_theta = 1.0  # assuming theta = 45 degrees
        Ash_sbh = Ved / (z * self.fsyd * cot_theta)  # EC 2-1, eqn. 6.8
        Ash_sbh_min = self.rhoh_min * self.b  # Min. transverse reinforcement
        Ash_sbh = np.maximum(Ash_sbh, Ash_sbh_min)
        # Save required transverse reinforcement area to spacing ratio
        self.Ash_sbh_req = Ash_sbh
