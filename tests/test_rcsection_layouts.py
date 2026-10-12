"""Tests for the rebar layouts, the Mander confinement model and the input
checks of the simplified section analysis."""
import sys
from pathlib import Path
import numpy as np
import pytest

# Add the project root to sys.path
sys.path.append(str(Path(__file__).parents[1]))

from simdesign.utils.rcsection import (  # noqa
    build_column_rebar_layout, build_beam_rebar_layout, get_sum_wi_sq,
    get_mander_confinement, do_simplified_section_analysis
)
from simdesign.utils.units import MPa  # noqa

# Column section in mm: 300 x 400, cover 25, hoops 8, corner bars 16 and one
# intermediate 14 bar per face
COLUMN = dict(dbl_cor=16, dbl_int=14, nbl_int_x=1, nbl_int_y=1, dbh=8,
              lx=300, ly=400, cv=25)


def mander(s: float, legs: int = 2, fc: float = 25.0) -> dict:
    """Mander confinement of the column section for a hoop spacing s."""
    layout = build_column_rebar_layout(**COLUMN)
    return get_mander_confinement(
        fc=fc, Lx=COLUMN['lx'], Ly=COLUMN['ly'], cover=COLUMN['cv'],
        db_v=COLUMN['dbh'], s=s, legs_x=legs, legs_y=legs, fy_v=420,
        rein_x=layout['rein_x'], rein_y=layout['rein_y'],
        rein_d=layout['rein_d'])


def test_column_layout():
    """Corner and intermediate bars of a column lie inside the section, at
    the cover plus the hoop and half the bar diameter."""
    layout = build_column_rebar_layout(**COLUMN)
    assert len(layout['rein_d']) == 4 + 2 * 1 + 2 * 1
    x, y, d = map(np.asarray, (layout['rein_x'], layout['rein_y'],
                               layout['rein_d']))
    edge = COLUMN['cv'] + COLUMN['dbh'] + d / 2
    assert np.all(x >= edge - 1e-9)
    assert np.all(x <= COLUMN['lx'] - edge + 1e-9)
    assert np.all(y >= edge - 1e-9)
    assert np.all(y <= COLUMN['ly'] - edge + 1e-9)
    assert sorted(set(d)) == [14, 16]


def test_beam_layout():
    """Beam bars are split into bottom and top bars of the given counts."""
    layout = build_beam_rebar_layout(16, 14, 16, 0, 2, 1, 2, 0, 8, 300,
                                     500, 25)
    assert len(layout['rein_db']) == 3
    assert len(layout['rein_dt']) == 2
    assert len(layout['rein_d']) == 5
    assert max(layout['rein_yb']) < min(layout['rein_yt'])


def test_sum_wi_sq():
    """The clear spacings between restrained bars are positive."""
    layout = build_column_rebar_layout(**COLUMN)
    wi, sum_wi_sq, counts = get_sum_wi_sq(
        layout['rein_x'], layout['rein_y'], layout['rein_d'])
    assert np.all(np.asarray(wi) > 0)
    assert sum_wi_sq == pytest.approx(np.sum(np.asarray(wi) ** 2))
    assert set(counts) == {'bottom', 'top', 'left', 'right'}


def test_mander_confinement_increases_strength_and_ductility():
    """Confined concrete is stronger and more ductile than unconfined
    concrete, and more so for closer hoops."""
    wide, close = mander(150), mander(75)
    for result in (wide, close):
        assert result['fcc'] > 25.0
        assert result['eps_cc'] > 0.002
        assert result['eps_cu'] > 0.004
        assert 0.0 < result['Ke'] < 1.0
    assert close['fcc'] > wide['fcc']
    assert close['eps_cu'] > wide['eps_cu']
    assert close['Ke'] > wide['Ke']


def test_mander_confinement_more_legs():
    """More hoop legs give more confinement."""
    assert mander(150, legs=3)['fcc'] > mander(150, legs=2)['fcc']


SECTION = dict(h=0.5, b=0.3, fc=25 * MPa, Ec=30e3 * MPa, Pext=0.0,
               fyL=400 * MPa, Es=200e3 * MPa)


@pytest.mark.parametrize('As_layers, y_layers', [
    ([1e-3], [0.05, 0.45]),          # lengths differ
    ([], []),                        # no layer
    ([1e-3, 1e-3], [0.45, 0.05]),    # not increasing
    ([-1e-3], [0.05]),               # negative area
    ([1e-3], [0.6]),                 # outside the section
])
def test_section_analysis_input_checks(As_layers, y_layers):
    """Invalid reinforcement layers raise an error."""
    with pytest.raises(ValueError):
        do_simplified_section_analysis(
            **SECTION, As_layers=As_layers, y_layers=y_layers)


def test_section_analysis_axial_load_raises_moment():
    """A moderate compressive axial load raises the yield moment."""
    layers = dict(As_layers=[8e-4, 8e-4], y_layers=[0.05, 0.45])
    My0 = do_simplified_section_analysis(**SECTION, **layers)[3]
    SECTION_N = dict(SECTION, Pext=500.0)
    My1 = do_simplified_section_analysis(**SECTION_N, **layers)[3]
    assert My1 > My0 > 0
