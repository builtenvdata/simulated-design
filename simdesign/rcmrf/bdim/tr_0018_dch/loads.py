"""This module provides the class implementations representing loads for the
``tr_0018_dch`` design class in the BDIM layer.
"""
# Imports from installed packages
from pathlib import Path
from typing import List, Type

# Imports from bdim base library
from ..baselib.loads import VariableBase, PermanentBase
from ..baselib.loads import CombinationBase, LoadsDataBase, LoadsBase


class Variable(VariableBase):
    """Variable load (Q) model implementation for the ``tr_0018_dch`` design
    class.

    This class directly uses the behaviour defined in ``VariableBase``.

    See Also
    --------
    :class:`~bdim.baselib.loads.VariableBase`
        Base class defining the core behaviour and configuration.
    """


class Permanent(PermanentBase):
    """Permanent load (G) model implementation for the ``tr_0018_dch`` design
    class.

    This class directly uses the behaviour defined in ``PermanentBase``.

    See Also
    --------
    :class:`~bdim.baselib.loads.PermanentBase`
        Base class defining the core behaviour and configuration.
    """


class Combination(CombinationBase):
    """Load combination model implementation for the ``tr_0018_dch`` design
    class.

    This class directly uses the behaviour defined in ``CombinationBase``.

    See Also
    --------
    :class:`~bdim.baselib.loads.CombinationBase`
        Base class defining the core behaviour and configuration.
    """


class LoadsData(LoadsDataBase):
    """Loads data model implementation for the ``tr_0018_dch`` design class.

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
    :class:`~bdim.baselib.loads.LoadsDataBase`
        Base class defining the core behaviour and configuration.
    """
    variable: Variable
    permanent: Permanent
    combinations: List[Combination]


class Loads(LoadsBase):
    """Loads implementation for the ``tr_0018_dch`` design class.

    This class extends ``LoadsBase`` by narrowing the attribute types.

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
    :class:`~bdim.baselib.loads.LoadsBase`
        Base class defining the core behaviour and configuration.
    """
    variable: Variable
    permanent: Permanent
    combinations: List[Combination]
    _data_path = Path(__file__).parent / 'data' / 'loads.json'
    _data_model: Type[LoadsData] = LoadsData
