"""This module provides the rebars class implementation representing the
detailing of structural members for the``eu_cdn`` design class in the BDIM
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
    """Rebars implementation for design class ``eu_cdn``.

    This class extends ``RebarsBase`` by providing the detailing rules
    appropriate for the ``eu_cdn`` design class.

    Attributes
    ----------
    _data_path: Path
        Path to the JSON file containing rebar data.

    See Also
    --------
    :class:`~bdim.baselib.rebars.RebarsBase`
        Base class defining the core behaviour and configuration.

    References
    ----------
    RBA (1935) Regulamento do Betão Armado.
    Decreto N.° 25:948, Lisbon, Portugal.
    """
    concrete: Concrete
    steel: Steel
    _data_path = Path(__file__).parent / "data" / "rebars.json"

    def _get_col_max_sbh(self, **kwargs) -> float | np.ndarray:
        """Get the maximum spacing between transverse reinforcement
        (horizontal bars) in columns.

        Returns
        -------
        float | np.ndarray
            Maximum spacing between transverse reinforcement.

        Notes
        -----
        Based on Article 37 of RBA (1935), which requires stirrup spacing
        not to exceed the smaller cross-sectional dimension nor 12 times
        the longitudinal bar diameter.
        """
        # maximum allowed spacing in current iteration
        by = kwargs["by"]  # column width along y
        bx = kwargs["bx"]  # column width along x
        dbl = kwargs["dbl"]  # long. reinf. diameter
        max_sbh = np.minimum(np.minimum(by, bx), 12 * dbl)
        return max_sbh

    def _get_beam_max_sbh(self, **kwargs) -> float | np.ndarray:
        """Get the maximum spacing between transverse reinforcement
        (horizontal bars) in beams.

        Returns
        -------
        float | np.ndarray
            Maximum spacing between transverse reinforcement.

        Notes
        -----
        The limits applied (200 mm, ``24 * dbh``, ``12 * dbl``) are not
        directly prescribed by RBA (1935).
        """
        # maximum allowed spacing in current iteration
        h = kwargs["h"]  # beam depth
        dbh = kwargs["dbh"]  # transverse reinf. diameter
        dbl = kwargs["dbl"]  # long. reinf. diameter
        max_sbh = np.minimum(
            np.minimum(200 * mm, h), np.minimum(24 * dbh, 12 * dbl)
        )
        return max_sbh
