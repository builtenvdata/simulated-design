:orphan:

API Reference
=============

This section documents the public API of SimDesign. The package is split
into two top-level subpackages:

- :mod:`simdesign.rcmrf` — the RC moment-resisting frame pipeline
  (BCIM → BDIM → BNSM), exposing the high-level
  :func:`simdesign.rcmrf.generate` entry point and the underlying
  data models, design-class implementations, and modelling strategies.
- :mod:`simdesign.utils` — general-purpose helpers used across the
  framework (mesh geometry, RC sections, statistics, units, plotting).

.. toctree::
   :maxdepth: 2

   rcmrf/index
   utils/index
