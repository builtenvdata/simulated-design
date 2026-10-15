"""
**BNSM CP01 Library**

This package provides a calibrated concentrated plasticity (CP)
modelling strategy within the Building Nonlinear Structural Model (BNSM),
suitable for performance-based seismic assessment of existing reinforced
concrete (RC) frame buildings. It contains instantiable component
implementations that inherit from the abstract modelling interfaces
provided by `bnsm.baselib`.

**Model Characteristics**

- Beam:
  Concentrated plasticity (CP) with end hinges (Haselton et al., 2008)
  defined using Hysteretic moment-rotation behaviour, in forceBeamColumn
  elements with ConcentratedPlasticity integration. The interior is nearly
  rigid in flexure, so the hinges, calibrated to the chord rotation of the
  member, carry the whole flexural flexibility. The hinge sections have
  elastic axial, torsional and weak-axis flexural materials.

- Column:
  Concentrated plasticity (Haselton et al., 2008) about both axes, as for
  the beams. Columns without capacity design for shear have degrading
  shear springs: LimitState materials coupled with ThreePoint limit curves
  (Elwood & Moehle, 2003), with the ASCE 41-17 shear strength and the
  post-failure slope of Shoraka & Elwood (2013).

- Joints:
  Rigid, elastic, or inelastic rotational spring models
  based on O’Reilly (2016).

- Infill:
  Equivalent diagonal strut macro-model for masonry infills
  (Crowley et al., 2021).

- Floor Diaphragm:
  Rigid diaphragm modelling via retained node and multi-point constraints.

- Foundation:
  Lumped fixed support node.

- Building:
  Aggregator class assembling all nonlinear components into a
  unified OpenSees domain without modification of base behaviour.

**References**

Haselton, C. B., Liel, A. B., Lange, S. T., & Deierlein, G. G. (2008).
Beam-column element model calibrated for predicting flexural response
leading to global collapse of RC frame buildings.
Pacific Earthquake Engineering Research Center,
University of California, Berkeley, CA.

Elwood, K. J., & Moehle, J. P. (2003).
Shake table tests and analytical studies on the gravity load collapse
of reinforced concrete frames.
PEER Report 2003/01.
Pacific Earthquake Engineering Research Center,
University of California, Berkeley.

ASCE/SEI 41-17. (2017). Seismic rehabilitation of existing buildings.
American Society of Civil Engineers.

Shoraka, M. B., & Elwood, K. J. (2013). Mechanical model for non ductile
reinforced concrete columns. Journal of Earthquake Engineering, 17(7),
937-957.

O'Reilly, G. J. (2016).
Performance-based seismic assessment and retrofit of existing
RC frame buildings in Italy (Doctoral dissertation, IUSS Pavia).

Crowley, H. M., Dabbeek, J., Despotaki, V., Rodrigues, D., Martins, L.,
Silva, V., Romão, X., Pereira, N., Weatherill, G. A., & Danciu, L. (2021).
European Seismic Risk Model (ESRM20).
EFEHR Technical Report 002.
https://doi.org/10.7414/EUC-EFEHR-TR002-ESRM20
"""

from .building import Building as CP01

__all__ = ['CP01']
