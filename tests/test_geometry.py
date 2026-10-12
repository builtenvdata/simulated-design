"""Tests for the tag encoding and the geometry classes."""
import sys
from pathlib import Path
import pandas as pd
import pytest

# Add the project root to sys.path
sys.path.append(str(Path(__file__).parents[1]))

from simdesign.rcmrf import StandardGeometry, CustomGeometry  # noqa
from simdesign.utils import tags  # noqa


# ---------------------------------------------------------------------------
# Tag encoding
# ---------------------------------------------------------------------------
@pytest.mark.parametrize('i, j, k', [(0, 0, 0), (3, 1, 2), (99, 99, 99)])
def test_point_tag_round_trip(i, j, k):
    """Point tags decode to their grid indices."""
    tag = tags.encode_point_tag(i, j, k)
    assert tags.decode_point_tag(tag) == (i, j, k)


@pytest.mark.parametrize('line_type', list(tags.LINE_CODES))
def test_line_tag_round_trip(line_type):
    """Line tags decode to their grid indices and line type."""
    tag = tags.encode_line_tag(2, 3, 1, line_type)
    assert tags.decode_line_tag(tag) == (2, 3, 1, line_type)


@pytest.mark.parametrize('plane', list(tags.RECTANGLE_CODES))
def test_rectangle_tag_round_trip(plane):
    """Rectangle tags decode to their grid indices and plane."""
    tag = tags.encode_rectangle_tag(1, 0, 2, plane)
    assert tags.decode_rectangle_tag(tag) == (1, 0, 2, plane)


def test_node_tags():
    """Node tags carry the node type and the element-end flag."""
    point = tags.encode_point_tag(3, 1, 2)
    node = tags.node_tag(point, 'floor')
    assert node == 10030102  # documented example
    assert tags.decode_node_tag(node) == (0, 1, 0, 3, 1, 2)
    end = tags.element_end_node_tag(node)
    assert tags.decode_node_tag(end)[0] == 1
    assert tags.diaphragm_node_tag(2) != tags.diaphragm_node_tag(3)


def test_stairs_point_tags():
    """Stair mid-level points take the indices of the point above them and
    differ from every floor-level point tag."""
    top = tags.encode_point_tag(1, 0, 2)
    mid = tags.stairs_point_tag(top)
    assert mid != top
    assert tags.point_tag_from_grid((1, 0, 1.5)) == mid
    assert tags.point_tag_from_grid((1, 0, 2)) == top


def test_tags_from_grids():
    """Line and rectangle tags follow from the grid indices of their
    points, whatever the point order."""
    column = tags.line_tag_from_grids([(1, 2, 0), (1, 2, 1)])
    assert column == tags.line_tag_from_grids([(1, 2, 1), (1, 2, 0)])
    assert tags.decode_line_tag(column) == (1, 2, 0, 'Z')
    slab = tags.rectangle_tag_from_grids(
        [(0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)])
    assert tags.decode_rectangle_tag(slab)[3] == 'XY'


@pytest.mark.parametrize('i, j, k', [(100, 0, 0), (0, -1, 0)])
def test_invalid_grid_indices_raise(i, j, k):
    """Grid indices must be within 0-99."""
    with pytest.raises(ValueError):
        tags.encode_point_tag(i, j, k)


def test_sub_tags_are_unique():
    """Sub-object tags of one owner differ from each other."""
    owner = tags.encode_line_tag(1, 1, 1, 'Z')
    assert len({tags.sub_tag(owner, i) for i in range(1, 99)}) == 98


# ---------------------------------------------------------------------------
# Standard geometry with stairs
# ---------------------------------------------------------------------------
def make_frame(stair_bays, num_bays=3, num_storeys=2, infills=True):
    """Frame with continuous staircases at the given (x, y) bay indices."""
    frame = StandardGeometry(num_storeys, 3.0, num_bays, 4.0, num_bays, 4.0)
    for bay in stair_bays:
        frame.set_continuous_stairs_rectangles(bay, 4.0, 4.0)
    if infills:
        frame.add_infills(exterior=True, interior=False, ext_type='Weak',
                          int_type='Weak')
    frame.add_new_elements_for_stairs(infills=infills)
    return frame


def all_tags_unique(frame) -> bool:
    """True if points, lines and rectangles have unique tags."""
    return all(len({o.tag for o in objs}) == len(objs)
               for objs in (frame.points, frame.lines, frame.rectangles))


@pytest.mark.parametrize('stair_bays', [
    [(0, 0)],                          # single stair bay
    [(0, 0), (1, 0)],                  # adjacent along x
    [(0, 0), (0, 1)],                  # adjacent along y
    [(0, 0), (1, 0), (0, 1), (1, 1)],  # 2x2 stair bays
])
def test_stair_layouts(stair_bays):
    """Stair layouts build with unique tags; stair bays adjacent along x
    share their mid-storey points."""
    frame = make_frame(stair_bays)
    assert all_tags_unique(frame)
    mid_points = frame.points_at_mid_floor_levels
    assert len(mid_points) > 0
    assert len({p.tag for p in mid_points}) == len(mid_points)


def test_adjacent_stair_bays_along_x_share_points():
    """Two stair bays adjacent along x have fewer mid-storey points than
    two separate stair bays."""
    adjacent = make_frame([(0, 0), (1, 0)], infills=False)
    separate = make_frame([(0, 0), (2, 0)], infills=False)
    assert (len(adjacent.points_at_mid_floor_levels)
            < len(separate.points_at_mid_floor_levels))


def test_retag_keeps_grid_based_tags():
    """retag() gives every object the tag of its grid location."""
    frame = make_frame([(0, 0)])
    mapping = frame.retag()
    assert set(mapping) == {'points', 'lines', 'rectangles'}
    assert all_tags_unique(frame)
    for point in frame.points:
        assert point.tag == tags.point_tag_from_grid(point.grid_ids)


# ---------------------------------------------------------------------------
# Custom geometry
# ---------------------------------------------------------------------------
@pytest.fixture
def frame_workbook(tmp_path):
    """Workbook written from a standard frame."""
    frame = make_frame([(0, 0)], infills=False)
    path = tmp_path / 'frame.xlsx'
    frame.write_mesh_to_xlsx(path=path)
    return frame, path


@pytest.mark.parametrize('retag', [False, True])
def test_custom_geometry_round_trip(frame_workbook, retag):
    """A workbook written from a frame reads back with the same objects."""
    frame, path = frame_workbook
    custom = CustomGeometry(path, retag=retag)
    assert len(custom.points) == len(frame.points)
    assert len(custom.lines) == len(frame.lines)
    assert len(custom.rectangles) == len(frame.rectangles)
    assert all_tags_unique(custom)


def test_custom_geometry_rejects_duplicate_tags(frame_workbook, tmp_path):
    """Duplicate point tags in the workbook raise an error."""
    _, path = frame_workbook
    sheets = pd.read_excel(path, sheet_name=None)
    name = StandardGeometry.POINTS_SHEET
    points = sheets[name]
    points.loc[1, 'tag'] = points.loc[0, 'tag']
    bad = tmp_path / 'duplicate.xlsx'
    with pd.ExcelWriter(bad) as writer:
        for sheet, df in sheets.items():
            (points if sheet == name else df).to_excel(
                writer, sheet_name=sheet, index=False)
    with pytest.raises(ValueError):
        CustomGeometry(bad)


def test_example_custom_geometry():
    """The example workbook of the repository reads without errors."""
    path = Path(__file__).parents[1] / 'data' / 'example-custom-geometry.xlsx'
    if not path.exists():
        pytest.skip('example workbook not available')
    custom = CustomGeometry(path)
    assert len(custom.points) > 0 and len(custom.lines) > 0
