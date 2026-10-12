"""This module provides the column class implementation for the ``DP05``
model in the BNSM layer.
"""
# Imports from bnsm library
from ..dp03.column import Column as ColumnDP03


class Column(ColumnDP03):
    """Column implementation for the ``DP05`` model, identical to ``DP03``.

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.dp03.column.Column`
        Class reused by this model.
    """
