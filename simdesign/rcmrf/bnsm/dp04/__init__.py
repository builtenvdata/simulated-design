"""
**BNSM DP04 Library**

This package provides an instantiable distributed-plasticity (DP)
modelling strategy within the Building Nonlinear Structural Model (BNSM),
suitable for nonlinear seismic assessment of reinforced concrete (RC)
moment-resisting frame buildings.

DP04 is a DP03-derived variant that retains the distributed-plasticity
framework and fiber-hinge column formulation, while adopting an elastic
interior section for columns. Beam modelling follows the base beam
implementation, and the remaining components are inherited without
modification.

**Model Characteristics**

- Beam:
  Distributed plasticity formulation using forceBeamColumn elements
  with plastic hinge integration and aggregated section behaviour
  (identical to the base implementation).

- Column:
  Distributed plasticity formulation using forceBeamColumn elements
  with fiber-discretized hinge sections inherited from DP03.
  The interior section is set to 'Elastic' by default, while optional
  degrading shear behaviour is retained from the base implementation.

- Beam:
  Distributed-plasticity beam formulation inherited directly from the
  base implementation (identical to the base implementation).

- Column:
  Fiber-hinge distributed-plasticity column formulation inherited from
  DP03, with the interior section set to 'Elastic' by default.

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
