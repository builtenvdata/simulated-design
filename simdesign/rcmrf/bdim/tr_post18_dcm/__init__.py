"""
**BDIM TrPost18DCM Library**

This package provides a Design Class Constructor (DCC) for defining the
Building Design Information Model (BDIM) of reinforced concrete (RC)
frame buildings corresponding to the Turkish design class ``tr_0018_dcm``.
It includes component implementations that inherit from the abstract
design interfaces defined in ``bdim.baselib``.

The ``TrPost18DCM`` class represents RC frame buildings constructed
after 2018, designed according to the provisions of TBEC-2018 together with
relevant requirements from TS500-2000. This class corresponds to **moderate
ductility level (DCM)** systems. Compared to high ductility systems, these
buildings follow simplified seismic detailing and do not enforce capacity
design principles. As a result, strength hierarchy rules (e.g., strong-column
weak-beam) and confinement requirements are less stringent. In this design
class, seismic code provisions (TBEC-2018) take precedence over TS500
requirements when determining design parameters.

**References**

TBEC (2018). *Deprem Etkisi Altında Binaların Tasarımı için Esaslar*.
Resmi Gazete, Türkiye.

TS500 (2000). *Requirements for Design and Construction of Reinforced
Concrete Structures*. Turkish Standards Institution (TSE), Ankara, Türkiye.
"""

from .building import Building as TrPost18DCM

__all__ = ["TrPost18DCM"]
