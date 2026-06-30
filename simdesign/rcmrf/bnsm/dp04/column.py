"""This module provides the column class implementation for the ``DP04`` model
in the BNSM layer.
"""
# Imports from installed packages
from typing import Literal

# Imports from bnsm base library
from ..dp03.column import Column as ColumnDP03


class Column(ColumnDP03):
    """Column implementation for the ``DP04`` model.

    This class directly uses the behaviour defined in ``ColumnDP03``, but
    overrides the default value of ``interior_section`` ('Inelastic')
    and sets it to 'Elastic'.

    Attributes
    ----------
    interior_section : Literal['Elastic', 'Inelastic'], optional
        Interior section used in the plastic hinge integration formulation,
        by default 'Elastic'.

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.dp03.column.Column`
        DP03 column model definition extended by this class
    """
    interior_section: Literal['Elastic', 'Inelastic'] = 'Elastic'
