"""This module provides the column class implementation for the ``eu_cdn``
design class in the BDIM layer.
"""
# Imports from installed packages
from math import ceil, pi

# Imports from the design class (eu_cdn) library
from .materials import Steel, Concrete

# Imports from bdim base library
from ..baselib.column import ColumnBase


class Column(ColumnBase):
    """Column implementation for design class ``eu_cdn``.

    This class extends ``ColumnBase`` by narrowing the attribute types
    and overriding design methods per RBA (1935).

    Attributes
    ----------
    steel : ~simdesign.rcmrf.bdim.eu_cdn.materials.Steel
        Steel material assigned to the column.
    concrete : ~simdesign.rcmrf.bdim.eu_cdn.materials.Concrete
        Concrete material assigned to the column.

    See Also
    --------
    :class:`~bdim.baselib.column.ColumnBase`
        Base class defining the core behaviour and configuration.

    Notes
    -----
    The design is based on the minimum reinforcemenet defined in RBA 1935.

    References
    ----------
    RBA (1935) Regulamento do Betão Armado.
    Decreto N.° 25:948, Lisbon, Portugal.
    """
    steel: Steel
    concrete: Concrete

    @property
    def rhol_max(self) -> float:
        """Maximum allowed longitudinal reinforcement ratio.

        Returns
        -------
        float
            Maximum allowed longitudinal reinforcement ratio.

        Notes
        -----
        Based on the Article 38 of RBA (1935).
        """
        return 0.06

    @property
    def rhol_min(self) -> float:
        """Minimum allowed longitudinal reinforcement ratio.

        Returns
        -------
        float
            Minimum allowed longitudinal reinforcement ratio.

        Notes
        -----
        Computed per Article 38 of RBA (1935).
        """
        ratio = 0.005 + 0.0006 * (self.line.length / min(self.bx, self.by) - 5)
        if ratio < 0.005:
            return 0.005
        elif ratio > 0.008:
            return 0.008
        else:
            return ratio

    def predesign_section_dimensions(self) -> None:
        """Make an initial guess for column section dimensions.

        Notes
        -----
        This method overrides ``ColumnBase.predesign_section_dimensions``
        with the following changes:

        - For rectangular sections, the longer dimension is no longer
          required to be twice the shorter one.
        """
        # Initial guess for column concrete area
        min_area = self.pre_Nd / self.fcd
        # Determine initial dimensions
        if self.section == 1:  # Square section
            self.bx = (min_area**0.5)
            self.by = (min_area**0.5)
        elif self.section == 2:  # Rectangular section
            if self.orient == "x":  # Longer dimension is bx
                self.by = self.min_b
                self.bx = min_area / self.min_b
            elif self.orient == "y":  # Longer dimension is by
                self.bx = self.min_b
                self.by = min_area / self.min_b
        # Check against minimum dimensions
        self.bx = max(ceil(20 * self.bx) / 20, self.min_b)
        self.by = max(ceil(20 * self.by) / 20, self.min_b)

    def apply_section_compatibility(self) -> None:
        """Modify section dimensions for compatibility with section type.

        This method is used in design iterations while increasing section
        dimensions.

        Notes
        -----
        This method overrides ``ColumnBase.apply_section_compatibility``
        with the following changes:

        - For rectangular sections, the longer dimension is no longer
          required to be twice the shorter one.
        """
        if self.section == 1:  # Square section
            # Make both dimensions equal to their maximum
            self.bx = ceil(20 * max(self.bx, self.by)) / 20
            self.by = ceil(20 * max(self.bx, self.by)) / 20
        elif self.section == 2:  # Rectangular section
            pass

    def verify_section_adequacy(self) -> None:
        """Verify the adequacy of section dimensions for design forces.

        Notes
        -----
        Adequacy is assessed solely against the maximum allowed dimension
        ``max_b``. No minimum dimension check is performed in this override.
        """
        # Only adequacy check is maximum dimensions
        if self.bx > self.max_b:
            self.ok_x = False
        else:
            self.ok_x = True
        if self.by > self.max_b:
            self.ok_y = False
        else:
            self.ok_y = True

    def compute_required_longitudinal_reinforcement(self) -> None:
        """Compute the required longitudinal reinforcement for design forces.

        Notes
        -----
        Design is based on the minimum reinforcement requirement from
        ``rhol_min``, applied to the gross section area ``Ag``.
        """
        # Design is based on minimum reinforcement requirement
        Asl_min = self.rhol_min * self.Ag
        Aslx = (0.5**2) * Asl_min
        Asly = (0.5**2) * Asl_min
        if self.section == 1:  # Square section
            pass
        elif self.section == 2:  # Rectangular section
            bx_by_ratio = self.bx / self.by
            if 0.8 < bx_by_ratio < 1.2:  # dims are close
                pass  # use the same reinf. area
            elif bx_by_ratio >= 1.2:  # bx is much larger
                Aslx = 0.33 * Asl_min
                Asly = 0.17 * Asl_min
            elif bx_by_ratio <= 0.8:  # by is much larger
                Aslx = 0.17 * Asl_min
                Asly = 0.33 * Asl_min
        # Save required reinforcement
        self.Aslx_req = Aslx
        self.Asly_req = Asly

    def compute_required_transverse_reinforcement(self) -> None:
        """Compute the required transverse reinforcement for design forces.

        Notes
        -----
        The values computed here represent default geometric minimums
        and they are not directly prescribed by RBA (1935).
        """
        sbh = 0.5  # stirrup spacing
        dbh = 0.006  # stirrup diameter
        nlegs = 2  # number of legs
        Ash_sbh_min = nlegs * (pi * 0.25 * dbh**2) / sbh
        self.Ashx_sbh_req = Ash_sbh_min
        self.Ashy_sbh_req = Ash_sbh_min
