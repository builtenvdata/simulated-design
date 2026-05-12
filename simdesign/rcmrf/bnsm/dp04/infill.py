"""This module provides the infill class implementation for the ``DP04`` model
in the BNSM layer.
"""
# Imports from bnsm base library
from ..baselib.infill import InfillBase


class Infill(InfillBase):
    """Masonry infill wall implementation for the ``DP04`` model.

    This class directly uses the behaviour defined in ``InfillBase``.

    See Also
    --------
    :class:`~InfillBase`
        Base class defining the core behaviour and configuration.
    """
