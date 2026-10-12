"""This module provides the integer tag encoding used for the geometry
(points, lines and rectangles) and for the objects of the numerical models
(nodes, elements, materials and sections).

The tags are readable: the grid location and the role of an object can be
read directly from its tag. Each grid index (i, j, k) takes two digits, so
that grids with up to 99 bays in each direction and 99 storeys are supported.

- Points: ``tag = S * 10**6 + i * 10**4 + j * 10**2 + k`` with the level flag
  ``S`` equal to 0 for floor-level grid points and 1 for stair mid-level
  points, which take the grid indices of the point above them.
- Nodes derived from points:
  ``tag = E * 10**8 + T * 10**7 + point_tag``, where ``T`` is the node type
  (see ``NODE_TYPES``) and ``E`` is 1 for the element-end nodes next to the
  plastic hinges of concentrated plasticity models.
- Lines: ``tag = code * 10**6 + i * 10**4 + j * 10**2 + k`` (see
  ``LINE_CODES``), anchored at the minimum grid indices.
- Rectangles: ``tag = code * 10**6 + i * 10**4 + j * 10**2 + k`` (see
  ``RECTANGLE_CODES``), anchored at the minimum grid indices.
- Lines and rectangles with a stair mid-level point are anchored at the floor
  level below it, and take the stair codes ('Z_lower', 'Z_upper', 'X_stairs',
  'lower', 'upper'). The tags of points, lines and rectangles can be derived
  from their grid indices with :func:`point_tag_from_grid`,
  :func:`line_tag_from_grids` and :func:`rectangle_tag_from_grids`.
- Sub-objects (materials, sections, infill struts, ...):
  ``tag = owner_tag * 100 + local_id``.

All tags stay below the 32-bit integer limit of OpenSees.

Examples
--------
>>> encode_point_tag(3, 1, 2)
30102
>>> node_tag(30102, 'floor')
10030102
>>> decode_node_tag(10030102)
(0, 1, 0, 3, 1, 2)
"""
# Imports from installed packages
from math import ceil, floor
from typing import Literal, Sequence, Tuple

FACTOR = 100
"""Positional base per grid index (two digits per index)."""
MAX_INDEX = FACTOR - 1
"""Maximum grid index on any axis."""
LEVEL_UNIT = FACTOR**3
"""Unit of the level flag (S) of point tags, and of line/rectangle codes."""
TYPE_UNIT = 10 * LEVEL_UNIT
"""Unit of the node type digit (T)."""
END_UNIT = 10 * TYPE_UNIT
"""Unit of the element-end node flag (E)."""
SUB_FACTOR = 100
"""Multiplier of owner tags for sub-object tags."""
MAX_TAG = 2**31 - 1
"""Maximum tag value accepted by OpenSees (32-bit signed integer)."""

LINE_CODES = {
    'X': 1,  # beams along x
    'Y': 2,  # beams along y
    'Z': 3,  # columns
    'Z_lower': 4,  # lower part of a column split by a stair landing
    'Z_upper': 5,  # upper part of a column split by a stair landing
    'X_stairs': 6,  # stair landing beam along x (mid-storey)
}
"""Codes of line tags."""
RECTANGLE_CODES = {
    'XY': 1,  # slabs
    'YZ': 2,  # infills in YZ plane
    'XZ': 3,  # infills in XZ plane
    'lower': 4,  # lower part of an infill split by a stair landing
    'upper': 5,  # upper part of an infill split by a stair landing
}
"""Codes of rectangle tags."""
NODE_TYPES = {
    'center': 0,  # grid point, joint centre node
    'floor': 1,  # beam-side joint node constrained by the diaphragm
    'bottom': 2,  # joint offset nodes (rigid links) in CP03
    'right': 3,
    'front': 4,
    'left': 5,
    'rear': 6,
    'top': 7,
    'foundation': 8,  # foundation node
    'diaphragm': 9,  # retained (master) node of a floor diaphragm
}
"""Node type digits (T) of node tags."""


def _check_indices(i: int, j: int, k: int) -> None:
    """Check that the grid indices can be encoded."""
    for index in (i, j, k):
        if not (0 <= index <= MAX_INDEX) or int(index) != index:
            raise ValueError(
                f"Grid indices must be integers between 0 and {MAX_INDEX} "
                f"(at most {MAX_INDEX} bays and storeys); got ({i}, {j}, {k})."
            )


def _check_tag(tag: int) -> int:
    """Check that the tag can be used in OpenSees."""
    if not (0 <= tag <= MAX_TAG):
        raise ValueError(f"Tag {tag} exceeds the OpenSees limit {MAX_TAG}.")
    return int(tag)


def _encode_grid(i: int, j: int, k: int) -> int:
    """Encode grid indices with two digits per index."""
    _check_indices(i, j, k)
    return int(i) * FACTOR**2 + int(j) * FACTOR + int(k)


def _decode_grid(tag: int) -> Tuple[int, int, int]:
    """Decode the grid indices (last six digits) of a tag."""
    grid = tag % LEVEL_UNIT
    return grid // FACTOR**2, (grid % FACTOR**2) // FACTOR, grid % FACTOR


def encode_point_tag(i: int, j: int, k: int) -> int:
    """Encode the grid indices of a floor-level point into a tag.

    Parameters
    ----------
    i, j, k : int
        Grid indices along x, y, z (0-based, at most ``MAX_INDEX``).

    Returns
    -------
    int
        Point tag, ``i * 10**4 + j * 10**2 + k``.
    """
    return _check_tag(_encode_grid(i, j, k))


def decode_point_tag(tag: int) -> Tuple[int, int, int]:
    """Decode a point tag back into grid indices.

    Parameters
    ----------
    tag : int
        Point tag.

    Returns
    -------
    Tuple[int, int, int]
        Grid indices ``(i, j, k)``. For stair mid-level points, these are the
        indices of the point above.
    """
    return _decode_grid(tag)


def stairs_point_tag(top_point_tag: int) -> int:
    """Tag of the stair mid-level point below a floor-level point.

    Parameters
    ----------
    top_point_tag : int
        Tag of the floor-level point above the mid-level point.

    Returns
    -------
    int
        Point tag with the level flag ``S = 1``.
    """
    return _check_tag(LEVEL_UNIT + top_point_tag % LEVEL_UNIT)


def encode_line_tag(i: int, j: int, k: int, line_type: str) -> int:
    """Encode the anchor grid indices and the type of a line into a tag.

    Parameters
    ----------
    i, j, k : int
        Anchor grid indices of the line (minimum indices along each axis).
    line_type : str
        Key of ``LINE_CODES``, e.g. 'X', 'Y', 'Z'.

    Returns
    -------
    int
        Line tag, ``code * 10**6 + i * 10**4 + j * 10**2 + k``.
    """
    return _check_tag(LINE_CODES[line_type] * LEVEL_UNIT
                      + _encode_grid(i, j, k))


def decode_line_tag(tag: int) -> Tuple[int, int, int, str]:
    """Decode a line tag back into anchor grid indices and type.

    Parameters
    ----------
    tag : int
        Line tag.

    Returns
    -------
    Tuple[int, int, int, str]
        ``(i, j, k, line_type)``; ``line_type`` is '?' if unknown.
    """
    types = {code: key for key, code in LINE_CODES.items()}
    return (*_decode_grid(tag), types.get(tag // LEVEL_UNIT, '?'))


def encode_rectangle_tag(i: int, j: int, k: int, plane: str) -> int:
    """Encode the anchor grid indices and the type of a rectangle into a tag.

    Parameters
    ----------
    i, j, k : int
        Anchor grid indices of the rectangle (lower/near corner).
    plane : str
        Key of ``RECTANGLE_CODES``, e.g. 'XY', 'YZ', 'XZ'.

    Returns
    -------
    int
        Rectangle tag, ``code * 10**6 + i * 10**4 + j * 10**2 + k``.
    """
    return _check_tag(RECTANGLE_CODES[plane] * LEVEL_UNIT
                      + _encode_grid(i, j, k))


def decode_rectangle_tag(tag: int) -> Tuple[int, int, int, str]:
    """Decode a rectangle tag back into anchor grid indices and type.

    Parameters
    ----------
    tag : int
        Rectangle tag.

    Returns
    -------
    Tuple[int, int, int, str]
        ``(i, j, k, plane)``; ``plane`` is '?' if unknown.
    """
    planes = {code: key for key, code in RECTANGLE_CODES.items()}
    return (*_decode_grid(tag), planes.get(tag // LEVEL_UNIT, '?'))


def _is_mid_level(k: float) -> bool:
    """Check if a z grid index is at a stair mid-level (ends with .5)."""
    return k % 1 != 0


def point_tag_from_grid(grid_ids: Sequence[float]) -> int:
    """Tag of a point from its grid indices.

    Parameters
    ----------
    grid_ids : Sequence[float]
        Grid indices ``(i, j, k)`` of the point. Stair mid-level points have
        ``k`` ending with .5.

    Returns
    -------
    int
        Point tag. Stair mid-level points take the level flag ``S = 1`` and
        the grid indices of the point above them.
    """
    i, j, k = grid_ids
    if _is_mid_level(k):
        return stairs_point_tag(encode_point_tag(int(i), int(j), ceil(k)))
    return encode_point_tag(int(i), int(j), int(k))


def line_tag_from_grids(grids: Sequence[Sequence[float]]) -> int:
    """Tag of a line from the grid indices of its end points.

    Parameters
    ----------
    grids : Sequence[Sequence[float]]
        Grid indices ``(i, j, k)`` of the two end points.

    Returns
    -------
    int
        Line tag anchored at the minimum grid indices, rounded down. Columns
        split by a stair landing take the 'Z_lower' and 'Z_upper' codes, and
        beams at a stair mid-level take the 'X_stairs' code.

    Raises
    ------
    ValueError
        If the line is not parallel to the X, Y or Z axis, or if a beam at a
        stair mid-level is not parallel to the X axis.
    """
    grid1, grid2 = grids
    axes = [n for n in range(3) if grid1[n] != grid2[n]]
    if len(axes) != 1:
        raise ValueError(
            f"The line between grid points {list(grid1)} and {list(grid2)} "
            "is not parallel to the X, Y or Z axis.")
    i, j, k = (floor(min(a, b)) for a, b in zip(grid1, grid2))
    line_type = 'XYZ'[axes[0]]
    if line_type == 'Z':
        top = grid1 if grid1[2] > grid2[2] else grid2
        bottom = grid2 if top is grid1 else grid1
        if _is_mid_level(top[2]):
            line_type = 'Z_lower'
        elif _is_mid_level(bottom[2]):
            line_type = 'Z_upper'
    elif _is_mid_level(grid1[2]):
        if line_type != 'X':
            raise ValueError(
                "Beams at a stair mid-level must be parallel to the X axis.")
        line_type = 'X_stairs'
    return encode_line_tag(i, j, k, line_type)


def rectangle_tag_from_grids(grids: Sequence[Sequence[float]]) -> int:
    """Tag of a rectangle from the grid indices of its corner points.

    Parameters
    ----------
    grids : Sequence[Sequence[float]]
        Grid indices ``(i, j, k)`` of the four corner points.

    Returns
    -------
    int
        Rectangle tag anchored at the minimum grid indices, rounded down.
        Infills split by a stair landing take the 'lower' and 'upper' codes.

    Raises
    ------
    ValueError
        If the rectangle is not parallel to the XY, XZ or YZ plane, or if a
        slab (XY) is at a stair mid-level.
    """
    axes = [n for n in range(3) if len({grid[n] for grid in grids}) == 1]
    if len(axes) != 1:
        raise ValueError(
            f"The rectangle with grid points {[list(g) for g in grids]} is "
            "not parallel to the XY, XZ or YZ plane.")
    i, j, k = (floor(min(grid[n] for grid in grids)) for n in range(3))
    plane = {0: 'YZ', 1: 'XZ', 2: 'XY'}[axes[0]]
    levels = [grid[2] for grid in grids]
    if any(_is_mid_level(level) for level in levels):
        if plane == 'XY':
            raise ValueError("Slabs cannot be at a stair mid-level.")
        plane = 'upper' if _is_mid_level(min(levels)) else 'lower'
    return encode_rectangle_tag(i, j, k, plane)


def node_tag(point_tag: int, node_type: Literal[
        'center', 'floor', 'bottom', 'right', 'front', 'left', 'rear', 'top',
        'foundation']) -> int:
    """Tag of a node associated with a geometry point.

    Parameters
    ----------
    point_tag : int
        Tag of the geometry point (floor-level or stair mid-level).
    node_type : str
        Key of ``NODE_TYPES``.

    Returns
    -------
    int
        Node tag, ``T * 10**7 + point_tag``.
    """
    if not (0 <= point_tag < TYPE_UNIT):
        raise ValueError(f"Point tag {point_tag} must be below {TYPE_UNIT}.")
    return _check_tag(NODE_TYPES[node_type] * TYPE_UNIT + point_tag)


def element_end_node_tag(tag: int) -> int:
    """Tag of the element-end node next to a plastic hinge.

    Parameters
    ----------
    tag : int
        Tag of the node on the other side of the hinge (joint offset or
        foundation node).

    Returns
    -------
    int
        Node tag with the element-end flag ``E = 1``.
    """
    if not (0 <= tag < END_UNIT):
        raise ValueError(f"Node tag {tag} must be below {END_UNIT}.")
    return _check_tag(END_UNIT + tag)


def diaphragm_node_tag(floor: int) -> int:
    """Tag of the retained (master) node of a floor diaphragm.

    Parameters
    ----------
    floor : int
        Floor number (1-based).

    Returns
    -------
    int
        Node tag with type ``T = 9`` and ``k = floor``.
    """
    return _check_tag(NODE_TYPES['diaphragm'] * TYPE_UNIT
                      + _encode_grid(0, 0, floor))


def decode_node_tag(tag: int) -> Tuple[int, int, int, int, int, int]:
    """Decode a node tag.

    Parameters
    ----------
    tag : int
        Node tag.

    Returns
    -------
    Tuple[int, int, int, int, int, int]
        ``(E, T, S, i, j, k)``: element-end flag, node type (see
        ``NODE_TYPES``), level flag and grid indices.
    """
    end = tag // END_UNIT
    node_type = (tag % END_UNIT) // TYPE_UNIT
    level = (tag % TYPE_UNIT) // LEVEL_UNIT
    return (end, node_type, level, *_decode_grid(tag))


def sub_tag(owner_tag: int, local_id: int) -> int:
    """Tag of a sub-object (material, section, strut, ...) of an owner.

    Parameters
    ----------
    owner_tag : int
        Tag of the owner object (e.g. line, rectangle or node tag).
    local_id : int
        Local identifier of the sub-object (0-99).

    Returns
    -------
    int
        Tag, ``owner_tag * 100 + local_id``.
    """
    if not (0 <= local_id < SUB_FACTOR):
        raise ValueError(f"Local id {local_id} must be below {SUB_FACTOR}.")
    return _check_tag(owner_tag * SUB_FACTOR + local_id)
