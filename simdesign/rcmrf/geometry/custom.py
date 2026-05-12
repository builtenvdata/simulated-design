"""
Custom geometry module for defining frame structures from Excel input files.

This module provides the :class:`CustomGeometry` class, which reads structural
geometry data (points, lines, and rectangles) from a user-supplied Excel
workbook and builds a complete frame model via the base geometry framework.
"""
# Imports from installed packages
import pandas as pd
from pathlib import Path
from typing import Union

# Imports from geometry library
from .base import GeometryBase, Point, SystemGridData


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
    """
    xlsx_path: Union[str, Path]

    __str: str
    """The private attribute for string representation of the CustomGeometry.
    """

    def __init__(self, xlsx_path: Union[str, Path]) -> None:
        """
        Initialize the CustomGeometry with data from the specified Excel file.

        Parameters
        ----------
        xlsx_path : Union[str, Path]
            The path to the Excel file containing the frame data.
        """
        tag = Path(xlsx_path).name.removeprefix(".xlsx")
        self.__str = f"CustomGeometry-{tag}"
        self.xlsx_path = xlsx_path
        self._build_base()
        self._check_for_any_not_allowed_lines()
        self._check_for_any_not_allowed_rectangles()

    def __str__(self) -> str:
        """
        Return a string representation of the CustomGeometry.

        Returns
        -------
        str
            String representation of the CustomGeometry.
        """
        return self.__str

    def _initialise_points(self) -> None:
        """
        Read point data from the Excel workbook and populate ``self.points``.

        Reads the ``POINTS_SHEET`` worksheet, derives grid indices from the
        unique coordinate values, and creates a
        :class:`~simdesign.utils.mesh.Point`
        for each row. Sets ``self.system_grid_data`` once all points are built.
        """
        # Get the data from excel sheet containing points tags and coordinates
        df = pd.read_excel(self.xlsx_path, sheet_name=self.POINTS_SHEET)
        # Set the grid coordinates
        unique_xs: list = (df['x-coord'].unique()).tolist()
        unique_ys: list = (df['y-coord'].unique()).tolist()
        unique_zs: list = (df['z-coord'].unique()).tolist()
        # Start creating points
        for _, row in df.iterrows():
            coords = [float(row['x-coord']), float(row['y-coord']),
                      float(row['z-coord'])]
            i = float(unique_xs.index(coords[0]))
            j = float(unique_ys.index(coords[1]))
            k = float(unique_zs.index(coords[2]))
            tag = int(row['tag'])
            grid = [i, j, k]
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
        df = df.where(pd.notna(df), None)
        # Start creating lines
        for _, row in df.iterrows():
            tag = int(row['tag'])
            point1 = self.find_point_by_tag(row['point-1'])
            point2 = self.find_point_by_tag(row['point-2'])
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
        df = df.where(pd.notna(df), None)
        # Go through rectangle shapes
        for _, row in df.iterrows():
            # Find points on the rectangle
            tag = int(row['tag'])
            point1 = self.find_point_by_tag(row['point-1'])
            point2 = self.find_point_by_tag(row['point-2'])
            point3 = self.find_point_by_tag(row['point-3'])
            point4 = self.find_point_by_tag(row['point-4'])
            points = [point1, point2, point3, point4]
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
