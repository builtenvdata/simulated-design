Workflow
--------

This example shows how to run the complete BED-RCMRF workflow for every available
design class, storing each portfolio's outputs in a dedicated subdirectory.

.. code-block:: python

    from pathlib import Path
    from simdesign import rcmrf
    from simdesign.utils.misc import make_dir

    inputs = {
        "bcim": {
            "sample_size": 30,
            "num_storeys": 4,
            "beta": 0.1,
            "seed": 2,
        },
        "bnsm": {
            "model": "DP01",
            "scheme": "EQL",
            "dincr": 1e-3,
            "max_drift": 0.1,
            "opensees": "py",
            "include_infills": False,
        },
    }

    design_classes = [
        "eu_cdn", "eu_cdl", "eu_cdm", "eu_cdh",
        "tr_7599", "tr_0018_dcm", "tr_0018_dch",
        "tr_post18_dcm", "tr_post18_dch",
    ]

    outdir_main = Path("Outputs-BED")
    make_dir(outdir_main)

    for design_class in design_classes:
        inputs["bcim"]["design_class"] = design_class
        outdir = outdir_main / design_class
        bcim, bdim, bnsm = rcmrf.generate(inputs, outdir)

The loop produces one subdirectory per design class under ``Outputs-BED/``:

.. code-block:: text

    Outputs-BED/
    ├── eu_cdn/
    ├── eu_cdl/
    ├── eu_cdm/
    ├── eu_cdh/
    ├── tr_7599/
    ├── tr_0018_dcm/
    ├── tr_0018_dch/
    ├── tr_post18_dcm/
    └── tr_post18_dch/

Each subdirectory contains the same outputs as a single
:func:`simdesign.rcmrf.generate` call: a BCIM CSV, BDIM CSVs, and OpenSees
model scripts for every building realisation in the portfolio.

.. note::

   Setting a fixed ``seed`` in the ``bcim`` configuration ensures the same
   building realisations are generated on every run, enabling reproducible
   comparisons across design classes.
