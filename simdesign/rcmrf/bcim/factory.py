"""BCIM factory module.

This module provides a factory interface for generating Building Class
Information Model (BCIM) for a given design class, number of storeys
and lateral load coefficient (beta).
"""
# Imports from installed packages
import json
import pandas as pd
from pathlib import Path
from typing import Dict, List, Literal, Optional, Union

# Imports from bcim library
from .parametrization import ArchetypeData, InputData
from .randomization import Sampler

# Imports from bdim common library
from ..bdim.baselib.building import TaxonomyData

# Imports from geometry library
from ..geometry import StandardGeometry

# Imports from utils library
from ...utils.misc import make_dir


INFILL_TYPE_MAPPER = {1: 'Weak', 2: 'Medium', 3: 'Strong'}
"""Infill typology mapper."""
INFILL_XZ_LIST = [1, 2, 3, 5, 6, 7, 9, 10, 11]
"""List of infill configuration IDs where infills exist in XZ plane."""
INFILL_YZ_LIST = [1, 2, 4, 5, 6, 8, 9, 10, 12]
"""List of infill configuration IDs where infills exist in YZ plane."""
INFILL_GROUND_LIST = [1, 5, 9]
"""List of infill configuration IDs where infills exist in ground floor."""
INFILL_INTERIOR_LIST = [5, 6, 7, 8, 9, 10, 11, 12]
"""List of infill configuration IDs where infills exist in interior frames."""
INFILL_EXTERIOR_LIST = [1, 2, 3, 4, 5, 6, 7, 8]
"""List of infill configuration IDs where infills exist in exterior frames."""


class Archetypes:
    """Orchestrator for the building archetypes data loaded from layouts file.

    Attributes
    ----------
    file_path : Path
        Path to the CSV file containing archetype data.
    all_data : List[ArchetypeData]
        List containing all archetype data loaded from the CSV file.
    """
    file_path: Path = Path(__file__).parent / 'data' / 'layouts.csv'
    all_data: List[ArchetypeData]

    def __init__(self) -> None:
        """Initialize the Archetypes instance by loading data from the CSV
        file.
        """
        csv_data = pd.read_csv(self.file_path)
        self.all_data = []
        for _, row in csv_data.iterrows():
            self.all_data.append(ArchetypeData(**row.to_dict()))

    @property
    def available_tags(self) -> List[str]:
        """List of available archetype tags.

        Returns
        -------
        List[str]
            List of available archetype tags.
        """
        return [archetype.tag for archetype in self.all_data]

    def get_data_for_given_tag(self, tag: str) -> Optional[ArchetypeData]:
        """Retrieve archetype data for the given tag.

        Parameters
        ----------
        tag : str
            The tag of the archetype (floor layout) for which data is
            requested.

        Returns
        -------
        ArchetypeData | None
            Archetype data (floor layout) if found, None otherwise.
        """
        if tag in self.available_tags:
            index = self.available_tags.index(tag)
            return self.all_data[index]

    def get_data_for_given_tags(
        self, tags: List[str]
    ) -> Optional[List[ArchetypeData]]:
        """Retrieve archetype data for the given list of tags.

        Parameters
        ----------
        tags : List[str]
            The list of tags for which archetype (floor layout) data is
            requested.

        Returns
        -------
        List[ArchetypeData] | None
            List of archetype data for the requested tags.
        """
        data_list = []
        for tag in tags:
            data = self.get_data_for_given_tag(tag)
            if data:
                data_list.append(data)
        # Return data for requested archetypes
        if any(data_list):
            return data_list

    def get_geometry(
        self, tag: str, num_storeys: int, storey_height: float,
        ground_storey_height: float, bay_width_x: float,
        bay_width_y: float, stairs_width_x: float, infill_loc: int,
        ext_infill: int, int_infill: int
    ) -> StandardGeometry:
        """Retrieve the geometry of a building archetype for the given tag.

        Parameters
        ----------
        tag : str
            The tag of the archetype (layout) for which geometry is
            requested.
        num_storeys : int
            Number of storeys in the building.
        storey_height : float
            Height of each storey.
        ground_storey_height : float
            Height of the ground storey.
        bay_width_x : float
            Width of the bays along the x-axis.
        bay_width_y : float
            Width of the bays along the y-axis.
        stairs_width_x : float
            Width of the stairs along the x-axis.
        infill_loc : int
            Infill location configuration ID.
        ext_infill : int
            Exterior infill typology ID.
        int_infill : int
            Interior infill typology ID.

        Returns
        -------
        StandardGeometry
            StandardGeometry object representing the geometry of the building
            archetype.
        """
        flag_stairs = True

        data = self.get_data_for_given_tag(tag)
        # Grid ID of left bottom point (or bay ID in x and y)
        stair_loc = (data.stairs_grid_x, data.stairs_grid_y)
        # Initialise the frame object
        regular_frame = StandardGeometry(
            num_storeys, storey_height, data.num_bays_x, bay_width_x,
            data.num_bays_y, bay_width_y, tag)
        # Set infill settings
        xz = infill_loc in INFILL_XZ_LIST
        yz = infill_loc in INFILL_YZ_LIST
        ground = infill_loc in INFILL_GROUND_LIST
        exterior = infill_loc in INFILL_EXTERIOR_LIST
        interior = infill_loc in INFILL_INTERIOR_LIST
        ext_type = INFILL_TYPE_MAPPER.get(ext_infill)
        int_type = INFILL_TYPE_MAPPER.get(int_infill)
        # Add infills
        regular_frame.add_infills(xz, yz, ground, exterior,
                                  interior, ext_type, int_type)
        # Set stairs location
        if flag_stairs:
            regular_frame.set_continuous_stairs_rectangles(
                stair_loc, stairs_width_x)
        else:
            regular_frame.modify_bay_width(
                stair_loc[0] + 1, stairs_width_x, 'x')
        # Modifying a floor height (ground floors are usually modified)
        ground_storey_id = 1
        regular_frame.modify_floor_height(ground_storey_id,
                                          ground_storey_height)
        # Add the new lines and points for stairs (For now do this in the end)
        if flag_stairs:
            regular_frame.add_new_elements_for_stairs(ext_type, int_type)

        return regular_frame


class DefaultInputs:
    """The class to load and manage the default input data from JSON files.

    The data include the statistical distribution parameters required
    to perform random sampling, the parameters required to define building
    geometries per realization (e.g., num_storeys) and those required to
    perform simulated designs (e.g., beta).

    Attributes
    ----------
    defaults : Dict[str, InputData]
        Data from all JSON files.
    data_path : Path
        Path to the folder containing JSON files of the parameters.
    """
    defaults: Dict[str, InputData]
    data_path: Path = Path(__file__).parent / 'data'

    def __init__(self):
        """Initialize the DefaultInputs object by loading all JSON data.
        """
        json_files = list(self.data_path.glob('*.json'))
        self.defaults = {}
        for file in json_files:
            with open(file, 'r') as json_file:
                # Load the JSON data into a Python dictionary
                data = json.load(json_file)
                # Initiate the InputData object and store with its filename
                self.defaults[file.name] = InputData(**data)

    def get(self, design_class: str) -> InputData:
        """Return the parameters data for the specified design class.

        Parameters
        ----------
        design_class : str
            The design class for which the parameters will be returned.

        Returns
        -------
        InputData
            The parameters defined for the specified design class.
        """
        index = self.available_classes.index(design_class)
        filename = list(self.defaults.keys())[index]
        return self.defaults[filename]

    @property
    def available_classes(self) -> List[str]:
        """List of available design classes.

        Returns
        -------
        List[str]
            List of available design classes.
        """
        return [item.design_class for _, item in self.defaults.items()]


class BCIM:
    """The class to generate Building Class Information Model (BCIM) data.

    Currently, portfolio generation is limited to with fixed floor layouts and
    single staircase throughout buildings.

    Attributes
    ----------
    inputs : InputData
        Input parameters used for BCIM data generation.
    staircase_span_length_x : List[float]
        Staircase span length in x direction.
    staircase_span_length_y : List[float]
        Staircase span length in y direction.
    typical_span_length_x : List[float]
        Typical span length in x direction.
    typical_span_length_y : List[float]
        Typical span length in y direction.
    layout : List[str]
        Building floor layouts.
    typical_storey_height : List[float]
        Typical storey height.
    ground_storey_height : List[float]
        Ground storey height.
    slab_thickness : List[float | None]
        Slab thickness.
    slab_type : List[int]
        Slab type.
        1: Solid two-way cast-in-situ slabs (SS2).
        2: Solid one-way cast-in-situ slabs (SS1).
        3: One-way composite slab with ceramic blocks and RC joists or
        pre-stressed beams (HS).
    staircase_slab_depth : List[float | None]
        Depth of the staircase slabs.
    beam_type : List[int]
        Beam typology.
        1: Wide beams.
        2: Emergent beams.
    column_section : List[int]
        Column cross-section.
        1: Square solid section.
        2: Rectangular solid section.
    steel_grade : List[str]
        Steel material grade, e.g., 'S400'.
    concrete_grade : List[str]
        Concrete material grade, e.g., 'C20'.
    quality : List[int]
        Construction quality.
        1: High quality.
        2: Moderate quality.
        3: Low quality.
    geometry : List[StandardGeometry]
        List of building geometry instances.
    floor_width_x : List[float]
        Total floor width in x direction in floor layout.
    floor_width_y : List[float]
        Total floor width in y direction in floor layout.
    floor_area : List[float]
        Total floor area in floor layout.
    long_over_short_width : List[float]
        Ratio of longer to shorter floor widths in floor layout.
    beta : List[float]
        Design lateral load factor.
    beta_v : List[float | None]
        Vertical load factor.
    num_storeys : List[int]
        Number of storeys.
    design_class : List[str]
        Building design class.
    infill_conf : List[int]
        Masonry infill wall configuration IDs.
    ext_infill : List[int]
        Exterior infill typology IDs.
    int_infill : List[int]
        Interior infill typology IDs.
    """
    inputs: InputData
    __defaults: DefaultInputs
    __archetypes: Archetypes
    staircase_span_length_x: List[float]
    staircase_span_length_y: List[float]
    typical_span_length_x: List[float]
    typical_span_length_y: List[float]
    layout: List[str]
    typical_storey_height: List[float]
    ground_storey_height: List[float]
    slab_thickness: List[float | None]
    slab_type: List[Literal[1, 2, 3]]
    staircase_slab_depth: List[float | None]
    beam_type: List[Literal[1, 2]]
    column_section: List[Literal[1, 2]]
    steel_grade: List[str]
    concrete_grade: List[str]
    quality: List[Literal[1, 2, 3]]
    geometry: List[StandardGeometry]
    floor_width_x: List[float]
    floor_width_y: List[float]
    floor_area: List[float]
    long_over_short_width: List[float]
    beta: List[float]
    beta_v: List[float | None]
    num_storeys: List[int]
    design_class: List[float]
    infill_conf: List[int]
    ext_infill: List[int]
    int_infill: List[int]

    def __init__(self) -> None:
        """Initialize BCIM object.
        """
        self.__defaults = DefaultInputs()
        self.__archetypes = Archetypes()

    def generate(self, design_class: str, **inputs) -> None:
        """Generate BCIM data based on the specified inputs.

        This method uses the parameters defined in JSON files for the specified
        `design_class` as the default inputs. If a parameter needs to be
        changed, it can be specified as a keyword argument. All possible
        inputs other than `design_class` are listed in the Examples section.

        Parameters
        ----------
        design_class : str
            Building design class.
        **inputs
            Contains input parameters required for data generation.
            These will replace the defaults obtained for the specified
            `design_class`.

        Examples
        --------
        >>> design_class = "eu_cdh"
        >>> inputs = {
                "typical_storey_height": {
                    "cv": 0.07,
                    "mu": 2.90,
                    "lower_bound": 2.3,
                    "upper_bound": 3.8
                },
                "staircase_bay_width": {
                    "lower_bound": 2.8,
                    "upper_bound": 3.2
                },
                "standard_bay_width": {
                    "corr_coeff_xy": -0.92,
                    "lower_bound_x": 3.5,
                    "upper_bound_x": 7.5,
                    "theta_x": 4.5,
                    "sigma_x": 0.35,
                    "lower_bound_y": 3.5,
                    "upper_bound_y": 7.5,
                    "theta_y": 4.5,
                    "sigma_y": 0.35
                },
                "steel": {
                    "tag": ["S400", "S500"],
                    "probability": [0.10, 0.90]
                },
                "concrete": {
                    "tag": ["C20", "C25", "C30", "C35"],
                    "probability": [0.30, 0.45, 0.20, 0.05]
                },
                "ground_storey_height": {
                    "maximum": 4.20,
                    "factor": [1.0, 1.1, 1.2, 1.3, 1.4],
                    "probability": [0.55, 0.10, 0.20, 0.10, 0.05]
                },
                "construction_quality": {
                    "quality" [1, 2, 3]
                    "probability": [0.6, 0.3, 0.1]
                },
                "slab_typology": {
                    "ss1_prob_given_ss1_or_hs": 0.50,
                    "ss2_prob_given_ss2_or_hs": 0.65,
                    "upper_lim_for_min_ss_span_length": 6.0,
                    "upper_lim_for_max_ss2_span_ratio": 2.0,
                    "staircase_slab_depth": 0.15,
                    "floor_slab_thickness": 0.15
                },
                "exterior_infill_type": {
                    "typology" [1, 2, 3]
                    "probability": [0.4, 0.4, 0.2]
                },
                "interior_infill_type": {
                    "typology" [1, 2]
                    "probability": [0.5, 0.5]
                },
                "infill_configuration": {
                    "configuration" [1, 2, 5, 6]
                    "probability": [0.2, 0.2, 0.3, 0.3]
                },
                "wb_prob_given_hs": 0.50,
                "square_column_prob": 0.50,
                "layout": "all",
                "beta": 0.15,
                "num_storeys": 5,
                "seed": 1993,
                "sample_size": 150
            }
        """
        # Retrieve default input parameters for the design class
        defaults = self.__defaults.get(design_class).__dict__
        # Update the parameters based on user input
        for key in inputs.keys():
            if key in defaults.keys():
                bool1 = isinstance(inputs[key], dict)
                bool2 = isinstance(defaults[key], dict)
                if bool1 and bool2:
                    inputs_sub: dict = inputs[key]
                    defaults_sub: dict = defaults[key]
                    for subkey in inputs_sub:
                        if subkey in defaults_sub.keys():
                            defaults_sub[subkey] = inputs_sub[subkey]
                else:
                    defaults[key] = inputs[key]
        # Store the updated input parameters
        self.inputs = InputData(**defaults)
        # Add all floor layout names
        if self.inputs.layout == "all":
            self.inputs.layout = self.available_archetypes
        # Generate the model data
        self.__generate()

    def __generate(self) -> None:
        """Complete BCIM data generation process.
        """
        # Generate realisations
        self.__get_realisations()
        # Reset sampler and get the realisation as dictionary
        self.__get_geometries()
        # Add the rest
        self.beta = \
            [self.inputs.beta] * self.inputs.sample_size
        self.beta_v = \
            [self.inputs.beta_v] * self.inputs.sample_size
        self.num_storeys = \
            [self.inputs.num_storeys] * self.inputs.sample_size
        self.design_class = \
            [self.inputs.design_class] * self.inputs.sample_size
        self.staircase_slab_depth = \
            [self.inputs.slab_typology.staircase_slab_depth] * \
            self.inputs.sample_size
        self.slab_thickness = \
            [self.inputs.slab_typology.floor_slab_thickness] * \
            self.inputs.sample_size
        # Bay with in y direction for staircases is the same as typical one
        self.staircase_span_length_y = self.typical_span_length_y.copy()

    def __get_realisations(self) -> None:
        """Generate realisations for BCIM data.
        """
        # Set the sampler to use
        sampler = Sampler(
            self.inputs.sample_size, self.inputs.seed)
        # Spans with staircase
        tmp = self.inputs.staircase_bay_width
        self.staircase_span_length_x = \
            sampler.set_stair_span_length_x(
                tmp.lower_bound, tmp.upper_bound)
        # Typical spans
        tmp = self.inputs.standard_bay_width
        self.typical_span_length_x, self.typical_span_length_y = \
            sampler.set_typical_span_length(
                tmp.corr_coeff_xy, (tmp.lower_bound_x, tmp.lower_bound_y),
                (tmp.upper_bound_x, tmp.upper_bound_y),
                (tmp.theta_x, tmp.theta_y), (tmp.sigma_x, tmp.sigma_y))
        # Layouts
        tmp = self.inputs.layout
        self.layout = sampler.set_layout(tmp)
        # Typical storey heights
        tmp = self.inputs.typical_storey_height
        self.typical_storey_height = \
            sampler.set_typical_storey_height(
                tmp.cv, tmp.mu, tmp.lower_bound, tmp.upper_bound)
        # Ground storey heights
        tmp = self.inputs.ground_storey_height
        self.ground_storey_height = \
            sampler.set_ground_storey_height(
                tmp.factor, tmp.probability, tmp.maximum)
        # Slab type
        tmp = self.inputs.slab_typology
        self.slab_type = \
            sampler.set_slab_type(
                tmp.ss1_prob_given_ss1_or_hs, tmp.ss2_prob_given_ss2_or_hs,
                tmp.max_ss_short_span,
                tmp.max_ss2_aspect_ratio)
        # Beam types
        tmp = self.inputs.wb_prob_given_hs
        self.beam_type = sampler.set_beam_type(tmp)
        # Column types
        tmp = self.inputs.square_column_prob
        self.column_section = sampler.set_column_type(tmp)
        # Steel materials
        tmp = self.inputs.steel
        self.steel_grade = sampler.set_material_class(
            tmp.grade, tmp.probability, 'steel')
        # Concrete materials
        tmp = self.inputs.concrete
        self.concrete_grade = sampler.set_material_class(
            tmp.grade, tmp.probability, 'concrete')
        # Construction quality
        tmp = self.inputs.construction_quality
        self.quality = sampler.set_construction_quality(
            tmp.quality, tmp.probability)
        # Infill location configuration
        tmp = self.inputs.infill_configuration
        self.infill_conf = sampler.set_infill_conf(
            tmp.configuration, tmp.probability)
        # Exterior infill types
        tmp = self.inputs.exterior_infill_type
        self.ext_infill = sampler.set_ext_infill_type(
            tmp.typology, tmp.probability)
        # Interior infill types
        tmp = self.inputs.interior_infill_type
        self.int_infill = sampler.set_int_infill_type(
            tmp.typology, tmp.probability)

    def __get_geometries(self) -> None:
        """Generate building geometries for BCIM data.
        """
        # Get geometries for the sample
        geometries = []
        area = []
        lx = []
        ly = []
        long_over_short = []
        for i in range(self.inputs.sample_size):
            geometry = self.__archetypes.get_geometry(
                self.layout[i], self.inputs.num_storeys,
                self.typical_storey_height[i],
                self.ground_storey_height[i],
                self.typical_span_length_x[i],
                self.typical_span_length_y[i],
                self.staircase_span_length_x[i],
                self.infill_conf[i],
                self.ext_infill[i],
                self.int_infill[i])
            # Compute other attributes
            xs = geometry.system_grid_data.x.ordinates
            ys = geometry.system_grid_data.y.ordinates
            lx.append(max(xs) - min(xs))
            ly.append(max(ys) - min(ys))
            area.append(lx[i] * ly[i])
            long_over_short.append(max(lx[i], ly[i]) / min(lx[i], ly[i]))
            geometries.append(geometry)
        # Add the geometry attributes to bcim data
        self.geometry = geometries
        self.floor_width_x = lx
        self.floor_width_y = ly
        self.floor_area = area
        self.long_over_short_width = long_over_short

    def _update_geometries(self):
        """Update building geometries if new data is provided.
        """
        self.__get_geometries()

    @property
    def available_design_classes(self) -> List[str]:
        """List of available design classes.

        Returns
        -------
        List[str]
            List of available design classes that can be used for BCIM data
            generation.
        """
        return self.__defaults.available_classes

    @property
    def available_archetypes(self) -> List[str]:
        """List of available archetype tags.

        Returns
        -------
        List[str]
            List of available archetype (layouts) tags that can be used for
            BCIM data generation.
        """
        return self.__archetypes.available_tags

    @property
    def taxonomy(self) -> List[TaxonomyData]:
        """List of taxonomy data for each building realisation.

        Returns
        -------
        List[TaxonomyData]
            List of design inputs (taxonomy) for each building realisation.
        """
        names = ['slab_thickness', 'slab_type',
                 'staircase_slab_depth', 'beam_type', 'column_section',
                 'geometry', 'steel_grade', 'concrete_grade', 'quality',
                 'beta', 'beta_v', 'design_class']
        taxonomy_list = []
        for i in range(self.inputs.sample_size):
            data = {name: getattr(self, name)[i] for name in names}
            taxonomy = TaxonomyData(**data)
            taxonomy_list.append(taxonomy)

        return taxonomy_list

    def to_csv(self, path: Union[str, Path]) -> None:
        """Save the generated BCIM data to the specified CSV file.

        Parameters
        ----------
        path : str | Path
            File path of the csv file.
            e.g., My/Path/To/The/File.csv
        """
        names = ['staircase_span_length_x', 'typical_span_length_x',
                 'typical_span_length_y', 'layout',
                 'typical_storey_height', 'ground_storey_height',
                 'slab_type', 'beam_type', 'column_section',
                 'steel_grade', 'concrete_grade', 'quality',
                 'floor_width_x', 'floor_width_y', 'floor_area',
                 'long_over_short_width', 'beta', 'num_storeys',
                 'design_class', 'staircase_span_length_y',
                 'infill_conf', 'ext_infill', 'int_infill']
        data = {name: getattr(self, name) for name in names}
        data = pd.DataFrame(data)
        # Create the output directory if needed
        path = Path(path)
        if not Path.exists(path.parent):
            make_dir(path.parent)
        data.to_csv(path, index=False, float_format='%g')
