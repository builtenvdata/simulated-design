2. Examples
===========

2.1. Minimal Inputs
-------------------

.. code-block:: python

    from simdesign import rcmrf

    # The main inputs for each design class
    inputs = {
        'bcim': {
            'design_class': 'eu_cdl',
            'sample_size': 30,
            'num_storeys': 4,
            'beta': 0.1,
            'seed': 2
        },
        'bnsm': {
            "scheme": 'FMP',
            "dincr": 1e-4,
            'max_drift': 0.1,
            'opensees': 'py'
        }
    }

    # Run the bed-workflow for rcmrf systems and save the outputs
    bcim, bdim, bnsm = rcmrf.generate(inputs=inputs, outdir="Outputs")

2.2. Advanced Inputs
--------------------

.. code-block:: python

    from simdesign import rcmrf

    # The main inputs for each design class
    inputs = {
            "bcim": {
                "design_class": "eu_cdh",
                "beta": 0.1,
                "sample_size": 150,
                "num_storeys": 5,
                # Distribution parameters
                "typical_storey_height": {
                    "cv": 0.07,
                    "mu": 2.90,
                    "lower_bound": 2.3,
                    "upper_bound": 3.8,
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
                    "sigma_y": 0.35,
                },
                "steel": {
                    "tag": ["S400", "S500"],
                    "probability": [0.10, 0.90]
                },
                "concrete": {
                    "tag": ["C20", "C25", "C30", "C35"],
                    "probability": [0.30, 0.45, 0.20, 0.05],
                },
                "ground_storey_height": {
                    "maximum": 4.20,
                    "factor": [1.0, 1.1, 1.2, 1.3, 1.4],
                    "probability": [0.55, 0.10, 0.20, 0.10, 0.05],
                },
                "construction_quality": {"probability": [0.6, 0.3, 0.1]},
                "slab_typology": {
                    "ss1_prob_given_ss1_or_hs": 0.50,
                    "ss2_prob_given_ss2_or_hs": 0.65,
                    "upper_lim_for_min_ss_span_length": 6.0,
                    "upper_lim_for_max_ss2_span_ratio": 2.0,
                    "staircase_slab_depth": 0.15,
                    "floor_slab_thickness": 0.15
                },
                "wb_prob_given_hs": 0.50,
                "square_column_prob": 0.50,
                "layout": "all",  # Considered layouts
                "seed": 1993  # Seed number for sampling
            },
            "bnsm": {
                "load_factors": {'G': 1.0, 'Q': 0.3},
                "mass_factors": {'G': 1.0, 'Q': 0.3},
                "scheme": 'EQL',  # 'FMP', 'EQL', 'MPP', 'TRI', 'UNI'
                "max_drift": 0.05,
                "dincr":  0.001,  # in meters
                "opensees": 'py'  # or tcl
            }
        }

    # Run the bed-workflow for rcmrf systems and save the outputs
    bcim, bdim, bnsm = rcmrf.generate(inputs=inputs, outdir="Outputs")

For more examples, please see the ``scripts`` folder in the repository.

2.3. Geometry-Specific Design
----------------------------------

It is possible to design and visualize buildings with specific geometries:

- `Example of standard frame geometry <https://htmlpreview.github.io/?https://raw.githubusercontent.com/builtenvdata/simulated-design/main/tmp/simple-uniform-geometry.html>`_

- `Example of custom frame geometry <https://htmlpreview.github.io/?https://raw.githubusercontent.com/builtenvdata/simulated-design/main/tmp/irregular-geometry.html>`_

