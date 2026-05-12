"""Integration tests for rcmrf.generate across all design classes."""
import pytest
from pathlib import Path
import sys

# Add the project root to sys.path
sys.path.append(str(Path(__file__).parents[1]))

from simdesign import rcmrf  # noqa
from simdesign.utils.misc import remove_dir  # noqa


@pytest.fixture
def base_inputs_opspy():
    """Return base inputs for the OpenSeesPy workflow."""
    return {
        'bcim': {
            'sample_size': 2,
            'num_storeys': 2,
            'beta': 0.05
        },
        'bnsm': {
            'opensees': 'py'
        }
    }


@pytest.mark.parametrize("design_class", [
    "eu_cdn",
    "eu_cdl",
    "eu_cdm",
    "eu_cdh",
    "tr_7599",
    "tr_0018_dcm",
    "tr_0018_dch",
    "tr_post18_dcm",
    "tr_post18_dch"
])
def test_rcmrf_opspy(base_inputs_opspy, design_class):
    """Test rcmrf.generate for each design class using the OpenSeesPy
    workflow.
    """
    base_inputs_opspy['bcim']['design_class'] = design_class
    outdir = Path(__file__).parent / f"{design_class}"
    rcmrf.generate(base_inputs_opspy, outdir)
    remove_dir(outdir)


@pytest.fixture
def base_inputs_opstcl():
    """Return base inputs for the OpenSeesTcl workflow."""
    return {
        'bcim': {
            'sample_size': 2,
            'num_storeys': 2,
            'beta': 0.05
        },
        'bnsm': {
            'opensees': 'tcl'
        }
    }


@pytest.mark.parametrize("design_class", [
    "eu_cdn",
    "eu_cdl",
    "eu_cdm",
    "eu_cdh",
    "tr_7599",
    "tr_0018_dcm",
    "tr_0018_dch",
    "tr_post18_dcm",
    "tr_post18_dch"
])
def test_rcmrf_opstcl(base_inputs_opstcl, design_class):
    """Test rcmrf.generate for each design class using the OpenSeesTcl
    workflow."""
    base_inputs_opstcl['bcim']['design_class'] = design_class
    outdir = Path(__file__).parent / f"{design_class}"
    rcmrf.generate(base_inputs_opstcl, outdir)
    remove_dir(outdir)
