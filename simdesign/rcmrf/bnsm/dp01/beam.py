"""This module provides the beam class implementation for the ``DP01`` model in
the BNSM layer.
"""
# Imports from installed packages
import numpy as np
from typing import List

# Imports from bnsm base library
from ..baselib.beam import BeamBase

# Imports from utils library
from ....utils.misc import round_list


class Beam(BeamBase):
    """Beam implementation for the ``DP01`` model.

    This class directly uses the behaviour defined in ``BeamBase``, except
    for the cracked elastic section (see ``_get_elastic_sec_inputs``).

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.baselib.beam.BeamBase`
        Base class defining the core behaviour and configuration.
    """

    def _get_elastic_sec_inputs(self) -> List[str | int | float]:
        """Retrieves elastic beam section inputs.

        Returns
        -------
        List[str | int | float]
            List of elastic beam section inputs.

        Notes
        -----
        The hinges carry the part of the yield rotation that the elastic
        interior does not (see ``_get_phiy_adjusted``). With ``cracked`` True,
        the moment of inertia is therefore at least ``_get_min_interior_Iz``,
        so that the elastic interior is not more flexible than the member at
        yield.
        """
        sec_inputs = super()._get_elastic_sec_inputs()
        if self.cracked is True:
            sec_inputs[4] = max(sec_inputs[4], self._get_min_interior_Iz())

        return round_list(sec_inputs)

    def _get_min_interior_Iz(self) -> float:
        """Gets the smallest moment of inertia of the elastic interior for
        which the member does not exceed the yield rotation at yielding.

        Returns
        -------
        float
            ``max(My·Ls/(3·E·theta_y))`` over both end sections and bending
            directions. With a larger moment of inertia, the elastic interior
            gives at most ``theta_y``, and the hinges the rest (see
            ``_get_phiy_adjusted``).

        Notes
        -----
        ``_Iz_eff`` is the mean of ``My / phi_y`` over both end sections and
        bending directions. At the section with the largest ``My / phi_y``,
        the elastic part ``My·Ls/(3·E·_Iz_eff)`` may then exceed
        ``theta_y``, and the member would yield beyond ``theta_y``.
        """
        props = self._get_rot_hinge_props()
        My = np.abs(np.concatenate([props[1][[0, -1]], props[8][[0, -1]]]))
        theta_y = np.abs(
            np.concatenate([props[4][[0, -1]], props[11][[0, -1]]]))
        ls = self.clear_length / 2  # Shear span, as in _get_rot_hinge_props
        return float(np.max(My * ls / (3 * theta_y)) / self.Ecm_q)
