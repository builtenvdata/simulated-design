"""This module provides the class implementations representing loads for the
``eu_cdl`` design class in the BDIM layer.
"""
# Imports from installed packages
import numpy as np
from pathlib import Path
from typing import Tuple, List, Type

# Imports from bdim base library
from ..baselib.loads import VariableBase, PermanentBase
from ..baselib.loads import CombinationBase, LoadsDataBase, LoadsBase


class Variable(VariableBase):
    """Variable load (Q) model implementation for the ``eu_cdl`` design class.

    This class directly uses the behaviour defined in ``VariableBase``.

    See Also
    --------
    :class:`~bdim.baselib.loads.VariableBase`
        Base class defining the core behaviour and configuration.
    """


class Permanent(PermanentBase):
    """Permanent load (G) model implementation for the ``eu_cdl`` design class.

    This class directly uses the behaviour defined in ``PermanentBase``.

    See Also
    --------
    :class:`~bdim.baselib.loads.PermanentBase`
        Base class defining the core behaviour and configuration.
    """


class Combination(CombinationBase):
    """Load combination model implementation for the ``eu_cdl`` design class.

    This class directly uses the behaviour defined in ``CombinationBase``.

    See Also
    --------
    :class:`~bdim.baselib.loads.CombinationBase`
        Base class defining the core behaviour and configuration.
    """


class LoadsData(LoadsDataBase):
    """Loads data model implementation for the ``eu_cdl`` design class.

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
    """Loads implementation for the ``eu_cdl`` design class.

    This class extends ``LoadsBase`` by narrowing the attribute types and
    overriding :meth:`get_seismic_loads` to use uniform weight distribution.

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

    def get_seismic_loads(self, **kwargs: float | np.ndarray
                          ) -> Tuple[np.float64, np.ndarray]:
        """Calculate and return seismic loads.

        Unlike :meth:`~bdim.baselib.loads.LoadsBase.get_seismic_loads`,
        this implementation distributes forces proportionally to storey
        weight alone, without height weighting. The ``heights`` parameter
        is therefore not required and should not be passed.

        Parameters
        ----------
        **kwargs : dict[float | np.ndarray]
            Keyword arguments consumed by this method:

            beta : float
                Design lateral load factor expressed as a fraction of
                building weight.
            weights : np.ndarray
                Array of storey weights in kN.

        Returns
        -------
        Tuple[np.float64, np.ndarray]
            Total base shear force (kN) and seismic forces acting at
            each storey (kN), distributed proportionally to storey
            weight. The forces array has the same shape as ``weights``.

        Notes
        -----
        ``**kwargs`` are used instead of explicit keyword arguments in
        order to satisfy the interface expected by
        :meth:`~analysis.ElasticModel.run_seismic_load_cases`.
        """
        beta = kwargs['beta']
        weights = kwargs['weights']
        base_shear = np.sum(beta * weights)
        forces = base_shear * (weights) / np.sum(weights)

        return base_shear, forces
