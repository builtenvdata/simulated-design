"""This module provides the floor diaphragm class implementation for the
``DP03`` model in the BNSM layer.
"""
# Imports from bnsm base library
from ..baselib.floor import FloorDiaphragmBase


class FloorDiaphragm(FloorDiaphragmBase):
    """Floor diaphragm implementation for the ``DP03`` model.

    This class directly uses the behaviour defined in ``FloorDiaphragmBase``.

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.baselib.floor.FloorDiaphragmBase.`
        Base class defining the core behaviour and configuration.
    """
