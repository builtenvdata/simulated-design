"""
**BNSM DP01 Library**

This package provides an instantiable distributed-plasticity (DP)
modelling strategy within the Building Nonlinear Structural Model (BNSM),
suitable for nonlinear seismic assessment of reinforced concrete (RC)
moment-resisting frame buildings.

The classes defined here inherit directly from the base implementations
in `bnsm.baselib`. Accordingly, for beams and columns, DP01 employs force-based
beam-column elements with distributed plasticity over a finite plastic-hinge
length computed in accordance with Priestley et al. (2007).

**Model Characteristics**

- Beam:
  Distributed plasticity formulation using forceBeamColumn elements
  with plastic hinge integration and aggregated section behaviour
  (identical to the base implementation).

- Column:
  Distributed plasticity formulation using forceBeamColumn elements
  with aggregated flexural and optional degrading shear behaviour
  (identical to the base implementation).

- Joints:
  Rigid, elastic, or inelastic rotational spring models
  (identical to the base implementation).

- Infill:
  Equivalent diagonal strut macro-model for masonry infills
  (identical to the base implementation).

- Floor Diaphragm:
  Rigid diaphragm modelling via retained node and multi-point constraints
  (identical to the base implementation).

- Foundation:
  Lumped fixed support node (identical to the base implementation).

- Building:
  Aggregator class assembling all nonlinear components into a
  unified OpenSees domain without modification of base behaviour.

**References**

Priestley, M. J. N., Calvi, G. M., & Kowalsky, M. J. (2007).
*Displacement-based seismic design of structures*.
IUSS Press.
"""

from .building import Building as DP01

__all__ = ['DP01']
