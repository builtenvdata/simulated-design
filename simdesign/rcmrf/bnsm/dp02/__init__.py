"""
**BNSM DP02 Library**

This package provides an instantiable distributed-plasticity (DP)
modelling strategy within the Building Nonlinear Structural Model (BNSM),
suitable for nonlinear seismic assessment of reinforced concrete (RC)
moment-resisting frame buildings.

DP02 extends the base beam and column implementations by introducing
O’Reilly (2016)-based calibrated moment-curvature relationships for
plastic hinge regions, while retaining force-based beam-column elements
with distributed plasticity over a finite plastic hinge length defined in
the base implementation.

**Model Characteristics**

- Beam:
  Distributed plasticity formulation using forceBeamColumn elements
  with Pinching4-based moment-curvature hinges at both ends following
  O’Reilly (2016). The hinge sections have elastic axial, torsional and
  weak-axis flexural materials, and all sections an elastic shear
  material with the gross shear stiffness.

- Column:
  Distributed plasticity formulation using forceBeamColumn elements
  with Pinching4-based moment-curvature hinges about both axes following
  O’Reilly (2016), and elastic axial and torsional materials. Shear
  materials act along the whole member: degrading shear springs (Zimos et
  al., 2015) for columns without capacity design for shear, elastic
  materials with the gross shear stiffness otherwise.

- Joints:
  Rigid, elastic, or inelastic rotational spring models
  (identical to the base implementation).

- Infill:
  Equivalent diagonal strut macro-model calibrated based on
  O’Reilly (2016).

- Floor Diaphragm:
  Rigid diaphragm modelling via retained node and multi-point constraints
  (identical to the base implementation).

- Foundation:
  Lumped fixed support node (identical to the base implementation).

- Building:
  Aggregator class assembling all nonlinear components into a
  unified OpenSees domain without modification of base assembly logic.

**References**

O'Reilly, G. J. (2016).
Performance-based seismic assessment and retrofit of existing
RC frame buildings in Italy (Doctoral dissertation, IUSS Pavia).
"""

from .building import Building as DP02

__all__ = ['DP02']
