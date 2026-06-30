"""This module provides the stairs class implementation for the ``tr_0018_dcm``
design class in the BDIM layer.
"""
# Imports from bdim base library
from ..baselib.stairs import StairsBase


class Stairs(StairsBase):
    """Stairs implementation for the ``tr_0018_dcm`` design class.

    This class directly uses the behaviour defined in ``StairsBase``.

    See Also
    --------
    :class:`~simdesign.rcmrf.bdim.baselib.stairs.StairsBase`
        Base class defining the core behaviour and configuration.
    """
