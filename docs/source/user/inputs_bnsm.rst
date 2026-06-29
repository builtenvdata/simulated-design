BNSM inputs
-----------

The ``bnsm`` input dictionary controls the configuration of the nonlinear
structural model, including the modelling strategy, load and mass assumptions,
pushover analysis settings, and output format.
The example below shows a complete ``bnsm`` configuration. All parameters are
optional; default values are applied when not specified.

.. code-block:: python

    "bnsm": {
        "model": "CP03",
        "opensees": "py",

        "load_factors": {"G": 1.0, "Q": 0.3},
        "mass_factors": {"G": 1.0, "Q": 0.3},

        "scheme": "EQL",
        "max_drift": 0.05,
        "dincr": 0.001,

        "include_infills": True,
        "cyclic_model": False,
        "cracked_beam": False,
        "cracked_column": False,
        "infill_column_connection": "parallel"
    }

Model Selection
^^^^^^^^^^^^^^^

The model identifier selects one of several pre-calibrated nonlinear modelling
strategies, all of which build on a shared base library (``bnsm.baselib``)
that provides the common element-level formulation. In particular, every model
inherits the same default treatment for the following components:

- **Beams** are modelled with force-based beam-column elements
  (``forceBeamColumn``) using a ``HingeRadau`` plastic-hinge integration scheme.
  Inelasticity is concentrated within finite plastic-hinge lengths at the
  element ends, while the interior is represented by an elastic section
  (optionally using cracked-section flexural stiffness). End-hinge
  moment-rotation behaviour follows a ``Hysteretic`` uniaxial material with a
  trilinear backbone (yield, capping, residual). Yield is computed using the
  approach of Panagiotakos and Fardis (2001); capping moment, plastic rotation
  capacity, and post-capping rotation capacity follow Haselton et al. (2008,
  2016), and yield rotation follows EN 1998-3:2004. Plastic hinge length is
  computed per Priestley et al. (2007). A bond-slip modification factor adjusts
  the hinge properties.

- **Columns** use the same ``forceBeamColumn`` / ``HingeRadau`` framework as
  beams, but with a P-Delta geometric transformation to capture second-order
  effects under gravity. Flexural behaviour about both local axes (``My``,
  ``Mz``) is represented by ``Hysteretic`` materials assembled in an aggregated
  hinge section. When capacity-design shear is not enforced, the aggregated
  section additionally includes ``Pinching4`` shear hinges (``Vy``, ``Vz``)
  wrapped with ``MinMax`` limiters, calibrated following Zimos et al. (2015)
  with input from Sezen and Moehle (2004), Priestley et al. (1994), Mergos and
  Kappos (2012), and O'Reilly (2016).

- **Beam-column joints** are represented by rotational spring models that can
  be rigid, elastic, or inelastic.

- **Masonry infills** are represented by an equivalent diagonal-strut
  macro-model: each infill panel is replaced by two compression-only diagonal
  truss elements with a nonlinear uniaxial material. The default panel
  properties for the three typologies (``"Weak"``, ``"Medium"``, ``"Strong"``,
  corresponding to T1/T2/T3) follow Hak et al. (2012); concrete-equivalent
  ``Concrete01`` material parameters (peak/residual strengths and strains)
  are derived from the same source.

- **Floor diaphragms** are modelled as rigid via a retained node and
  multi-point constraints.

- **Foundations** are lumped fixed support nodes.

Each model below either uses these defaults directly or replaces specific
components with calibrated alternatives.

**model** (str, default: ``"CP03"``)
   Identifier of the nonlinear modelling strategy to use. The following
   pre-defined models are currently available, organised by plasticity
   formulation.

   *Concentrated plasticity (CP) models*

   - ``"CP01"``: Lumped-plasticity model using the base ``forceBeamColumn``
     framework, with beam and column flexural hinges defined through the
     ``Hysteretic`` moment-rotation formulation calibrated by Haselton et al.
     (2008). Columns optionally include a degrading shear hinge using a
     ``LimitState`` material coupled with ``ThreePoint`` limit curves per
     Elwood and Moehle (2003). Beam-column joint springs follow O'Reilly
     (2016). Masonry infills use the equivalent diagonal-strut model
     calibrated within ESRM20 (Crowley et al., 2021): each strut is assigned a
     ``Concrete01`` material whose peak compressive strength is obtained from
     a regression on Hak et al. (2012) data as a function of panel length and
     height.

   - ``"CP02"``: Extends CP01 by replacing the ``Hysteretic`` end-hinge
     material in both beams and columns with the energy-based ``HystereticSM``
     formulation of Hasanoglu and O'Reilly (2026), which provides improved
     control of hysteretic energy dissipation under cyclic loading. Shear
     hinges, joints, infills (ESRM20-calibrated ``Concrete01`` strut inherited
     from CP01), and assembly logic are inherited from CP01 unchanged.

   - ``"CP03"``: Extends CP01 by representing the plastic hinges explicitly as
     ``zeroLength`` (beams) and ``zeroLengthSection`` (columns) elements placed
     in series with an elastic interior beam-column element, with hinge
     stiffness corrected following Ibarra and Krawinkler (2005). Rigid joint
     offsets are modelled with rigid-like ``elasticBeamColumn`` elements rather
     than ``geomTransf`` joint offsets, which allows auxiliary plastic hinge
     nodes to be defined explicitly. The infill formulation (ESRM20
     ``Concrete01`` strut) is inherited from CP01, but CP03 additionally
     exposes a configurable series-or-parallel infill-column shear
     interaction (see ``infill_column_connection`` below).

   *Distributed plasticity (DP) models*

   - ``"DP01"``: Direct use of the base distributed-plasticity formulation.
     Beams and columns are modelled with ``forceBeamColumn`` elements and a
     ``HingeRadau`` integration scheme over a finite plastic-hinge length
     computed per Priestley et al. (2007), with aggregated end-hinge sections
     combining flexural (``Hysteretic``) and optional degrading shear
     (``Pinching4+MinMax``) responses. Masonry infills use the base
     equivalent-strut macro-model directly, with Hak et al. (2012) panel
     properties. Suitable as a general-purpose baseline distributed-plasticity
     model.

   - ``"DP02"``: Extends DP01 by recalibrating the end-hinge flexural
     moment-curvature relationships using ``Pinching4`` materials following
     O'Reilly (2016), offering refined cyclic energy dissipation, pinching, and
     strength/stiffness degradation behaviour. Masonry infill struts are
     recalibrated for ``Pinching4`` behaviour with cracking, peak, and residual
     strength/drift parameters from O'Reilly (2016). The remaining components
     are inherited from the base library.

   - ``"DP03"``: Extends DP01 by replacing aggregated end-hinge sections with
     ``fiber``-discretized sections at both ends of beams and columns,
     explicitly capturing axial-flexure interaction and the influence of
     reinforcement detailing. Concrete confinement follows Mander et al.
     (1988), and reinforcing steel is wrapped with ``MinMax`` limiters
     enforcing strain bounds that approximate bar buckling or rupture per
     Priestley et al. (2007). The interior section of beams and columns can be
     defined as elastic or inelastic. Infills are inherited from the base
     library (Hak et al. 2012 diagonal strut).

   - ``"DP04"``: A DP03-derived variant intended for cases where fiber-level
     refinement is required only for columns. Column end-hinge sections retain
     the DP03 fiber formulation, but the interior column section is set to
     elastic by default. Beam modelling reverts to the DP01 aggregated-section
     formulation. Joints, base-library diagonal-strut infills, diaphragms, and
     foundations are inherited unchanged.

**opensees** (``"py"`` or ``"tcl"``, default: ``"py"``)
   Output format for the generated OpenSees model script.

   - ``"py"``: generates an OpenSeesPy-compatible Python script.
   - ``"tcl"``: generates an OpenSees Tcl script.

Load and Mass Parameters
^^^^^^^^^^^^^^^^^^^^^^^^

**load_factors** (dict, default: ``{"G": 1.0, "Q": 0.3}``)
   Load combination factors used to compute gravity loads applied to the model.

   - ``"G"`` (float): factor for permanent (dead) loads.
   - ``"Q"`` (float): factor for variable (live) loads.

**mass_factors** (dict, default: ``{"G": 1.0, "Q": 0.3}``)
   Factors used to compute seismic masses from gravity loads.

   - ``"G"`` (float): factor for permanent (dead) loads.
   - ``"Q"`` (float): factor for variable (live) loads.

Pushover Analysis Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**scheme** (str, default: ``"EQL"``)
   Lateral load distribution scheme used for nonlinear static (pushover) analysis.

   - ``"FMP"``: fundamental-mode proportional loading.
   - ``"EQL"``: equivalent lateral force distribution.
   - ``"MPP"``: mass-proportional loading.
   - ``"TRI"``: triangular (height-proportional) loading.
   - ``"UNI"``: uniform loading.

**max_drift** (float, default: ``0.05``)
   Maximum inter-storey drift ratio used to define the target displacement of
   the control node.

**dincr** (float, default: ``0.001``)
   First displacement increment applied at the control node during pushover
   analysis (in metres).

Modelling Settings
^^^^^^^^^^^^^^^^^^

.. note::

   The parameters below are available for all model types unless stated
   otherwise. Parameters not recognised by the selected model are silently
   ignored.

**include_infills** (bool, default: ``True``)
   If ``True``, masonry infill panels are included in the structural model.

**cyclic_model** (bool, default: ``False``)
   If ``True``, model parameters are adjusted for cyclic (as opposed to
   monotonic) analysis.

**cracked_beam** (bool, default: ``False``)
   If ``True``, effective (cracked-section) flexural stiffness is used for
   elastic beam elements. If ``False``, gross-section properties are applied.

**cracked_column** (bool, default: ``False``)
   If ``True``, effective (cracked-section) flexural stiffness is used for
   elastic column elements. If ``False``, gross-section properties are applied.

**infill_column_connection** (``"parallel"`` or ``"series"``, default: ``"parallel"``)
   .. note:: This parameter is only applicable to ``"CP03"``.

   Modelling assumption governing the interaction between masonry infill struts
   and column lateral response.

   - ``"parallel"``: the infill strut acts in parallel with the column,
     contributing directly to the global lateral strength of the frame.
   - ``"series"``: the column lateral response acts in series with the
     horizontal component of the infill strut. The effective lateral strength
     is governed solely by the column.

References
^^^^^^^^^^

Crowley, H. M., Dabbeek, J., Despotaki, V., Rodrigues, D., Martins, L.,
Silva, V., Romão, X., Pereira, N., Weatherill, G. A., & Danciu, L. (2021).
European Seismic Risk Model (ESRM20). *EFEHR Technical Report 002*.
https://doi.org/10.7414/EUC-EFEHR-TR002-ESRM20

Elwood, K. J., & Moehle, J. P. (2003).
Shake table tests and analytical studies on the gravity load collapse of
reinforced concrete frames. *PEER Report 2003/01*.
Pacific Earthquake Engineering Research Center, University of California, Berkeley.

Hak, S., Morandi, P., Magenes, G., & Sullivan, T. J. (2012).
Damage control for clay masonry infills in the design of RC frame structures.
*Journal of Earthquake Engineering*, 16(sup1), 1-35.
https://doi.org/10.1080/13632469.2012.670575

Hasanoglu, S., & O'Reilly, G. J. (2026).
A hysteretic energy-based framework for seismic fragility assessment of ductile
reinforced concrete frame buildings. *(in preparation)*

Haselton, C. B., Liel, A. B., Lange, S. T., & Deierlein, G. G. (2008).
Beam-column element model calibrated for predicting flexural response leading
to global collapse of RC frame buildings.
Pacific Earthquake Engineering Research Center, University of California, Berkeley, CA.

Haselton, C. B., Liel, A. B., Taylor-Lange, S. C., & Deierlein, G. G. (2016).
Calibration of model to simulate response of reinforced concrete beam-columns to collapse.
*ACI Structural Journal*, 113(6).

Ibarra, L. F., & Krawinkler, H. (2005).
Global collapse of frame structures under seismic excitations.
*Technical Report 152*, John A. Blume Earthquake Engineering Center, Stanford University.

Mander, J. B., Priestley, M. J. N., & Park, R. (1988).
Theoretical stress-strain model for confined concrete.
*Journal of Structural Engineering*, 114(8), 1804-1826.
https://doi.org/10.1061/(ASCE)0733-9445(1988)114:8(1804)

Mergos, P. E., & Kappos, A. J. (2012).
A gradual spread inelasticity model for R/C beam-columns, accounting for
flexure, shear and anchorage slip.
*Engineering Structures*, 44, 94-106.
https://doi.org/10.1016/j.engstruct.2012.05.035

O'Reilly, G. J. (2016).
*Performance-based seismic assessment and retrofit of existing RC frame
buildings in Italy*. Doctoral dissertation, IUSS Pavia.

Panagiotakos, T. B., & Fardis, M. N. (2001).
Deformations of reinforced concrete members at yielding and ultimate.
*Structural Journal*, 98(2), 135-148.

Priestley, M. N., Verma, R., & Xiao, Y. (1994).
Seismic shear strength of reinforced concrete columns.
*Journal of Structural Engineering*, 120(8), 2310-2329.
https://doi.org/10.1061/(ASCE)0733-9445(1994)120:8(2310)

Priestley, M. J. N., Calvi, G. M., & Kowalsky, M. J. (2007).
*Displacement-based seismic design of structures*. IUSS Press, Pavia.

Sezen, H., & Moehle, J. P. (2004).
Shear strength model for lightly reinforced concrete columns.
*Journal of Structural Engineering*, 130(11), 1692-1703.
https://doi.org/10.1061/(ASCE)0733-9445(2004)130:11(1692)

Zimos, D. K., Mergos, P. E., & Kappos, A. J. (2015).
Shear hysteresis model for reinforced concrete elements including the post-peak range.
*Proceedings of COMPDYN 2015*, Crete Island, Greece.
https://doi.org/10.7712/120115.3565.1184
