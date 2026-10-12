"""
**BNSM CP02 Library**

This package provides an alternative concentrated plasticity (CP)
modelling strategy within the Building Nonlinear Structural Model (BNSM).
It extends the CP01, by adopting energy-based hysteretic plastic hinge models
for beams and columns, following the work of Hasanoglu and O'Reilly (2027).

The classes defined here inherit from the abstract modelling interfaces
in `bnsm.baselib` and extend the CP01 implementations where required,
providing instantiable component implementations.

**Model Characteristics**

- Beam:
  Concentrated plasticity with end hinges.
  Plastic hinge moment-rotation behaviour is defined using
  an energy-based HystereticSM material formulation
  (Hasanoglu  and O’Reilly, 2027), replacing the default CP01 hinge model.

- Column:
  Concentrated plasticity with energy-based rotational hinge
  formulation (Hasanoglu  and O’Reilly, 2027).
  Shear and axial interaction behaviour follow CP01.

- Joints:
  Rigid, elastic, or inelastic rotational spring models
  (identical to the base implementation).

- Infill:
  Equivalent diagonal strut macro-model for masonry infills
  (Identical to the base implementation).

- Floor Diaphragm:
  Rigid diaphragm modelling via retained node constraints
  (identical to the base implementation).

- Foundation:
  Lumped fixed support node (identical to the base implementation).

- Building:
  Aggregator class assembling all nonlinear components into a
  unified OpenSees domain without modification of base behaviour.

**References**

Hasanoglu, S. and O'Reilly G. J. (2027). Calibration of cyclic backbone
parameters for numerical modelling and hysteretic energy capacity of
ductile reinforced concrete members.
"""

from .building import Building as CP02

__all__ = ['CP02']
