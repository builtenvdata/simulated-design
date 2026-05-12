"""This module provides the class implementations representing materials for
the ``tr_7599`` design class in the BDIM layer.
"""
# Imports from installed packages
from pathlib import Path
from typing import List, Optional, Type

# Imports from bdim base library
from ..baselib.materials import (ConcreteBase, SteelBase,
                                 MaterialDataBase, MaterialsBase)


class Steel(SteelBase):
    """Steel model implementation for design class ``tr_7599``.

    This class extends ``SteelBase`` by overriding partial factor attribute.

    Attributes
    ----------
    PARTIAL_FACTOR : float
        Partial factor for steel, by default 1.15.

    See Also
    --------
    :class:`~bdim.baselib.materials.SteelBase`
        Base class defining the core behaviour and configuration.
    """
    PARTIAL_FACTOR: float = 1.15


class Concrete(ConcreteBase):
    """Concrete model implementation for design class ``tr_7599``.

    This class extends ``ConcreteBase`` by adding the cubic specimen
    compressive strength attribute and overriding partial factor attribute.

    Attributes
    ----------
    PARTIAL_FACTOR : float
        Partial factor for concrete, by default 1.5.

    See Also
    --------
    :class:`~bdim.baselib.materials.ConcreteBase`
        Base class defining the core behaviour and configuration.
    """
    PARTIAL_FACTOR: float = 1.5


class MaterialData(MaterialDataBase):
    """Materials data model implementation for design class ``tr_7599``.

    This class extends ``MaterialDataBase`` by narrowing the attribute types.

    Attributes
    ----------
    concrete : List[Concrete]
        List of concrete materials.
    steel : List[Steel]
        List of steel materials.

    See Also
    --------
    :class:`~bdim.baselib.materials.MaterialDataBase`
        Base class defining the core behaviour and configuration.
    """
    concrete: List[Concrete]
    steel: List[Steel]


class Materials(MaterialsBase):
    """Materials implementation for design class ``tr_7599``.

    This class extends ``MaterialsBase`` by narrowing the attribute types and
    exposing public accessors for retrieving concrete and steel material
    instances by grade.

    Attributes
    ----------
    concrete : List[Concrete]
        List of concrete material instances.
    steel : List[Steel]
        List of steel material instances.
    _data_path : Path
        Path to the JSON file containing material data.

    See Also
    --------
    :class:`~bdim.baselib.materials.MaterialsBase`
        Base class defining the core behaviour and configuration.
    """
    concrete: List[Concrete]
    steel: List[Steel]
    _data_path = Path(__file__).parent / 'data' / 'materials.json'
    _data_blueprint: Type[MaterialData] = MaterialData

    def get_steel(self, grade: str) -> Optional[Steel]:
        """
        Find and return the steel material instance with the specified grade.

        Parameters
        ----------
        grade : str
            grade or identifier of the steel material to find.

        Returns
        -------
        Steel or None
            The steel material instance with the specified grade, if found;
            otherwise None.
        """
        return super()._get_steel(grade)

    def get_concrete(self, grade: str) -> Optional[Concrete]:
        """
        Find and return the concrete material instance with the specified
        grade.

        Parameters
        ----------
        grade : str
            grade or identifier of the concrete material to find.

        Returns
        -------
        Concrete or None
            The concrete material instance with the specified grade, if found;
            otherwise None.
        """
        return super()._get_concrete(grade)

    def get_next_concrete(self, concrete: Concrete) -> Concrete:
        """
        Return the concrete material coming after the given.

        Parameters
        ----------
        concrete : ~simdesign.rcmrf.bdim.tr_7599.materials.Concrete
            Current concrete material.

        Returns
        -------
        Concrete or None
            The next concrete material instance if the given is not
            the final option; otherwise None.
        """
        return super()._get_next_concrete(concrete)

    def get_next_steel(self, steel: Steel) -> Steel:
        """
        Return the steel material coming after the given.

        Parameters
        ----------
        steel : ~simdesign.rcmrf.bdim.tr_7599.materials.Steel
            Current steel material.

        Returns
        -------
        Steel or None
            The next steel material instance if the given is not
            the final option; otherwise None.
        """
        return super()._get_next_steel(steel)
