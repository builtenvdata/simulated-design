"""
Custom geometry module for defining frame structures from Excel input files.

This module provides the :class:`CustomGeometry` class, which reads structural
geometry data (points, lines, and rectangles) from a user-supplied Excel
workbook and builds a complete frame model via the base geometry framework.
"""
# Imports from installed packages
import numpy as np
import pandas as pd
from pathlib import Path
from typing import Dict, List, Literal, Union

# Imports from geometry library
from .base import GeometryBase, Point, SystemGridData

# Imports from utils library
from ...utils.tags import TYPE_UNIT


# TODO: Use pydantic to set schema for CustomGeometry
class CustomGeometry(GeometryBase):
    """
    Class representing a custom frame structure.

    This class inherits from
    :class:`~simdesign.rcmrf.geometry.base.GeometryBase` and extends it to
    represent a custom frame structure. It initializes the frame with data from
    an Excel file specified by the provided path.

    Attributes
    ----------
    xlsx_path : str | Path
        The path to the Excel file containing the frame data.
    input_tags : Dict[str, Dict[int, int]]
        Tags assigned to the points, lines and rectangles of the workbook,
        keyed by object type ('points', 'lines', 'rectangles') and by workbook
        tag.
    """
    xlsx_path: Union[str, Path]
    input_tags: Dict[Literal['points', 'lines', 'rectangles'], Dict[int, int]]

    __str: str
    """The private attribute for string representation of the CustomGeometry.
    """

    def __init__(self, xlsx_path: Union[str, Path],
                 retag: bool = False) -> None:
        """
        Initialize the CustomGeometry with data from the specified Excel file.

        Parameters
        ----------
        xlsx_path : Union[str, Path]
            The path to the Excel file containing the frame data.
        retag : bool, optional
            If ``True``, the points, lines and rectangles are renumbered with
            the tag encoding of :mod:`simdesign.utils.tags`, so that their
            grid location and type can be read from their tags (see
            :meth:`retag`). If ``False``, the tags of the workbook are kept.
            By default ``False``.
        """
        tag = Path(xlsx_path).name.removeprefix(".xlsx")
        self.__str = f"CustomGeometry-{tag}"
        self.xlsx_path = xlsx_path
        # The workbook tags are used while reading the workbook
        self.encoded_tags = False
        self.input_tags = {'points': {}, 'lines': {}, 'rectangles': {}}
        self._build_base()
        self._check_for_any_not_allowed_lines()
        self._check_for_any_not_allowed_rectangles()
        if retag:
            new_tags = self.retag()
            self.input_tags = {
                name: {input_tag: new_tags[name][tag]
                       for input_tag, tag in tags.items()}
                for name, tags in self.input_tags.items()
            }
        else:
            self._check_tag_ranges()

    def __str__(self) -> str:
        """
        Return a string representation of the CustomGeometry.

        Returns
        -------
        str
            String representation of the CustomGeometry.
        """
        return self.__str

    @staticmethod
    def _check_tags(tags: List[int], name: str) -> None:
        """Check that the tags read from the workbook are unique.

        Parameters
        ----------
        tags : List[int]
            Tags read from the workbook.
        name : str
            Name of the objects, used in the error message.

        Raises
        ------
        ValueError
            If the tags are not unique.
        """
        if len(set(tags)) != len(tags):
            raise ValueError(f"Duplicate {name} tags in the workbook.")

    def _check_tag_ranges(self) -> None:
        """Check that the kept workbook tags can be used in the model.

        Raises
        ------
        ValueError
            If any point, line or rectangle tag is not in ``[0, 10**7)``,
            which is required by the node and sub-object tag encoding (see
            :mod:`simdesign.utils.tags`).
        """
        for name, tags in (('point', self.point_tags),
                           ('line', self.line_tags),
                           ('rectangle', self.rectangle_tags)):
            invalid = [tag for tag in tags if not 0 <= tag < TYPE_UNIT]
            if invalid:
                raise ValueError(
                    f"{name.capitalize()} tags must be in [0, {TYPE_UNIT}); "
                    f"invalid tags: {invalid}.")

    def _find_input_point(self, input_tag: int) -> Point:
        """Find a point by its workbook tag.

        Parameters
        ----------
        input_tag : int
            Tag of the point in the workbook.

        Returns
        -------
        Point
            The point with the specified workbook tag.

        Raises
        ------
        ValueError
            If there is no point with the specified tag in the workbook.
        """
        try:
            tag = self.input_tags['points'][int(input_tag)]
        except (KeyError, TypeError, ValueError):
            raise ValueError(
                f"Point {input_tag} is not defined in the workbook.") from None
        return self.find_point_by_tag(tag)

    def _initialise_points(self) -> None:
        """
        Read point data from the Excel workbook and populate ``self.points``.

        Reads the ``POINTS_SHEET`` worksheet, derives grid indices from the
        sorted unique coordinate values, and creates a
        :class:`~simdesign.utils.mesh.Point`
        for each row. Sets ``self.system_grid_data`` once all points are built.
        """
        # Get the data from excel sheet containing points tags and coordinates
        df = pd.read_excel(self.xlsx_path, sheet_name=self.POINTS_SHEET)
        self._check_tags(df['tag'].astype(int).tolist(), 'point')
        # Set the grid coordinates (sorted, as in SystemGridData)
        unique_xs = np.unique(df['x-coord'].astype(float)).tolist()
        unique_ys = np.unique(df['y-coord'].astype(float)).tolist()
        unique_zs = np.unique(df['z-coord'].astype(float)).tolist()
        # Start creating points
        for _, row in df.iterrows():
            coords = [float(row['x-coord']), float(row['y-coord']),
                      float(row['z-coord'])]
            i = unique_xs.index(coords[0])
            j = unique_ys.index(coords[1])
            k = unique_zs.index(coords[2])
            tag = int(row['tag'])
            if self.find_point_by_coordinates(coords):
                raise ValueError(
                    f"Point {tag} has the same coordinates as another point "
                    "in the workbook.")
            self.input_tags['points'][tag] = tag
            grid = [float(i), float(j), float(k)]
            point = Point(grid, coords, tag)
            self.points.append(point)
        # Set the system grid data
        self.system_grid_data = SystemGridData(self.points)

    def _initialise_lines(self) -> None:
        """
        Read line connectivity from the Excel workbook and populate frame
        lines.

        Reads the ``LINES_SHEET`` worksheet and calls :meth:`add_new_line` for
        each row, assigning the component type and section rotation angle.
        """
        # Get the data from excel sheet containing lines connectivity
        df = pd.read_excel(self.xlsx_path, sheet_name=self.LINES_SHEET)
        self._check_tags(df['tag'].astype(int).tolist(), 'line')
        df = df.where(pd.notna(df), None)
        # Start creating lines
        for _, row in df.iterrows():
            tag = int(row['tag'])
            point1 = self._find_input_point(row['point-1'])
            point2 = self._find_input_point(row['point-2'])
            if self.find_line_by_points([point1, point2]):
                raise ValueError(
                    f"Line {tag} overlaps another line in the workbook.")
            self.input_tags['lines'][tag] = tag
            rot_angle = float(row['sec-rotation'])
            component = row['component']
            if component:
                component = str(component).lower().capitalize()
            self.add_new_line([point1, point2], tag, component, rot_angle)

    def _initialise_rectangles(self) -> None:
        """
        Read rectangle data from the Excel workbook and populate floor slabs.

        Reads the ``RECTANGLES_SHEET`` worksheet and calls
        :meth:`add_new_rectangle` for each row, assigning the component type
        and infill strength.
        """
        # Dataframe containing rectangles of floor slabs
        df = pd.read_excel(self.xlsx_path, sheet_name=self.RECTANGLES_SHEET)
        self._check_tags(df['tag'].astype(int).tolist(), 'rectangle')
        df = df.where(pd.notna(df), None)
        # Go through rectangle shapes
        for _, row in df.iterrows():
            # Find points on the rectangle
            tag = int(row['tag'])
            points = [self._find_input_point(row[f'point-{n}'])
                      for n in range(1, 5)]
            if self.find_rectangle_by_points(points):
                raise ValueError(
                    f"Rectangle {tag} overlaps another rectangle in the "
                    "workbook.")
            self.input_tags['rectangles'][tag] = tag
            # Component type
            component = row['component']
            if component:
                component = str(component).lower().capitalize()
            # infill strength - type
            strength = row['infill-type']
            if strength:
                strength = str(strength).lower().capitalize()
            # Add new rectangle
            self.add_new_rectangle(points, tag, component, strength)
