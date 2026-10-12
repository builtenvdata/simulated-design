"""This module provides various methods for reinforced concrete sections
such as moment-curvature analysis and confined concrete parameter calculations.
"""
# Imports from installed packages
import numpy as np
from typing import Tuple, Sequence, List, Dict, Optional
from scipy.optimize import root_scalar, minimize_scalar
from dataclasses import dataclass

from .units import MPa, MN, mm, N
from .misc import PRECISION


@dataclass(frozen=True)
class SectionState:
    """Section resultants at a given neutral axis depth c.

    This container is used internally during axial-force compatibility solves
    (i.e., finding ``c`` such that internal axial force equals the applied
    axial force).

    Attributes
    ----------
    c : float
        Neutral axis depth from the **top** fiber.
    phi : float
        Curvature.
    Fint : float
        Internal axial resultant. Positive sign is compression.
    M : float
        Internal bending moment about the section centroid.
    """
    c: float
    phi: float
    Fint: float
    M: float


def do_simplified_section_analysis(
    h: float,
    b: float,
    fc: float,
    Ec: float,
    Pext: float,
    fyL: float,
    Es: float,
    As_layers: Sequence[float],
    y_layers: Sequence[float],
    pflag: int = 0,
) -> Tuple[float, float, float, float]:
    """
    Compute cracking, first-yield, and nominal/ultimate moments.

    - Cracking moment Mcr: uncracked elastic analysis with steel included
      via transformed section; cracking occurs when bottom fiber concrete
      stress reaches fcr.
    - First-yield moment My: curvature fixed at phi_y (Priestley et al. 2007).
      If the extreme compression fiber would be crushed at phi_y (high axial
      load), the yield point is taken at the largest curvature at which the
      axial force can be carried without crushing it.
    - Concrete follows the parabolic stress-strain relationship of Collins &
      Mitchell (1997), integrated exactly over the compressed depth, with no
      stress beyond the crushing strain. The whole section may be in
      compression.
    - Reinforcement is provided directly as steel area per layer at specified
      depths from the top fiber. Any number of layers is supported.

    Sign convention: compression is positive for both concrete and steel.

    Parameters
    ----------
    h : float
        Total section depth (m).
    b : float
        Section width (m).
    fc : float
        Concrete compressive strength (kPa).
    Ec : float
        Concrete elastic modulus (kPa).
    Pext : float
        Applied axial force (kN). Compression is positive.
    fyL : float
        Yield strength of longitudinal reinforcement (kPa).
    Es : float
        Elastic modulus of steel (kPa).
    As_layers : Sequence[float]
        Steel area in each layer (m^2), ordered top -> bottom.
    y_layers : Sequence[float]
        Depth of each reinforcement layer from the top fiber (m), ordered
        top -> bottom. Must be strictly increasing and same length as
        As_layers.
    pflag : int, optional
        Print/debug flag:
        - 0: no output
        - 1: print final moments

    Returns
    -------
    Mcr : float
        Cracking moment (kNm).
    phi_cr : float
        Cracking curvature (rad/m).
    ccr : float
        Neutral axis depth at cracking (m) from top fiber (centroidal NA).
    My : float
        Yield bending moment (kNm).
    phi_y : float
        Yield curvature (rad/m).
    cy : float
        Neutral axis depth at first yield (m). It exceeds ``h`` if the whole
        section is in compression.

    Raises
    ------
    ValueError
        If the axial force exceeds the axial capacity of the section in
        compression or in tension.

    References
    ----------
    Priestley, M. J. N., Calvi, G. M., & Kowalsky, M. J. (2007).
    Displacement-based seismic design of structures. IUSS Press.

    Collins, M. P., & Mitchell, D. (1997). Prestressed concrete
    structures. Prentice Hall.
    """

    def validate_inputs(hh: float, As: np.ndarray, y: np.ndarray) -> None:
        """
        Validate reinforcement layer inputs.

        Parameters
        ----------
        hh : float
            Section depth (m).
        As : np.ndarray
            Reinforcement areas (m^2), 1D.
        y : np.ndarray
            Layer depths from top fiber (m), 1D.

        Raises
        ------
        ValueError
            If arrays are not 1D, lengths mismatch, are empty, contain invalid
            values, or are not ordered consistently.
        """
        if As.ndim != 1 or y.ndim != 1:
            raise ValueError("As_layers and y_layers must be 1D sequences.")
        if len(As) != len(y):
            raise ValueError("As_layers and y_layers must have same length.")
        if len(As) == 0:
            raise ValueError("At least one reinforcement layer is required.")
        if np.any(np.diff(y) < 0.0):
            raise ValueError("y_layers must be strictly increasing.")
        if np.any(y < 0.0) or np.any(y > hh):
            raise ValueError("All y_layers values must be within [0, h].")
        if np.any(As < 0.0):
            raise ValueError("As_layers cannot contain negative values.")

    # Parabolic concrete stress-strain relationship, f = fc (2r - r^2) with
    # r = e / e_c, in Collins & Mitchell 1997
    n_c = 0.8 + fc / (17.0 * MPa)  # Eqn 3-4
    e_c = (fc / Ec) * (n_c / (n_c - 1.0)) if n_c > 1.0 else np.inf  # Eqn 3-5
    # Eqn 3-5 diverges as n_c -> 1 (fc -> 3.4 MPa) and turns negative below
    e_c = min(e_c, 0.002)
    e_lim = 2.0 * e_c  # Strain at which the stress drops to zero (crushing)

    def conc_force(e: float) -> float:
        """Integral of the concrete stress over strain, from 0 to ``e``."""
        return fc * (e**2 / e_c - e**3 / (3.0 * e_c**2))

    def conc_moment(e: float) -> float:
        """Integral of the concrete stress times strain, from 0 to ``e``."""
        return fc * (2.0 * e**3 / (3.0 * e_c) - e**4 / (4.0 * e_c**2))

    def section_state(c: float, phi: float) -> SectionState:
        """
        Build the section force state for a given neutral axis depth and
        curvature.

        Strains follow from compatibility, ``eps = (c - depth) * phi``.
        Steel stresses are bilinear with perfect plasticity via clipping to
        ``[-fyL, fyL]``. Concrete in compression follows the parabolic
        stress-strain relationship, integrated exactly over the section
        depth. The concrete carries no tension, and no stress beyond the
        crushing strain ``2 e_c``. The neutral axis may lie below the section
        (``c > h``), i.e., the whole section may be in compression.

        Parameters
        ----------
        c : float
            Neutral axis depth from the top fiber (m).
        phi : float
            Curvature (rad/m).

        Returns
        -------
        SectionState
            Internal axial force and moment about the section centroid.
        """
        # Reinforcing steel strains, stresses and forces
        e_s = (c - y) * phi
        Fs = np.clip(e_s * Es, -fyL, fyL) * As
        # Concrete strains at the top and bottom of the compressed part
        e_top = min(c * phi, e_lim)
        e_bot = max((c - h) * phi, 0.0)
        if e_top > e_bot:
            dF = conc_force(e_top) - conc_force(e_bot)
            dG = conc_moment(e_top) - conc_moment(e_bot)
            # Depth of a fiber is c - e/phi, and its lever arm about the
            # centroid is h/2 - (c - e/phi)
            Fc = b * dF / phi
            Mc = b * ((0.5 * h - c) * dF + dG / phi) / phi
        else:
            Fc = Mc = 0.0
        Fint = Fc + float(Fs.sum())
        M = Mc + float((Fs * (0.5 * h - y)).sum())
        return SectionState(c=c, phi=phi, Fint=Fint, M=M)

    def get_max_force(phi: float) -> Tuple[float, float]:
        """
        Maximum internal axial force at a given curvature, without crushing
        the extreme compression fiber.

        Parameters
        ----------
        phi : float
            Curvature (rad/m).

        Returns
        -------
        c_max : float
            Neutral axis depth at the maximum axial force (m).
        F_max : float
            Maximum internal axial force (kN).
        """
        c_lim = e_lim / phi  # Neutral axis depth at crushing
        c_grid = np.linspace(1.0e-6 * c_lim, c_lim, 200)
        F_grid = np.array([section_state(ci, phi).Fint for ci in c_grid])
        j = int(np.argmax(F_grid))
        if 0 < j < len(c_grid) - 1:  # refine an interior maximum
            sol = minimize_scalar(
                lambda ci: -section_state(ci, phi).Fint,
                bounds=(c_grid[j - 1], c_grid[j + 1]), method="bounded",
                options={"xatol": 1.0e-10 * c_lim})
            if -sol.fun > F_grid[j]:
                return float(sol.x), float(-sol.fun)
        return float(c_grid[j]), float(F_grid[j])

    def solve_c(phi: float, c_max: float) -> Optional[SectionState]:
        """
        Solve for the neutral axis depth ``c`` using axial-force
        compatibility at a given curvature.

        Finds ``c`` in ``(0, c_max]`` such that
        ``section_state(c, phi).Fint - Pext = 0``. The routine first searches
        for a sign change on a grid, then uses Brent's method on the first
        bracket found.

        Parameters
        ----------
        phi : float
            Curvature (rad/m).
        c_max : float
            Upper bound of the neutral axis depth (m).

        Returns
        -------
        SectionState | None
            Section state at the converged ``c``, or None if no sign change
            is found on the grid.
        """
        def g(c: float) -> float:
            """Axial force residual: internal minus external."""
            return section_state(c, phi).Fint - Pext

        c_grid = np.linspace(1.0e-6 * c_max, c_max, 120)
        g_vals = np.array([g(ci) for ci in c_grid], dtype=float)
        idx = np.where(np.sign(g_vals[:-1]) * np.sign(g_vals[1:]) <= 0.0)[0]
        if len(idx) == 0:
            return None
        sol = root_scalar(
            g,
            bracket=(float(c_grid[idx[0]]), float(c_grid[idx[0] + 1])),
            method="brentq",
            xtol=1.0e-10,
            rtol=1.0e-10,
            maxiter=200,
        )
        return section_state(float(sol.root), phi)

    As = np.asarray(As_layers, dtype=float)
    y = np.asarray(y_layers, dtype=float)
    validate_inputs(hh=h, As=As, y=y)
    # Yield curvature in Priestley et al. 2007
    phi_y = 2.1 * fyL / (Es * h)  # Eqn 4.57b

    def get_mcr() -> Tuple[float, float]:
        """
        Compute cracking moment for an uncracked elastic rectangular section.

        Parameters
        ----------
        None

        Returns
        -------
        Mcr : float
            Cracking moment about centroid.
        phi_cr : float
            Cracking curvature.
        ccr : float
            Neutral axis depth at cracking from top fiber.
        """

        # Gross section section properties
        Ag = b * h
        yg = 0.5 * h
        Ig = b * h**3 / 12.0
        # Modular ratio
        n = Es / Ec
        # Tansformed section area, Eqn. 5-31
        Atr = Ag + float(((n - 1.0) * As).sum())
        # Tansformed section centroid distance from top, Eqn. 5-32
        ytr = float((Ag * yg + float(((n - 1.0) * As * y).sum())) / Atr)
        # Tansformed section moment of inertia, Eqn. 5-33
        Itr = (Ig + Ag * (yg - ytr) ** 2
               + float(((n - 1.0) * As * (y - ytr) ** 2).sum()))

        # Concrete cracking stress
        fcr = 0.33 * np.sqrt(fc / MPa) * MPa  # Eqn. 3-16

        # Extreme tensile fiber for positive bending is bottom fiber.
        yt = h - ytr  # distance from centroid to bottom (m)
        Mcr = max((fcr + Pext / Atr) * Itr / yt, 0.0)  # Crackng moment
        phi_cr = Mcr / (Ec * Itr)  # cracking curvature

        return Mcr, phi_cr, ytr

    Mcr, phi_cr, ccr = get_mcr()

    if Pext < -fyL * float(As.sum()):
        raise ValueError(
            f"No axial equilibrium: the axial force {Pext:.6g} kN exceeds "
            "the tensile capacity of the section.")
    # Yield at the curvature phi_y, without crushing the extreme compression
    # fiber (c <= e_lim / phi_y)
    st_y = solve_c(phi_y, e_lim / phi_y)
    if st_y is None:
        c_max, F_max = get_max_force(phi_y)
        if Pext <= F_max:  # Maximum between the grid points
            st_y = solve_c(phi_y, c_max) or section_state(c_max, phi_y)
    if st_y is None:
        # The extreme compression fiber would be crushed at phi_y. The yield
        # point is taken at the largest curvature at which the axial force
        # can be carried without crushing it.
        phi_min = 1.0e-4 * phi_y
        if get_max_force(phi_min)[1] < Pext:
            raise ValueError(
                f"No axial equilibrium: the axial force {Pext:.6g} kN "
                "exceeds the axial capacity of the section.")
        sol = root_scalar(
            lambda phi: get_max_force(phi)[1] - Pext,
            bracket=(phi_min, phi_y),
            method="brentq",
            xtol=1.0e-10 * phi_y,
            rtol=1.0e-10,
            maxiter=200,
        )
        phi_y = float(sol.root)
        st_y = section_state(get_max_force(phi_y)[0], phi_y)
        if pflag:
            print(f"Crushing governs the yield point: phi_y = {phi_y:.6g}.")
    My = st_y.M
    cy = st_y.c

    if pflag:
        print(f"Mcr: {Mcr:.6f} kNm, ccr: {ccr:.6f} m")
        print(f"My:  {My:.6f} kNm, cy:  {cy:.6f} m")

    return Mcr, phi_cr, ccr, My, phi_y, cy


def get_sum_wi_sq(
    rein_x: List[float],
    rein_y: List[float],
    rein_ds: List[float],
    clear: bool = True,
) -> Tuple[List[float], float, Dict[str, int]]:
    """
    Compute Mander's w' spacings and their squared-sum for rectangular
    confinement.

    Parameters
    ----------
    rein_x : List[float]
        x-coordinates of longitudinal reinforcement bars.
        Used to estimate bar spacing for confinement effectiveness.
    rein_y : List[float]
        y-coordinates of longitudinal reinforcement bars.
    rein_ds : List[float]
        Diameters of longitudinal reinforcement bars.
    clear : bool, optional
        If True, the clear spacings ``w'`` of Mander et al. (1988) are
        returned. If False, the centre-to-centre distances ``bi`` of
        EN 1998-1:2004, Eq. 5.16a are returned. By default True.

    Returns
    -------
    w_dash : list[float]
        Clear (or centre-to-centre) spacings along faces between adjacent
        perimeter bars.
    sum_w2 : float
        Summation of w'i^2 values.
    n_face : dict
        Counts per face: bottom/top/left/right

    References
    ----------
    Mander, J. B., Priestley, M. J. N., & Park, R. (1988). Theoretical
    Stress-Strain Model for Confined Concrete. Journal of Structural
    Engineering, 114(8), 180-1826.
    https://doi.org/10.1061/(asce)0733-9445(1988)114:8(1804)
    """

    eps = 1e-6
    tol = 0.5 * (max(rein_ds) - min(rein_ds)) + eps
    x = np.asarray(rein_x, dtype=float)
    y = np.asarray(rein_y, dtype=float)
    d = np.asarray(rein_ds, dtype=float)
    if not (len(x) == len(y) == len(d)):
        raise ValueError("rein_x, rein_y, rein_ds must have same length")

    x_min, x_max = float(x.min()), float(x.max())
    y_min, y_max = float(y.min()), float(y.max())

    faces = {
        "bottom": np.where(np.isclose(y, y_min, atol=tol))[0],
        "top":    np.where(np.isclose(y, y_max, atol=tol))[0],
        "left":   np.where(np.isclose(x, x_min, atol=tol))[0],
        "right":  np.where(np.isclose(x, x_max, atol=tol))[0],
    }
    n_face = {k: int(len(v)) for k, v in faces.items()}

    w_dash: List[float] = []

    def add_face_spacings(indices: np.ndarray, sort_coord: np.ndarray):
        if len(indices) < 2:
            return
        idx = indices[np.argsort(sort_coord[indices])]
        for a, b in zip(idx[:-1], idx[1:]):
            delta_cc = float(sort_coord[b] - sort_coord[a])  # center-to-center
            db_avg = 0.5 * float(d[a] + d[b]) if clear else 0.0
            w = max(delta_cc - db_avg, 0.0)                  # clear spacing
            w_dash.append(w)

    # bottom/top: spacing along x
    add_face_spacings(faces["bottom"], x)
    add_face_spacings(faces["top"], x)

    # left/right: spacing along y
    add_face_spacings(faces["left"], y)
    add_face_spacings(faces["right"], y)

    sum_wi_sq = float(np.sum(np.square(w_dash))) if w_dash else 0.0

    return w_dash, sum_wi_sq, n_face


def get_mander_confinement(
    fc: float, Lx: float, Ly: float, cover: float, db_v: float, s: float,
    legs_x: int, legs_y: int, fy_v: float, rein_x: List[float],
    rein_y: List[float], rein_d: List[float], eps_su: float = 0.10,
    eps_c0: float = 0.002, eps_cu_factor: float = 1.3
) -> Dict:
    """
    Compute confined concrete parameters using the Mander model.

    Parameters
    ----------
    fc : float
        Unconfined concrete compressive strength (same stress units as fy_v).
        Must be positive.
    Lx : float
        Section dimension in x-direction (overall width).
    Ly : float
        Section dimension in y-direction (overall depth).
    cover : float
        Clear concrete cover, i.e., to the outside of the transverse
        reinforcement. The core is measured to the centreline of the
        transverse reinforcement.
    db_v : float
        Diameter of transverse reinforcement (stirrups/ties).
    s : float
        Center-to-center spacing of transverse reinforcement.
    legs_x : int
        Number of transverse reinforcement legs effective in x-direction.
    legs_y : int
        Number of transverse reinforcement legs effective in y-direction.
    fy_v : float
        Yield strength of transverse reinforcement (same units as fc).
    rein_x : List[float]
        x-coordinates of longitudinal reinforcement bars.
    rein_y : List[float]
        y-coordinates of longitudinal reinforcement bars.
    rein_d : List[float]
        Diameters of longitudinal reinforcement bars.
    eps_su : float, optional
        Ultimate reinforcing steel strain, by default 0.10.
    eps_c0 : float, optional
        Unconfined concrete strain at peak compressive stress,
        by default 0.002.
    eps_cu_factor : float, optional
        Factor for increasing confined concrete ultimate strain. The value
        of this factor changes between 1.3 - 1.6 according to Priestley et al.
        2007. For design purposes, conservatively, can be taken as 1.0.
        By default 1.3.

    Returns
    -------
    Output dictionary containing:

    core_x_min : float
        Minimum x-coordinate of confined core (centerline of stirrups).
    core_x_max : float
        Maximum x-coordinate of confined core.
    core_y_min : float
        Minimum y-coordinate of confined core.
    core_y_max : float
        Maximum y-coordinate of confined core.
    bc_x : float
        Core dimension in x-direction (centerline-to-centerline).
    bc_y : float
        Core dimension in y-direction.
    Ke : float
        Confinement effectiveness coefficient (0-1).
    fl_eff : float
        Effective lateral confining pressure.
    fcc : float
        Confined concrete compressive strength (f'cc).
    eps_cc : float
        Confined concrete strain at peak stress.
    eps_cu : float
        Ultimate confined concrete strain.
    Ec : float
        Initial tangent modulus of concrete.
    r : float
        Stress-strain curve shape parameter.
    strength_ratio : float
        Ratio f'cc / fc.

    Notes
    -----
    - The confinement effectiveness factor Ke accounts for:
        • Bar spacing between longitudinal reinforcement
        • Vertical spacing of stirrups
        • Ineffective concrete regions
    - Assumes a rectangular section with uniformly spaced transverse
      reinforcement provided by rectangular stirrups/ties.
    - Steel reaches 0.10 ultimate strain (eps_su = 0.10).
    - Unconfined concrete peak strain eps_c0 = 0.002.
    - eps_cu is increased by eps_cu_factor because Eqn. 4.21 in the DBD
      book is conservative for assessment; eps_cu_factor = 1.3 by default.
    - Expected units: length in mm, stress in MPa.

    References
    ----------
    Mander, J. B., Priestley, M. J. N., & Park, R. (1988). Theoretical
    Stress-Strain Model for Confined Concrete. Journal of Structural
    Engineering, 114(8), 180-1826.
    https://doi.org/10.1061/(asce)0733-9445(1988)114:8(1804)

    Priestley, M. J. N., Calvi, G. M., & Kowalsky, M. J. (2007).
    *Displacement-based seismic design of structures*.
    IUSS Press.

    Priestley, M. J. N., F. Seible & Calvi, G. M. (1996).
    *Seismic design and retrofit of bridges*.
    John Wiley & Sons.
    """
    # Core dimensions (centerline of stirrups)
    core_offset = cover + db_v / 2
    bc_x = Lx - 2 * core_offset
    bc_y = Ly - 2 * core_offset

    # Core boundaries
    core_x_min = core_offset
    core_x_max = Lx - core_offset
    core_y_min = core_offset
    core_y_max = Ly - core_offset

    # Area of stirrup legs
    Asv = np.pi * (db_v / 2)**2

    # Total area of transverse reinforcement in each direction
    Asx = legs_x * Asv
    Asy = legs_y * Asv

    # Transverse reinforcement ratios
    rho_x = Asx / (s * bc_y)
    rho_y = Asy / (s * bc_x)

    # Clear spacing between stirrups
    s_clear = s - db_v

    # Confined concrete strength - Mander et al. 1988
    rein_ds_arr = np.array(rein_d)
    As_long = np.sum(np.pi * (rein_ds_arr / 2)**2)
    Ac = bc_x * bc_y
    rho_cc = As_long / Ac
    # Get the sum of the squared wi value - based on Fig. 3
    _, sum_wi_sq, _ = get_sum_wi_sq(rein_x, rein_y, rein_d)
    # Eqn. 21
    Ae_horizontal = max(bc_x * bc_y - sum_wi_sq / 6, 0)
    Ae_vertical_factor = max((1 - s_clear / (2 * bc_x)), 0) * max(
        (1 - s_clear / (2 * bc_y)), 0)
    Ae = Ae_horizontal * Ae_vertical_factor
    # Eqn. 11
    Acc = Ac * (1 - rho_cc)
    # Eqn. 10
    Ke = Ae / Acc if Acc > 0 else 0
    Ke = min(max(Ke, 0.0), 1.0)
    # Eqn. 25
    fl_x = rho_x * fy_v
    # Eqn. 26
    fl_y = rho_y * fy_v
    # Eqn. 27
    fl_x_eff = Ke * fl_x
    # Eqn. 28
    fl_y_eff = Ke * fl_y
    # NOTE: Should be from Fig. 4, multiaxial failure criterion
    # Following is just an approximation
    if fl_x_eff > 0 and fl_y_eff > 0:
        fl_eff = np.sqrt(fl_x_eff * fl_y_eff)  # geometric mean
    else:
        fl_eff = (fl_x_eff + fl_y_eff) / 2  # arithmetic mean
    # Eqn. 29
    fl_ratio = fl_eff / fc if fc > 0 else 0
    if fl_ratio > 0:
        fcc = fc * (
            -1.254 + 2.254 * np.sqrt(1 + 7.94 * fl_ratio) - 2 * fl_ratio
            )
    else:
        fcc = fc
    fcc = max(fcc, fc)

    # Confined strain at peak
    eps_cc = eps_c0 * (1 + 5 * (fcc / fc - 1))  # Eqn. 4.12 - DBD book

    # Ultimate strain - Priestley et al. (1996, 2007)
    rho_v = rho_x + rho_y  # Priestley 1996 - p. 272
    eps_cu = 0.004 + 1.4 * rho_v * fy_v * eps_su / fcc  # Eqn. 4.21 - DBD book
    eps_cu = eps_cu_factor * eps_cu  # see text in DBD book p.142
    eps_cu = max(eps_cu, 0.006)  # check against spalling strain

    # Curve shape parameter
    Ec = 5000 * np.sqrt(fc)  # Eqn. 4.14 - DBD book
    Esec = fcc / eps_cc  # Eqn. 4.15 - DBD book
    r = Ec / (Ec - Esec) if (Ec - Esec) > 0 else 5.0  # Eqn. 4.13 - DBD book

    return {
        'core_x_min': core_x_min, 'core_x_max': core_x_max,
        'core_y_min': core_y_min, 'core_y_max': core_y_max,
        'bc_x': bc_x, 'bc_y': bc_y,
        'Ke': Ke, 'fl_eff': fl_eff,
        'fcc': fcc, 'eps_cc': eps_cc, 'eps_cu': eps_cu,
        'Ec': Ec, 'r': r,
        'strength_ratio': fcc / fc,
    }


def _match_short_to_long_by_sampling(
    long_list: List[float],
    short_list: List[float],
) -> List[float]:
    """
    Return a modified copy of `short_list` aligned to `long_list`.

    The longer list is considered the "reference" and is not changed. The
    returned list has the same length as `short_list`, but its values are
    adjusted so that:

    - the first and last values match the first/last of `long_list`
    - interior values are sampled from the interior of `long_list`, with
      indices spread evenly in index-space

    Parameters
    ----------
    long_list : List[float]
        Reference coordinate list (unchanged).
    short_list : List[float]
        Coordinate list to be modified (returned as a new list).

    Returns
    -------
    List[float]
        The adjusted coordinate list.
    """
    n_long = len(long_list)
    n_short = len(short_list)

    if n_short >= n_long:
        return short_list[:]

    start, end = long_list[0], long_list[-1]
    k = n_short - 2

    if k <= 0:
        if n_short == 2:
            return [start, end]
        return [0.5 * (start + end)]

    long_interior = long_list[1:-1]
    m = len(long_interior)

    if k == 1:
        indices = [m // 2]
    else:
        indices = [round(i * (m - 1) / (k - 1)) for i in range(k)]

    return [start] + [long_interior[i] for i in indices] + [end]


def _arrange_diameters_big_at_ends(
    d_big: float,
    n_big: int,
    d_small: float,
    n_small: int,
) -> List[float]:
    """
    Build a diameter list with larger bars placed at both ends.

    The larger diameter is split as evenly as possible between left and right
    ends. All smaller bars fill the middle.

    Parameters
    ----------
    d_big : float
        Larger bar diameter.
    n_big : int
        Count of larger bars.
    d_small : float
        Smaller bar diameter.
    n_small : int
        Count of smaller bars.

    Returns
    -------
    List[float]
        Diameter list of length (n_big + n_small).
    """
    left_big = n_big // 2
    right_big = n_big - left_big
    return [d_big] * left_big + [d_small] * n_small + [d_big] * right_big


def build_beam_rebar_layout(
    db1: float,
    db2: float,
    dt1: float,
    dt2: float,
    nb1: int,
    nb2: int,
    nt1: int,
    nt2: int,
    dbh: float,
    lx: float,
    ly: float,
    cv: float,
) -> Dict[str, List[float]]:
    """
    Build bottom/top rebar coordinates and diameters for a rectangular section.

    Notes
    -----
    - Bottom layer contains nb1 bars of db1 (big) and nb2 bars of db2 (small).
    - Top layer contains nt1 bars of dt1 (big) and nt2 bars of dt2 (small).
    - Big bars are arranged at ends of each layer.
    - X-coordinates are initially uniform within each layer.
    - If bottom/top x-coordinate lengths differ, only the shorter layer is
      modified by sampling from the longer layer so ends match and interior
      points follow the longer layer's interior.

    Parameters
    ----------
    db1 : float
        Bottom-layer big bar diameter.
    db2 : float
        Bottom-layer small bar diameter.
    dt1 : float
        Top-layer big bar diameter.
    dt2 : float
        Top-layer small bar diameter.
    nb1 : int
        Bottom-layer big bar count.
    nb2 : int
        Bottom-layer small bar count.
    nt1 : int
        Top-layer big bar count.
    nt2 : int
        Top-layer small bar count.
    dbh : float
        Hoop/stirrup diameter.
    lx : float
        Section width.
    ly : float
        Section height.
    cv : float
        Concrete cover.

    Returns
    -------
    Dict[str, List[float]]
        Dictionary containing layer-wise and combined arrays:
        - rein_xb, rein_yb, rein_db (bottom)
        - rein_xt, rein_yt, rein_dt (top)
        - rein_x,  rein_y,  rein_d  (combined)
    """
    nb = nb1 + nb2
    nt = nt1 + nt2

    if nb < 2 or nt < 2:
        raise ValueError(
            "Each layer must have at least 2 bars to define end coordinates."
        )

    yb1 = cv + dbh + db1 / 2.0
    yb2 = cv + dbh + db2 / 2.0
    yt1 = ly - (cv + dbh + dt1 / 2.0)
    yt2 = ly - (cv + dbh + dt2 / 2.0)

    xb_0 = cv + dbh + db1 / 2.0
    xb_n = lx - (cv + dbh + db1 / 2.0)
    xt_0 = cv + dbh + dt1 / 2.0
    xt_n = lx - (cv + dbh + dt1 / 2.0)

    dxb = (xb_n - xb_0) / (nb - 1)
    dxt = (xt_n - xt_0) / (nt - 1)

    rein_xb = [xb_0 + i * dxb for i in range(nb)]
    rein_xt = [xt_0 + i * dxt for i in range(nt)]

    if len(rein_xb) > len(rein_xt):
        rein_xt = _match_short_to_long_by_sampling(rein_xb, rein_xt)
    elif len(rein_xt) > len(rein_xb):
        rein_xb = _match_short_to_long_by_sampling(rein_xt, rein_xb)

    rein_db = _arrange_diameters_big_at_ends(db1, nb1, db2, nb2)
    rein_dt = _arrange_diameters_big_at_ends(dt1, nt1, dt2, nt2)

    if len(rein_db) != len(rein_xb):
        raise RuntimeError(
            f"Bottom diameter length {len(rein_db)} != x length {len(rein_xb)}"
        )
    if len(rein_dt) != len(rein_xt):
        raise RuntimeError(
            f"Top diameter length {len(rein_dt)} != x length {len(rein_xt)}"
        )

    rein_yb = [yb1 if d == db1 else yb2 for d in rein_db]
    rein_yt = [yt1 if d == dt1 else yt2 for d in rein_dt]

    rein_x = rein_xb + rein_xt
    rein_y = rein_yb + rein_yt
    rein_d = rein_db + rein_dt

    return {
        "rein_xb": rein_xb,
        "rein_xt": rein_xt,
        "rein_yb": rein_yb,
        "rein_yt": rein_yt,
        "rein_db": rein_db,
        "rein_dt": rein_dt,
        "rein_x": rein_x,
        "rein_y": rein_y,
        "rein_d": rein_d,
    }


def build_column_rebar_layout(
    dbl_cor: float,
    dbl_int: float,
    nbl_int_x: int,
    nbl_int_y: int,
    dbh: float,
    lx: float,
    ly: float,
    cv: float,
) -> Dict[str, List[float]]:
    """
    Build rebar coordinates and diameters for a rectangular column section.

    This function computes the coordinates of longitudinal reinforcement bars
    (corner and internal bars) within a rectangular cross-section, accounting
    for concrete cover and transverse reinforcement (stirrups). Bar coordinates
    are measured from the section origin located at the bottom-left corner.

    Corner bars are placed at the four corners of the effective core, while
    internal bars are distributed uniformly in a grid defined by the number of
    intermediate bars along the x- and y-directions.

    Parameters
    ----------
    dbl_cor : float
        Diameter of corner longitudinal reinforcement bars.
    dbl_int : float
        Diameter of internal longitudinal reinforcement bars.
    nbl_int_x : int
        Number of internal reinforcement bars in the x-direction.
    nbl_int_y : int
        Number of internal reinforcement bars in the y-direction.
    dbh : float
        Diameter of transverse (stirrup) reinforcement.
    lx : float
        Section width in the x-direction.
    ly : float
        Section height in the y-direction.
    cv : float
        Concrete cover to the outer surface of stirrups.

    Returns
    -------
    Dict[str, List[float]]
        Dictionary containing reinforcement layout:
        - ``"rein_x"`` : list of x-coordinates of bars
        - ``"rein_y"`` : list of y-coordinates of bars
        - ``"rein_d"`` : list of bar diameters corresponding to each bar

    Notes
    -----
    - The effective distance from the section edge to bar centerline is
      ``cv + dbh + db / 2``.
    - Corner bars are always included (4 bars).
    - Internal bars are placed in a regular grid between corner bars.
    - Coordinates follow a Cartesian system with origin at the bottom-left
      corner.
    """
    # Corner bar centerline offsets
    xc_l = cv + dbh + dbl_cor / 2.0
    xc_r = lx - (cv + dbh + dbl_cor / 2.0)
    yc_b = cv + dbh + dbl_cor / 2.0
    yc_t = ly - (cv + dbh + dbl_cor / 2.0)

    # Intermediate bar centerline offsets
    xi_l = cv + dbh + dbl_int / 2.0
    xi_r = lx - (cv + dbh + dbl_int / 2.0)
    yi_b = cv + dbh + dbl_int / 2.0
    yi_t = ly - (cv + dbh + dbl_int / 2.0)

    rein_x: List[float] = []
    rein_y: List[float] = []
    rein_d: List[float] = []

    # Helper to avoid duplicates (e.g., corners)
    seen = set()

    def add_bar(x: float, y: float, d: float) -> None:
        key = (round(x, 10), round(y, 10))
        if key in seen:
            return
        seen.add(key)
        rein_x.append(float(x))
        rein_y.append(float(y))
        rein_d.append(float(d))

    # 1) Corner bars
    add_bar(xc_l, yc_b, dbl_cor)
    add_bar(xc_l, yc_t, dbl_cor)
    add_bar(xc_r, yc_b, dbl_cor)
    add_bar(xc_r, yc_t, dbl_cor)

    # 2) Intermediate bars on TOP and BOTTOM faces (vary x, fixed y)
    if nbl_int_x > 0:
        # place them between the (intermediate) face endpoints
        dx = (xi_r - xi_l) / (nbl_int_x + 1)
        for i in range(1, nbl_int_x + 1):
            x = xi_l + i * dx
            add_bar(x, yi_b, dbl_int)  # bottom face
            add_bar(x, yi_t, dbl_int)  # top face

    # 3) Intermediate bars on LEFT and RIGHT faces (vary y, fixed x)
    if nbl_int_y > 0:
        dy = (yi_t - yi_b) / (nbl_int_y + 1)
        for j in range(1, nbl_int_y + 1):
            y = yi_b + j * dy
            add_bar(xi_l, y, dbl_int)  # left face
            add_bar(xi_r, y, dbl_int)  # right face

    return {"rein_x": rein_x, "rein_y": rein_y, "rein_d": rein_d}


def get_kent_park_confinement(
    fc: float, Lx: float, Ly: float, cover: float, db_v: float, s: float,
    legs_x: int, legs_y: int, fy_v: float, eps_c0: float = 0.002,
) -> Dict:
    """
    Compute confined concrete parameters using the Modified Kent and Park
    model.

    Parameters
    ----------
    fc : float
        Unconfined concrete compressive strength (same stress units as fy_v).
        Must be positive.
    Lx : float
        Section dimension in x-direction (overall width).
    Ly : float
        Section dimension in y-direction (overall depth).
    cover : float
        Clear concrete cover, i.e., to the outside of the transverse
        reinforcement. The core is measured to the centreline of the
        transverse reinforcement.
    db_v : float
        Diameter of transverse reinforcement (stirrups/ties).
    s : float
        Center-to-center spacing of transverse reinforcement.
    legs_x : int
        Number of transverse reinforcement legs effective in x-direction.
    legs_y : int
        Number of transverse reinforcement legs effective in y-direction.
    fy_v : float
        Yield strength of transverse reinforcement (same units as fc).
    eps_c0 : float, optional
        Unconfined concrete strain at peak compressive stress,
        by default 0.002.

    Returns
    -------
    Output dictionary containing:

    core_x_min : float
        Minimum x-coordinate of confined core (centerline of stirrups).
    core_x_max : float
        Maximum x-coordinate of confined core.
    core_y_min : float
        Minimum y-coordinate of confined core.
    core_y_max : float
        Maximum y-coordinate of confined core.
    bc_x : float
        Core dimension in x-direction (centerline-to-centerline).
    bc_y : float
        Core dimension in y-direction.
    Ke : float
        Confinement effectiveness coefficient (0-1).
    fcc : float
        Confined concrete compressive strength (f'cc).
    eps_cc : float
        Confined concrete strain at peak stress.
    eps_cu : float
        Ultimate confined concrete strain.
    strength_ratio : float
        Ratio f'cc / fc.

    Notes
    -----
    - Assumes a rectangular section with uniformly spaced transverse
      reinforcement provided by rectangular stirrups/ties.
    - Unconfined concrete peak strain eps_c0 = 0.002.
    - Confined section width is approximated as the average of the two
      directions.
    - Low strain model.
    - Expected units: length in mm, stress in MPa.

    References
    ----------
    Scott, B. D., R. Park, and M. J. N. Priestley (1982).
    Stress-strain behavior of concrete confined by overlapping hoops at low
    and high strain rates. Journal of the American Concrete Institute
    79(1): 13-27.
    """
    # Core dimensions (centerline of stirrups)
    core_offset = cover + db_v / 2
    bc_x = Lx - 2 * core_offset
    bc_y = Ly - 2 * core_offset

    # Core boundaries
    core_x_min = core_offset
    core_x_max = Lx - core_offset
    core_y_min = core_offset
    core_y_max = Ly - core_offset

    # Area of stirrup legs
    Asv = np.pi * (db_v / 2)**2

    # Total area of transverse reinforcement in each direction
    Asx = legs_x * Asv
    Asy = legs_y * Asv

    # Transverse reinforcement ratios
    rho_x = Asx / (s * bc_y)
    rho_y = Asy / (s * bc_x)
    rho_s = rho_x + rho_y

    # Confined concrete strength - Scott, Park & Priestley 1982
    ke = 1 + rho_s * fy_v / fc  # Eqn. (3)
    fcc = ke * fc

    # Confined concrete strain at peak
    eps_cc = ke * eps_c0

    # Slope, eqn. 4
    eps_50u = (3 + 0.29 * fc) / (145 * fc - 1000)
    h_ = (bc_x + bc_y) / 2  # assumed
    eps_50h = 0.75 * rho_s * (h_ / s)**0.5  # Scott et al. (1982)
    zm = 0.5 / (eps_50u + eps_50h - eps_cc)

    # Ultimate confined concrete strain
    eps_cu = max(0.8 / zm + eps_cc, 0.006)

    return {
        'core_x_min': core_x_min, 'core_x_max': core_x_max,
        'core_y_min': core_y_min, 'core_y_max': core_y_max,
        'bc_x': bc_x, 'bc_y': bc_y,
        'Ke': ke,
        'fcc': fcc, 'eps_cc': eps_cc, 'eps_cu': eps_cu,
        'strength_ratio': fcc / fc,
    }


def get_my_phiy_panagiotakos_fardis2001(
    h: float | np.ndarray, b: float | np.ndarray,
    fc: float | np.ndarray, Ec: float | np.ndarray,
    Es: float | np.ndarray, fsyl: float | np.ndarray,
    As_tens: float | np.ndarray, As_comp: float | np.ndarray,
    dd: float | np.ndarray,
    As_int: float | np.ndarray = 0.0, Nu: float | np.ndarray = 0.0,
    dd_prime: float | np.ndarray | None = None, eps_cu: float = 0.0035
) -> Tuple[float | np.ndarray, float | np.ndarray]:
    """Computes the yield moment and curvature of a rectangular RC section
    with the empirical expressions of Panagiotakos and Fardis (2001).

    The inputs may be scalars or arrays of the same shape (e.g., the start,
    mid and end sections of a beam), and the result has the same shape.

    Parameters
    ----------
    h : float | np.ndarray
        Section depth in the bending direction (m).
    b : float | np.ndarray
        Section width (m).
    fc : float | np.ndarray
        Concrete compressive strength (kPa).
    Ec : float | np.ndarray
        Concrete modulus of elasticity (kPa).
    Es : float | np.ndarray
        Steel modulus of elasticity (kPa).
    fsyl : float | np.ndarray
        Yield strength of the longitudinal steel (kPa).
    As_tens : float | np.ndarray
        Area of the longitudinal reinforcement on the tension side (m2).
    As_comp : float | np.ndarray
        Area of the longitudinal reinforcement on the compression side (m2).
    dd : float | np.ndarray
        Effective depth (m), i.e., distance from the extreme compression fiber
        to the centroid of the tension reinforcement.
    As_int : float | np.ndarray, optional
        Area of the intermediate (web) longitudinal reinforcement, on both
        sides together (m2). By default 0.0, e.g., for beams.
    Nu : float | np.ndarray, optional
        Axial load, positive in compression (kN). By default 0.0, e.g., beams.
    dd_prime : float | np.ndarray | None, optional
        Distance from the extreme compression fiber to the centroid of the
        compression reinforcement (m). If None, it is taken as ``h - dd``,
        i.e., the same distance from the face to the bars on both sides.
    eps_cu : float, optional
        Concrete crushing strain used to find the balanced neutral axis
        depth. By default 0.0035.

    Returns
    -------
    My : float | np.ndarray
        Yield moment (kN.m).
    phi_y : float | np.ndarray
        Yield curvature (1/m).
    cy : float | np.ndarray
        Neutral axis depth at yield (m).

    Notes
    -----
    - Yielding is controlled by the tension steel (Eqs. 1 and 4) if the
      neutral axis depth of the section with outer reinforcement only is
      below the balanced depth, and by the compression zone otherwise
      (Eqs. 2 and 5). For ``Nu = 0`` and ``As_int = 0`` Eqs. 4 and 5 give the
      same result, so the control only changes the yield curvature.
    - The neutral axis depth of the outer-reinforcement section uses the ACI
      318-25 rectangular stress block (Table 22.2.2.4.3).

    References
    ----------
    Panagiotakos, T. B., & Fardis, M. N. (2001).
    Deformations of reinforced concrete members at yielding and ultimate.
    Structural Journal, 98(2), 135-148.

    ACI CODE 318-25. (2025). Building Code for Structural Concrete-Code
    Requirements and Commentary. American Concrete Institute.
    """
    h, b, fc, Ec, Es, fsyl, As_tens, As_comp, As_int, Nu, dd = (
        np.asarray(x, dtype=float)
        for x in (h, b, fc, Ec, Es, fsyl, As_tens, As_comp, As_int, Nu, dd)
    )
    # Distance from ext. concrete fiber (comp.) to the rebars (comp.)
    dd_prime = h - dd if dd_prime is None else np.asarray(
        dd_prime, dtype=float)

    # Stress-block coefficient, Table 22.2.2.4.3 of ACI 318-25
    betac = np.where(
        fc < 27.6 * MPa, 0.85,
        np.where(fc > 55.17 * MPa, 0.65, 1.05 - 0.05 * fc / (6.9 * MPa)))
    # Modular ratio
    nyoung = Es / Ec
    # Yield strain of steel bars
    esy = fsyl / Es
    # Balanced c value: dist. to neutral axis from ext. conc. fiber (comp.)
    cb = (eps_cu * dd) / (eps_cu + esy)
    # Tension, compression and web longitudinal reinforcement ratios
    rhol_tens = As_tens / (b * dd)
    rhol_comp = As_comp / (b * dd)
    rhol_int = As_int / (b * dd)
    # Relative distance of the compression reinforcement
    delta = dd_prime / dd
    # Compute distance to neutral axis with outer faces (simplification)
    c = (As_tens * fsyl - As_comp * fsyl + Nu) / (0.85 * fc * b * betac)

    # Decide whether yielding is controlled by tension or compression zone
    tens_ctrl = c < cb
    # Yielding is controlled by the tension steel: Equation 4
    A_tens = rhol_tens + rhol_comp + rhol_int + (Nu / (b * dd * fsyl))
    B_tens = (rhol_tens + rhol_comp * delta
              + 0.5 * rhol_int * (1 + delta) + (Nu / (b * dd * fsyl)))
    # Yielding is controlled by the compression zone: Equation 5
    A_comp = (rhol_tens + rhol_comp + rhol_int
              - (Nu / (1.8 * nyoung * b * dd * fc)))
    B_comp = rhol_tens + rhol_comp * delta + 0.5 * rhol_int * (1 + delta)
    A_to_use = np.where(tens_ctrl, A_tens, A_comp)
    B_to_use = np.where(tens_ctrl, B_tens, B_comp)

    # The compression zone depth: Equation 3
    ky = (
        (nyoung**2) * (A_to_use**2) + (2 * nyoung * B_to_use)
    ) ** 0.5 - nyoung * A_to_use
    # Yield curvature: Equation 1 (tension steel) or 2 (compression zone)
    phi_y = np.where(
        tens_ctrl, fsyl / (Es * (1 - ky) * dd), (1.8 * fc) / (Ec * ky * dd))
    # Yield Moment: Equation 6
    term1 = (Ec * (ky**2) / 2) * (0.5 * (1 + delta) - (ky / 3))
    term2 = (
        (Es / 2)
        * (
            (1 - ky) * rhol_tens
            + (ky - delta) * rhol_comp
            + (rhol_int / 6) * (1 - delta)
        )
        * (1 - delta)
    )
    My = (b * (dd**3)) * phi_y * (term1 + term2)

    # Compute the neutral axis depth
    cy = ky * dd

    # Scalars are returned for scalar inputs
    return My[()], phi_y[()], cy[()]


def get_yield_rot_eurocode8(
    phi_y: float | np.ndarray, h: float | np.ndarray,
    Ls: float | np.ndarray, fc: float | np.ndarray,
    fsyl: float | np.ndarray, db: float | np.ndarray,
    bondslip_factor: float = 1.0, av: float | np.ndarray | None = None,
    z: float | np.ndarray | None = None, include_shear: bool = True,
    My: float | np.ndarray | None = None, b: float | np.ndarray | None = None,
    As_tens: float | np.ndarray | None = None,
    dd: float | np.ndarray | None = None, Nu: float | np.ndarray = 0.0
) -> float | np.ndarray:
    """Computes the yield chord rotation of an RC member with the expression
    of EN 1998-3:2005, Eq. (A.10b).

    The yield rotation is the sum of the flexural term (including the tension
    shift of the bending moment diagram), the shear term, and the term of the
    slip of the longitudinal bars from the anchorage zone (bond-slip):

    ``theta_y = phi_y (Ls + av z) / 3 + 0.0014 (1 + 1.5 h / Ls)
    + bondslip_factor phi_y db fsyl / (8 sqrt(fc))``

    where ``fsyl`` and ``fc`` are in MPa in the last term. ``av`` is 1 if
    shear cracking precedes flexural yielding and 0 otherwise. Unless it is
    given, it is determined from the yield moment and the shear resistance of
    the concrete, see :func:`_get_av_ec8` and :func:`_get_vrc_ec2`. The inputs
    may be
    scalars or arrays of the same shape (e.g., the start, mid and end
    sections of a beam), and the result has the same shape.

    Parameters
    ----------
    phi_y : float | np.ndarray
        Yield curvature of the end section (1/m).
    h : float | np.ndarray
        Section depth in the bending direction (m).
    Ls : float | np.ndarray
        Shear span (m), i.e., the moment-to-shear ratio at the end section.
    fc : float | np.ndarray
        Concrete compressive strength (kPa).
    fsyl : float | np.ndarray
        Yield strength of the longitudinal steel (kPa).
    db : float | np.ndarray
        Diameter of the longitudinal bars (m).
    bondslip_factor : float, optional
        Factor of the bond-slip term, 1.0 if the slip of the longitudinal bars
        from the anchorage zone is possible and 0.0 otherwise.
        By default 1.0.
    av : float | np.ndarray | None, optional
        Factor of the tension shift, 1.0 if shear cracking is expected to
        precede flexural yielding and 0.0 otherwise. If None, it is determined
        from `My`, `b`, `As_tens`, `dd` and `Nu`. By default None.
    z : float | np.ndarray | None, optional
        Lever arm (m). If None, ``0.9 * (0.9 * h)``, i.e., 0.9 times the
        effective depth 0.9 h.
    include_shear : bool, optional
        If True, the shear term is included. If False, it is left out, e.g.,
        if the shear deformations are modelled separately. By default True.
    My : float | np.ndarray | None, optional
        Yield moment of the end section (kNm). Required if `av` is None.
    b : float | np.ndarray | None, optional
        Section width (m). Required if `av` is None.
    As_tens : float | np.ndarray | None, optional
        Area of the tension reinforcement (m2). Required if `av` is None.
    dd : float | np.ndarray | None, optional
        Effective depth, i.e., the distance from the extreme compression fiber
        to the centroid of the tension reinforcement (m). Required if `av` is
        None.
    Nu : float | np.ndarray, optional
        Axial force, positive in compression (kN), used if `av` is None.
        By default 0.0, e.g., for beams.

    Returns
    -------
    float | np.ndarray
        Yield chord rotation.

    Raises
    ------
    ValueError
        If `av` is None and any of `My`, `b`, `As_tens` and `dd` is None.

    Notes
    -----
    - ``av z`` is the tension shift of the bending moment diagram, see
      EN 1992-1-1:2004, 9.2.1.3(2).
    - The shear term is the average shear distortion of the shear span at
      flexural yielding (Panagiotakos and Fardis, 2001).

    References
    ----------
    CEN (2005) Eurocode 8: Design of structures for earthquake resistance -
    Part 3: Assessment and retrofitting of existing buildings.
    Brussels, Belgium

    Panagiotakos, T. B., & Fardis, M. N. (2001).
    Deformations of reinforced concrete members at yielding and ultimate.
    Structural Journal, 98(2), 135-148.
    """
    fc_mpa = fc / MPa  # in MPa
    fsyl_mpa = fsyl / MPa  # in MPa
    # Factor of the tension shift
    if av is None:
        if any(x is None for x in (My, b, As_tens, dd)):
            raise ValueError(
                "My, b, As_tens and dd must be given if av is None.")
        VRc = _get_vrc_ec2(b, dd, As_tens, fc, Nu, h)
        av = _get_av_ec8(My, Ls, VRc)
    # Lever arm
    if z is None:
        z = 0.9 * (0.9 * h)
    theta_y1 = phi_y * ((Ls + (av * z)) / 3)  # Flexure and tension shift
    theta_y2 = 0.0014 * (1 + 1.5 * h / Ls) if include_shear else 0.0  # Shear
    theta_y3 = 0.125 * phi_y * db * (fsyl_mpa / (fc_mpa**0.50))  # Bond-slip
    return theta_y1 + theta_y2 + bondslip_factor * theta_y3


def _get_vrc_ec2(
    b_w: float | np.ndarray, d: float | np.ndarray,
    A_sl: float | np.ndarray, f_ck: float | np.ndarray,
    N_Ed: float | np.ndarray = 0.0, h: float | np.ndarray | None = None,
    gamma_c: float = 1.0, k1: float = 0.15
) -> float | np.ndarray:
    """Computes the shear resistance of a member without shear
    reinforcement ``V_R,c``, i.e., the concrete shear cracking resistance,
    with the expressions of EN 1992-1-1:2004, Cl. 6.2.2:

    ``V_R,c = max(C_Rc k (100 rho_l f_ck)^(1/3) + k1 sigma_cp,
    v_min + k1 sigma_cp) b_w d``

    with ``C_Rc = 0.18 / gamma_c``, the size effect factor
    ``k = min(1 + sqrt(200 / d), 2)``, the longitudinal reinforcement ratio
    ``rho_l = min(A_sl / (b_w d), 0.02)``, the axial stress
    ``0 <= sigma_cp = N_Ed / A_c <= 0.2 f_ck / gamma_c`` and the lower bound
    ``v_min = 0.035 k^(3/2) f_ck^(1/2)``. The inputs may be scalars, lists or
    arrays of the same shape, and the result has the same shape.

    Parameters
    ----------
    b_w : float | np.ndarray
        Web width (m).
    d : float | np.ndarray
        Effective depth (m).
    A_sl : float | np.ndarray
        Area of the tension reinforcement (m2).
    f_ck : float | np.ndarray
        Concrete compressive strength (kPa).
    N_Ed : float | np.ndarray, optional
        Axial force, positive in compression (kN). By default 0.0.
    h : float | np.ndarray | None, optional
        Total section depth (m), used for the gross section area
        ``A_c = b_w h`` of the axial stress. If None, it is estimated as
        ``d / 0.9``. By default None.
    gamma_c : float, optional
        Partial safety factor of the concrete, 1.0 for the assessment of
        existing buildings with EN 1998-3. By default 1.0.
    k1 : float, optional
        Factor of the axial stress, the recommended value of EN 1992-1-1
        Cl. 6.2.2(1). By default 0.15.

    Returns
    -------
    float | np.ndarray
        Shear resistance ``V_R,c`` (kN). A float for scalar inputs.

    Notes
    -----
    The expressions of EN 1992-1-1 are evaluated in N, mm and MPa internally.

    References
    ----------
    CEN (2004) Eurocode 2: Design of concrete structures - Part 1-1: General
    rules and rules for buildings. EN 1992-1-1:2004. Brussels, Belgium
    """
    # Convert inputs to numpy arrays (handles scalars, lists, and arrays) in
    # N, mm and MPa, the units of the expressions of the code
    b_w = np.asarray(b_w, dtype=float) / mm
    d = np.asarray(d, dtype=float) / mm
    A_sl = np.asarray(A_sl, dtype=float) / mm**2
    f_ck = np.asarray(f_ck, dtype=float) / MPa
    N_Ed = np.asarray(N_Ed, dtype=float) / N

    # Gross section area Ac: use h if given, otherwise estimate h ≈ d / 0.9
    if h is None:
        A_c = b_w * (d / 0.9)
    else:
        A_c = b_w * (np.asarray(h, dtype=float) / mm)

    # 1. Size effect factor: k = 1 + sqrt(200 / d) <= 2.0
    k = np.minimum(1.0 + (200.0 / d) ** 0.5, 2.0)

    # 2. Longitudinal reinforcement ratio: rho_l <= 0.02
    rho_l = np.minimum(A_sl / (b_w * d), 0.02)

    # 3. Axial stress: 0 <= sigma_cp <= 0.2 * f_cd
    f_cd = f_ck / gamma_c
    sigma_cp = np.maximum(0.0, N_Ed / A_c)
    sigma_cp = np.minimum(sigma_cp, 0.2 * f_cd)

    # 4. Coefficients and lower bound v_min
    C_Rc = 0.18 / gamma_c
    v_min = 0.035 * (k ** 1.5) * (f_ck ** 0.5)

    # 5. Shear strength formulations (MPa)
    v_rc_standard = (C_Rc * k * ((100.0 * rho_l * f_ck) ** (1.0 / 3.0))
                     + k1 * sigma_cp)
    v_rc_min = v_min + k1 * sigma_cp

    # Governing shear stress and capacity
    v_rc = np.maximum(v_rc_standard, v_rc_min)
    V_Rc = (v_rc * b_w * d) * N  # in base force unit (kN)

    # Return float if input was a scalar, array otherwise
    if V_Rc.ndim == 0:
        return float(V_Rc)
    return V_Rc


def _get_av_ec8(
    My: float | np.ndarray, Ls: float | np.ndarray,
    VRc: float | np.ndarray
) -> float | np.ndarray:
    """Determines the factor ``av`` of the tension shift in the yield chord
    rotation of EN 1998-3, Eq. (A.10b), see :func:`get_yield_rot_eurocode8`.

    ``av`` is 1 if shear cracking precedes flexural yielding at the end
    section and 0 otherwise, i.e., ``av = 0`` if the yield moment is lower
    than the shear span times the shear resistance of the concrete,
    ``My < Ls VRc``. The inputs may be scalars or arrays of the same shape
    (e.g., the sections or the bending directions of a beam), and the result
    has the same shape.

    Parameters
    ----------
    My : float | np.ndarray
        Yield moment of the end section (kNm).
    Ls : float | np.ndarray
        Shear span (m), i.e., the moment-to-shear ratio at the end section.
    VRc : float | np.ndarray
        Shear resistance of the member without shear reinforcement (kN), i.e.,
        the shear cracking resistance, e.g., from :func:`_get_vrc_ec2`.

    Returns
    -------
    float | np.ndarray
        1.0 if shear cracking precedes flexural yielding, 0.0 otherwise.

    See Also
    --------
    _get_vrc_ec2 : Shear resistance of the concrete.
    get_yield_rot_eurocode8 : Yield chord rotation, which uses ``av``.

    References
    ----------
    CEN (2005) Eurocode 8: Design of structures for earthquake resistance -
    Part 3: Assessment and retrofitting of existing buildings.
    Brussels, Belgium
    """
    av = np.where(My < Ls * VRc, 0.0, 1.0)
    # Scalars are returned for scalar inputs
    return av[()]


def get_capping_mom_plastic_rot_haselton2016(
    My: float | np.ndarray, fc: float | np.ndarray,
    fsyl: float | np.ndarray, rhol: float | np.ndarray,
    rhoh: float | np.ndarray, sbh: float | np.ndarray,
    dbl: float | np.ndarray, niu: float | np.ndarray = 0.0,
    bondslip_factor: float = 1.0,
    rhol_tens: float | np.ndarray | None = None,
    rhol_comp: float | np.ndarray | None = None,
    cyclic_model: bool = False
) -> Tuple[float | np.ndarray, float | np.ndarray]:
    """Computes the capping (maximum) moment and the plastic rotation capacity
    of an RC member with the expressions of Haselton et al. (2016).

    The plastic rotation capacity is the rotation between yielding and the
    peak moment (Eq. 5). The capping moment is the yield moment times the
    ratio ``Mc / My = 1.25 (0.89^niu) (0.91^(0.01 fc))`` (Haselton et al.,
    2008, Eq. 3.17). The inputs may be scalars or arrays of the same shape,
    and the results have the same shape.

    Parameters
    ----------
    My : float | np.ndarray
        Yield moment.
    fc : float | np.ndarray
        Concrete compressive strength (kPa).
    fsyl : float | np.ndarray
        Yield strength of the longitudinal steel (kPa).
    rhol : float | np.ndarray
        Longitudinal reinforcement ratio ``As / (b h)``.
    rhoh : float | np.ndarray
        Transverse reinforcement ratio ``Ash / (s b)``.
    sbh : float | np.ndarray
        Spacing of the transverse reinforcement.
    dbl : float | np.ndarray
        Diameter of the longitudinal bars, used for the slenderness of the
        bars between the stirrups ``sn = (sbh / dbl) sqrt(fsyl / 100)``, with
        ``fsyl`` in MPa (Dhakal and Maekawa, 2002).
    niu : float | np.ndarray, optional
        Axial load ratio ``P / (Ag fc)``. By default 0.0, e.g., for beams.
    bondslip_factor : float, optional
        Coefficient ``a_sl``, 1.0 if bond-slip is included in the yield
        rotation and 0.0 otherwise. By default 1.0.
    rhol_tens : float | np.ndarray | None, optional
        Longitudinal reinforcement ratio on the tension side of a
        non-symmetric section, for the bending direction considered. It must
        be given together with `rhol_comp`. If None, the section is taken as
        symmetric. By default None.
    rhol_comp : float | np.ndarray | None, optional
        Longitudinal reinforcement ratio on the compression side of a
        non-symmetric section, for the bending direction considered.
        By default None.
    cyclic_model : bool, optional
        If True, the plastic rotation capacity is reduced for cyclic loading
        with a factor of 0.7 (Haselton et al., 2016, Eq. 12). By default
        False.

    Returns
    -------
    Mc : float | np.ndarray
        Capping (maximum) moment.
    theta_cap_pl : float | np.ndarray
        Plastic rotation capacity, i.e., from yielding to the capping moment.

    Raises
    ------
    ValueError
        If only one of `rhol_tens` and `rhol_comp` is given.

    Notes
    -----
    - Haselton et al. (2016) use a constant ``Mc / My = 1.13`` (Eq. 9),
      because the axial load ratio and the concrete strength explain little
      of its variation (R2 of 0.17). This function uses the expression of
      Haselton et al. (2008).
    - For a non-symmetric section, the plastic rotation capacity is multiplied
      by ``(max(0.01, w_comp) / max(0.01, w_tens))^0.225``, with the
      mechanical reinforcement ratios ``w = rhol fsyl / fc`` of the
      compression and tension sides (Haselton et al., 2016, Eq. 7).

    References
    ----------
    Haselton, C. B., Liel, A. B., Taylor-Lange, S. C., & Deierlein, G. G.
    (2016). Calibration of model to simulate response of reinforced
    concrete beam-columns to collapse. ACI Structural Journal, 113(6).

    Haselton, C. B., Liel, A. B., Lange, S. T., & Deierlein, G. G. (2008).
    Beam-column element model calibrated for predicting flexural response
    leading to global collapse of RC frame buildings. Pacific Earthquake
    Engineering Research Center, University of California, Berkeley, CA.

    Dhakal, R. P., & Maekawa, K. (2002). Modeling for postyield buckling of
    reinforcement. Journal of Structural Engineering, 128(9).
    """
    if (rhol_tens is None) != (rhol_comp is None):
        raise ValueError(
            "rhol_tens and rhol_comp must be given together.")
    fc_mpa = fc / MPa  # in MPa
    fsyl_mpa = fsyl / MPa  # in MPa
    # Reinforcing bar buckling coefficient, by Dhakal and Maekawa 2002
    sn = (sbh / dbl) * (fsyl_mpa / 100) ** 0.5
    # Capping moment to yield moment ratio - Haselton et al. 2008 - Eq. 3.17
    Mc_My = 1.25 * (0.89**niu) * (0.91 ** (0.01 * fc_mpa))
    Mc = Mc_My * My
    # Plastic rotation capacity by Haselton et al. 2016 - Equation 5
    theta_cap_pl = (
        0.12
        * (1 + 0.55 * bondslip_factor)
        * (0.16**niu)
        * ((0.02 + 40 * rhoh) ** 0.43)
        * (0.54 ** (0.01 * fc_mpa))
        * (0.66 ** (0.1 * sn))
        * (2.27 ** (10.0 * rhol))
    )
    # Non-symmetric section - Equation 7
    if rhol_tens is not None:
        w_tens = np.maximum(0.01, fsyl_mpa * rhol_tens / fc_mpa)
        w_comp = np.maximum(0.01, fsyl_mpa * rhol_comp / fc_mpa)
        theta_cap_pl = ((w_comp / w_tens) ** 0.225) * theta_cap_pl
    # Rotation values needs to be adjusted for cyclic loading - Equation 12
    if cyclic_model:
        theta_cap_pl = 0.7 * theta_cap_pl
    return Mc, theta_cap_pl


def get_residual_mom_post_capping_rot_haselton2016(
    Mc: float | np.ndarray, rhoh: float | np.ndarray,
    niu: float | np.ndarray = 0.0, Mr_Mc: float = 0.1,
    cyclic_model: bool = False
) -> Tuple[float | np.ndarray, float | np.ndarray]:
    """Computes the residual moment and the post-capping rotation capacity of
    an RC member with the expressions of Haselton et al. (2016).

    The post-capping rotation capacity is the rotation between the peak
    moment and the residual moment (Eq. 8), limited to 0.10 rad. The inputs
    may be scalars or arrays of the same shape, and the results have the same
    shape.

    Parameters
    ----------
    Mc : float | np.ndarray
        Capping (maximum) moment.
    rhoh : float | np.ndarray
        Transverse reinforcement ratio ``Ash / (s b)``.
    niu : float | np.ndarray, optional
        Axial load ratio ``P / (Ag fc)``. By default 0.0, e.g., for beams.
    Mr_Mc : float, optional
        Ratio of the residual moment to the capping moment, which is assumed.
        By default 0.1.
    cyclic_model : bool, optional
        If True, the post-capping rotation capacity is reduced for cyclic
        loading with a factor of 0.5 (Haselton et al., 2016, Eq. 13).
        By default False.

    Returns
    -------
    Mr : float | np.ndarray
        Residual moment.
    theta_pc : float | np.ndarray
        Post-capping rotation capacity, i.e., from the capping moment to the
        residual moment.

    References
    ----------
    Haselton, C. B., Liel, A. B., Taylor-Lange, S. C., & Deierlein, G. G.
    (2016). Calibration of model to simulate response of reinforced
    concrete beam-columns to collapse. ACI Structural Journal, 113(6).
    """
    # Residual moment capacity
    Mr = Mr_Mc * Mc
    # Post-capping rotation capacity by Haselton et al. 2016 - Equation 8
    theta_pc = np.minimum(
        0.10, 0.76 * (0.031**niu) * ((0.02 + 40 * rhoh) ** 1.02))
    # Rotation values needs to be adjusted for cyclic loading - Equation 13
    if cyclic_model:
        theta_pc = 0.5 * theta_pc
    return Mr, theta_pc


def get_lp_priestley_2007(
    Ls: float | np.ndarray, fsyl: float | np.ndarray,
    db: float | np.ndarray
) -> float | np.ndarray:
    """Computes the plastic hinge length of an RC member with the expression
    of Priestley et al. (2007):

    ``Lp = 0.08 Ls + 0.022 fsyl db``

    where ``fsyl`` is in MPa and ``Ls`` and ``db`` are in mm. The inputs may
    be scalars or arrays of the same shape (e.g., the start, mid and end
    sections of a beam), and the result has the same shape.

    Parameters
    ----------
    Ls : float | np.ndarray
        Shear span (m), i.e., the moment-to-shear ratio at the end section.
    fsyl : float | np.ndarray
        Yield strength of the longitudinal steel (kPa).
    db : float | np.ndarray
        Diameter of the longitudinal bars (m).

    Returns
    -------
    float | np.ndarray
        Plastic hinge length (m), rounded to the precision of the package.

    References
    ----------
    Priestley, M. J. N., Calvi, G. M., & Kowalsky, M. J. (2007).
    *Displacement-based seismic design of structures*. IUSS Press.
    """
    # The expression is in mm and MPa
    Lp = 0.08 * (Ls / mm) + 0.022 * (fsyl / MPa) * (db / mm)
    return np.round(Lp, PRECISION) * mm


def get_shear_cracking_sezen_moehle2004(
    fc: float | np.ndarray, Gc: float | np.ndarray,
    Ag: float | np.ndarray, d: float | np.ndarray,
    Ls: float | np.ndarray, P: float | np.ndarray = 0.0
) -> Tuple[float | np.ndarray, float | np.ndarray]:
    """Computes the shear force and shear strain at diagonal cracking of an
    RC column with the expression of Sezen and Moehle (2004), Eq. 11:

    ``V1 = fct / (a / d) sqrt(1 + P / (fct Ag)) Ae``

    with the shear span ratio ``a / d = Ls / d`` limited to 2-4, the tensile
    strength of the concrete ``fct = sqrt(fc) / 3`` (in MPa, Collins and
    Mitchell, 1997, Eq. 3-16) instead of ``0.5 sqrt(fc)``, and the effective
    shear area ``Ae = 0.8 Ag``. The cracking shear strain is
    ``gamma1 = V1 / (Gc Ae)``, i.e., the uncracked shear stiffness (Zimos et
    al., 2015). The inputs may be scalars or arrays of the same shape, and
    the results have the same shape.

    Parameters
    ----------
    fc : float | np.ndarray
        Concrete compressive strength (kPa).
    Gc : float | np.ndarray
        Shear modulus of the concrete (kPa).
    Ag : float | np.ndarray
        Gross area of the section (m2).
    d : float | np.ndarray
        Effective depth (m).
    Ls : float | np.ndarray
        Shear span (m).
    P : float | np.ndarray, optional
        Axial force, positive in compression (kN). By default 0.0.

    Returns
    -------
    V1 : float | np.ndarray
        Shear force at diagonal cracking (kN).
    gamma1 : float | np.ndarray
        Shear strain at diagonal cracking.

    References
    ----------
    Sezen, H., & Moehle, J. P. (2004). Shear strength model for lightly
    reinforced concrete columns. Journal of Structural Engineering,
    130(11), 1692-1703.

    Collins, M. P., & Mitchell, D. (1997). Prestressed concrete structures.
    Prentice Hall.

    Zimos, D. K., Mergos, P. E., & Kappos, A. J. (2015). Shear hysteresis
    model for reinforced concrete elements including the post-peak range.
    Proceedings of COMPDYN 2015.
    """
    fc_mpa = fc / MPa  # in MPa
    # Effective shear area for rectangular sections
    Ae = 0.8 * Ag
    # Concrete tensile strength - Collins and Mitchell (1997) - Eq. 3-16
    fct = ((fc_mpa**0.5) / 3.0) * MPa
    # Shear span ratio, 2 <= a/d <= 4
    a_d = np.minimum(np.maximum(Ls / d, 2.0), 4.0)
    # Cracking shear - Sezen and Moehle (2004) - Eq. 11
    V1 = fct / a_d * np.sqrt(1 + P / (fct * Ag)) * Ae
    # Cracking shear strain with the uncracked shear stiffness
    gamma1 = V1 / (Gc * Ae)
    return V1, gamma1


def get_shear_strength_priestley1994(
    fc: float | np.ndarray, Ag: float | np.ndarray,
    h: float | np.ndarray, c: float | np.ndarray,
    Ls: float | np.ndarray, Av: float | np.ndarray,
    fsyh: float | np.ndarray, hc: float | np.ndarray,
    sbh: float | np.ndarray, P: float | np.ndarray = 0.0,
    k: float = 0.29, theta: float = 45.0
) -> Tuple[float | np.ndarray, float | np.ndarray, float | np.ndarray]:
    """Computes the components of the shear strength of an RC column with
    the expressions of Priestley et al. (1994):

    - concrete, Eq. 27: ``Vc = k sqrt(fc) Ae`` (``fc`` in MPa), with the
      effective shear area ``Ae = 0.8 Ag``;
    - axial load, Eq. 28: ``Vp = P (h - c) / (2 Ls)``, zero if ``c > h``;
    - truss mechanism, Eq. 29: ``Vs = (Av fsyh hc / sbh) cot(theta)``.

    The shear strength is ``Vc + Vp + Vs``. The inputs may be scalars or
    arrays of the same shape, and the results have the same shape.

    Parameters
    ----------
    fc : float | np.ndarray
        Concrete compressive strength (kPa).
    Ag : float | np.ndarray
        Gross area of the section (m2).
    h : float | np.ndarray
        Section depth parallel to the shear force (m).
    c : float | np.ndarray
        Neutral axis depth (m).
    Ls : float | np.ndarray
        Shear span (m).
    Av : float | np.ndarray
        Area of the transverse reinforcement within the spacing ``sbh``,
        parallel to the shear force (m2).
    fsyh : float | np.ndarray
        Yield strength of the transverse reinforcement (kPa).
    hc : float | np.ndarray
        Core dimension parallel to the shear force, measured to the
        centreline of the transverse reinforcement (m).
    sbh : float | np.ndarray
        Spacing of the transverse reinforcement (m).
    P : float | np.ndarray, optional
        Axial force, positive in compression (kN). By default 0.0.
    k : float, optional
        Factor of the concrete component, which depends on the member
        displacement ductility (Fig. 7 of the reference). By default 0.29,
        for low ductility.
    theta : float, optional
        Angle of the diagonal compression struts to the member axis
        (degrees). By default 45.0 (Zimos et al., 2015).

    Returns
    -------
    Vc : float | np.ndarray
        Concrete component (kN).
    Vp : float | np.ndarray
        Axial load component (kN).
    Vs : float | np.ndarray
        Truss mechanism component (kN).

    References
    ----------
    Priestley, M. N., Verma, R., & Xiao, Y. (1994). Seismic shear strength
    of reinforced concrete columns. Journal of Structural Engineering,
    120(8), 2310-2329.
    """
    fc_mpa = fc / MPa  # in MPa
    # Effective shear area for rectangular sections
    Ae = 0.8 * Ag
    # Concrete component - Eq. 27
    Vc = k * ((fc_mpa**0.5) * MPa) * Ae
    # Axial load component - Eq. 28 (no axial term if c > h)
    Vp = P * np.maximum(h - c, 0.0) / (2 * Ls)
    # Truss mechanism component - Eq. 29
    cot_th = 1 / np.tan(np.deg2rad(theta))
    Vs = (Av * fsyh * hc / sbh) * cot_th
    return Vc, Vp, Vs


def get_shear_strains_mergos_kappos2012(
    V1: float | np.ndarray, gamma1: float | np.ndarray,
    V2: float | np.ndarray, Es: float | np.ndarray,
    Ec: float | np.ndarray, b: float | np.ndarray,
    hc: float | np.ndarray, rhoh: float | np.ndarray,
    fsyh: float | np.ndarray, fc: float | np.ndarray,
    Ls: float | np.ndarray, h: float | np.ndarray,
    nu: float | np.ndarray = 0.0, theta: float = 45.0
) -> Tuple[float | np.ndarray, float | np.ndarray, float | np.ndarray]:
    """Computes the cracked shear stiffness and the shear strains at the
    maximum shear force and at the onset of shear failure of an RC column
    with the expressions of Mergos and Kappos (2012).

    The cracked shear stiffness follows the truss analogy (Eq. 7), with the
    core dimension ``hc`` instead of ``d - d'``. The shear strain at the
    maximum shear force ``V2`` is the truss strain
    ``gamma1 + (V2 - V1) / GA1`` corrected for the axial load and the shear
    span (Eqs. 8-10), and the shear strain at the onset of shear failure
    follows Eq. 11. The axial load ratio, the shear span ratio and the
    mechanical transverse reinforcement ratio are limited to the ranges of
    the calibration (0.6 or 0.4, 2.5 and 0.08). The inputs may be scalars or
    arrays of the same shape, and the results have the same shape.

    Parameters
    ----------
    V1 : float | np.ndarray
        Shear force at diagonal cracking (kN).
    gamma1 : float | np.ndarray
        Shear strain at diagonal cracking.
    V2 : float | np.ndarray
        Maximum shear force (kN).
    Es : float | np.ndarray
        Elastic modulus of the transverse reinforcement (kPa).
    Ec : float | np.ndarray
        Elastic modulus of the concrete (kPa).
    b : float | np.ndarray
        Section width perpendicular to the shear force (m).
    hc : float | np.ndarray
        Core dimension parallel to the shear force, measured to the
        centreline of the transverse reinforcement (m).
    rhoh : float | np.ndarray
        Transverse reinforcement ratio parallel to the shear force.
    fsyh : float | np.ndarray
        Yield strength of the transverse reinforcement (kPa).
    fc : float | np.ndarray
        Concrete compressive strength (kPa).
    Ls : float | np.ndarray
        Shear span (m).
    h : float | np.ndarray
        Section depth parallel to the shear force (m).
    nu : float | np.ndarray, optional
        Axial load ratio ``P / (Ag fc)``. By default 0.0.
    theta : float, optional
        Angle of the diagonal compression struts to the member axis
        (degrees). By default 45.0.

    Returns
    -------
    GA1 : float | np.ndarray
        Cracked shear stiffness (kN).
    gamma2 : float | np.ndarray
        Shear strain at the maximum shear force.
    gamma3 : float | np.ndarray
        Shear strain at the onset of shear failure.

    References
    ----------
    Mergos, P. E., & Kappos, A. J. (2012). A gradual spread inelasticity
    model for R/C beam-columns, accounting for flexure, shear and anchorage
    slip. Engineering Structures, 44, 94-106.
    """
    cot_th = 1 / np.tan(np.deg2rad(theta))
    sin4_th = np.sin(np.deg2rad(theta))**4
    cot2_th = cot_th**2
    # Modular ratio
    eta = Es / Ec
    # Cracked shear stiffness - Eq. 7
    GA1 = (Es * b * hc * rhoh * sin4_th * cot2_th) / (sin4_th + eta * rhoh)
    # Shear strain at the maximum shear force from the truss analogy
    gamma_truss = gamma1 + (V2 - V1) / GA1
    # Corrections of the truss strain - Eqs. 8-10
    kappa = 1 - 1.07 * np.minimum(nu, 0.6)  # Eq. 8
    lambda_ = 5.37 - 1.59 * np.minimum(Ls / h, 2.5)  # Eq. 9
    gamma2 = kappa * lambda_ * gamma_truss  # Eq. 10
    # Shear strain at the onset of shear failure - Eq. 11
    omega_k = rhoh * fsyh / fc  # Eq. 11.5
    lambda_1 = 1 - 2.5 * np.minimum(nu, 0.4)  # Eq. 11.2
    lambda_2 = np.minimum(Ls / h, 2.5)**2  # Eq. 11.3
    lambda_3 = 0.31 + 17.8 * np.minimum(omega_k, 0.08)  # Eq. 11.4
    gamma3 = np.maximum(lambda_1 * lambda_2 * lambda_3, 1) * gamma2  # 11.1
    return GA1, gamma2, gamma3


def get_shear_post_peak_zimos2015(
    Vmax: float | np.ndarray, P: float | np.ndarray,
    b: float | np.ndarray, d: float | np.ndarray,
    Ag: float | np.ndarray, Ac: float | np.ndarray,
    rhol: float | np.ndarray, rhoh: float | np.ndarray,
    fc: float | np.ndarray, fsyl: float | np.ndarray,
    fsyh: float | np.ndarray, sbh: float | np.ndarray,
    dbl: float | np.ndarray, nu: float | np.ndarray = 0.0
) -> Tuple[float | np.ndarray, float | np.ndarray]:
    """Computes the slope of the descending branch and the total post-peak
    shear strain of an RC column with the expressions of Zimos et al.
    (2015).

    The residual shear force is ``Vmax (1 - Spp gamma_tpp)`` (Eq. 3), with
    the normalised slope of the descending branch ``Spp`` (Eq. 4) and the
    total post-peak shear strain ``gamma_tpp`` (Eq. 7), which is zero
    without axial load. The inputs may be scalars or arrays of the same
    shape, and the results have the same shape.

    Parameters
    ----------
    Vmax : float | np.ndarray
        Maximum shear force (kN).
    P : float | np.ndarray
        Axial force, positive in compression (kN).
    b : float | np.ndarray
        Section width perpendicular to the shear force (m).
    d : float | np.ndarray
        Effective depth (m).
    Ag : float | np.ndarray
        Gross area of the section (m2).
    Ac : float | np.ndarray
        Area of the confined concrete core (m2).
    rhol : float | np.ndarray
        Longitudinal reinforcement ratio ``Asl / Ag``.
    rhoh : float | np.ndarray
        Transverse reinforcement ratio parallel to the shear force.
    fc : float | np.ndarray
        Concrete compressive strength (kPa).
    fsyl : float | np.ndarray
        Yield strength of the longitudinal reinforcement (kPa).
    fsyh : float | np.ndarray
        Yield strength of the transverse reinforcement (kPa).
    sbh : float | np.ndarray
        Spacing of the transverse reinforcement (m).
    dbl : float | np.ndarray
        Average diameter of the longitudinal bars (m).
    nu : float | np.ndarray, optional
        Axial load ratio ``P / (Ag fc)``. By default 0.0.

    Returns
    -------
    Spp : float | np.ndarray
        Normalised slope of the descending branch, i.e., the relative drop
        of the shear force per unit shear strain.
    gamma_tpp : float | np.ndarray
        Total post-peak shear strain.

    References
    ----------
    Zimos, D. K., Mergos, P. E., & Kappos, A. J. (2015). Shear hysteresis
    model for reinforced concrete elements including the post-peak range.
    Proceedings of COMPDYN 2015.
    """
    # Expressions in MPa
    fc_mpa = fc / MPa
    fsyl_mpa = fsyl / MPa
    fsyh_mpa = fsyh / MPa
    # Axial load ratio of the longitudinal reinforcement
    nu_l = np.asarray(P, dtype=float) / ((rhol * Ag) * fsyl)
    # Maximum average shear stress (MPa)
    tau_ave_max = Vmax / (b * d) / MPa
    # Ratio of confined to gross concrete area
    aconf = Ac / Ag
    # Total post-peak shear strain - Eq. 7 (zero without axial load)
    with np.errstate(divide='ignore'):
        gamma_tpp = np.maximum(
            (0.65 * (rhol / aconf) ** 1.2)
            / (
                (
                    (rhoh * fsyh_mpa)
                    / (nu_l * (sbh / d) * (tau_ave_max / (fc_mpa**0.5)))
                )
                ** 0.5
            ),
            0
        )
    # Normalised slope of the descending branch - Eq. 4
    Spp = 7.36 + (0.28 * (nu + 0.02) ** 0.5) / (
        (rhoh + 0.0011)
        * ((fsyl_mpa * rhol / aconf) * (dbl / d) + 0.06)
    )
    # Scalars are returned for scalar inputs
    return Spp, gamma_tpp[()]


def get_shear_residual_zimos2015(
    Vmax: float | np.ndarray, Spp: float | np.ndarray,
    gamma_tpp: float | np.ndarray, Vr_Vmax: float = 0.1
) -> Tuple[float | np.ndarray, float | np.ndarray]:
    """Computes the residual point of the shear force - shear strain
    backbone of an RC column with the linear descending branch of Zimos et
    al. (2015), Eq. 3:

    ``V = Vmax (1 - Spp (gamma - gamma_sh,f))``

    The residual point is at the onset of axial failure, i.e., at the total
    post-peak shear strain ``gamma_tpp`` after the onset of shear failure
    ``gamma_sh,f``. If the shear force there is lower than ``Vr_Vmax Vmax``
    (or negative, if the shear strength vanishes before axial failure), the
    residual point is taken on the descending branch where the shear force
    is ``Vr_Vmax Vmax``, i.e., at ``gamma_tpp = (1 - Vr_Vmax) / Spp``, so
    that the slope of the branch is kept. The inputs may be scalars or
    arrays of the same shape, and the results have the same shape.

    Parameters
    ----------
    Vmax : float | np.ndarray
        Maximum shear force, at the onset of shear failure (kN).
    Spp : float | np.ndarray
        Normalised slope of the descending branch, see
        :func:`get_shear_post_peak_zimos2015`.
    gamma_tpp : float | np.ndarray
        Total post-peak shear strain at the onset of axial failure, see
        :func:`get_shear_post_peak_zimos2015`.
    Vr_Vmax : float, optional
        Minimum ratio of the residual to the maximum shear force, which is
        assumed. By default 0.1.

    Returns
    -------
    Vr : float | np.ndarray
        Residual shear force (kN).
    gamma_tpp : float | np.ndarray
        Post-peak shear strain of the residual point, i.e., from the onset of
        shear failure.

    References
    ----------
    Zimos, D. K., Mergos, P. E., & Kappos, A. J. (2015). Shear hysteresis
    model for reinforced concrete elements including the post-peak range.
    Proceedings of COMPDYN 2015.
    """
    # Residual shear force at the onset of axial failure - Eq. 3
    Vr = Vmax * (1 - Spp * gamma_tpp)
    # Residual point on the descending branch at the minimum shear force
    floor = Vr < Vr_Vmax * Vmax
    Vr = np.where(floor, Vr_Vmax * Vmax, Vr)
    gamma_tpp = np.where(floor, (1 - Vr_Vmax) / Spp, gamma_tpp)
    # Scalars are returned for scalar inputs
    return Vr[()], gamma_tpp[()]


def get_shear_strength_asce41_17(
    fc: float | np.ndarray, Ag: float | np.ndarray,
    d: float | np.ndarray, Av: float | np.ndarray,
    fsyh: float | np.ndarray, sbh: float | np.ndarray,
    Ls: float | np.ndarray, P: float | np.ndarray = 0.0,
    k: float = 1.0, lambda_: float = 1.0
) -> float | np.ndarray:
    """Computes the shear strength of an RC column with the expression of
    ASCE/SEI 41-17, Eq. 10-3 (after Sezen and Moehle, 2004):

    ``Vn = k [alpha Av fyt d / s + lambda (0.5 sqrt(fc) / (M / V d))
    sqrt(1 + P / (0.5 sqrt(fc) Ag)) 0.8 Ag]``

    in MPa, with ``M / V d = Ls / d`` limited to 2-4, and the effectiveness
    factor of the transverse reinforcement ``alpha`` equal to 1 for
    ``s / d <= 0.75``, 0 for ``s / d >= 1`` and linear in between. The inputs
    may be scalars, and the result has the same shape.

    Parameters
    ----------
    fc : float | np.ndarray
        Concrete compressive strength (kPa).
    Ag : float | np.ndarray
        Gross area of the section (m2).
    d : float | np.ndarray
        Effective depth (m); ASCE/SEI 41-17 permits ``0.8 h``.
    Av : float | np.ndarray
        Area of the transverse reinforcement within the spacing ``sbh``,
        parallel to the shear force (m2).
    fsyh : float | np.ndarray
        Yield strength of the transverse reinforcement (kPa).
    sbh : float | np.ndarray
        Spacing of the transverse reinforcement (m).
    Ls : float | np.ndarray
        Shear span (m), i.e., the largest moment-to-shear ratio ``M / V``.
    P : float | np.ndarray, optional
        Axial force, positive in compression (kN). By default 0.0.
    k : float, optional
        Factor of the strength degradation with the displacement ductility,
        1.0 for the initial strength. By default 1.0.
    lambda_ : float, optional
        Factor of the concrete aggregate, 1.0 for normal-weight concrete.
        By default 1.0.

    Returns
    -------
    float | np.ndarray
        Shear strength (kN).

    References
    ----------
    ASCE/SEI 41-17. (2017). Seismic evaluation and retrofit of existing
    buildings. American Society of Civil Engineers.

    Sezen, H., & Moehle, J. P. (2004). Shear strength model for lightly
    reinforced concrete columns. Journal of Structural Engineering,
    130(11), 1692-1703.
    """
    # The expression is in MN, m and MPa
    fc_mpa = fc / MPa
    fsyh_mpa = fsyh / MPa
    P_mn = P / MN
    # Effectiveness factor of the transverse reinforcement
    alpha = np.interp(sbh / d, [0.75, 1.0], [1.0, 0.0])
    # Moment-to-shear ratio over the effective depth, 2 <= M/Vd <= 4
    M_Vd_rat = np.minimum(np.maximum(Ls / d, 2), 4)
    Vn = k * (
        alpha * (Av * fsyh_mpa * d / sbh)
        + lambda_
        * (
            (fc_mpa**0.5)
            / (2 * M_Vd_rat)
            * (1 + (2 * P_mn) / ((fc_mpa**0.5) * Ag)) ** 0.5
        )
        * (0.8 * Ag)
    )
    # Convert from MN to the base force unit (kN)
    return Vn * MN


def get_shear_stiffness_leborgne_ghannoum2014(
    Gc: float | np.ndarray, Ag: float | np.ndarray,
    L: float | np.ndarray
) -> float | np.ndarray:
    """Computes the elastic stiffness of the shear-drift spring of an RC
    column with the expression of LeBorgne and Ghannoum (2014), Eq. 1:

    ``k_el = (5 / 6) Gc Ag / L``

    i.e., the shear stiffness of the rectangular member. The inputs may be
    scalars or arrays of the same shape, and the result has the same shape.

    Parameters
    ----------
    Gc : float | np.ndarray
        Shear modulus of the concrete (kPa).
    Ag : float | np.ndarray
        Gross area of the section (m2).
    L : float | np.ndarray
        Clear length of the member (m).

    Returns
    -------
    float | np.ndarray
        Elastic stiffness of the shear spring (kN/m).

    References
    ----------
    LeBorgne, M. R., & Ghannoum, W. M. (2014). Calibrated analytical
    element for lateral-strength degradation of reinforced concrete
    columns. Engineering Structures, 81, 35-48.
    """
    return (5 / 6) * (Gc * Ag / L)


def get_shear_degrading_slope_shoraka_elwood2013(
    P: float | np.ndarray, Av: float | np.ndarray,
    fsyh: float | np.ndarray, dc: float | np.ndarray,
    sbh: float | np.ndarray, L: float | np.ndarray
) -> float | np.ndarray:
    """Computes the degrading slope of the shear-drift backbone of an RC
    column after shear failure with the expression of Shoraka and Elwood
    (2013), Eq. 20:

    ``k_deg = 4.5 P (4.6 Av fyt dc / (s P) + 1)^2 / L``

    The inputs may be scalars or arrays of the same shape, and the result
    has the same shape.

    Parameters
    ----------
    P : float | np.ndarray
        Axial force, positive in compression (kN). It must be positive.
    Av : float | np.ndarray
        Area of the transverse reinforcement within the spacing ``sbh``,
        parallel to the shear force (m2).
    fsyh : float | np.ndarray
        Yield strength of the transverse reinforcement (kPa).
    dc : float | np.ndarray
        Depth of the column core (m).
    sbh : float | np.ndarray
        Spacing of the transverse reinforcement (m).
    L : float | np.ndarray
        Clear length of the member (m).

    Returns
    -------
    float | np.ndarray
        Degrading slope of the shear-drift backbone, as a positive value
        (kN/m).

    References
    ----------
    Shoraka, M. B., & Elwood, K. J. (2013). Mechanical model for non ductile
    reinforced concrete columns. Journal of Earthquake Engineering, 17(7),
    937-957.
    """
    return (4.5 * P * (((Av * fsyh * dc) / (P * sbh)) * 4.6 + 1) ** 2) / L
