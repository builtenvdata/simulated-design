"""This module provides the Building Nonlinear Structural Model (BNSM)
implementation for the ``CP02`` modelling configuration.
"""
# Imports from installed packages
from typing import List, Type, Optional
from pathlib import Path
import json

# Imports from bnsm ibrary
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

# Imports from utils library
from ....utils.units import MPa


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

    def _find_beam_by_design(self, design: BeamDesign) -> Optional[Beam]:
        """Finds the beam model by the given design.

        Parameters
        ----------
        design : ~simdesign.rcmrf.bnsm.cp02.beam.BeamDesign
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
        design : ~simdesign.rcmrf.bnsm.cp02.column.ColumnDesign
            Column design instance used for search.

        Returns
        -------
        Column | None
            Returns Column object if design attribute matches with
            given design, otherwise, returns None.
        """
        return super()._find_column_by_design(design)

    def export_hinges(self, directory: Optional[str | Path] = None) -> None:
        """Export plastic-hinge capacity data for beams and columns to JSON.

        For every floor joint and foundation joint in the model, this method
        computes the hysteretic energy capacity (Eh_cap) and ultimate
        chord rotation (theta_ult) of the plastic hinges framing into
        that joint, then writes the collected data to "info_hinges.json"
        in the target directory.

        The hysteretic energy capacity is computed as::

            Eh_cap = My * (theta_ult - theta_y) * lambda

        where "lambda" is an empirical definition that depends on concrete
        strength (fc), longitudinal-steel yield strength (fsyl), normalised
        axial load (niu), and the transverse-reinforcement spacing ratio
        (s_h = s / h).

            lambda = 52 * 0.41^(0.01*(fc + 0.1*fsyl)) * 0.34^niu * 0.21^(s/h)

        Notes
        -----
        - Beam ends are tagged "I" for the start end (right/front beam)
          and "J" for the end (left/rear beam), following the
          convention in "BEAM_END_MAP".
        - Column ends are tagged "I" for the top column and "J"
          for the bottom column.
        - For beams, "niu" is assumed to be 0 (axial load neglected).
        """

        # ------------------------------------------------------------------
        # Output directory setup
        # ------------------------------------------------------------------
        directory = Path(directory) if directory is not None else Path.cwd()
        directory.mkdir(parents=True, exist_ok=True)

        # Maps the joint's beam attribute name to the corresponding hinge
        # end label. "I" = start end, "J" = end end. right/front beams
        # frame into the joint at their I-end; left/rear beams at their
        # J-end.
        BEAM_END_MAP = {"right_beam": "I", "left_beam": "J",
                        "front_beam": "I", "rear_beam": "J"}

        # Top-level container:
        #    {storey: {joint_id: {"beams": ..., "columns": ...}}}
        info_hinges = {}

        # Iterate over every joint where hinges may form: floor joints
        # above ground level and foundation joints at the base.
        for joint in self.floor_joints + self.foundations:
            # Storey index is the third grid coordinate of the elastic node
            storey = int(joint.design.elastic_node.grid_ids[2])

            # Ensure the storey bucket exists before we write into it
            info_hinges.setdefault(storey, {})

            # Foundation joints carry a "foundation_node", floor joints a
            # "floor_node". Use whichever is present as the joint identifier.
            joint_id = (joint.foundation_node.tag if hasattr(
                joint, "foundation_node") else joint.floor_node.tag)

            # Initialise the dictionary for the joint
            info_hinges[storey][joint_id] = {"beams": {}, "columns": {}}

            # --------------------------------------------------------------
            # Beams framing into this joint
            # --------------------------------------------------------------
            for beam_attr, beam_end in BEAM_END_MAP.items():
                # Each joint may have up to four incident beams (one per
                # cardinal direction).
                beam_design = getattr(joint.design, beam_attr)
                if beam_design:
                    beam = self._find_beam_by_design(beam_design)
                else:
                    continue

                # Pull the backbone moment-rotation inputs for the relevant
                # end of the beam, plus the normalised stirrup spacing s/h
                # at that same end.
                #   _get_mz_mat_inputs() -> (inputs_at_I, inputs_at_J)
                #   sbh_q[0]  -> stirrup spacing at I-end
                #   sbh_q[-1] -> stirrup spacing at J-end
                if beam_end == "I":
                    mat_inputs, _ = beam._get_mz_mat_inputs()
                    s_h = beam.design.sbh_q[0] / beam.design.h
                elif beam_end == "J":
                    _, mat_inputs = beam._get_mz_mat_inputs()
                    s_h = beam.design.sbh_q[-1] / beam.design.h

                # Backbone parameters: yield moment, yield rotation,
                # ultimate rotation, and derived plastic rotation.
                My = mat_inputs[2]
                theta_y = mat_inputs[3]
                theta_ult = mat_inputs[7]
                theta_pl_total = theta_ult - theta_y

                # Convert material strengths from model units (Pa) to MPa
                # for use in the empirical lambda formula.
                fc_mpa = beam.design.fc_q / MPa
                fsyl_mpa = beam.design.fsyl_q / MPa

                # Axial load on beams is neglected: niu = 0.
                niu = 0.0

                # Empirical hysteretic energy capacity factor.
                lamda = (52 *
                         (0.41 ** (0.01 * (fc_mpa + 0.1 * fsyl_mpa))) *
                         (0.34 ** niu) * (0.21 ** s_h))

                # Hysteretic energy capacity of the beam hinge
                Eh_cap = round(My * theta_pl_total * lamda, 1)

                # Record this beam hinge under its element tag
                info_hinges[storey][joint_id]["beams"][beam.ele_tag] = {
                    "beam_end": beam_end,
                    "Eh_cap": Eh_cap,
                    "theta_ult": round(theta_ult, 4)}

            # --------------------------------------------------------------
            # Columns framing into this joint
            # --------------------------------------------------------------
            for col_attr in ["top_column", "bottom_column"]:
                # A joint may have a column above it, below it, or both.
                col_design = getattr(joint.design, col_attr)
                if col_design:
                    column = self._find_column_by_design(col_design)
                else:
                    continue

                # Material strengths in MPa for the lambda formula
                fc_mpa = column.design.fc_q / MPa
                fsyl_mpa = column.design.fsyl_q / MPa

                # Normalised axial load ratio
                N = max(-column.axial_force, 0)
                niu = N / (column.design.Ag * column.design.fc_q)

                # Stirrup spacing ratio depends on bending axis:
                s_h_x = column.design.sbh_q / column.design.by
                s_h_y = column.design.sbh_q / column.design.bx

                # Calculate hysteretic energy capacity of section
                # around x (Eh_cap_x)
                mat_inputs_x = column._get_rot_hinge_mat_inputs("x")
                My_x = mat_inputs_x[2]
                theta_y_x = mat_inputs_x[3]
                theta_ult_x = mat_inputs_x[7]
                theta_pl_total_x = theta_ult_x - theta_y_x
                lamda_x = (52 *
                           (0.41 ** (0.01 * (fc_mpa + 0.1 * fsyl_mpa))) *
                           (0.34 ** niu) * (0.21 ** s_h_x))
                Eh_cap_x = round(My_x * theta_pl_total_x * lamda_x, 1)

                # Calculate hysteretic energy capacity of section
                # around y (Eh_cap_y)
                mat_inputs_y = column._get_rot_hinge_mat_inputs("y")
                My_y = mat_inputs_y[2]
                theta_y_y = mat_inputs_y[3]
                theta_ult_y = mat_inputs_y[7]
                theta_pl_total_y = theta_ult_y - theta_y_y
                lamda_y = (52 *
                           (0.41 ** (0.01 * (fc_mpa + 0.1 * fsyl_mpa))) *
                           (0.34 ** niu) * (0.21 ** s_h_y))
                Eh_cap_y = round(My_y * theta_pl_total_y * lamda_y, 1)

                # Column end label: top column's hinge is the "I" end,
                # bottom column's hinge is the "J" end.
                if col_attr == "top_column":
                    column_end = "I"
                elif col_attr == "bottom_column":
                    column_end = "J"

                # Record this column hinge under its element tag
                info_hinges[storey][joint_id]["columns"][column.ele_tag] = {
                    "column_end": column_end,
                    "Eh_cap_x": Eh_cap_x,
                    "Eh_cap_y": Eh_cap_y,
                    "theta_ult_x": round(theta_ult_x, 4),
                    "theta_ult_y": round(theta_ult_y, 4)}

        # ------------------------------------------------------------------
        # Write the json file
        # ------------------------------------------------------------------
        with open(directory / "info_hinges.json", "w") as f:
            json.dump(info_hinges, f, indent=2)
