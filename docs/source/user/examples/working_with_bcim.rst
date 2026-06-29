Portfolio
---------

The examples below illustrate how to use the
:class:`~simdesign.rcmrf.bcim.factory.BCIM` class directly, independently of
the high-level :func:`simdesign.rcmrf.generate` convenience function. The
generated portfolio can be further refined — for example by adjusting
individual :class:`~simdesign.rcmrf.bcim.factory.TaxonomyData` objects —
before passing it to the design stage.

Generating a portfolio with default inputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from pathlib import Path
    from simdesign.rcmrf import BCIM

    bcim = BCIM()
    bcim.generate(
        sample_size=10,
        design_class="eu_cdl",
        num_storeys=5,
        beta=0.15,
    )
    taxonomy = bcim.taxonomy
    bcim.to_csv(Path("bcim_default.csv"))

The :attr:`~simdesign.rcmrf.bcim.factory.BCIM.taxonomy` attribute is a list
of :class:`~simdesign.rcmrf.bcim.factory.TaxonomyData` objects — one per
building realisation — that can be passed directly to
:class:`~simdesign.rcmrf.bdim.baselib.building.BDIM` for the design stage.

Overriding default probability distributions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Any secondary taxonomy parameter can be overridden by passing it as a keyword
argument to :meth:`~simdesign.rcmrf.bcim.factory.BCIM.generate`. The example
below replaces the default steel grade probabilities defined in the
design-class configuration file with a custom distribution.

.. code-block:: python

    custom_inputs = {
        "design_class": "eu_cdl",
        "num_storeys": 5,
        "beta": 0.20,
        "sample_size": 20,
        "steel": {
            "grade": ["A24", "A40", "A50"],
            "probability": [0.40, 0.50, 0.10],
        },
    }

    bcim.generate(**custom_inputs)
    bcim.to_csv(Path("bcim_custom_steel.csv"))

The same pattern applies to all optional parameters described in
:doc:`../inputs_bcim`, such as ``concrete``, ``construction_quality``,
``exterior_infill_type``, and the geometry distribution parameters.
