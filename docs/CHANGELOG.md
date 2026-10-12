# Changelog

All notable changes to SimDesign are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.2.0] - 2026-10-12

### Added

- `DP05` BNSM model: DP03 with an axial release at the end of each beam, so the fiber-section beams can elongate under the rigid diaphragm.
- `beam_loads` BNSM option (`'uniform'`, `'point'` or `'auto'`) for applying beam gravity loads.
- Readable tag encoding in `simdesign.utils.tags`, with `decode_*` functions for points, lines, rectangles and nodes.
- `GeometryBase.retag()` and `CustomGeometry(retag=True)` to renumber geometry objects with the new tag encoding.
- `cracked_beam` and `cracked_column` accept a float, the ratio of effective to gross flexural stiffness.
- Shared hinge property functions in `simdesign.utils.rcsection` (yield point, yield rotation, Haselton backbone, plastic hinge length).
- EC8 local ductility check (EN 1998-1 Eq. 5.15) at the base of `eu_cdh` columns.
- Equilibrium and stiffness checks in `do_nspa`, which stop pushovers on unrealistic base shear spikes.

### Changed

- Default BNSM model is CP01 instead of CP03.
- CP01-CP03 elastic members are nearly rigid in flexure (`STIFF_INTERIOR_FACTOR`), so the hinges carry the whole member flexibility.
- CP01 and CP02 hinge sections have elastic axial and torsional materials (and elastic weak-axis flexure in beams) instead of rigid ones.
- CP03 hinges use the full EN 1998-3 yield rotation θy instead of θy/10.
- Shear span of the hinge properties is taken from the clear length of the member instead of the node-to-node length (all models).
- DP01 beams and columns and DP04 beams yield at the EN 1998-3 yield rotation θy.
- DP01 and DP04 cracked elastic interiors are not more flexible than the member at yield.
- `cracked_*=True` uses `EIeff = My / phi_y` of the plastic hinges.
- θy leaves out the shear term for columns with shear springs.
- Tension shift factor `av` of θy is set from the shear cracking check instead of always 1.
- Beam hinges use the tension bar diameter for each bending direction.
- DP shear springs limit the shear span ratio of the cracking shear to 2–4.
- CP01-CP03 post-failure shear slope uses the column core depth and an axial load ratio limited to 0.15–0.61.
- CP01-CP03 shear springs each take the member post-failure slope; residual shear strength is 10% of Vn.
- CP02 backbone zero-moment point is 10% of Mu instead of Mc.
- CP02 always uses the cyclic backbone; `cyclic_model` no longer affects CP02.
- `Concrete01` fiber concrete uses the modified Kent and Park parameters.
- Joint models use `MinMax`-wrapped rotational materials and an elastic axial spring, as in O'Reilly's `jointModel.tcl`.
- DP05 stairs beams have no axial release.
- Beam gravity loads are applied as end point loads by default when the joints are inelastic.
- Tags of all model objects follow the new encoding, also in exported models.
- Geometry objects added without a tag are tagged from their grid location.
- `CustomGeometry` validates duplicate tags, coincident points, overlapping objects and undefined points.
- Infills are a runtime flag in exported models.
- Gravity analysis raises an error if it does not converge.
- Infill struts are added after the gravity analysis.
- Recalibrated `tr_7599` material and quality data and BCIM concrete grade probabilities.

### Fixed

- Two-way slab tributary areas of the long-span beams were doubled.
- Slab self-weight used each slab's own thickness instead of the final building thickness.
- All buildings of a portfolio used the same quality seed.
- `seed=0` was ignored.
- Infill strut 2 started at the stair landing node next to split stair columns.
- Infill struts in tension after gravity dropped out of the modal analysis.
- Beam-column joint connectivity; joints behaved as rigid.
- CP03 beam rigid-offset links and node definition order.
- CP03 beam hinge moment signs were swapped.
- Beam gravity load over the joint regions was not applied.
- Turkish column design tables (`design_tables.json`).
- Beam maximum depth in the Turkish design classes used `max` instead of `min`.
- Doubly reinforced beam sections got zero steel in the Turkish design classes.
- Column capacity shear in `tr_0018_dch` and `tr_post18_dch` used the axial force with the wrong sign.
- Turkish column shear design treated tension as compression.
- `tr_7599` column shear design used the signed end shears.
- `tr_7599` minimum column hoops.
- `tr_7599` quality adjustment overwrote the design reinforcement.
- `tr_7599` beam ends with h ≤ 222 mm got oversized stirrups.
- `tr_0018_dcm` column hoop spacing used the high-ductility rule.
- REBAP shear stresses τ1 and τ2 in `eu_cdm` did not depend on the concrete class.
- `eu_cdm` column shear design ignored the concrete contribution.
- `eu_cdm` minimum column hoops and beam bar spacing limits; crash with A235 steel.
- Capacity-design shears paired end moments from opposite sway directions.
- Corner bar area in `eu_cdl` used the intermediate bar diameter.
- Missing C40/50 concrete grade in `eu_cdh`.
- Stirrup leg count could exceed the number of longitudinal bars.
- Beam bottom bar index wrapped round to the largest diameter.
- Column rebar spacing check would raise a `TypeError`.
- BDIM base shear included the weights at the base nodes.
- BDIM rigid diaphragms were not rebuilt at the updated centre of mass.
- Material restore in the iterative design did not restore the initial grades.
- BDIM modified the given `TaxonomyData`.
- Slabs and beam loads were not rebuilt when the slab type changed.
- Stair loads on beams were overwritten instead of accumulated.
- `TaxonomyData.slab_orientation` was not used.
- Failed designs did not emit a warning.
- `fcm` column of the exported `joints.csv`.
- `rcsection.get_moments` returned a wrong My at high axial load.
- Popovics peak strain diverged for very low concrete strengths.
- `rcsection.get_kent_park_confinement` strain term was missing the hoop ratio.
- Haselton correction for non-symmetric beam reinforcement was applied to the wrong bending direction.
- Beam plastic hinge length used the design instead of the quality-adjusted bar diameters.
- CP column shear springs: stiffness halved by the two springs in series, and the θy shear term counted twice.
- CP02 shear failure curve used the CP01 yield rotation.
- DP01 and DP02 column shear springs acted only over the hinge lengths.
- DP column shear hinges used the wrong transverse reinforcement ratio.
- DP shear spring backbones could become non-monotonic, and the residual point jumped at zero.
- `do_nspa` returned `ok = -1` after a successful run, and the final step was not recorded.
- Pushover solver tolerance stayed relaxed after a hard step.
- Exported `nspa.tcl` overestimated the base shear.
- `storey_heights.out` was rounded to 0.1 m.
- EQL and TRI load patterns and BDIM eccentricity forces used absolute heights.
- `do_modal` accepted invalid or unset eigenvalues, and returned invalid periods with a single mode.
- `cracked_beam` and `cracked_column` accepted any value.
- BNSM inputs could flip or be dropped silently.
- `generate()` deleted the output directory and modified the caller's inputs.
- BCIM input overrides persisted between calls and did not merge nested inputs.
- Removing read-only directories failed on Python 3.12 or newer.
- `tr_post18_*` crashed when `beta_v` was not given.
- Tag collisions in buildings with 10 or more storeys or bays.
- `CustomGeometry` grid indices depended on the workbook row order.
- Rectangle corner order depended on the input winding; parallelograms were accepted as rectangles.
- Stair rectangles were added twice, and stair side-wall infills were tagged one storey too high.
- Stair bays adjacent along x crashed the geometry.
- `stairs_lines_z3` and `stairs_lines_z4` kept stale lines with adjacent stair bays.
- `misc.dot` returned 0.0 for lists of different lengths.

### Removed

- CP02 `export_hinges`.

## [1.1.0] - 2026-09-07

### Added

 - Added changelog to the documentation.

### Changed

- Updated `HystereticSM` material parameters in CP02.
- CP02 now uses the base infill implementation.
- Default `gE` parameter of the DP02 model changed to 10.
- Default external infill type changed to medium quality.
- Lowered `sigma_cover` for Turkish design classes.
- Concentrated-plasticity (CP02) integration now uses elastic rather than rigid element properties.

### Fixed

- Reinforcing bar buckling coefficient now uses the actual `sbh` values instead of a single shared value.
- Bug in `quality.py`.
- Bug in the shear model.
- Unit conversion error.
- Bug in eccentricity calculation for Turkish design classes.
- Bug in exterior infill identification.
- Typos in the infill property calculations, in the `dbl_ave` calculation, and in the joint offset definition of foundation columns.

### Removed

- Unnecessary class inheritance in the CP02 model.

## [1.0.1] - 2026-06-30

### Added

- Test suite with coverage reporting, with a minimum threshold of 75%.
- Full Sphinx API documentation for the `bcim`, `bdim`, and `bnsm` modules.

### Changed

- Updated BNSM algorithms.
- Renamed `model.py` to `factory.py`.
- Design beta values specified per frame storey height; added an excellent construction quality option.

## [1.0.0] - 2026-05-12

### Added

- Initial public release of the SimDesign framework: BCIM parametrization and
  randomization, BDIM simulated design for European and Turkish design codes,
  and BNSM nonlinear model generation for OpenSees.

[Unreleased]: https://github.com/builtenvdata/simulated-design/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/builtenvdata/simulated-design/compare/v.1.1.0...v1.2.0
[1.1.0]: https://github.com/builtenvdata/simulated-design/compare/v1.0.1...v.1.1.0
[1.0.1]: https://github.com/builtenvdata/simulated-design/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/builtenvdata/simulated-design/releases/tag/v1.0.0
