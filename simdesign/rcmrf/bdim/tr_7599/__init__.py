"""
**BDIM Tr7599 Library**

This package provides a Design Class Constructor (DCC) for defining the
Building Design Information Model (BDIM) of reinforced concrete (RC)
frame buildings corresponding to the Turkish design class ``tr_7599``.
It includes component implementations that inherit from the abstract
design interfaces defined in ``bdim.baselib``.

The ``Tr7599`` class represents RC frame buildings constructed in Türkiye
between 1975 and 1999, designed under the provisions of TBEC-1975 and
TS500-1984. Due to the widespread presence of poor-quality construction in
this period, design outcomes from simulations of this class are adjusted
through a quality-based design modification process. While both the allowable
stress and ultimate strength methods were used during this period, the latter
was implemented in this design class, assuming that the buildings constructed
after the mid-1980s constitute a larger portion of the Turkish RC building
stock (Bal et al. 2008).

**References**

TBEC (1975). *Afet Bölgelerinde Yapılacak Yapılar Hakkında Yönetmelik*.
Resmi Gazete, Ankara, Türkiye.

TS500 (1984). *Requirements for Design and Construction of Reinforced
Concrete Structures*. Turkish Standards Institution (TSE), Ankara, Türkiye.

Bal, I.E., Crowley, H., Pinho, R., and Gülay, F.G. (2008). Detailed Assessment
of Structural Characteristics of Turkish RC Building Stock for Loss Assessment
Models. *Soil Dynamics and Earthquake Engineering*, 28(10-11), 914-932.
https://doi.org/10.1016/j.soildyn.2007.10.005
"""

from .building import Building as Tr7599

__all__ = ["Tr7599"]
