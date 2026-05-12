"""This module provides the Building Nonlinear Structural Model (BNSM)
implementation for the ``CP03`` modelling configuration.
"""
# Imports from installed packages
import openseespy.opensees as ops
from pathlib import Path
from typing import List, Type, Optional, Literal, Dict

# Imports from bnsm ibrary
from .foundation import Foundation
from .joint import StairsJoint, FloorJoint
from .floor import FloorDiaphragm
from .beam import Beam
from .column import Column
from .infill import Infill

# Imports from bnsm base library
from ..baselib.building import BuildingBase, BuildingDesign
from ..baselib.beam import BeamDesign
from ..baselib.column import ColumnDesign
from ..baselib.constants import (
    RIGID_SEC, RIGID_MAT, BIG_VALUE,
    LINEAR_TRANSF_X, LINEAR_TRANSF_Y, LINEAR_TRANSF_Z,
    PDELTA_TRANSF_Z, VECXZ_X, VECXZ_Y, VECXZ_Z
)

# Imports from utils library
from ....utils.misc import make_dir
from ....utils import plotter as pl


class Building(BuildingBase):
    """BNSM implementation for the ``CP03`` model.

    This class aggregates CP03-specific structural components (e.g. beams,
    columns, joints, infills) and extends the base implementation in
    ``BuildingBase`` by introducing auxiliary plastic hinge nodes,
    rigid-like offset elements, and configurable series or parallel
    infill-column shear interaction.

    Attributes
    ----------
    foundations : List[~simdesign.rcmrf.bnsm.cp03.foundation.Foundation]
        List of foundation instances.
    floors : List[~simdesign.rcmrf.bnsm.cp03.floor.FloorDiaphragm]
        List of floor instances.
    floor_joints : List[~simdesign.rcmrf.bnsm.cp03.joint.FloorJoint]
        List of floor joints instances.
    stairs_joints : List[~simdesign.rcmrf.bnsm.cp03.joint.StairsJoint]
        List of stairs joints instances.
    beams : List[~simdesign.rcmrf.bnsm.cp03.beam.Beam]
        List of beam instances.
    columns : List[~simdesign.rcmrf.bnsm.cp03.column.Column]
        List of column instances.
    infills : List[~simdesign.rcmrf.bnsm.cp03.infill.Infill]
        List of infill instances.
    infill_column_connection : {'series', 'parallel'}
        Defines the modelling assumption governing the interaction between
        masonry infill struts and column lateral response.
        - 'series': the column lateral response acts in series with the
        horizontal component of the infill strut response. In this
        configuration, the effective lateral strength of the frame is
        governed solely by the column.
        - 'parallel': the infill strut acts in parallel with the column
        lateral response, allowing the direct contribution of the infills to
        the global lateral strength.

    See Also
    --------
    :class:`~BuildingBase`
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
    infill_column_connection: Literal['series', 'parallel']

    def __init__(
        self, design: BuildingDesign,
        load_factors: Dict[Literal['G', 'Q'], float] = {'G': 1.0, 'Q': 0.3},
        mass_factors: Dict[Literal['G', 'Q'], float] = {'G': 1.0, 'Q': 0.3},
        scheme: Literal['FMP', 'EQL', 'MPP', 'TRI', 'UNI'] = 'EQL',
        max_drift: float = 0.05, dincr: float = 0.001,
        include_infills: bool = True, cyclic_model: bool = False,
        cracked_beam: bool = False, cracked_column: bool = False,
        infill_column_connection: Literal['series', 'parallel'] = 'parallel'
    ) -> None:
        """Initialize BNSM object.

        Parameters
        ----------
        design : BuildingDesign
            Instance of building design information model (BDIM)
        load_factors : Dict[Literal['G', 'Q'], float], optional
            Load factors used to compute gravity loads & seismic masses. By
            default {'G': 1.0, 'Q': 0.3}.
            - 'G' : Permanent load factor
            - 'Q' : Variable load factor
        mass_sources : Dict[Literal['G', 'Q'], float], optional
            Mass sources used to compute seismic masses. By default
            {'G': 1.0, 'Q': 0.3}.
            - 'G' : Permanent mass factor
            - 'Q' : Variable mass factor
        scheme : Literal['FMP', 'EQL', 'MPP', 'TRI', 'UNI'], optional
            The loading scheme considered for retriving pushover loads. By
            default 'EQL'.
            - 'FMP : Fundamental-mode proportional loading.
            - 'EQL : Equivalent lateral loading.
            - 'MPP : Mass proportional loading.
            - 'TRI : Triangular or height propotional loading.
            - 'UNI : Uniform loading.
        max_drift : float, optional
            The drift value used to calculate maximum disp. of control node.
            By default 0.05.
        dincr: float
            First displacement increment considered during nspa.
            By default 0.001.
        include_infills : bool
            Flag to check whether include infills in the frame model or not.
        cyclic_model : bool, optional
            If True, the model parameters will be adjusted for cyclic analysis.
            By default False.
        cracked_beam: bool, optional
            If True, the elastic beam sections uses cracked-section
            (effective) flexural properties. If False, gross-section
            properties are used. By default False.
        cracked_column : bool, optional
            If True, the elastic column sections uses cracked-section
            (effective) flexural properties. If False, gross-section
            properties are used. By default False.
        infill_column_connection : {'series', 'parallel'}, optional
            Defines the modelling assumption governing the interaction between
            masonry infill struts and column lateral response. By default
            'parallel'.
            - 'series' : The column lateral response acts in series with the
            horizontal component of the infill strut response. In this
            configuration, the effective lateral strength of the frame is
            governed by the weaker of the column and infill lateral strengths.
            - 'parallel' : The infill strut acts in parallel with the column
            lateral response, allowing the direct contribution of the infills
            to the global lateral strength.
        """
        self.design = design
        self.load_factors = load_factors
        self.mass_sources = mass_factors
        self.scheme = scheme
        self.max_drift = max_drift
        self.dincr = dincr
        self.include_infills = include_infills
        self.cyclic_model = cyclic_model
        self.cracked_beam = cracked_beam
        self.cracked_column = cracked_column
        self.infill_column_connection = infill_column_connection
        self.foundations = []
        self.floors = []
        self.floor_joints = []
        self.stairs_joints = []
        self.beams = []
        self.columns = []
        self.infills = []
        self._set_basic_masses()
        self._initialize_floor_joints()
        self._initialize_stairs_joints()
        self._initialize_foundations()
        self._initialize_beams()
        self._initialize_columns()
        self._initialize_infills()

    def _initialize_beams(self) -> None:
        """Initialize beam models.
        """
        # Initialize the beam models
        bondslip_fact = self.design.quality.model.bondslip_factor
        self.beams = [
            self.BeamClass(beam, bondslip_fact, self.load_factors,
                           self.cyclic_model, self.cracked_beam)
            for beam in self.design.beams
            ]
        # Initialize beam nodes at floor levels
        for joint in self.floor_joints:
            if joint.design.left_beam:
                design = joint.design.left_beam
                node_j = joint.left_node
                beam = self._find_beam_by_design(design)
                if beam and node_j:
                    beam.hinge_node_j = node_j
                    beam.set_ele_node_j()
            if joint.design.right_beam:
                design = joint.design.right_beam
                node_i = joint.right_node
                beam = self._find_beam_by_design(design)
                if beam and node_i:
                    beam.hinge_node_i = node_i
                    beam.set_ele_node_i()
            if joint.design.rear_beam:
                design = joint.design.rear_beam
                node_j = joint.rear_node
                beam = self._find_beam_by_design(design)
                if beam and node_j:
                    beam.hinge_node_j = node_j
                    beam.set_ele_node_j()
            if joint.design.front_beam:
                design = joint.design.front_beam
                node_i = joint.front_node
                beam = self._find_beam_by_design(design)
                if beam and node_i:
                    beam.hinge_node_i = node_i
                    beam.set_ele_node_i()
        # Initialize beam nodes at mid-storeys (stairs beams)
        for joint in self.stairs_joints:
            if joint.design.left_beam:
                design = joint.design.left_beam
                node_j = joint.left_node
                beam = self._find_beam_by_design(design)
                if beam and node_j:
                    beam.hinge_node_j = node_j
                    beam.set_ele_node_j()
            if joint.design.right_beam:
                design = joint.design.right_beam
                node_i = joint.right_node
                beam = self._find_beam_by_design(design)
                if beam and node_i:
                    beam.hinge_node_i = node_i
                    beam.set_ele_node_i()

    def _initialize_columns(self) -> None:
        """Initialize column models.
        """
        # Set bondslip factor
        bondslip_fact = self.design.quality.model.bondslip_factor
        # Check if capacity design is followed for shear
        if self.design.OVERSTRENGTH_FACTOR_COLUMN_SHEAR:
            capacity_des = True
        else:
            capacity_des = False

        # Initialize columns
        self.columns = [
            self.ColumnClass(
                column, bondslip_fact, capacity_des, self.load_factors,
                self.cyclic_model, self.cracked_column
            )
            for column in self.design.columns
        ]
        # Initialize column nodes at stairs and floor joints
        for joint in self.floor_joints + self.stairs_joints:
            if joint.design.bottom_column:
                design = joint.design.bottom_column
                node_j = joint.bottom_node
                column = self._find_column_by_design(design)
                if column and node_j:
                    column.hinge_node_j = node_j
                    column.set_ele_node_j()
            if joint.design.top_column:
                design = joint.design.top_column
                node_i = joint.top_node
                column = self._find_column_by_design(design)
                if column and node_i:
                    column.hinge_node_i = node_i
                    column.set_ele_node_i()

        # Initialize column nodes at foundations
        for foundation in self.foundations:
            if foundation.design.top_column:
                design = foundation.design.top_column
                node_i = foundation.foundation_node
                column = self._find_column_by_design(design)
                if column and node_i:
                    column.hinge_node_i = node_i
                    column.set_ele_node_i()

    def _initialize_infills(self) -> None:
        """Initialize infill models.

        Notes
        -----
        The original ESRM20 implementation adopts an off-diagonal (single-
        strut) approach for masonry infills. In this approach, the column
        lateral response acts in *series* with the horizontal component of the
        infill strut response. Unlike the *parallel* case, this configuration
        eliminates the direct contribution of the infill to the global lateral
        strength of the frame. Consequently, the effective lateral strength is
        governed solely by the column.

        TODO
        ----
        For the single-strut approach, it remains to be evaluated whether
        off-diagonal nodes (series case) or central nodes (parallel case)
        provide the most appropriate strut definition.
        """
        for design in self.design.infills:  # go through each infill design
            if isinstance(design.columns[0], list):
                c1b = self._find_column_by_design(design.columns[0][0])
                c1t = self._find_column_by_design(design.columns[0][1])
                if self.infill_column_connection == 'series':
                    s1_ni = c1b.ele_node_i
                    s2_ni = c1t.ele_node_i
                elif self.infill_column_connection == 'parallel':
                    s1_ni = c1b.hinge_node_i
                    s2_ni = c1t.hinge_node_i
            else:
                c1 = self._find_column_by_design(design.columns[0])
                if self.infill_column_connection == 'series':
                    s1_ni = c1.ele_node_i
                    s2_ni = c1.ele_node_j
                elif self.infill_column_connection == 'parallel':
                    s1_ni = c1.hinge_node_i
                    s2_ni = c1.hinge_node_j
            if isinstance(design.columns[1], list):
                c2b = self._find_column_by_design(design.columns[1][0])
                c2t = self._find_column_by_design(design.columns[1][1])
                if self.infill_column_connection == 'series':
                    s1_nj = c2t.ele_node_j
                    s2_nj = c2b.ele_node_i
                elif self.infill_column_connection == 'parallel':
                    s1_nj = c2t.hinge_node_j
                    s2_nj = c2b.hinge_node_i
            else:
                c2 = self._find_column_by_design(design.columns[1])
                if self.infill_column_connection == 'series':
                    s1_nj = c2.ele_node_j
                    s2_nj = c2.ele_node_i
                elif self.infill_column_connection == 'parallel':
                    s1_nj = c2.hinge_node_j
                    s2_nj = c2.hinge_node_i
            strut1_nodes = [s1_ni, s1_nj]
            strut2_nodes = [s2_ni, s2_nj]
            infill = Infill(design, strut1_nodes, strut2_nodes)
            self.infills.append(infill)

    def _find_beam_by_design(self, design: BeamDesign) -> Optional[Beam]:
        """Finds the beam model by the given design.

        Parameters
        ----------
        design : ~simdesign.rcmrf.bnsm.cp03.beam.BeamDesign
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
        design : ~simdesign.rcmrf.bnsm.cp03.column.ColumnDesign
            Column design instance used for search.

        Returns
        -------
        Column | None
            Returns Column object if design attribute matches with
            given design, otherwise, returns None.
        """
        return super()._find_column_by_design(design)

    def _add_shared_ops_objects(self) -> None:
        """Add shared OpenSees objects to the domain.

        Defines materials, sections, and geometric transformations
        that can be referenced by multiple structural components.
        """
        ops.model('basic', '-ndm', 3, '-ndf', 6)
        # Geometric transformations
        ops.geomTransf('Linear', LINEAR_TRANSF_X, *VECXZ_X)
        ops.geomTransf('Linear', LINEAR_TRANSF_Y, *VECXZ_Y)
        ops.geomTransf('Linear', LINEAR_TRANSF_Z, *VECXZ_Z)
        ops.geomTransf('PDelta', PDELTA_TRANSF_Z, *VECXZ_Z)
        # Rigid-like material and section
        ops.uniaxialMaterial('Elastic', RIGID_MAT, BIG_VALUE)
        ops.section(
            'Aggregator', RIGID_SEC,
            RIGID_MAT, 'P', RIGID_MAT, 'Vy', RIGID_MAT, 'Vz',
            RIGID_MAT, 'My', RIGID_MAT, 'Mz', RIGID_MAT, 'T'
        )

    def _get_shared_opspy(self) -> List[str]:
        """Generate Python lines for shared OpenSees domain objects.

        Return
        ------
        List[str]
            List of lines that define reusable materials, sections, and
            geometric transformations that can be referenced by multiple
            structural components.
        """
        # Convert geometric transformation vectors to strings
        vecxz_x = ', '.join([str(v) for v in VECXZ_X])
        vecxz_y = ', '.join([str(v) for v in VECXZ_Y])
        vecxz_z = ', '.join([str(v) for v in VECXZ_Z])

        return [
            "# Geometric transformations",
            f"ops.geomTransf('Linear', {LINEAR_TRANSF_X}, {vecxz_x})",
            f"ops.geomTransf('Linear', {LINEAR_TRANSF_Y}, {vecxz_y})",
            f"ops.geomTransf('Linear', {LINEAR_TRANSF_Z}, {vecxz_z})",
            f"ops.geomTransf('PDelta', {PDELTA_TRANSF_Z}, {vecxz_z})",
            "",
            "# Rigid-like material and section",
            f"ops.uniaxialMaterial('Elastic', {RIGID_MAT}, {BIG_VALUE})",
            f"ops.section('Aggregator', {RIGID_SEC}, {RIGID_MAT}, 'P', "
            + f"{RIGID_MAT}, 'Vy',  {RIGID_MAT}, 'Vz', {RIGID_MAT}, 'My', "
            + f"{RIGID_MAT}, 'Mz', {RIGID_MAT}, 'T')",
        ]

    def _get_shared_opstcl(self) -> List[str]:
        """Generate Tcl lines for shared OpenSees domain objects.

        Return
        ------
        List[str]
            List of lines that define reusable materials, sections, and
            geometric transformations that can be referenced by multiple
            structural components.
        """
        # Convert geometric transformation vectors to strings
        vecxz_x = ' '.join([str(v) for v in VECXZ_X])
        vecxz_y = ' '.join([str(v) for v in VECXZ_Y])
        vecxz_z = ' '.join([str(v) for v in VECXZ_Z])

        return [
            "# Geometric transformations",
            f"geomTransf Linear {LINEAR_TRANSF_X} {vecxz_x}",
            f"geomTransf Linear {LINEAR_TRANSF_Y} {vecxz_y}",
            f"geomTransf Linear {LINEAR_TRANSF_Z} {vecxz_z}",
            f"geomTransf PDelta {PDELTA_TRANSF_Z} {vecxz_z}",
            "",
            "# Rigid-like material and section",
            f"uniaxialMaterial Elastic {RIGID_MAT} {BIG_VALUE}",
            f"section Aggregator {RIGID_SEC} {RIGID_MAT} P "
            + f"{RIGID_MAT} Vy {RIGID_MAT} Vz {RIGID_MAT} My "
            + f"{RIGID_MAT} Mz {RIGID_MAT} T",
        ]

    def plot_model(
        self, show_nodes: Literal['no', 'yes'] = 'yes', line_width: float = 3,
        directory: Optional[str | Path] = None, show: bool = True
    ) -> None:
        """
        Plots the structural model, showing nodes and elements grouped by type
        (rigid elements, beams, and columns).

        Parameters
        ----------
        show_nodes : Literal['no', 'yes'], optional
            A flag to control whether to display the nodes in the plot.
            'yes' to show the nodes, 'no' to hide them. By default 'yes'.
        line_width : float, optional
            Specifies the line width used to draw the elements in the plot.
            By default 3.
        directory : str | Path | None, optional
            Directory to save an image of the model. If None, the image will
            not be saved. By default None.
        show : bool, optional
                Flag for showing the figure in an interactive window,
                by default True.
        """
        # Set the group elements
        rigid = []
        for joint in self.floor_joints:
            rigid.extend(joint.rigid_ele)
        for joint in self.stairs_joints:
            rigid.extend(joint.rigid_ele)
        beams = [beam.design.line.tag for beam in self.beams]
        columns = [column.design.line.tag for column in self.columns]
        infills = []
        if self.include_infills:
            for infill in self.infills:
                s1 = int(str(infill.design.rectangle.tag) + '001')
                s2 = int(str(infill.design.rectangle.tag) + '002')
                infills.append(s1)
                infills.append(s2)
        groups = [
            [rigid, beams, columns, infills],
            ["black", "red", "blue", "green"]
        ]
        # Build the model
        self.build()
        # Path to the file (without the file extension)
        if directory:
            filename = str(Path(directory) / 'model_view.html')
            if not Path.exists(Path(directory)):
                make_dir(directory)
        else:
            filename = None
        # Plot the model
        pl.plot_model(show_nodes=show_nodes, ele_groups=groups, show=show,
                      line_width=line_width, filename=filename)
