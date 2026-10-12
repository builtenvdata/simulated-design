"""Tests that build every BNSM model, run the gravity and modal analyses and
export the models, plus the BNSM input checks. Pushover analyses are left out
because they are slow."""
import sys
from pathlib import Path
import numpy as np
import pytest

# Add the project root to sys.path
sys.path.append(str(Path(__file__).parents[1]))

from simdesign import rcmrf  # noqa
from conftest import MATERIALS  # noqa

MODELS = ['CP01', 'CP02', 'CP03', 'DP01', 'DP02', 'DP03', 'DP04', 'DP05']


def first_periods(bnsm, num_modes: int = 3) -> np.ndarray:
    """Periods of the first modes (gravity analysis included)."""
    return np.array(bnsm.do_modal(num_modes=num_modes)['eigenPeriod'])


@pytest.mark.parametrize('design_class', list(MATERIALS))
@pytest.mark.parametrize('model', MODELS)
def test_modal_and_exports(designs, design_class, model, tmp_path):
    """Each model builds, carries the gravity loads, gives valid periods and
    exports to OpenSeesPy and Tcl."""
    bnsm = rcmrf.BNSM(design=designs[design_class], model=model,
                      include_infills=False)
    periods = first_periods(bnsm)
    assert len(periods) == 3
    assert np.all(np.isfinite(periods))
    assert np.all((periods > 0.05) & (periods < 5.0))
    assert np.all(np.diff(periods) <= 1e-9)  # sorted, longest first

    bnsm.to_py(tmp_path / 'py')
    bnsm.to_tcl(tmp_path / 'tcl')
    assert any((tmp_path / 'py').rglob('*.py'))
    assert any((tmp_path / 'tcl').rglob('*.tcl'))


@pytest.mark.parametrize('model', ['CP01', 'CP03', 'DP02', 'DP05'])
def test_infills_stiffen_the_frame(designs, model):
    """The infill struts shorten the fundamental period."""
    design = designs['eu_cdl']
    bare = first_periods(rcmrf.BNSM(design=design, model=model,
                                    include_infills=False), 1)
    infilled = first_periods(rcmrf.BNSM(design=design, model=model,
                                        include_infills=True), 1)
    assert infilled[0] < bare[0]


@pytest.mark.parametrize('model', ['DP01', 'DP04'])
def test_cracked_sections_soften_the_frame(designs, model):
    """Cracked elastic sections lengthen the fundamental period, and a
    stiffness ratio of 0.5 also does."""
    design = designs['eu_cdl']
    gross = first_periods(rcmrf.BNSM(design=design, model=model), 1)[0]
    cracked = first_periods(rcmrf.BNSM(
        design=design, model=model, cracked_beam=True,
        cracked_column=True), 1)[0]
    half = first_periods(rcmrf.BNSM(
        design=design, model=model, cracked_beam=0.5,
        cracked_column=0.5), 1)[0]
    assert cracked > gross
    assert half > gross


@pytest.mark.parametrize('beam_loads', ['uniform', 'point'])
@pytest.mark.parametrize('model', ['CP01', 'DP03'])
def test_beam_load_options(designs, model, beam_loads):
    """Both ways of applying the beam gravity loads give valid periods."""
    bnsm = rcmrf.BNSM(design=designs['eu_cdl'], model=model,
                      beam_loads=beam_loads)
    assert np.all(np.isfinite(first_periods(bnsm, 1)))


def test_cyclic_model_option(designs):
    """The cyclic model option gives valid periods."""
    bnsm = rcmrf.BNSM(design=designs['eu_cdl'], model='DP02',
                      cyclic_model=True)
    assert np.all(np.isfinite(first_periods(bnsm, 1)))


@pytest.mark.parametrize('value', ['auto', 1.5, -0.1, 0.0, [0.5]])
def test_invalid_cracked_values_raise(designs, value):
    """cracked_* accepts None, a bool or a number in (0, 1] only."""
    with pytest.raises(ValueError):
        rcmrf.BNSM(design=designs['eu_cdl'], model='DP01',
                   cracked_beam=value)


def test_cracked_integer_one_is_a_ratio(designs):
    """An integer 1 is the stiffness ratio 1.0, not True."""
    bnsm = rcmrf.BNSM(design=designs['eu_cdl'], model='DP01',
                      cracked_column=1)
    assert isinstance(bnsm.cracked_column, float)
    assert bnsm.cracked_column == 1.0


def test_unknown_input_warns(designs):
    """Inputs that the selected model does not accept are ignored with a
    warning."""
    with pytest.warns(UserWarning):
        rcmrf.BNSM(design=designs['eu_cdl'], model='DP01',
                   not_an_option=1)


@pytest.mark.parametrize('value, expected', [
    ('yes', True), ('off', False), (1, True), (0, False)])
def test_boolean_inputs(designs, value, expected):
    """Boolean inputs accept bools, 0/1 and yes/no style strings."""
    bnsm = rcmrf.BNSM(design=designs['eu_cdl'], model='DP01',
                      include_infills=value)
    assert bnsm.include_infills is expected


def test_invalid_boolean_input_raises(designs):
    """Other values of a boolean input raise an error."""
    with pytest.raises(ValueError):
        rcmrf.BNSM(design=designs['eu_cdl'], model='DP01',
                   include_infills='maybe')


def test_default_model_is_cp01(designs):
    """Without a model name, BNSM builds the CP01 model."""
    from simdesign.rcmrf.bnsm.cp01.building import Building as BuildingCP01
    bnsm = rcmrf.BNSM(design=designs['eu_cdl'])
    assert type(bnsm) is BuildingCP01


def test_invalid_model_raises(designs):
    """An unknown model name raises an error."""
    with pytest.raises(ValueError):
        rcmrf.BNSM(design=designs['eu_cdl'], model='XX01')
