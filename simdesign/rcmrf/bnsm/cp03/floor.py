"""This module provides the floor diaphragm class implementation for the
``CP03`` model in the BNSM layer.
"""
# Imports from bnsm base library
from ..baselib.floor import FloorDiaphragmBase


class FloorDiaphragm(FloorDiaphragmBase):
    """Floor diaphragm implementation for the ``CP03`` model.

    This class directly uses the behaviour defined in ``FloorDiaphragmBase``.

    See Also
    --------
    :class:`~FloorDiaphragmBase.`
        Base class defining the core behaviour and configuration.
    """
