"""This module provides the rebars class implementation representing the
detailing of structural members for the``tr_7599`` design class in the BDIM
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
from ....utils.misc import PRECISION


class Rebars(RebarsBase):
    """Rebars implementation for design class ``tr_7599``.

    This class extends ``RebarsBase`` by providing the detailing rules
    appropriate for the ``tr_7599`` design class.

    Attributes
    ----------
    concrete : ~simdesign.rcmrf.bdim.tr_7599.materials.Concrete
        Concrete material instance considered in design of beams and columns.
    steel : ~simdesign.rcmrf.bdim.tr_7599.materials.Steel
        Steel material instance considered in design of beams and columns.
    _data_path : Path | str
        Path to the json file containing rebar data.

    See Also
    --------
    :class:`~simdesign.rcmrf.bdim.baselib.rebars.RebarsBase`
        Base class defining the core behaviour and configuration.

    References
    ----------
    TBEC (1975). *Afet Bölgelerinde Yapılacak Yapılar Hakkında Yönetmelik*.
    Resmi Gazete, Ankara, Türkiye.

    TS500 (1984). *Requirements for Design and Construction of Reinforced
    Concrete Structures*. Turkish Standards Institution (TSE), Ankara, Türkiye.
    """
    concrete: Concrete
    steel: Steel
    _data_path = Path(__file__).parent / "data" / "rebars.json"

    def _get_min_beam_dbh(self, **kwargs) -> float | np.ndarray:
        """Get the minimum transverse reinforcement diameter in beams.

        Returns
        -------
        float | np.ndarray
            Minimum transverse reinforcement diameter.

        Notes
        -----
        Based on Section-6.9.7 from TBEC-1975.
        """
        return 8 * mm * np.ones(np.size(kwargs["dbl"]))

    def _get_min_col_dbh(self, **kwargs) -> float | np.ndarray:
        """Get the minimum transverse reinforcement diameter in columns.

        Returns
        -------
        float | np.ndarray
            Minimum transverse reinforcement diameter.

        Notes
        -----
        Based on:
            Section 6.6.5.1 from TBEC-1975,
            Section 7.6 from TS500-1975.
        """
        dbl = kwargs["dbl"]
        return np.maximum(dbl / 3, 8 * mm)

    def _get_beam_max_sbh_mid(self, **kwargs) -> float | np.ndarray:
        """Get maximum spacing between horizontal bars in the middle
        (transverse reinforcement) for beams.

        Returns
        -------
        float | np.ndarray
            Maximum spacing between transverse reinforcement in the middle.

        Notes
        -----
        Based on Section 6.9.7 in TBEC-1975.
        """
        # maximum allowed spacing in current iteration
        bw = kwargs["b"]  # beam width
        h = kwargs["h"]  # beam depth
        max_sbh = np.minimum(bw, h / 2)
        return max_sbh

    def _get_beam_max_sbh_end(self, **kwargs) -> float | np.ndarray:
        """Get maximum spacing between horizontal bars in the ends
        (transverse reinforcement) for beams.

        Returns
        -------
        float | np.ndarray
            Maximum spacing between transverse reinforcement in the ends.

        Notes
        -----
        Based on Section 6.9.7 in TBEC-1975.
        """
        # maximum allowed spacing in current iteration
        h = kwargs["h"]  # beam depth
        max_sbh = (0.9 * h) / 4
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
        Based on Section 6.6.5.1 in TBEC-1975.
        """
        return 100 * mm

    def get_beam_transv_rebars(
        self, Ash_sbh: np.ndarray, nbl_t1: np.ndarray, nbl_t2: np.ndarray,
        nbl_b1: np.ndarray, nbl_b2: np.ndarray, dbl_t1: np.ndarray,
        dbl_b1: np.ndarray, b: np.ndarray, h: np.ndarray
    ) -> tuple[np.ndarray]:
        """
        Select transverse reinforcement solution for a generic beam with
        dimension `b` and `h` over an alignment with N sections.

        Parameters
        ----------
        Ash_sbh : np.ndarray
            Required transverse reinforcement area to spacing ratio.
        nbl_t1 : np.ndarray
            Number of 1st type of longitudinal bars at top.
        nbl_t2 : np.ndarray
            Number of 2nd type of longitudinal bars at top.
        nbl_b1 : np.ndarray
            Number of 1st type of longitudinal bars at bottom.
        nbl_b2 : np.ndarray
            Number of 2nd type of longitudinal bars at bottom.
        dbl_t1 : np.ndarray
            Diameter of 1st type of longitudinal bars at top.
        dbl_b1 : np.ndarray
            Diameter of 1st type of longitudinal bars at bottom.
        b : float
            Beam breadth (width).
        h : float
            Beam height (depth).

        Returns
        -------
        dbh : np.ndarray
            Diameter of horizontal bars (transverse reinforcement).
        sbh : np.ndarray
            Spacing of horizontal bars (transverse reinforcement).
        nbh_parallel_b : np.ndarray
            Number of horizontal bars (stirrup legs) parallel to width.
        nbh_parallel_h : np.ndarray
            Number of horizontal bars (stirrup legs) parallel to height.

        Abbreviations for rebars
        ------------------------
        - The same of `get_beam_long_rebars`.

        Assumptions
        -----------
        - The same of `get_beam_long_rebars`.
        """
        # Initialization
        num_sec = len(Ash_sbh)  # Number of beam sections
        nbh_x = 2 * np.ones(num_sec)  # no. of legs parallel to width, always 2
        nbh_y = np.zeros(num_sec)  # no. of legs parallel to height
        sbh = np.zeros(num_sec)  # transverse reinforcement (bar) spacing
        dbh = np.zeros(num_sec)  # transverse reinforcement (bar) diameter
        # Maximum possible number of legs (bars) parallel to height
        max_nbh_y = np.minimum(nbl_t1 + nbl_t2, nbl_b1 + nbl_b2)
        # Minimum transverse reinforcement diameter
        dbh_min = self._get_min_beam_dbh(dbl=np.maximum(dbl_t1, dbl_b1))
        for j in range(num_sec):
            # Initial assumptions for number of legs and diameters
            nbh = 2  # start with closed stirrup
            leg_conf_dist = 0.9 * b[j] / (nbh - 1)
            while leg_conf_dist > self.beam_max_leg_dist:
                nbh += 1  # add stirrup
                leg_conf_dist = 0.9 * b[j] / (nbh - 1)
            # No. of stirrup legs parallel to height
            nbh_y[j] = nbh
            # Current transverse reinforcement diameter
            diff = self.beam_trans_bar_diams - dbh_min[j]
            dbh[j] = self.beam_trans_bar_diams[np.where(diff >= 0)[0][0]]
            # maximum allowed spacing in current iteration
            subsec_id = j % 3
            is_beam_end_section = (subsec_id == 0 or subsec_id == 2)
            if is_beam_end_section:
                max_sbh = self._get_beam_max_sbh_end(
                    b=b[j], h=h[j], dbh=dbh[j],
                    dbl=dbl_t1[j], cover=self.beam_cover)
                max_sbh = np.round(max_sbh, PRECISION)
            else:
                max_sbh = self._get_beam_max_sbh_mid(
                    b=b[j], h=h[j], dbh=dbh[j],
                    dbl=dbl_t1[j], cover=self.beam_cover)
                max_sbh = np.round(max_sbh, PRECISION)

            # Iterate for a solution
            iterate = True
            while iterate:
                # total transverse reinforcement area along y
                Ashy = 0.25 * np.pi * nbh_y[j] * dbh[j]**2
                if Ash_sbh[j] == 0.0:
                    sbhy = self.beam_trans_bar_spacings[0]
                else:
                    sbhy = Ashy / Ash_sbh[j]
                sbh[j] = min(sbhy, max_sbh)  # current spacing
                for spacing in self.beam_trans_bar_spacings:
                    if sbh[j] >= spacing:
                        sbh[j] = spacing  # This spacing works for this section
                        iterate = False  # Stop iterating for this section
                        break  # break the for loop

                if iterate:
                    if sbh[j] == sbhy and np.all(nbh_y[j] <= max_nbh_y[j]):
                        # add a stirrup leg along y
                        nbh_y[j] += 1
                    elif iterate and dbh[j] < max(self.beam_trans_bar_diams):
                        # increase transverse reinforcement diameter
                        idx = np.where(
                            self.beam_trans_bar_diams == dbh[j])[0][0]
                        dbh[j] = self.beam_trans_bar_diams[idx + 1]
                    elif iterate:
                        # Accept the underdesign, no solution is found.
                        nbh_y[j] = max_nbh_y[j]
                        sbh[j] = min(self.beam_trans_bar_spacings)
                        dbh[j] = max(self.beam_trans_bar_diams)
                        iterate = False

        return dbh, sbh, nbh_x, nbh_y
