"""This module provides the beam class implementation for the ``CP01`` model in
the BNSM layer.
"""
# Imports from installed packages
import openseespy.opensees as ops
from typing import Tuple, List

# Imports from bnsm base library
from ..baselib.beam import BeamBase, HYSTERETIC_PARAMETERS
from .column import STIFF_INTERIOR_FACTOR

# Imports from utils library
from ....utils.misc import round_list, PRECISION
from ....utils.tags import sub_tag


class Beam(BeamBase):
    """Beam implementation for the ``CP01`` model.

    The beam is modeled using a concentrated plasticity approach. Plastic
    rotations are concentrated at the element ends via
    ``beamIntegration('ConcentratedPlasticity', ...)`` (end hinge integration
    points with an elastic interior region), while the element formulation is
    provided by ``BeamBase``.

    End-hinge flexural behaviour about the local z-axis (Mz) is defined using a
    uniaxial ``Hysteretic`` material, expressed in terms of bending moment vs.
    chord rotation of the whole member (the yield rotation includes the
    elastic deformations). The elastic interior is therefore nearly rigid in
    flexure about local-z (``STIFF_INTERIOR_FACTOR``), and the springs carry
    the whole flexural flexibility.

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.baselib.beam.BeamBase`
        Base beam definition extended by this class.
    """

    def _get_mz_mat_inputs(self) -> Tuple[List[str | float | int],
                                          List[str | float | int]]:
        """Retrieves the material inputs defining the flexural behaviour
        around local-z for the plastic hinge.

        Returns
        -------
        hinge_i_mat_inputs : List[str | float | int]
            Hysteretic material model inputs for hinge at the start section.
        hinge_j_mat_inputs : List[str | float | int]
            Hysteretic material model inputs for hinge at the end section.
        """
        # Backbone of the plastic hinges
        (
            _, My_neg, Mc_neg, Mr_neg,
            theta_y_neg, theta_cap_pl_neg, theta_pc_neg,
            _, My_pos, Mc_pos, Mr_pos,
            theta_y_pos, theta_cap_pl_pos, theta_pc_pos,
        ) = self._get_rot_hinge_props()

        # Rotation values
        theta_1_neg = theta_y_neg
        theta_2_neg = theta_1_neg + theta_cap_pl_neg
        theta_3_neg = theta_2_neg + theta_pc_neg
        theta_1_pos = theta_y_pos
        theta_2_pos = theta_1_pos + theta_cap_pl_pos
        theta_3_pos = theta_2_pos + theta_pc_pos

        # Material inputs
        hinge_i_mat_inputs = [
            'Hysteretic', self.mz_i_mat_tag,
            My_pos[0], theta_1_pos[0],
            Mc_pos[0], theta_2_pos[0],
            Mr_pos[0], theta_3_pos[0],
            -My_neg[0], -theta_1_neg[0],
            -Mc_neg[0], -theta_2_neg[0],
            -Mr_neg[0], -theta_3_neg[0],
            *HYSTERETIC_PARAMETERS
        ]
        hinge_j_mat_inputs = [
            'Hysteretic', self.mz_j_mat_tag,
            My_pos[-1], theta_1_pos[-1],
            Mc_pos[-1], theta_2_pos[-1],
            Mr_pos[-1], theta_3_pos[-1],
            -My_neg[-1], -theta_1_neg[-1],
            -Mc_neg[-1], -theta_2_neg[-1],
            -Mr_neg[-1], -theta_3_neg[-1],
            *HYSTERETIC_PARAMETERS
        ]

        # Rounding to precision
        hinge_i_mat_inputs = round_list(hinge_i_mat_inputs)
        hinge_j_mat_inputs = round_list(hinge_j_mat_inputs)

        return hinge_i_mat_inputs, hinge_j_mat_inputs

    @property
    def p_mat_tag(self) -> int:
        """Elastic material tag for the axial response (P) of the hinges."""
        return sub_tag(self.design.line.tag, 92)

    @property
    def my_mat_tag(self) -> int:
        """Elastic material tag for the flexural response about local-y (My)
        of the hinges."""
        return sub_tag(self.design.line.tag, 93)

    @property
    def t_mat_tag(self) -> int:
        """Elastic material tag for the torsional response (T) of the
        hinges."""
        return sub_tag(self.design.line.tag, 94)

    def add_to_ops(self) -> None:
        """Adds beam components to the OpenSees domain
        (i.e, beam element and nodes).
        """
        # Create the elastic materials of the hinge sections
        for mat_inputs in self._get_hinge_elastic_mat_inputs():
            ops.uniaxialMaterial(*mat_inputs)
        super().add_to_ops()

    def to_py(self) -> List[str]:
        """Gets the Python commands to construct beam components in OpenSees
        domain (i.e, beam element and nodes).

        Returns
        -------
        List[str]
            List of Python commands for constructing the components of beam
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
        """Gets the Tcl commands to construct beam components in OpenSees
        domain (i.e, beam element and nodes).

        Returns
        -------
        List[str]
            List of Tcl commands for constructing the components of beam
            object in OpenSees.
        """
        content = super().to_tcl()
        # Create the elastic materials of the hinge sections
        idx = content.index('# Create element sections')
        for mat_inputs in reversed(self._get_hinge_elastic_mat_inputs()):
            mat_inputs = ' '.join(f"{item}" for item in mat_inputs)
            content.insert(idx, f"uniaxialMaterial {mat_inputs}")

        return content

    def _get_hinge_elastic_mat_inputs(
        self
    ) -> List[List[str | float | int]]:
        """Retrieves the elastic material inputs of the hinge sections.

        Returns
        -------
        List[List[str | float | int]]
            Inputs of the elastic axial (EA), flexural about local-y (EIy) and
            torsional (GJ) materials.

        Notes
        -----
        ``ConcentratedPlasticity`` gives each hinge section a weight of one
        length unit and removes the same length from the elastic interior.
        The hinge sections therefore carry the elastic flexibility of that
        length. With rigid materials, the axial stiffness becomes EA/(L-2),
        which is negative for clear lengths below 2 m.
        """
        return [
            round_list(['Elastic', self.p_mat_tag,
                        self.Ecm_q * self.design.Ag]),
            round_list(['Elastic', self.my_mat_tag,
                        self.Ecm_q * self.design.Iy]),
            round_list(['Elastic', self.t_mat_tag,
                        self.Gcm_q * self.design.J])
        ]

    def _get_inelastic_sec_i_inputs(self) -> List[str | int]:
        """Retrieves inputs for inelastic beam section at ith end.

        Returns
        -------
        List[str | int]
            List of inputs for inelastic beam section at ith end, with
            elastic My, P and T materials.
        """
        sec_inputs = super()._get_inelastic_sec_i_inputs()
        sec_inputs[6], sec_inputs[10], sec_inputs[12] = \
            self.my_mat_tag, self.p_mat_tag, self.t_mat_tag

        return sec_inputs

    def _get_inelastic_sec_j_inputs(self) -> List[str | int]:
        """Retrieves inputs for inelastic beam section at jth end.

        Returns
        -------
        List[str | int]
            List of inputs for inelastic beam section at jth end, with
            elastic My, P and T materials.
        """
        sec_inputs = super()._get_inelastic_sec_j_inputs()
        sec_inputs[6], sec_inputs[10], sec_inputs[12] = \
            self.my_mat_tag, self.p_mat_tag, self.t_mat_tag

        return sec_inputs

    def _get_elastic_sec_inputs(self) -> List[str | int | float]:
        """Retrieves elastic beam section inputs.

        Returns
        -------
        List[str | int | float]
            List of elastic beam section inputs.

        Notes
        -----
        The moment of inertia about local-z (Iz) is multiplied by
        ``STIFF_INTERIOR_FACTOR``. The backbone rotations are chord rotations
        of the whole member, so the springs carry the whole flexural
        flexibility. The weak-axis flexure (Iy) has no spring and keeps its
        elastic stiffness.
        """
        sec_inputs = super()._get_elastic_sec_inputs()
        sec_inputs[4] = round(sec_inputs[4] * STIFF_INTERIOR_FACTOR, PRECISION)

        return sec_inputs

    def _get_int_inputs(self) -> List[str | float]:
        """Retrieves beam integration inputs.

        Returns
        -------
        List[float]
            List of beam integration inputs.
        """
        int_inputs = [
            'ConcentratedPlasticity',
            self.int_tag, self.inelastic_sec_i_tag,
            self.inelastic_sec_j_tag, self.elastic_sec_tag
        ]

        return int_inputs
