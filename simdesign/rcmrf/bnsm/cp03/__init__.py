"""
**BNSM CP03 Library**

This package provides an instantiable lumped-plasticity modelling strategy
within the Building Nonlinear Structural Model (BNSM), suitable for
performance-based seismic assessment of existing reinforced concrete (RC)
moment-resisting frame buildings. It extends CP01 by explicitly introducing
plastic hinges via zeroLength elements for beams and columns. Furthermore,
rigid joint offsets are defined using rigid-like elements rather than
geometric transformations.

The classes defined here inherit from the abstract modelling interfaces
in `bnsm.baselib` and extend the CP01 implementations where required,
providing instantiable component implementations.

**Model Characteristics**

- Beam:
  Concentrated plasticity (CP) with explicit zeroLength end hinges
  placed in series with an elastic interior beam element.
  Hinge moment-rotation behaviour follows CP01, with elastic stiffness
  modification according to Ibarra & Krawinkler (2005).

- Column:
  Concentrated plasticity with explicit zeroLengthSection end hinges
  and an elastic interior column element.
  Flexural hinge behaviour follows CP01, with elastic stiffness
  modification according to Ibarra & Krawinkler (2005) and optional
  degrading shear hinges supported through the inherited CP01 Column.

- Joints:
  Rigid joint offsets are modelled explicitly using rigid-like
  elasticBeamColumn elements, rather than through geometric transformations
  applied to beam-column elements. Beam-column joint springs may be defined as
  rigid, elastic, or inelastic, consistent with CP01.

- Infill:
  Equivalent diagonal strut macro-model for masonry infills
  (identical to CP01).

- Floor Diaphragm:
  Rigid diaphragm modelling via retained node and multi-point constraints
  (identical to the base implementation).

- Foundation:
  Lumped fixed support node (identical to the base implementation).

- Building:
  Aggregator class assembling all nonlinear components into a
  unified OpenSees domain. Extends base implementation by introducing auxiliary
  plastic hinge nodes, rigid-like offset elements, and configurable
  series or parallel infill-column shear interaction.

**References**

Ibarra, L. F., & Krawinkler, H. (2005).
Global collapse of frame structures under seismic excitations.
Technical Report 152, Stanford University.
"""

from .building import Building as CP03

__all__ = ['CP03']
