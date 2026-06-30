"""This module provides the column class implementation for the ``DP01`` model
in the BNSM layer.
"""
# Imports from bnsm base library
from ..baselib.column import ColumnBase


class Column(ColumnBase):
    """Column implementation for the ``DP01`` model.

    This class directly uses the behaviour defined in ``ColumnBase``.

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.baselib.column.ColumnBase`
        Base class defining the core behaviour and configuration.
    """
