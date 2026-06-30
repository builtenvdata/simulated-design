"""A modular computational framework for the generation and nonlinear
modelling of reinforced concrete (RC) moment-resisting frames (MRFs).
It orchestrates the BCIM → BDIM → BNSM pipeline, generating portfolio-level
building class and design information data (exported CSV files), alongside
OpenSees-compatible nonlinear numerical models (in Python or Tcl).
:meth:`simdesign.rcmrf.generate` serves as the entry point for running the
pipeline.

Pipeline::

    BCIM (Realisation Layer)
            ↓
    BDIM (Design Layer)
            ↓
    BNSM (Modelling Layer)
            ↓
    OpenSees (Analysis Layer)
"""

from typing import Dict, Literal, Tuple, List
from pathlib import Path

from .bcim import BCIM
from .bdim import BDIM, TaxonomyData
from .bdim.factory import BuildingBase as BuildingDesign
from .bnsm import BNSM
from .bnsm.factory import BuildingBase as BuildingModel
from .geometry import StandardGeometry, CustomGeometry

from ..utils.misc import make_dir


__all__ = ["BCIM", "BDIM", "BNSM",
           "TaxonomyData", "StandardGeometry", "CustomGeometry"]


def generate(
    inputs: Dict[Literal['bcim', 'bnsm'], Dict], outdir: str | Path = None
) -> Tuple[BCIM, List[BuildingDesign | None], List[BuildingModel | None]]:
    """Generates BCIM, BDIM and BNSM data by following complete workflow
    in Built Data Environment (BED) SimDesign framework for RC-MRF systems.

    Parameters
    ----------
    inputs : Dict[Literal['bcim', 'bnsm'], Dict]
        Contains input parameters required for data generation.
        These will replace the defaults obtained for the specified
        `design_class`.
    outdir : str | Path, optional
        Path to the user-defined output directory.
        If None, set to `Path.cwd() / 'Outputs'`. by default None.

    Returns
    -------
    bcim : BCIM
        Building Class Information Model.
    bdim : List[BuildingDesign | None]
        List of Building Design Information Models (None if design failed).
    bnsm : List[BuildingModel | None]
        List of Building Nonlinear Structural Models (None if design failed).

    Raises
    ------
    KeyError
        `inputs['bcim']['design_class']` is not specified.

    Examples
    --------
    Example dictionary to pass as ``inputs``:

    .. code-block:: python

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
                    "upper_bound": 3.2,
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
                    "probability": [0.10, 0.90],
                },
                "concrete": {
                    "tag": ["C20/25", "C25/30", "C30/37", "C35/45"],
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
                    "floor_slab_thickness": 0.15,
                },
                "wb_prob_given_hs": 0.50,
                "square_column_prob": 0.50,
                "layout": "all",
                "seed": 1993,
            },
            "bnsm": {
                "model": "CP03",
                "load_factors": {"G": 1.0, "Q": 0.3},
                "mass_factors": {"G": 1.0, "Q": 0.3},
                "scheme": "EQL",
                "max_drift": 0.05,
                "dincr": 0.001,
                "opensees": "py",
            },
        }
    """

    # Get bcim generation settings
    bcim_inputs = inputs.get('bcim')
    if not bcim_inputs or not bcim_inputs.get('design_class'):
        raise KeyError('design_class in bcim is not specified!')

    # Get bnsm settings
    bnsm_inputs = inputs.get('bnsm')
    lang = 'py'
    if bnsm_inputs is None:
        bnsm_inputs = {}
    elif bnsm_inputs.get('opensees'):
        lang = bnsm_inputs.pop('opensees')

    # Create output directory
    if outdir is None:
        outdir = Path.cwd() / 'Outputs'
    else:
        outdir = Path(outdir)
    bcim_path = outdir / "BCIM.csv"
    bdim_path = outdir / 'BDIM'
    bnsm_path = outdir / 'BNSM'
    make_dir(outdir)
    make_dir(bdim_path)
    make_dir(bnsm_path)

    # Initialize BCIM
    bcim = BCIM()
    # Generate a building portfolio
    bcim.generate(**bcim_inputs)
    # BDIM database
    bdim = []
    # BNSM database
    bnsm = []
    # Loop through each building in portfolio
    for i, taxonomy in enumerate(bcim.taxonomy):
        print("----------------------------------------------------")
        print(f"Designing {taxonomy.design_class} building",
              f"{i + 1}/{len(bcim.taxonomy)} for beta={taxonomy.beta}g")
        # Initialize BDIM
        bdim_ = BDIM(taxonomy)
        # To ensure the reproducibility of BDIM set the seed
        bdim_.set_seed_for_quality_adjustments(bcim.inputs.seed)
        # Make simumlated design
        bdim_.run_iterative_design_algorithm()
        # Update BCIM in case some properties changed during design
        if bdim_.ok:  # If the design is ok, continue with the model
            bcim.column_section[i] = bdim_.column_section
            bcim.beam_type[i] = bdim_.beam_type
            bcim.concrete_grade[i] = bdim_.concrete_grade
            bcim.steel_grade[i] = bdim_.steel_grade
            # Export to csv
            bdim_.to_csv(bdim_path / f'Building_{i + 1}')
            # Initialize BNSM
            kwargs = bnsm_inputs.copy()
            kwargs['design'] = bdim_
            bnsm_ = BNSM(**kwargs)
            if lang == 'py':
                # Export numerical models for OpenSeesPy
                bnsm_.to_py(bnsm_path / f'Building_{i + 1}')
            elif lang == 'tcl':
                # Export numerical models for OpenSeesTcl
                bnsm_.to_tcl(bnsm_path / f'Building_{i + 1}')
            # Plot the model and save
            bnsm_.plot_model(directory=bnsm_path / f'Building_{i + 1}',
                             show=False)
            # Add to the BDIM and BNSM databases
            bdim.append(bdim_)
            bnsm.append(bnsm_)
        else:
            bdim.append(None)
            bnsm.append(None)
    # Save bcim information
    bcim.to_csv(bcim_path)

    return bcim, bdim, bnsm
