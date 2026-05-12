"""BNSM factory module.

This module provides a factory interface for creating Building Nonlinear
Structural Model (BNSM) instances corresponding to predefined modelling
configurations.

The :class:`~BNSM` class dynamically maps a string-based model identifier
(e.g., "CP01", "DP03") to its corresponding implementation class and
returns an initialized instance.

All model implementations inherit from ``BuildingBase`` and define
specific modelling strategies.
"""

from .baselib import BuildingBase
from .cp01 import CP01
from .cp02 import CP02
from .cp03 import CP03
from .dp01 import DP01
from .dp02 import DP02
from .dp03 import DP03
from .dp04 import DP04
from ...utils.misc import filter_args


MODELLERS = {
    "CP01": CP01,
    "CP02": CP02,
    "CP03": CP03,
    "DP01": DP01,
    "DP02": DP02,
    "DP03": DP03,
    "DP04": DP04
}
"""Registry of available BNSM implementations or numerical model constructors.
"""


class BNSM:
    """
    Factory class to dynamically create a BNSM instance of the corresponding
    selected model.

    The model type is selected using the ``model`` keyword argument
    (e.g., ``model="CP03"``). The returned object is an instance of the
    corresponding implementation class inheriting from :class:`BuildingBase`.

    See Also
    --------
    :class:`CP01`
        Concentrated plasticity model variant 01.
    :class:`CP02`
        Concentrated plasticity model variant 02.
    :class:`CP03`
        Concentrated plasticity model variant 03.
    :class:`DP01`
        Distributed plasticity model variant 01.
    :class:`DP02`
        Distributed plasticity model variant 02.
    :class:`DP03`
        Distributed plasticity model variant 03.
    :class:`DP04`
        Distributed plasticity model variant 04.
    """

    def __new__(cls, **kwargs) -> BuildingBase:
        """
        Dynamically creates a BNSM instance based on the model type.

        Parameters
        ----------
        model : str | None, optional
            Identifier of the BNSM implementation to instantiate.
            If not provided, defaults to ``'CP03'``.
        **kwargs
            Keyword arguments forwarded to the constructor (``__init__``) of
            the selected model implementation. Therefore, the valid set of
            keyword arguments depends on the chosen ``model``
            (e.g., for ``model='CP03'``, ``**kwargs`` must match :class:`CP03`
            constructor parameters).

        Returns
        -------
        BuildingBase
            A bnsm instance of the corresponding model type.

        Raises
        ------
        ValueError
            If the keyword argument 'model' is invalid.

        See Also
        --------
        :class:`~CP01`, :class:`~CP02`, :class:`~CP03`,
        :class:`~DP01`, :class:`~DP02`, :class:`~DP03`, :class:`~DP04`

            BNSM implementations whose constructor parameters define the
            accepted ``**kwargs`` for the corresponding ``model`` value.
        """
        model = kwargs.get('model') or 'CP03'
        # Check if the model in kwargs is valid
        if model not in MODELLERS.keys():
            valid_options = ", ".join(MODELLERS.keys())
            raise ValueError(
                f"Invalid modelling option: {model}. "
                f"Valid modelling options are: {valid_options}."
            )

        # Get appropriate bnsm class
        bnsm = MODELLERS.get(model)
        # Instantiate and return the appropriate class
        filtered_args = filter_args(bnsm.__init__, kwargs)
        return bnsm(**filtered_args)
