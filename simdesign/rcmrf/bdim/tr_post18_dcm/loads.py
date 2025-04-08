"""
Pydantic models for defining loads in tr_post18_dcm buildings.

NOTES
-----
1- "modify_seismic_load_combos" method were created to include
vertical load effect into the seismic combinations.
"""

# Imports from installed packages
from pathlib import Path
from typing import List, Type

# Imports from bdim base library
from ..baselib.loads import VariableBase, PermanentBase
from ..baselib.loads import CombinationBase, LoadsDataBase, LoadsBase


class Variable(VariableBase):
    """
    Model representing live loads (Q) for design class tr_post18_dcm.

    Attributes
    ----------
    floor : float
        Live load on the floor.
    roof : float
        Live load on the roof.
    staircase : float
        Live load on the staircase.
    """
    pass


class Permanent(PermanentBase):
    """
    Model representing superimposed dead loads (G) for design class
    tr_post18_dcm.

    Attributes
    ----------
    floor : float
        Superimposed dead load on the floor.
    roof : float
        Superimposed dead load on the roof.
    staircase : float
        Superimposed dead load on the staircase.
    infill : float
        Superimposed dead load due to infill walls.
    gamma_rc : float
        Unit weight of reinforced concrete.
    """
    pass


class Combination(CombinationBase):
    """
    Model representing a load combination for design class tr_post18_dcm.

    This combination includes:
    - Dead loads (G)
    - Live loads (Q)
    - Seismic loads (E+X, E-X, E+Y, E-Y)

    Attributes
    ----------
    tag : str
        Tag identifying the load combination.
    loads : Dict[Literal["G", "Q", "E+X", "E-X", "E+Y", "E-Y"], float]
        Dictionary containing load tags and factors corresponding to
        each load type in the load combination.
    masses : Dict[Literal["G", "Q"], float]
        Dictionary containing mass sources and factors used to compute
        seismic loads considered in the load combination.
        Default is None.
    """
    pass


class LoadsData(LoadsDataBase):
    """
    Model representing the format of loads data for design class tr_post18_dcm.

    Attributes
    ----------
    variable : Variable
        Object representing variable (live) loads.
    permanent : Permanent
        Object representing permanent (dead) loads.
    combinations : List[Combination]
        List of load combination objects.
    eccentricity : float
        Accidental eccentricity [in %] needs to be considered in the
        earthquake loading direction, by default 0.
    """
    variable: Variable
    """Object representing variable (live) loads."""
    permanent: Permanent
    """Object representing permanent (dead) loads."""
    combinations: List[Combination]
    """List of load combination objects."""


class Loads(LoadsBase):
    """Class for retrieving loads data from a json file
    for design class tr_post18.

    Attributes
    ----------
    variable : Variable
        Object representing variable (live) loads.
    permanent : Permanent
        Object representing permanent (dead) loads.
    combinations : List[Combination]
        List of load combinations.
    eccentricity : float
        Accidental eccentricity [in %] needs to be considered in the
        earthquake loading direction.
    _data_path : Path
        Path to the file containing loads data.
    _data_model : LoadsData
        Pydantic model used for loading data format.
    """
    variable: Variable
    """Object representing variable (live) loads."""
    permanent: Permanent
    """Object representing permanent (dead) loads."""
    combinations: List[Combination]
    """List of load combinations."""
    _data_path = Path(__file__).parent / 'data' / 'loads.json'
    """Path to the file containing loads data."""
    _data_model: Type[LoadsData]

    def __init__(self) -> None:
        """Initializes Loads object.
        """
        self._data_model = LoadsData
        super().__init__()

    def modify_seismic_load_combos(self, beta_v: float) -> None:
        """Modify load combinations containing seismic loading for
        vertical load effect.

        Returns
        -------
        None
        """
        seismic_strs = ["E+X", "E-X", "E+Y", "E-Y"]
        for combo in self.combinations:
            if any(item in seismic_strs for item in combo.loads.keys()):
                if combo.loads.get("G") == 1.0:
                    combo.loads["G"] = round(1.0 + 0.3 * (2/3) * beta_v, 2)
                elif combo.loads.get("G") == 0.9:
                    combo.loads["G"] = round(0.9 - 0.3 * (2/3) * beta_v, 2)
