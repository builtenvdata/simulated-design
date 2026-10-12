"""This module provides the beam class implementation for the ``DP04`` model in
the BNSM layer.
"""
# Imports from installed packages
from typing import Literal

# Imports from bnsm dp01 library
from ..dp01.beam import Beam as BeamDP01


class Beam(BeamDP01):
    """Beam implementation for the ``DP04`` model.

    This class directly uses the behaviour defined in ``BeamDP01``, with
    the yield moment and curvature of the plastic hinges, and hence the
    cracked-section properties, from the simplified section analysis by
    default (``yield_mom_curv='analytical'``).

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.dp01.beam.Beam`
        DP01 beam model definition extended by this class.
    """

    def __init__(
        self, *args,
        yield_mom_curv: Literal['empirical', 'analytical'] = 'analytical',
        **kwargs
    ) -> None:
        """Initialize the Beam object (see ``BeamDP01``), with the yield moment
        and curvature of the plastic hinges from section analysis by default.
        """
        super().__init__(*args, yield_mom_curv=yield_mom_curv, **kwargs)
