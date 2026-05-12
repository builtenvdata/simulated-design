"""This module provides the rebars class implementation representing the
detailing of structural members for the``eu_cdl`` design class in the BDIM
layer.
"""
# Imports from installed packages
import numpy as np
from pathlib import Path

# Imports from bdim base library
from ..baselib.rebars import RebarsBase
from .materials import Concrete, Steel

# Imports from utils library
from ....utils.units import mm


class Rebars(RebarsBase):
    """Rebars implementation for design class ``eu_cdl``.

    This class extends ``RebarsBase`` by providing the detailing rules
    appropriate for the ``eu_cdl`` design class.

    Attributes
    ----------
    concrete : ~simdesign.rcmrf.bdim.eu_cdl.materials.Concrete
        Concrete material instance considered in design of beams and columns.
    steel : ~simdesign.rcmrf.bdim.eu_cdl.materials.Steel
        Steel material instance considered in design of beams and columns.
    _data_path : Path | str
        Path to the json file containing rebar data.

    See Also
    --------
    :class:`~bdim.baselib.rebars.RebarsBase`
        Base class defining the core behaviour and configuration.
    """
    concrete: Concrete
    steel: Steel
    _data_path = Path(__file__).parent / "data" / "rebars.json"

    def _get_beam_max_sbh(self, **kwargs) -> float | np.ndarray:
        """Get maximum spacing between horizontal bars
        (transverse reinforcement) for beams.

        Returns
        -------
        float | np.ndarray
            Maximum spacing between transverse reinforcement.
        """
        # maximum allowed spacing in current iteration
        h = kwargs['h']  # beam depth
        dbh = kwargs['dbh']  # transverse reinf. diameter
        dbl = kwargs['dbl']  # long. reinf. diameter
        max_sbh = np.minimum(
            np.minimum(200 * mm, h),
            np.minimum(24 * dbh, 12 * dbl)
        )
        return max_sbh
