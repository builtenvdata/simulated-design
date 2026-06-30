"""This module provides the infill class implementation for the ``CP01`` model
in the BNSM layer.
"""
# Imports from installed packages
from typing import Tuple, List

# Imports from bnsm base library
from ..baselib.infill import InfillBase

# Imports from utils library
from ....utils.misc import PRECISION, round_list
from ....utils.units import kN, m

COEFFS = {
    'Weak': (-21.61, 27.92, 18.18),
    'Medium': (-31.54, 41.17, 26.5),
    'Strong': (-41.03, 55.07, 35.22)
}
"""Regression coefficients fpc = (a0 + a1.L + a2.H).
Based on the data obtained from the expressions in Hak et al. 2012.
"""


class Infill(InfillBase):
    """Masonry infill wall implementation for the ``CP01`` model.

    This class extends ``InfillBase`` with the material modelling
    strategy utilised in ESRM20 for the struts.

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.baselib.infill.InfillBase`
        Infill class definition extended by this class.
    """

    def _get_mat_inputs(self) -> Tuple[List[str | float | int], float]:
        """
        Compute the uniaxial material definition for the equivalent diagonal
        strut and the corresponding strut cross-sectional area based on
        infills models utilised in esrm20.

        Returns
        -------
        mat_inputs : List[str | float | int]
            OpenSees `uniaxialMaterial` argument list.
        Aw : float
            Equivalent diagonal strut area.
        """
        a0, a1, a2 = COEFFS.get(self.design.typology)
        # Compressive strength of the infill
        fpc = -(a0 + a1 * self.design.length
                + a2 * self.design.height) * kN
        fpcu = 0.01 * fpc  # assumed, %1 to avoid numerical issues
        epsc0 = -0.0013  # from Hak et al. 2012, Figure 12b
        epscu = -0.0045  # from Hak et al. 2012, Figure 12b
        mat_inputs = round_list([fpc, epsc0, fpcu, epscu], PRECISION)
        mat_inputs = ['Concrete01', self.design.rectangle.tag] + mat_inputs
        Aw = 1.0 * m**2

        return mat_inputs, Aw
