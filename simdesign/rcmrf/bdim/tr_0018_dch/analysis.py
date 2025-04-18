# Imports from installed packages
from typing import List

# Imports from the design class (tr_0018_dch) library
from .beam import Beam
from .column import Column

# Imports from bdim base library
from ..baselib.analysis import ElasticModelBase


class ElasticModel(ElasticModelBase):
    """Elastic model builder in OpenSees for design class tr_0018_dch.
    """
    beams: List[Beam]
    """Beam objects of the building."""
    columns: List[Column]
    """Column objects of the building."""
