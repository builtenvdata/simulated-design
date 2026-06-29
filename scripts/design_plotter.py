import pyvista as pv
import numpy as np
import pandas as pd
from pathlib import Path


def find_overlapping_stairs(df_stairs, df_nodes):
    """
    Find rectangles that share the same x,y footprint but have different z
    coordinates.
    Returns a dict mapping (x,y) footprint tuples to lists of stair indices.
    """
    # Store each rectangle's x,y footprint (ignoring z)
    footprints = {}

    for index, row in df_stairs.iterrows():
        # Get x,y coords for all 4 nodes (ignore z)
        node_cols = ["node_1", "node_2", "node_3", "node_4"]
        xy_coords = []

        for node_col in node_cols:
            node_id = row[node_col]
            x = round(
                df_nodes.loc[node_id, "x-coord [m]"], 4
            )  # round to avoid float issues
            y = round(df_nodes.loc[node_id, "y-coord [m]"], 4)
            xy_coords.append((x, y))

        # Sort the xy coords so order doesn't matter for comparison
        footprint_key = tuple(sorted(xy_coords))

        if footprint_key not in footprints:
            footprints[footprint_key] = []
        footprints[footprint_key].append(index)

    # Filter to only footprints with more than one rectangle (overlapping)
    overlapping = [v for _, v in footprints.items() if len(v) > 1]

    return overlapping


def get_coords(df_nodes, row, node_col):
    return df_nodes.loc[
        row[node_col], ["x-coord [m]", "y-coord [m]", "z-coord [m]"]
    ].to_numpy(dtype=float)


def create_staircase(df_stairs, df_nodes):

    staircase_idxs = find_overlapping_stairs(df_stairs, df_nodes)

    stair_meshes = pv.MultiBlock()

    for staircase in staircase_idxs:
        for i in range(len(staircase) - 1):
            idx_lower = staircase[i]
            idx_upper = staircase[i + 1]
            stairs_lower = df_stairs.loc[idx_lower]
            stairs_upper = df_stairs.loc[idx_upper]

            lx = stairs_upper["lx [mm]"] / 1000
            t = stairs_upper["t [mm]"] / 1000
            width = 0.6  # Landing slab width

            p1_l = get_coords(df_nodes, stairs_lower, "node_2")
            p2_l = get_coords(df_nodes, stairs_lower, "node_1")
            p3_l = get_coords(df_nodes, stairs_lower, "node_4")
            p4_l = get_coords(df_nodes, stairs_lower, "node_3")
            p2_u = get_coords(df_nodes, stairs_upper, "node_2")
            p3_u = get_coords(df_nodes, stairs_upper, "node_3")

            # Mid-z for the transition between lower and upper slab
            zmid = (p1_l[2] + p2_u[2]) / 2

            # Lower inclined panel: p1_l, p4_l at bottom;
            # raised mid-points at top
            p2_l[2] = zmid
            p3_l[2] = zmid
            p2_l[1] = p2_l[1] + width
            p3_l[1] = p3_l[1] + width
            p3_l[0] = p3_l[0] - lx / 2
            p4_l[0] = p4_l[0] - lx / 2
            # p3_l[1] = p3_l[1] - width
            # p4_l[1] = p4_l[1] - width

            # Upper inclined panel: mid-points at bottom; p2_u, p3_u at top
            p1_u = p3_l.copy()
            p4_u = p3_l.copy()
            p4_u[0] = p4_u[0] + lx / 2
            p2_u[0] = p2_u[0] + lx / 2
            # p4_u[1] = p4_u[1] + width
            # p2_u[1] = p2_u[1] + width
            # Lower inclined slab:  p0=p1_l, p1=p2_l, p2=p3_l, p3=p4_l
            # (CW from above)
            stair_meshes.append(create_slab(p1_l, p2_l, p3_l, p4_l, t))

            # Upper inclined slab:  p0=p1_u, p1=p2_u, p2=p3_u, p3=p4_u
            # (CW from above)
            stair_meshes.append(create_slab(p1_u, p2_u, p3_u, p4_u, t))

            # --- Mid-level landing ---
            # (flat slab connecting the two inclined panels)
            p1_m = get_coords(df_nodes, stairs_lower, "node_1")
            p1_m[2] = zmid
            p4_m = get_coords(df_nodes, stairs_lower, "node_4")
            p4_m[2] = zmid
            p2_m = p1_m.copy()
            p2_m[1] = p2_m[1] + width
            p3_m = p4_m.copy()
            p3_m[1] = p3_m[1] + width
            stair_meshes.append(create_slab(p1_m, p2_m, p3_m, p4_m, t))

            # --- Ground floor landing (flat slab, only for the first step) ---
            if i == 0:
                lx = stairs_lower["lx [mm]"] / 1000
                t = stairs_lower["t [mm]"] / 1000
                p1_gf_l = get_coords(df_nodes, stairs_lower, "node_2")
                p2_gf_l = get_coords(df_nodes, stairs_lower, "node_1")
                p3_gf_l = get_coords(df_nodes, stairs_lower, "node_4")
                p4_gf_l = get_coords(df_nodes, stairs_lower, "node_3")
                p2_gf_u = get_coords(df_nodes, stairs_lower, "node_2")
                p3_gf_u = get_coords(df_nodes, stairs_lower, "node_3")
                p1_gf_l[2], p2_gf_l[2], p3_gf_l[2], p4_gf_l[2] = (
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                )
                # Mid-z for the transition between lower and upper slab
                zmid = (p1_gf_l[2] + p2_gf_u[2]) / 2

                # Lower inclined panel: p1_l, p4_l at bottom;
                # raised mid-points at top
                p2_gf_l[2] = zmid
                p3_gf_l[2] = zmid
                p2_gf_l[1] = p2_gf_l[1] + width
                p3_gf_l[1] = p3_gf_l[1] + width
                p3_gf_l[0] = p3_gf_l[0] - lx / 2
                p4_gf_l[0] = p4_gf_l[0] - lx / 2

                # Upper inclined panel: mid-points at bottom; p2_u, p3_u at top
                p1_gf_u = p3_gf_l.copy()
                p4_gf_u = p3_gf_l.copy()
                p4_gf_u[0] = p4_gf_u[0] + lx / 2
                p2_gf_u[0] = p2_gf_u[0] + lx / 2
                # Lower inclined slab:  p0=p1_l, p1=p2_l, p2=p3_l, p3=p4_l
                # (CW from above)
                stair_meshes.append(
                    create_slab(p1_gf_l, p2_gf_l, p3_gf_l, p4_gf_l, t)
                )

                # Upper inclined slab:  p0=p1_u, p1=p2_u, p2=p3_u, p3=p4_u
                # (CW from above)
                stair_meshes.append(
                    create_slab(p1_gf_u, p2_gf_u, p3_gf_u, p4_gf_u, t)
                )

                # --- Mid-level landing ---
                # (flat slab connecting the two inclined panels)
                p1_m = get_coords(df_nodes, stairs_lower, "node_1")
                p1_m[2] = zmid
                p4_m = get_coords(df_nodes, stairs_lower, "node_4")
                p4_m[2] = zmid
                p2_m = p1_m.copy()
                p2_m[1] = p2_m[1] + width
                p3_m = p4_m.copy()
                p3_m[1] = p3_m[1] + width
                stair_meshes.append(create_slab(p1_m, p2_m, p3_m, p4_m, t))

    return stair_meshes


def create_beam(
    p0: np.ndarray,
    p1: np.ndarray,
    width: float,
    depth: float,
    up: np.ndarray = None,
) -> pv.PolyData:
    """
    Create a rectangular beam (box) between two points p0 and p1.

    Builds a full right-hand local coordinate frame so that:
      - Local X  : along element axis (p0 → p1)
      - Local Z  : as close to `up` as possible (default: world Z = [0,0,1])
      - Local Y  : completes the frame (cross(local_z, local_x))

    This ensures `depth` is always the vertical (strong-axis) dimension
    and `width` is the horizontal (weak-axis) dimension, regardless of
    element orientation.

    Parameters
    ----------
    p0, p1 : array-like, shape (3,)
        Start and end points of the element in world coordinates.
    width : float
        Cross-section dimension along local Y (weak axis / horizontal).
    depth : float
        Cross-section dimension along local Z (strong axis / vertical).
    up : array-like, shape (3,), optional
        Reference "up" vector. Defaults to world Z [0, 0, 1].
        For nearly-vertical elements (columns), automatically falls back
        to world X [1, 0, 0] to avoid a degenerate frame.

    Returns
    -------
    pv.PolyData
        Transformed box mesh in world coordinates.

    Raises
    ------
    ValueError
        If p0 == p1 (zero-length element).
    """
    p0 = np.asarray(p0, dtype=float)
    p1 = np.asarray(p1, dtype=float)

    # --- Element axis (local X) -------------------------------------------
    vec = p1 - p0
    length = np.linalg.norm(vec)
    if length < 1e-12:
        raise ValueError(f"Zero-length element: p0={p0}, p1={p1}")
    local_x = vec / length

    # --- Reference "up" vector, with automatic fallback for vertical members -
    if up is None:
        up = np.array([0.0, 0.0, 1.0])
    else:
        up = np.asarray(up, dtype=float)
        up = up / np.linalg.norm(up)

    # If element is nearly parallel to `up`, fall back to world X
    if abs(np.dot(local_x, up)) > 1.0 - 1e-6:
        up = np.array([1.0, 0.0, 0.0])

    # --- Build orthonormal frame via Gram-Schmidt --------------------------
    # local_z: project `up` onto the plane perpendicular to local_x
    local_z = up - np.dot(up, local_x) * local_x
    local_z /= np.linalg.norm(local_z)

    # local_y: right-hand rule completes the frame
    local_y = np.cross(local_z, local_x)
    local_y /= np.linalg.norm(local_y)

    # --- Build 4x4 rotation matrix (local → world) ------------------------
    # Columns are the local axes expressed in world coordinates
    rotation = np.eye(4)
    rotation[:3, 0] = local_x  # box X → element axis
    rotation[:3, 1] = local_y  # box Y → weak axis (width)
    rotation[:3, 2] = local_z  # box Z → strong axis (depth)

    # --- Create box at origin, apply rotation, then translate to midpoint --
    midpoint = 0.5 * (p0 + p1)

    box = pv.Box(
        bounds=(
            -length / 2,
            length / 2,  # X: along element
            -width / 2,
            width / 2,  # Y: weak axis
            -depth / 2,
            depth / 2,  # Z: strong axis
        )
    )

    box.transform(rotation, inplace=True)
    box.translate(midpoint, inplace=True)

    return box


def create_column(
    p0: np.ndarray,
    p1: np.ndarray,
    bx: float,  # dimension along global X
    by: float,  # dimension along global Y
) -> pv.PolyData:
    """
    Create a column box aligned with global X and Y axes.
    p0/p1 are assumed to differ only in Z (vertical element).
    """
    p0 = np.asarray(p0, dtype=float)
    p1 = np.asarray(p1, dtype=float)

    z0, z1 = sorted([p0[2], p1[2]])
    cx = 0.5 * (p0[0] + p1[0])
    cy = 0.5 * (p0[1] + p1[1])

    return pv.Box(
        bounds=(
            cx - bx / 2,
            cx + bx / 2,  # global X
            cy - by / 2,
            cy + by / 2,  # global Y
            z0,
            z1,  # global Z (full height, no centering needed)
        )
    )


def create_slab(
    p0: np.ndarray,
    p1: np.ndarray,
    p2: np.ndarray,
    p3: np.ndarray,
    thickness: float,
) -> pv.PolyData:
    """
    Create a rectangular slab from 4 corner nodes + thickness.

    Nodes should be ordered CW when viewed from above:

        p1 ------- p2
        |           |
        p0 ------- p3

    The slab normal (local Z) is derived from the cross product of the
    two edge directions, so orientation is fully determined by the nodes.
    Thickness is extruded along that normal.

    Parameters
    ----------
    p0, p1, p2, p3 : array-like (3,)
        Four corner nodes in CW order from above.
    thickness : float
        Slab thickness extruded along the normal direction.

    Returns
    -------
    pv.PolyData
        Transformed box mesh in world coordinates.

    Raises
    ------
    ValueError
        If nodes are collinear or the quad is degenerate.
    """
    p0 = np.asarray(p0, dtype=float)
    p1 = np.asarray(p1, dtype=float)
    p2 = np.asarray(p2, dtype=float)
    p3 = np.asarray(p3, dtype=float)

    # --- Edge vectors from p0 -----------------------------------------------
    edge_x = (
        p3 - p0
    )  # first edge  → defines local X and length  (p0 → p3, rightward)
    edge_y = (
        p1 - p0
    )  # second edge → defines local Y and width   (p0 → p1, upward)

    length = np.linalg.norm(edge_x)
    width = np.linalg.norm(edge_y)

    if length < 1e-12:
        raise ValueError(f"Degenerate slab: p0 == p3, {p0}")
    if width < 1e-12:
        raise ValueError(f"Degenerate slab: p0 == p1, {p0}")

    # --- Orthonormal frame --------------------------------------------------
    local_x = edge_x / length
    local_y = edge_y / width

    local_z = np.cross(local_x, local_y)
    norm_z = np.linalg.norm(local_z)
    if norm_z < 1e-12:
        raise ValueError(
            "Degenerate slab: edges are parallel (collinear nodes)."
        )
    local_z /= norm_z

    # Re-orthogonalize local_y in case edges aren't perfectly perpendicular
    local_y = np.cross(local_z, local_x)
    local_y /= np.linalg.norm(local_y)

    # --- Rotation matrix (local → world) ------------------------------------
    rotation = np.eye(4)
    rotation[:3, 0] = local_x
    rotation[:3, 1] = local_y
    rotation[:3, 2] = local_z

    # --- Box centered at slab centroid --------------------------------------
    centroid = 0.25 * (p0 + p1 + p2 + p3)

    box = pv.Box(
        bounds=(
            -length / 2,
            length / 2,
            -width / 2,
            width / 2,
            -thickness / 2,
            thickness / 2,
        )
    )

    box.transform(rotation, inplace=True)
    box.translate(centroid, inplace=True)

    return box


if __name__ == "__main__":
    infills_flag = False

    design_dir = Path.cwd() / "tmp" / "specific-frame" / "design"
    beams_path = design_dir / "beams.csv"
    columns_path = design_dir / "columns.csv"
    slabs_path = design_dir / "slabs.csv"
    stairs_path = design_dir / "stairs.csv"
    infills_path = design_dir / "infills.csv"
    joints_path = design_dir / "joints.csv"

    beams = pd.read_csv(beams_path)
    columns = pd.read_csv(columns_path)
    slabs = pd.read_csv(slabs_path)
    stairs = pd.read_csv(stairs_path)
    infills = pd.read_csv(infills_path)
    joints = pd.read_csv(joints_path)
    df_nodes = joints.set_index("id")

    plotter = pv.Plotter()

    beam_meshes = pv.MultiBlock()
    for index, row in beams.iterrows():
        nI = row["node_i"]
        nJ = row["node_j"]
        b = row["b [mm]"] / 1000
        h = row["h [mm]"] / 1000
        coordsI = df_nodes.loc[
            nI, ["x-coord [m]", "y-coord [m]", "z-coord [m]"]
        ].to_numpy()
        coordsJ = df_nodes.loc[
            nJ, ["x-coord [m]", "y-coord [m]", "z-coord [m]"]
        ].to_numpy()
        beam_meshes.append(create_beam(coordsI, coordsJ, b, h))
    plotter.add_mesh(beam_meshes.combine(), color="red")

    column_meshes = pv.MultiBlock()
    for index, row in columns.iterrows():
        nI = row["node_i"]
        nJ = row["node_j"]
        bx = row["bx [mm]"] / 1000
        by = row["by [mm]"] / 1000
        coordsI = df_nodes.loc[
            nI, ["x-coord [m]", "y-coord [m]", "z-coord [m]"]
        ].to_numpy()
        coordsJ = df_nodes.loc[
            nJ, ["x-coord [m]", "y-coord [m]", "z-coord [m]"]
        ].to_numpy()
        column_meshes.append(create_column(coordsI, coordsJ, bx, by))
    plotter.add_mesh(column_meshes.combine(), color="blue")

    slab_meshes = pv.MultiBlock()
    for index, row in slabs.iterrows():
        nI = row["node_1"]
        nJ = row["node_2"]
        nK = row["node_3"]
        nL = row["node_4"]
        t = row["t [mm]"] / 1000
        coordsI = df_nodes.loc[
            nI, ["x-coord [m]", "y-coord [m]", "z-coord [m]"]
        ].to_numpy()
        coordsJ = df_nodes.loc[
            nJ, ["x-coord [m]", "y-coord [m]", "z-coord [m]"]
        ].to_numpy()
        coordsK = df_nodes.loc[
            nK, ["x-coord [m]", "y-coord [m]", "z-coord [m]"]
        ].to_numpy()
        coordsL = df_nodes.loc[
            nL, ["x-coord [m]", "y-coord [m]", "z-coord [m]"]
        ].to_numpy()
        slab_meshes.append(create_slab(coordsI, coordsJ, coordsK, coordsL, t))
    plotter.add_mesh(slab_meshes.combine(), color="lightgray", opacity=0.6)

    if all(stairs.any()):
        stair_meshes = create_staircase(stairs, df_nodes)
        plotter.add_mesh(stair_meshes.combine(), color="green")

    if infills_flag:
        infill_meshes = pv.MultiBlock()
        for index, row in infills.iterrows():
            nI = row["node_1"]
            nJ = row["node_2"]
            nK = row["node_3"]
            nL = row["node_4"]
            t = row["tw [mm]"] / 1000
            coordsI = df_nodes.loc[
                nI, ["x-coord [m]", "y-coord [m]", "z-coord [m]"]
            ].to_numpy()
            coordsJ = df_nodes.loc[
                nJ, ["x-coord [m]", "y-coord [m]", "z-coord [m]"]
            ].to_numpy()
            coordsK = df_nodes.loc[
                nK, ["x-coord [m]", "y-coord [m]", "z-coord [m]"]
            ].to_numpy()
            coordsL = df_nodes.loc[
                nL, ["x-coord [m]", "y-coord [m]", "z-coord [m]"]
            ].to_numpy()
            infill_meshes.append(
                create_slab(coordsI, coordsJ, coordsK, coordsL, t)
            )
        plotter.add_mesh(
            infill_meshes.combine(), color="sandybrown", opacity=0.6
        )

    plotter.export_html(design_dir.parent / "specific-design.html")
    plotter.show()
