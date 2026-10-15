"""
**BNSM DP04 Library**

This package provides an instantiable distributed-plasticity (DP)
modelling strategy within the Building Nonlinear Structural Model (BNSM),
suitable for nonlinear seismic assessment of reinforced concrete (RC)
moment-resisting frame buildings.

DP04 combines the DP01 beams with the DP03 fiber-section columns, which
have an elastic interior section by default. The remaining components are
inherited without modification.

**Model Characteristics**

- Beam:
  Distributed plasticity formulation using forceBeamColumn elements
  with Hysteretic moment-curvature hinges (identical to DP01).

- Column:
  Distributed plasticity formulation using forceBeamColumn elements
  with fiber-discretized hinge sections and shear materials (identical to
  DP03), with the interior section set to 'Elastic' by default.

- Joints:
  Rigid, elastic, or inelastic rotational spring models
  (identical to the base implementation).

- Infill:
  Equivalent diagonal strut macro-model
  (identical to the base implementation).

- Floor Diaphragm:
  Rigid diaphragm modelling via retained node and multi-point constraints
  (identical to the base implementation).

- Foundation:
  Lumped fixed support node
  (identical to the base implementation).

- Building:
  Aggregator class assembling all nonlinear components into a unified
  OpenSees domain without modification of the base assembly logic.
"""

from .building import Building as DP04

__all__ = ['DP04']
