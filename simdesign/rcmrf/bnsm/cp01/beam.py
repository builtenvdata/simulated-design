"""This module provides the beam class implementation for the ``CP01`` model in
the BNSM layer.
"""
# Imports from installed packages
from typing import Tuple, List

# Imports from bnsm base library
from ..baselib.beam import BeamBase

# Imports from utils library
from ....utils.misc import round_list


class Beam(BeamBase):
    """Beam implementation for the ``CP01`` model.

    The beam is modeled using a concentrated plasticity approach. Plastic
    rotations are concentrated at the element ends via
    ``beamIntegration('ConcentratedPlasticity', ...)`` (end hinge integration
    points with an elastic interior region), while the element formulation is
    provided by ``BeamBase``.

    End-hinge flexural behaviour about the local z-axis (Mz) is defined using a
    uniaxial ``Hysteretic`` material, expressed in terms of bending moment vs.
    plastic rotation.

    See Also
    --------
    :class:`~BeamBase`
        Base beam definition extended by this class.
    """

    def _get_mz_mat_inputs(self) -> Tuple[List[str | float | int],
                                          List[str | float | int]]:
        """Retrieves the material inputs defining the flexural behaviour
        around local-z for the plastic hinge.

        Returns
        -------
        hinge_i_mat_inputs : List[str | float | int]
            Hysteretic material model inputs for hinge at the start section.
        hinge_j_mat_inputs : List[str | float | int]
            Hysteretic material model inputs for hinge at the end section.
        """
        # Plastic hinge properties
        (
            _, My_neg, Mc_neg, Mr_neg,
            theta_y_neg, theta_cap_pl_neg, theta_pc_neg,
            _, My_pos, Mc_pos, Mr_pos,
            theta_y_pos, theta_cap_pl_pos, theta_pc_pos,
            pinchx, pinchy, damage1, damage2, beta,
        ) = self._get_rot_hinge_props()

        # Rotation values
        theta_1_neg = theta_y_neg
        theta_2_neg = theta_y_neg + theta_cap_pl_neg
        theta_3_neg = theta_y_neg + theta_cap_pl_neg + theta_pc_neg
        theta_1_pos = theta_y_pos
        theta_2_pos = theta_y_pos + theta_cap_pl_pos
        theta_3_pos = theta_y_pos + theta_cap_pl_pos + theta_pc_pos

        # Material inputs
        hinge_i_mat_inputs = [
            'Hysteretic', self.mz_i_mat_tag,
            My_pos[0], theta_1_pos[0],
            Mc_pos[0], theta_2_pos[0],
            Mr_pos[0], theta_3_pos[0],
            -My_neg[0], -theta_1_neg[0],
            -Mc_neg[0], -theta_2_neg[0],
            -Mr_neg[0], -theta_3_neg[0],
            pinchx, pinchy, damage1, damage2, beta
        ]
        hinge_j_mat_inputs = [
            'Hysteretic', self.mz_j_mat_tag,
            My_pos[-1], theta_1_pos[-1],
            Mc_pos[-1], theta_2_pos[-1],
            Mr_pos[-1], theta_3_pos[-1],
            -My_neg[-1], -theta_1_neg[-1],
            -Mc_neg[-1], -theta_2_neg[-1],
            -Mr_neg[-1], -theta_3_neg[-1],
            pinchx, pinchy, damage1, damage2, beta
        ]

        # Rounding to precision
        hinge_i_mat_inputs = round_list(hinge_i_mat_inputs)
        hinge_j_mat_inputs = round_list(hinge_j_mat_inputs)

        return hinge_i_mat_inputs, hinge_j_mat_inputs

    def _get_int_inputs(self) -> List[str | float]:
        """Retrieves beam integration inputs.

        Returns
        -------
        List[float]
            List of beam integration inputs.
        """
        int_inputs = [
            'ConcentratedPlasticity',
            self.int_tag, self.inelastic_sec_i_tag,
            self.inelastic_sec_j_tag, self.elastic_sec_tag
        ]

        return int_inputs
