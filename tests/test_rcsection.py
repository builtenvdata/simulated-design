"""Tests for the reinforced concrete section methods."""
import sys
from pathlib import Path
import numpy as np
import pytest

# Add the project root to sys.path
sys.path.append(str(Path(__file__).parents[1]))

from simdesign.utils.rcsection import (  # noqa
    do_simplified_section_analysis, get_my_phiy_panagiotakos_fardis2001,
    get_yield_rot_eurocode8, get_capping_mom_plastic_rot_haselton2016,
    get_residual_mom_post_capping_rot_haselton2016, get_lp_priestley_2007,
    get_shear_cracking_sezen_moehle2004, get_shear_strength_priestley1994,
    get_shear_strains_mergos_kappos2012, get_shear_post_peak_zimos2015,
    get_shear_residual_zimos2015,
    get_shear_strength_asce41_17, get_shear_stiffness_leborgne_ghannoum2014,
    get_shear_degrading_slope_shoraka_elwood2013,
    _get_vrc_ec2, _get_av_ec8
)
from simdesign.utils.units import MPa  # noqa

# Materials in base units (kN, m)
FC, EC, ES, FY = 25 * MPa, 30e3 * MPa, 200e3 * MPa, 400 * MPa


def bar_area(diameter: float) -> float:
    """Area of a circular bar."""
    return 0.25 * np.pi * diameter**2


def reference_yield_point(h, b, fc, Ec, Es, fy, As_tens, As_comp, dd,
                          As_int=0.0, Nu=0.0, eps_cu=0.0035):
    """Scalar implementation of Equations 1 to 6 of Panagiotakos and Fardis
    (2001) with explicit branches for the yielding control.

    Returns the yield moment, the yield curvature, the compression zone
    depth, and True if yielding is controlled by the tension steel (False if
    by the compression zone).
    """
    if fc < 27.6 * MPa:
        betac = 0.85
    elif fc > 55.17 * MPa:
        betac = 0.65
    else:
        betac = 1.05 - 0.05 * fc / (6.9 * MPa)
    n = Es / Ec
    delta = (h - dd) / dd
    cb = eps_cu * dd / (eps_cu + fy / Es)
    rho_t, rho_c, rho_i = (A / (b * dd) for A in (As_tens, As_comp, As_int))
    c = (As_tens * fy - As_comp * fy + Nu) / (0.85 * fc * b * betac)
    tension_controlled = c < cb
    if tension_controlled:  # Equation 4
        A = rho_t + rho_c + rho_i + Nu / (b * dd * fy)
        B = (rho_t + rho_c * delta + 0.5 * rho_i * (1 + delta)
             + Nu / (b * dd * fy))
    else:  # Equation 5
        A = rho_t + rho_c + rho_i - Nu / (1.8 * n * b * dd * fc)
        B = rho_t + rho_c * delta + 0.5 * rho_i * (1 + delta)
    ky = np.sqrt((n * A)**2 + 2 * n * B) - n * A  # Equation 3
    if tension_controlled:  # Equation 1
        phi_y = fy / (Es * (1 - ky) * dd)
    else:  # Equation 2
        phi_y = 1.8 * fc / (Ec * ky * dd)
    # Equation 6
    My = b * dd**3 * phi_y * (
        Ec * ky**2 / 2 * (0.5 * (1 + delta) - ky / 3)
        + Es / 2 * ((1 - ky) * rho_t + (ky - delta) * rho_c
                    + rho_i / 6 * (1 - delta)) * (1 - delta)
    )
    return My, phi_y, ky * dd, tension_controlled


def column_inputs(Nu: float) -> dict:
    """Inputs of a 0.4 x 0.4 m column: 3 bars of 16 mm on each face and two
    16 mm web bars, with axial load `Nu` (kN, compression positive)."""
    h = b = 0.4
    dd = h - 0.03 - 0.008 - 0.5 * 0.016
    return dict(h=h, b=b, fc=FC, Ec=EC, Es=ES, fsyl=FY,
                As_tens=3 * bar_area(0.016), As_comp=3 * bar_area(0.016),
                dd=dd, As_int=2 * bar_area(0.016), Nu=Nu)


def beam_inputs(rho_tens: float, rho_comp: float) -> dict:
    """Inputs of a 0.3 x 0.6 m beam with the given reinforcement ratios,
    computed on the effective area b.dd."""
    h, b = 0.6, 0.3
    dd = h - 0.03 - 0.008 - 0.5 * 0.02
    return dict(h=h, b=b, fc=FC, Ec=EC, Es=ES, fsyl=FY,
                As_tens=rho_tens * b * dd, As_comp=rho_comp * b * dd, dd=dd)


def reference_from_inputs(inputs: dict):
    """Evaluates the reference implementation for scalar inputs."""
    ref = dict(inputs)
    ref['fy'] = ref.pop('fsyl')
    return reference_yield_point(**ref)


CASES = {
    'beam, tension controlled': (beam_inputs(0.010, 0.005), True),
    'beam, over-reinforced': (beam_inputs(0.045, 0.002), False),
    'column, no axial load': (column_inputs(0.0), True),
    'column, moderate axial load': (column_inputs(400.0), True),
    'column, high axial load': (column_inputs(2400.0), False),
}


@pytest.mark.parametrize('name', list(CASES))
def test_yield_point_matches_reference(name: str) -> None:
    """The vectorised helper reproduces the explicit-branch implementation of
    the equations in both yielding control regimes."""
    inputs, tension_controlled = CASES[name]
    My_ref, phi_ref, cy_ref, control = reference_from_inputs(inputs)
    assert control == tension_controlled, 'The case does not test its branch'
    My, phi_y, cy = get_my_phiy_panagiotakos_fardis2001(**inputs)
    assert My == pytest.approx(My_ref, rel=1e-12)
    assert phi_y == pytest.approx(phi_ref, rel=1e-12)
    assert cy == pytest.approx(cy_ref, rel=1e-12)
    assert My > 0.0 and phi_y > 0.0 and 0.0 < cy < inputs['dd']


def test_yield_point_scalar_inputs_return_scalars() -> None:
    """Scalar inputs give scalar outputs."""
    My, phi_y, cy = get_my_phiy_panagiotakos_fardis2001(
        **column_inputs(400.0))
    assert np.ndim(My) == 0 and np.ndim(phi_y) == 0 and np.ndim(cy) == 0
    assert isinstance(float(My), float) and isinstance(float(phi_y), float)


def test_yield_point_arrays_with_mixed_control() -> None:
    """Array inputs, e.g., the start, mid and end sections of a beam, are
    evaluated section by section, with a different control per section."""
    normal, over = beam_inputs(0.010, 0.005), beam_inputs(0.045, 0.002)
    keys = ('As_tens', 'As_comp')
    inputs = dict(normal)
    for key in keys:
        inputs[key] = np.array([normal[key], over[key], normal[key]])
    My, phi_y, cy = get_my_phiy_panagiotakos_fardis2001(**inputs)
    assert My.shape == (3,) and phi_y.shape == (3,) and cy.shape == (3,)
    for i, source in enumerate((normal, over, normal)):
        My_ref, phi_ref, cy_ref, _ = reference_from_inputs(source)
        assert My[i] == pytest.approx(My_ref, rel=1e-12)
        assert phi_y[i] == pytest.approx(phi_ref, rel=1e-12)
        assert cy[i] == pytest.approx(cy_ref, rel=1e-12)
    # Inputs are not modified
    assert inputs['As_tens'][1] == over['As_tens']


def test_yield_point_dd_prime_default() -> None:
    """The compression steel is at ``h - dd`` from the compression fiber
    unless ``dd_prime`` is given."""
    inputs = column_inputs(400.0)
    default = get_my_phiy_panagiotakos_fardis2001(**inputs)
    explicit = get_my_phiy_panagiotakos_fardis2001(
        **inputs, dd_prime=inputs['h'] - inputs['dd'])
    farther = get_my_phiy_panagiotakos_fardis2001(
        **inputs, dd_prime=inputs['h'] - inputs['dd'] + 0.03)
    assert explicit == default
    assert farther != default


@pytest.mark.parametrize('name', ['beam, tension controlled',
                                  'column, no axial load',
                                  'column, moderate axial load'])
def test_yield_point_close_to_section_analysis(name: str) -> None:
    """The empirical expressions are close to the first-yield point of the
    moment-curvature analysis of the same section (loose, independent check
    of the units and of the equations)."""
    inputs, _ = CASES[name]
    My, _, _ = get_my_phiy_panagiotakos_fardis2001(**inputs)
    h, dd = inputs['h'], inputs['dd']
    layers = [(h - dd, inputs['As_comp'])]
    if inputs.get('As_int', 0.0) > 0.0:
        layers.append((h / 2, inputs['As_int']))
    layers.append((dd, inputs['As_tens']))
    _, _, _, My_section, _, _ = do_simplified_section_analysis(
        h=h, b=inputs['b'], fc=FC, Ec=EC, Pext=inputs.get('Nu', 0.0),
        fyL=FY, Es=ES, As_layers=[A for _, A in layers],
        y_layers=[y for y, _ in layers])
    assert My == pytest.approx(My_section, rel=0.10)


def test_yield_rot_eurocode8_hand_calculation() -> None:
    """Hand calculation of EN 1998-3 Eq. (A.10b) for phi_y = 0.008 1/m,
    h = 0.5 m, Ls = 1.5 m, fc = 25 MPa, fy = 400 MPa and db = 16 mm, with the
    lever arm z = 0.9 (0.9 h) = 0.405 m:

    - flexure and tension shift: 0.008 (1.5 + 0.405) / 3 = 0.00508
    - shear: 0.0014 (1 + 1.5 0.5 / 1.5) = 0.0021
    - bond-slip: 0.125 0.008 0.016 400 / sqrt(25) = 0.00128
    """
    inputs = dict(phi_y=0.008, h=0.5, Ls=1.5, fc=25 * MPa, fsyl=400 * MPa,
                  db=0.016, av=1.0)
    assert get_yield_rot_eurocode8(**inputs) == pytest.approx(0.00846,
                                                              rel=1e-12)
    # No bond-slip
    assert get_yield_rot_eurocode8(
        **inputs, bondslip_factor=0.0) == pytest.approx(0.00718, rel=1e-12)
    # No tension shift: 0.008 1.5 / 3 + 0.0021 + 0.00128
    assert get_yield_rot_eurocode8(
        **{**inputs, 'av': 0.0}) == pytest.approx(0.00738, rel=1e-12)
    # Lever arm given explicitly: 0.008 (1.5 + 0.4) / 3 + 0.0021 + 0.00128
    assert get_yield_rot_eurocode8(
        **inputs, z=0.4) == pytest.approx(0.0084467, rel=1e-5)


def test_yield_rot_eurocode8_arrays() -> None:
    """Arrays, e.g., the sections of a beam, are evaluated element by
    element."""
    phi_y = np.array([0.006, 0.008, 0.010])
    theta = get_yield_rot_eurocode8(
        phi_y, 0.5, 1.5, 25 * MPa, 400 * MPa, np.array([0.016, 0.016, 0.02]),
        av=1.0)
    assert theta.shape == (3,)
    for i in range(3):
        db = [0.016, 0.016, 0.02][i]
        assert theta[i] == pytest.approx(get_yield_rot_eurocode8(
            phi_y[i], 0.5, 1.5, 25 * MPa, 400 * MPa, db, av=1.0),
            rel=1e-12)


# Column of Table 2 of Haselton et al. (2016): axial load ratio 0.25, ratio
# of longitudinal reinforcement 0.02, ratio of transverse reinforcement
# 0.0075, bar slenderness sn = 12.7, fc = 30 MPa, bond-slip included. With
# fy = 400 MPa and 20 mm bars, sn = 12.7 is a tie spacing of 127 mm.
BASELINE = dict(niu=0.25, rhol=0.02, rhoh=0.0075, sn=12.7, fc=30.0,
                bondslip_factor=1.0)
# Name: (changed parameters, theta_cap_pl, theta_pc) of Table 2. The values
# are rounded to 3 decimals. The rows of an axial load ratio of 0.4 and of the
# transverse reinforcement ratio of 0.002 (post-capping rotation) of the
# printed table do not follow Equations 5 and 8 and are not included.
HASELTON_TABLE_2 = {
    'baseline': ({}, 0.042, 0.100),
    'niu = 0.0': (dict(niu=0.0), 0.066, 0.100),
    'niu = 0.8': (dict(niu=0.8), 0.015, 0.015),
    'rhol = 0.01': (dict(rhol=0.01), 0.038, None),
    'rhol = 0.03': (dict(rhol=0.03), 0.045, None),
    'rhoh = 0.002': (dict(rhoh=0.002), 0.025, None),
    'rhoh = 0.010': (dict(rhoh=0.010), 0.047, 0.100),
    'rhoh = 0.020': (dict(rhoh=0.020), 0.062, 0.100),
    'sn = 8': (dict(sn=8.0), 0.051, None),
    'sn = 16': (dict(sn=16.0), 0.036, None),
    'sn = 20': (dict(sn=20.0), 0.031, None),
    'fc = 40 MPa': (dict(fc=40.0), 0.039, None),
    'fc = 80 MPa': (dict(fc=80.0), 0.031, None),
    'no bond-slip': (dict(bondslip_factor=0.0), 0.027, None),
}


@pytest.mark.parametrize('name', list(HASELTON_TABLE_2))
def test_haselton_rotation_capacities_table_2(name: str) -> None:
    """The plastic and post-capping rotation capacities reproduce the
    predictions of Haselton et al. (2016) printed in their Table 2."""
    changes, theta_cap_pl_ref, theta_pc_ref = HASELTON_TABLE_2[name]
    p = {**BASELINE, **changes}
    dbl = 0.020
    My = 100.0
    # sn = (sbh / dbl) sqrt(fsyl / 100), with fsyl = 400 MPa
    Mc, theta_cap_pl = get_capping_mom_plastic_rot_haselton2016(
        My, p['fc'] * MPa, 400 * MPa, p['rhol'], p['rhoh'],
        sbh=p['sn'] * dbl / 2, dbl=dbl, niu=p['niu'],
        bondslip_factor=p['bondslip_factor'])
    _, theta_pc = get_residual_mom_post_capping_rot_haselton2016(
        Mc, p['rhoh'], p['niu'])
    assert theta_cap_pl == pytest.approx(theta_cap_pl_ref, abs=6e-4)
    if theta_pc_ref is not None:
        assert theta_pc == pytest.approx(theta_pc_ref, abs=6e-4)


def test_haselton_capping_moment() -> None:
    """Mc / My = 1.25 (0.89^niu) (0.91^(0.01 fc)), from Haselton et al.
    (2008), and 1 for no axial load and fc = 0 MPa gives 1.25."""
    args = dict(fsyl=400 * MPa, rhol=0.02, rhoh=0.0075, sbh=0.1, dbl=0.02)
    Mc, _ = get_capping_mom_plastic_rot_haselton2016(
        100.0, fc=30 * MPa, niu=0.25, **args)
    assert Mc == pytest.approx(
        100.0 * 1.25 * 0.89**0.25 * 0.91**0.3, rel=1e-12)
    Mc, _ = get_capping_mom_plastic_rot_haselton2016(
        100.0, fc=1e-9 * MPa, niu=0.0, **args)
    assert Mc == pytest.approx(125.0, rel=1e-6)


def test_haselton_residual_moment_and_cap_of_post_capping_rotation() -> None:
    """The residual moment is a fraction of the capping moment (10% by
    default) and the post-capping rotation capacity is limited to 0.10."""
    Mr, theta_pc = get_residual_mom_post_capping_rot_haselton2016(
        200.0, rhoh=0.0075, niu=0.0)
    assert Mr == pytest.approx(20.0, rel=1e-12)
    assert theta_pc == 0.10  # 0.76 (0.32^1.02) = 0.2377 is limited
    Mr, _ = get_residual_mom_post_capping_rot_haselton2016(
        200.0, rhoh=0.0075, niu=0.0, Mr_Mc=0.2)
    assert Mr == pytest.approx(40.0, rel=1e-12)
    # Below the limit: 0.76 0.031^0.8 0.32^1.02
    _, theta_pc = get_residual_mom_post_capping_rot_haselton2016(
        200.0, rhoh=0.0075, niu=0.8)
    assert theta_pc == pytest.approx(
        0.76 * 0.031**0.8 * 0.32**1.02, rel=1e-12)
    assert theta_pc < 0.10


def test_haselton_functions_arrays_not_modified() -> None:
    """Arrays, e.g., the sections of a beam, are evaluated element by element
    and the inputs are not modified."""
    My = np.array([80.0, 100.0, 80.0])
    rhoh = np.array([0.004, 0.0015, 0.004])  # The second is limited
    rhoh_copy = rhoh.copy()
    Mc, theta_cap_pl = get_capping_mom_plastic_rot_haselton2016(
        My, 25 * MPa, 400 * MPa, np.array([0.01, 0.015, 0.01]), rhoh,
        np.array([0.1, 0.1, 0.1]), np.array([0.02, 0.02, 0.02]))
    Mr, theta_pc = get_residual_mom_post_capping_rot_haselton2016(Mc, rhoh)
    assert Mc.shape == theta_cap_pl.shape == Mr.shape == theta_pc.shape == (3,)
    assert np.array_equal(Mr, 0.1 * Mc)
    assert np.array_equal(rhoh, rhoh_copy)
    assert np.all(theta_pc <= 0.10)
    assert theta_cap_pl[0] == pytest.approx(theta_cap_pl[2], rel=1e-12)


def test_yield_rot_eurocode8_without_shear() -> None:
    """The shear term 0.0014 (1 + 1.5 h / Ls) = 0.0021 is left out."""
    inputs = dict(phi_y=0.008, h=0.5, Ls=1.5, fc=25 * MPa, fsyl=400 * MPa,
                  db=0.016, av=1.0)
    with_shear = get_yield_rot_eurocode8(**inputs)
    without_shear = get_yield_rot_eurocode8(**inputs, include_shear=False)
    assert without_shear == pytest.approx(0.00636, rel=1e-12)
    assert with_shear - without_shear == pytest.approx(0.0021, rel=1e-9)
    # The default includes the shear term
    assert get_yield_rot_eurocode8(
        **inputs, include_shear=True) == with_shear
    # Arrays
    theta = get_yield_rot_eurocode8(
        np.array([0.006, 0.008]), 0.5, 1.5, 25 * MPa, 400 * MPa, 0.016,
        av=1.0, include_shear=False)
    assert theta.shape == (2,)
    assert theta[1] == pytest.approx(0.00636, rel=1e-12)


def haselton_args(**changes) -> dict:
    """Inputs of the capping moment and plastic rotation capacity."""
    args = dict(My=100.0, fc=25 * MPa, fsyl=400 * MPa, rhol=0.02,
                rhoh=0.0075, sbh=0.1, dbl=0.02, niu=0.25)
    args.update(changes)
    return args


def test_haselton_cyclic_model() -> None:
    """For cyclic loading, the plastic rotation capacity is multiplied by
    0.7 and the post-capping rotation capacity by 0.5, and the moments are
    not changed."""
    Mc, theta_cap_pl = get_capping_mom_plastic_rot_haselton2016(
        **haselton_args())
    Mc_cyc, theta_cap_pl_cyc = get_capping_mom_plastic_rot_haselton2016(
        **haselton_args(), cyclic_model=True)
    assert Mc_cyc == Mc
    assert theta_cap_pl_cyc == pytest.approx(0.7 * theta_cap_pl, rel=1e-12)
    for niu, limited in ((0.8, False), (0.0, True)):
        Mr, theta_pc = get_residual_mom_post_capping_rot_haselton2016(
            Mc, 0.0075, niu)
        Mr_cyc, theta_pc_cyc = get_residual_mom_post_capping_rot_haselton2016(
            Mc, 0.0075, niu, cyclic_model=True)
        assert (theta_pc == 0.10) == limited
        assert Mr_cyc == Mr
        # The limit of 0.10 applies before the reduction
        assert theta_pc_cyc == pytest.approx(0.5 * theta_pc, rel=1e-12)


def test_haselton_non_symmetric_section() -> None:
    """The plastic rotation capacity is multiplied by
    ``(w_comp / w_tens)^0.225``, with the mechanical reinforcement ratios
    ``w = rhol fsyl / fc`` (floored at 0.01) on the compression and tension
    sides. Here ``fsyl / fc = 16``."""
    _, symmetric = get_capping_mom_plastic_rot_haselton2016(**haselton_args())
    Mc_sym, _ = get_capping_mom_plastic_rot_haselton2016(**haselton_args())

    def capacity(rhol_tens, rhol_comp, **kwargs):
        return get_capping_mom_plastic_rot_haselton2016(
            **haselton_args(), rhol_tens=rhol_tens, rhol_comp=rhol_comp,
            **kwargs)

    # More reinforcement in compression: w_comp / w_tens = 0.32 / 0.16 = 2
    Mc, theta = capacity(0.01, 0.02)
    assert theta == pytest.approx(2**0.225 * symmetric, rel=1e-12)
    assert Mc == Mc_sym  # The moment does not depend on the direction
    # The opposite bending direction
    _, theta = capacity(0.02, 0.01)
    assert theta == pytest.approx(2**-0.225 * symmetric, rel=1e-12)
    # Same reinforcement on both sides
    _, theta = capacity(0.015, 0.015)
    assert theta == pytest.approx(symmetric, rel=1e-12)
    # Both mechanical ratios are below 0.01 and floored: ratio of 1
    _, theta = capacity(0.0001, 0.0002)
    assert theta == pytest.approx(symmetric, rel=1e-12)
    # With the cyclic reduction
    _, theta = capacity(0.01, 0.02, cyclic_model=True)
    assert theta == pytest.approx(0.7 * 2**0.225 * symmetric, rel=1e-12)
    # Arrays, e.g., the sections of a beam
    _, theta = capacity(np.array([0.01, 0.02, 0.01]),
                        np.array([0.02, 0.01, 0.02]))
    assert theta[0] == pytest.approx(2**0.225 * symmetric, rel=1e-12)
    assert theta[1] == pytest.approx(2**-0.225 * symmetric, rel=1e-12)
    assert theta[2] == theta[0]


def test_haselton_non_symmetric_section_needs_both_ratios() -> None:
    """The reinforcement ratios of the tension and compression sides must be
    given together."""
    with pytest.raises(ValueError):
        get_capping_mom_plastic_rot_haselton2016(
            **haselton_args(), rhol_tens=0.01)
    with pytest.raises(ValueError):
        get_capping_mom_plastic_rot_haselton2016(
            **haselton_args(), rhol_comp=0.01)


def vrc_beam_inputs(**changes) -> dict:
    """Inputs of the shear resistance of a 300 x 500 mm beam with 3 bars of
    16 mm and an effective depth of 450 mm (base units)."""
    inputs = dict(b_w=0.3, d=0.45, A_sl=3 * np.pi / 4 * 0.016**2,
                  f_ck=25 * MPa)
    inputs.update(changes)
    return inputs


def test_calculate_vrc_ec2_regimes() -> None:
    """Shear resistance of EN 1992-1-1 6.2.2 in its regimes, with the
    expected values from the expressions: k = 1 + sqrt(200 / d) = 1.6667,
    rho_l = 0.00447 and v = 0.18 k (100 rho_l f_ck)^(1/3) = 0.6706 MPa."""
    # Standard expression: 0.6706 x 300 x 450 = 90.53 kN
    assert _get_vrc_ec2(**vrc_beam_inputs()) == pytest.approx(
        90.533, rel=1e-5)
    # Minimum shear stress: v_min = 0.035 k^1.5 sqrt(25) governs for a very
    # low reinforcement ratio
    k = 1 + np.sqrt(200 / 450)
    v_min = 0.035 * k**1.5 * 5.0
    assert _get_vrc_ec2(
        **vrc_beam_inputs(A_sl=0.0005 * 0.3 * 0.45)) == pytest.approx(
            v_min * 300 * 450 / 1e3, rel=1e-12)
    # Axial force of 300 kN on 300 x 500 mm: sigma_cp = 2 MPa adds 0.15 x 2
    rho_l = 3 * np.pi / 4 * 16**2 / (300 * 450)
    v = 0.18 * k * (100 * rho_l * 25) ** (1 / 3)
    assert _get_vrc_ec2(
        **vrc_beam_inputs(), N_Ed=300.0, h=0.5) == pytest.approx(
            (v + 0.15 * 2.0) * 300 * 450 / 1e3, rel=1e-12)
    # Axial stress is limited to 0.2 f_cd = 5 MPa
    assert _get_vrc_ec2(
        **vrc_beam_inputs(), N_Ed=2000.0, h=0.5) == pytest.approx(
            (v + 0.15 * 5.0) * 300 * 450 / 1e3, rel=1e-12)
    # Tension does not change the resistance
    assert _get_vrc_ec2(
        **vrc_beam_inputs(), N_Ed=-100.0) == _get_vrc_ec2(
            **vrc_beam_inputs())
    # Size effect factor limited to 2 and reinforcement ratio to 0.02
    assert _get_vrc_ec2(
        b_w=0.3, d=0.1, A_sl=0.01 * 0.3 * 0.1,
        f_ck=25 * MPa) == pytest.approx(31.5794, rel=1e-6)
    assert _get_vrc_ec2(
        **vrc_beam_inputs(A_sl=0.05 * 0.3 * 0.45)) == pytest.approx(
            149.2033, rel=1e-6)


def test_calculate_vrc_ec2_shapes() -> None:
    """Scalars give a float, lists and arrays are evaluated element by
    element."""
    assert isinstance(_get_vrc_ec2(**vrc_beam_inputs()), float)
    inputs = dict(b_w=[0.3, 0.3, 0.25], d=[0.45, 0.1, 0.8],
                  A_sl=[6e-4, 4e-4, 9e-3],
                  f_ck=[25 * MPa, 25 * MPa, 40 * MPa],
                  N_Ed=[0.0, 100.0, 2000.0], h=[0.5, 0.12, 0.9])
    V = _get_vrc_ec2(**inputs)
    assert V.shape == (3,)
    for i in range(3):
        assert V[i] == pytest.approx(_get_vrc_ec2(
            **{key: value[i] for key, value in inputs.items()}), rel=1e-12)


def test_get_av_eurocode8() -> None:
    """``av`` is 0 if the yield moment is lower than the shear span times the
    shear resistance, i.e., if flexural yielding precedes shear cracking."""
    # My / Ls = 100 / 1.5 = 66.7 kN
    assert _get_av_ec8(100.0, 1.5, 50.0) == 1.0  # Cracking first
    assert _get_av_ec8(100.0, 1.5, 80.0) == 0.0  # Yielding first
    assert _get_av_ec8(100.0, 2.0, 50.0) == 1.0  # Equal: My = Ls VRc
    assert isinstance(float(_get_av_ec8(100.0, 1.5, 50.0)), float)
    assert np.ndim(_get_av_ec8(100.0, 1.5, 50.0)) == 0
    # Arrays, e.g., the sections of a beam
    av = _get_av_ec8(np.array([100.0, 100.0, 100.0]), 1.5,
                     np.array([50.0, 80.0, 66.0]))
    assert av.shape == (3,)
    assert np.array_equal(av, [1.0, 0.0, 1.0])


def test_get_av_eurocode8_with_shear_resistance() -> None:
    """With the shear resistance of the concrete of the 300 x 500 mm beam,
    90.5 kN: a beam with a shear span of 2.5 m and a yield moment of 100 kNm
    yields in flexure first (40 kN), and a column with a shear span of 1.5 m
    and a yield moment of 200 kNm (133 kN) cracks in shear first."""
    VRc = _get_vrc_ec2(**vrc_beam_inputs())  # in kN
    assert _get_av_ec8(100.0, 2.5, VRc) == 0.0
    assert _get_av_ec8(200.0, 1.5, VRc) == 1.0
    # The yield rotation is smaller without the tension shift
    inputs = dict(phi_y=0.008, h=0.5, Ls=2.5, fc=25 * MPa, fsyl=400 * MPa,
                  db=0.016)
    assert get_yield_rot_eurocode8(
        **inputs, av=0.0) < get_yield_rot_eurocode8(**inputs, av=1.0)


def test_yield_rot_eurocode8_automatic_av() -> None:
    """If ``av`` is not given, it is determined from the yield moment and the
    shear resistance of the 300 x 500 mm beam of 90.5 kN."""
    inputs = dict(phi_y=0.008, h=0.5, Ls=2.5, fc=25 * MPa, fsyl=400 * MPa,
                  db=0.016, b=0.3, As_tens=3 * np.pi / 4 * 0.016**2, dd=0.45)
    # My / Ls = 40 kN < VRc: yielding precedes shear cracking, av = 0
    assert get_yield_rot_eurocode8(**inputs, My=100.0) == pytest.approx(
        get_yield_rot_eurocode8(
            **{k: v for k, v in inputs.items()
               if k in ('phi_y', 'h', 'Ls', 'fc', 'fsyl', 'db')}, av=0.0),
        rel=1e-12)
    # My / Ls = 120 kN > VRc: shear cracking first, av = 1
    assert get_yield_rot_eurocode8(**inputs, My=300.0) == pytest.approx(
        get_yield_rot_eurocode8(
            **{k: v for k, v in inputs.items()
               if k in ('phi_y', 'h', 'Ls', 'fc', 'fsyl', 'db')}, av=1.0),
        rel=1e-12)
    # An explicit av takes precedence over the inputs of the automatic mode
    assert get_yield_rot_eurocode8(
        **inputs, My=100.0, av=1.0) == get_yield_rot_eurocode8(
            **inputs, My=300.0)
    # The compressive axial force raises VRc by 0.15 sigma_cp b d: 2000 kN on
    # 300 x 500 mm is limited to 0.2 fc = 5 MPa, so that VRc = 90.5 + 101 kN
    # and a column with My / Ls = 150 kN yields before shear cracking
    assert get_yield_rot_eurocode8(
        **inputs, My=375.0, Nu=2000.0) == get_yield_rot_eurocode8(
            **inputs, My=100.0)
    assert get_yield_rot_eurocode8(
        **inputs, My=375.0) == get_yield_rot_eurocode8(**inputs, My=300.0)


def test_yield_rot_eurocode8_automatic_av_missing_inputs() -> None:
    """The automatic mode requires the yield moment and the section."""
    inputs = dict(phi_y=0.008, h=0.5, Ls=2.5, fc=25 * MPa, fsyl=400 * MPa,
                  db=0.016, My=100.0, b=0.3, As_tens=6e-4, dd=0.45)
    get_yield_rot_eurocode8(**inputs)
    for key in ('My', 'b', 'As_tens', 'dd'):
        with pytest.raises(ValueError):
            get_yield_rot_eurocode8(**{**inputs, key: None})


def test_get_lp_priestley_2007() -> None:
    """Hand calculation for Ls = 2 m, fsyl = 400 MPa and db = 16 mm:
    Lp = 0.08 2000 + 0.022 400 16 = 160 + 140.8 = 300.8 mm."""
    assert get_lp_priestley_2007(
        2.0, 400 * MPa, 0.016) == pytest.approx(0.3008, rel=1e-12)
    # Arrays, e.g., the sections of a beam
    Lp = get_lp_priestley_2007(2.0, 400 * MPa, np.array([0.016, 0.02, 0.025]))
    assert Lp.shape == (3,)
    assert Lp == pytest.approx([0.3008, 0.336, 0.38], rel=1e-12)


# Shear hinge of a 0.4 x 0.4 m column: fc = 25 MPa, d = 0.35 m, Ls = 1.5 m,
# 2-leg 8 mm stirrups at 0.15 m (fy = 400 MPa), core hc = 0.332 m
SHEAR = dict(fc=25 * MPa, Ag=0.16, d=0.35, Ls=1.5, h=0.4, b=0.4,
             Av=2 * bar_area(0.008), fsyh=400 * MPa, hc=0.332, sbh=0.15)


def test_shear_cracking_sezen_moehle2004() -> None:
    """Hand calculation: fct = sqrt(25) / 3 = 1.667 MPa, Ae = 0.128 m2,
    a / d = 1.5 / 0.35 = 4.29 is limited to 4, so
    V1 = fct / 4 sqrt(1 + P / (fct Ag)) Ae; with P = 400 kN the square root
    is sqrt(2.5), so V1 = 84.33 kN, and V1 = 53.33 kN without axial load.
    gamma1 = V1 / (Gc Ae). For a squat column, a / d = 0.5 / 0.35 = 1.43 is
    limited to 2."""
    args = dict(fc=SHEAR['fc'], Gc=12.5e6, Ag=SHEAR['Ag'], d=SHEAR['d'],
                Ls=SHEAR['Ls'])
    V1, gamma1 = get_shear_cracking_sezen_moehle2004(**args, P=400.0)
    fct = 5.0 / 3.0 * 1000
    assert V1 == pytest.approx(fct / 4 * np.sqrt(2.5) * 0.128, rel=1e-12)
    assert gamma1 == pytest.approx(V1 / (12.5e6 * 0.128), rel=1e-12)
    V1, _ = get_shear_cracking_sezen_moehle2004(**args)
    assert V1 == pytest.approx(53.333333, rel=1e-6)
    V1, _ = get_shear_cracking_sezen_moehle2004(**{**args, 'Ls': 0.5})
    assert V1 == pytest.approx(fct / 2 * 0.128, rel=1e-12)
    # Within the limits, a / d = 1.0 / 0.35 = 2.86
    V1, _ = get_shear_cracking_sezen_moehle2004(**{**args, 'Ls': 1.0})
    assert V1 == pytest.approx(fct * 0.35 / 1.0 * 0.128, rel=1e-12)


def test_shear_strength_priestley1994() -> None:
    """Hand calculation: Vc = 0.29 sqrt(25) 0.128 = 185.6 kN,
    Vp = 400 (0.4 - 0.1) / (2 1.5) = 40 kN, Vs = Av fy hc / s = 89.0 kN.
    The axial load term is zero if the neutral axis depth exceeds h."""
    args = {k: SHEAR[k] for k in ('fc', 'Ag', 'h', 'Ls', 'Av', 'fsyh', 'hc',
                                  'sbh')}
    Vc, Vp, Vs = get_shear_strength_priestley1994(**args, c=0.1, P=400.0)
    assert Vc == pytest.approx(185.6, rel=1e-12)
    assert Vp == pytest.approx(40.0, rel=1e-12)
    assert Vs == pytest.approx(89.003414, rel=1e-6)
    _, Vp, _ = get_shear_strength_priestley1994(**args, c=0.5, P=400.0)
    assert Vp == 0.0
    # theta = 30 degrees multiplies the truss component by cot(30) = 1.732
    _, _, Vs30 = get_shear_strength_priestley1994(
        **args, c=0.1, P=400.0, theta=30.0)
    assert Vs30 == pytest.approx(Vs * np.sqrt(3), rel=1e-12)


def mergos_kappos_args(**changes) -> dict:
    """Inputs of the shear strains for the column above."""
    args = dict(V1=78.7, gamma1=5e-5, V2=310.0, Es=200e6, Ec=30e6, b=0.4,
                hc=0.332, rhoh=0.0017, fsyh=400 * MPa, fc=25 * MPa, Ls=1.5,
                h=0.4, nu=0.2)
    args.update(changes)
    return args


def test_shear_strains_mergos_kappos2012() -> None:
    """Hand calculation of Eqs. 7-11 for theta = 45 degrees (sin^4 = 0.25,
    cot^2 = 1)."""
    a = mergos_kappos_args()
    GA1, gamma2, gamma3 = get_shear_strains_mergos_kappos2012(**a)
    GA1_ref = (a['Es'] * a['b'] * a['hc'] * a['rhoh'] * 0.25) / (
        0.25 + a['Es'] / a['Ec'] * a['rhoh'])
    # Ls / h = 3.75 is limited to 2.5
    gamma2_ref = ((1 - 1.07 * 0.2) * (5.37 - 1.59 * 2.5)
                  * (a['gamma1'] + (a['V2'] - a['V1']) / GA1_ref))
    omega = a['rhoh'] * 400 / 25
    gamma3_ref = max((1 - 2.5 * 0.2) * 2.5**2 * (0.31 + 17.8 * omega),
                     1) * gamma2_ref
    assert GA1 == pytest.approx(GA1_ref, rel=1e-12)
    assert gamma2 == pytest.approx(gamma2_ref, rel=1e-12)
    assert gamma3 == pytest.approx(gamma3_ref, rel=1e-12)
    assert gamma3 >= gamma2 > a['gamma1']


def test_shear_strains_mergos_kappos2012_limits() -> None:
    """The axial load ratio, the shear span ratio and the mechanical
    transverse reinforcement ratio are limited to 0.6 (Eq. 8) or 0.4
    (Eq. 11.2), 2.5 and 0.08; gamma3 is at least gamma2."""
    ref = get_shear_strains_mergos_kappos2012(**mergos_kappos_args(nu=0.6))
    assert get_shear_strains_mergos_kappos2012(
        **mergos_kappos_args(nu=0.9)) == ref
    ref = get_shear_strains_mergos_kappos2012(**mergos_kappos_args(Ls=1.0))
    assert get_shear_strains_mergos_kappos2012(
        **mergos_kappos_args(Ls=1.0, h=0.2))[1:] == pytest.approx(
            ref[1:], rel=1e-12)
    # omega_k = rhoh fy / fc = 0.16 and 0.08 (the limit)
    big = get_shear_strains_mergos_kappos2012(
        **mergos_kappos_args(rhoh=0.01, fsyh=400 * MPa))
    cap = get_shear_strains_mergos_kappos2012(
        **mergos_kappos_args(rhoh=0.01, fsyh=200 * MPa))
    assert big[2] / big[1] == pytest.approx(cap[2] / cap[1], rel=1e-12)
    # High axial load: lambda_1 = 0, so gamma3 = gamma2
    _, gamma2, gamma3 = get_shear_strains_mergos_kappos2012(
        **mergos_kappos_args(nu=0.5))
    assert gamma3 == gamma2


def zimos_args(**changes) -> dict:
    """Inputs of the post-peak branch for the column above."""
    args = dict(Vmax=300.0, P=400.0, b=0.4, d=0.35, Ag=0.16, Ac=0.332**2,
                rhol=0.01, rhoh=0.0017, fc=25 * MPa, fsyl=400 * MPa,
                fsyh=400 * MPa, sbh=0.15, dbl=0.016, nu=0.1)
    args.update(changes)
    return args


def test_shear_post_peak_zimos2015() -> None:
    """Hand calculation of Eqs. 4 and 7 (stresses in MPa)."""
    a = zimos_args()
    Spp, gamma_tpp = get_shear_post_peak_zimos2015(**a)
    aconf = a['Ac'] / a['Ag']
    nu_l = 400.0 / (0.01 * 0.16 * 400e3)
    tau = 300.0 / (0.4 * 0.35) / 1000
    gamma_ref = (0.65 * (0.01 / aconf)**1.2) / np.sqrt(
        (0.0017 * 400) / (nu_l * (0.15 / 0.35) * (tau / 5.0)))
    Spp_ref = 7.36 + 0.28 * np.sqrt(0.12) / (
        (0.0017 + 0.0011) * ((400 * 0.01 / aconf) * (0.016 / 0.35) + 0.06))
    assert gamma_tpp == pytest.approx(gamma_ref, rel=1e-12)
    assert Spp == pytest.approx(Spp_ref, rel=1e-12)


def test_shear_post_peak_zimos2015_without_axial_load() -> None:
    """Without axial load the total post-peak shear strain is zero, also for
    plain float inputs, and a scalar is returned."""
    _, gamma_tpp = get_shear_post_peak_zimos2015(**zimos_args(P=0.0, nu=0.0))
    assert gamma_tpp == 0.0
    assert np.ndim(gamma_tpp) == 0


def asce41_args(**changes) -> dict:
    """Inputs of the ASCE/SEI 41-17 shear strength of the 0.4 x 0.4 m column
    above, with d = 0.8 h = 0.32 m."""
    args = dict(fc=25 * MPa, Ag=0.16, d=0.32, Av=2 * bar_area(0.008),
                fsyh=400 * MPa, sbh=0.15, Ls=1.5, P=400.0)
    args.update(changes)
    return args


def test_shear_strength_asce41_17() -> None:
    """Hand calculation in MN, m and MPa: s / d = 0.47, so alpha = 1;
    M / V d = 1.5 / 0.32 = 4.69 is limited to 4;
    Vs = Av fy d / s = 1.0053e-4 x 400 x 0.32 / 0.15 = 0.08579 MN;
    Vc = 5 / (2 x 4) sqrt(1 + 2 x 0.4 / (5 x 0.16)) x 0.128 = 0.11314 MN."""
    Vs = 2 * bar_area(0.008) * 400 * 0.32 / 0.15
    Vc = 5 / 8 * np.sqrt(1 + 0.8 / 0.8) * 0.128
    assert get_shear_strength_asce41_17(**asce41_args()) == pytest.approx(
        (Vs + Vc) * 1000, rel=1e-12)
    # M / V d below 2 is limited to 2: Ls = 0.5 m gives 1.56
    Vc2 = 5 / 4 * np.sqrt(2.0) * 0.128
    assert get_shear_strength_asce41_17(
        **asce41_args(Ls=0.5)) == pytest.approx((Vs + Vc2) * 1000, rel=1e-12)
    # alpha: 0 for s / d >= 1, 0.5 for s / d = 0.875
    assert get_shear_strength_asce41_17(
        **asce41_args(sbh=0.32)) == pytest.approx(Vc * 1000, rel=1e-12)
    assert get_shear_strength_asce41_17(
        **asce41_args(sbh=0.28)) == pytest.approx(
            (0.5 * Vs * 0.15 / 0.28 + Vc) * 1000, rel=1e-12)
    # Degradation factor
    assert get_shear_strength_asce41_17(
        **asce41_args(), k=0.7) == pytest.approx(
            0.7 * (Vs + Vc) * 1000, rel=1e-12)


def test_shear_stiffness_leborgne_ghannoum2014() -> None:
    """k_el = 5 / 6 Gc Ag / L."""
    assert get_shear_stiffness_leborgne_ghannoum2014(
        12.5e6, 0.16, 3.0) == pytest.approx(5 / 6 * 12.5e6 * 0.16 / 3.0,
                                            rel=1e-12)


def test_shear_degrading_slope_shoraka_elwood2013() -> None:
    """k_deg = 4.5 P (4.6 Av fy dc / (s P) + 1)^2 / L, here with
    Av fy dc / (s P) = 1.0053e-4 x 4e5 x 0.36 / (0.15 x 400) = 0.2413."""
    Av = 2 * bar_area(0.008)
    ratio = Av * 400e3 * 0.36 / (0.15 * 400.0)
    assert get_shear_degrading_slope_shoraka_elwood2013(
        400.0, Av, 400 * MPa, 0.36, 0.15, 3.0) == pytest.approx(
            4.5 * 400.0 * (4.6 * ratio + 1)**2 / 3.0, rel=1e-12)


def test_shear_residual_zimos2015() -> None:
    """Eq. 3: Vr = Vmax (1 - Spp gamma_tpp). With Spp = 10 and
    gamma_tpp = 0.05, Vr = 0.5 Vmax. Below 0.1 Vmax (gamma_tpp = 0.095 gives
    0.05 Vmax, gamma_tpp = 0.2 gives -Vmax), the residual point is on the
    descending branch at 0.1 Vmax, gamma_tpp = 0.9 / Spp = 0.09."""
    Vr, gamma_tpp = get_shear_residual_zimos2015(300.0, 10.0, 0.05)
    assert Vr == pytest.approx(150.0, rel=1e-12)
    assert gamma_tpp == 0.05
    for gamma in (0.095, 0.2):
        Vr, gamma_tpp = get_shear_residual_zimos2015(300.0, 10.0, gamma)
        assert Vr == pytest.approx(30.0, rel=1e-12)
        assert gamma_tpp == pytest.approx(0.09, rel=1e-12)
        # The point is on the descending branch of Eq. 3
        assert Vr == pytest.approx(300.0 * (1 - 10.0 * gamma_tpp), rel=1e-12)
    # Other minimum ratio, and arrays
    Vr, gamma_tpp = get_shear_residual_zimos2015(
        np.array([300.0, 300.0]), 10.0, np.array([0.05, 0.2]), Vr_Vmax=0.2)
    assert Vr == pytest.approx([150.0, 60.0], rel=1e-12)
    assert gamma_tpp == pytest.approx([0.05, 0.08], rel=1e-12)
    assert np.ndim(get_shear_residual_zimos2015(300.0, 10.0, 0.05)[0]) == 0
