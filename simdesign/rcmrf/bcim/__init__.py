"""
Building Class Information Model (BCIM) package.

This package generates the information dataset representing the general
characteristics of a building portfolio. It constitutes the first step of
the BED framework pipeline (BCIM → BDIM → BNSM), producing realisations
by sampling secondary building attributes from class-specific probability
distributions and decision trees, conditioned on primary attributes (e.g.,
design class, number of storeys, lateral load factor).

Sampled attributes include geometry variables (storey heights, bay widths,
floor layout), taxonomy (slab type, beam type, column section, material
grades, construction quality), and masonry infill configuration. The main
entry point is the :class:`~simdesign.rcmrf.bcim.factory.BCIM` class.

Example
-------
>>> from bcim import BCIM
>>> model = BCIM()
>>> model.generate(design_class="eu_cdh", beta=0.1
                   num_storeys=4, sample_size=150)
>>> model.to_csv("path/to/output.csv")
"""

from .factory import BCIM

__all__ = ["BCIM"]
