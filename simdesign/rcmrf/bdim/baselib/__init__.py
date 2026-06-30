"""
**BDIM Base Library**

This package provides the abstract design interfaces of the Building Design
Information Model (BDIM). It defines the abstract base class implementations
that must be inherited by design class-specific implementations
(e.g., ``eu_cdh``, ``eu_cdm``, ``tr_0018_dch``, ``tr_post18_dcm``).

While higher-level BDIM packages provide instantiable component
implementations, ``baselib`` establishes the abstract definitions of these
components that bridge the taxonomy data and the design layer. The architecture
is described in Ozsarac et al. 2025.

This package is intentionally abstraction-focused to allow flexible
extension to new design class-specific implementations as proposed
by Ozsarac et al. 2025 for European RC frame buildings and
by Hasanoğlu et al. 2025 for Turkish RC frame buildings.

References
----------
Ozsarac, V., Pereira, N., Mohamed, H., Romão, X., & O'Reilly, G. J. (2025).
The Built Environment Data Framework for Simulated Design and Vulnerability
Modelling in Earthquake Engineering. Earthquake Engineering & Structural
Dynamics, 54(11), 2651-2670. https://doi.org/10.1002/eqe.4378

Hasanoğlu, S., Ozsarac, V., & O'Reilly, G. J. (2025). A model for the
simulated design of Turkish RC frame buildings in seismic vulnerability
analysis. Bulletin of Earthquake Engineering, 23(15), 6829-6856.
https://doi.org/10.1007/s10518-025-02301-y
"""

from .analysis import ElasticModelBase
from .beam import BeamBase, BeamForces, BeamEnvelopeForces
from .building import BuildingBase, TaxonomyData
from .column import ColumnBase, ColumnForces, ColumnEnvelopeForces
from .infill import InfillBase
from .joint import JointBase
from .loads import (
    LoadsBase, LoadsDataBase, VariableBase, PermanentBase, CombinationBase
    )
from .materials import SteelBase, ConcreteBase, MaterialsBase, MaterialDataBase
from .quality import QualityBase, QualityData, QualityModelData
from .rebars import RebarsBase, RebarData
from .slab import SlabBase
from .stairs import StairsBase

__all__ = [
    'ElasticModelBase',
    'BeamBase', 'BeamForces', 'BeamEnvelopeForces',
    'BuildingBase', 'TaxonomyData',
    'ColumnBase', 'ColumnForces', 'ColumnEnvelopeForces',
    'InfillBase',
    'JointBase',
    'LoadsBase', 'LoadsDataBase',
    'VariableBase', 'PermanentBase', 'CombinationBase',
    'SteelBase', 'ConcreteBase', 'MaterialsBase', 'MaterialDataBase',
    'QualityBase', 'QualityData', 'QualityModelData',
    'RebarsBase', 'RebarData',
    'SlabBase',
    'StairsBase',
]
