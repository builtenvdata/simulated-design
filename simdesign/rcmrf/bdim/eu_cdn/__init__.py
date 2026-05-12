"""
**BDIM EuCDN Library**

This package provides a Design Class Constructor (DCC) for defining the
Building Design Information Model (BDIM) of reinforced concrete (RC)
frame buildings corresponding to the European design class ``eu_cdn``.
It includes component implementations that inherit from the abstract
design interfaces defined in ``bdim.baselib``.

The ``EuCDN`` class refers to older structures constructed before
the 1960s, designed only for gravity loads using the allowable stress
method and typically employing low-strength materials. The design rules
from RBA (1935) are adopted herein as representative of European
practice at the time. As noted in the standard, its rules were informed
by regulations, standards and guidelines from countries such as Austria,
Belgium, Denmark, Germany, Hungary, Italy, Sweden and Switzerland,
published between 1924 and 1933.

**References**

RBA (1935). *Regulamento do Betão Armado*.
Decreto N.° 25:948, Lisbon, Portugal.
"""

from .building import Building as EuCDN

__all__ = ["EuCDN"]
