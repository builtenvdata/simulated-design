"""
**BDIM Tr0018DCH Library**

This package provides a Design Class Constructor (DCC) for defining the
Building Design Information Model (BDIM) of reinforced concrete (RC)
frame buildings corresponding to the Turkish design class ``tr_0018_dch``.
It includes component implementations that inherit from the abstract
design interfaces defined in ``bdim.baselib``.

The ``Tr0018DCH`` class represents buildings constructed between 2000 and 2018,
and designed with a **high ductility level (DCH)**. This implies the
application of capacity design principles to ensure ductile global behavior,
including strong-column weak-beam hierarchy and detailing requirements for
plastic hinge regions. The design rules implemented in this class are
primarily based on TBEC-1998, which remained largely consistent for RC frame
design in TBEC-2007, together with relevant provisions from TS500-2000.

**References**

TBEC (1998). *Afet Bölgelerinde Yapılacak Yapılar Hakkında Yönetmelik*.
Resmi Gazete, Ankara, Türkiye.

TBEC (2007). *Deprem Bölgelerinde Yapılacak Binalar Hakkında Esaslar*.
Resmi Gazete, Ankara, Türkiye.

TS500 (2000). *Requirements for Design and Construction of Reinforced
Concrete Structures*. Turkish Standards Institution (TSE), Ankara, Türkiye.
"""

from .building import Building as Tr0018DCH

__all__ = ["Tr0018DCH"]
