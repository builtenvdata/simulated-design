BCIM inputs
-----------

The ``bcim`` input dictionary controls the generation of the portfolio taxonomy attributes and geometry variables, which are subsequently used in the simulated design process.
The example below illustrates a complete ``bcim`` input dictionary configuration. The individual parameters are described in the sections that follow.

.. important::

   The taxonomy attributes defined by the ``design_class``, ``num_storeys``,
   and ``beta`` parameters must **always be specified by the user**,
   together with the building portfolio size defined by ``sample_size``.
   All other parameters are optional. If not specified,
   default values defined in the design-class configuration files (e.g., ``eu_cdl.json``)
   located in ``simdesign/rcmrf/bcim/data`` are applied automatically.

.. code-block:: json

    {
      "sample_size": 150,
      "seed": 1993,

      "beta": 0.1,
      "num_storeys": 5,
      "design_class": "eu_cdh",

      "exterior_infill_type": {
        "typology": [1, 2, 3],
        "probability": [0.4, 0.4, 0.2]
      },
      "interior_infill_type": {
        "typology": [1, 2, 3],
        "probability": [0.4, 0.4, 0.2]
      },
      "infill_configuration": {
        "configuration": [1, 2, 5, 6],
        "probability": [0.2, 0.2, 0.3, 0.3]
      },

      "typical_storey_height": {
        "cv": 0.07,
        "mu": 2.90,
        "lower_bound": 2.3,
        "upper_bound": 3.8
      },
      "staircase_bay_width": {
        "lower_bound": 2.8,
        "upper_bound": 3.2
      },
      "standard_bay_width": {
        "corr_coeff_xy": -0.92,
        "lower_bound_x": 3.5,
        "upper_bound_x": 7.5,
        "theta_x": 4.5,
        "sigma_x": 0.35,
        "lower_bound_y": 3.5,
        "upper_bound_y": 7.5,
        "theta_y": 4.5,
        "sigma_y": 0.35
      },
      "layout": ["B01", "B04", "B05"],

      "steel": {
        "grade": ["S400", "S500"],
        "probability": [0.10, 0.90]
      },
      "concrete": {
        "grade": ["C20/25", "C25/30", "C30/37", "C35/45"],
        "probability": [0.30, 0.45, 0.20, 0.05]
      },

      "ground_storey_height": {
        "maximum": 4.20,
        "factor": [1.0, 1.1, 1.2, 1.3, 1.4],
        "probability": [0.55, 0.10, 0.20, 0.10, 0.05]
      },

      "construction_quality": {
        "quality": [1, 2, 3],
        "probability": [0.6, 0.3, 0.1]
      },
      "slab_typology": {
        "ss1_prob_given_ss1_or_hs": 0.50,
        "ss2_prob_given_ss2_or_hs": 0.65
      },

      "wb_prob_given_hs": 0.50,
      "square_column_prob": 0.50
    }

Primary Taxonomy Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The parameters in this section are specified by the user and define
the primary taxonomy attributes of the building portfolio.

**beta** (float)
   Design lateral load factor.

**num_storeys** (int)
   Number of storeys in each building.

**design_class** (str)
   Design class identifier (e.g., ``"eu_cdh"``)
   The following design classes are currently available:

   - ``"eu_cdn"``
     Buildings designed without explicit seismic provisions, typically
     constructed before the 1960s for gravity loads only using allowable
     stress methods. Structural design follows the provisions of **RBA-1935**,
     adopted as representative of European practice of the time.

   - ``"eu_cdl"``
     Buildings designed with early seismic provisions (approximately
     1960s-1970s). Lateral loads are considered but design is based on
     allowable stress design and the stress-block method (Guerrin, 1966).
     Structural design follows the provisions of **REBA-1967**, which traces
     back to the **CEB-1963** guidelines and is broadly representative of
     European practice of that era.

   - ``"eu_cdm"``
     Buildings designed according to more modern seismic design codes
     (approximately 1970s-2000s) using limit-state design concepts and
     improved detailing rules to enhance structural ductility. Structural
     design follows the provisions of **REBAP-1983** (d'Arga e Lima et al.,
     2005), which is based on the **CEB-1978** recommendations.

   - ``"eu_cdh"``
     Buildings designed according to contemporary seismic design standards
     (early 2000s-present), implementing capacity design principles and
     reinforcement detailing rules aimed at achieving target ductility levels.
     Structural design follows **EN 1992-1-1:2004** (Eurocode 2) and
     **EN 1998-1:2004** (Eurocode 8), with section design based on
     d'Arga e Lima et al. (2005).

   - ``"tr_7599"``
     Buildings constructed between **1975 and 1999**, designed according to
     **TBEC-1975** and reinforced concrete design provisions in **TS500-1984**.
     This class represents early seismic design practices in Türkiye, often
     associated with relatively low ductility capacity and variable construction
     quality.

   - ``"tr_0018_dcm"``
     Buildings constructed between **2000 and 2018** with **moderate ductility
     level (DCM)**. Designs follow provisions from **TBEC-1998** (largely retained
     in TBEC-2007) together with **TS500-2000** reinforced concrete design rules.
     Capacity design principles are generally not enforced.

   - ``"tr_0018_dch"``
     Buildings constructed between **2000 and 2018** with **high ductility level
     (DCH)**. Designs follow **TBEC-1998 / TBEC-2007** seismic provisions and
     **TS500-2000**, including capacity design principles such as the
     strong-column-weak-beam concept and capacity-based shear design.

   - ``"tr_post18_dcm"``
     Buildings constructed **after 2018** with **moderate ductility level (DCM)**,
     designed according to the **TBEC-2018** seismic code and **TS500-2000**.
     These buildings incorporate updated seismic hazard definitions and improved
     detailing rules introduced in the modern code framework.

   - ``"tr_post18_dch"``
     Buildings constructed **after 2018** with **high ductility level (DCH)**,
     designed according to **TBEC-2018** with full implementation of modern
     capacity design principles and stricter detailing requirements to ensure
     enhanced seismic performance.

**beta_v** (float)
   Design vertical load factor. This is only required ``"tr_post18_dch"`` and ``"tr_post18_dcm"`` design classes.

Sampling Parameters
^^^^^^^^^^^^^^^^^^^^

The parameters in this section control the sampling process.

**sample_size** (int)
   Size of the generated sample (number of realisations).

**seed** (int)
   Seed used for random number generation.


Parameters for Sampling of Geometry Variables
+++++++++++++++++++++++++++++++++++++++++++++

These parameters control the sampling of geometry variables
describing the geometric characteristics of the buildings.

**typical_storey_height (dict)**  
   Parameters for typical storey heights represented by a truncated
   log-normal distribution.

   - ``mu`` (float): mean storey height
   - ``cv`` (float): coefficient of variation
   - ``lower_bound`` (float): lower bound value
   - ``upper_bound`` (float): upper bound value

**standard_bay_width (dict)**  
   Parameters of a truncated log-normal distribution for standard bay widths.

   - ``corr_coeff_xy`` (float): correlation coefficient between x and y bay widths
   - ``lower_bound_x`` (float): lower bound for bay width in x direction
   - ``upper_bound_x`` (float): upper bound for bay width in x direction
   - ``theta_x`` (float): median (x)
   - ``sigma_x`` (float): logarithmic standard deviation (x)
   - ``lower_bound_y`` (float): lower bound for bay width in y direction
   - ``upper_bound_y`` (float): upper bound for bay width in y direction
   - ``theta_y`` (float): median (y)
   - ``sigma_y`` (float): logarithmic standard deviation (y)

**staircase_bay_width (dict)**  
   Parameters of a uniform distribution for staircase bay width.

   - ``lower_bound`` (float): lower bound value
   - ``upper_bound`` (float): upper bound value

**ground_storey_height (dict)**  
   Parameters used to sample ground storey heights.

   Sampled typical storey heights are multiplied by factors sampled
   from ``factor`` according to the corresponding ``probability``
   values. If the resulting value exceeds ``maximum``, it is capped
   at this limit.

   - ``maximum`` (float): maximum possible ground storey height
   - ``factor`` (list[float]): factors applied to typical storey heights
   - ``probability`` (list[float]): probabilities of the factors (the sum should be equal to 1.0)

**layout** (``"all"`` or list[str])  
   Layout IDs considered for building generation.

   Use ``"all"`` to include all layouts or provide a list of layout tags.
   Layouts are defined in the internal layout database.

.. list-table:: Available floor layouts
   :header-rows: 1

   * - Tag
     - num_bays_x
     - num_bays_y
     - stairs_grid_x
     - stairs_grid_y
   * - B01
     - 3
     - 2
     - 1
     - 0
   * - B02
     - 5
     - 2
     - 2
     - 0
   * - B03
     - 7
     - 2
     - 3
     - 0
   * - B04
     - 3
     - 3
     - 1
     - 0
   * - B04b
     - 3
     - 3
     - 1
     - 1
   * - B05
     - 5
     - 3
     - 2
     - 0
   * - B06
     - 7
     - 3
     - 3
     - 0
   * - B07
     - 3
     - 3
     - 0
     - 0
   * - B08
     - 3
     - 4
     - 0
     - 0
   * - B09
     - 3
     - 5
     - 0
     - 0
   * - B10
     - 3
     - 6
     - 0
     - 0

Parameters for Sampling of Secondary Taxonomy Attributes
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

These parameters control the sampling of the secondary taxonomy attributes
describing initial conceptual design choices for the buildings.

**exterior_infill_type (dict)**
   Parameters for sampling exterior masonry infill typologies.

   - ``typology`` (list[int], default: ``[1, 2, 3]``)

     Infill typology identifiers (IDs):

     - 1: Weak (T1 in Hak et al. 2012)
     - 2: Medium (T2 in Hak et al. 2012)
     - 3: Strong (T3 in Hak et al. 2012)

   - ``probability`` (list[float], default: ``[0.6, 0.3, 0.1]``)

     Probability associated with each typology ID (The sum should be equal to 1.0)

**interior_infill_type (dict)**  
   Same structure as ``exterior_infill_type``, applied to interior infills.

**infill_configuration (dict)**  
   Parameters for sampling masonry infill configuration IDs.

   - ``configuration`` (list[int], default: ``[1, 2]``)

    Masonry infill wall configuration IDs:

     - 1: Exterior only, Regular over the height, XX + YY
     - 2: Exterior only, Pilotis, XX + YY
     - 3: Exterior only, Pilotis, XX
     - 4: Exterior only, Pilotis, YY
     - 5: Exterior + Interior, Regular over the height, XX + YY
     - 6: Exterior + Interior, Pilotis, XX + YY
     - 7: Exterior + Interior, Pilotis, XX
     - 8: Exterior + Interior, Pilotis, YY
     - 9: Interior only, Regular over the height, XX + YY
     - 10: Interior only, Pilotis, XX + YY
     - 11: Interior only, Pilotis, XX
     - 12: Interior only, Pilotis, YY

   - ``probability`` (list[float], default: ``[0.7, 0.3]``)

     Probability associated with each configuration ID.
     The sum should be equal to 1.0.

   *Notes:*

   - Infills around the stairs are included regardless of the configuration.
   - Gravity loads associated with masonry infills are derived directly
     from the selected infill configuration.

**concrete (dict)** / **steel (dict)**
   Material grade sampling distributions.

   - ``grade`` (list[str]): material tags, i.e., concrete strength classes or steel grades
   - ``probability`` (list[float]): occurrence probabilities for each material, the sum should be equal to 1.0

**construction_quality (dict)**
   Construction quality sampling distribution.

   - ``quality`` (list[int], default: ``[1, 2, 3]``): Construction quality identifiers (IDs)

     - 1: High quality
     - 2: Moderate quality
     - 3: Low quality

   - ``probability`` (list[float]): occurrence probabilities for each quality ID, the sum should be equal to 1.0

**slab_typology (dict)**
   Parameters required for slab typology sampling / decision tree.

   - ``ss1_prob_given_ss1_or_hs`` (float): probability of having SS1 type slab given that the slab type is either SS1 or HS
   - ``ss2_prob_given_ss2_or_hs`` (float): probability of having SS2 type slab given that the slab type is either SS2 or HS
   - ``max_ss_short_span`` (float): upper limit for the short span length in solid slabs (SS1, SS2)
   - ``max_ss2_aspect_ratio`` (float): upper limit for the ratio of maximum to minimum span lengths (aspect ratio) in SS2 slabs
   - ``staircase_slab_depth`` (float): depth of the staircase slabs, if not provided computed during the design process
   - ``floor_slab_thickness`` (float): thickness of the floor slabs, if not provided computed the design process

    *Definitions:*
        1. SS2 refers to solid two-way cast-in-situ slabs
        2. SS1 refers to solid one-way cast-in-situ slabs
        3. HS refers to composite slabs with pre-fabricated joists and ceramic blocks.

**wb_prob_given_hs** (float)
   Probability of having wide beams (WB) given slab type is HS.

**square_column_prob** (float)
   Probability of having square columns.

References
^^^^^^^^^^

RBA (1935). *Regulamento do Betão Armado.*
Decreto N.° 25:948, Lisbon, Portugal.

REBAP (1983). *Regulamento de Estruturas de Betão Armado e Pré-Esforçado.*
Decreto-Lei N.° 349-C/83, Lisbon, Portugal.

Comité Européen du Béton, CEB (1963). *Recommandations Pratiques à l'Usage des
Constructeurs.*
fib - International Federation for Structural Concrete, Lausanne, Switzerland.

Guerrin, A. (1966). *Traité de Béton Armé.*
Dunod, Paris, France.

REBA (1967). *Regulamento de Estruturas de Betão Armado.*
Decreto N.° 47:723, Lisbon, Portugal.

d'Arga e Lima, J., Monteiro, V., and Mun, M. (2005). *Betão Armado — Esforços
Normais e de Flexão (REBAP-83).*
Laboratório Nacional de Engenharia Civil, Lisbon, Portugal.

Comité Européen du Béton, CEB (1978). *Système International de Réglementation
Technique Unifiée des Structures, Vol. 1 — Règles Unifiées Communes.*
fib - International Federation for Structural Concrete, Lausanne, Switzerland.

Comité Européen du Béton, CEB (1978). *Système International de Réglementation
Technique Unifiée des Structures, Vol. 2 — Code-Modèle CEB-FIP pour les
Structures en Béton.*
fib - International Federation for Structural Concrete, Lausanne, Switzerland.

Comité Européen de Normalisation, CEN (2004). *Eurocode 2: Design of Concrete
Structures — Part 1-1: General Rules and Rules for Buildings.*
European Committee for Standardization, Brussels, Belgium.

Comité Européen de Normalisation, CEN (2004). *Eurocode 8: Design of Structures
for Earthquake Resistance — Part 1: General Rules, Seismic Actions and Rules
for Buildings.*
European Committee for Standardization, Brussels, Belgium.

Hak, S., Morandi, P., Magenes, G., & Sullivan, T. J. (2012).
Damage control for clay masonry infills in the design of RC frame structures.
*Journal of Earthquake Engineering*, 16(sup1), 1-35.
https://doi.org/10.1080/13632469.2012.670575

TBEC (1975). *Afet Bölgelerinde Yapılacak Yapılar Hakkında Yönetmelik*.
Resmi Gazete, Ankara, Türkiye.

TBEC (1998). *Afet Bölgelerinde Yapılacak Yapılar Hakkında Yönetmelik*.
Resmi Gazete, Ankara, Türkiye.

TBEC (2007). *Deprem Bölgelerinde Yapılacak Binalar Hakkında Esaslar*.
Resmi Gazete, Ankara, Türkiye.

TBEC (2018). *Deprem Etkisi Altında Binaların Tasarımı için Esaslar*.
Resmi Gazete, Türkiye.

TS500 (1984). *Requirements for Design and Construction of Reinforced
Concrete Structures*. Turkish Standards Institution (TSE), Ankara, Türkiye.

TS500 (2000). *Requirements for Design and Construction of Reinforced
Concrete Structures*. Turkish Standards Institution (TSE), Ankara, Türkiye.
