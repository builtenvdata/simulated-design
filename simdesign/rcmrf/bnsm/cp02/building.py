"""This module provides the Building Nonlinear Structural Model (BNSM)
implementation for the ``CP02`` modelling configuration.
"""
# Imports from installed packages
from typing import List, Type

# Imports from bnsm ibrary
from .foundation import Foundation
from .joint import StairsJoint, FloorJoint
from .floor import FloorDiaphragm
from .beam import Beam
from .column import Column
from .infill import Infill

# Imports from bnsm base library
from ..baselib.building import BuildingBase


class Building(BuildingBase):
    """BNSM implementation for the ``CP02`` model.

    This class aggregates CP02-specific structural components (e.g. beams,
    columns, joints, infills) and relies on the behaviour defined in
    ``BuildingBase`` without modification.

    Attributes
    ----------
    foundations : List[~simdesign.rcmrf.bnsm.cp02.foundation.Foundation]
        List of foundation instances.
    floors : List[~simdesign.rcmrf.bnsm.cp02.floor.FloorDiaphragm]
        List of floor instances.
    floor_joints : List[~simdesign.rcmrf.bnsm.cp02.joint.FloorJoint]
        List of floor joints instances.
    stairs_joints : List[~simdesign.rcmrf.bnsm.cp02.joint.StairsJoint]
        List of stairs joints instances.
    beams : List[~simdesign.rcmrf.bnsm.cp02.beam.Beam]
        List of beam instances.
    columns : List[~simdesign.rcmrf.bnsm.cp02.column.Column]
        List of column instances.
    infills : List[~simdesign.rcmrf.bnsm.cp02.infill.Infill]
        List of infill instances.

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.baselib.building.BuildingBase`
        Base class defining the core behaviour and configuration.
    """
    foundations: List[Foundation]
    floors: List[FloorDiaphragm]
    floor_joints: List[FloorJoint]
    stairs_joints: List[StairsJoint]
    beams: List[Beam]
    columns: List[Column]
    infills: List[Infill]
    FoundationClass: Type[Foundation] = Foundation
    FloorDiaphragmClass: Type[FloorDiaphragm] = FloorDiaphragm
    FloorJointClass: Type[FloorJoint] = FloorJoint
    StairsJointClass: Type[StairsJoint] = StairsJoint
    BeamClass: Type[Beam] = Beam
    ColumnClass: Type[Column] = Column
    InfillClass: Type[Infill] = Infill
