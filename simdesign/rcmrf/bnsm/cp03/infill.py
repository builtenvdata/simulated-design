"""This module provides the infill class implementation for the ``CP03`` model
in the BNSM layer.
"""
# Imports from bnsm base library
from ..cp01.infill import Infill as InfillCP01


class Infill(InfillCP01):
    """Masonry infill wall implementation for the ``CP03`` model.

    This class directly uses the behaviour defined in ``InfillCP01``.

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.cp01.infill.Infill`
        CP01 Infill model definition used by this class.
    """
