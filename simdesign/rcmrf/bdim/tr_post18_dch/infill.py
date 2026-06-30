"""This module provides the infill class implementation representing
masonry infill walls for the ``tr_post18_dch`` design class in the BDIM layer.
"""
# Imports from installed packages
from typing import List, Optional

# Imports from bdim base library
from ..baselib.infill import InfillBase

# Imports from the design class (tr_post18_dch) library
from .beam import Beam
from .column import Column


class Infill(InfillBase):
    """Masonry infill wall implementation for design class ``tr_post18_dch``.

    This class extends ``InfillBase`` by narrowing the attribute types.

    Attributes
    ----------
    beams : List[~simdesign.rcmrf.bdim.tr_post18_dch.beam.Beam or None]
        List of beams corresponding to the horizontal edges of the bounding
        rectangle (indices 1 and 3).
    columns : List[~simdesign.rcmrf.bdim.tr_post18_dch.column.Column]
        List of columns corresponding to the vertical edges of the bounding
        rectangle (indices 0 and 2).

    See Also
    --------
    :class:`~simdesign.rcmrf.bdim.baselib.infill.InfillBase`
        Base class defining the core behaviour and configuration.
    """
    beams: List[Optional[Beam]]
    columns: List[Column]
