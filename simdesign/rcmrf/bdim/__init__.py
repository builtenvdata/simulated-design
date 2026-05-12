"""
Building Design Information Model (BDIM) package.

This package provides a factory interface for generating design-class-specific
building models. The main entry point is the :class:`BDIM` factory class,
which selects and instantiates the appropriate design-class-specific
implementation based on a :class:`TaxonomyData` input.

Example
-------
>>> from bdim import BDIM, TaxonomyData
>>> taxonomy = TaxonomyData(design_class="eu_cdh", ...)
>>> model = BDIM(taxonomy)
"""

from .factory import BDIM, TaxonomyData

__all__ = ["BDIM", "TaxonomyData"]
