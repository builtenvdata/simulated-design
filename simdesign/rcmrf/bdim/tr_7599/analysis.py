"""This module provides the class implementation representing the elastic
numerical model used in the BDIM layer for the ``tr_7599`` design class.
"""
# Imports from installed packages
from typing import List

# Imports from the design class (tr_7599) library
from .beam import Beam
from .column import Column

# Imports from bdim base library
from ..baselib.analysis import ElasticModelBase


class ElasticModel(ElasticModelBase):
    """Elastic model implementation for design class ``tr_7599``.

    This class extends ``ElasticModelBase`` by narrowing the attribute types.

    Attributes
    ----------
    beams : List[~simdesign.rcmrf.bdim.tr_7599.beam.Beam]
        List of beam objects of the building.
    columns : List[~simdesign.rcmrf.bdim.tr_7599.column.Column]
        List of column objects of the building.

    See Also
    --------
    :class:`~bdim.baselib.analysis.ElasticModelBase`
        Base class defining the core behaviour and configuration.
    """
    beams: List[Beam]
    columns: List[Column]
