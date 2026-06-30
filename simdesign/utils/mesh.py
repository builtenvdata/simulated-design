"""This module provides the classes used for defining structural
meshes with varying geometries.
"""
# Imports from installed packages
import numpy as np
from typing import Union, Optional, List
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for geometric shapes.

    Attributes
    ----------
    tag : Optional[int]
        Unique identifier for the shape.
    """
    tag: Optional[int]

    def __init__(self, tag: int | None) -> None:
        """Initialize a Shape object.

        Parameters
        ----------
        tag : int | None
            Unique identifier for the shape.
        """
        self.tag = tag

    @property
    @abstractmethod
    def ndim(self) -> int:
        """Return the number of dimensions of the shape.

        Returns
        -------
        int
            Number of dimensions.
        """


class Point(Shape):
    """Point in 3D space defined by grid IDs and coordinates.

    Attributes
    ----------
    grid_ids : List[int | float]
        Point grid identifiers (x, y, z).
    coordinates : List[float]
        Point coordinates (x, y, z).
    """
    grid_ids: List[Union[int, float]]
    coordinates: List[float]

    def __init__(self, grid: List[Union[int, float]], coordinates: List[float],
                 tag: int) -> None:
        """Initialize a Point object.

        Parameters
        ----------
        grid : List[int | float]
            Grid IDs in x, y, z.
        coordinates : List[float]
            Coordinates in x, y, z.
        tag : int
            Unique identifier for the point.
        """
        super().__init__(tag)
        self.grid_ids = grid  # Grid IDs in x, y, z
        self.coordinates = coordinates  # Coordinates in x, y, z

    def __str__(self) -> str:
        """Return a string representation of the Point object.

        Returns
        -------
        str
            String representation.
        """
        return f"Point{self.tag}{tuple(self.coordinates)}"

    @property
    def ndim(self) -> int:
        """Return the number of dimensions (always 0 for a point).

        Returns
        -------
        int
            Number of dimensions (always 0 for a point).
        """
        return 0


class Line(Shape):
    """Straight line segment defined by two points.

    Attributes
    ----------
    points : List[Point]
        List of points defining the line.
    """
    points: List[Point]

    def __init__(self, points: List[Point], tag: Optional[int] = None) -> None:
        """Initialize a Line object.

        Parameters
        ----------
        points : List[Point]
            List of points defining the line.
        tag : int, optional
            Unique identifier for the line. By default None.
        """
        super().__init__(tag)

        # Check for None points
        if None in points:
            raise ValueError("The object contains undefined points.")
        else:
            self.points = points
            self._is_line()
            self.sort_points_xyz()

    def __str__(self) -> str:
        """Return a string representation of the Line object.

        Returns
        -------
        str
            String representation.
        """
        points = ", ".join([str(point) for point in self.points])
        return (f"Line[{points}]")

    @property
    def direction_vector(self) -> np.ndarray:
        """Return the direction vector of the line.

        Returns
        -------
        np.ndarray
            Direction vector of the line.
        """
        start_point = np.array(self.points[0].coordinates)
        end_point = np.array(self.points[1].coordinates)
        return end_point - start_point

    @property
    def unit_vector(self) -> np.ndarray:
        """Return the unit vector of the line.

        Returns
        -------
        np.ndarray
            Unit vector of the line.
        """
        magnitude = np.linalg.norm(self.direction_vector)
        if magnitude != 0:
            return self.direction_vector / magnitude
        else:
            return self.direction_vector

    @property
    def ndim(self) -> int:
        """Return the number of dimensions (always 1 for a line).

        Returns
        -------
        int
            Number of dimensions (always 1 for a line).
        """
        return 1

    @property
    def length(self) -> np.float64:
        """Return the line length.

        Returns
        -------
        np.float64
            Line length.
        """
        start_point = np.array(self.points[0].coordinates)
        end_point = np.array(self.points[1].coordinates)
        return np.sum((end_point - start_point)**2)**0.5

    def _is_line(self) -> None:
        """Check if the shape is a line.

        Raises
        ------
        ValueError
            If the shape is not a line.
        """
        if len(self.points) != 2:
            ValueError("The points in shape is not 2."
                       "It cannot be a line.")
        if self.length == 0:
            ValueError("The points of line should have different coordinates.")

    def sort_points_xyz(self) -> None:
        """Sort points in increasing (x, y, z) lexicographic order."""
        def xyz_key(p: Point):
            return tuple(p.coordinates)

        self.points = sorted(self.points, key=xyz_key)


class Polygon(Shape):
    """Flat polygon defined by an ordered list of coplanar points.

    Attributes
    ----------
    points : List[Point]
        List of points defining the polygon.
    lines : List[Line], optional
        List of lines composing the polygon.
    """
    points: List[Point]
    lines: Optional[List[Line]]

    def __init__(self, points: List[Point], lines: List[Line] = None,
                 tag: Optional[int] = None) -> None:
        """Initialize a Polygon object.

        Parameters
        ----------
        points : List[Point]
            List of points defining the polygon.
        lines : List[Line], optional
            List of lines composing the polygon. By default None.
        tag : int, optional
            Unique identifier for the polygon. By default None.
        """
        super().__init__(tag)

        # Check for None points
        if None in points:
            raise ValueError("The object contains undefined points.")
        else:
            self.points = points
            self.lines = lines
            self.sort_points_xyz_ccw()
            self.sort_lines()
            self._is_polygon()

    @property
    def ndim(self) -> int:
        """Return the number of dimensions (always 2 for a polygon).

        Returns
        -------
        int
            Number of dimensions (always 2 for a polygon).
        """
        return 2

    @property
    def vertices(self) -> np.ndarray:
        """Return the vertices of the polygon as a 2D array.

        Returns
        -------
        np.ndarray
            Vertices of the polygon.
        """
        return np.array([point.coordinates for point in self.points])

    @property
    def centroid(self) -> np.ndarray:
        """Return the centroid coordinates of the polygon.

        Returns
        -------
        np.ndarray
            Coordinates of the centroid of the polygon.
        """
        return np.mean(
            np.array([point.coordinates for point in self.points]),
            axis=0)

    @property
    def normal_vector(self) -> np.ndarray:
        """Return the normal vector of the polygon.

        Returns
        -------
        np.ndarray
            Normal vector of the polygon.
        """
        # Convert the coordinates of the three points on polygon to arrays
        point1 = np.array(self.points[0].coordinates)
        point2 = np.array(self.points[1].coordinates)
        point3 = np.array(self.points[2].coordinates)
        # Compute vectors lying in the polygon's plane.
        vector1 = point2 - point1
        vector2 = point3 - point1
        # Calculate the cross product to get the vector normal to the
        # polygon's plane.
        return np.cross(vector1, vector2)

    @property
    def unit_normal_vector(self) -> np.ndarray:
        """Return the unit normal vector of the polygon.

        Returns
        -------
        np.ndarray
            Unit normal vector of the polygon.
        """
        # Normalize the vector to get a unit vector.
        return self.normal_vector / np.linalg.norm(self.normal_vector)

    @property
    def perimeter(self) -> float:
        """Return the perimeter of the polygon.

        Returns
        -------
        float
            Polygon perimeter.
        """
        return sum([line.length for line in self.lines])

    @property
    def area(self) -> float:
        """Return the area of the polygon.

        Returns
        -------
        float
            Polygon area.
        """
        total_area = 0.0
        # Select a fixed vertex
        fixed_vertex = np.array(self.points[0].coordinates)
        for i in range(1, len(self.points) - 1):
            # Get the coordinates of consecutive vertices
            vertex1 = np.array(self.points[i].coordinates)
            vertex2 = np.array(self.points[i + 1].coordinates)
            # Calculate the cross product of the vectors formed by the vertices
            cross_product = np.cross(vertex1 - fixed_vertex,
                                     vertex2 - fixed_vertex)
            # Calculate the area of the triangle formed by the vertices
            triangle_area = 0.5 * np.linalg.norm(cross_product)
            # Add the area of the triangle to the total area
            total_area += triangle_area
        return total_area

    def _is_polygon(self) -> None:
        """Check if the shape is a polygon.

        Raises
        ------
        ValueError
            If the shape cannot form a polygon.
        """
        # Check if polygon has enough points
        if len(self.vertices) < 3:
            # Coplanarity is not defined for fewer than three points
            raise ValueError("The shape contains points less than 3."
                             "It cannot be a polygon")

        # Check for repeated points
        coords = [tuple(p.coordinates) for p in self.points]
        if len(set(coords)) != len(coords):
            raise ValueError("Polygon contains repeated points.")

        # Check for colinearity
        def is_colinear(p1: Point, p2: Point, p3: Point):
            v1 = np.array(p2.coordinates) - np.array(p1.coordinates)
            v2 = np.array(p3.coordinates) - np.array(p2.coordinates)
            return np.allclose(np.cross(v1, v2), 0, atol=1e-6)
        for i in range(len(self.points)):
            p1 = self.points[i]
            p2 = self.points[(i + 1) % len(self.points)]
            p3 = self.points[(i + 2) % len(self.points)]
            if is_colinear(p1, p2, p3):
                raise ValueError(
                    f"Points {p1.tag}, {p2.tag}, {p3.tag} are colinear."
                )

        # Check if all points are coplanar
        for vertex in self.vertices[3:]:
            vector = vertex - self.vertices[0]
            if not np.isclose(np.dot(self.normal_vector, vector), 0):
                raise ValueError(
                    "The given points does not satisfy coplanarity."
                    "The shape cannot be a polygon."
                    "Check if points are correctly defined. Adjacent lines"
                    "between consecutive points should not be in the same"
                    "direction.")

    def sort_points_xyz_ccw(self) -> None:
        """Sort the polygon's points counter-clockwise starting from the
        lowest (x, y, z) point."""

        origin = self.centroid
        normal = self.unit_normal_vector

        # Create local 2D coordinate system (u, v) in the polygon's plane
        u = self.vertices[0] - origin
        u = u / np.linalg.norm(u)
        v = np.cross(normal, u)

        # Project each point into 2D and store original point
        def project_to_plane(p: Point):
            vec = np.array(p.coordinates) - origin
            return np.array([np.dot(vec, u), np.dot(vec, v)])

        projected = [project_to_plane(p) for p in self.points]
        centroid_2d = np.mean(projected, axis=0)

        # Compute angle from centroid to each projected point
        def angle_from_centroid(p2d):
            return np.arctan2(p2d[1] - centroid_2d[1], p2d[0] - centroid_2d[0])

        # Pair original points with their projections and angles
        points_with_angles = list(zip(self.points, projected))
        points_with_angles.sort(key=lambda item: angle_from_centroid(item[1]))

        # Extract sorted points
        sorted_points = [p for p, _ in points_with_angles]

        # Find the index of the minimal (x, y, z) point
        def xyz_key(p: Point):
            return tuple(p.coordinates)  # (x, y, z) comparison

        min_point = min(sorted_points, key=xyz_key)
        min_index = sorted_points.index(min_point)

        # Rotate the list so the minimal point comes first
        self.points = sorted_points[min_index:] + sorted_points[:min_index]

    def sort_lines(self) -> None:
        """Sort Line objects to match the current ordered points in the
        polygon."""
        # Assuming they form a polygon
        if self.lines and None not in self.lines:
            n = len(self.points)
            # Create sorted tuples of line endpoints
            expected_pairs = [
                tuple(
                    sorted(
                        [self.points[i], self.points[(i + 1) % n]],
                        key=lambda p: tuple(p.coordinates),
                    )
                )
                for i in range(n)
            ]

            def line_key(line: Line):
                return tuple(
                    sorted(line.points, key=lambda p: tuple(p.coordinates))
                )

            self.lines = sorted(
                self.lines,
                key=lambda line: expected_pairs.index(line_key(line))
            )

    def create_lines_from_points(self) -> None:
        """Create Line objects from the current ordered points in the polygon.
        """
        n = len(self.points)
        self.lines = []
        for i in range(n):
            line = Line([self.points[i], self.points[(i + 1) % n]])
            line.sort_points_xyz()
            self.lines.append(line)


class Quadrilateral(Polygon):
    """Quadrilateral defined as a polygon with exactly four sides and four
    vertices.
    """

    def __init__(self, points: List[Point], lines: List[Line] = None,
                 tag: Optional[int] = None) -> None:
        """Initialize a Quadrilateral object.

        Parameters
        ----------
        points : List[Point]
            List of points defining the quadrilateral.
        lines : List[Line], optional
            List of lines composing the quadrilateral. By default None.
        tag : int, optional
            Unique identifier for the quadrilateral. By default None.
        """
        super().__init__(points, lines, tag)
        # Check if the points satisfy quadrilateral conditions
        self._is_quadrilateral()

    def __str__(self) -> str:
        """Return a string representation of the Quadrilateral object.

        Returns
        -------
        str
            String representation.
        """
        points = ", ".join([str(point) for point in self.points])
        return (f"Quad[{points}]")

    def _is_quadrilateral(self) -> None:
        """Check if the shape is a quadrilateral.

        Raises
        ------
        ValueError
            If the shape is not a quadrilateral.
        """
        # Check the number of vertices
        if len(self.vertices) != 4:
            raise ValueError(
                "The number of points in Polygon is not 4."
                "It cannot be quadrilateral.")


class Parallelogram(Quadrilateral):
    """Parallelogram defined as a quadrilateral with both pairs of opposite
    sides parallel.
    """

    def __init__(self, points: List[Point], lines: List[Line] = None,
                 tag: Optional[int] = None) -> None:
        """Initialize a Parallelogram object.

        Parameters
        ----------
        points : List[Point]
            List of points defining the parallelogram.
        lines : List[Line], optional
            List of lines composing the parallelogram. By default None.
        tag : int, optional
            Unique identifier for the parallelogram. By default None.
        """
        super().__init__(points, lines, tag)
        self._is_parallelogram()

    def _is_parallelogram(self) -> None:
        """Check if the shape is a parallelogram.

        Raises
        ------
        ValueError
            If the shape is not a parallelogram.
        """
        # Check if opposite sides are parallel
        v1 = self.vertices[1] - self.vertices[0]
        v2 = self.vertices[2] - self.vertices[3]
        v3 = self.vertices[2] - self.vertices[1]
        v4 = self.vertices[3] - self.vertices[0]
        bool1 = np.allclose(np.cross(v1, v2), 0)
        bool2 = np.allclose(np.cross(v3, v4), 0)

        if not (bool1 and bool2):
            raise ValueError(
                "Quadrilateral does not have parallel opposite sides."
                "It cannot be a parallelogram.")


class Rectangle(Parallelogram):
    """Rectangled defined as a parallelogram whose four interior angles
    are all right angles.
    """

    def __init__(self, points: List[Point], lines: Optional[List[Line]] = None,
                 tag: Optional[int] = None) -> None:
        """Initialize a Rectangle object.

        Parameters
        ----------
        points : List[Point]
            List of points defining the rectangle.
        lines : List[Line], optional
            List of lines composing the rectangle. By default None.
        tag : int, optional
            Unique identifier for the rectangle. By default None.
        """
        super().__init__(points, lines, tag)
        self._is_rectangle()

    def _is_rectangle(self) -> None:
        """Check if the shape is a rectangle.

        Raises
        ------
        ValueError
            If the shape is not a rectangle.
        """
        # Check if opposite sides are equal
        side_lengths = []
        for i in range(4):
            side_lengths.append(
                np.linalg.norm(self.vertices[i] - self.vertices[i - 1]))
        bool1 = np.allclose(side_lengths[0], side_lengths[2])
        bool2 = np.allclose(side_lengths[1], side_lengths[3])
        if not (bool1 and bool2):
            raise ValueError(
                "Parallelogram does not have equal opposite sides."
                "It cannot be a Rectangle.")


class Square(Rectangle):
    """Square defined as a rectangle whose four sides are all of equal length.
    """

    def __init__(self, points: List[Point], lines: Optional[List[Line]] = None,
                 tag: Optional[int] = None) -> None:
        """Initialize a Square object.

        Parameters
        ----------
        points : List[Point]
            List of points defining the square.
        lines : List[Line], optional
            List of lines composing the square. By default None.
        tag : int, optional
            Unique identifier for the square. By default None.
        """
        super().__init__(points, lines, tag)
        self._is_square()

    def _is_square(self) -> None:
        """Check if the shape is a square.

        Raises
        ------
        ValueError
            If the shape is not a square.
        """
        # Check if all sides are equal
        side_lengths = []
        for i in range(4):
            side_lengths.append(
                np.linalg.norm(self.vertices[i] - self.vertices[i - 1]))
        bool1 = np.allclose(side_lengths[0], side_lengths[1])
        bool2 = np.allclose(side_lengths[1], side_lengths[2])
        if not (bool1 and bool2):
            raise ValueError(
                "Rectangle does not have equal adjacent sides."
                "It cannot be a Square.")


class Trapezoid(Quadrilateral):
    """Trapezoid defined as a quadrilateral with at least one pair of parallel
    opposite sides.
    """

    def __init__(self, points: List[Point], lines: Optional[List[Line]] = None,
                 tag: Optional[int] = None) -> None:
        """Initialize a Trapezoid object.

        Parameters
        ----------
        points : List[Point]
            List of points defining the trapezoid.
        lines : List[Line], optional
            List of lines composing the trapezoid. By default None.
        tag : int, optional
            Unique identifier for the trapezoid. By default None.
        """
        super().__init__(points, lines, tag)
        self._is_trapezoid()

    def _is_trapezoid(self) -> None:
        """Check if the shape is a trapezoid.

        Raises
        ------
        ValueError
            If the shape is not a trapezoid.
        """
        # Check if at least one pair of opposite sides is parallel
        v1 = self.vertices[1] - self.vertices[0]
        v2 = self.vertices[2] - self.vertices[3]
        v3 = self.vertices[2] - self.vertices[1]
        v4 = self.vertices[3] - self.vertices[0]
        bool1 = np.allclose(np.cross(v1, v2), 0)
        bool2 = np.allclose(np.cross(v3, v4), 0)
        if not (bool1 or bool2):
            raise ValueError(
                "Quadrilateral does not have any parallel opposite sides."
                "It cannot be a trapezoid")
