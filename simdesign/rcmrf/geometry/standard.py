"""
Standard geometry module for defining regular frame structures parametrically.

This module provides the :class:`StandardGeometry` class for uniform,
rectangular RC moment-resisting frames (equal bay widths and storey heights),
using the tag encoding of :mod:`simdesign.utils.tags` for points, lines and
rectangles (two digits per grid index).
"""
# Imports from installed packages
from typing import Literal, Optional

# Imports from geometry library
from .base import GeometryBase, Point, SystemGridData

# Imports from utils library
from ...utils.misc import round_list
from ...utils.tags import (  # noqa: F401 (decoders re-exported)
    encode_point_tag, decode_point_tag, encode_line_tag, decode_line_tag,
    encode_rectangle_tag, decode_rectangle_tag
)


class StandardGeometry(GeometryBase):
    """
    Class representing a standard frame structure.

    This class inherits from
    :class:`~simdesign.rcmrf.geometry.base.GeometryBase` and extends
    it to represent a standard frame structure. It initializes the
    frame with the given parameters and constructs the base geometry
    of the frame. It is called StandardGeometry because its base
    geometry is built as a uniform and regular frame (equal bay widths
    and storey heights).

    Parameters
    ----------
    num_storeys : int
        The number of storeys in the frame.
    storey_height : float
        The height of each storey.
    num_bays_x : int
        The number of bays along the X-direction.
    bay_width_x : float
        The width of each bay along the X-direction.
    num_bays_y : int
        The number of bays along the Y-direction.
    bay_width_y : float
        The width of each bay along the Y-direction.

    Attributes
    ----------
    _num_storeys : int
        The number of storeys in the frame.
    _num_bays_x : int
        The number of bays along the X-direction.
    _num_bays_y : int
        The number of bays along the Y-direction.
    _storey_height : float
        The height of each storey.
    _bay_width_x : float
        The width of each bay along the X-direction.
    _bay_width_y : float
        The width of each bay along the Y-direction.
    """
    _num_storeys: int
    _num_bays_x: int
    _num_bays_y: int
    _storey_height: float
    _bay_width_x: float
    _bay_width_y: float
    __str: str = "StandardGeometry"
    """The private attribute for string representation of the StandardGeometry.
    """

    def __init__(
        self, num_storeys: int, storey_height: float, num_bays_x: int,
        bay_width_x: float, num_bays_y: int, bay_width_y: float,
        tag: str | None = None
    ) -> None:
        """
        Initialize the StandardGeometry with the given parameters.

        Parameters
        ----------
        tag : str | None
            Optional tag appended to the string representation of the instance:
            ``self.__str = f"StandardGeometry-{tag}"``. If ``None``, the
            default ``"StandardGeometry"`` label is used.
        """
        if tag:
            self.__str = f"StandardGeometry-{tag}"

        self._num_storeys = num_storeys
        self._storey_height = storey_height
        self._num_bays_x = num_bays_x
        self._bay_width_x = bay_width_x
        self._num_bays_y = num_bays_y
        self._bay_width_y = bay_width_y
        self._build_base()
        self._check_for_any_not_allowed_lines()
        self._check_for_any_not_allowed_rectangles()

    def __str__(self) -> str:
        """
        Return a string representation of the StandardGeometry.

        Returns
        -------
        str
            String representation of the StandardGeometry.
        """
        return self.__str

    def _initialise_points(self) -> None:
        """
        Generate grid points for the regular frame and populate
        ``self.points``.

        Iterates over all storey, y-bay, and x-bay indices to create a
        :class:`~simdesign.utils.mesh.Point` at each grid node. Coordinates are
        computed from the uniform bay widths and storey height, and tags are
        encoded via :func:`encode_point_tag`. Sets ``self.system_grid_data``
        once all points are built.
        """
        for k in range(self._num_storeys + 1):  # Along -z
            for j in range(self._num_bays_y + 1):  # Along -y
                for i in range(self._num_bays_x + 1):  # Along -x
                    tag = encode_point_tag(i, j, k)
                    x = i * self._bay_width_x  # x-coord
                    y = j * self._bay_width_y  # y-coord
                    z = k * self._storey_height  # z-coord
                    grid = [i, j, k]  # Grid IDs in x, y, z
                    coords = round_list([x, y, z])  # # Coordinates in x, y, z
                    new_point = Point(grid, coords, tag)  # create the Point
                    self.points.append(new_point)  # append to points

        # Set the system grid data
        self.system_grid_data = SystemGridData(self.points)

    def _initialise_lines(self) -> None:
        """
        Generate column and beam lines for the regular frame.

        Creates three groups of lines via :meth:`add_new_line`:

        - **Columns** (Z-direction): one per grid node from storey ``k`` to
          ``k+1``, tagged with ``'Z'`` orientation. Section rotation angles
          are assigned afterwards by :meth:`_set_column_line_rot_angles`.
        - **X-beams**: one per bay along x at each elevated storey level,
          tagged with ``'X'`` orientation.
        - **Y-beams**: one per bay along y at each elevated storey level,
          tagged with ``'Y'`` orientation.
        """
        # Lines along -Z
        for k in range(self._num_storeys):  # Along -z
            for j in range(self._num_bays_y + 1):  # Along -y
                for i in range(self._num_bays_x + 1):  # Along -x
                    point1_grid = [i, j, k]
                    point2_grid = [i, j, k + 1]
                    point1 = self.find_point_by_grid_ids(point1_grid)
                    point2 = self.find_point_by_grid_ids(point2_grid)
                    points = [point1, point2]
                    tag = encode_line_tag(i, j, k, 'Z')
                    self.add_new_line(points, tag, 'Column')
        # Assign column line rotation angle
        self._set_column_line_rot_angles()

        # Lines along -X
        for k in range(1, self._num_storeys + 1):  # Along -z
            for j in range(self._num_bays_y + 1):  # Along -y
                for i in range(self._num_bays_x):  # Along -x
                    point1_grid = [i, j, k]
                    point2_grid = [i + 1, j, k]
                    point1 = self.find_point_by_grid_ids(point1_grid)
                    point2 = self.find_point_by_grid_ids(point2_grid)
                    points = [point1, point2]
                    tag = encode_line_tag(i, j, k, 'X')
                    self.add_new_line(points, tag, 'Beam')
        # Lines along -Y
        for k in range(1, self._num_storeys + 1):  # Along -z
            for j in range(self._num_bays_y):  # Along -y
                for i in range(self._num_bays_x + 1):  # Along -x
                    point1_grid = [i, j, k]
                    point2_grid = [i, j + 1, k]
                    point1 = self.find_point_by_grid_ids(point1_grid)
                    point2 = self.find_point_by_grid_ids(point2_grid)
                    points = [point1, point2]
                    tag = encode_line_tag(i, j, k, 'Y')
                    self.add_new_line(points, tag, 'Beam')

    def _initialise_rectangles(self) -> None:
        """
        Generate slab rectangles for each floor bay and populate the frame.

        Iterates over all elevated storey levels and XY bays, creating one
        :class:`~simdesign.rcmrf.geometry.base.Rectangle` per bay via
        :meth:`add_new_rectangle` with component type ``'Slab'``.
        Tags are encoded via :func:`encode_rectangle_tag` using
        the ``'XY'`` plane.
        """
        # Counter for line tags
        for k in range(1, self._num_storeys + 1):  # Along -z
            for j in range(self._num_bays_y):  # Along -y
                for i in range(self._num_bays_x):  # Along -x
                    # Find points on the rectangle
                    lower_left_grid = [i, j, k]
                    upper_right_grid = [i + 1, j + 1, k]
                    lower_right_grid = [i + 1, j, k]
                    upper_left_grid = [i, j + 1, k]
                    point1 = self.find_point_by_grid_ids(lower_left_grid)
                    point2 = self.find_point_by_grid_ids(upper_left_grid)
                    point3 = self.find_point_by_grid_ids(upper_right_grid)
                    point4 = self.find_point_by_grid_ids(lower_right_grid)
                    points = [point1, point2, point3, point4]
                    # Create a Rectangle object and append
                    tag = encode_rectangle_tag(i, j, k, 'XY')
                    self.add_new_rectangle(points, tag, 'Slab')

    def _set_column_line_rot_angles(self) -> None:
        """Set the default rotation angles of the element sections in degrees,
        measured counterclockwise from the positive x-axis.
        """
        # Get maximum and minimum grid ids
        xid_min = min(self.system_grid_data.x.ids)
        xid_max = max(self.system_grid_data.x.ids)
        yid_min = min(self.system_grid_data.y.ids)
        yid_max = max(self.system_grid_data.y.ids)

        for line in self.column_lines:
            # Get facade id
            facade_id = 0
            pi, _ = line.points
            grid_i = pi.grid_ids.copy()
            if grid_i[0] == xid_min:
                facade_id = 1
            elif grid_i[0] == xid_max:
                facade_id = 3
            elif grid_i[1] == yid_min:
                facade_id = 2
            elif grid_i[1] == yid_max:
                facade_id = 4
            # Corner lines
            if grid_i[0] == xid_min and grid_i[1] == yid_min:
                facade_id = 12
            elif grid_i[0] == xid_min and grid_i[1] == yid_max:
                facade_id = 14
            elif grid_i[0] == xid_max and grid_i[1] == yid_min:
                facade_id = 32
            elif grid_i[0] == xid_max and grid_i[1] == yid_max:
                facade_id = 34

            # The rotation angle of the element section.
            if facade_id in [2, 4, 12, 14, 32, 34]:
                line.rot_angle = 90.0  # +y
            else:
                line.rot_angle = 0.0   # +x

    def add_infills(
        self, xz: bool = True, yz: bool = True, ground: bool = True,
        exterior: bool = True, interior: bool = False,
        ext_type: Optional[Literal['Weak', 'Medium', 'Strong']] = None,
        int_type: Optional[Literal['Weak', 'Medium', 'Strong']] = None,
    ) -> None:
        """
        Initialize the rectangles representing infill panels
        in XZ and/or YZ planes of the frame.

        Parameters
        ----------
        xz : bool, default=True
            If True, add infill rectangles in XZ planes
            (varying x and z for fixed y).
        yz : bool, default=True
            If True, add infill rectangles in YZ planes
            (varying y and z for fixed x).
        ground : bool, default=True
            If True, include panels starting from ground level
            (k=0..num_storeys-1).
            If False, start from the first elevated storey
            (k=1..num_storeys-1).
        exterior : bool, default=True
            Include infills on exterior grid lines
            (i=0 or i=n_x, j=0 or j=n_y).
        interior : bool, default=False
            Include infills on interior grid lines
            (excluding the exterior lines).
        ext_type : str | None
            Typology of exterior frame infills.
            Options: 'Weak', 'Medium', 'Strong'.
        int_type : str | None
            Typology of interior frame infills
            Options: 'Weak', 'Medium', 'Strong'.

        Notes
        -----
        - For YZ panels, the fixed-x indices (``i_range``) are determined by
          the ``yz``, ``exterior``, and ``interior`` switches.
        - For XZ panels, the fixed-y indices (``j_range``) are determined by
          the ``xz``, ``exterior``, and ``interior`` switches.
        - Created rectangles are tagged using :func:`encode_rectangle_tag`
          with plane 'YZ' or 'XZ' and assigned the label 'Infill'.
        """
        # Helper to pick correct strength
        def get_typology(is_exterior: bool
                         ) -> Optional[Literal['Weak', 'Medium', 'Strong']]:
            """Return appropriate strength label."""
            if is_exterior and ext_type is not None:
                return ext_type
            if not is_exterior and int_type is not None:
                return int_type
            return None

        # Grid IDs along -Z
        if ground:
            k_range = range(self._num_storeys)
        else:
            k_range = range(1, self._num_storeys)

        # Grid IDs along -X
        if yz and exterior and interior:
            i_range = range(self._num_bays_x + 1)
        elif yz and interior:
            i_range = range(1, self._num_bays_x)
        elif yz and exterior:
            i_range = [0, self._num_bays_x]
        else:
            i_range = []

        # Grid IDs along -Y
        if xz and exterior and interior:
            j_range = range(self._num_bays_y + 1)
        elif xz and interior:
            j_range = range(1, self._num_bays_y)
        elif xz and exterior:
            j_range = [0, self._num_bays_y]
        else:
            j_range = []

        # Infills in YZ planes
        for i in i_range:  # Along X
            for k in k_range:  # Along Z
                for j in range(self._num_bays_y):  # Along Y
                    lower_left_grid = [i, j, k]
                    upper_right_grid = [i, j + 1, k + 1]
                    lower_right_grid = [i, j + 1, k]
                    upper_left_grid = [i, j, k + 1]
                    points = [
                        self.find_point_by_grid_ids(lower_left_grid),
                        self.find_point_by_grid_ids(upper_left_grid),
                        self.find_point_by_grid_ids(upper_right_grid),
                        self.find_point_by_grid_ids(lower_right_grid)
                    ]
                    is_exterior = (i == 0 or i == self._num_bays_x)
                    typology = get_typology(is_exterior)
                    tag = encode_rectangle_tag(i, j, k, 'YZ')
                    self.add_new_rectangle(points, tag, 'Infill', typology)

        # Infills in XZ planes
        for j in j_range:  # Along Y
            for k in k_range:  # Along Z
                for i in range(self._num_bays_x):  # Along X
                    lower_left_grid = [i, j, k]
                    upper_right_grid = [i + 1, j, k + 1]
                    lower_right_grid = [i + 1, j, k]
                    upper_left_grid = [i, j, k + 1]
                    points = [
                        self.find_point_by_grid_ids(lower_left_grid),
                        self.find_point_by_grid_ids(upper_left_grid),
                        self.find_point_by_grid_ids(upper_right_grid),
                        self.find_point_by_grid_ids(lower_right_grid)
                    ]
                    is_exterior = (j == 0 or j == self._num_bays_y)
                    typology = get_typology(is_exterior)
                    tag = encode_rectangle_tag(i, j, k, 'XZ')
                    self.add_new_rectangle(points, tag, 'Infill', typology)

    def add_new_elements_for_stairs(
        self,
        ext_type: Optional[Literal['Weak', 'Medium', 'Strong']] = None,
        int_type: Optional[Literal['Weak', 'Medium', 'Strong']] = None,
        infills: bool = True
    ) -> None:
        """Adds the new lines (beams) and connecting points for supporting
        stairs along with the masonry infill walls surrounding the stairs.

        This method adds new lines and points to represent stairs in the frame.
        It identifies rectangles that represent stairs and generates additional
        points and lines for each staircase within those rectangles. For each
        staircase, it creates two additional points at mid-storey height,
        divides the vertical lines passing through these points into two, and
        adds a beam between the two nodes supporting the staircase loads.

        Parameters
        ----------
        ext_type : str | None
            Typology of exterior frame infills.
            Options: 'Weak', 'Medium', 'Strong'.
        int_type : str | None
            Typology of interior frame infills.
            Options: 'Weak', 'Medium', 'Strong'.
        infills : bool, optional
            Flag to add infill walls surrounding the stairs.

        Notes
        -----
        - Ensure to add the lines and points for stairs after finalizing the
          base geometry.
        - The grid IDs at the stair line levels should always end with
          '.5'. For example, for stairs between floor one and two the grid id
          will be 1.5.
        - Do not update the grid system after using this method.

        TODO
        ----
        - Improve the the behaviour grid id restrictions of stairs.
        - Add option for defining the supporting beam location
        """
        if infills:
            self._add_infills_for_stairs(ext_type, int_type)
        super().add_new_elements_for_stairs()

    def _add_infills_for_stairs(
        self,
        ext_type: Optional[Literal['Weak', 'Medium', 'Strong']] = None,
        int_type: Optional[Literal['Weak', 'Medium', 'Strong']] = None
    ) -> None:
        """
        Adds the masonry infill walls which are located around the
        stairs. Typically these walls are reinforced concrete in
        the new buildings.

        Parameters
        ----------
        ext_type : str | None
            Typology of exterior frame infills.
            Options: 'Weak', 'Medium', 'Strong'.
        int_type : str | None
            Typology of interior frame infills.
            Options: 'Weak', 'Medium', 'Strong'.
        """
        # Helper to pick correct strength
        def get_typology(is_exterior: bool
                         ) -> Optional[Literal['Weak', 'Medium', 'Strong']]:
            """Return appropriate strength label."""
            if is_exterior and ext_type is not None:
                return ext_type
            if not is_exterior and int_type is not None:
                return int_type
            return None

        for rectangle in self.stairs_rectangles:

            # 1st side wall in YZ
            i, j, k = rectangle.points[0].grid_ids
            lower_left_grid = [i, j, k - 1]
            upper_right_grid = [i, j + 1, k]
            lower_right_grid = [i, j + 1, k - 1]
            upper_left_grid = [i, j, k]
            points = [
                self.find_point_by_grid_ids(lower_left_grid),
                self.find_point_by_grid_ids(upper_left_grid),
                self.find_point_by_grid_ids(upper_right_grid),
                self.find_point_by_grid_ids(lower_right_grid)
            ]
            inf = self.find_rectangle_by_points(points)
            if inf is None:
                is_exterior = (i == 0 or i == self._num_bays_x)
                typology = get_typology(is_exterior)
                inf = self.add_new_rectangle(points, None, "Infill", typology)
            inf.stairs = True

            # 2nd side wall in YZ
            i, j, k = rectangle.points[3].grid_ids
            lower_left_grid = [i, j, k - 1]
            upper_right_grid = [i, j + 1, k]
            lower_right_grid = [i, j + 1, k - 1]
            upper_left_grid = [i, j, k]
            points = [
                self.find_point_by_grid_ids(lower_left_grid),
                self.find_point_by_grid_ids(upper_left_grid),
                self.find_point_by_grid_ids(upper_right_grid),
                self.find_point_by_grid_ids(lower_right_grid)
            ]
            inf = self.find_rectangle_by_points(points)
            if inf is None:
                is_exterior = (i == 0 or i == self._num_bays_x)
                typology = get_typology(is_exterior)
                inf = self.add_new_rectangle(points, None, "Infill", typology)
            inf.stairs = True

            # 1st side wall in XZ
            i, j, k = rectangle.points[0].grid_ids
            lower_left_grid = [i, j, k - 1]
            upper_right_grid = [i + 1, j, k]
            lower_right_grid = [i + 1, j, k - 1]
            upper_left_grid = [i, j, k]
            points = [
                self.find_point_by_grid_ids(lower_left_grid),
                self.find_point_by_grid_ids(upper_left_grid),
                self.find_point_by_grid_ids(upper_right_grid),
                self.find_point_by_grid_ids(lower_right_grid)
            ]
            inf = self.find_rectangle_by_points(points)
            if inf is None:
                is_exterior = (j == 0 or j == self._num_bays_y)
                typology = get_typology(is_exterior)
                inf = self.add_new_rectangle(points, None, "Infill", typology)
            inf.stairs = True
