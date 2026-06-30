"""This module provides the column class implementation for the ``CP01`` model
in the BNSM layer.
"""
# Imports from installed packages
import numpy as np
import openseespy.opensees as ops
from typing import Literal, List, Tuple

# Imports from bnsm base library
from ..baselib.column import ColumnBase

# Imports from utils library
from ....utils.units import MPa, MN
from ....utils.misc import round_list


class Column(ColumnBase):
    """Column implementation for the ``CP01`` model.

    The column is modeled using a concentrated plasticity approach. Plastic
    rotations are concentrated at the element ends via
    ``beamIntegration('ConcentratedPlasticity', ...)`` (end hinge integration
    points with an elastic interior region), while the element formulation is
    provided by ``ColumnBase``.

    End-hinge flexural behaviour about the local z-axis (Mz) is defined using a
    uniaxial ``Hysteretic`` material, expressed in terms of bending moment vs.
    plastic rotation.

    If there is no capacity design, degrading shear springs are
    defined using the uniaxial ``LimitState`` material coupled with a
    ``ThreePoint`` ``limitCurve`` (drift-based), following the strength and
    post-peak degradation formulations adopted from Elwood & Moehle (2003) and
    Sezen & Moehle (2004).

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.baselib.column.ColumnBase`
        Base column definition extended by this class.
    """

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
        ops.uniaxialMaterial(*self._get_rot_hinge_mat_inputs('x'))
        ops.uniaxialMaterial(*self._get_rot_hinge_mat_inputs('y'))
        if not self.capacity_design:
            vy_mat, vy_curve = self._get_shear_hinge_mat_inputs('y')
            vz_mat, vz_curve = self._get_shear_hinge_mat_inputs('x')
            ops.limitCurve(*vy_curve)
            ops.uniaxialMaterial(*vy_mat)
            ops.limitCurve(*vz_curve)
            ops.uniaxialMaterial(*vz_mat)

        # Create element sections
        ops.section(*self._get_elastic_sec_inputs())
        ops.section(*self._get_inelastic_sec_inputs())

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
        content.append('# Create uniaxial materials')
        mz_mat_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_rot_hinge_mat_inputs('x')
        )
        my_mat_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_rot_hinge_mat_inputs('y')
        )
        content.append(f"ops.uniaxialMaterial({mz_mat_inputs})")
        content.append(f"ops.uniaxialMaterial({my_mat_inputs})")

        if not self.capacity_design:
            vy_mat, vy_curve = self._get_shear_hinge_mat_inputs('y')
            vz_mat, vz_curve = self._get_shear_hinge_mat_inputs('x')
            vy_mat_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in vy_mat
            )
            vz_mat_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in vz_mat
            )
            vy_curve_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in vy_curve
            )
            vz_curve_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in vz_curve
            )
            content.append(f"ops.limitCurve({vy_curve_inputs})")
            content.append(f"ops.uniaxialMaterial({vy_mat_inputs})")
            content.append(f"ops.limitCurve({vz_curve_inputs})")
            content.append(f"ops.uniaxialMaterial({vz_mat_inputs})")

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
        mz_mat_inputs = ' '.join(
            f"{item}" for item in self._get_rot_hinge_mat_inputs('x'))
        my_mat_inputs = ' '.join(
            f"{item}" for item in self._get_rot_hinge_mat_inputs('y'))
        content.append(f"uniaxialMaterial {mz_mat_inputs}")
        content.append(f"uniaxialMaterial {my_mat_inputs}")

        if not self.capacity_design:
            vy_mat, vy_curve = self._get_shear_hinge_mat_inputs('y')
            vz_mat, vz_curve = self._get_shear_hinge_mat_inputs('x')
            vy_mat_inputs = ' '.join(f"{item}" for item in vy_mat)
            vz_mat_inputs = ' '.join(f"{item}" for item in vz_mat)
            vy_curve_inputs = ' '.join(f"{item}" for item in vy_curve)
            vz_curve_inputs = ' '.join(f"{item}" for item in vz_curve)
            content.append(f"limitCurve {vy_curve_inputs}")
            content.append(f"uniaxialMaterial {vy_mat_inputs}")
            content.append(f"limitCurve {vz_curve_inputs}")
            content.append(f"uniaxialMaterial {vz_mat_inputs}")

        # Create sections
        content.append('# Create element sections')
        elastic_sec_inputs = ' '.join(
            f"{item}" for item in self._get_elastic_sec_inputs())
        inelastic_sec_inputs = ' '.join(
            f"{item}" for item in self._get_inelastic_sec_inputs())
        content.append(f"section {elastic_sec_inputs}")
        content.append(f"section {inelastic_sec_inputs}")

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

    def _get_int_inputs(self) -> List[str | float]:
        """Retrieves column integration inputs.

        Returns
        -------
        List[float]
            List of column integration inputs.
        """
        int_inputs = [
            'ConcentratedPlasticity',
            self.int_tag, self.inelastic_sec_tag,
            self.inelastic_sec_tag, self.elastic_sec_tag
        ]

        return int_inputs

    def _get_rot_hinge_mat_inputs(self, axis: Literal['x', 'y']
                                  ) -> List[int | float | str]:
        """Gets the plastic hinge material inputs for given axis.

        Parameters
        ----------
        axis : Literal['x', 'y']
            The local axis considered for the calculations.

        Returns
        -------
        rot_mat_inputs : List[int | float | str]
            Hysteretic material model inputs for the plastic hinge describing
            behaviour in flexure around `axis`.
        """
        if axis == 'x':
            # The integer tag for the material describing flexure behaviour
            # around local -x (corresponds to z in ops)
            flex_mat_tag = self.mz_mat_tag

        elif axis == 'y':
            # The integer tag for the material describing flexure behaviour
            # around local -y axis (corresponds to y in ops)
            flex_mat_tag = self.my_mat_tag

        # Plastic hinge properties
        (
            _, My, Mc, Mr, theta_y, theta_cap_pl, theta_pc,
            pinchx, pinchy, damage1, damage2, beta
         ) = self._get_rot_hinge_props(axis)

        # Rotation values for monotonic loading
        theta_1 = theta_y
        theta_2 = theta_y + theta_cap_pl
        theta_3 = theta_y + theta_cap_pl + theta_pc

        # Pinching factor for strain (or deformation) during reloading
        pinchx = 1.0  # no pinching (default)
        # Pinching factor for stress (or force) during reloading
        pinchy = 1.0  # no pinching (default)
        # Damage due to ductility: D1(mu-1)
        damage1 = 0.0  # no degradation (default)
        # Damage due to energy: D2(Eii/Eult)
        damage2 = 0.0  # no degradation (default)
        # Power used to determine the degraded unloading stiffness based on
        # ductility, mu-beta (optional, default=0.0)
        beta = 0.0  # elastic unloading (default)
        # Material inputs other than tag and type
        rot_mat_inputs = [
            'Hysteretic', flex_mat_tag,
            My, theta_1, Mc, theta_2, Mr, theta_3,
            -My, -theta_1, -Mc, -theta_2, -Mr, -theta_3,
            pinchx, pinchy, damage1, damage2, beta
        ]

        # Rounding to precision
        rot_mat_inputs = round_list(rot_mat_inputs)

        return rot_mat_inputs

    def _get_shear_hinge_mat_inputs(
        self, axis: Literal['x', 'y'],
    ) -> Tuple[List[int | float | str], List[int | float | str]]:
        """Gets inputs the shear plastic hinge materials for given axis.

        Parameters
        ----------
        axis : Literal['x', 'y']
            The local axis considered for the calculations.

        Returns
        -------
        mat_inputs : List[int | float | str]
            Inputs for the limit state material for describing the shear
            behaviour in `axis`.
        limit_curve_inputs : List[int | float | str]
            Inputs for limit curve used by the limit state material describing
            the shear behaviour in `axis`.

        References
        ----------
        CEN (2005) Eurocode 8: Design of structures for earthquake resistance -
        Part 3: Assessment and retrofitting of existing buildings.
        Brussels, Belgium

        ASCE/SEI 41-17. (2017). Seismic rehabilitation of existing buildings.
        American Society of Civil Engineers.

        LeBorgne, M. R., & Ghannoum, W. M. (2014). Calibrated analytical
        element for lateral-strength degradation of reinforced concrete
        columns. Engineering Structures, 81, 35-48.

        Sezen, H. and Moehle, J.P. (2004). Shear Strength Model for Lightly
        Reinforced Concrete Columns. J Struct Eng 130:1692-1703.
        https://doi.org/10.1061/(asce)0733-9445(2004)130:11(1692)

        Elwood K. J., & Moehle J. P. (2003). Shake table tests and analytical
        studies on the gravity load collapse of reinforced concrete frames.
        PEER report 2003/01. Pacific Earthquake Engineering Research Center,
        College of Engineering,  University of California, Berkeley.
        """
        if axis == 'y':
            # theta_y is about local-x (-z in ops)
            theta_y = self._get_rot_hinge_props('x')[3]
            # Section height
            h = self.design.by  # along y
            # Number of horizontal bars (stirrup legs)
            nbh = self.design.nbh_y_q
            # The integer tag for the Limit Curve defining the limit surface
            limit_curve_tag = self.vy_mat_tag
            # The integer tag for the material describing shear behaviour in
            # local -y (corresponds to y in ops)
            shear_mat_tag = self.vy_mat_tag
        elif axis == 'x':
            # theta_y is about local-y
            theta_y = self._get_rot_hinge_props('y')[3]
            # Section height
            h = self.design.bx  # along x
            # Number of horizontal bars (stirrup legs)
            nbh = self.design.nbh_x_q
            # The integer tag for the Limit Curve defining the limit surface
            limit_curve_tag = self.vz_mat_tag
            # The integer tag for the material describing shear behaviour in
            # local -x (corresponds to z in ops)
            shear_mat_tag = self.vz_mat_tag

        # Horizontal (stirrup) reinforcement diameter
        dbh = self.design.dbh_q
        # Concrete compressive strength in MPa
        fc_mpa = self.design.fc_q / MPa  # convert to MPa
        # Nominal length of column
        Ln = self.design.H
        # Stirrup spacing
        sbh = self.design.sbh_q
        # Shear span, assuming equal to 50% of the free length of the element
        Ls = Ln / 2  # NOTE: Could be varied with intensity of loading, but ok.
        # Effective depth: dist. between outer comp. fiber and tens. steel
        d = 0.9 * h
        # Transverse reinforcement yield strength (quality adjusted)
        fsyh_mpa = self.design.fsyh_q / MPa  # in MPa
        fsyh = self.design.fsyh_q  # in base units
        # Gross corss-section area
        Ag = self.design.Ag
        # Compressive axial load (+) - Positive in compression
        Nu = max(-self.axial_force, 0)
        # Axial load in Mega Newton (mN) - Positive in compression
        Nu_MN = Nu / MN  # convert to mN
        # Transverse reinforcement area
        Av = nbh * np.pi * (dbh**2) / 4
        # Initial shear strength, see ASCE/SEI 41-17 - Equation 10-3si
        k = 1.0  # Degradation factor (1.0 for initial strength)
        lambda_ = 1.0  # Assuming normal weight concrete aggregate
        d = 0.8 * h  # Effective depth, permitted to assume by ASCE
        alpha = np.interp(sbh / d, [0.75, 1.0], [1.0, 0.0])
        M_V_rat = Ls  # Largest ratio of moment to shear, assumed
        M_Vd_rat = min(max(M_V_rat / d, 2), 4)  # Should satify: 2 <= M/Vd <= 4
        Vn = k * (
            alpha * (Av * fsyh_mpa * d / sbh)
            + lambda_
            * (
                (fc_mpa**0.5)
                / (2 * M_Vd_rat)
                * (1 + (2 * Nu_MN) / ((fc_mpa**0.5) * Ag)) ** 0.5
            )
            * (0.8 * Ag)
        )
        # Convert from MPa units to based units
        Vn *= MN
        # Shear-spring elastic slope - LeBorgne and Ghannoum (2014) - Eqn. 1
        k_el = (5 / 6) * (self.Gcm_q * Ag / Ln)
        # Degrading slope of the shear-drift spring backbone
        # Shoraka and Elwood (2013) - Eqn. 20
        k_deg = (
            4.5 * Nu * (((Av * fsyh * 0.9 * h) / (Nu * sbh)) * 4.6 + 1) ** 2
        ) / Ln

        # Inputs for Three-Point Limit Curve - Elwood and Moehle 2003
        # integer element tag for the associated beam-column element
        eleTag = self.design.line.tag
        # Three-Point strength degradation model by Sezen and Moehle 2004
        k0, k1, k2 = 1.0, 1.0, 0.7  # Strength degradation factors
        mu_y0, mu_y1, mu_y2 = 0.0, 2.0, 6.0  # Displacement ductilities
        # The coordinates of points on the limit curve
        # x1, y1 = -10, Vn  # the first point
        x1, y1 = mu_y0 * theta_y, k0 * Vn  # the first point TODO: verify
        # x2, y2 = 0, Vn  # the second point
        x2, y2 = mu_y1 * theta_y, k1 * Vn  # the second point TODO: verify
        # x3, y3 = 10, Vn  # the third point
        x3, y3 = mu_y2 * theta_y, k2 * Vn  # the third point TODO: verify
        # Floating point value for the slope of the third branch in the
        # post-failure backbone, assumed to be negative
        Kdeg = -k_deg
        # Floating point value for the residual force capacity of the
        # post-failure backbone
        Fres = 0.05  # should be a small value - shear failure
        # Integer flag for type of deformation defining the abscissa
        # of the limit curve:
        # 1 = maximum beam-column chord rotations
        # 2 = drift based on displacement of nodes ndI and ndJ
        defType = 2
        # Integer flag for type of force defining the ordinate of the
        # limit curve:
        # 0 = force in associated limit state material
        # 1 = shear in beam-column element
        # 2 = axial load in beam-column element
        # Option 1 assumes no member loads
        forType = 0
        # Integer node tag for the first associated node
        # (normally node I of $eleTag beam-column element)
        ndl = self.ele_node_i.tag
        # Integer node tag for the second associated node
        # (normally node J of $eleTag beam-column element)
        ndJ = self.ele_node_j.tag
        # Nodal degree of freedom to monitor for drift
        if axis == 'x':
            dof = 1
        elif axis == 'y':
            dof = 2
        # Perpendicular global direction from which length is
        # determined to compute drift: 1 = X, 2 = Y, 3 = Z
        perpDirn = 3
        # Variable containing limit curve inputs
        limit_curve_inputs = [
            'ThreePoint', limit_curve_tag, eleTag,
            x1, y1, x2, y2, x3, y3, Kdeg, Fres,
            defType, forType, ndl, ndJ, dof, perpDirn
        ]
        # Inputs for LimitState material model - Elwood and Moehle 2003
        # Stress and strain (or force & deformation) at the three points of
        # the envelope in the positive direction
        s1p, e1p = 0.25 * Vn, 0.25 * Vn / k_el  # 1st
        s2p, e2p = 0.75 * Vn, 0.75 * Vn / k_el  # 2nd
        s3p, e3p = 2.5 * Vn, 2.5 * Vn / k_el  # 3rd
        # Stress and strain (or force & deformation) at the three points the
        # envelope in the negative direction (all are negative values)
        s1n, e1n = -0.25 * Vn, -0.25 * Vn / k_el  # 1st
        s2n, e2n = -0.75 * Vn, -0.75 * Vn / k_el  # 2nd
        s3n, e3n = -2.5 * Vn, -2.5 * Vn / k_el  # 3rd
        # Pinching factor for strain (or deformation) during reloading
        pinchX = 0.4  # TODO: Reference
        # Pinching factor for stress (or force) during reloading
        pinchY = 0.3  # TODO: Reference
        # Damage due to ductility: D1(m-1)
        damage1 = 0.003  # TODO: Reference
        # Damage due to energy: D2(Ei/Eult)
        damage2 = 0.0  # TODO: Reference
        # Power used to determine the degraded unloading stiffness based on
        # ductility, mu-beta (optional, default=0.0)
        beta = 0.0  # TODO: Reference
        # The integer defining the type of LimitCurve (0 = no curve,
        # 1 = axial curve, all other curves can be any other integer)
        curveType = 2
        # Variable containing limit state material inputs
        mat_inputs = [
            'LimitState', shear_mat_tag,
            s1p, e1p, s2p, e2p, s3p, e3p,
            s1n, e1n, s2n, e2n, s3n, e3n,
            pinchX, pinchY, damage1, damage2, beta,
            limit_curve_tag, curveType
        ]

        # Rounding to precision
        limit_curve_inputs = round_list(limit_curve_inputs)
        mat_inputs = round_list(mat_inputs)

        return mat_inputs, limit_curve_inputs
