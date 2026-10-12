"""This module provides the joint class implementations for the ``DP05``
model in the BNSM layer.
"""
# Imports from bnsm library
from ..dp03.joint import (
    StairsJoint as StairsJointDP03, FloorJoint as FloorJointDP03)


class StairsJoint(StairsJointDP03):
    """Stairs joint implementation for the ``DP05`` model, identical to
    ``DP03``.

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.dp03.joint.StairsJoint`
        Class reused by this model.
    """


class FloorJoint(FloorJointDP03):
    """Floor joint implementation for the ``DP05`` model, identical to
    ``DP03``.

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.dp03.joint.FloorJoint`
        Class reused by this model.
    """
