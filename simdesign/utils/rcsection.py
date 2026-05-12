"""This module provides various methods for reinforced concrete sections
such as moment-curvature analysis and confined concrete parameter calculations.
"""
# Imports from installed packages
import numpy as np
from typing import Tuple, Sequence, Callable, List, Dict
from scipy.optimize import root_scalar
from dataclasses import dataclass

from .units import MPa


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
    Fint : float
        Internal axial resultant. Positive sign is compression.
    Fc : float
        Concrete compressive resultant from the assumed stress block.
    Fs : np.ndarray
        Steel forces for each reinforcement layer.
    b1 : float
        Stress-block centroid factor (dimensionless) used to locate the
        concrete compressive resultant within the compression zone.
    """
    c: float
    Fint: float
    Fc: float
    Fs: np.ndarray
    b1: float


def get_moments(
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
    pflag : bool, optional
        Print/debug flag:
        - 0: no output
        - 1: print final moments
        - Use an int >= 2 to print iteration progress.

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
    phi_cr : float
        Yield curvature (rad/m).
    cy : float
        Neutral axis depth at first yield (m).

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

    def solve_c(
        section_state: Callable[[float], SectionState],
        label: str,
    ) -> Tuple[SectionState, float]:
        """
        Solve for neutral axis depth ``c`` using axial-force compatibility.

        Finds ``c`` such that:
            ``section_state(c).Pint - Pext = 0``

        The routine first searches for a sign change on a grid in (0, h),
        then uses Brent's method on the first bracket found. If no bracket is
        found, it falls back to the grid point with smallest residual.

        Parameters
        ----------
        section_state : Callable[[float], SectionState]
            Function returning section resultants for a given ``c``.
        label : str
            Label used in debug printing.

        Returns
        -------
        st : SectionState
            Section state at the selected/converged ``c``.
        c : float
            Neutral axis depth from top fiber.
        """
        def g(c: float) -> float:
            """Axial force residual: internal minus external.

            Parameters
            ----------
            c : float
                Neutral axis depth from top fiber.

            Returns
            -------
            float
                Axial force residual: internal minus external.
            """
            return section_state(c).Fint - Pext  # Axial force compatibility

        c_grid = np.linspace(1.0e-6, h - 1.0e-6, 120)
        g_vals = np.array([g(ci) for ci in c_grid], dtype=float)
        idx = np.where(np.sign(g_vals[:-1]) * np.sign(g_vals[1:]) <= 0.0)[0]

        if len(idx) == 0:
            j = int(np.argmin(np.abs(g_vals)))
            c = float(c_grid[j])
            st = section_state(c)
            if pflag:
                print(
                    f"[{label}] No root bracket found. Using least-residual "
                    f"c={st.c:.6g} m, Pint={st.Fint:.6g} kN, "
                    f"Pext={Pext:.6g} kN."
                )
            return st, c

        a = float(c_grid[idx[0]])
        bnd = float(c_grid[idx[0] + 1])
        sol = root_scalar(
            g,
            bracket=(a, bnd),
            method="brentq",
            xtol=1.0e-10,
            rtol=1.0e-10,
            maxiter=200,
        )
        c = float(sol.root)
        st = section_state(c)

        if pflag >= 2:
            print(f"[{label}] Converged: c={st.c:.6g} m, "
                  f"Pint={st.Fint:.6g} kN.")

        return st, c

    def get_my(st: SectionState) -> float:
        """
        Compute section moment about the centroid for a given SectionState.

        The concrete compressive resultant is assumed to act at the centroid of
        the equivalent stress block. Steel forces act at their layer locations.

        Parameters
        ----------
        st : SectionState
            Section state containing concrete and steel resultants.

        Returns
        -------
        M : float
            Bending moment about the section centroid.
        """
        ys = 0.5 * h - y
        M_steel = float((st.Fs * ys).sum())
        y_bar = st.c - 0.5 * st.b1 * st.c  # Eqn 5-8
        yc = 0.5 * h - (st.c - y_bar)  # lever arm
        M_conc = st.Fc * yc

        return M_conc + M_steel

    As = np.asarray(As_layers, dtype=float)
    y = np.asarray(y_layers, dtype=float)
    validate_inputs(hh=h, As=As, y=y)
    # Yield curvature in Priestley et al. 2007
    phi_y = 2.1 * fyL / (Es * h)  # Eqn 4.57b

    def state_yield(c: float) -> SectionState:
        """
        Build the section force state at first yield curvature for a given
        ``c``.

        Assumes a fixed curvature ``phi_y`` and enforces strain compatibility:
            ``eps_s = (c - y) * phi_y``

        Steel stresses are bilinear with perfect plasticity via clipping to
        ``[-fyL, fyL]``. Concrete compression is represented using the
        parabolic stress-strain relationship and resulting equivalent stress
        block parameters per Collins & Mitchell (1997).

        Parameters
        ----------
        c : float
            Neutral axis depth from the top fiber (m).

        Returns
        -------
        SectionState
            Internal force state (axial resultants and stress-block factor).
        """
        # Steel fiber strains & stresses from compatibility
        e_s = (c - y) * phi_y  # Reinforcing steel strains
        f_s = np.clip(e_s * Es, -fyL, fyL)  # Reinforcing steel stresses
        Fs = f_s * As  # Reinforcing steel forces

        # Stress block forces using the parabolic stress-strain
        # relationship in Collins & Mitchell 1997
        n_c = 0.8 + fc / (17.0 * MPa)  # Eqn 3-4
        e_c = (fc / Ec) * (n_c / (n_c - 1.0))  # Eqn 3-5
        e_top = c * phi_y  # Top concrete fiber strain
        r = e_top / e_c
        a1b1 = r - (r * r) / 3.0  # Eqn 5-7
        b1 = (4.0 - r) / (6.0 - 2.0 * r)  # Eqn 5-9
        Fc = a1b1 * c * fc * b

        Pint = Fc + float(Fs.sum())
        return SectionState(c=c, Fint=Pint, Fc=Fc, Fs=Fs, b1=b1)

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

    st_y, cy = solve_c(state_yield, label="yield")
    My = get_my(st_y)

    if pflag:
        print(f"Mcr: {Mcr:.6f} kNm, ccr: {ccr:.6f} m")
        print(f"My:  {My:.6f} kNm, cy:  {cy:.6f} m")

    return Mcr, phi_cr, ccr, My, phi_y, cy


def get_sum_wi_sq(
    rein_x: List[float],
    rein_y: List[float],
    rein_ds: List[float],
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

    Returns
    -------
    w_dash : list[float]
        Clear spacings along faces between adjacent perimeter bars.
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
            db_avg = 0.5 * float(d[a] + d[b])
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
        Concrete cover to centerline of transverse reinforcement.
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
        Concrete cover to centerline of transverse reinforcement.
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
    eps_50h = 0.75 * (h_ / s)**0.5
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
