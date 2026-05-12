"""This module provides the rebars class implementation representing the
detailing of structural members for the``eu_cdh`` design class in the BDIM
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
    """Rebars implementation for design class ``eu_cdh``.

    This class extends ``RebarsBase`` by providing the detailing rules
    appropriate for the ``eu_cdh`` design class.

    Attributes
    ----------
    concrete : ~simdesign.rcmrf.bdim.eu_cdh.materials.Concrete
        Concrete material instance considered in design of beams and columns.
    steel : ~simdesign.rcmrf.bdim.eu_cdh.materials.Steel
        Steel material instance considered in design of beams and columns.
    col_max_leg_dist : float
        Maximum distance between longitudinal bars within a column
        section that can be considered to be confined without the need to have
        an extra stirrup leg around them. The default value is set as the
        minimum of the two following clauses:
        - EC2-1-1 clause 9.5.3 (6): 150 mm for corner bars
        - EC8-1 clause 5.4.3.2.2 (11) b): 200 mm for interior bars
    _data_path : Path | str
        Path to the json file containing rebar data.

    See Also
    --------
    :class:`~bdim.baselib.rebars.RebarsBase`
        Base class defining the core behaviour and configuration.

    References
    ----------
    Comité Européen de Normalisation, CEN (2004). Eurocode 2: Design of
    Concrete Structures — Part 1-1: General Rules and Rules for Buildings.
    European Committee for Standardization, Brussels, Belgium.

    Comité Européen de Normalisation, CEN (2004). Eurocode 8: Design of
    Structures for Earthquake Resistance — Part 1: General Rules,
    Seismic Actions and Rules for Buildings.
    European Committee for Standardization, Brussels, Belgium.
    """
    concrete: Concrete
    steel: Steel
    col_max_leg_dist: float = 150 * mm
    _data_path = Path(__file__).parent / 'data' / 'rebars.json'

    def _get_min_beam_dbh(self, **kwargs) -> float | np.ndarray:
        """Get the minimum transverse reinforcement diameter in beams.

        Returns
        -------
        float | np.ndarray
            Minimum transverse reinforcement diameter.

        Notes
        -----
        Based on EN 1992-1-1:2004 clause 9.5.3(1).
        """
        dbl = kwargs['dbl']
        return np.maximum(dbl / 4, 6 * mm)

    def _get_min_col_dbh(self, **kwargs) -> float | np.ndarray:
        """Get the minimum transverse reinforcement diameter in columns.

        Returns
        -------
        float | np.ndarray
            Minimum transverse reinforcement diameter.

        Notes
        -----
        Based on EN 1992-1-1:2004 clause 9.5.3(1).
        """
        dbl = kwargs['dbl']
        return np.maximum(dbl / 4, 6 * mm)

    def _get_beam_max_sbh(self, **kwargs) -> float | np.ndarray:
        """Get maximum spacing between horizontal bars
        (transverse reinforcement) for beams.

        Returns
        -------
        float | np.ndarray
            Maximum spacing between transverse reinforcement.

        Notes
        -----
        Based on EN 1998-1:2004 eqn. 5.13
        """
        # maximum allowed spacing in current iteration
        h = kwargs['h']  # beam depth
        dbh = kwargs['dbh']  # transverse reinf. diameter
        dbl = kwargs['dbl']  # long. reinf. diameter
        max_sbh = np.minimum(
            np.minimum(225 * mm, h / 4), np.minimum(24 * dbh, 8 * dbl)
        )
        return max_sbh

    def _get_col_max_sbh(self, **kwargs) -> float | np.ndarray:
        """Get maximum spacing between horizontal bars
        (transverse reinforcement) for columns.

        Returns
        -------
        float | np.ndarray
            Maximum spacing between transverse reinforcement.

        Notes
        -----
        Based on EN 1998-1:2004 eqn. 5.18
        """
        # maximum allowed spacing in current iteration
        by = kwargs['by']  # column width along y
        bx = kwargs['bx']  # column width along x
        cover = kwargs['cover']
        b0 = np.minimum(by, bx) - 2 * cover
        dbl = kwargs["dbl"]  # long. reinf. diameter
        max_sbh = np.minimum(np.minimum(b0 / 2, 175 * mm), 8 * dbl)
        return max_sbh
