"""This module provides the Building Nonlinear Structural Model (BNSM)
implementation for the ``DP05`` modelling configuration.
"""
# Imports from installed packages
from typing import List, Type, Optional

# Imports from bnsm library
from .foundation import Foundation
from .joint import StairsJoint, FloorJoint
from .floor import FloorDiaphragm
from .beam import Beam
from .column import Column
from .infill import Infill

# Imports from bnsm base library
from ..baselib.building import BuildingBase
from ..baselib.beam import BeamDesign
from ..baselib.column import ColumnDesign


class Building(BuildingBase):
    """BNSM implementation for the ``DP05`` model.

    This class aggregates the DP05 components, i.e., the DP03 components with
    an axial release at the *j-end* of each beam (see
    :class:`~simdesign.rcmrf.bnsm.dp05.beam.Beam`).

    Attributes
    ----------
    foundations : List[~simdesign.rcmrf.bnsm.dp05.foundation.Foundation]
        List of foundation instances.
    floors : List[~simdesign.rcmrf.bnsm.dp05.floor.FloorDiaphragm]
        List of floor instances.
    floor_joints : List[~simdesign.rcmrf.bnsm.dp05.joint.FloorJoint]
        List of floor joints instances.
    stairs_joints : List[~simdesign.rcmrf.bnsm.dp05.joint.StairsJoint]
        List of stairs joints instances.
    beams : List[~simdesign.rcmrf.bnsm.dp05.beam.Beam]
        List of beam instances.
    columns : List[~simdesign.rcmrf.bnsm.dp05.column.Column]
        List of column instances.
    infills : List[~simdesign.rcmrf.bnsm.dp05.infill.Infill]
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

    def _initialize_beams(self) -> None:
        """Initialize beam models, with the axial release at the *j-end* of
        each beam.
        """
        super()._initialize_beams()
        for beam in self.beams:
            beam.set_axial_release()

    def _find_beam_by_design(self, design: BeamDesign) -> Optional[Beam]:
        """Finds the beam model by the given design.

        Parameters
        ----------
        design : ~simdesign.rcmrf.bnsm.dp05.beam.BeamDesign
            Beam design instance used for search.

        Returns
        -------
        Beam | None
            Returns Beam object if design attribute matches with
            given design, otherwise, returns None.
        """
        return super()._find_beam_by_design(design)

    def _find_column_by_design(self, design: ColumnDesign) -> Optional[Column]:
        """Finds the column model by the given design.

        Parameters
        ----------
        design : ~simdesign.rcmrf.bnsm.dp05.column.ColumnDesign
            Column design instance used for search.

        Returns
        -------
        Column | None
            Returns Column object if design attribute matches with
            given design, otherwise, returns None.
        """
        return super()._find_column_by_design(design)
