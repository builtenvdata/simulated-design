"""This module provides the Building Design Information Model (BDIM)
implementation for the ``tr_0018_dch`` design class.
"""
# Imports from installed packages
from typing import List, Type, Tuple

# Imports from the design class (tr_0018_dch) library
from .analysis import ElasticModel
from .beam import Beam
from .column import Column
from .joint import Joint
from .materials import Materials, Concrete, Steel
from .quality import Quality
from .loads import Loads
from .rebars import Rebars
from .slab import Slab
from .stairs import Stairs
from .infill import Infill

# Imports from bdim base library
from ..baselib.building import BuildingBase, TaxonomyData

# Imports from units library
from ....utils.units import m


class Building(BuildingBase):
    """BDIM implementation for design class ``tr_0018_dch``.

    This class extends ``BuildingBase`` by narrowing the attribute types
    to the ``tr_0018_dch`` implementations and overriding design class-specific
    methods.

    Attributes
    ----------
    beams : List[~simdesign.rcmrf.bdim.tr_0018_dch.beam.Beam]
        List of beam instances.
    columns : List[~simdesign.rcmrf.bdim.tr_0018_dch.column.Column]
        List of column instances.
    joints : List[~simdesign.rcmrf.bdim.tr_0018_dch.joint.Joint]
        List of joint instances.
    slabs : List[~simdesign.rcmrf.bdim.tr_0018_dch.slab.Slab]
        List of slab instances.
    stairs : List[~simdesign.rcmrf.bdim.tr_0018_dch.stairs.Stairs]
        List of stairs instances.
    infills : List[~simdesign.rcmrf.bdim.tr_0018_dch.infill.Infill]
        List of infill wall instances.
    steel : ~simdesign.rcmrf.bdim.tr_0018_dch.materials.Steel
        Steel material instance used in the design of beams and columns.
    concrete : ~simdesign.rcmrf.bdim.tr_0018_dch.materials.Concrete
        Concrete material instance used in the design of beams and columns.
    loads : ~simdesign.rcmrf.bdim.tr_0018_dch.loads.Loads
        Loads instance used to apply building loads.
    materials : ~simdesign.rcmrf.bdim.tr_0018_dch.materials.Materials
        Materials instance used to set building materials.
    rebars : ~simdesign.rcmrf.bdim.tr_0018_dch.rebars.Rebars
        Rebars instance used to determine reinforcement arrangement.
    quality : ~simdesign.rcmrf.bdim.tr_0018_dch.quality.Quality
        Quality instance used to adjust properties of structural elements.
    OVERSTRENGTH_FACTOR_COLUMN_MOMENT : float
        Safety or overstrength factor considered in calculation of capacity
        design moments for columns (strong-column weak-beam principle).
    OVERSTRENGTH_FACTOR_BEAM_SHEAR : float
        Safety or overstrength factor considered in calculation of capacity
        design shear forces for beams.
    OVERSTRENGTH_FACTOR_COLUMN_SHEAR : float
        Safety or overstrength factor considered in calculation of capacity
        design shear forces for columns.

    See Also
    --------
    :class:`~bdim.baselib.building.BuildingBase`
        Base class defining the core behaviour and configuration.

    Notes
    -----
    - Design follows limit state design approach.
    - Capacity design principle is followed (weak-beam strong-column).
    - Main reference building code is TBEC-2007 (high ductility class).
    - Basic units are kN, m, sec
    - Overrides :meth:`_set_column_capacity_design_moments` method
      because TBEC-2007 does not enforce roof-level columns
      to follow capacity design principles.
    - Overrides :meth:`_set_column_capacity_design_shear_forces` method
      to calculate column capacity shear forces using beam capacity
      moments, except for ground floor columns, which are treated as specified
      in TBEC-2007.
    - Overrides :meth:`_set_beam_capacity_design_shear_forces` method
      since the rules in TBEC-2007 differ from those in EN 1998-1:2004.
    - Overrides :meth:`_set_maximum_column_dimensions` method to set
      design-class specific maximum column dimensions.

    References
    ----------
    TBEC (2007). *Deprem Bölgelerinde Yapılacak Binalar Hakkında Esaslar*.
    Resmi Gazete, Ankara, Türkiye.
    """
    beams: List[Beam]
    columns: List[Column]
    joints: List[Joint]
    slabs: List[Slab]
    stairs: List[Stairs]
    infills: List[Infill]
    steel: Steel
    concrete: Concrete
    loads: Loads
    materials: Materials
    rebars: Rebars
    quality: Quality
    ColumnClass: Type[Column]
    BeamClass: Type[Beam]
    JointClass: Type[Joint]
    SlabClass: Type[Slab]
    StairsClass: Type[Stairs]
    InfillClass: Type[Infill]
    ElasticModelClass: Type[ElasticModel]
    OVERSTRENGTH_FACTOR_COLUMN_MOMENT = 1.2
    OVERSTRENGTH_FACTOR_BEAM_SHEAR = 1.4
    OVERSTRENGTH_FACTOR_COLUMN_SHEAR = 1.4

    def __init__(self, taxonomy: TaxonomyData) -> None:
        """Initialize the Building object.

        Parameters
        ----------
        taxonomy : TaxonomyData
            Taxonomy data required for performing simulated-designs.
        """
        # Set classes used define building components.
        self.ColumnClass = Column
        self.BeamClass = Beam
        self.JointClass = Joint
        self.SlabClass = Slab
        self.StairsClass = Stairs
        self.InfillClass = Infill
        self.ElasticModelClass = ElasticModel
        # Set the available materials
        self.materials = Materials()
        # Set the design loads and combinations
        self.loads = Loads()
        # Set the rebar options considered for detailing
        self.rebars = Rebars()
        # Set the quality models considered for structural property adjusments
        self.quality = Quality()
        # Initialise the building
        super().__init__(taxonomy=taxonomy)
        # Set the maximum column dimensions for full design routine
        self._set_maximum_column_dimensions()

    def _set_maximum_column_dimensions(self) -> None:
        """Set the maximum column dimensions based on number of storeys.

        Notes
        -----
        The limitations based on engineering judgement. They can be changed.
        In case they are independent from number of storeys, these can be
        set within column object as similar to the minimum dimension.
        """
        for column in self.columns:
            if self.num_storeys <= 3:
                column.MAX_B_SQUARE = 0.60 * m
                column.MAX_B_RECTANGLE = 0.80 * m
            elif self.num_storeys <= 6:
                column.MAX_B_SQUARE = 0.80 * m
                column.MAX_B_RECTANGLE = 1.00 * m
            elif self.num_storeys <= 9:
                column.MAX_B_SQUARE = 0.80 * m
                column.MAX_B_RECTANGLE = 1.30 * m

    def _set_column_capacity_design_moments(self) -> None:
        """Append the capacity design moments to the list of design forces
        for columns.

        Notes
        -----
        Based on:
            Section 7.3.5 in TBEC-1998,
            Section 3.3.5 in TBEC-2007.
        """
        if self.OVERSTRENGTH_FACTOR_COLUMN_MOMENT is None:  # Do not add
            return
        else:
            gamma_rd = self.OVERSTRENGTH_FACTOR_COLUMN_MOMENT

        # Unique gravity load factors from seismic load combinations
        combo_grav_factors = self._get_unique_seism_combo_grav_factors()
        # Loop through each beam-column joint
        for joint in self.joints:
            # Sum of the design values of moment of resistances for beams
            sum_mrdb_x_pos = 0.0
            sum_mrdb_x_neg = 0.0
            sum_mrdb_y_pos = 0.0
            sum_mrdb_y_neg = 0.0
            if joint.left_beam:
                sum_mrdb_x_pos += joint.left_beam.mrd_pos[-1]
                sum_mrdb_x_neg += joint.left_beam.mrd_neg[-1]
            if joint.right_beam:
                sum_mrdb_x_pos += joint.right_beam.mrd_neg[0]
                sum_mrdb_x_neg += joint.right_beam.mrd_pos[0]
            if joint.rear_beam:
                sum_mrdb_y_pos += joint.rear_beam.mrd_pos[-1]
                sum_mrdb_y_neg += joint.rear_beam.mrd_neg[-1]
            if joint.front_beam:
                sum_mrdb_y_pos += joint.front_beam.mrd_neg[0]
                sum_mrdb_y_neg += joint.front_beam.mrd_pos[0]
            sum_mrdb_y = max(sum_mrdb_y_pos, sum_mrdb_y_neg)
            sum_mrdb_x = max(sum_mrdb_x_pos, sum_mrdb_x_neg)

            # Capacity design forces for columns
            for factors in combo_grav_factors:
                # Both top and bottom columns exist
                if joint.top_column and joint.bottom_column:
                    forces_top = (
                        factors["G"] * joint.top_column.forces["G/seismic"]
                        + factors["Q"] * joint.top_column.forces["Q/seismic"]
                    )
                    forces_bottom = (
                        factors["G"] * joint.bottom_column.forces["G/seismic"]
                        + factors["Q"]
                        * joint.bottom_column.forces["Q/seismic"]
                    )
                    forces_top.Mx1 = 0.5 * gamma_rd * sum_mrdb_y
                    forces_top.My1 = 0.5 * gamma_rd * sum_mrdb_x
                    forces_top.case = "capacity"
                    joint.top_column.design_forces.append(forces_top)
                    forces_bottom.Mx9 = 0.5 * gamma_rd * sum_mrdb_y
                    forces_bottom.My9 = 0.5 * gamma_rd * sum_mrdb_x
                    forces_bottom.case = "capacity"
                    joint.bottom_column.design_forces.append(forces_bottom)
                # Only top column exists
                elif joint.top_column:
                    forces_top = (
                        factors["G"] * joint.top_column.forces["G/seismic"]
                        + factors["Q"] * joint.top_column.forces["Q/seismic"]
                    )
                    forces_top.Mx1 = gamma_rd * sum_mrdb_y
                    forces_top.My1 = gamma_rd * sum_mrdb_x
                    forces_top.case = "capacity"
                    joint.top_column.design_forces.append(forces_top)

    def _set_column_capacity_design_shear_forces(self) -> None:
        """Append the column capacity design shear forces to the list of
        column design forces.

        Notes
        -----
        Based on:
            Section 7.3.5 in TBEC-1998,
            Section 3.3.5 in TBEC-2007.
        """

        def get_column_clear_length() -> Tuple[float, float]:
            """Get column clear length (distance between column faces).

            Returns
            -------
            Tuple[float, float]
                Column clear lengths for shear forces in local x and y axes.
            """
            hx_i = 1000
            hx_j = 1000
            hy_i = 1000
            hy_j = 1000
            # i'th joint height
            if joint_i.left_beam:
                hx_i = min(hx_i, joint_i.left_beam.h)
            if joint_i.right_beam:
                hx_i = min(hx_i, joint_i.right_beam.h)
            if joint_i.rear_beam:
                hy_i = min(hy_i, joint_i.rear_beam.h)
            if joint_i.front_beam:
                hy_i = min(hy_i, joint_i.front_beam.h)
            # j'th joint height
            if joint_j.left_beam:
                hx_j = min(hx_j, joint_j.left_beam.h)
            if joint_j.right_beam:
                hx_j = min(hx_j, joint_j.right_beam.h)
            if joint_j.rear_beam:
                hy_j = min(hy_j, joint_j.rear_beam.h)
            if joint_j.front_beam:
                hy_j = min(hy_j, joint_j.front_beam.h)
            if hx_i == 1000:
                hx_i = 0.0
            if hx_j == 1000:
                hx_j = 0.0
            if hy_i == 1000:
                hy_i = 0.0
            if hy_j == 1000:
                hy_j = 0.0

            # Return beam clear length
            lclx = column.H - (hx_i + hx_j) / 2
            lcly = column.H - (hy_i + hy_j) / 2

            return lclx, lcly

        # Check if the capacity design forces will be added
        if self.OVERSTRENGTH_FACTOR_COLUMN_SHEAR is None:  # Do not add
            return
        else:  # Add
            gamma_rd = self.OVERSTRENGTH_FACTOR_COLUMN_SHEAR

        # Loop through each column
        for column in self.columns:
            # Find joints at both ends
            joint_i = self._find_joint_by_point(column.elastic_nodes[0])
            joint_j = self._find_joint_by_point(column.elastic_nodes[1])

            Vcap_x, Vcap_y = 0, 0
            for force in column.design_forces:
                # Clear lengths of column in x and y
                col_lcx, col_lcy = get_column_clear_length()

                # The column moment of resistances at both ends
                mrdx_i = column.get_mrdx(Ned=abs(force.N1))
                mrdy_i = column.get_mrdy(Ned=abs(force.N1))
                mrdx_j = column.get_mrdx(Ned=abs(force.N9))
                mrdy_j = column.get_mrdy(Ned=abs(force.N9))

                # Column plastic moments for shear capacity forces
                Mpi_x_pos = gamma_rd * mrdx_i
                Mpi_x_neg = gamma_rd * mrdx_i
                Mpj_x_pos = gamma_rd * mrdx_j
                Mpj_x_neg = gamma_rd * mrdx_j
                Mpi_y_pos = gamma_rd * mrdy_i
                Mpi_y_neg = gamma_rd * mrdy_i
                Mpj_y_pos = gamma_rd * mrdy_j
                Mpj_y_neg = gamma_rd * mrdy_j

                # Capacity design shear forces at both ends
                Vdx_pos = (Mpi_y_pos + Mpj_y_neg) / col_lcx
                Vdx_neg = (Mpi_y_neg + Mpj_y_pos) / col_lcx
                Vdy_pos = (Mpi_x_pos + Mpj_x_neg) / col_lcy
                Vdy_neg = (Mpi_x_neg + Mpj_x_pos) / col_lcy

                # Set the capacity design shear forces
                Vcap_x = max(Vcap_x, Vdx_pos, Vdx_neg)
                Vcap_y = max(Vcap_y, Vdy_pos, Vdy_neg)

            # Set the design shear values
            column.Ve_x = max(Vcap_x, column.envelope_forces.Vx1,
                              column.envelope_forces.Vx9)
            column.Ve_y = max(Vcap_y, column.envelope_forces.Vy1,
                              column.envelope_forces.Vy9)

    def _set_beam_capacity_design_shear_forces(self) -> None:
        """Append the beam capacity design shear forces to the list of
        beam design forces.

        Notes
        -----
        Based on:
            Section 7.4.5 in TBEC-1998,
            Section 3.4.5 in TBEC-2007.
        """

        def get_beam_clear_length() -> float:
            """Get beam clear length (distance between column faces).

            Returns
            -------
            float
                Beam clear length
            """
            # i'th joint width
            if joint_i.top_column and joint_i.bottom_column:
                if beam.direction == "x":
                    bc_i = min(joint_i.top_column.bx, joint_i.bottom_column.bx)
                elif beam.direction == "y":
                    bc_i = min(joint_i.top_column.by, joint_i.bottom_column.by)
            elif joint_i.top_column:
                if beam.direction == "x":
                    bc_i = joint_i.top_column.bx
                if beam.direction == "y":
                    bc_i = joint_i.top_column.by
            elif joint_i.bottom_column:
                if beam.direction == "x":
                    bc_i = joint_i.bottom_column.bx
                if beam.direction == "y":
                    bc_i = joint_i.bottom_column.by
            # j'th joint width
            if joint_j.top_column and joint_j.bottom_column:
                if beam.direction == "x":
                    bc_j = min(joint_j.top_column.bx, joint_j.bottom_column.bx)
                elif beam.direction == "y":
                    bc_j = min(joint_j.top_column.by, joint_j.bottom_column.by)
            elif joint_j.top_column:
                if beam.direction == "x":
                    bc_j = joint_j.top_column.bx
                if beam.direction == "y":
                    bc_j = joint_j.top_column.by
            elif joint_j.bottom_column:
                if beam.direction == "x":
                    bc_j = joint_j.bottom_column.bx
                if beam.direction == "y":
                    bc_j = joint_j.bottom_column.by
            # Return beam clear length
            return beam.L - (bc_i + bc_j) / 2

        # Check if the capacity design forces will be added
        if self.OVERSTRENGTH_FACTOR_BEAM_SHEAR is None:  # Do not add
            return
        else:  # Add
            gamma_rd = self.OVERSTRENGTH_FACTOR_BEAM_SHEAR

        # Loop through each beam
        for beam in self.beams:
            # Find joints at both ends
            joint_i = self._find_joint_by_point(beam.elastic_nodes[0])
            joint_j = self._find_joint_by_point(beam.elastic_nodes[1])

            # Clear length of beam
            beam_lc = get_beam_clear_length()

            # Shear force due to gravity loads
            forces = beam.forces["G/seismic"] + beam.forces["Q/seismic"]
            Vdy_i = abs(forces.V1)
            Vdy_j = abs(forces.V9)

            # The beam moment of resistances at both ends
            Mpi_pos = gamma_rd * beam.mrd_pos[0]
            Mpi_neg = gamma_rd * beam.mrd_neg[0]
            Mpj_pos = gamma_rd * beam.mrd_pos[-1]
            Mpj_neg = gamma_rd * beam.mrd_neg[-1]

            # Capacity design shear forces at both ends
            Ved_i_pos = Vdy_i + (Mpi_pos + Mpj_neg) / beam_lc
            Ved_i_neg = Vdy_i - (Mpi_neg + Mpj_pos) / beam_lc
            Ved_j_pos = Vdy_j + (Mpj_pos + Mpi_neg) / beam_lc
            Ved_j_neg = Vdy_j - (Mpj_neg + Mpi_pos) / beam_lc

            beam.Ve1 = max(Ved_i_pos, abs(Ved_i_neg))
            beam.Ve9 = max(Ved_j_pos, abs(Ved_j_neg))
