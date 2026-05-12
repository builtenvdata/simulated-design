"""
**BDIM EuCDH Library**

This package provides a Design Class Constructor (DCC) for defining the
Building Design Information Model (BDIM) of reinforced concrete (RC)
frame buildings corresponding to the European design class ``eu_cdh``.
It includes component implementations that inherit from the abstract
design interfaces defined in ``bdim.baselib``.

The ``EuCDH`` class represents RC buildings designed under contemporary
seismic practices in Europe (early 2000s to present), implementing capacity
design principles and reinforcement detailing aimed at achieving specific
ductility levels. Structural design follows the Eurocode provisions for
ductility class medium (DCM), assumed to reflect the most commonly adopted
ductility class in Europe.

**References**

Comité Européen de Normalisation, CEN (2004). Eurocode 2: Design of Concrete
Structures — Part 1-1: General Rules and Rules for Buildings.
European Committee for Standardization, Brussels, Belgium.

Comité Européen de Normalisation, CEN (2004). Eurocode 8: Design of Structures
for Earthquake Resistance — Part 1: General Rules, Seismic Actions and Rules
for Buildings.
European Committee for Standardization, Brussels, Belgium.

d'Arga e Lima, J., Monteiro, V., Mun, M. (2005).
Betão armado: esforços normais e de flexão: REBAP-83.
Laboratório Nacional de Engenharia Civil, Lisboa.
"""

from .building import Building as EuCDH

__all__ = ["EuCDH"]
