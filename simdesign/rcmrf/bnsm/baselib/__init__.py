"""
**BNSM Base Library**

This package provides the abstract modelling interfaces of the
Building Nonlinear Structural Model (BNSM). It defines the
component-level architecture and modelling contracts used by
nonlinear model implementations (e.g., DP01, CP01).

While higher-level BNSM packages provide instantiable component
implementations, ``baselib`` establishes the abstract definitions of
these components that bridge the BDIM design layer and the OpenSees
analysis domain.

This package is intentionally abstraction-focused to allow flexible
extension, alternative modelling strategies, and future nonlinear
formulations.

**Modelling Strategy**

The modelling philosophy is component-based and macro-model oriented,
suitable for nonlinear seismic analysis of reinforced concrete (RC)
frame buildings.

The base components defined here include:

- Beam and Column:
  Abstract beam-column interfaces supporting plastic-hinge material
  formulations and section aggregation strategies.

- Joints:
  Abstract joint representations supporting rigid, elastic,
  or inelastic rotational spring modelling.

- Infill:
  Abstract equivalent diagonal strut interface for masonry panels.

- Floor Diaphragm:
  Interface for rigid diaphragm constraints.

- Foundation:
  Base support node representation (extendable for SSI).

- Node:
  Structural node abstraction with optional translational masses.
"""

from .building import BuildingBase

__all__ = ['BuildingBase']
