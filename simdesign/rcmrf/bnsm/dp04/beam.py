"""This module provides the beam class implementation for the ``DP04`` model in
the BNSM layer.
"""
# Imports from bnsm base library
from ..baselib.beam import BeamBase


class Beam(BeamBase):
    """Beam implementation for the ``DP04`` model.

    This class directly uses the behaviour defined in ``BeamBase``.

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.baselib.beam.BeamBase`
        Base class defining the core behaviour and configuration.
    """
