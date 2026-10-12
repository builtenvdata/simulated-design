"""This module provides the column class implementation for the ``DP01`` model
in the BNSM layer.
"""
# Imports from installed packages
from typing import List, Literal

# Imports from bnsm base library
from ..baselib.column import ColumnBase

# Imports from utils library
from ....utils.misc import round_list


class Column(ColumnBase):
    """Column implementation for the ``DP01`` model.

    This class directly uses the behaviour defined in ``ColumnBase``, except
    for the cracked elastic section (see ``_get_elastic_sec_inputs``).

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.baselib.column.ColumnBase`
        Base class defining the core behaviour and configuration.
    """

    def _get_elastic_sec_inputs(self) -> List[str | float | int]:
        """Retrieves elastic column section inputs.

        Returns
        -------
        List[str | float | int]
            List of elastic column section inputs.

        Notes
        -----
        The hinges carry the part of the yield rotation that the elastic
        interior does not (see ``_get_phiy_adjusted``). With ``cracked`` True,
        the moments of inertia are therefore at least
        ``_get_min_interior_I``, so that the elastic interior is not more
        flexible than the member at yield.
        """
        sec_inputs = super()._get_elastic_sec_inputs()
        if self.cracked is True:
            sec_inputs[4] = max(sec_inputs[4], self._get_min_interior_I('x'))
            sec_inputs[5] = max(sec_inputs[5], self._get_min_interior_I('y'))

        return round_list(sec_inputs)

    def _get_min_interior_I(self, axis: Literal['x', 'y']) -> float:
        """Gets the smallest moment of inertia of the elastic interior for
        which the member does not exceed the yield rotation at yielding.

        Parameters
        ----------
        axis : Literal['x', 'y']
            The local axis considered for the calculations.

        Returns
        -------
        float
            ``My·Ls/(3·E·theta_y)`` around `axis`. With a larger moment of
            inertia, the elastic interior gives at most ``theta_y``, and the
            hinges the rest (see ``_get_phiy_adjusted``).
        """
        props = self._get_rot_hinge_props(axis)
        My, theta_y = abs(props[1]), abs(props[4])
        ls = self.clear_length / 2  # Shear span, as in _get_phiy_adjusted
        return float(My * ls / (3 * theta_y) / self.Ecm_q)
