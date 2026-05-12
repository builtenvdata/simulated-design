"""This module provides base classes for representing loads
within the BDIM layer.
"""
# Imports from installed packages
from abc import ABC
import json
import inspect
import numpy as np
from pathlib import Path
from pydantic import BaseModel
from typing import List, Literal, Type, Tuple, Dict, Optional


class VariableBase(BaseModel, ABC):
    """Abstract base class representing live loads (Q).

    Subclasses must provide the field values appropriate to the design class.

    Attributes
    ----------
    floor : float
        Live load on the floor (kN/m^2).
    roof : float
        Live load on the roof (kN/m^2).
    staircase : float
        Live load on the staircase (kN/m^2).
    """
    floor: float
    roof: float
    staircase: float


class PermanentBase(BaseModel, ABC):
    """Abstract base class representing superimposed dead loads (G).

    Subclasses must provide the field values appropriate to the design class.

    Attributes
    ----------
    floor : float
        Superimposed dead load on the floor (kN/m^2).
    roof : float
        Superimposed dead load on the roof (kN/m^2).
    staircase : float
        Superimposed dead load on the staircase (kN/m^2).
    gamma_rc : float
        Unit weight of reinforced concrete (kN/m^3).
    """
    floor: float
    roof: float
    staircase: float
    gamma_rc: float


class CombinationBase(BaseModel, ABC):
    """Abstract base class representing a load combination.

    Subclasses must provide the field values appropriate to the design class.
    The load combination can include dead loads (G), live loads (Q), and
    seismic loads (E+X, E-X, E+Y, E-Y).

    Attributes
    ----------
    tag : str
        Tag identifying the load combination.
    loads : Dict[Literal["G", "Q", "E+X", "E-X", "E+Y", "E-Y"], float]
        Dictionary containing load tags and factors corresponding to
        each load type in the load combination.
    masses : Dict[Literal["G", "Q"], float], optional
        Dictionary containing mass sources and factors used to compute
        seismic loads considered in the load combination. If not
        provided, defaults are assigned automatically by
        ``LoadsBase._set_mass_sources`` based on the gravity load
        factors present in ``loads``.
    """
    tag: str
    loads: Dict[Literal["G", "Q", "E+X", "E-X", "E+Y", "E-Y"], float]
    masses: Optional[Dict[Literal["G", "Q"], float]] = None


class LoadsDataBase(BaseModel, ABC):
    """Abstract base class representing the aggregated loads data.

    Subclasses must provide the field values appropriate to the design class.

    Attributes
    ----------
    variable : VariableBase
        Object representing variable (live) loads.
    permanent : PermanentBase
        Object representing permanent (dead) loads.
    combinations : List[CombinationBase]
        List of load combination objects.
    eccentricity : float
        Accidental eccentricity to be considered in the earthquake
        loading direction, expressed as a percentage (e.g. ``5.0``
        for 5%). Defaults to ``0.0``.
    """
    variable: VariableBase
    permanent: PermanentBase
    combinations: List[CombinationBase]
    eccentricity: float = 0.0


class LoadsBase(ABC):
    """Abstract base class for reading loads data from a JSON file.

    Subclasses must define the class variables ``_data_path`` and
    ``_data_model`` before instantiation, as ``__init__`` depends on
    both. Failing to do so will raise an ``AttributeError`` at runtime.

    Attributes
    ----------
    variable : VariableBase
        Object representing variable (live) loads.
    permanent : PermanentBase
        Object representing permanent (dead) loads.
    combinations : List[CombinationBase]
        List of load combinations.
    eccentricity : float
        Accidental eccentricity to be considered in the earthquake
        loading direction, expressed as a percentage (e.g. ``5.0``
        for 5%).
    _data_path : Path or str
        Class variable — must be defined by subclass. Path to the JSON
        file containing loads data.
    _data_model : Type[LoadsDataBase]
        Class variable — must be defined by subclass. Pydantic model
        used to validate and parse the loads data file.
    """
    variable: VariableBase
    permanent: PermanentBase
    combinations: List[CombinationBase]
    eccentricity: float
    _data_path: Path | str
    _data_model: Type[LoadsDataBase]

    @classmethod
    def get_data_path(cls) -> Path:
        """
        Return the path to the ``loads.json`` data file associated with the
        class.

        The path is resolved relative to the module where the class is defined,
        allowing subclasses to automatically reference their own ``data``
        directory.

        Returns
        -------
        Path
            Absolute path to the ``loads.json`` file located in the
            design class-specific ``data`` folder.

        TODO
        ----
        Utilise this method in the future instead of _data_path attribute.
        """
        file = inspect.getfile(cls)
        return Path(file).parent / 'data' / 'loads.json'

    def __init__(self) -> None:
        """Initialize a new instance of LoadsBase.

        Reads and parses the JSON file at ``_data_path`` using
        ``_data_model``. Both class variables must be defined by the
        subclass prior to calling this method.

        Raises
        ------
        FileNotFoundError
            If the file at ``_data_path`` does not exist.
        json.JSONDecodeError
            If the file at ``_data_path`` is not valid JSON.
        pydantic.ValidationError
            If the parsed data does not conform to ``_data_model``.
        """
        with open(self._data_path, 'r') as json_file:
            # Load the JSON data into a Python dictionary
            data = json.load(json_file)
            # Initiate the InputData object and store with its filename
            loads_data = self._data_model(**data)

        self.permanent = loads_data.permanent
        self.variable = loads_data.variable
        self.combinations = loads_data.combinations
        self.eccentricity = loads_data.eccentricity
        # Check for mass sources
        self._set_mass_sources()

    def get_seismic_load_combos(self) -> List[CombinationBase]:
        """Return load combinations containing seismic loading.

        Returns
        -------
        List[CombinationBase]
            List of seismic load combinations.
        """
        seismic_combos = []
        seismic_strs = ["E+X", "E-X", "E+Y", "E-Y"]
        for combo in self.combinations:
            if any(item in seismic_strs for item in combo.loads.keys()):
                seismic_combos.append(combo)

        return seismic_combos

    def get_gravity_load_combos(self) -> List[CombinationBase]:
        """Return load combinations containing only gravity loads.

        Other gravity loads such as snow (S) can be added. In that case,
        this method should be overridden in the subclass to extend
        ``grav_strs`` with the additional load keys (e.g.
        ``["G", "Q", "S"]``).

        Returns
        -------
        List[CombinationBase]
            List of gravity load combinations.
        """
        grav_combos = []
        grav_strs = ["G", "Q"]  # permanent, variable
        for combo in self.combinations:
            if all(item in grav_strs for item in combo.loads.keys()):
                grav_combos.append(combo)

        return grav_combos

    def _set_mass_sources(self) -> None:
        """Check for mass sources and assign defaults where absent.

        Iterates over all seismic load combinations. Combinations that
        already define ``masses`` are left unchanged; those without
        ``masses`` are assigned default values derived from the gravity
        load factors present in ``loads`` (``"G"`` and ``"Q"``),
        defaulting to ``0.0`` if either key is absent.

        If other gravity loads such as snow (S) are added,
        this method should be overridden in the subclass to handle the
        additional mass source, following the same pattern used here
        for ``"G"`` and ``"Q"``.
        """
        # Check for mass sources
        for combo in self.get_seismic_load_combos():
            if combo.masses:
                continue
            else:
                combo.masses = {}
                if 'G' in combo.loads.keys():
                    combo.masses["G"] = combo.loads["G"]
                else:
                    combo.masses["G"] = 0.0
                if 'Q' in combo.loads:
                    combo.masses["Q"] = combo.loads["Q"]
                else:
                    combo.masses["Q"] = 0.0

    def get_seismic_loads(
        self, beta: float, weights: np.ndarray, heights: np.ndarray
    ) -> Tuple[np.float64, np.ndarray]:
        """Calculate and return seismic loads (E).

        Parameters
        ----------
        beta : float
            Design lateral load factor expressed as a fraction of
            building weight.
        weights : np.ndarray
            Array of storey weights. Units must be consistent with
            those used for ``heights`` (e.g. kN if heights are in m).
        heights : np.ndarray
            Array of storey heights measured from the base, one entry
            per storey. Must be the same length as ``weights`` and use
            consistent units.

        Returns
        -------
        base_shear : np.float64
            Total base shear force, in the same units as ``weights``.
        forces : np.ndarray
            Seismic forces acting at each storey, distributed
            proportionally to the product of weight and height.
            Same shape as ``weights``.
        """
        base_shear = np.sum(beta * weights)
        forces = base_shear * (weights * heights) / np.sum(weights * heights)

        return base_shear, forces
