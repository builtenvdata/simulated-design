"""
**BDIM EuCDL Library**

This package provides a Design Class Constructor (DCC) for defining the
Building Design Information Model (BDIM) of reinforced concrete (RC)
frame buildings corresponding to the European design class ``eu_cdl``.
It includes component implementations that inherit from the abstract
design interfaces defined in ``bdim.baselib``.

The ``EuCDL`` class represents RC buildings constructed in Europe during
the 1960s and 1970s, designed under early seismic codes that introduced
lateral loads distributed proportionally to floor weights. Structural design
follows the material-specific provisions of REBA-1967, based on allowable
stress design and the stress-block method (Guerrin, 1966). These rules trace
back to the 1963 guidelines of the Comité Européen du Béton (CEB), making this
standard broadly representative of European practice of that era.

**References**

Comité Européen du Béton, CEB (1963). Recommandations Pratiques à l'Usage des
Constructeurs.
fib - International Federation for Structural Concrete, Lausanne, Switzerland.

Guerrin, A. (1966). Traité de Béton Armé.
Dunod, Paris, France.

REBA (1967). Regulamento de Estruturas de Betão Armado.
Decreto N.° 47:723, Lisbon, Portugal.
"""

from .building import Building as EuCDL

__all__ = ["EuCDL"]
