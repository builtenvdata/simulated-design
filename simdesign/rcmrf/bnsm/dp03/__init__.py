"""
**BNSM DP03 Library**

This package provides an instantiable distributed-plasticity (DP)
modelling strategy within the Building Nonlinear Structural Model (BNSM),
suitable for nonlinear seismic assessment of reinforced concrete (RC)
moment-resisting frame buildings.

DP03 extends the base beam and column implementations by introducing
explicit fiber-section modelling at plastic hinge regions, incorporating
concrete confinement effects and reinforcement detailing. Force-based
beam-column elements with distributed plasticity over a finite plastic
hinge length are retained from the base implementation.

**Model Characteristics**

- Beam:
  Distributed plasticity formulation using forceBeamColumn elements
  with fiber-discretized end sections. Concrete confinement is modelled
  using the Mander model (Mander et al., 1988), and reinforcing steel
  includes MinMax strain limits to simulate bar buckling or rupture
  (Priestley et al., 2007). Optional elastic or inelastic interior
  sections are supported.

- Column:
  Distributed plasticity formulation using forceBeamColumn elements
  with fiber-discretized end sections capturing axial-flexure interaction.
  Confinement and steel modelling are consistent with the beam formulation.
  Optional degrading shear behaviour is retained from the base implementation.

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
"""

from .building import Building as DP03

__all__ = ['DP03']
