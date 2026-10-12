"""Tests for geometry editing, the mesh shapes, the modal analysis fallbacks
and the plots (skipped where off-screen rendering is not available)."""
import os
import subprocess
import sys
from pathlib import Path
import numpy as np
import pytest

# Add the project root to sys.path
sys.path.append(str(Path(__file__).parents[1]))

from simdesign import rcmrf  # noqa
from simdesign.rcmrf import StandardGeometry  # noqa
from simdesign.utils.mesh import Point, Line, Rectangle, Square  # noqa
import simdesign.rcmrf.bnsm.baselib.building as bnsm_building  # noqa


def make_frame():
    """Two storeys of 3 m and 2x2 bays of 4 m."""
    return StandardGeometry(2, 3.0, 2, 4.0, 2, 4.0)


# ---------------------------------------------------------------------------
# Geometry editing
# ---------------------------------------------------------------------------
def test_modify_floor_height():
    """Changing a storey height shifts the floors above it."""
    frame = make_frame()
    frame.modify_floor_height(1, 4.0)
    z = frame.system_grid_data.z
    assert [z.ord_by_id(k) for k in range(3)] == [0.0, 4.0, 7.0]
    assert {p.coordinates[2] for p in frame.points
            if p.grid_ids[2] == 1} == {4.0}


def test_modify_bay_width():
    """Changing a bay width shifts the grid lines after it."""
    frame = make_frame()
    frame.modify_bay_width(1, 5.0, 'x')
    x = frame.system_grid_data.x
    assert [x.ord_by_id(i) for i in range(3)] == [0.0, 5.0, 9.0]
    assert {p.coordinates[0] for p in frame.points
            if p.grid_ids[0] == 2} == {9.0}


@pytest.mark.parametrize('stairs', [False, True])
def test_uniformise(stairs):
    """uniformise places the points at equal bay widths and storey heights
    (stair landings at mid-storey) and keeps the grid ordinates consistent
    with the points."""
    frame = make_frame()
    if stairs:
        frame.set_continuous_stairs_rectangles((0, 0), 4.0, 4.0)
        frame.add_new_elements_for_stairs(infills=False)
    frame.modify_bay_width(1, 5.0, 'x')
    frame.uniformise(bay_width_x=4.5, bay_width_y=4.5, storey_height=3.2)
    grid = frame.system_grid_data
    for point in frame.points:
        i, j, k = point.grid_ids
        np.testing.assert_allclose(point.coordinates,
                                   [4.5 * i, 4.5 * j, 3.2 * k])
        np.testing.assert_allclose(
            point.coordinates,
            [grid.x.ord_by_id(i), grid.y.ord_by_id(j), grid.z.ord_by_id(k)])
    # coordinates taken from the grid find the points again
    corner = [grid.x.ord_by_id(2), grid.y.ord_by_id(2), grid.z.ord_by_id(0)]
    assert frame.find_point_by_coordinates(corner) is not None
    if stairs:
        assert any(k % 1 for k in grid.z.ids)  # mid-storey landing level


def test_remove_rectangle():
    """Removing a slab can keep or remove its lines and points."""
    frame = make_frame()
    n_rect, n_line, n_point = (len(frame.rectangles), len(frame.lines),
                               len(frame.points))
    frame.remove_rectangle([0, 0, 1], remove_lines=False,
                           remove_points=False)
    assert len(frame.rectangles) == n_rect - 1
    assert len(frame.lines) == n_line
    frame.remove_rectangle([1, 1, 2], remove_lines=True, remove_points=True)
    assert len(frame.rectangles) == n_rect - 2
    assert len(frame.lines) < n_line
    assert len(frame.points) < n_point


def test_add_point_line_and_search():
    """New points and lines can be added and found again."""
    frame = make_frame()
    with pytest.warns(UserWarning):  # the point adds a grid line
        point = frame.add_new_point([8.0, 8.0, 1.0])
    base = frame.find_point_by_grid_ids([2, 2, 0])
    assert frame.find_point_by_coordinates(list(point.coordinates)) is point
    line = frame.add_new_line([base, point])
    assert frame.find_line_by_points([base, point]) is line
    assert frame.find_line_by_points([point, base]) is line


def test_find_rectangles():
    """Slabs are found from their corner points and edge lines."""
    frame = make_frame()
    corner = frame.find_point_by_grid_ids([0, 0, 1])
    assert len(frame.find_rectangles_by_point(corner)) >= 1
    beam = frame.find_line_by_points(
        [corner, frame.find_point_by_grid_ids([1, 0, 1])])
    assert len(frame.find_rectangles_by_line(beam)) >= 1


# ---------------------------------------------------------------------------
# Mesh shapes
# ---------------------------------------------------------------------------
def make_points(coords):
    """Points with the given coordinates (grid ids equal to coordinates)."""
    return [Point(list(c), list(c), tag) for tag, c in enumerate(coords, 1)]


def test_rectangle_area_and_perimeter():
    """A 4 x 3 rectangle has an area of 12 and a perimeter of 14."""
    rect = Rectangle(make_points([(0, 0, 0), (4, 0, 0), (4, 3, 0),
                                  (0, 3, 0)]))
    rect.create_lines_from_points()
    assert rect.area == pytest.approx(12.0)
    assert rect.perimeter == pytest.approx(14.0)


def test_square_rejects_a_rectangle():
    """A Square needs equal sides."""
    Square(make_points([(0, 0, 0), (2, 0, 0), (2, 2, 0), (0, 2, 0)]))
    with pytest.raises(Exception):
        Square(make_points([(0, 0, 0), (4, 0, 0), (4, 3, 0), (0, 3, 0)]))


def test_line_unit_vector_and_length():
    """A line knows its direction and length."""
    a, b = make_points([(0, 0, 0), (3, 4, 0)])
    line = Line([a, b])
    np.testing.assert_allclose(line.unit_vector, [0.6, 0.8, 0.0])
    assert line.length == pytest.approx(5.0)


# ---------------------------------------------------------------------------
# Modal analysis fallbacks
# ---------------------------------------------------------------------------
def test_do_modal_falls_back_to_the_next_solver(designs, monkeypatch):
    """An invalid spectrum from the first solver is replaced by the next
    solver's."""
    real_eigen = bnsm_building.ops.eigen
    calls = []

    def first_solver_fails(*args):
        calls.append(args)
        values = real_eigen(*args)
        return [-1.0] * len(values) if len(calls) == 1 else values

    monkeypatch.setattr(bnsm_building.ops, 'eigen', first_solver_fails)
    bnsm = rcmrf.BNSM(design=designs['eu_cdh'], model='DP01')
    periods = bnsm.do_modal(num_modes=3)['eigenPeriod']
    assert len(calls) >= 2
    assert all(np.isfinite(periods)) and all(t > 0 for t in periods)


def test_do_modal_raises_without_a_valid_spectrum(designs, monkeypatch):
    """If no solver gives valid eigenvalues, do_modal raises an error."""
    monkeypatch.setattr(bnsm_building.ops, 'eigen',
                        lambda *args: [0.0] * int(args[-1]))
    bnsm = rcmrf.BNSM(design=designs['eu_cdh'], model='DP01')
    with pytest.raises(RuntimeError):
        bnsm.do_modal(num_modes=3)


# ---------------------------------------------------------------------------
# Plots (off-screen rendering with pyvista)
# ---------------------------------------------------------------------------
RENDER_PROBE = (
    "import pyvista as pv; p = pv.Plotter(off_screen=True); "
    "p.add_mesh(pv.Sphere()); p.screenshot(return_img=True); p.close()"
)


def rendering_available() -> bool:
    """True if pyvista can render off screen on this machine.

    The plots are skipped on CI runners, which have no OpenGL. Elsewhere, a
    test render runs in a separate process, because VTK aborts the whole
    process (no Python exception) when off-screen rendering is not
    available.
    """
    if os.environ.get('CI'):
        return False
    try:
        result = subprocess.run([sys.executable, '-c', RENDER_PROBE],
                                capture_output=True, timeout=120)
    except (OSError, subprocess.TimeoutExpired):
        return False
    return result.returncode == 0


needs_rendering = pytest.mark.skipif(
    not rendering_available(), reason='off-screen rendering not available')


@needs_rendering
def test_export_mesh_to_html(tmp_path):
    """The geometry exports to an HTML file."""
    frame = make_frame()
    frame.set_continuous_stairs_rectangles((0, 0), 4.0, 4.0)
    frame.add_infills(exterior=True, interior=False, ext_type='Weak',
                      int_type='Weak')
    frame.add_new_elements_for_stairs(infills=True)
    path = tmp_path / 'mesh.html'
    frame.export_mesh_to_html(path=str(path))
    assert path.stat().st_size > 0


@needs_rendering
@pytest.mark.parametrize('model', ['CP03', 'DP01'])
def test_plot_model_and_mode_shape(designs, model, tmp_path):
    """The model and its first mode shape are plotted to files."""
    bnsm = rcmrf.BNSM(design=designs['eu_cdh'], model=model,
                      include_infills=True)
    bnsm.plot_model(directory=tmp_path, show=False)
    bnsm.plot_mode_shape(mode_number=1, contour='x', show=False,
                         directory=tmp_path)
    assert len(list(tmp_path.iterdir())) >= 2
