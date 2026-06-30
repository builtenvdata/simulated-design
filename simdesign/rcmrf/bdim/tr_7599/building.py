"""This module provides the Building Design Information Model (BDIM)
implementation for the ``tr_7599`` design class.
"""
# Imports from installed packages
from typing import List, Type

# Imports from the design class (tr_7599) library
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
    """BDIM implementation for design class ``tr_7599``.

    This class extends ``BuildingBase`` by narrowing the attribute types
    to the ``tr_7599`` implementations and overriding design class-specific
    methods.

    Attributes
    ----------
    beams : List[~simdesign.rcmrf.bdim.tr_7599.beam.Beam]
        List of beam instances.
    columns : List[~simdesign.rcmrf.bdim.tr_7599.column.Column]
        List of column instances.
    joints : List[~simdesign.rcmrf.bdim.tr_7599.joint.Joint]
        List of joint instances.
    slabs : List[~simdesign.rcmrf.bdim.tr_7599.slab.Slab]
        List of slab instances.
    stairs : List[~simdesign.rcmrf.bdim.tr_7599.stairs.Stairs]
        List of stairs instances.
    infills : List[~simdesign.rcmrf.bdim.tr_7599.infill.Infill]
        List of infill wall instances.
    steel : ~simdesign.rcmrf.bdim.tr_7599.materials.Steel
        Steel material instance used in the design of beams and columns.
    concrete : ~simdesign.rcmrf.bdim.tr_7599.materials.Concrete
        Concrete material instance used in the design of beams and columns.
    loads : ~simdesign.rcmrf.bdim.tr_7599.loads.Loads
        Loads instance used to apply building loads.
    materials : ~simdesign.rcmrf.bdim.tr_7599.materials.Materials
        Materials instance used to set building materials.
    rebars : ~simdesign.rcmrf.bdim.tr_7599.rebars.Rebars
        Rebars instance used to determine reinforcement arrangement.
    quality : ~simdesign.rcmrf.bdim.tr_7599.quality.Quality
        Quality instance used to adjust properties of structural elements.

    See Also
    --------
    :class:`~simdesign.rcmrf.bdim.baselib.building.BuildingBase`
        Base class defining the core behaviour and configuration.

    Notes
    -----
    - Design follows limit state design approach.
    - Main reference building code is TBEC-1975.
    - Basic units are kN, m, sec
    - Overrides :meth:`_change_beam_type` method to update slab type
      together with beam type.
    - Overrides :meth:`_set_maximum_column_dimensions` method to set
      design-class specific maximum column dimensions.

    References
    ----------
    TBEC (1975). *Afet Bölgelerinde Yapılacak Yapılar Hakkında Yönetmelik*.
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

    def _change_beam_type(self) -> None:
        """The method used for changing beam types.

        Notes
        -----
        Slab type is also updated together with beam type.
        """
        # Change from wide beam to emergent beam
        self.beam_type = 2
        # Change from asmolen slab to oneway or twoway slab
        self._change_slab_type()
