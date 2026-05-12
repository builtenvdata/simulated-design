"""This module provides the base class for representing the
construction quality-based modifications in the BDIM layer.
"""
# Imports from installed packages
from abc import ABC
import numpy as np
from scipy.stats import lognorm, uniform
import json
from pathlib import Path
from pydantic import BaseModel
from typing import Literal, Optional, List

# Imports from bdim base library
from .beam import BeamBase
from .column import ColumnBase


class QualityModelData(BaseModel):
    """Construction quality model data.

    Attributes
    ----------
    joint : Literal["inelastic", "elastic", "rigid"]
        Joint modelling option considered in nonlinear models.
    bondslip_factor : float
        Bondslip factor considered for nonlinear beam-column elements.
    theta_fck : float
        Median concrete strength ratio, by default 1.0.
    sigma_fck : float
        Logarithmic standard deviation of concrete strength ratio.
    theta_fsyk : float
        Median steel yield strength ratio, by default 1.0.
    sigma_fsyk : float
        Logarithmic standard deviation of steel yield strength ratio.
    theta_cover : float
        Median concrete cover ratio, by default 1.0.
    sigma_cover : float
        Logarithmic standard deviation of concrete cover ratio.
    uniform_low_sbh : float
        Lower boundary of uniform stirrup spacing ratio distribution.
    uniform_up_sbh : float
        Upper boundary of uniform stirrup spacing ratio distribution.
    rand : bool, optional
        If True, sample the parameters randomly from the relevant distribution.
        If False, always return 1.0 (deterministic mode). By default True.
    """
    joint: Literal["inelastic", "elastic", "rigid"]
    bondslip_factor: float
    theta_fck: float = 1.0
    sigma_fck: float
    theta_fsyk: float = 1.0
    sigma_fsyk: float
    theta_cover: float = 1.0
    sigma_cover: float
    uniform_low_sbh: float
    uniform_up_sbh: float
    rand: bool = True


class QualityData(BaseModel):
    """Construction quality models.

    Attributes
    ----------
    high : QualityModelData
        High construction quality model.
    moderate : QualityModelData
        Moderate construction quality model.
    low : QualityModelData
        Low construction quality model.
    """
    high: QualityModelData
    moderate: QualityModelData
    low: QualityModelData


class QualityBase(ABC):
    """Abstract base class for adjusting properties of structural members
    based on construction quality level.

    Attributes
    ----------
    data_path : Path | str
        Path to the json file containing all the construction quality data.
    data : QualityData
        All the construction quality data considered for the design class.
    _model : QualityModelData
        Internal attribute for selected construction quality model.
    seed : int, optional
        Seed number considered for generating random values, by default None.
    """
    data_path: Path | str
    data: QualityData
    _model: QualityModelData
    seed: Optional[int] = None

    def __init__(self) -> None:
        """Initialize a new instance of QualityBase.
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
        """Selected construction quality model.

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
            Construction quality identifier.
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

    def set_new_seed(self, seed: int) -> None:
        """Set a new random seed for reproducibility.

        Parameters
        ----------
        seed : int
            New seed value.
        """
        self.seed = seed
        np.random.seed(self.seed)

    def set_adjusted_properties(self, beams: List[BeamBase],
                                columns: List[ColumnBase]) -> None:
        """Set quality-adjusted properties of beams and columns.

        Parameters
        ----------
        beams : List[~simdesign.rcmrf.bdim.baselib.beam.BeamBase]
            List of beams whose properties will be adjusted.
        columns : List[~simdesign.rcmrf.bdim.baselib.column.ColumnBase]
            List of columns whose properties will be adjusted.

        Notes
        -----
        The following properties are adjusted:

        - Concrete compressive strength
        - Longitudinal reinforcement yield strength
        - Transverse reinforcement yield strength
        - Concrete cover
        - Stirrup spacing
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
                loc=uniform_low_sbh,
                scale=uniform_up_sbh - uniform_low_sbh,
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
