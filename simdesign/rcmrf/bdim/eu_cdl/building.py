"""This module provides the Building Design Information Model (BDIM)
implementation for the ``eu_cdl`` design class.
"""
# Imports from installed packages
from typing import List, Type

# Imports from the design class (eu_cdl) library
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
    """BDIM implementation for design class ``eu_cdl``.

    This class extends ``BuildingBase`` by narrowing the attribute types
    to the ``eu_cdl`` implementations and overriding design class-specific
    methods.

    Attributes
    ----------
    beams : List[~simdesign.rcmrf.bdim.eu_cdl.beam.Beam]
        List of beam instances.
    columns : List[~simdesign.rcmrf.bdim.eu_cdl.column.Column]
        List of column instances.
    joints : List[~simdesign.rcmrf.bdim.eu_cdl.joint.Joint]
        List of joint instances.
    slabs : List[~simdesign.rcmrf.bdim.eu_cdl.slab.Slab]
        List of slab instances.
    stairs : List[~simdesign.rcmrf.bdim.eu_cdl.stairs.Stairs]
        List of stairs instances.
    infills : List[~simdesign.rcmrf.bdim.eu_cdl.infill.Infill]
        List of infill wall instances.
    steel : ~simdesign.rcmrf.bdim.eu_cdl.materials.Steel
        Steel material instance used in the design of beams and columns.
    concrete : ~simdesign.rcmrf.bdim.eu_cdl.materials.Concrete
        Concrete material instance used in the design of beams and columns.
    loads : ~simdesign.rcmrf.bdim.eu_cdl.loads.Loads
        Loads instance used to apply building loads.
    materials : ~simdesign.rcmrf.bdim.eu_cdl.materials.Materials
        Materials instance used to set building materials.
    rebars : ~simdesign.rcmrf.bdim.eu_cdl.rebars.Rebars
        Rebars instance used to determine reinforcement arrangement.
    quality : ~simdesign.rcmrf.bdim.eu_cdl.quality.Quality
        Quality instance used to adjust properties of structural elements.
    COLUMN_UNIFORMIZATION_STEP : int
        Step size for column section uniformisation across storeys. For
        example, a value of 2 allows the section to vary every two storeys
        from bottom to top.

    See Also
    --------
    :class:`~bdim.baselib.building.BuildingBase`
        Base class defining the core behaviour and configuration.

    Notes
    -----
    - Design follows allowable stress design and the stress-block method.
    - Main reference building code is REBA-1967.
    - Material strengths are higher compared to 'eu_cdn'.
    - Basic units are kN, m, sec.
    - Overrides :meth:`_set_maximum_column_dimensions` method to set
      design-class specific maximum column dimensions.
    - Overrides :meth:`_change_materials` method to use design-class
      specific material change order.

    References
    ----------
    REBA (1967). Regulamento de Estruturas de Betão Armado.
    Decreto N.° 47:723, Lisbon, Portugal.
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
        # Initialise the structure
        super().__init__(taxonomy=taxonomy)
        # Set the maximum column dimensions for full design routine
        self._set_maximum_column_dimensions()

    def _set_maximum_column_dimensions(self) -> None:
        """Set the maximum column dimensions based on number of storeys
        and seismic input.

        Notes
        -----
        The limitations based on engineering judgement. They can be changed.
        In case they are independent from such parameters, these can be
        set within column object as similar to the minimum dimension.
        """
        for column in self.columns:
            if self.num_storeys <= 3:
                if self.beta < 0.20:
                    column.MAX_B_SQUARE = 0.45 * m
                    column.MAX_B_RECTANGLE = 0.70 * m
                else:
                    column.MAX_B_SQUARE = 0.60 * m
                    column.MAX_B_RECTANGLE = 0.80 * m
            elif self.num_storeys <= 6:
                if self.beta < 0.20:
                    column.MAX_B_SQUARE = 0.60 * m
                    column.MAX_B_RECTANGLE = 1.00 * m
                else:
                    column.MAX_B_SQUARE = 0.80 * m
                    column.MAX_B_RECTANGLE = 1.20 * m
            elif self.num_storeys <= 9:
                if self.beta < 0.20:
                    column.MAX_B_SQUARE = 0.80 * m
                    column.MAX_B_RECTANGLE = 1.20 * m
                else:
                    column.MAX_B_SQUARE = 1.00 * m
                    column.MAX_B_RECTANGLE = 1.40 * m

    def _change_materials(self) -> None:
        """The method used for changing materials in iterative design
        algorithm.

        Notes
        -----
        It is overwritten for eu_cdm design class with following changes:
        - The method is modified such that steel and concrete materials
        is not updated simultaneously in the same iteration. Instead,
        they were updated following a specific order based on the current
        concrete or steel material.
        """
        if self.steel.grade == 'A24':
            self.steel = self.next_steel
        elif self.concrete.grade in ['B180', 'B225']:
            self.concrete = self.next_concrete
        elif self.steel.grade == 'A40':
            self.steel = self.next_steel
        elif self.next_concrete:
            self.concrete = self.next_concrete
        elif self.next_steel:
            self.steel = self.next_steel
