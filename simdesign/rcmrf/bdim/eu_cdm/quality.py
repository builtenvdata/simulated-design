"""This module provides the quality class implementation representing the
quality-based modifications for the ``eu_cdm`` design class in the BDIM layer.
"""
# Imports from installed packages
from pathlib import Path

# Imports from bdim base library
from ..baselib.quality import QualityBase


class Quality(QualityBase):
    """Quality implementation for the ``eu_cdm`` design class.

    This class directly uses the behaviour defined in ``QualityBase`` and
    overrides the default data path used to load construction quality data.

    Attributes
    ----------
    data_path : Path
        Path to the JSON file containing construction quality data.

    See Also
    --------
    :class:`~simdesign.rcmrf.bdim.baselib.quality.QualityBase`
        Base class defining the core behaviour and configuration.
    """
    data_path = Path(__file__).parent / 'data' / 'quality.json'
