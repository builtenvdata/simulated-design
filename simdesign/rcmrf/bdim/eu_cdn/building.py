"""This module provides the Building Design Information Model (BDIM)
implementation for the ``eu_cdh`` design class.
"""
# Imports from installed packages
from typing import List, Type

# Imports from the design class (eu_cdn) library
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
    """BDIM implementation for design class ``eu_cdn``.

    This class extends ``BuildingBase`` by narrowing the attribute types
    to the ``eu_cdn`` implementations and overriding design class-specific
    methods.

    Attributes
    ----------
    beams : List[~simdesign.rcmrf.bdim.eu_cdn.beam.Beam]
        List of beam instances.
    columns : List[~simdesign.rcmrf.bdim.eu_cdn.column.Column]
        List of column instances.
    joints : List[~simdesign.rcmrf.bdim.eu_cdn.joint.Joint]
        List of joint instances.
    slabs : List[~simdesign.rcmrf.bdim.eu_cdn.slab.Slab]
        List of slab instances.
    stairs : List[~simdesign.rcmrf.bdim.eu_cdn.stairs.Stairs]
        List of stairs instances.
    infills : List[~simdesign.rcmrf.bdim.eu_cdn.infill.Infill]
        List of infill wall instances.
    steel : ~simdesign.rcmrf.bdim.eu_cdn.materials.Steel
        Steel material instance used in the design of beams and columns.
    concrete : ~simdesign.rcmrf.bdim.eu_cdn.materials.Concrete
        Concrete material instance used in the design of beams and columns.
    loads : ~simdesign.rcmrf.bdim.eu_cdn.loads.Loads
        Loads instance used to apply building loads.
    materials : ~simdesign.rcmrf.bdim.eu_cdn.materials.Materials
        Materials instance used to set building materials.
    rebars : ~simdesign.rcmrf.bdim.eu_cdn.rebars.Rebars
        Rebars instance used to determine reinforcement arrangement.
    quality : ~simdesign.rcmrf.bdim.eu_cdn.quality.Quality
        Quality instance used to adjust properties of structural elements.
    COLUMN_UNIFORMIZATION_STEP : int
        Step size for column section uniformisation across storeys. For
        example, a value of 2 allows the section to vary every two storeys
        from bottom to top.

    Notes
    -----
    - Design follows allowable stress design approach.
    - Design is based on gravity loading only (no seismic design).
    - Main reference building code is RBA-1935.
    - Basic units are kN, m, sec.
    - Overrides :meth:`_set_maximum_column_dimensions` method to set
      design-class specific maximum column dimensions.

    See Also
    --------
    :class:`~simdesign.rcmrf.bdim.baselib.building.BuildingBase`
        Base class defining the core behaviour and configuration.

    References
    ----------
    RBA (1935). *Regulamento do Betão Armado*.
    Decreto N.° 25:948, Lisbon, Portugal.
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
    COLUMN_UNIFORMIZATION_STEP = 2

    def __init__(self, taxonomy: TaxonomyData) -> None:
        """Initialize the Building object.

        Parameters
        ----------
        taxonomy : TaxonomyData
            Taxonomy data required for performing simulated designs.
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
        # Set the quality models considered for structural property adjustments
        self.quality = Quality()
        # Initialise the structure
        super().__init__(taxonomy=taxonomy)
        # Set the maximum column dimensions for full design routine
        self._set_maximum_column_dimensions()

    def _set_maximum_column_dimensions(self) -> None:
        """Set the maximum column dimensions based on number of storeys.

        Notes
        -----
        The limits are based on engineering judgement and can be modified.
        If the limits are independent of the number of storeys, they can
        instead be set directly within the column object, similarly to the
        minimum dimension.
        """
        for column in self.columns:
            if self.num_storeys <= 3:
                column.MAX_B_SQUARE = 0.45 * m
                column.MAX_B_RECTANGLE = 0.70 * m
            elif self.num_storeys <= 6:
                column.MAX_B_SQUARE = 0.60 * m
                column.MAX_B_RECTANGLE = 1.00 * m
            elif self.num_storeys <= 9:
                column.MAX_B_SQUARE = 0.85 * m
                column.MAX_B_RECTANGLE = 1.20 * m
