"""This module provides the infill class implementation representing
masonry infill walls for the ``eu_cdl`` design class in the BDIM layer.
"""
# Imports from installed packages
from typing import List, Optional

# Imports from bdim base library
from ..baselib.infill import InfillBase

# Imports from the design class (eu_cdl) library
from .beam import Beam
from .column import Column


class Infill(InfillBase):
    """Masonry infill wall implementation for design class ``eu_cdl``.

    This class extends ``InfillBase`` by narrowing the attribute types.

    Attributes
    ----------
    beams : List[~simdesign.rcmrf.bdim.eu_cdl.beam.Beam or None]
        List of beams corresponding to the horizontal edges of the bounding
        rectangle (indices 1 and 3).
    columns : List[~simdesign.rcmrf.bdim.eu_cdl.column.Column]
        List of columns corresponding to the vertical edges of the bounding
        rectangle (indices 0 and 2).

    See Also
    --------
    :class:`~bdim.baselib.infill.InfillBase`
        Base class defining the core behaviour and configuration.
    """
    beams: List[Optional[Beam]]
    columns: List[Column]
