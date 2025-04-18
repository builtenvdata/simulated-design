# Imports from installed packages
from abc import ABC
from typing import List, Literal, Tuple
import openseespy.opensees as ops
import numpy as np
from itertools import product

# Imports from bdim base library
from .beam import BeamBase, BeamForces
from .column import ColumnBase, ColumnForces
from .loads import LoadsBase

# Imports from geometry library
from ...geometry.base import FrameBase

# Imports from utils library
from ....utils.misc import PRECISION
from ....utils.units import grav_acc


class ElasticModelBase(ABC):
    """Abstract base class for elastic model builder in OpenSees.
    """
    beams: List[BeamBase]
    """Beam objects of the building."""
    columns: List[ColumnBase]
    """Column objects of the building."""
    geometry: FrameBase
    """Loads instance for the current design class."""
    loads: LoadsBase
    """General building geometry (elastic frame geometry)."""
    beta: float
    """Design lateral load factor (in g)."""

    def __init__(
        self, beams: List[BeamBase], columns: List[ColumnBase],
        loads: LoadsBase, geometry: FrameBase, beta: float
    ) -> None:
        """Initialize elastic model object.

        Parameters
        ----------
        beams : List[BeamBase]
            Beam objects of the building.
        columns : List[ColumnBase]
            Column objects of the building.
        loads : LoadsBase
            Loads instance for the current design class.
        geometry : FrameBase
            General building geometry (elastic frame geometry).
        beta : float
            Design lateral load factor (in g).
        """
        self.beams = beams
        self.columns = columns
        self.geometry = geometry
        self.loads = loads
        self.beta = beta

    def _get_mass_factors(self) -> List[Tuple[float, float]]:
        """Get unique mass factors in combinations for each seismic load case.

        Returns
        -------
        List[Tuple[float, float]]
            Unique mass factors in combinations for gravity loads (G, Q).
        """
        seismic_combos = self.loads.get_seismic_load_combos()
        all_factors = []
        for combo in seismic_combos:
            factors = [0.0, 0.0]
            if 'G' in combo.masses:
                factors[0] = combo.masses['G']
            if 'Q' in combo.masses:
                factors[1] = combo.masses['Q']
            all_factors.append(tuple(factors))

        # Unique tuples in 'Factors'
        all_factors = list(set(all_factors))
        return all_factors

    def _get_nodal_masses(self) -> Tuple[List[float], List[float]]:
        """Compute nodal masses based on loads.

        Returns
        -------
        Tuple[List[float], List[float]]
            Nodal masses from permanent loads and from live loads.

        Note
        ----
        Alternative is to compute the masses from element forces
        or nodal reaction forces. Previous version uses this approach.
        """
        node_tags = self.geometry.point_tags
        masses_g = [0] * len(node_tags)
        masses_q = [0] * len(node_tags)
        # Beams
        for beam in self.beams:
            node_i, node_j = [p.tag for p in beam.line.points]
            i = node_tags.index(node_i)
            j = node_tags.index(node_j)
            mg = (beam.line.length * beam.wg_total) / 2 / grav_acc
            mq = (beam.line.length * beam.wq_total) / 2 / grav_acc
            masses_g[i] += mg
            masses_g[j] += mg
            masses_q[i] += mq
            masses_q[j] += mq
        # Columns
        for column in self.columns:
            node_i, node_j = [p.tag for p in column.line.points]
            i = node_tags.index(node_i)
            j = node_tags.index(node_j)
            mg = (column.line.length * column.self_wg) / 2 / grav_acc
            masses_g[i] += mg
            masses_g[j] += mg
        # Return masses
        return masses_g, masses_q

    def _get_nodal_heights(self) -> List[float]:
        """Computes nodal heights.

        Returns
        -------
        List[float]
            Heights of structural nodes measured from the ground level.
        """
        z0 = min(self.geometry.system_grid_data.z.ordinates)
        heights = []
        for point in self.geometry.points:
            z = point.coordinates[2]
            h = round(z - z0, PRECISION)
            heights.append(h)

        return heights

    def _init_ops_model(self) -> None:
        """Start a clean opensees model.
        """
        ops.wipe()
        ops.wipeAnalysis()
        ops.model('basic', '-ndm', 3, '-ndf', 6)

    def _add_ops_nodes(self) -> None:
        """Defines structural nodes.
        """
        # Nodes connecting beam-column elements
        for node in self.geometry.points:
            ops.node(node.tag, *node.coordinates)

    def _add_ops_beam_column_elements(self, cracked_section: bool = False
                                      ) -> None:
        """Create beam-column elements in the numerical model.

        Parameters
        ----------
        cracked_section : bool, optional
            Flag for using cracked section properties, by default False.

        References
        ----------
        https://openseespydoc.readthedocs.io/en/latest/src/LinearTransf.html
        https://openseespydoc.readthedocs.io/en/latest/src/elasticSection.html
        https://openseespydoc.readthedocs.io/en/latest/src/beamIntegration.html
        https://openseespydoc.readthedocs.io/en/latest/src/ForceBeamColumn.html

        Notes
        -----
        Outside the analysis routine, for design purposes local axes are named
        as x and y. On the other hand, herein, OpenSees always labels the axis
        as z and y.
        Thus, x-axis is called as z axis in OpenSees
        y
        |__x
            --------------    ----
            |     y      |    |
            |     |      |    |
            |     +--z   |    by
            |            |    |
            |            |    |
            --------------    ----
            |---- bx ----|
        """
        # COLUMNS
        TRANSF_TAG = 1  # Geometric transformation tag
        VECXZ = [-1, 0, 0]  # X, Y, and Z components of vecxz
        FACTY = 5 / 6  # shear shape factor along local Y
        FACTZ = 5 / 6  # shear shape factor along local Z
        NUM_INT_PTS = 9  # number of integration points along the element
        # Define geometric transformation
        ops.geomTransf('Linear', TRANSF_TAG, *VECXZ)
        # Loop through columns
        for column in self.columns:
            ele = column.line.tag  # element tag
            sec = column.line.tag  # section tag
            int_tag = column.line.tag  # integration tag
            nodes = [p.tag for p in column.line.points]  # node tags (i, j)
            Ec = column.Ecm  # youngs' modulus
            Gc = column.Gcm  # shear modulus
            Ag = column.Ag  # gross section area
            Jxx = column.J  # torsional moment of inertia
            if cracked_section:  # using cracked section properties
                Iz = column.Ix_eff  # moment of inertia about the local z-axis
                Iy = column.Iy_eff  # moment of inertia about the local y-axis
            else:  # using gross section properties
                Iz = column.Ix  # moment of inertia about the local z-axis
                Iy = column.Iy  # moment of inertia about the local y-axis
            # Create elastic section
            ops.section('Elastic', sec, Ec, Ag, Iz, Iy, Gc, Jxx, FACTY, FACTZ)
            # Create beam integration object
            ops.beamIntegration('Lobatto', int_tag, sec, NUM_INT_PTS)
            # Create column element
            ops.element('forceBeamColumn', ele, *nodes, TRANSF_TAG, int_tag)

        # BEAMS
        TRANSF_TAG_X = 2  # Geometric transformation tag for beams along X
        VECXZ_X = [0, -1, 0]  # X, Y, and Z components of vecxz for beams in X
        TRANSF_TAG_Y = 3  # Geometric transformation tag for beams along Y
        VECXZ_Y = [1, 0, 0]  # X, Y, and Z components of vecxz for beams in Y
        FACTY = 5 / 6  # shear shape factor along local Y
        FACTZ = 5 / 6  # shear shape factor along local Z
        NUM_INT_PTS = 9  # number of integration points along the element
        # Define geometric transformations
        ops.geomTransf('Linear', TRANSF_TAG_X, *VECXZ_X)
        ops.geomTransf('Linear', TRANSF_TAG_Y, *VECXZ_Y)
        # Loop through beams
        for beam in self.beams:
            ele = beam.line.tag  # element tag
            sec = beam.line.tag  # section tag
            int_tag = beam.line.tag  # integration tag
            nodes = [p.tag for p in beam.line.points]  # node tags (i, j)
            Ec = beam.Ecm  # youngs' modulus
            Gc = beam.Gcm  # shear modulus
            Ag = beam.Ag  # gross section area
            Jxx = beam.J  # torsional moment of inertia
            if cracked_section:  # using cracked section properties
                Iz = beam.Ix_eff  # moment of inertia about the local z-axis
                Iy = beam.Iy_eff  # moment of inertia about the local y-axis
            else:  # using gross section properties
                Iz = beam.Ix  # moment of inertia about the local z-axis
                Iy = beam.Iy  # moment of inertia about the local y-axis
            # Transformation for beams along global X
            if beam.direction == 'x':
                transf_tag = TRANSF_TAG_X
            # Transformation for beams along global Y
            elif beam.direction == 'y':
                transf_tag = TRANSF_TAG_Y
            else:
                raise ValueError("Something is wrong")
            # Create elastic section
            ops.section('Elastic', sec, Ec, Ag, Iz, Iy, Gc, Jxx, FACTY, FACTZ)
            # Create beam integration object
            ops.beamIntegration('Lobatto', int_tag, sec, NUM_INT_PTS)
            # Create beam element
            ops.element('forceBeamColumn', ele, *nodes, transf_tag, int_tag)

    def _add_ops_sp_constraints(self) -> None:
        """Define single-point (SP) constraints.

        Ground nodes are restrained in all DOFs.
        """
        # Restraints for ground level nodes
        for node in self.geometry.ground_level_points:
            ops.fix(node.tag, 1, 1, 1, 1, 1, 1)

    def _add_ops_mp_constraints(self, masses: np.ndarray = None) -> None:
        """Define multi-point (MP) constraints.

        Notes
        -----
        - Floor centre of mass may differ depending on the masses
        considered in seismic loading. If nodal masses are not specified,
        the centre of mass is computed based on 1.0G + 1.0Q
        - To define rigid diapragms, also retained nodes and corresponding
        single-point constraints are added.

        Returns
        -------
        List[int]
            List of floor retained node tags
        np.ndarray
            List of total floor weights
        np.ndarray
            List of floor heights
        np.ndarray
            Diaphragm length along -X
        np.ndarray
            Diaphragm length along -Y
        """
        perp_dirn = 3
        if masses is None:  # Set the masses for finding the center of mass
            masses_g, masses_q = np.array(self._get_nodal_masses())
            masses = masses_g + masses_q

        rnodes = []
        floor_weights = []
        floor_heights = []
        floor_lx = []
        floor_ly = []
        for i, nodes in enumerate(self.geometry.floor_level_points):
            sum_mass = 0  # summation of the masses
            sum_mass_moment = 0  # summation of the mass moments
            cnodes = []
            all_coords = []
            for node in nodes:
                cnodes.append(node.tag)
                idx = self.geometry.point_tags.index(node.tag)
                mass = np.array([masses[idx]] * 3)
                coords = np.array(node.coordinates)
                all_coords.append(coords)
                sum_mass += mass
                sum_mass_moment += mass * coords
            # Find centre of (CM)
            cm = np.round(sum_mass_moment / sum_mass, 2)
            # Floor retained node tag
            rnode = int(90000 + 1000 * i)
            # Rigid diaphragm node tags
            floor_nodes = [rnode] + cnodes
            # Recreate the retained nodes with new CM
            if rnode in ops.getNodeTags():
                ops.remove('node', rnode)
                ops.node(rnode, *cm.tolist())
            else:
                # Create floor retained node
                ops.node(rnode, *cm.tolist())
                # Add single-point restraints for the retained node
                ops.fix(rnode, 0, 0, 1, 1, 1, 0)
                # Create the rigid diaphragm
                ops.rigidDiaphragm(perp_dirn, *floor_nodes)
            # Rigid diaphragm dimensions
            rnodes.append(rnode)
            all_coords = np.array(all_coords)
            lx, ly, _ = all_coords.max(axis=0) - all_coords.min(axis=0)
            floor_lx.append(lx)
            floor_ly.append(ly)
            floor_weights.append(sum_mass[0] * grav_acc)
            floor_heights.append(cm[2])

        return (rnodes, np.array(floor_weights), np.array(floor_heights),
                np.array(floor_lx), np.array(floor_ly))

    def _add_ops_gravity_loads(self, load_case: Literal['G', 'Q'],
                               alpha: bool = False) -> None:
        """Adds gravity loads to opensees model for given load situation.

        Parameters
        ----------
        load_case : Literal['G', 'Q']
            Definition of gravity load case.
            ('G': permanent loads, 'Q': variable loads)
        alpha : bool, optional
            Flag to determine whether beam gravity loads are computed
            considering alpha factored slab loads or not, by default False.
        """
        # Reset the model to initial state for gravity loading
        p_tag = 1
        ts_tag = 1
        self._reset_state_remove_loads(p_tag, ts_tag)
        # Time-series defines relationship between time-domain and loads
        ops.timeSeries("Linear", p_tag)
        # Plain load pattern added to the domain
        ops.pattern('Plain', ts_tag, p_tag)
        # Beam loading
        wz = 0.0
        wx = 0.0
        for beam in self.beams:
            ele = beam.line.tag  # element tag
            # Distributed load in local y-axis
            if load_case == "G":
                if alpha:
                    wy = -beam.wg_total_alpha
                else:
                    wy = -beam.wg_total
            elif load_case == "Q":
                if alpha:
                    wy = -beam.wq_total_alpha
                else:
                    wy = -beam.wq_total
            ops.eleLoad('-ele', ele, '-type', '-beamUniform', wy, wz, wx)
        # Column loading
        if load_case == "G":
            wy = 0.0
            wz = 0.0
            for column in self.columns:
                ele = column.line.tag  # element tag
                wx = -column.self_wg  # distributed load in local x-axis
                ops.eleLoad('-ele', ele, '-type', '-beamUniform', wy, wz, wx)

    def _add_ops_seismic_loads(
        self, nodal_forces: List[float],
        load_case: Literal["E+X", "E-X", "E+Y", "E-Y"],
        rnodes: List[int],
        ecc_mom: List[float]
    ) -> None:
        """Adds seismic loads to the OpenSees model for a given load case.

        Parameters
        ----------
        nodal_forces : List[float]
            List of equivalent seismic lateral forces to be applied at each
            retained floor node. The order should correspond to
            `self.geometry.point_tags`.
        load_case : Literal["E+X", "E-X", "E+Y", "E-Y"]
            Seismic load case indicating excitation direction.
        rnodes : List[int]
            List of node tags for retained floor nodes where torsional
            moments resulting from accidental eccentricity are applied.
        ecc_mom : List[float]
            List of torsional moments applied at ach retained floor node
            due to accidental eccentricity from the center of mass.
            Must be in the same order as `rnodes`.
        """
        # Reset the model to initial state for gravity loading
        p_tag = 2
        ts_tag = 2
        self._reset_state_remove_loads(p_tag, ts_tag)
        # Time-series defines relationship between time-domain and loads
        ops.timeSeries("Linear", p_tag)
        # Plain load pattern added to the domain
        ops.pattern('Plain', ts_tag, p_tag)
        # Loop through all nodes and add horizontal loads
        for i, force in enumerate(nodal_forces):
            node = self.geometry.point_tags[i]
            if load_case == 'E+X':  # in plus x direction
                ops.load(node, force, 0.0, 0.0, 0.0, 0.0, 0.0)
            elif load_case == 'E-X':  # in negative x direction
                ops.load(node, -force, 0.0, 0.0, 0.0, 0.0, 0.0)
            elif load_case == 'E+Y':  # in plus y direction
                ops.load(node, 0.0, force, 0.0, 0.0, 0.0, 0.0)
            elif load_case == 'E-Y':  # in negative y direction
                ops.load(node, 0.0, -force, 0.0, 0.0, 0.0, 0.0)
        # Loop through retained floor nodes to add torsion due to ecc.
        for i, node in enumerate(rnodes):
            ops.load(node, 0.0, 0.0, 0.0, 0.0, 0.0, ecc_mom[i])

    def _build_ops_model_gravity(self) -> None:
        """Builds the model for load cases of gravity load combos.
        """
        self._init_ops_model()
        self._add_ops_nodes()
        self._add_ops_beam_column_elements()
        self._add_ops_sp_constraints()
        self._add_ops_mp_constraints()

    def _build_ops_model_seismic(self) -> None:
        """Builds the model for load cases of seismic load combos.
        """
        self._init_ops_model()
        self._add_ops_nodes()
        self._add_ops_beam_column_elements(True)
        self._add_ops_sp_constraints()
        self._add_ops_mp_constraints()

    def _do_linear_static_analysis(self) -> None:
        """Perform load controlled linear static analysis.
        """
        ops.system('UmfPack')
        ops.numberer('RCM')
        ops.constraints('Transformation')
        ops.test('NormDispIncr', 1e-08, 6)
        ops.integrator('LoadControl', 1)
        ops.algorithm('Linear')
        ops.analysis('Static')
        ops.analyze(1)
        ops.loadConst('-time', 0.0)

    def _run_gravity_load_cases(self) -> None:
        """Saves the results from gravity load cases.
        """
        # Analysis with gross section properties
        # Using slab loads without alpha factor
        self._build_ops_model_gravity()  # The model for gravity loading
        self._add_ops_gravity_loads('G')
        self._do_linear_static_analysis()
        self._get_element_forces(load_case="G/gravity")
        self._add_ops_gravity_loads('Q')
        self._do_linear_static_analysis()
        self._get_element_forces(load_case="Q/gravity")
        # Using alpha factored slab loads
        self._add_ops_gravity_loads('G', alpha=True)
        self._do_linear_static_analysis()
        self._get_element_forces(load_case="G/gravity/alpha")
        self._add_ops_gravity_loads('Q', alpha=True)
        self._do_linear_static_analysis()
        self._get_element_forces(load_case="Q/gravity/alpha")
        # Analysis with cracked section properties
        # Using slab loads without alpha factor
        self._build_ops_model_seismic()  # The model for seismic loading
        self._add_ops_gravity_loads('G')
        self._do_linear_static_analysis()
        self._get_element_forces(load_case="G/seismic")
        self._add_ops_gravity_loads('Q')
        self._do_linear_static_analysis()
        self._get_element_forces(load_case="Q/seismic")
        # Alpha factored slab loads
        self._add_ops_gravity_loads('G', alpha=True)
        self._do_linear_static_analysis()
        self._get_element_forces(load_case="G/seismic/alpha")
        self._add_ops_gravity_loads('Q', alpha=True)
        self._do_linear_static_analysis()
        self._get_element_forces(load_case="Q/seismic/alpha")

    def _run_seismic_load_cases(self) -> None:
        """Saves the results from seismic load cases.
        """
        # Accidental eccentricity
        if self.loads.eccentricity != 0:
            ecc = self.loads.eccentricity
            ecc_factors = [ecc / 100, -ecc / 100]
        else:
            ecc_factors = []
        mass_factors = self._get_mass_factors()
        masses_g, masses_q = np.array(self._get_nodal_masses())
        heights = np.array(self._get_nodal_heights())
        seismic_load_cases = ["E+X", "E-X", "E+Y", "E-Y"]
        self._build_ops_model_seismic()  # Initialize model for seismic loading
        for load_case in seismic_load_cases:
            for gfact, qfact in mass_factors:
                masses = gfact * masses_g + qfact * masses_q
                weights = grav_acc * masses
                # Redefine the rigid diaphragms with load-specific location
                rnodes, floor_weights, floor_heights, lx, ly = \
                    self._add_ops_mp_constraints(masses)
                _, nodal_forces = self.loads.get_seismic_loads(
                    beta=self.beta, weights=weights, heights=heights)
                self._add_ops_seismic_loads(
                    nodal_forces.tolist(), load_case, [], 0.0)
                self._do_linear_static_analysis()
                load_tag = f"{load_case}/{gfact}G/{qfact}Q"
                self._get_element_forces(load_case=load_tag)

                # Find forces resulting from accidental eccentricty
                _, floor_forces = self.loads.get_seismic_loads(
                    beta=self.beta, weights=floor_weights,
                    heights=floor_heights)
                # Loop through each eccentricity case
                for ecc_fact in ecc_factors:
                    if 'X' in load_case:
                        ecc = ly * ecc_fact
                    elif 'Y' in load_case:
                        ecc = lx * ecc_fact
                    ecc_mom = floor_forces * ecc
                    self._add_ops_seismic_loads(
                        [], load_case, rnodes, ecc_mom)
                    self._do_linear_static_analysis()
                    load_tag = f"{load_case}/{gfact}G/{qfact}Q/{ecc_fact}ecc"
                    self._get_element_forces(load_case=load_tag)

    def _get_element_forces(self, load_case: str) -> None:
        """Gets the element forces and saves with specified tag.

        Parameters
        ----------
        load_case : str
            Loading tag used for saving the element forces.
        """
        # Get forces for beams
        for beam in self.beams:
            ele = beam.line.tag  # element tag
            M1 = ops.sectionForce(ele, 1, 2)
            M5 = ops.sectionForce(ele, 5, 2)
            M9 = ops.sectionForce(ele, 9, 2)
            V1 = ops.sectionForce(ele, 1, 3)
            V5 = ops.sectionForce(ele, 5, 3)
            V9 = ops.sectionForce(ele, 9, 3)
            beam.forces[load_case] = BeamForces(M1, M5, M9, V1, V5, V9)
        # Get forces for columns
        for column in self.columns:
            ele = column.line.tag  # element tag
            N1 = ops.sectionForce(ele, 1, 1)
            Mx1 = ops.sectionForce(ele, 1, 2)  # z is renamed as x outside
            Vy1 = ops.sectionForce(ele, 1, 3)
            My1 = ops.sectionForce(ele, 1, 4)
            Vx1 = ops.sectionForce(ele, 1, 5)  # z is renamed as x outside
            N9 = ops.sectionForce(ele, 9, 1)
            Mx9 = ops.sectionForce(ele, 9, 2)  # z is renamed as x outside
            Vy9 = ops.sectionForce(ele, 9, 3)
            My9 = ops.sectionForce(ele, 9, 4)
            Vx9 = ops.sectionForce(ele, 9, 5)  # z is renamed as x outside
            column.forces[load_case] = ColumnForces(N1, Mx1, Vy1, My1, Vx1,
                                                    N9, Mx9, Vy9, My9, Vx9)

    def _reset_state_remove_loads(self, p_tag: int, ts_tag: int) -> None:
        """Removes specified loads, and then resets the model state to initial.

        Parameters
        ----------
        p_tag : int
            Load pattern tag for loading
        ts_tag : int
            Time series tag for loading
        """
        ops.remove('loadPattern', p_tag)
        ops.remove('timeSeries', ts_tag)
        ops.reset()
        ops.wipeAnalysis()

    def analyze_for_all(self):
        """Analyzes the building all load cases and combinations.

        Stores element forces for each.
        """
        # Seismic load cases
        seismic_load_cases = ["E+X", "E-X", "E+Y", "E-Y"]
        # Distinguish gravity and seismic load combinations
        seismic_combos = self.loads.get_seismic_load_combos()
        gravity_combos = self.loads.get_gravity_load_combos()
        # Run all load cases
        self._run_gravity_load_cases()
        if any(seismic_combos):
            self._run_seismic_load_cases()
        # Accidental eccentricity
        ecc = self.loads.eccentricity
        ecc_factors = [ecc / 100, 0.0, -ecc / 100] if ecc != 0 else [0.0]
        # Start combining forces for BEAMS
        for beam in self.beams:
            # Restart combo forces
            beam.design_forces = []
            # Loop through combinations
            for combo in self.loads.combinations:
                # Initialzie total combined forces
                forces = BeamForces(0, 0, 0, 0, 0, 0)
                # Determine type of the load combination
                if combo in seismic_combos:
                    combo_type = 'seismic'
                elif combo in gravity_combos:
                    combo_type = 'gravity'
                # Permanent Loads
                if 'G' in combo.loads:
                    gfactor = combo.loads['G']
                    if combo_type == 'gravity':
                        forces += gfactor * beam.forces["G/gravity/alpha"]
                    if combo_type == 'seismic':
                        forces += gfactor * beam.forces["G/seismic/alpha"]
                # Variable Loads
                if 'Q' in combo.loads:
                    qfactor = combo.loads['Q']
                    if combo_type == 'gravity':
                        forces += qfactor * beam.forces["Q/gravity/alpha"]
                    if combo_type == 'seismic':
                        forces += qfactor * beam.forces["Q/seismic/alpha"]
                if combo_type == 'gravity':
                    # Set the loading case (type)
                    forces.case = combo_type
                    # Append the combined forces
                    beam.design_forces.append(forces)
                # Add the forces from seismic loading
                elif combo_type == 'seismic' and self.beta > 0.0:
                    # Add the forces from seismic loading
                    ecc_forces = []  # forces due to eccentric loading
                    gfactor = combo.masses['G']  # permanent loads factor
                    qfactor = combo.masses['Q']  # variable loads factor
                    for load_case in seismic_load_cases:
                        if load_case in combo.loads:
                            tag = f"{load_case}/{gfactor}G/{qfactor}Q"
                            fact = combo.loads[load_case]
                            forces += fact * beam.forces[tag]
                            tmp = []
                            for ecc in ecc_factors:
                                if ecc == 0:
                                    tmp.append(BeamForces(0, 0, 0, 0, 0, 0))
                                else:
                                    tag_e = tag + f"/{ecc}ecc"
                                    tmp.append(fact * beam.forces[tag_e])
                            ecc_forces.append(tmp)
                    # Possible combinations with eccentric loadings
                    ecc_combos = list(product(*ecc_forces))
                    for ecc_combo in ecc_combos:
                        # Add the forces due to ecc. loading
                        forces_ = sum(ecc_combo, forces)
                        # Set the loading case (type)
                        forces_.case = combo_type
                        # Append the combined forces
                        beam.design_forces.append(forces_)

        # Start combining forces for COLUMNS
        for column in self.columns:
            # Restart combo forces
            column.design_forces = []
            # Loop through combinations
            for combo in self.loads.combinations:
                # Initialzie total combined forces
                forces = ColumnForces(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                # Determine type of the load combination
                if combo in seismic_combos:
                    combo_type = 'seismic'
                elif combo in gravity_combos:
                    combo_type = 'gravity'
                # Permanent Loads
                if 'G' in combo.loads:
                    gfactor = combo.loads['G']
                    if combo_type == 'gravity':
                        forces += gfactor * column.forces["G/gravity"]
                    if combo_type == 'seismic':
                        forces += gfactor * column.forces["G/seismic"]
                # Variable Loads
                if 'Q' in combo.loads:
                    qfactor = combo.loads['Q']
                    if combo_type == 'gravity':
                        forces += qfactor * column.forces["Q/gravity"]
                    if combo_type == 'seismic':
                        forces += qfactor * column.forces["Q/seismic"]
                if combo_type == 'gravity':
                    # Set the loading case (type)
                    forces.case = combo_type
                    # Append the combined forces
                    column.design_forces.append(forces)
                # Add the forces from seismic loading
                elif combo_type == 'seismic' and self.beta > 0.0:
                    # Add the forces from seismic loading
                    ecc_forces = []  # forces due to eccentric loading
                    gfactor = combo.masses['G']  # permanent loads factor
                    qfactor = combo.masses['Q']  # variable loads factor
                    for load_case in seismic_load_cases:
                        if load_case in combo.loads:
                            tag = f"{load_case}/{gfactor}G/{qfactor}Q"
                            fact = combo.loads[load_case]
                            forces += fact * column.forces[tag]
                            tmp = []  # ecc. forces per load_case
                            for ecc in ecc_factors:
                                if ecc == 0:
                                    tmp.append(ColumnForces(0, 0, 0, 0, 0,
                                                            0, 0, 0, 0, 0))
                                else:
                                    tag_e = tag + f"/{ecc}ecc"
                                    tmp.append(fact * column.forces[tag_e])
                            ecc_forces.append(tmp)
                    # Possible combinations with eccentric loadings
                    ecc_combos = list(product(*ecc_forces))
                    for ecc_combo in ecc_combos:
                        # Add the forces due to ecc. loading
                        forces_ = sum(ecc_combo, forces)
                        # Set the loading case (type)
                        forces_.case = combo_type
                        # Append the combined forces
                        column.design_forces.append(forces_)
