"""This module provides the infill class implementation for the ``CP02`` model
in the BNSM layer.
"""
# Imports from bnsm base library
from ..baselib.infill import InfillBase


class Infill(InfillBase):
    """Masonry infill wall implementation for the ``CP02`` model.

    This class directly uses the behaviour defined in ``InfillBase``.

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.baselib.infill.InfillBase`
        Infill class definition extended by this class.
    """
