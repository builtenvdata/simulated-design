"""This module provides the class implementations representing loads for the
``tr_post18_dch`` design class in the BDIM layer.
"""
# Imports from installed packages
from pathlib import Path
from typing import List, Type

# Imports from bdim base library
from ..baselib.loads import VariableBase, PermanentBase
from ..baselib.loads import CombinationBase, LoadsDataBase, LoadsBase


class Variable(VariableBase):
    """Variable load (Q) model implementation for the ``tr_post18_dch`` design
    class.

    This class directly uses the behaviour defined in ``VariableBase``.

    See Also
    --------
    :class:`~simdesign.rcmrf.bdim.baselib.loads.VariableBase`
        Base class defining the core behaviour and configuration.
    """


class Permanent(PermanentBase):
    """Permanent load (G) model implementation for the ``tr_post18_dch`` design
    class.

    This class directly uses the behaviour defined in ``PermanentBase``.

    See Also
    --------
    :class:`~simdesign.rcmrf.bdim.baselib.loads.PermanentBase`
        Base class defining the core behaviour and configuration.
    """


class Combination(CombinationBase):
    """Load combination model implementation for the ``tr_post18_dch`` design
    class.

    This class directly uses the behaviour defined in ``CombinationBase``.

    See Also
    --------
    :class:`~simdesign.rcmrf.bdim.baselib.loads.CombinationBase`
        Base class defining the core behaviour and configuration.
    """


class LoadsData(LoadsDataBase):
    """Loads data model implementation for the ``tr_post18_dch`` design class.

    This class extends ``LoadsDataBase`` by narrowing the attribute types.

    Attributes
    ----------
    variable : Variable
        Object representing variable (live) loads.
    permanent : Permanent
        Object representing permanent (dead) loads.
    combinations : List[Combination]
        List of load combination objects.

    See Also
    --------
    :class:`~simdesign.rcmrf.bdim.baselib.loads.LoadsDataBase`
        Base class defining the core behaviour and configuration.
    """
    variable: Variable
    permanent: Permanent
    combinations: List[Combination]


class Loads(LoadsBase):
    """Loads implementation for the ``tr_post18_dch`` design class.

    This class extends ``LoadsBase`` by narrowing the attribute types
    and with a new method.

    Attributes
    ----------
    variable : Variable
        Object representing variable (live) loads.
    permanent : Permanent
        Object representing permanent (dead) loads.
    combinations : List[Combination]
        List of load combinations.
    _data_path : Path
        Path to the file containing loads data.

    See Also
    --------
    :class:`~simdesign.rcmrf.bdim.baselib.loads.LoadsBase`
        Base class defining the core behaviour and configuration.

    Notes
    -----
    - Extends the class with :meth:`modify_seismic_load_combos` method to
      incorporate vertical load effect into the seismic combinations.
    """
    variable: Variable
    permanent: Permanent
    combinations: List[Combination]
    _data_path = Path(__file__).parent / 'data' / 'loads.json'
    _data_model: Type[LoadsData] = LoadsData

    def modify_seismic_load_combos(self, beta_v: float) -> None:
        """Modify load combinations containing seismic loading for
        vertical load effect.
        """
        seismic_strs = ["E+X", "E-X", "E+Y", "E-Y"]
        for combo in self.combinations:
            if any(item in seismic_strs for item in combo.loads.keys()):
                if combo.loads.get("G") == 1.0:
                    combo.loads["G"] = round(1.0 + 0.3 * (2/3) * beta_v, 2)
                elif combo.loads.get("G") == 0.9:
                    combo.loads["G"] = round(0.9 - 0.3 * (2/3) * beta_v, 2)
