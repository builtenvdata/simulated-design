"""This module provides the joint class implementations for the ``CP01`` model
in the BNSM layer.
"""
# Imports from bnsm base library
from ..baselib.joint import StairsJointBase, FloorJointBase


class StairsJoint(StairsJointBase):
    """Stairs joint implementation for the ``CP01`` model

    Represents a beam-column joint located at an intermediate (mid-storey)
    level associated with staircase framing.

    This class directly uses the behaviour defined in ``StairsJointBase``.

    See Also
    --------
    :class:`~StairsJointBase`
        Base class defining the core behaviour and configuration.
    """


class FloorJoint(FloorJointBase):
    """Floor joint implementation for the ``CP01`` model.

    Represents a beam-column joint located at a floor level.

    This class directly uses the behaviour defined in ``FloorJointBase``.

    See Also
    --------
    :class:`~FloorJointBase`
        Base class defining the core behaviour and configuration.
    """
