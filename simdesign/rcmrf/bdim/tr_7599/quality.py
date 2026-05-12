"""This module provides the quality class implementation representing the
quality-based modifications for the ``tr_7599`` design class in the BDIM layer.
"""
# Imports from installed packages
from pathlib import Path
from typing import List, Literal
import numpy as np
from scipy.stats import lognorm, uniform, truncnorm
import json

# Imports from tr_7599
from .column import Column
from .beam import Beam

# Imports from bdim base library
from ..baselib.quality import QualityBase
from ..baselib.quality import QualityModelData as QualityModelDataBase
from ..baselib.quality import QualityData as QualityDataBase


POSSIBLE_FI = np.array([12, 16, 20, 24]) / 1000
"""Array of allowed reinforcement bar diameters (in meters) commonly used in
design."""
ALPHA_LOW = 0
"""Lower bound for scaling factor used in grid search for reinforcement
adjustment."""
ALPHA_HIGH = 1.05
"""Upper bound for scaling factor used in grid search for reinforcement
adjustment."""
STEP = 0.05
"""Step size for generating alpha scaling factors between ALPHA_LOW
and ALPHA_HIGH."""
# Generate scaling factor grid for modifying reinforcement configurations
alphas = np.arange(ALPHA_LOW, ALPHA_HIGH, STEP)
# Generate 2D meshgrid of alphas for longitudinal bar diameters and bar counts
alpha_dbl, alpha_nbl = np.meshgrid(alphas, alphas)
# Flatten the scaling factors to vectors
alpha_dbl_flat = alpha_dbl.ravel()
alpha_nbl_flat = alpha_nbl.ravel()


class QualityModelData(QualityModelDataBase):
    """Construction quality model data for the ``tr_7599`` design class.

    This class extends the ``QualityModelData`` class in baselib by introducing
    new attributes related to the adjusted longitudinal reinforcement ratio.

    Attributes
    ----------
    uniform_low_sbh_column : float
        Lower boundary of uniform stirrup spacing ratio distribution in
        columns.
    uniform_up_sbh_column : float
        Upper boundary of uniform stirrup spacing ratio distribution in
        columns.
    mean_col_rhol : float
        Mean of in-situ to design rhol ratio distribution.
    std_col_rhol : float
        Standard deviation of in-situ to design rhol ratio distribution.
    lower_col_rhol : float
        Lower bound of in-situ to design rhol ratio distribution.
    upper_col_rhol : float
        Upper bound of in-situ to design rhol ratio distribution.
    mean_beam_rhol_top : float
        Mean of in-situ to design rhol ratio distribution.
    std_beam_rhol_top : float
        Standard deviation of in-situ to design rhol ratio distribution.
    lower_beam_rhol_top : float
        Lower bound of in-situ to design rhol ratio distribution.
    upper_beam_rhol_top : float
        Upper bound of in-situ to design rhol ratio distribution.
    mean_beam_rhol_bot : float
        Mean of in-situ to design rhol ratio distribution.
    std_beam_rhol_bot : float
        Standard deviation of in-situ to design rhol ratio distribution.
    lower_beam_rhol_bot : float
        Lower bound of in-situ to design rhol ratio distribution.
    upper_beam_rhol_bot : float
        Upper bound of in-situ to design rhol ratio distribution.

    See Also
    --------
    :class:`~QualityModelDataBase`
        Base class defining the core behaviour and configuration.
    """
    uniform_low_sbh_column: float
    uniform_up_sbh_column: float
    mean_col_rhol: float
    std_col_rhol: float
    lower_col_rhol: float
    upper_col_rhol: float
    mean_beam_rhol_top: float
    std_beam_rhol_top: float
    lower_beam_rhol_top: float
    upper_beam_rhol_top: float
    mean_beam_rhol_bot: float
    std_beam_rhol_bot: float
    lower_beam_rhol_bot: float
    upper_beam_rhol_bot: float


class QualityData(QualityDataBase):
    """Construction quality models for the ``tr_7599`` design class.

    This class extends ``QualityDataBase`` class in baselib by narrowing
    the attribute types.

    Attributes
    ----------
    high : QualityModelData
        High construction quality model.
    moderate : QualityModelData
        Moderate construction quality model.
    low : QualityModelData
        Low construction quality model.

    See Also
    --------
    :class:`~QualityDataBase`
        Base class defining the core behaviour and configuration.
    """
    high: QualityModelData
    moderate: QualityModelData
    low: QualityModelData


class Quality(QualityBase):
    """Quality implementation for the ``tr_7599`` design class.

    This class extends ``QualityBase`` by narrowing the attribute types
    and overriding :meth:`set_adjusted_properties` method.

    Attributes
    ----------
    data_path : Path
        Path to the JSON file containing construction quality data.
    data : QualityData
        All the construction quality data considered for the design class.
    _model : QualityModelData
        Internal attribute for selected construction quality model.

    See Also
    --------
    :class:`~QualityBase`
        Base class defining the core behaviour and configuration.
    """
    data_path: Path | str = Path(__file__).parent / 'data' / 'quality.json'
    data: QualityData
    _model: QualityModelData

    def __init__(self) -> None:
        """Initialize a new instance of Quality class.
        """
        # Load quality model data
        with open(self.data_path, 'r') as json_file:
            # Load the JSON data into a Python dictionary
            data = json.load(json_file)
            # Store the quality model
            self.data = QualityData(**data)
        # Set the seed to use
        if self.seed:
            np.random.seed(self.seed)

    @property
    def model(self) -> QualityModelData:
        """Get the selected construction quality model.

        Returns
        -------
        QualityModelData
            Construction quality model.
        """
        return self._model

    @model.setter
    def model(self, identifier: Literal[0, 1, 2, 3]) -> None:
        """Select construction quality model based on the quality identifier.

        Parameters
        ----------
        identifier : Literal[0, 1, 2, 3]
            Construction quality identifier
            0. Excellent construction quality.
            1. High construction quality.
            2. Moderate construction quality.
            3. Low construction quality.

        Notes
        -----
        Excellent construction quality (0) corresponds to the expected values.
        In other words, quality based modification is not performed to adjust
        the expected parameters through sampling (deterministic mode). Fixed
        parameters such as bondslip_factor correspond to that of high
        construction quality.
        """
        mapper = {
            0: self.data.high,
            1: self.data.high,
            2: self.data.moderate,
            3: self.data.low
        }
        self._model = mapper.get(identifier)
        if identifier == 0:
            self._model.rand = False

    def set_adjusted_properties(self, beams: List[Beam],
                                columns: List[Column]) -> None:
        """Set the quality adjusted properties of beams and columns:

        Notes
        -----
        In particular, the following properties are modified:
        - Concrete compressive strength
        - Longitudinal reinforcement yield strength
        - Transverse reinforcement yield strength
        - Concrete cover
        - Stirrup spacing
        - Number of longitudinal bars
        - Diameter of longitudinal bars

        Parameters
        ----------
        beams : List[~simdesign.rcmrf.bnsm.baselib.beam.BeamBase]
            List of beams whose properties will be adjusted.
        columns : List[~simdesign.rcmrf.bnsm.baselib.column.ColumnBase]
            List of columns whose properties will be adjusted.
        """
        # Initialize some parameters
        theta_fck = self.model.theta_fck
        sigma_fck = self.model.sigma_fck
        theta_fsyk = self.model.theta_fsyk
        sigma_fsyk = self.model.sigma_fsyk
        theta_cover = self.model.theta_cover
        sigma_cover = self.model.sigma_cover
        uniform_low_sbh = self.model.uniform_low_sbh
        uniform_up_sbh = self.model.uniform_up_sbh
        uniform_low_sbh_column = self.model.uniform_low_sbh_column
        uniform_up_sbh_column = self.model.uniform_up_sbh_column
        num_columns = len(columns)
        num_beams = len(beams)

        # NOTE: Mean strength ratio is also randomised*
        theta_fck = lognorm.ppf(np.random.rand(), s=sigma_fck, scale=theta_fck)

        if self._model.rand:
            # Concrete compressive strength
            col_fc_ratio = lognorm.ppf(
                np.random.rand(num_columns), s=sigma_fck, scale=theta_fck
            )
            beam_fc_ratio = lognorm.ppf(
                np.random.rand(num_beams), s=sigma_fck, scale=theta_fck
            )
            # Longitudinal steel yield strength
            col_fsyl_ratio = lognorm.ppf(
                np.random.rand(num_columns), s=sigma_fsyk, scale=theta_fsyk
            )
            beam_fsyl_ratio = lognorm.ppf(
                np.random.rand(num_beams), s=sigma_fsyk, scale=theta_fsyk
            )
            # Transverse steel yield strength
            col_fsyh_ratio = lognorm.ppf(
                np.random.rand(num_columns), s=sigma_fsyk, scale=theta_fsyk
            )
            beam_fsyh_ratio = lognorm.ppf(
                np.random.rand(num_beams), s=sigma_fsyk, scale=theta_fsyk
            )
            # Concrete cover
            col_cover_ratio = lognorm.ppf(
                np.random.rand(num_columns), s=sigma_cover, scale=theta_cover
            )
            beam_cover_ratio = lognorm.ppf(
                np.random.rand(num_beams), s=sigma_cover, scale=theta_cover
            )
            # Stirrup spacing
            col_sbh_ratio = uniform.ppf(
                np.random.rand(num_columns),
                loc=uniform_low_sbh_column,
                scale=uniform_up_sbh_column - uniform_low_sbh_column,
            )
            beam_sbh_start_ratio = uniform.ppf(
                np.random.rand(num_beams),
                loc=uniform_low_sbh,
                scale=uniform_up_sbh - uniform_low_sbh,
            )
            beam_sbh_end_ratio = uniform.ppf(
                np.random.rand(num_beams),
                loc=uniform_low_sbh,
                scale=uniform_up_sbh - uniform_low_sbh,
            )
            beam_sbh_mid_ratio = uniform.ppf(
                np.random.rand(num_beams),
                loc=uniform_low_sbh,
                scale=uniform_up_sbh - uniform_low_sbh,
            )

        else:
            # Concrete compressive strength
            col_fc_ratio = np.ones(num_columns)
            beam_fc_ratio = np.ones(num_beams)
            # Longitudinal steel yield strength
            col_fsyl_ratio = np.ones(num_columns)
            beam_fsyl_ratio = np.ones(num_beams)
            # Transverse steel yield strength
            col_fsyh_ratio = np.ones(num_columns)
            beam_fsyh_ratio = np.ones(num_beams)
            # Concrete cover
            col_cover_ratio = np.ones(num_columns)
            beam_cover_ratio = np.ones(num_beams)
            # Stirrup spacing
            col_sbh_ratio = np.ones(num_columns)
            beam_sbh_start_ratio = np.ones(num_beams)
            beam_sbh_end_ratio = np.ones(num_beams)
            beam_sbh_mid_ratio = np.ones(num_beams)

        # Store adjusted properties of columns
        for i, col in enumerate(columns):
            col.fc_q = col.fcm * col_fc_ratio[i]
            col.fsyl_q = col.fsym * col_fsyl_ratio[i]
            col.fsyh_q = col.fsym * col_fsyh_ratio[i]
            col.cover_q = col.cover * col_cover_ratio[i]
            col.sbh_q = col.sbh * col_sbh_ratio[i]
            # Extra design parameters which can be quality adjusted
            col.dbh_q = col.dbh
            col.nbh_x_q = col.nbh_x
            col.nbh_y_q = col.nbh_x
            col.dbl_cor_q = col.dbl_cor
            col.dbl_int_q = col.dbl_int
            col.nblx_int_q = col.nblx_int
            col.nbly_int_q = col.nbly_int

        # Store adjusted properties of beams
        for i, beam in enumerate(beams):
            beam.fc_q = beam.fcm * beam_fc_ratio[i]
            beam.fsyl_q = beam.fsym * beam_fsyl_ratio[i]
            beam.fsyh_q = beam.fsym * beam_fsyh_ratio[i]
            beam.cover_q = beam.cover * beam_cover_ratio[i]
            sbh_start = beam.sbh[0] * beam_sbh_start_ratio[i]
            sbh_mid = beam.sbh[1] * beam_sbh_mid_ratio[i]
            sbh_end = beam.sbh[2] * beam_sbh_end_ratio[i]
            beam.sbh_q = np.array([sbh_start, sbh_mid, sbh_end])
            # Extra design parameters which can be quality adjusted
            beam.nbh_b_q = beam.nbh_b
            beam.nbh_h_q = beam.nbh_h
            beam.dbh_q = beam.dbh
            beam.dbl_t1_q = beam.dbl_t1
            beam.nbl_t1_q = beam.nbl_t1
            beam.dbl_t2_q = beam.dbl_t2
            beam.nbl_t2_q = beam.nbl_t2
            beam.dbl_b1_q = beam.dbl_b1
            beam.nbl_b1_q = beam.nbl_b1
            beam.dbl_b2_q = beam.dbl_b2
            beam.nbl_b2_q = beam.nbl_b2

        if not self._model.rand:
            return

        # Start adjusting column longitudinal reinforcement ratio
        # Compute ratio of in-situ vs. design rhol
        if self._model.std_col_rhol == 0.0:
            ratios = self._model.mean_col_rhol * np.ones(len(columns))
        else:
            mean = self._model.mean_col_rhol
            std = self._model.std_col_rhol
            lower = self._model.lower_col_rhol
            upper = self._model.upper_col_rhol
            # Convert to standard normal bounds
            a, b = (lower - mean) / std, (upper - mean) / std
            # Create and sample
            trunc_normal = truncnorm(a, b, loc=mean, scale=std)
            ratios = trunc_normal.rvs(size=len(columns))
        # Start changing column
        for i, col in enumerate(columns):
            self._grid_search_reduce_col_rhol_q(col, ratios[i])

        # Start adjusting beam top longitudinal reinforcement ratio
        # Compute ratio of in-situ vs. design rhol
        if self._model.std_beam_rhol_top == 0.0:
            ratios = self._model.mean_beam_rhol_top * np.ones(len(beams))
        else:
            mean = self._model.mean_beam_rhol_top
            std = self._model.std_beam_rhol_top
            lower = self._model.lower_beam_rhol_top
            upper = self._model.upper_beam_rhol_top
            # Convert to standard normal bounds
            a, b = (lower - mean) / std, (upper - mean) / std
            # Create and sample
            trunc_normal = truncnorm(a, b, loc=mean, scale=std)
            ratios = trunc_normal.rvs(size=len(beams))
        # Start changing beam
        for i, beam in enumerate(beams):
            self._grid_search_reduce_beam_rhol_top_q(beam, ratios[i])

        # Start adjusting beam bottom longitudinal reinforcement ratio
        # Compute ratio of in-situ vs. design rhol
        if self._model.std_beam_rhol_bot == 0.0:
            ratios = self._model.mean_beam_rhol_bot * np.ones(len(beams))
        else:
            mean = self._model.mean_beam_rhol_bot
            std = self._model.std_beam_rhol_bot
            lower = self._model.lower_beam_rhol_bot
            upper = self._model.upper_beam_rhol_bot
            # Convert to standard normal bounds
            a, b = (lower - mean) / std, (upper - mean) / std
            # Create and sample
            trunc_normal = truncnorm(a, b, loc=mean, scale=std)
            ratios = trunc_normal.rvs(size=len(beams))
        # Start changing beam
        for i, beam in enumerate(beams):
            self._grid_search_reduce_beam_rhol_bot_q(beam, ratios[i])

    def _grid_search_reduce_col_rhol_q(
        self, col: Column, target_ratio: float
    ) -> None:
        """Reduces the longitudinal reinforcement ratio (rhol) of a column
        by selecting the closest feasible bar configuration.

        This is done via a brute-force grid search over a precomputed meshgrid
        of scaling factors applied to:
        - Corner and internal longitudinal bar diameters.
        - Internal bar counts in x and y directions.

        The best combination is selected to minimize the error from
        the target in-situ/design rhol ratio.

        Parameters
        ----------
        col : Column
            Column object whose reinforcement configuration is to be modified.
        target_ratio : float
            Target ratio of in-situ to design longitudinal reinforcement.
        """
        if target_ratio == 1.0:
            return

        orig_dbl_cor = col.dbl_cor
        orig_dbl_int = col.dbl_int
        orig_nbly = col.nbly_int
        orig_nblx = col.nblx_int
        Ag = col.Ag
        original_rhol = col.rhol
        target_rhol = target_ratio * original_rhol

        # Compute scaled diameters and bar counts
        dbl_cor_scaled = self.__closest_diameter(orig_dbl_cor * alpha_dbl_flat)
        dbl_int_scaled = self.__closest_diameter(orig_dbl_int * alpha_dbl_flat)
        nbly_scaled = np.maximum(0, (orig_nbly * alpha_nbl_flat).astype(int))
        nblx_scaled = np.maximum(0, (orig_nblx * alpha_nbl_flat).astype(int))

        # Compute areas
        Abl_cor = (np.pi * dbl_cor_scaled**2) / 4
        Abl_int = (np.pi * dbl_int_scaled**2) / 4
        nbl_cor = 4
        nbl_int = 2 * (nbly_scaled + nblx_scaled)

        # Compute rhol_q for all combinations
        rhol_q = (nbl_cor * Abl_cor + nbl_int * Abl_int) / Ag
        error = np.abs(rhol_q - target_rhol)

        # Find best configuration
        best_idx = np.argmin(error)
        col.dbl_cor_q = dbl_cor_scaled[best_idx]
        col.dbl_int_q = dbl_int_scaled[best_idx]
        col.nbly_int_q = nbly_scaled[best_idx]
        col.nblx_int_q = nblx_scaled[best_idx]

    def _grid_search_reduce_beam_rhol_top_q(
        self, beam: Beam, target_ratio: float
    ) -> None:
        """Reduces the top longitudinal reinforcement ratio
        (rhol) of a beam by selecting the closest feasible bar
        configuration.

        This is done via a brute-force grid search over a precomputed meshgrid
        of scaling factors applied to:
        - Top layer bar diameters (dbl_t1, dbl_t2).
        - Secondary top bar count (nbl_t2).

        The best combination is selected to minimize the error from
        the target in-situ/design rhol ratio.

        Parameters
        ----------
        beam : Beam
            Beam object whose reinforcement configuration is to be modified.
        target_ratio : float
            Target ratio of in-situ to design longitudinal reinforcement.
        """
        if target_ratio == 1.0:
            return

        orig_dbl_t1 = beam.dbl_t1[0]
        orig_dbl_t2 = beam.dbl_t2[0]
        orig_nbl_t2 = beam.nbl_t2[0]
        Ag = beam.Ag
        original_rhol_top = beam.rhol_top[0]
        target_rhol_top = target_ratio * original_rhol_top

        # Compute scaled diameters and bar counts
        dbl_t1_scaled = self.__closest_diameter(orig_dbl_t1 * alpha_dbl_flat)
        dbl_t2_scaled = self.__closest_diameter(orig_dbl_t2 * alpha_dbl_flat)
        nbl_t2_scaled = np.maximum(
            0, (orig_nbl_t2 * alpha_nbl_flat).astype(int)
        )

        # Compute areas
        Abl_t1 = (np.pi * dbl_t1_scaled**2) / 4
        Abl_t2 = (np.pi * dbl_t2_scaled**2) / 4

        # Compute rhol_q for all combinations
        rhol_top_q = (2 * Abl_t1 + nbl_t2_scaled * Abl_t2) / Ag
        error = np.abs(rhol_top_q - target_rhol_top)

        # Find best configuration
        best_idx = np.argmin(error)
        beam.dbl_t1_q[0] = dbl_t1_scaled[best_idx]
        beam.dbl_t2_q[0] = dbl_t2_scaled[best_idx]
        beam.nbl_t2_q[0] = nbl_t2_scaled[best_idx]
        beam.dbl_t1_q[2] = dbl_t1_scaled[best_idx]
        beam.dbl_t2_q[2] = dbl_t2_scaled[best_idx]
        beam.nbl_t2_q[2] = nbl_t2_scaled[best_idx]

    def _grid_search_reduce_beam_rhol_bot_q(
        self, beam: Beam, target_ratio: float
    ) -> None:
        """Reduces the bottom longitudinal reinforcement ratio
        (rhol) of a beam by selecting the closest feasible bar
        configuration.

        This is done via a brute-force grid search over a precomputed meshgrid
        of scaling factors applied to:
        - Bottom layer bar diameters (dbl_b1, dbl_b2).
        - Secondary bottom bar count (nbl_b2).

        The best combination is selected to minimize the error from
        the target in-situ/design rhol ratio.

        Parameters
        ----------
        beam : Beam
            Beam object whose reinforcement configuration is to be modified.
        target_ratio : float
            Target ratio of in-situ to design longitudinal reinforcement.
        """
        if target_ratio == 1.0:
            return

        orig_dbl_b1 = beam.dbl_b1[0]
        orig_dbl_b2 = beam.dbl_b2[0]
        orig_nbl_b2 = beam.nbl_b2[0]
        Ag = beam.Ag
        original_rhol_bot = beam.rhol_bot[0]
        target_rhol_bot = target_ratio * original_rhol_bot

        # Compute scaled diameters and bar counts
        dbl_b1_scaled = self.__closest_diameter(orig_dbl_b1 * alpha_dbl_flat)
        dbl_b2_scaled = self.__closest_diameter(orig_dbl_b2 * alpha_dbl_flat)
        nbl_b2_scaled = np.maximum(
            0, (orig_nbl_b2 * alpha_nbl_flat).astype(int)
        )

        # Compute areas
        Abl_b1 = (np.pi * dbl_b1_scaled**2) / 4
        Abl_b2 = (np.pi * dbl_b2_scaled**2) / 4

        # Compute rhol_q for all combinations
        rhol_bot_q = (2 * Abl_b1 + nbl_b2_scaled * Abl_b2) / Ag
        error = np.abs(rhol_bot_q - target_rhol_bot)

        # Find best configuration
        best_idx = np.argmin(error)
        beam.dbl_b1_q[0] = dbl_b1_scaled[best_idx]
        beam.dbl_b2_q[0] = dbl_b2_scaled[best_idx]
        beam.nbl_b2_q[0] = nbl_b2_scaled[best_idx]
        beam.dbl_b1_q[2] = dbl_b1_scaled[best_idx]
        beam.dbl_b2_q[2] = dbl_b2_scaled[best_idx]
        beam.nbl_b2_q[2] = nbl_b2_scaled[best_idx]

    @staticmethod
    def __closest_diameter(values):
        """Returns the largest possible diameter that is less than or equal
        to each value in the input array.

        Parameters
        ----------
        values : np.ndarray
            Input array of diameter values.

        Returns
        -------
        np.ndarray
            Array of closest possible diameters.
        """
        indices = np.searchsorted(POSSIBLE_FI, values, side='right') - 1
        indices = np.clip(indices, 0, len(POSSIBLE_FI) - 1)
        return POSSIBLE_FI[indices]
