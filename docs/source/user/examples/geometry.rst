Geometry
--------

SimDesign provides two geometry classes for defining a building's structural
layout before performing simulated design:

- :class:`~simdesign.rcmrf.geometry.base.StandardGeometry` — programmatically
  constructed rectangular grids with optional bay and storey modifications.
- :class:`~simdesign.rcmrf.geometry.base.CustomGeometry` — layouts loaded from
  an Excel file (including those previously exported from ``StandardGeometry``).

The sections below progress from a simple uniform grid to increasingly complex
configurations and finally show how to use a custom geometry in design.

Simple uniform geometry
^^^^^^^^^^^^^^^^^^^^^^^^

A regular 4 × 4 bay, 4-storey frame with constant bay widths and storey heights.

.. code-block:: python

    from pathlib import Path
    from simdesign.rcmrf import StandardGeometry

    regular_frame = StandardGeometry(
        num_storeys=4,
        storey_height=3.0,
        num_bays_x=4,
        bay_width_x=5.0,
        num_bays_y=4,
        bay_width_y=3.5,
    )
    regular_frame.add_infills()

    # Place a staircase bay starting at grid position (0, 0)
    regular_frame.set_continuous_stairs_rectangles(
        stair_loc=(0, 0),
        stairs_width_x=2,
        stairs_width_y=4,
    )

    # Export to Excel for later use as a CustomGeometry input
    regular_frame.write_mesh_to_xlsx(Path("uniform-geometry.xlsx"))

    # Add stair elements and visualise
    regular_frame.add_new_elements_for_stairs()
    regular_frame.show_mesh()
    regular_frame.export_mesh_to_html(Path("uniform-geometry.html"))

.. raw:: html

   <iframe
     src="../../_static/geometry/simple-uniform-geometry.html"
     width="100%"
     height="500px"
     style="border:none; border-radius:4px;">
   </iframe>

.. note::

   :meth:`~simdesign.rcmrf.geometry.base.StandardGeometry.add_new_elements_for_stairs`
   must always be called **after** all geometry modifications are complete and
   before the geometry object is used in design.

Non-uniform geometry
^^^^^^^^^^^^^^^^^^^^^

Individual floor heights and bay widths can be modified after construction to
introduce non-uniformity.

.. code-block:: python

    from pathlib import Path
    from simdesign.rcmrf import StandardGeometry

    regular_frame = StandardGeometry(
        num_storeys=4,
        storey_height=3.0,
        num_bays_x=4,
        bay_width_x=5.0,
        num_bays_y=4,
        bay_width_y=3.5,
    )
    regular_frame.set_continuous_stairs_rectangles(
        stair_loc=(0, 0),
        stairs_width_x=2,
        stairs_width_y=4,
    )

    # Raise the ground-floor height to 4 m (floor_id=1 is the ground floor)
    regular_frame.modify_floor_height(floor_id=1, height=4.0)
    # Widen the fourth bay in the Y direction
    regular_frame.modify_bay_width(bay_id=3, width=5.0, direction="y")

    regular_frame.write_mesh_to_xlsx(Path("nonuniform-geometry.xlsx"))
    regular_frame.add_new_elements_for_stairs(infills=False)
    regular_frame.show_mesh()
    regular_frame.export_mesh_to_html(Path("nonuniform-geometry.html"))

.. raw:: html

   <iframe
     src="../../_static/geometry/simple-nonuniform-geometry.html"
     width="100%"
     height="500px"
     style="border:none; border-radius:4px;">
   </iframe>

L-shaped geometry
^^^^^^^^^^^^^^^^^^

An L-shaped footprint is obtained by removing bays from a regular grid using
:meth:`~simdesign.rcmrf.geometry.base.StandardGeometry.remove_rectangle`.
Each bay is identified by its grid indices ``[ix, iy, iz]`` (x-bay, y-bay,
storey level, all starting from 1 for the first storey).

.. code-block:: python

    from pathlib import Path
    from simdesign.rcmrf import StandardGeometry

    regular_frame = StandardGeometry(
        num_storeys=5,
        storey_height=3.0,
        num_bays_x=5,
        bay_width_x=4.0,
        num_bays_y=5,
        bay_width_y=4.0,
    )

    # Remove the upper-right 3×3 block of bays on every storey
    bays_to_remove = [
        [ix, iy, iz]
        for iz in range(1, 6)
        for ix in [2, 3, 4]
        for iy in [2, 3, 4]
    ]
    for grid_ids in bays_to_remove:
        regular_frame.remove_rectangle(
            grid_ids, remove_lines=True, remove_points=True
        )

    regular_frame.set_continuous_stairs_rectangles(
        stairs_loc=(0, 0), stairs_width_x=4, stairs_width_y=4
    )
    regular_frame.modify_floor_height(floor_id=1, height=4.0)
    regular_frame.write_mesh_to_xlsx(Path("l-shape-geometry.xlsx"))
    regular_frame.add_new_elements_for_stairs(infills=False)
    regular_frame.show_mesh()
    regular_frame.export_mesh_to_html(Path("l-shape-geometry.html"))

.. raw:: html

   <iframe
     src="../../_static/geometry/irregular-geometry.html"
     width="100%"
     height="500px"
     style="border:none; border-radius:4px;">
   </iframe>

.. note::

   ``remove_lines=True, remove_points=True`` also deletes grid lines and nodes
   that become isolated after the bay is removed. Use ``remove_lines=False,
   remove_points=False`` when adjacent bays still share those elements and they
   should be retained.

Complex geometry with custom elements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Custom lines and points can be added to the mesh after standard operations,
enabling geometries that cannot be expressed purely through grid modifications.

.. code-block:: python

    from pathlib import Path
    from simdesign.rcmrf import StandardGeometry

    regular_frame = StandardGeometry(
        num_storeys=4,
        storey_height=3.0,
        num_bays_x=4,
        bay_width_x=4.0,
        num_bays_y=4,
        bay_width_y=4.0,
    )

    # Remove two bays on storey 1 without deleting shared elements
    for grid_ids in [[1, 0, 1], [2, 0, 1]]:
        regular_frame.remove_rectangle(
            grid_ids, remove_lines=False, remove_points=False
        )

    # Remove two bays on storeys 1–2 with full cleanup
    for grid_ids in [[3, 3, 2], [3, 3, 1]]:
        regular_frame.remove_rectangle(
            grid_ids, remove_lines=True, remove_points=True
        )

    # Add a vertical element at a corner that was removed from the grid
    grids = regular_frame.system_grid_data
    x = grids.x.ord_by_id(4)
    y = grids.y.ord_by_id(4)
    z_bottom = grids.z.ord_by_id(0)
    z_top    = grids.z.ord_by_id(3)
    pt_bottom = regular_frame.add_new_point([x, y, z_bottom])
    pt_top    = regular_frame.find_point_by_coordinates([x, y, z_top])
    regular_frame.add_new_line([pt_bottom, pt_top])

    regular_frame.set_continuous_stairs_rectangles(
        stairs_bay_loc=(0, 0), stairs_width_x=2, stairs_width_y=4
    )
    regular_frame.add_new_elements_for_stairs(infills=False)
    regular_frame.modify_floor_height(floor_id=1, height=4.0)
    regular_frame.show_mesh()
    regular_frame.export_mesh_to_html(Path("complex-geometry.html"))

.. raw:: html

   <iframe
     src="../../_static/geometry/complex-geometry.html"
     width="100%"
     height="500px"
     style="border:none; border-radius:4px;">
   </iframe>

Loading and modifying geometry from file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A geometry exported with
:meth:`~simdesign.rcmrf.geometry.base.StandardGeometry.write_mesh_to_xlsx`
can be reloaded as a :class:`~simdesign.rcmrf.geometry.base.CustomGeometry`
object, uniformised, and further modified before use in design.

.. code-block:: python

    from pathlib import Path
    from simdesign.rcmrf import CustomGeometry

    custom_frame = CustomGeometry(Path("uniform-geometry.xlsx"))

    # Overwrite all bay widths and storey heights with uniform values
    custom_frame.uniformise(
        bay_width_x=4.0, bay_width_y=4.0, storey_height=3.0
    )

    # Redefine the staircase location
    custom_frame.set_continuous_stairs_rectangles(
        stairs_loc=(0, 0), stairs_width_x=2, stairs_width_y=4
    )

    # Raise the ground floor
    custom_frame.modify_floor_height(floor_id=1, height=4.0)

    custom_frame.add_new_elements_for_stairs()
    custom_frame.show_mesh()
    custom_frame.export_mesh_to_html(Path("modified-custom-geometry.html"))

.. raw:: html

   <iframe
     src="../../_static/geometry/modified-custom-geometry.html"
     width="100%"
     height="500px"
     style="border:none; border-radius:4px;">
   </iframe>

Using custom geometry in design
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For a complete example of using a
:class:`~simdesign.rcmrf.geometry.base.CustomGeometry` or a
:class:`~simdesign.rcmrf.geometry.base.StandardGeometry` object in the full
BED workflow (BDIM → BNSM → pushover), see
:doc:`design_with_specific_geometry`.
