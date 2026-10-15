"""
**BNSM DP01 Library**

This package provides an instantiable distributed-plasticity (DP)
modelling strategy within the Building Nonlinear Structural Model (BNSM),
suitable for nonlinear seismic assessment of reinforced concrete (RC)
moment-resisting frame buildings.

The classes defined here inherit from the base implementations in
`bnsm.baselib`. For beams and columns, DP01 employs force-based beam-column
elements with distributed plasticity over a finite plastic-hinge length
computed in accordance with Priestley et al. (2007).

**Model Characteristics**

- Beam:
  Distributed plasticity formulation using forceBeamColumn elements
  with plastic hinge integration. The Hysteretic moment-curvature hinges
  reach the EN 1998-3 yield rotation (including its shear and bond-slip
  terms) together with the elastic interior. The hinge sections have
  elastic axial, torsional and weak-axis flexural materials.

- Column:
  Distributed plasticity formulation using forceBeamColumn elements
  with aggregated sections: Hysteretic moment-curvature hinges about both
  axes, as for the beams, and elastic axial and torsional materials.
  Columns without capacity design for shear have degrading shear springs
  (Zimos et al., 2015) along the whole member; in capacity-designed
  columns the shear deformation is included through the yield rotation.

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

Zimos, D. K., Mergos, P. E., & Kappos, A. J. (2015). Shear hysteresis
model for reinforced concrete elements including the post-peak range.
Proceedings of the COMPDYN. https://doi.org/10.7712/120115.3565.1184
"""

from .building import Building as DP01

__all__ = ['DP01']
