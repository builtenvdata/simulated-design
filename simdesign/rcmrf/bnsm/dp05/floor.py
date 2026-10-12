"""This module provides the floor diaphragm class implementation for the
``DP05`` model in the BNSM layer.
"""
# Imports from bnsm library
from ..dp03.floor import FloorDiaphragm as FloorDiaphragmDP03


class FloorDiaphragm(FloorDiaphragmDP03):
    """Floor diaphragm implementation for the ``DP05`` model, identical to
    ``DP03``.

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.dp03.floor.FloorDiaphragm`
        Class reused by this model.
    """
