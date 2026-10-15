"""
**BNSM DP03 Library**

This package provides an instantiable distributed-plasticity (DP)
modelling strategy within the Building Nonlinear Structural Model (BNSM),
suitable for nonlinear seismic assessment of reinforced concrete (RC)
moment-resisting frame buildings.

DP03 extends the base beam and column implementations by introducing
explicit fiber-section modelling, incorporating concrete confinement effects
and reinforcement detailing. Force-based beam-column elements with plastic
hinge integration over a finite plastic hinge length are retained from the
base implementation. The interior sections are fiber sections by default
(``interior_section='Inelastic'``) or elastic.

**Model Characteristics**

- Beam:
  Distributed plasticity formulation using forceBeamColumn elements
  with fiber-discretized sections. Concrete confinement is modelled
  using the Mander model (Mander et al., 1988) with ``Concrete04``, or
  the modified Kent and Park model with ``Concrete01``, and reinforcing
  steel includes MinMax strain limits to simulate bar buckling or rupture
  (Priestley et al., 2007). All sections are aggregated with an elastic
  shear material with the gross shear stiffness.

- Column:
  Distributed plasticity formulation using forceBeamColumn elements
  with fiber-discretized sections capturing axial-flexure interaction.
  Confinement and steel modelling are consistent with the beam formulation.
  The sections are aggregated with shear materials along the whole member:
  degrading shear springs (Zimos et al., 2015) for columns without
  capacity design for shear, elastic materials with the gross shear
  stiffness otherwise.

- Joints:
  Rigid, elastic, or inelastic rotational spring models
  (identical to base implementation).

- Infill:
  Equivalent diagonal strut macro-model
  (identical to base implementation).

- Floor Diaphragm:
  Rigid diaphragm modelling via retained node and multi-point constraints
  (identical to base implementation).

- Foundation:
  Lumped fixed support node
  (identical to base implementation).

- Building:
  Aggregator class assembling all nonlinear components into a
  unified OpenSees domain without modification of base assembly logic.

**References**

Priestley, M. J. N., Calvi, G. M., & Kowalsky, M. J. (2007).
*Displacement-based seismic design of structures*. IUSS Press.

Mander, J. B., Priestley, M. J. N., & Park, R. (1988).
Theoretical stress-strain model for confined concrete.
Journal of Structural Engineering, 114(8), 1804-1826.

Zimos, D. K., Mergos, P. E., & Kappos, A. J. (2015). Shear hysteresis
model for reinforced concrete elements including the post-peak range.
Proceedings of the COMPDYN. https://doi.org/10.7712/120115.3565.1184
"""

from .building import Building as DP03

__all__ = ['DP03']
