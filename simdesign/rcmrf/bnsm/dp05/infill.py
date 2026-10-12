"""This module provides the infill class implementation for the ``DP05``
model in the BNSM layer.
"""
# Imports from bnsm library
from ..dp03.infill import Infill as InfillDP03


class Infill(InfillDP03):
    """Infill implementation for the ``DP05`` model, identical to ``DP03``.

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.dp03.infill.Infill`
        Class reused by this model.
    """
