# Changelog

All notable changes to SimDesign are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

[1.1.0]: https://github.com/builtenvdata/simulated-design/compare/v1.0.1...v1.1.0
[1.0.1]: https://github.com/builtenvdata/simulated-design/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/builtenvdata/simulated-design/releases/tag/v1.0.0
