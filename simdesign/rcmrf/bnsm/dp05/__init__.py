"""
**BNSM DP05 Library**

This package provides an instantiable distributed-plasticity (DP)
modelling strategy within the Building Nonlinear Structural Model (BNSM),
suitable for nonlinear seismic assessment of reinforced concrete (RC)
moment-resisting frame buildings.

DP05 is DP03 (fiber-section beams and columns) with an axial release at one
end of each beam. The rigid floor diaphragm enforces zero axial strain in the
beams, whereas the axis of an RC beam with fiber sections elongates as the
section cracks and yields (the neutral axis moves towards the compression
face). With the diaphragm, this elongation is restrained and the beams
develop fictitious axial compression, which increases their flexural
strength and stiffness. In DP05, the beam frames into an auxiliary node at
its end section (*j-end*), connected to the joint by a ``zeroLength``
element that is nearly free along the beam axis (a soft elastic spring) and
rigid in the other degrees of freedom (an axial buffer element), so the beams
can elongate practically freely.

**Model Characteristics**

- Beam:
  As DP03 (force-based elements with fiber end sections), with an axial
  release at the *j-end*. The beams carry practically no axial force.

- Column, Joints, Infill, Floor Diaphragm, Foundation:
  Identical to DP03.

- Building:
  Aggregator class assembling all nonlinear components into a unified
  OpenSees domain. Extends the DP03 assembly by connecting the *j-end* of
  each beam to an auxiliary node through the axial release.

**References**

Priestley, M. J. N., Calvi, G. M., & Kowalsky, M. J. (2007).
*Displacement-based seismic design of structures*. IUSS Press.

Mander, J. B., Priestley, M. J. N., & Park, R. (1988).
Theoretical stress-strain model for confined concrete.
Journal of Structural Engineering, 114(8), 1804-1826.

OpenSees Wiki. Rigid Diaphragm Consequences.
https://opensees.berkeley.edu/wiki/index.php/Rigid_Diaphragm_Consequences
"""

from .building import Building as DP05

__all__ = ['DP05']
