"""This module provides the joint class implementation representing
beam-column joints for the ``tr_post18_dch`` design class in the BDIM layer.
"""
# Imports from installed packages
from typing import Optional

# Imports from bdim base library
from ..baselib.joint import JointBase

# Imports from the design class (tr_post18_dch) library
from .beam import Beam
from .column import Column
from .materials import Steel, Concrete


class Joint(JointBase):
    """Joint implementation for design class ``tr_post18_dch``.

    This class extends ``JointBase`` by narrowing the attribute types.

    Attributes
    ----------
    left_beam : ~simdesign.rcmrf.bdim.tr_post18_dch.beam.Beam, optional
        Beam located on the left side of the joint (along global X-axis).
    right_beam : ~simdesign.rcmrf.bdim.tr_post18_dch.beam.Beam, optional
        Beam located on the right side of the joint (along global X-axis).
    front_beam : ~simdesign.rcmrf.bdim.tr_post18_dch.beam.Beam, optional
        Beam located in front of the joint (along global Y-axis).
    rear_beam : ~simdesign.rcmrf.bdim.tr_post18_dch.beam.Beam, optional
        Beam located behind the joint (along global Y-axis).
    top_column : ~simdesign.rcmrf.bdim.tr_post18_dch.column.Column, optional
        Column located on top of the joint (along global Z-axis).
    bottom_column : ~simdesign.rcmrf.bdim.tr_post18_dch.column.Column, optional
        Column located below the joint (along global Z-axis).
    steel : ~simdesign.rcmrf.bdim.tr_post18_dch.materials.Steel
        Steel material assigned to the joint.
    concrete : ~simdesign.rcmrf.bdim.tr_post18_dch.materials.Concrete
        Concrete material assigned to the joint.

    See Also
    --------
    :class:`~simdesign.rcmrf.bdim.baselib.joint.JointBase`
        Base class defining the core behaviour and configuration.
    """
    left_beam: Optional[Beam]
    right_beam: Optional[Beam]
    front_beam: Optional[Beam]
    rear_beam: Optional[Beam]
    top_column: Optional[Column]
    bottom_column: Optional[Column]
    steel: Steel
    concrete: Concrete
