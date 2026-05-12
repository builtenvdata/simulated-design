"""
Building geometry package for RC moment-resisting frames.

This package provides geometry definitions used to construct the structural
layout of RC-MRF buildings within the BED framework pipeline
(BCIM → BDIM → BNSM). Both classes inherit from ``GeometryBase`` and
populate the same internal data structures (points, lines, rectangles),
making them interchangeable in downstream modelling stages.

Two entry points are available:

- :class:`StandardGeometry` — regular frames with uniform bay widths and
  storey heights, where the full 3D grid is generated automatically. Supports
  optional masonry infill panels and staircase elements.

- :class:`CustomGeometry` — irregular or non-uniform frames loaded from an
  Excel workbook, where nodes, members, and panel elements are defined
  explicitly.
"""

from .standard import StandardGeometry
from .custom import CustomGeometry

__all__ = ["StandardGeometry", "CustomGeometry"]
