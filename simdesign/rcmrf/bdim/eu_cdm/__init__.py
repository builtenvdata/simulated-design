"""
**BDIM EuCDM Library**

This package provides a Design Class Constructor (DCC) for defining the
Building Design Information Model (BDIM) of reinforced concrete (RC)
frame buildings corresponding to the European design class ``eu_cdm``.
It includes component implementations that inherit from the abstract
design interfaces defined in ``bdim.baselib``.

The ``EuCDM`` class represents RC buildings constructed in Europe during
the 1970s to 2000s, designed under limit state design principles, incorporating
ultimate strength, partial safety factors, and improved detailing rules to
enhance global ductility. Structural design follows the provisions of
REBAP-1983, which distributes seismic lateral loads as a function of both
floor weights and storey heights. These rules trace back to the two-volume
recommendations published in 1978 by the Comité Européen du Béton (CEB),
which include the 1978 CEB-FIP Model Code and influenced the evolution of
reinforced concrete design regulations across Europe. Therefore, REBAP-1983
is also assumed to be broadly representative of European practice at the time.

**References**

REBAP (1983). Regulamento de Estruturas de Betão Armado e Pré-Esforçado.
Decreto-Lei N.° 349-C/83, Lisbon, Portugal.

d'Arga e Lima, J., Monteiro, V., and Mun, M. (2005). Betão Armado — Esforços
Normais e de Flexão (REBAP-83).
Laboratório Nacional de Engenharia Civil, Lisbon, Portugal.

Comité Européen du Béton, CEB (1978). Système International de Réglementation
Technique Unifiée des Structures, Vol. 1 — Règles Unifiées Communes.
fib - International Federation for Structural Concrete, Lausanne, Switzerland.

Comité Européen du Béton, CEB (1978). Système International de Réglementation
Technique Unifiée des Structures, Vol. 2 — Code-Modèle CEB-FIP pour les
Structures en Béton.
fib - International Federation for Structural Concrete, Lausanne, Switzerland.
"""

from .building import Building as EuCDM

__all__ = ["EuCDM"]
