"""This module provides the beam class implementation for the ``CP01`` model in
the BNSM layer.
"""
# Imports from installed packages
import numpy as np
from typing import Tuple, List

# Imports from bnsm base library
from ..cp01.beam import Beam as BeamCP01

# Imports from utils library
from ....utils.units import MPa
from ....utils.misc import round_list


class Beam(BeamCP01):
    """Beam implementation for the ``CP02`` model.

    This class directly uses the behaviour defined in ``BeamCP01``,
    but overrides the plastic hinge material definition for rotational
    degrees of freedoms based on the PhD Thesis of Serkan Hasanoglu.

    See Also
    --------
    :class:`~BeamCP01`
        CP01 beam model definition extended by this class.
    """

    def _get_mz_mat_inputs(self) -> Tuple[List[str | float | int],
                                          List[str | float | int]]:
        """Retrieves the material inputs defining the flexural behaviour
        around local-z for the plastic hinge.

        Returns
        -------
        mat_inputs_i : List[str | float | int]
            HystereticSM material model inputs for hinge at the start section.
        mat_inputs_j : List[str | float | int]
            HystereticSM material model inputs for hinge at the end section.

        References
        ---------
        Hasanoglu, S. and O'Reilly G. J. (2026). A hysteretic energy-based
        framework for seismic fragility assessment of ductile reinforced
        concrete frame buildings
        """
        h = self.design.h
        ln = self.design.L
        fc_mpa = self.design.fc_q / MPa
        fsyl_mpa = self.design.fsyl_q / MPa
        dbh = self.design.dbh_q
        dbl = self.design.dbl_b1_q
        cover = self.design.cover_q
        rhol = self.rhol_q
        rhoh = self.rhoh_y_q

        ls = ln / 2  # Shear span length
        niu = 0.0  # Axial load ratio, assuming beams do not have any
        dd = h - cover - dbh - 0.5 * dbl
        rSsD = ls / dd  # shear span to effective depth ratio

        # Compute yield moments in positive and negative directions at both
        # end sections of the beam (i and j) - Panagiotakos and Fardis (2001)
        My_pos, _ = self._compute_yield_point('positive')
        My_neg, _ = self._compute_yield_point('negative')

        # Capping moment capacities in positive and negative directions
        Mc_My = (1.08 ** niu) * (1.38 ** (10*rhol)) * (1.14 ** (0.1*rSsD))
        Mc_pos = Mc_My * My_pos
        Mc_neg = Mc_My * My_neg

        # Ultimate moment capacities in positive and negative directions
        Mu_Mc = (0.91 ** (0.01*fc_mpa)) * (0.8 ** (0.1*rSsD))
        Mu_pos = Mu_Mc * Mc_pos
        Mu_neg = Mu_Mc * Mc_neg

        # Zero moment values in positive and negative directions
        M0_neg = 0.1 * My_neg
        M0_pos = 0.1 * My_pos

        # Yield rotation capacities in positive and negative directions
        EI_ratio = np.clip(0.08 * (1.25 ** (10*niu)) * (1.2 ** rSsD), 0.2, 0.8)
        EI_gross = self.Ecm_q * self.design.Iz
        EIy = EI_gross * EI_ratio
        theta_y_pos = My_pos * ls / (3 * EIy)
        theta_y_neg = My_neg * ls / (3 * EIy)

        # Plastic rotation capacities before capping
        theta_cap_pl_pos = 0.009 * (0.25 ** (0.01*fc_mpa)) * (0.23 ** niu) * \
            (2.17 ** (100*rhol))
        ratio_pos_neg = (
            np.maximum(0.01, fsyl_mpa * self.rhol_top_q / fc_mpa)
            / np.maximum(0.01, fsyl_mpa * self.rhol_bot_q / fc_mpa)
        ) ** 0.225
        theta_cap_pl_neg = ratio_pos_neg * theta_cap_pl_pos

        # Post-capping rotation capacity
        theta_pc_pos = 0.01 * (0.07 ** niu) * (1.78 ** (100*rhoh)) * \
            (1.18 ** (0.01*fsyl_mpa))
        theta_pc_neg = 0.01 * (0.07 ** niu) * (1.78 ** (100*rhoh)) * \
            (1.18 ** (0.01*fsyl_mpa))

        # Post-ultimate rotation capacity
        theta_pu_pos = 0.0023 * (1.96 ** (0.1*fc_mpa)) * (2.74 ** (100*rhoh))
        theta_pu_neg = 0.0023 * (1.96 ** (0.1*fc_mpa)) * (2.74 ** (100*rhoh))
        theta_pu_pos = np.minimum(theta_pu_pos, 4*theta_pc_pos)
        theta_pu_neg = np.minimum(theta_pu_neg, 4*theta_pc_neg)

        # Rotation values for cyclic loading (HystereticSM material)
        if self.cyclic_model:
            # Positive backbone
            moment_1_pos = My_pos
            moment_2_pos = Mc_pos
            moment_3_pos = Mu_pos
            moment_4_pos = M0_pos
            theta_1_pos = theta_y_pos
            theta_2_pos = theta_y_pos + theta_cap_pl_pos
            theta_3_pos = theta_y_pos + theta_cap_pl_pos + theta_pc_pos
            theta_4_pos = theta_y_pos + theta_cap_pl_pos + theta_pc_pos + \
                theta_pu_pos
            # Negative backbone
            moment_1_neg = My_neg
            moment_2_neg = Mc_neg
            moment_3_neg = Mu_neg
            moment_4_neg = M0_neg
            theta_1_neg = theta_y_neg
            theta_2_neg = theta_y_neg + theta_cap_pl_neg
            theta_3_neg = theta_y_neg + theta_cap_pl_neg + theta_pc_neg
            theta_4_neg = theta_y_neg + theta_cap_pl_neg + theta_pc_neg + \
                theta_pu_neg
        else:
            # These modifiers were determined based on the suggested
            # values in ATC 72-1 report
            # Positive backbone
            moment_1_pos = My_pos
            moment_2_pos = 1.1 * Mc_pos
            moment_3_pos = 1.1 * Mu_pos
            moment_4_pos = M0_pos
            theta_1_pos = theta_y_pos
            theta_2_pos = theta_y_pos + 1.4*theta_cap_pl_pos
            theta_3_pos = theta_y_pos + 1.4*theta_cap_pl_pos + 2*theta_pc_pos
            theta_4_pos = theta_y_pos + 1.4*theta_cap_pl_pos + \
                2*theta_pc_pos + 2*theta_pu_pos
            # Negative backbone
            moment_1_neg = My_neg
            moment_2_neg = 1.1 * Mc_neg
            moment_3_neg = 1.1 * Mu_neg
            moment_4_neg = M0_neg
            theta_1_neg = theta_y_neg
            theta_2_neg = theta_y_neg + 1.4*theta_cap_pl_neg
            theta_3_neg = theta_y_neg + 1.4*theta_cap_pl_neg + 2*theta_pc_neg
            theta_4_neg = theta_y_neg + 1.4*theta_cap_pl_neg + \
                2*theta_pc_neg + 2*theta_pu_neg

        # Pinching factor for strain (or deformation) during reloading
        pinchx = 0.5
        # Pinching factor for stress (or force) during reloading
        pinchy = 0.5
        # Damage due to ductility: D1(mu-1)
        damage1 = 0.0
        # Damage due to energy: D2(Eii/Eult)
        damage2 = 0.7
        # Power used to determine the degraded unloading stiffness
        beta = 0.2

        # The negative ones are based on top (compression) reinforcement
        # The positive ones are based on bottom (tension) renforcement
        hinge_i_mat_inputs = [
            'HystereticSM', self.mz_i_mat_tag,
            moment_1_pos[0], theta_1_pos[0],
            moment_2_pos[0], theta_2_pos[0],
            moment_3_pos[0], theta_3_pos[0],
            moment_4_pos[0], theta_4_pos[0],
            -moment_1_neg[0], -theta_1_neg[0],
            -moment_2_neg[0], -theta_2_neg[0],
            -moment_3_neg[0], -theta_3_neg[0],
            -moment_4_neg[0], -theta_4_neg[0],
            pinchx, pinchy, damage1, damage2, beta
        ]
        hinge_j_mat_inputs = [
            'HystereticSM', self.mz_j_mat_tag,
            moment_1_pos[-1], theta_1_pos[-1],
            moment_2_pos[-1], theta_2_pos[-1],
            moment_3_pos[-1], theta_3_pos[-1],
            moment_4_pos[-1], theta_4_pos[-1],
            -moment_1_neg[-1], -theta_1_neg[-1],
            -moment_2_neg[-1], -theta_2_neg[-1],
            -moment_3_neg[-1], -theta_3_neg[-1],
            -moment_4_neg[-1], -theta_4_neg[-1],
            pinchx, pinchy, damage1, damage2, beta
        ]

        # Rounding to precision
        hinge_i_mat_inputs = round_list(hinge_i_mat_inputs)
        hinge_j_mat_inputs = round_list(hinge_j_mat_inputs)

        return hinge_i_mat_inputs, hinge_j_mat_inputs
