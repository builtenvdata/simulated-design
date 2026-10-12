"""This module provides the Building Design Information Model (BDIM)
implementation for the ``eu_cdh`` design class.
"""
# Imports from installed packages
from typing import List, Type
import numpy as np

# Imports from the design class (eu_cdh) library
from .analysis import ElasticModel
from .beam import Beam
from .column import Column
from .joint import Joint
from .loads import Loads
from .materials import Materials, Concrete, Steel
from .quality import Quality
from .rebars import Rebars
from .slab import Slab
from .stairs import Stairs
from .infill import Infill

# Imports from bdim base library
from ..baselib.building import BuildingBase, TaxonomyData

# Imports from units library
from ....utils.units import m


class Building(BuildingBase):
    """BDIM implementation for design class ``eu_cdh``.

    This class extends ``BuildingBase`` by narrowing the attribute types
    to the ``eu_cdh`` implementations and overriding design class-specific
    methods.

    Attributes
    ----------
    beams : List[~simdesign.rcmrf.bdim.eu_cdh.beam.Beam]
        List of beam instances.
    columns : List[~simdesign.rcmrf.bdim.eu_cdh.column.Column]
        List of column instances.
    joints : List[~simdesign.rcmrf.bdim.eu_cdh.joint.Joint]
        List of joint instances.
    slabs : List[~simdesign.rcmrf.bdim.eu_cdh.slab.Slab]
        List of slab instances.
    stairs : List[~simdesign.rcmrf.bdim.eu_cdh.stairs.Stairs]
        List of stairs instances.
    infills : List[~simdesign.rcmrf.bdim.eu_cdh.infill.Infill]
        List of infill wall instances.
    steel : ~simdesign.rcmrf.bdim.eu_cdh.materials.Steel
        Steel material instance used in the design of beams and columns.
    concrete : ~simdesign.rcmrf.bdim.eu_cdh.materials.Concrete
        Concrete material instance used in the design of beams and columns.
    loads : ~simdesign.rcmrf.bdim.eu_cdh.loads.Loads
        Loads instance used to apply building loads.
    materials : ~simdesign.rcmrf.bdim.eu_cdh.materials.Materials
        Materials instance used to set building materials.
    rebars : ~simdesign.rcmrf.bdim.eu_cdh.rebars.Rebars
        Rebars instance used to determine reinforcement arrangement.
    quality : ~simdesign.rcmrf.bdim.eu_cdh.quality.Quality
        Quality instance used to adjust properties of structural elements.
    OVERSTRENGTH_FACTOR_COLUMN_MOMENT : float | None
        Safety or overstrength factor considered in calculation of capacity
        design moments for columns (strong-column weak-beam principle).
        The default value is 1.3, see EN 1998-1:2004 4.4.2.3(4).
    OVERSTRENGTH_FACTOR_BEAM_SHEAR : float | None
        Safety or overstrength factor considered in calculation of capacity
        design shear forces for beams. Overstrength factor for DCM is
        considered here.
        - 1.0 for DCM beams, see EN 1998-1:2004 clause 5.4.2.2(2)
        - 1.2 for DCH beams, see EN 1998-1:2004 clause 5.5.2.1(3)
    OVERSTRENGTH_FACTOR_COLUMN_SHEAR : float | None
        Safety or overstrength factor considered in calculation of capacity
        design shear forces for columns. Overstrength factor for DCM is
        considered here.
        - 1.1 for DCM columns, see EN 1998-1:2004 5.4.2.3(2)
        - 1.3 for DCH columns, see EN 1998-1:2004 5.5.2.2(3)

    See Also
    --------
    :class:`~simdesign.rcmrf.bdim.baselib.building.BuildingBase`
        Base class defining the core behaviour and configuration.

    Notes
    -----
    - Design follows limit state design approach.
    - Capacity design principle is followed (weak-beam strong-column).
    - Main reference building code is Eurocode 8-1 (moderate ductility class).
    - Material strengths are higher compared to 'eu_cdm'.
    - Basic units are kN, m, sec
    - Overrides :meth:`_set_maximum_column_dimensions` method to set
      design-class specific maximum column dimensions.
    - Overrides :meth:`_change_materials` method to use design-class
      specific material change order.

    References
    ----------
    Comité Européen de Normalisation, CEN (2004). Eurocode 8: Design of
    Structures for Earthquake Resistance — Part 1: General Rules,
    Seismic Actions and Rules for Buildings.
    European Committee for Standardization, Brussels, Belgium.
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
    OVERSTRENGTH_FACTOR_COLUMN_MOMENT = 1.3  # EN 1998-1:2004 clause 4.4.2.3(4)
    OVERSTRENGTH_FACTOR_BEAM_SHEAR = 1.0  # EN 1998-1:2004 clause 5.4.2.2(2)
    OVERSTRENGTH_FACTOR_COLUMN_SHEAR = 1.1  # EN 1998-1:2004 clause 5.4.2.3(2)
    LOCAL_DUCTILITY_ITER_MAX = 5
    """Maximum number of transverse reinforcement updates of a base column
    for the local ductility requirement of EN 1998-1:2004, 5.4.3.2.2(8)."""
    CT = 0.075
    """Coefficient Ct of the approximate fundamental period of RC moment
    resisting frames, T1 = Ct H^(3/4) (EN 1998-1:2004, 4.6.3.2, Eq. 4.6)."""
    TC = 0.5  # Assumed: most buildings are located at B sites
    """Corner period Tc (s) of the constant spectral acceleration branch,
    ground type B, Type 1 spectrum (EN 1998-1:2004, Table 3.2)."""

    def __init__(self, taxonomy: TaxonomyData) -> None:
        """Initialize the Building object.

        Parameters
        ----------
        taxonomy : TaxonomyData
            Taxonomy data required for performing simulated-designs.

        See Also
        --------
        :class:`~simdesign.rcmrf.bdim.baselib.building.TaxonomyData`
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

    def _check_columns_local_ductility(self) -> None:
        """Check the local ductility requirement of EN 1998-1:2004,
        5.4.3.2.2(8), in the critical regions at the base of the columns
        (see ``Column.check_local_ductility_requirement``).

        If a base column does not satisfy the requirement, its required
        ratio of transverse reinforcement area to spacing is increased in
        proportion to the shortfall of ``alpha omega_wd``, and its transverse
        reinforcement is selected again. This is repeated up to
        ``LOCAL_DUCTILITY_ITER_MAX`` times. If the requirement is still not
        satisfied, the column is marked as failed (``ok_x``, ``ok_y``), so
        that its dimensions are increased, which reduces the normalised
        axial force.

        Notes
        -----
        - The curvature ductility factor uses the approximate fundamental
          period ``T1 = CT H^(3/4)``, with the height ``H`` of the building
          above the base, and the corner period ``TC``.
        - The transverse reinforcement of the whole ground-storey column is
          increased, not only that of its critical region.
        """
        if self.columns_fail:  # Columns have already failed
            return
        factors = self._get_unique_seism_combo_grav_factors()
        # Ground level, where the base columns start
        z0 = min(self.geometry.system_grid_data.z.ordinates)
        # Approximate fundamental period - EN 1998-1:2004, Eq. 4.6
        height = max(self.geometry.system_grid_data.z.ordinates) - z0
        T1 = self.CT * height**0.75
        for col in self.columns:
            z_bottom = min(p.coordinates[2] for p in col.line.points)
            if not np.isclose(z_bottom, z0):
                continue  # Not a base column
            for _ in range(self.LOCAL_DUCTILITY_ITER_MAX):
                ok, alpha_omega_wd, required = (
                    col.check_local_ductility_requirement(
                        factors, T1=T1, Tc=self.TC))
                if ok:
                    break
                # Increase the required transverse reinforcement (at least
                # the provided one) in proportion to the shortfall
                factor = 1.05 * required / max(alpha_omega_wd, 1e-6)
                Ab = 0.25 * np.pi * col.dbh**2
                col.Ashx_sbh_req = factor * max(
                    col.Ashx_sbh_req, col.nbh_x * Ab / col.sbh)
                col.Ashy_sbh_req = factor * max(
                    col.Ashy_sbh_req, col.nbh_y * Ab / col.sbh)
                # Select the transverse reinforcement again
                dbh, sbh, nbh_x, nbh_y = self.rebars.get_column_transv_rebars(
                    np.array([col.bx]), np.array([col.by]),
                    np.array([col.Ashx_sbh_req]),
                    np.array([col.Ashy_sbh_req]),
                    np.array([col.dbl_cor]), np.array([col.nblx_int]),
                    np.array([col.nbly_int]))
                col.dbh, col.sbh = dbh[0], sbh[0]
                col.nbh_x, col.nbh_y = nbh_x[0], nbh_y[0]
                col.validate_transverse_reinforcement()
            else:
                ok, _, _ = col.check_local_ductility_requirement(
                    factors, T1=T1, Tc=self.TC)
            if not ok:
                # Increase the column dimensions in the next iteration
                col.ok_x = False
                col.ok_y = False

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

    def _change_materials(self) -> None:
        """The method used for changing materials in iterative design
        algorithm.

        Notes
        -----
        It is overwritten for eu_cdh design class with following changes:
        - The method is modified such that steel and concrete materials
        is not updated simultaneously in the same iteration. Instead,
        first, the concrete material is updated, when the final concrete
        material is reached steel material is updated.
        """
        if self.next_concrete:
            self.concrete = self.next_concrete
        elif self.next_steel:
            self.steel = self.next_steel
