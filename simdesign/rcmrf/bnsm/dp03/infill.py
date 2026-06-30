"""This module provides the infill class implementation for the ``DP03`` model
in the BNSM layer.
"""
# Imports from bnsm base library
from ..baselib.infill import InfillBase


class Infill(InfillBase):
    """Masonry infill wall implementation for the ``DP03`` model.

    This class directly uses the behaviour defined in ``InfillBase``.

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.baselib.infill.InfillBase`
        Base class defining the core behaviour and configuration.
    """
