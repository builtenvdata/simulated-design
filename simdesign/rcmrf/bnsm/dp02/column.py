"""This module provides the column class implementation for the ``DP02`` model
in the BNSM layer.
"""
# Imports from installed packages
import openseespy.opensees as ops
from typing import Literal, List, Tuple

# Imports from bnsm base library
from ..baselib.column import ColumnBase

# Imports from utils library
from ....utils.units import MPa
from ....utils.misc import round_list
from ....utils.tags import sub_tag


class Column(ColumnBase):
    """Column implementation for the ``DP02`` model.

    This class extends ``ColumnBase`` with a force-based beam-column
    formulation and lumped plasticity end hinges following the modelling
    strategy in O'Reilly (2016).

    The hinge sections have elastic materials in the degrees of freedom
    without a hinge (axial and torsion), with the properties of the elastic
    section, instead of rigid ones. With ``HingeRadau`` integration, the
    hinge sections carry the elastic flexibility over the plastic hinge
    lengths, which rigid materials would leave out. The moment-curvature
    hinges do not include shear deformation, so columns with capacity design
    for shear have elastic shear materials along the whole member (see
    ``_get_shear_mat_inputs``).

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.baselib.column.ColumnBase`
        Column definition extended by this class.
    """

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
    def mz_mat_tag_(self) -> int:
        """Pinching4 material tag for the flexural hinge about local-z (Mz)."""
        return sub_tag(self.design.line.tag, 90)

    @property
    def my_mat_tag_(self) -> int:
        """Pinching4 material tag for the flexural hinge about local-y (My)."""
        return sub_tag(self.design.line.tag, 92)

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the Column object (see ``ColumnBase``), with the
        yield point of the plastic hinges from section analysis, consistent
        with the cracked-section method.
        """
        super().__init__(*args, **kwargs)
        self.yield_mom_curv = 'analytical'
        # Update the cracked-section properties for the section yield point
        self._set_cracked_properties()

    def add_to_ops(self) -> None:
        """Adds column components to the OpenSees domain
        (i.e, column element and nodes).

        Notes
        -----
        Same hinge materials are used at both ends.
        """
        # Define geometric transformation
        ops.geomTransf(*self._get_geo_transf_inputs())

        # Create the section materials
        mz_mat, minmax_mz = self._get_rot_hinge_mat_inputs('x')
        my_mat, minmax_my = self._get_rot_hinge_mat_inputs('y')
        ops.uniaxialMaterial(*mz_mat)
        ops.uniaxialMaterial(*my_mat)
        ops.uniaxialMaterial(*minmax_mz)
        ops.uniaxialMaterial(*minmax_my)
        for mat_inputs in self._get_shear_mat_inputs():
            ops.uniaxialMaterial(*mat_inputs)

        # Elastic materials of the hinge sections
        for mat_inputs in self._get_hinge_elastic_mat_inputs():
            ops.uniaxialMaterial(*mat_inputs)

        # Create element sections
        ops.section(*self._get_elastic_sec_inputs())
        ops.section(*self._get_inelastic_sec_inputs())
        ops.section(*self._get_interior_sec_inputs())

        # Create beam integration
        ops.beamIntegration(*self._get_int_inputs())

        # Create the element
        ops.element(*self._get_ele_inputs())

    def to_py(self) -> List[str]:
        """Gets the Python commands to construct column components in OpenSees
        domain (i.e, column element and nodes).

        Returns
        -------
        List[str]
            List of Python commands for constructing the components of column
            object in OpenSees.

        Notes
        -----
        Same hinge materials are used at both ends.
        """
        # Define geometric transformation
        content = ['# Create geometric transformation']
        transf_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_geo_transf_inputs()
        )
        content.append(f"ops.geomTransf({transf_inputs})")

        # Create the section materials
        pinching_mz, minmax_mz = self._get_rot_hinge_mat_inputs('x')
        pinching_my, minmax_my = self._get_rot_hinge_mat_inputs('y')
        content.append('# Create uniaxial materials')
        pinching_mz = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in pinching_mz
        )
        pinching_my = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in pinching_my
        )
        minmax_mz = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in minmax_mz
        )
        minmax_my = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in minmax_my
        )
        content.append(f"ops.uniaxialMaterial({pinching_mz})")
        content.append(f"ops.uniaxialMaterial({minmax_mz})")
        content.append(f"ops.uniaxialMaterial({pinching_my})")
        content.append(f"ops.uniaxialMaterial({minmax_my})")
        for mat_inputs in self._get_shear_mat_inputs():
            mat_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in mat_inputs
            )
            content.append(f"ops.uniaxialMaterial({mat_inputs})")

        # Elastic materials of the hinge sections
        for mat_inputs in self._get_hinge_elastic_mat_inputs():
            mat_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in mat_inputs
            )
            content.append(f"ops.uniaxialMaterial({mat_inputs})")

        # Create sections
        content.append('# Create element sections')
        elastic_sec_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_elastic_sec_inputs()
        )
        inelastic_sec_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_inelastic_sec_inputs()
        )
        content.append(f"ops.section({elastic_sec_inputs})")
        content.append(f"ops.section({inelastic_sec_inputs})")
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
        """Gets the Tcl commands to construct column components in OpenSees
        domain (i.e, column element and nodes).

        Returns
        -------
        List[str]
            List of Tcl commands for constructing the components of column
            object in OpenSees.

        Notes
        -----
        Same hinge materials are used at both ends.
        """
        # Define geometric transformation
        content = ['# Create geometric transformation']
        transf_inputs = ' '.join(f"{item}" for item in
                                 self._get_geo_transf_inputs())
        content.append(f"geomTransf {transf_inputs}")

        # Create the section materials
        content.append('# Create uniaxial materials')
        pinching_mz, minmax_mz = self._get_rot_hinge_mat_inputs('x')
        pinching_my, minmax_my = self._get_rot_hinge_mat_inputs('y')
        pinching_mz = ' '.join(f"{item}" for item in pinching_mz)
        pinching_my = ' '.join(f"{item}" for item in pinching_my)
        minmax_mz = ' '.join(f"{item}" for item in minmax_mz)
        minmax_my = ' '.join(f"{item}" for item in minmax_my)
        content.append(f"uniaxialMaterial {pinching_mz}")
        content.append(f"uniaxialMaterial {minmax_mz}")
        content.append(f"uniaxialMaterial {pinching_my}")
        content.append(f"uniaxialMaterial {minmax_my}")

        for mat_inputs in self._get_shear_mat_inputs():
            mat_inputs = ' '.join(f"{item}" for item in mat_inputs)
            content.append(f"uniaxialMaterial {mat_inputs}")

        # Elastic materials of the hinge sections
        for mat_inputs in self._get_hinge_elastic_mat_inputs():
            mat_inputs = ' '.join(f"{item}" for item in mat_inputs)
            content.append(f"uniaxialMaterial {mat_inputs}")

        # Create sections
        content.append('# Create element sections')
        elastic_sec_inputs = ' '.join(
            f"{item}" for item in self._get_elastic_sec_inputs())
        inelastic_sec_inputs = ' '.join(
            f"{item}" for item in self._get_inelastic_sec_inputs())
        content.append(f"section {elastic_sec_inputs}")
        content.append(f"section {inelastic_sec_inputs}")
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

    def _get_inelastic_sec_inputs(self) -> List[str | int]:
        """Retrieves inputs for inelastic aggregated column section.

        Returns
        -------
        List[str | int]
            List of inputs for inelastic aggregated column section, with
            elastic P and T materials, and the shear materials (see
            ``_get_shear_mat_inputs``) also with capacity design for shear.
        """
        sec_inputs = super()._get_inelastic_sec_inputs()
        sec_inputs[2], sec_inputs[12] = self.p_mat_tag, self.t_mat_tag
        sec_inputs[6], sec_inputs[10] = self.vy_mat_tag, self.vz_mat_tag

        return sec_inputs

    def _get_int_inputs(self) -> List[str | float | int]:
        """Retrieves column integration inputs.

        Returns
        -------
        List[str | float | int]
            List of column integration inputs, with the interior section
            aggregated with the shear materials, also with capacity design
            for shear.
        """
        int_inputs = super()._get_int_inputs()
        int_inputs[-1] = self.interior_sec_tag

        return int_inputs

    def _get_rot_hinge_mat_inputs(
        self, axis=Literal['x', 'y']
    ) -> Tuple[List[float | str | int], List[float | str | int]]:
        """Gets the flexure plastic hinge material properties for given axis.

        The model is based on O'Reilly 2016. It does not explicitly address
        confinement effects and bond-slip. It is more suitable for CDN
        like classes that are only gravity-load designed or those designed
        with low transverse reinforcement requiremenets, e.g., CDL.

        Parameters
        ----------
        axis : {'x', 'y'}
            The local axis considered for the calculations.

        Returns
        -------
        flex_mat_inputs : List[float | str | int]
            Pinching4 material model inputs for the plastic hinge describing
            behaviour in flexure around `axis`.
        minmax_mat_inputs : List[float | str | int]
            Inputs for MinMax material describing the failure in flexure
            around `axis`.

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
        if axis == 'x':
            # Section height
            h = self.design.by  # along y
            # The integer tag for the material describing flexure behaviour
            # around local -x (corresponds to z in ops)
            flex_mat_tag = self.mz_mat_tag_
            minmax_mat_tag = self.mz_mat_tag

        elif axis == 'y':
            # Section height
            h = self.design.bx  # along x
            # Number of internal reinforcement (on a single side)
            # The integer tag for the material describing flexure behaviour
            # around local -y axis (corresponds to y in ops)
            flex_mat_tag = self.my_mat_tag_
            minmax_mat_tag = self.my_mat_tag

        # Diameter of internal reinforcement
        dbl_int = self.design.dbl_int_q
        # Concrete compressive strength in base units
        fc = self.design.fc_q
        # Concrete cover
        cover = self.design.cover_q
        # Horizontal (stirrup) reinforcement diameter
        dbh = self.design.dbh_q
        # Compressive axial load (+)
        Nu = max(-self.axial_force, 0)
        # Normalized axial load ratio (dimensionless)
        nu = Nu / (self.design.Ag * fc)

        # Moment, curvature, and neutral axis depth at yielding
        My, phi_y, cy = self._get_my_phiy_analytical(axis)

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
        # Distance from top fiber to bottom rebars
        dd = cover + dbh + dbl_int / 2
        # Distance from top fiber to top rebars
        dd_prime = h - (cover + dbh + dbl_int / 2)
        yb = dd - cy  # rupture case (assuming c=cy - O'Reilly 2016)
        yt = cy - dd_prime  # buckling case (assuming c=cy - O'Reilly 2016)
        e_su = 0.08  # Rupture strain DBD book-p141 (conservative value)
        phi_max = e_su / max(1e-12, yt, yb)  # exhaustion curvature

        # Pinching4 material backbone parameters
        # NOTE: Might use Mcr, My, Mc, Mr instead. The stiffness does not
        # change between the capping and residual strength points.
        ePf1, ePf2, ePf3, ePf4 = My, Mc, Mu, Mr
        ePd1, ePd2, ePd3, ePd4 = phi_y, phi_c, phi_u, phi_r
        eNf1, eNf2, eNf3, eNf4 = -My, -Mc, -Mu, -Mr
        eNd1, eNd2, eNd3, eNd4 = -phi_y, -phi_c, -phi_u, -phi_r

        # Pinching4 material Unloading/Reloading parameters
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

        flex_mat_inputs = [
            'Pinching4', flex_mat_tag,
            ePf1, ePd1, ePf2, ePd2, ePf3, ePd3, ePf4, ePd4,
            eNf1, eNd1, eNf2, eNd2, eNf3, eNd3, eNf4, eNd4,
            rDispP, rForceP, uForceP,
            rDispN, rForceN, uForceN,
            gK1, gK2, gK3, gK4, gKLim,
            gD1, gD2, gD3, gD4, gDLim,
            gF1, gF2, gF3, gF4, gFLim,
            gE, dmgType
        ]
        # MinMax material inputs
        minmax_mat_inputs = [
            'MinMax', minmax_mat_tag, flex_mat_tag,
            '-min', -phi_max, '-max', phi_max
        ]

        # Rounding to precision
        flex_mat_inputs = round_list(flex_mat_inputs)
        minmax_mat_inputs = round_list(minmax_mat_inputs)

        return flex_mat_inputs, minmax_mat_inputs
