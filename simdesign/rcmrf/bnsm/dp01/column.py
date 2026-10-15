"""This module provides the column class implementation for the ``DP01`` model
in the BNSM layer.
"""
# Imports from installed packages
import openseespy.opensees as ops
from typing import List, Literal

# Imports from bnsm base library
from ..baselib.column import ColumnBase

# Imports from utils library
from ....utils.misc import round_list


class Column(ColumnBase):
    """Column implementation for the ``DP01`` model.

    This class directly uses the behaviour defined in ``ColumnBase``, except
    for the cracked elastic section (see ``_get_elastic_sec_inputs``) and the
    elastic materials of the hinge sections.

    The hinge sections have elastic materials in the degrees of freedom
    without a hinge (axial and torsion), with the properties of the elastic
    section, instead of rigid ones. With ``HingeRadau`` integration, the
    hinge sections carry the elastic flexibility over the plastic hinge
    lengths, which rigid materials would leave out.

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.baselib.column.ColumnBase`
        Base class defining the core behaviour and configuration.
    """

    def add_to_ops(self) -> None:
        """Adds column components to the OpenSees domain
        (i.e, column element and nodes).
        """
        # Create the elastic materials of the hinge sections
        for mat_inputs in self._get_hinge_elastic_mat_inputs():
            ops.uniaxialMaterial(*mat_inputs)
        super().add_to_ops()

    def to_py(self) -> List[str]:
        """Gets the Python commands to construct column components in OpenSees
        domain (i.e, column element and nodes).

        Returns
        -------
        List[str]
            List of Python commands for constructing the components of column
            object in OpenSees.
        """
        content = super().to_py()
        # Create the elastic materials of the hinge sections
        idx = content.index('# Create element sections')
        for mat_inputs in reversed(self._get_hinge_elastic_mat_inputs()):
            mat_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in mat_inputs
            )
            content.insert(idx, f"ops.uniaxialMaterial({mat_inputs})")

        return content

    def to_tcl(self) -> List[str]:
        """Gets the Tcl commands to construct column components in OpenSees
        domain (i.e, column element and nodes).

        Returns
        -------
        List[str]
            List of Tcl commands for constructing the components of column
            object in OpenSees.
        """
        content = super().to_tcl()
        # Create the elastic materials of the hinge sections
        idx = content.index('# Create element sections')
        for mat_inputs in reversed(self._get_hinge_elastic_mat_inputs()):
            mat_inputs = ' '.join(f"{item}" for item in mat_inputs)
            content.insert(idx, f"uniaxialMaterial {mat_inputs}")

        return content

    def _get_inelastic_sec_inputs(self) -> List[str | int]:
        """Retrieves inputs for inelastic aggregated column section.

        Returns
        -------
        List[str | int]
            List of inputs for inelastic aggregated column section, with
            elastic P and T materials.
        """
        sec_inputs = super()._get_inelastic_sec_inputs()
        sec_inputs[2], sec_inputs[12] = self.p_mat_tag, self.t_mat_tag

        return sec_inputs

    def _get_elastic_sec_inputs(self) -> List[str | float | int]:
        """Retrieves elastic column section inputs.

        Returns
        -------
        List[str | float | int]
            List of elastic column section inputs.

        Notes
        -----
        The hinges carry the part of the yield rotation that the elastic
        interior does not (see ``_get_phiy_adjusted``). With ``cracked`` True,
        the moments of inertia are therefore at least
        ``_get_min_interior_I``, so that the elastic interior is not more
        flexible than the member at yield.
        """
        sec_inputs = super()._get_elastic_sec_inputs()
        if self.cracked is True:
            sec_inputs[4] = max(sec_inputs[4], self._get_min_interior_I('x'))
            sec_inputs[5] = max(sec_inputs[5], self._get_min_interior_I('y'))

        return round_list(sec_inputs)

    def _get_min_interior_I(self, axis: Literal['x', 'y']) -> float:
        """Gets the smallest moment of inertia of the elastic interior for
        which the member does not exceed the yield rotation at yielding.

        Parameters
        ----------
        axis : Literal['x', 'y']
            The local axis considered for the calculations.

        Returns
        -------
        float
            ``My·Ls/(3·E·theta_y)`` around `axis`. With a larger moment of
            inertia, the elastic interior gives at most ``theta_y``, and the
            hinges the rest (see ``_get_phiy_adjusted``).
        """
        props = self._get_rot_hinge_props(axis)
        My, theta_y = abs(props[1]), abs(props[4])
        ls = self.clear_length / 2  # Shear span, as in _get_phiy_adjusted
        return float(My * ls / (3 * theta_y) / self.Ecm_q)
