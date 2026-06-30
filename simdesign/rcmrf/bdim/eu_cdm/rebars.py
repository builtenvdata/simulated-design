"""This module provides the rebars class implementation representing the
detailing of structural members for the``eu_cdm`` design class in the BDIM
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
    """Rebars implementation for design class ``eu_cdm``.

    This class extends ``RebarsBase`` by providing the detailing rules
    appropriate for the ``eu_cdm`` design class.

    Attributes
    ----------
    concrete : ~simdesign.rcmrf.bdim.eu_cdm.materials.Concrete
        Concrete material instance considered in design of beams and columns.
    steel : ~simdesign.rcmrf.bdim.eu_cdm.materials.Steel
        Steel material instance considered in design of beams and columns.
    col_max_leg_dist : float
        Maximum distance between longitudinal bars within a column
        section that can be considered to be confined without the need to have
        an extra stirrup leg around them.
    _data_path : Path | str
        Path to the json file containing rebar data.

    See Also
    --------
    :class:`~simdesign.rcmrf.bdim.baselib.rebars.RebarsBase`
        Base class defining the core behaviour and configuration.

    References
    ----------
    REBAP (1983). Regulamento de Estruturas de Betão Armado e Pré-Esforçado.
    Decreto-Lei N.° 349-C/83, Lisbon, Portugal.
    """
    concrete: Concrete
    steel: Steel
    col_max_leg_dist: float = 150 * mm
    _data_path = Path(__file__).parent / 'data' / 'rebars.json'

    @property
    def beam_max_sbl(self) -> float | np.ndarray:
        """
        Returns
        -------
        float
            Maximum spacing between longitudinal bars (reinforcement)
            for beams.
        """
        # Art 91 in REBAP (1983) - defined for tensile reinforcement
        if self.steel.fsyk == 400:
            return 100 * mm
        elif self.steel.fsyk == 500:
            return 125 * mm

    def _get_col_max_sbh(self, **kwargs) -> float | np.ndarray:
        """Get maximum spacing between horizontal bars
        (transverse reinforcement) for columns.

        Returns
        -------
        float | np.ndarray
            Maximum spacing between transverse reinforcement.
        """
        # maximum allowed spacing in current iteration
        by = kwargs['by']  # column width along y
        bx = kwargs['bx']  # column width along x
        dbl = kwargs['dbl']  # long. reinf. diameter
        max_sbh = np.minimum(
            np.minimum(12 * dbl, 300 * mm),
            np.minimum(by, bx),
        )
        return max_sbh

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
