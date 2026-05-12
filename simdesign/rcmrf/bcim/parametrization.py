"""This module provides pydantic models used for parametrizing BCIM inputs.
"""
from pydantic import BaseModel, Field
from typing import List, Union, Literal, Optional


class InfillType(BaseModel):
    """Infill typology IDs and their occurrence probability in
    the generated building portfolio.

    Attributes
    ----------
    typology : List[int]
        Infill typology identifiers (IDs).
    probability : List[float]
        Probability values for each typology ID.
    """
    typology: List[int] = Field(default_factory=lambda: [1, 2, 3])
    probability: List[float] = Field(
        default_factory=lambda: [0.6, 0.3, 0.1]
    )


class InfillConfiguration(BaseModel):
    """Infill configuration IDs and their occurrence probability in
    the generated building portfolio.

    Attributes
    ----------
    configuration : List[int]
        Infill configuration identifiers (IDs).
    probability : List[float]
        Probability values for each configuration ID.
    """
    configuration: List[int] = Field(default_factory=lambda: [1, 2])
    probability: List[float] = [0.7, 0.3]


class GroundStoreyHeight(BaseModel):
    """Parameters used to define ground storey heights.

    Sampled typical storey heights are factored by the `factor` values
    based on their `probability` to obtain ground storey heights.
    If the factored storey height exceeds `maximum`, it will be capped
    at `maximum`.

    Attributes
    ----------
    maximum : float
        Maximum possible ground storey height.
    factor : List[float]
        Factors applied to typical storey heights to obtain
        ground storey heights.
    probability : List[float]
        Corresponding probabilities of factors. The sum should be equal to 1.0.
    """
    maximum: float
    factor: List[float]
    probability: List[float]


class ConstructionQuality(BaseModel):
    """Construction quality IDs and their occurrence probability in
    the generated building portfolio.

    Attributes
    ----------
    quality : List[int]
        Construction quality identifiers (IDs).
    probability : List[float]
        Probability values for each quality ID.
    """
    quality: List[int] = [1, 2, 3]
    probability: List[float]


class SlabTypology(BaseModel):
    """Parameters required for slab typology sampling or decision tree.

    Attributes
    ----------
    ss1_prob_given_ss1_or_hs : float
        Probability of having SS1 type slab given that the slab type
        is either SS1 or HS.
    ss2_prob_given_ss2_or_hs : float
        Probability of having SS2 type slab given that the slab type
        is either SS2 or HS.
    max_ss_short_span : float
        Upper limit for the short span length in solid slabs (SS1, SS2).
    max_ss2_aspect_ratio : float
        Upper limit for the ratio of maximum to minimum span lengths
        in SS2 slabs.
    staircase_slab_depth : float | None
        Depth of the staircase slabs, by default None.
    floor_slab_thickness : float | None
        Thickness of the floor slabs, by default None.

    Notes
    -----
    1. SS2 refers to solid two-way cast-in-situ slabs.
    2. SS1 refers to solid one-way cast-in-situ slabs.
    3. HS refers to composite slabs with pre-fabricated joists and ceramic
       blocks.
    """
    ss1_prob_given_ss1_or_hs: float
    ss2_prob_given_ss2_or_hs: float
    max_ss_short_span: float = 6.0
    max_ss2_aspect_ratio: float = 2.0
    staircase_slab_depth: Optional[float] = None
    floor_slab_thickness: Optional[float] = None


class TypicalStoreyHeight(BaseModel):
    """Parameters for typical storey heights represented by a
    truncated log-normal distribution.

    Attributes
    ----------
    cv : float
        Coefficient of variation (sigma/mu).
    mu : float
        Mean value for the typical storey heights.
    lower_bound : float
        Lower bound value.
    upper_bound : float
        Upper bound value.
    """
    cv: float
    mu: float
    lower_bound: float
    upper_bound: float


class StaircaseBayWidth(BaseModel):
    """Parameters of the uniform distribution representing
    the staircase bay width.

    Attributes
    ----------
    lower_bound : float
        Lower bound value.
    upper_bound : float
        Upper bound value.
    """
    lower_bound: float
    upper_bound: float


class StandardBayWidth(BaseModel):
    """Parameters of the truncated log-normal distribution representing
    the standard bay width.

    Attributes
    ----------
    corr_coeff_xy : float
        Correlation coefficient between bay widths in two principal
        horizontal directions (-X and -Y).
    lower_bound_x : float
        Lower bound of truncated log-normal distribution (-X).
    upper_bound_x : float
        Upper bound of truncated log-normal distribution (-X).
    theta_x : float
        Median of log-normal distribution (-X).
    sigma_x : float
        Logarithmic standard deviation of the lognormal distribution (-X).
    lower_bound_y : float
        Lower bound of truncated log-normal distribution (-Y).
    upper_bound_y : float
        Upper bound of truncated log-normal distribution (-Y).
    theta_y : float
        Median of log-normal distribution (-Y).
    sigma_y : float
        Logarithmic standard deviation of the lognormal distribution (-Y).
    """
    corr_coeff_xy: float
    lower_bound_x: float
    upper_bound_x: float
    theta_x: float
    sigma_x: float
    lower_bound_y: float
    upper_bound_y: float
    theta_y: float
    sigma_y: float


class Material(BaseModel):
    """Material grades and their occurrence probabilities.

    Attributes
    ----------
    grade : List[str]
        Material tags, i.e., concrete strength classes or steel grades.
    probability : List[float]
        Occurrence probabilities for each material.
    """
    grade: List[str]
    probability: List[float]


class InputData(BaseModel):
    """Input parameters obtained from JSON files to generate BCIM data.

    Attributes
    ----------
    exterior_infill_type : InfillType
        Parameters for sampling exterior infill typologies.
    interior_infill_type : InfillType
        Parameters for sampling interior infill typologies.
    infill_configuration : InfillConfiguration
        Parameters for sampling infill location configurations.
    typical_storey_height : TypicalStoreyHeight
        Parameters for sampling typical storey heights.
    staircase_bay_width : StaircaseBayWidth
        Parameters for sampling staircase bay widths.
    standard_bay_width : StandardBayWidth
        Parameters for sampling standard bay widths.
    steel : Material
        Parameters for sampling steel grades.
    concrete : Material
        Parameters for sampling concrete grades.
    ground_storey_height : GroundStoreyHeight
        Parameters for ground storey height sampling or decision tree
        operations.
    construction_quality : ConstructionQuality
        Parameters for sampling construction quality levels.
    slab_typology : SlabTypology
        Parameters for slab typology sampling or decision tree operations.
    wb_prob_given_hs : float
        Probability of having wide beams (WB) given the slab type is HS.
    square_column_prob : float
        Probability of having square columns.
    layout : Union[Literal["all"], List[str]]
        Layout IDs considered for the building generation process.
        Can be "all" to include all layouts or a list of specific layouts.
    beta : float
        Design lateral load factor.
    beta_v : float | None
        Vertical load factor.
    num_storeys : int
        Number of storeys in the building.
    design_class : str
        Building seismic design class.
    sample_size : int
        Size of the generated sample.
    seed : int
        Seed value for the random number generator.
    """
    exterior_infill_type: InfillType = Field(default_factory=InfillType)
    interior_infill_type: InfillType = Field(default_factory=InfillType)
    infill_configuration: InfillConfiguration = Field(
        default_factory=InfillConfiguration)
    typical_storey_height: TypicalStoreyHeight
    staircase_bay_width: StaircaseBayWidth
    standard_bay_width: StandardBayWidth
    steel: Material
    concrete: Material
    ground_storey_height: GroundStoreyHeight
    construction_quality: ConstructionQuality
    slab_typology: SlabTypology
    wb_prob_given_hs: float
    square_column_prob: float
    layout: Union[Literal["all"], List[str]]
    beta: float
    beta_v: Optional[float] = None
    num_storeys: int
    design_class: str
    sample_size: int
    seed: int


class ArchetypeData(BaseModel):
    """Model representing data for a specific building archetype.

    Attributes
    ----------
    tag : str
        Unique identifier for the archetype.
    num_bays_x : int
        Number of bays along the X-axis.
    num_bays_y : int
        Number of bays along the Y-axis.
    stairs_grid_x : int
        Grid position of stairs along the X-axis.
    stairs_grid_y : int
        Grid position of stairs along the Y-axis.
    """
    tag: str
    num_bays_x: int
    num_bays_y: int
    stairs_grid_x: int
    stairs_grid_y: int
