"""This module provides the column class implementation for the ``eu_cdh``
design class in the BDIM layer.
"""
# Imports from installed packages
from math import ceil
import numpy as np
from typing import Dict, List, Literal, Tuple

# Imports from the design class (eu_cdh) library
from .materials import Steel, Concrete

# Imports from bdim base library
from ..baselib.column import ColumnBase

# Imports from units library
from ....utils.units import MPa, m
from ....utils.rcsection import build_column_rebar_layout, get_sum_wi_sq

# Constants
ECONOMIC_MU: float = 0.25
"""Maximum mu value considered for the economic column design."""
MAX_NIU = 0.65
"""Maximum allowed value of axial load ratio.
For DCM columns, 0.65 according to Eurocode 8 - Part 1: 5.4.3.2.1(3)P
For DCH columns, 0.55 according to Eurocode 8 - Part 1: 5.5.3.2.1(3)P
"""
BETA_FC_VECTOR = [1.00, 0.93, 0.88, 0.88, 0.93]
"""Stress block coefficients for different axial load ratio (in REBAP 1983)."""
NIU_VECTOR = [0.40, 0.50, 0.60, 0.70, 0.85]
"""Axial load ratio corresponding to each stress block coefficient."""


class Column(ColumnBase):
    """Column implementation for design class ``eu_cdh``.

    This class extends ``ColumnBase`` by narrowing the attribute types
    and overriding design methods per Eurocodes 2 and 8.

    Attributes
    ----------
    steel : ~simdesign.rcmrf.bdim.eu_cdh.materials.Steel
        Steel material assigned to the column.
    concrete : ~simdesign.rcmrf.bdim.eu_cdh.materials.Concrete
        Concrete material assigned to the column.

    See Also
    --------
    :class:`~simdesign.rcmrf.bdim.baselib.column.ColumnBase`
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
    """
    steel: Steel
    concrete: Concrete

    @property
    def Ix_eff(self) -> float:
        """
        Returns
        -------
        float
            Effective column moment of inertia around x-axis.
        """
        return 0.5 * self.Ix  # EN 1998-1:2004 4.3.1(7)

    @property
    def Iy_eff(self) -> float:
        """
        Returns
        -------
        float
            Effective column moment of inertia around y-axis.
        """
        return 0.5 * self.Iy  # EN 1998-1:2004 4.3.1(7)

    @property
    def rhol_max(self) -> float:
        """
        Returns
        -------
        float
            Maximum longitudinal reinforcement ratio.
        """
        return 0.04  # EN 1992-1-1:2004 9.5.2(3)

    @property
    def rhol_min(self) -> float:
        """
        Returns
        -------
        float
            Minimum longitudinal reinforcement ratio.
        """
        min_tensile_force = min(
            self.envelope_forces.N1_pos,
            self.envelope_forces.N9_pos,
        )
        if min_tensile_force > 0.0:  # Tensile axial force
            Ned = 0.0
        else:  # Compressive axial force
            Ned = min(
                abs(self.envelope_forces.N1_neg),
                abs(self.envelope_forces.N9_neg),
            )
        # EN 1992-1-1:2004 9.5.2(2)
        rhol_min_ec2 = max(0.1 * Ned / self.fsyd, 0.002 * self.Ag) / self.Ag
        # 0.01 is introduced as a rule of thumb from practical point.
        # It is not a code requirement.
        return max(0.01, rhol_min_ec2)

    @property
    def rhoh_min(self) -> float:
        """
        Returns
        -------
        float
            Minimum transverse reinforcement ratio.

        Notes
        -----
        The equation used herein is originally defined for beams.
        We keep using it for columns just to ensure safety.
        """
        # EN 1992-1-1:2004, 9.2.2(5), Eqn. 9.5N
        return 0.08 * ((self.fck / MPa) ** 0.5) / (self.fsyk / MPa)

    def predesign_section_dimensions(self) -> None:
        """Make an initial guess for column section dimensions.

        Notes
        -----
        This method overrides ``ColumnBase.predesign_section_dimensions``
        with the following changes:

        - Minimum cross section area is calculated based on axial load ratio
          limit from EC8.
        """
        # Initial guess for column concrete area
        min_area = self.pre_Nd / (self.fcd * MAX_NIU)
        # Determine initial dimensions
        if self.section == 1:  # Square section
            self.bx = (min_area**0.5)
            self.by = (min_area**0.5)
        elif self.section == 2:  # Rectangular section
            if self.orient == 'x':  # Longer dimension is bx
                self.bx = (2 * min_area) ** 0.5
                self.by = 0.5 * self.bx
            elif self.orient == 'y':  # Longer dimension is by
                self.by = (2 * min_area) ** 0.5
                self.bx = 0.5 * self.by
        # Check against minimum dimensions
        self.bx = max(ceil(20 * self.bx) / 20, self.min_b)
        self.by = max(ceil(20 * self.by) / 20, self.min_b)

    def verify_section_adequacy(self) -> None:
        """Verify the adequacy of section dimensions for design forces.

        Notes
        -----
        - In accordance with EN 1992-1-1:2004 5.4.3.2.1(2) biaxial bending
          is taken into account by decreasing the uniaxial moment of resistance
          by 30%.
        """
        # Distance from extreme compression fiber to centroid of longitudinal
        # tension reinforcement.
        dx = 0.9 * self.bx
        dy = 0.9 * self.by
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
        alpha_cw = 1.0  # assuming no axial force (tension case), eqn. 6.11aN
        # Angle between the conc. comp. strut and the beam axis perp. to shear
        theta = 21.80140948635181  # in degrees, based on eqn. 6.7N
        theta = 45  # in degrees, based on eqn. 6.7N
        tan_theta = np.tan(theta * np.pi / 180)  # 0.4 - 1.0
        cot_theta = 1 / tan_theta  # 1.0 - 2.5
        # lever arm, i.e., distance between comp. and tens. forces
        zx = 0.9 * dx
        zy = 0.9 * dy
        # Assuming vertical shear reinforcement is provided: Eqn. 6.9
        Vrdx = (alpha_cw * self.by * zx * v1 * self.fcd) / (
            cot_theta + tan_theta
        )
        Vrdy = (alpha_cw * self.bx * zy * v1 * self.fcd) / (
            cot_theta + tan_theta
        )

        # Maximum axial load ratio
        max_niu = max(
            self.envelope_forces.N1_pos,
            self.envelope_forces.N9_pos,
            abs(self.envelope_forces.N1_neg),
            abs(self.envelope_forces.N9_neg),
        ) / (self.Ag * self.fcd)
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
        max_Vx = max(
            self.envelope_forces.Vx1,
            self.envelope_forces.Vx9
        )
        max_Vy = max(
            self.envelope_forces.Vy1,
            self.envelope_forces.Vy9
        )

        # Verify the adequacy of the section dimensions
        if (max_mu_y / 0.70) > ECONOMIC_MU or max_Vx > Vrdx:
            # Need to increase dimension parallel to global-x
            self.ok_x = False
        else:
            self.ok_x = True
        if (max_mu_x / 0.70) > ECONOMIC_MU or max_Vy > Vrdy:
            # Need to increase dimension parallel to global-y
            self.ok_y = False
        else:
            self.ok_y = True
        if max_niu > MAX_NIU and self.ok_x and self.ok_y:
            # May increase both dimensions or random one?
            self.ok_x = False
            self.ok_y = False

    def compute_required_longitudinal_reinforcement(self) -> None:
        """Compute the required longitudinal reinforcement for design forces.

        Notes
        -----
        - In accordance with EN 1992-1-1:2004 5.4.3.2.1(2) biaxial bending
          is taken into account by decreasing the uniaxial moment of resistance
          by 30%.
        """
        # Initial longitudinal reinforcement area
        Aslx_req = 2 * np.pi * 0.25 * ((0.012 * m)**2)  # Minimum reinforcement
        Asly_req = 2 * np.pi * 0.25 * ((0.012 * m)**2)  # Minimum reinforcement
        for force in self.design_forces:
            # Dimensionless design force quantities
            niu_1 = (-force.N1) / (self.Ag * self.fcd)
            niu_9 = (-force.N9) / (self.Ag * self.fcd)
            mu_x1 = abs(force.Mx1) / ((self.bx * self.by**2) * self.fcd) / 0.7
            mu_y1 = abs(force.My1) / ((self.by * self.bx**2) * self.fcd) / 0.7
            mu_x9 = abs(force.Mx9) / ((self.bx * self.by**2) * self.fcd) / 0.7
            mu_y9 = abs(force.My9) / ((self.by * self.bx**2) * self.fcd) / 0.7
            # Determine the required longitudinal reinforcement ratio
            beta1 = np.interp(niu_1, NIU_VECTOR, BETA_FC_VECTOR)
            beta9 = np.interp(niu_9, NIU_VECTOR, BETA_FC_VECTOR)
            lambda_y = 0.5 - self.cover / self.bx
            lambda_x = 0.5 - self.cover / self.by
            niuc_1 = niu_1 - 0.85
            niuc_9 = niu_9 - 0.85
            # Start section
            if niu_1 < 0.0:  # Axial force is tensile
                # REBAP (1983), pp. 48, eqn. 22
                omega_x1 = mu_x1 / (lambda_x * beta1) - niu_1
                omega_y1 = mu_y1 / (lambda_y * beta1) - niu_1
            elif niu_1 <= 0.85:
                omega_x1 = (mu_x1 + 0.55 * niu_1 * niuc_1) / (lambda_x * beta1)
                omega_y1 = (mu_y1 + 0.55 * niu_1 * niuc_1) / (lambda_y * beta1)
            else:
                omega_x1 = mu_x1 / (lambda_x * beta1) + niuc_1
                omega_y1 = mu_y1 / (lambda_y * beta1) + niuc_1
            # End section
            if niu_9 < 0.0:  # Axial force is tensile
                # REBAP (1983), pp. 48, eqn. 22
                omega_x9 = mu_x9 / (lambda_x * beta9) - niu_9
                omega_y9 = mu_y9 / (lambda_y * beta9) - niu_9
            elif niu_9 <= 0.85:
                omega_x9 = (mu_x9 + 0.55 * niu_9 * niuc_9) / (lambda_x * beta9)
                omega_y9 = (mu_y9 + 0.55 * niu_9 * niuc_9) / (lambda_y * beta9)
            else:
                omega_x9 = mu_x9 / (lambda_x * beta9) + niuc_9
                omega_y9 = mu_y9 / (lambda_y * beta9) + niuc_9
            # Compute required reinforcement area on two sides
            omega_x = max(omega_x1, omega_x9)
            omega_y = max(omega_y1, omega_y9)
            Aslx = (0.5 * omega_x * self.Ag * self.fcd / self.fsyd)
            Asly = (0.5 * omega_y * self.Ag * self.fcd / self.fsyd)
            # Update the reinforcement area
            Aslx_req = max(Aslx_req, Aslx)
            Asly_req = max(Asly_req, Asly)
        # Save the required longitudinal reinforcement area
        # on each side, along x and y axes
        self.Aslx_req = Aslx_req
        self.Asly_req = Asly_req

    def compute_required_transverse_reinforcement(self) -> None:
        """Compute the required transverse reinforcement for design forces.
        """
        # Distance of long. bars in tens. to extreme conc. fibers in compr.
        dx = 0.9 * self.bx
        dy = 0.9 * self.by
        # lever arm, i.e., distance between comp. and tens. forces
        zx = 0.9 * dx
        zy = 0.9 * dy
        # Compression strut angle, EN 1992-1-1:2004 eqn. 6.7N
        """TODO: This could 2.0 for both beams and columns.
        1.0 is not ralistic (too conservative)."""
        cot_theta = 1.0  # 45 degrees
        # Initial transverse reinforcement area to spacing ratio
        Ashx_sh_min = self.rhoh_min * self.by
        Ashy_sh_min = self.rhoh_min * self.bx
        # Design forces
        Ved_x = max(self.envelope_forces.Vx1, self.envelope_forces.Vx9)
        Ved_y = max(self.envelope_forces.Vy1, self.envelope_forces.Vy9)
        # EN 1992-1-1:2004 6.2.3(3) eqn. 6.8
        Ashx_sh = Ved_x / (zx * self.fsyd * cot_theta)
        Ashy_sh = Ved_y / (zy * self.fsyd * cot_theta)
        # Save the required ratio of transverse reinforcement area along
        # x and y axes to the reinforcement spacing
        self.Ashx_sbh_req = max(Ashx_sh_min, Ashx_sh)
        self.Ashy_sbh_req = max(Ashy_sh_min, Ashy_sh)

    def check_local_ductility_requirement(
        self, combo_grav_factors: List[Dict[Literal['G', 'Q'], float]],
        q0: float = 3.9, T1: float | None = None, Tc: float | None = None
    ) -> Tuple[bool, float, float]:
        """Checks the confinement of the critical region at the base of the
        column against the local ductility requirement of EN 1998-1:2004,
        5.4.3.2.2(8), Eq. 5.15:

        ``alpha omega_wd >= 30 mu_phi nu_d eps_syd bc / b0 - 0.035``

        Parameters
        ----------
        combo_grav_factors : List[Dict[Literal['G', 'Q'], float]]
            Gravity load factors of the seismic load combinations, e.g., from
            the ``_get_unique_seism_combo_grav_factors`` method of the
            building. The largest normalised axial force ``nu_d`` governs.
        q0 : float, optional
            Basic value of the behaviour factor. By default 3.9, i.e.,
            ``3.0 alpha_u / alpha_1`` with ``alpha_u / alpha_1 = 1.3`` for a
            multi-storey, multi-bay frame of DCM (EN 1998-1:2004, 5.2.2.2).
        T1 : float | None, optional
            Fundamental period of the building. If None (or `Tc` is None),
            ``T1 >= Tc`` is assumed. By default None.
        Tc : float | None, optional
            Corner period of the constant spectral acceleration branch.
            By default None.

        Returns
        -------
        ok : bool
            True if the requirement is satisfied.
        alpha_omega_wd : float
            Provided value ``alpha omega_wd``.
        required : float
            Required value ``30 mu_phi nu_d eps_syd bc / b0 - 0.035``.

        Notes
        -----
        - The check applies to the critical regions at the base of primary
          seismic columns; the caller selects these columns. The column
          attributes are not changed.
        - Curvature ductility factor (EN 1998-1:2004, 5.2.3.4(3), Eq. 5.4):
          ``mu_phi = 2 q0 - 1`` if ``T1 >= Tc``, otherwise
          ``mu_phi = 1 + 2 (q0 - 1) Tc / T1``. The periods are not estimated
          by the design; without them ``T1 >= Tc`` is assumed, which gives
          the smaller value for short-period buildings.
        - ``omega_wd`` is the mechanical volumetric ratio of the hoops within
          the confined core, ``(hoop volume / core volume) fyd / fcd``. The
          core dimensions ``b0`` and ``h0`` are measured to the centreline
          of the hoops.
        - Confinement effectiveness factor ``alpha = alpha_n alpha_s``
          (Eqs. 5.16a and 5.16b), with the distances ``bi`` between the
          centres of consecutive perimeter bars from the bar layout, i.e.,
          all perimeter bars are assumed to be engaged by a hoop corner or a
          cross-tie.
        - ``bc / b0`` is taken for the direction with the larger ratio.

        References
        ----------
        CEN (2004) Eurocode 8: Design of structures for earthquake resistance
        - Part 1: General rules, seismic actions and rules for buildings.
        EN 1998-1:2004. Brussels, Belgium.
        """
        # Curvature ductility factor - Eq. 5.4
        if T1 is None or Tc is None or T1 >= Tc:
            mu_phi = 2 * q0 - 1
        else:
            mu_phi = 1 + 2 * (q0 - 1) * Tc / T1
        # Confined core dimensions, to the centreline of the hoops
        b0 = self.bx - 2 * self.cover - self.dbh  # along x
        h0 = self.by - 2 * self.cover - self.dbh  # along y
        # Confinement effectiveness factor - Eqs. 5.16a and 5.16b, with bi
        # the distances between the centres of consecutive perimeter bars
        layout = build_column_rebar_layout(
            self.dbl_cor, self.dbl_int, int(self.nblx_int),
            int(self.nbly_int), self.dbh, self.bx, self.by, self.cover)
        _, sum_bi2, _ = get_sum_wi_sq(
            layout['rein_x'], layout['rein_y'], layout['rein_d'], clear=False)
        alpha_n = 1 - sum_bi2 / (6 * b0 * h0)
        alpha_s = (1 - self.sbh / (2 * b0)) * (1 - self.sbh / (2 * h0))
        alpha = alpha_n * alpha_s
        # Mechanical volumetric ratio of the hoops within the core
        Abh = np.pi * self.dbh**2 / 4
        rho_w = Abh * (self.nbh_x * b0 + self.nbh_y * h0) / (
            self.sbh * b0 * h0)
        omega_wd = rho_w * self.fsyd / self.fcd
        # Largest normalised axial force in the seismic design situation
        nu_d = max(
            -(factors['G'] * self.forces['G/seismic']
              + factors['Q'] * self.forces['Q/seismic']).N1
            / (self.Ag * self.fcd)
            for factors in combo_grav_factors
        )
        # Design value of the yield strain of the longitudinal steel
        eps_syd = self.fsyd / self.Es
        # Gross to core width ratio
        bc_b0 = max(self.bx / b0, self.by / h0)
        # Local ductility requirement - Eq. 5.15
        alpha_omega_wd = alpha * omega_wd
        required = 30 * mu_phi * nu_d * eps_syd * bc_b0 - 0.035
        return alpha_omega_wd >= required, alpha_omega_wd, required
