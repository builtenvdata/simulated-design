"""
Specific routines for defining eu_cdn construction quality adjustments.
"""
# Imports from installed packages
from pathlib import Path

# Imports from bdim base library
from ..baselib.quality import QualityBase


class Quality(QualityBase):
    """Quality object for design class: eu_cdn.
    """
    data_path = Path(__file__).parent / 'data' / 'quality.json'
    """Path to the json file containing all the construction quality data."""
