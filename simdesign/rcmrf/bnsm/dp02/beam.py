"""This module provides the beam class implementation for the ``DP02`` model in
the BNSM layer.
"""
# Imports from installed packages
import openseespy.opensees as ops
from typing import List, Literal, Tuple

# Imports from bnsm base library
from ..baselib.beam import BeamBase

# Imports from utils library
from ....utils.units import MPa
from ....utils.misc import round_list
from ....utils.tags import sub_tag


class Beam(BeamBase):
    """Beam implementation for the ``DP02`` model.

    This class extends ``BeamBase`` with a force-based beam-column
    formulation and lumped plasticity end hinges following the modelling
    strategy in O'Reilly (2016).

    The hinge sections have elastic materials in the degrees of freedom
    without a hinge (axial, torsion and flexure about local-y), with the
    properties of the elastic section, instead of rigid ones. With
    ``HingeRadau`` integration, the hinge sections carry the elastic
    flexibility over the plastic hinge lengths, which rigid materials would
    leave out. The moment-curvature hinges do not include shear deformation,
    so all sections have an elastic shear material (see
    ``_get_shear_mat_inputs``).

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.baselib.beam.BeamBase`
        Base beam definition extended by this class.
    """

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the Beam object (see ``BeamBase``), with the
        yield point of the plastic hinges from section analysis, consistent
        with the cracked-section method.
        """
        super().__init__(*args, **kwargs)
        self.yield_mom_curv = 'analytical'
        # Update the cracked-section properties for the section yield point
        self._set_cracked_properties()

    @property
    def Ecm_q(self) -> float:
        """
        Returns
        -------
        float
            Elastic young's modulus of concrete (in base units).

        References
        ----------
        Collins, M. P., & Mitchell, D. (1997). *Prestressed concrete
        structures*. Prentice Hall.
        """
        # Use quality adjusted elastic youngs modulus
        fc_mpa = self.design.fc_q / MPa  # convert to MPa
        return (3320 * (fc_mpa**0.5) + 6900) * MPa  # Eqn. 3-3

    @property
    def mz_i_mat_tag_(self) -> int:
        """Pinching4 material tag for the *i-end* flexural hinge about local-z
        (Mz)."""
        return sub_tag(self.design.line.tag, 90)

    @property
    def mz_i_mat_tag(self) -> int:
        """MinMax Material tag for the *i-end* hinge about local-z (Mz)."""
        return sub_tag(self.design.line.tag, 91)

    @property
    def mz_j_mat_tag_(self) -> int:
        """Pinching4 material tag for the *J-end* flexural hinge about local-z
        (Mz)."""
        return sub_tag(self.design.line.tag, 92)

    @property
    def mz_j_mat_tag(self) -> int:
        """MinMax Material tag for the *J-end* hinge about local-z (Mz)."""
        return sub_tag(self.design.line.tag, 93)

    @property
    def shear_mat_tag(self) -> int:
        """Elastic material tag for the shear response (Vy and Vz) of the
        sections."""
        return sub_tag(self.design.line.tag, 97)

    @property
    def interior_sec_tag(self) -> int:
        """Section tag for the elastic interior section aggregated with the
        shear material."""
        return sub_tag(self.design.line.tag, 93)

    def add_to_ops(self) -> None:
        """Adds beam components to the OpenSees domain
        (i.e, elastic beam element and nodes).
        """
        # Define geometric transformation
        ops.geomTransf(*self._get_geo_transf_inputs())

        # Create the section materials
        mz_i, mz_j, mz_minmax_i, mz_minmax_j = self._get_mz_mat_inputs()
        ops.uniaxialMaterial(*mz_i)
        ops.uniaxialMaterial(*mz_j)
        ops.uniaxialMaterial(*mz_minmax_i)
        ops.uniaxialMaterial(*mz_minmax_j)

        # Elastic materials of the hinge sections
        for mat_inputs in self._get_hinge_elastic_mat_inputs():
            ops.uniaxialMaterial(*mat_inputs)
        ops.uniaxialMaterial(*self._get_shear_mat_inputs())

        # Create element sections
        ops.section(*self._get_elastic_sec_inputs())
        ops.section(*self._get_inelastic_sec_i_inputs())
        ops.section(*self._get_inelastic_sec_j_inputs())
        ops.section(*self._get_interior_sec_inputs())

        # Create beam integration
        ops.beamIntegration(*self._get_int_inputs())

        # Create the element
        ops.element(*self._get_ele_inputs())

    def to_py(self) -> List[str]:
        """Gets the Python commands to construct beam components in OpenSees
        domain (i.e, beam element and nodes).

        Returns
        -------
        List[str]
            List of Python commands for constructing the components of beam
            object in OpenSees.
        """
        # Define geometric transformation
        content = ['# Create geometric transformation']
        transf_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_geo_transf_inputs()
        )
        content.append(f"ops.geomTransf({transf_inputs})")

        # Create the section materials
        content.append('# Create uniaxial materials')
        mz_i, mz_j, minmax_i, minmax_j = self._get_mz_mat_inputs()
        mz_mat_inputs_i = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in mz_i
        )
        mz_mat_inputs_j = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in mz_j
        )
        mz_minmax_mat_inputs_i = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in minmax_i
        )
        mz_minmax_mat_inputs_j = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in minmax_j
        )
        content.append(f"ops.uniaxialMaterial({mz_mat_inputs_i})")
        content.append(f"ops.uniaxialMaterial({mz_mat_inputs_j})")
        content.append(f"ops.uniaxialMaterial({mz_minmax_mat_inputs_i})")
        content.append(f"ops.uniaxialMaterial({mz_minmax_mat_inputs_j})")

        # Elastic materials of the hinge sections
        for mat_inputs in self._get_hinge_elastic_mat_inputs():
            mat_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in mat_inputs
            )
            content.append(f"ops.uniaxialMaterial({mat_inputs})")
        shear_mat = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_shear_mat_inputs()
        )
        content.append(f"ops.uniaxialMaterial({shear_mat})")

        # Create sections
        content.append('# Create element sections')
        elastic_sec_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_elastic_sec_inputs()
        )
        inelastic_sec_i_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_inelastic_sec_i_inputs()
        )
        inelastic_sec_j_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_inelastic_sec_j_inputs()
        )
        content.append(f"ops.section({elastic_sec_inputs})")
        content.append(f"ops.section({inelastic_sec_i_inputs})")
        content.append(f"ops.section({inelastic_sec_j_inputs})")
        interior_sec_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_interior_sec_inputs()
        )
        content.append(f"ops.section({interior_sec_inputs})")

        # Create beam integration
        content.append('# Create integration scheme')
        int_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_int_inputs()
        )
        content.append(f"ops.beamIntegration({int_inputs})")

        # Create column element
        content.append('# Create element')
        ele_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_ele_inputs()
        )
        content.append(f"ops.element({ele_inputs})")

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
        # Define geometric transformation
        content = ['# Create geometric transformation']
        transf_inputs = ' '.join(f"{item}" for item in
                                 self._get_geo_transf_inputs())
        content.append(f"geomTransf {transf_inputs}")

        # Create the section materials
        content.append('# Create uniaxial materials')
        mz_i, mz_j, minmax_i, minmax_j = self._get_mz_mat_inputs()
        mz_mat_inputs_i = ' '.join(f"{item}" for item in mz_i)
        mz_mat_inputs_j = ' '.join(f"{item}" for item in mz_j)
        mz_minmax_mat_inputs_i = ' '.join(f"{item}" for item in minmax_i)
        mz_minmax_mat_inputs_j = ' '.join(f"{item}" for item in minmax_j)
        content.append(f"uniaxialMaterial {mz_mat_inputs_i}")
        content.append(f"uniaxialMaterial {mz_mat_inputs_j}")
        content.append(f"uniaxialMaterial {mz_minmax_mat_inputs_i}")
        content.append(f"uniaxialMaterial {mz_minmax_mat_inputs_j}")

        # Elastic materials of the hinge sections
        for mat_inputs in self._get_hinge_elastic_mat_inputs():
            mat_inputs = ' '.join(f"{item}" for item in mat_inputs)
            content.append(f"uniaxialMaterial {mat_inputs}")
        shear_mat = ' '.join(
            f"{item}" for item in self._get_shear_mat_inputs())
        content.append(f"uniaxialMaterial {shear_mat}")

        # Create sections
        content.append('# Create element sections')
        elastic_sec_inputs = ' '.join(
            f"{item}" for item in self._get_elastic_sec_inputs())
        inelastic_sec_i_inputs = ' '.join(
            f"{item}" for item in self._get_inelastic_sec_i_inputs())
        inelastic_sec_j_inputs = ' '.join(
            f"{item}" for item in self._get_inelastic_sec_j_inputs())
        content.append(f"section {elastic_sec_inputs}")
        content.append(f"section {inelastic_sec_i_inputs}")
        content.append(f"section {inelastic_sec_j_inputs}")
        interior_sec_inputs = ' '.join(
            f"{item}" for item in self._get_interior_sec_inputs())
        content.append(f"section {interior_sec_inputs}")

        # Create beam integration
        content.append('# Create integration scheme')
        int_inputs = ' '.join(
            f"{item}" for item in self._get_int_inputs())
        content.append(f"beamIntegration {int_inputs}")

        # Create column element
        content.append('# Create element')
        ele_inputs = ' '.join(
            f"{item}" for item in self._get_ele_inputs())
        content.append(f"element {ele_inputs}")

        return content

    def _get_inelastic_sec_i_inputs(self) -> List[str | int]:
        """Retrieves inputs for inelastic beam section at ith end.

        Returns
        -------
        List[str | int]
            List of inputs for inelastic beam section at ith end, with
            elastic Vy, My, Vz, P and T materials.
        """
        sec_inputs = super()._get_inelastic_sec_i_inputs()
        sec_inputs[6], sec_inputs[10], sec_inputs[12] = \
            self.my_mat_tag, self.p_mat_tag, self.t_mat_tag
        sec_inputs[4], sec_inputs[8] = self.shear_mat_tag, self.shear_mat_tag

        return sec_inputs

    def _get_inelastic_sec_j_inputs(self) -> List[str | int]:
        """Retrieves inputs for inelastic beam section at jth end.

        Returns
        -------
        List[str | int]
            List of inputs for inelastic beam section at jth end, with
            elastic Vy, My, Vz, P and T materials.
        """
        sec_inputs = super()._get_inelastic_sec_j_inputs()
        sec_inputs[6], sec_inputs[10], sec_inputs[12] = \
            self.my_mat_tag, self.p_mat_tag, self.t_mat_tag
        sec_inputs[4], sec_inputs[8] = self.shear_mat_tag, self.shear_mat_tag

        return sec_inputs

    def _get_shear_mat_inputs(self) -> List[str | float | int]:
        """Retrieves the inputs of the elastic shear material of the
        sections.

        Returns
        -------
        List[str | float | int]
            Inputs of an ``Elastic`` material with the gross shear stiffness,
            ``G (5/6) A``, used for both Vy and Vz.

        Notes
        -----
        The moment-curvature hinges and the elastic section do not include
        shear deformation. Without the shear material, the beams would have
        no shear flexibility.
        """
        GAv = self.Gcm_q * (5 / 6) * self.design.Ag
        return round_list(['Elastic', self.shear_mat_tag, GAv])

    def _get_interior_sec_inputs(self) -> List[str | int]:
        """Retrieves the inputs of the elastic interior section aggregated
        with the shear material.

        Returns
        -------
        List[str | int]
            Inputs of the ``Aggregator`` section with the shear material in
            Vy and Vz and the elastic section.
        """
        return ['Aggregator', self.interior_sec_tag,
                self.shear_mat_tag, 'Vy', self.shear_mat_tag, 'Vz',
                '-section', self.elastic_sec_tag]

    def _get_int_inputs(self) -> List[str | int | float]:
        """Retrieves beam integration inputs.

        Returns
        -------
        List[str | int | float]
            List of beam integration inputs, with the interior section
            aggregated with the shear material.
        """
        int_inputs = super()._get_int_inputs()
        int_inputs[-1] = self.interior_sec_tag

        return int_inputs

    def _get_ele_inputs(self) -> List[str | int | float]:
        """Retrieves beam element inputs.

        Returns
        -------
        List[str | int | float]
            List of beam element inputs.
        """
        ele_inputs = [
            'forceBeamColumn', self.design.line.tag,
            self.ele_node_i.tag, self.ele_node_j.tag,
            self.geo_transf_tag, self.int_tag
        ]

        return ele_inputs

    def _get_mz_mat_inputs(
        self
    ) -> Tuple[List[str | float | int], List[str | float | int],
               List[str | float | int], List[str | float | int]]:
        """Retrieves the material inputs defining the flexural behaviour
        around local-z for the plastic hinge of forceBeamColumn element.

        Returns
        -------
        flex_inputs_i : List[str | float | int]
            Inputs for the Pinching4 material at the i-end section.
        flex_inputs_j : List[str | float | int]
            Inputs for the Pinching4 material at the j-end section.
        minmax_inputs_i : List[str | float | int]
            Inputs for the MinMax wrapper material at the i-end section.
        minmax_inputs_j : List[str | float | int]
            Inputs for the MinMax wrapper material at the j-end section.

        References
        ----------
        O'Reilly, G. J. (2016). Performance-based seismic assessment and
        retrofit of existing RC frame buildings in Italy (Doctoral
        dissertation, IUSS Pavia).
        """
        # Get pinching4 backbone parameters
        backbone_pos_i, phi_max_pos_i = self._get_backbone('positive', 'i')
        backbone_neg_i, phi_max_neg_i = self._get_backbone('negative', 'i')
        backbone_pos_j, phi_max_pos_j = self._get_backbone('positive', 'j')
        backbone_neg_j, phi_max_neg_j = self._get_backbone('negative', 'j')

        # Unloading/Reloading parameters from O'Reilly 2016
        # Ratio of maximum deformation at which reloading begins
        rDispP, rDispN = 0.1, 0.1  # from Table 2.2. in O'Reilly 2016
        # Ratio of envelope force at which reloading begins
        rForceP, rForceN = 0.4, 0.4  # from Table 2.2. in O'Reilly 2016
        # Ratio of monotonic strength developed upon unloading
        uForceP, uForceN = -0.8, -0.8  # from Table 2.2. in O'Reilly 2016
        # Coefficients for Unloading Stiffness degradation
        gK1, gK2, gK3, gK4, gKLim = 0.0, 0.0, 0.0, 0.0, 0.0  # No degradation
        # gK1, gK2, gK3, gK4, gKLim = 1.0, 0.2, 0.3, 0.2, 0.9  # OpenSees ex.
        # gK1, gK2, gK3, gK4, gKLim = 0.0, 0.1, 0.0, 0.0, 0.2  # ATC62, Spring1
        # Coefficients for Reloading Stiffness degradation
        gD1, gD2, gD3, gD4, gDLim = 0.0, 0.0, 0.0, 0.0, 0.0  # No degradation
        # gD1, gD2, gD3, gD4, gDLim = 0.5, 0.5, 2.0, 2.0, 0.5  # OpenSees ex.
        # gD1, gD2, gD3, gD4, gDLim = 0.0, 0.1, 0.0, 0.0, 0.2  # ATC62, Spring1
        # Coefficients for Strength degradation
        gF1, gF2, gF3, gF4, gFLim = 0.0, 0.0, 0.0, 0.0, 0.0  # No degradation
        # gF1, gF2, gF3, gF4, gFLim = 1.0, 0.0, 1.0, 1.0, 0.9  # OpenSees ex.
        # gF1, gF2, gF3, gF4, gFLim = 0.0, 0.4, 0.0, 0.4, 0.9  # ATC62, Spring1
        # Cyclic energy dissipation factor (E_cyclic=gE*E_monotonic)
        gE = 10.0  # suitable for low to moderate ductility
        # gE = 10.0  # No degradation
        # Damage type
        dmgType = "energy"
        params = [
            rDispP, rForceP, uForceP,
            rDispN, rForceN, uForceN,
            gK1, gK2, gK3, gK4, gKLim,
            gD1, gD2, gD3, gD4, gDLim,
            gF1, gF2, gF3, gF4, gFLim,
            gE, dmgType
        ]

        # Pinching4 material inputs for the ith end section
        flex_inputs_i = (
            ["Pinching4", self.mz_i_mat_tag_]
            + backbone_pos_i
            + backbone_neg_i
            + params
        )
        # MinMax material inputs for the ith end section
        minmax_inputs_i = [
            'MinMax', self.mz_i_mat_tag, self.mz_i_mat_tag_,
            '-min', phi_max_neg_i, '-max', phi_max_pos_i
        ]
        # Pinching4 material inputs for the jth end section
        flex_inputs_j = (
            ["Pinching4", self.mz_j_mat_tag_]
            + backbone_pos_j
            + backbone_neg_j
            + params
        )
        # MinMax material inputs for the ith end section
        minmax_inputs_j = [
            'MinMax', self.mz_j_mat_tag, self.mz_j_mat_tag_,
            '-min', phi_max_neg_j, '-max', phi_max_pos_j
        ]

        # Rounding to precision
        flex_inputs_i = round_list(flex_inputs_i)
        flex_inputs_j = round_list(flex_inputs_j)
        minmax_inputs_i = round_list(minmax_inputs_i)
        minmax_inputs_j = round_list(minmax_inputs_j)

        return flex_inputs_i, flex_inputs_j, minmax_inputs_i, minmax_inputs_j

    def _get_backbone(self, direction: Literal['negative', 'positive'],
                      end_section: Literal['i', 'j']
                      ) -> Tuple[List[float], float]:
        """Compute moment-curvature backbone parameters for an end section.

        Parameters
        ----------
        direction : Literal['negative', 'positive']
            Bending direction. The returned moment/curvature values follow this
            sign convention (negative direction returns negative values).
        end_section : Literal['i', 'j']
            Element end where the backbone is computed.

        Returns
        -------
        backbone : List[float]
            Ordered moment-curvature backbone points.
        phi_max : float
            Curvature limit at which exhaustion is defined.

        References
        ----------
        Priestley, M. J. N., Calvi, G. M., & Kowalsky, M. J. (2007).
        *Displacement-based seismic design of structures*. IUSS Press.

        Collins, M. P., & Mitchell, D. (1997). *Prestressed concrete
        structures*. Prentice Hall.

        O'Reilly, G. J. (2016). Performance-based seismic assessment and
        retrofit of existing RC frame buildings in Italy (Doctoral
        dissertation, IUSS Pavia).
        """
        # Index for the specified end section
        if end_section == 'i':
            idx = 0
        elif end_section == 'j':
            idx = -1
        # Section properties
        h = self.design.h
        Ag = self.design.Ag
        cv = float(self.design.cover_q)
        dbl_b1 = float(self.design.dbl_b1_q[idx])
        dbl_b2 = float(self.design.dbl_b2_q[idx])
        dbl_t1 = float(self.design.dbl_t1_q[idx])
        dbl_t2 = float(self.design.dbl_t2_q[idx])
        dbh = float(self.design.dbh_q[idx])
        P = 0.0
        nu = P / Ag

        # Reinforcement layout (top to bottom)
        yt1 = cv + dbh + dbl_t1 / 2
        yt2 = cv + dbh + dbl_t2 / 2
        yb1 = h - (cv + dbh + dbl_b1 / 2)
        yb2 = h - (cv + dbh + dbl_b2 / 2)
        # Set the layer distances and total areas
        if direction == 'positive':  # Top section is under compression
            y_layers = [yt2, yt1, yb1, yb2]
        elif direction == 'negative':  # Bottom section is under compression
            y_layers = [h-yb2, h-yb1, h-yt1, h-yt2]  # compression comes first
        # Sort the distances in ascending order
        y_layers = sorted(y_layers)

        # Moment, curvature, and neutral axis depth at yielding
        My, phi_y, cy = (
            x[idx] for x in self._get_my_phiy_analytical(direction)
        )
        # Capping to yield moment ratio
        Mc_My = 1.077  # O'Reilly 2016 - Eqn. 2.2
        # Ultimate to capping moment ratio
        Mu_Mc = 0.8  # 20% reduction - Fig. 2.2
        # Residual to capping moment ratio
        Mr_Mc = 0.1  # 10% assumed
        # Capping moment
        Mc = Mc_My * My
        # Ultimate moment
        Mu = Mu_Mc * Mc
        # Residual moment
        Mr = Mr_Mc * Mc

        # Ultimate curvature
        _nu = min(max(nu, 0.1), 0.25)  # dont extrapolate if 0.1>nu or nu>0.25
        mu_phi = 22.7 - 47.4 * _nu  # Eqn. 2.5
        phi_u = phi_y * mu_phi
        # Capping curvature
        app = -0.1437 * _nu - 0.0034  # Eqn. 2.6
        phi_c = phi_y * (mu_phi + (0.2 * Mc_My) / app)  # Eqn. 2.7
        # Residual curvature
        kpp = app * My / phi_y  # p32
        phi_r = phi_c + (Mr - Mc) / kpp  # Fig. 2.2

        # Rupture and buckling curvature limits, assuming the same yield N.A.
        dd = y_layers[-1]  # Distance from top fiber to bottom rebars
        dd_prime = y_layers[0]  # Distance from top fiber to top rebars
        yb = dd - cy  # rupture case (assuming c=cy - O'Reilly 2016)
        yt = cy - dd_prime  # buckling case (assuming c=cy - O'Reilly 2016)
        e_su = 0.08  # Rupture strain DBD book-p141 (conservative value)
        phi_max = e_su / max(1e-12, yt, yb)  # exhaustion curvature

        if direction == 'positive':
            backbone = [My, phi_y, Mc, phi_c, Mu, phi_u, Mr, phi_r]
        elif direction == 'negative':
            backbone = [-My, -phi_y, -Mc, -phi_c, -Mu, -phi_u, -Mr, -phi_r]
            phi_max = -1.0 * phi_max

        return backbone, phi_max
