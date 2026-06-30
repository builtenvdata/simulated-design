"""This module provides the column class implementation for the ``DP02`` model
in the BNSM layer.
"""
# Imports from installed packages
import numpy as np
import openseespy.opensees as ops
from typing import Literal, List, Tuple, Dict

# Imports from bnsm base library
from ..baselib.column import ColumnBase, ColumnDesign

# Imports from utils library
from ....utils.units import MPa
from ....utils.misc import round_list
from ....utils.rcsection import get_moments


class Column(ColumnBase):
    """Column implementation for the ``DP02`` model.

    This class extends ``ColumnBase`` with a force-based beam-column
    formulation and lumped plasticity end hinges following the modelling
    strategy in O'Reilly (2016).

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
        return int(str(self.design.line.tag) + '990')

    @property
    def my_mat_tag_(self) -> int:
        """Pinching4 material tag for the flexural hinge about local-y (My)."""
        return int(str(self.design.line.tag) + '992')

    def __init__(
        self, design: ColumnDesign, bondslip_factor: float,
        capacity_design: bool, load_factors: Dict[Literal['G', 'Q'], float],
        cyclic_model: bool = False, cracked_section: bool = False
    ) -> None:
        """Initialize the Column object.

        Parameters
        ----------
        design : ColumnDesign
            Instance of column design information model.
        bondslip_factor : float
            Bondslip factor considered while defining plastic hinges.
        capacity_design : bool
            Flag to check whether capacity shear design is followed or not.
        load_factors :  Dict[Literal['G', 'Q'], float]
            Load factors used to compute gravity loads/forces on the column.
        cyclic_model : bool, optional
            If True, the model parameters will be adjusted for cyclic analysis.
            By default False.
        cracked_section : bool, optional
            If True, the elastic sections uses cracked-section
            (effective) flexural properties. If False, gross-section
            properties are used. By default False.

        Notes
        -----
        Removed cracked section computations here to reduce the time.
        It is being computed in later stages.
        """
        self.design = design
        self.bondslip_factor = bondslip_factor
        self.capacity_design = capacity_design
        self.cyclic_model = cyclic_model
        self.cracked_section = cracked_section
        self.axial_force = -(load_factors['G'] * design.hinge_Ng
                             + load_factors['Q'] * design.hinge_Nq)
        self.ele_load = float(design.self_wg * load_factors['G'])
        self.jnt_offsets = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

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
        if not self.capacity_design:
            vy_mat, minmax_vy = self._get_shear_hinge_mat_inputs('y')
            vz_mat, minmax_vz = self._get_shear_hinge_mat_inputs('x')
            ops.uniaxialMaterial(*vy_mat)
            ops.uniaxialMaterial(*vz_mat)
            ops.uniaxialMaterial(*minmax_vy)
            ops.uniaxialMaterial(*minmax_vz)

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
        if not self.capacity_design:
            vy_mat, minmax_vy = self._get_shear_hinge_mat_inputs('y')
            vz_mat, minmax_vz = self._get_shear_hinge_mat_inputs('x')
            vy_mat_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in vy_mat
            )
            vz_mat_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in vz_mat
            )
            minmax_vy_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in minmax_vy
            )
            minmax_vz_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in minmax_vz
            )
            content.append(f"ops.uniaxialMaterial({vy_mat_inputs})")
            content.append(f"ops.uniaxialMaterial({vz_mat_inputs})")
            content.append(f"ops.uniaxialMaterial({minmax_vy_inputs})")
            content.append(f"ops.uniaxialMaterial({minmax_vz_inputs})")

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

        if not self.capacity_design:
            vy_mat, minmax_vy = self._get_shear_hinge_mat_inputs('y')
            vz_mat, minmax_vz = self._get_shear_hinge_mat_inputs('x')
            vy_mat_inputs = ' '.join(f"{item}" for item in vy_mat)
            vz_mat_inputs = ' '.join(f"{item}" for item in vz_mat)
            minmax_vy_inputs = ' '.join(f"{item}" for item in minmax_vy)
            minmax_vz_inputs = ' '.join(f"{item}" for item in minmax_vz)
            content.append(f"uniaxialMaterial {vy_mat_inputs}")
            content.append(f"uniaxialMaterial {vz_mat_inputs}")
            content.append(f"uniaxialMaterial {minmax_vy_inputs}")
            content.append(f"uniaxialMaterial {minmax_vz_inputs}")

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
            # Section width
            b = self.design.bx  # along x
            # Number of internal web reinforcement (intermediate)
            nbl_v = np.array(self.design.nbly_int_q, dtype=int)
            # Number of internal reinforcement (on a single side)
            nbl_int = np.array(self.design.nblx_int_q, dtype=int)
            # The integer tag for the material describing flexure behaviour
            # around local -x (corresponds to z in ops)
            flex_mat_tag = self.mz_mat_tag_
            minmax_mat_tag = self.mz_mat_tag

        elif axis == 'y':
            # Section height
            h = self.design.bx  # along x
            # Section width
            b = self.design.by  # along y
            # Number of internal web reinforcement (intermediate)
            nbl_v = np.array(self.design.nblx_int_q, dtype=int)
            # Number of internal reinforcement (on a single side)
            nbl_int = np.array(self.design.nbly_int_q, dtype=int)
            # The integer tag for the material describing flexure behaviour
            # around local -y axis (corresponds to y in ops)
            flex_mat_tag = self.my_mat_tag_
            minmax_mat_tag = self.my_mat_tag

        # Number of corner reinforcement (on a single side)
        nbl_cor = 2
        # Diameter of corner reinforcement
        dbl_cor = self.design.dbl_cor_q
        # Diameter of internal reinforcement
        dbl_int = self.design.dbl_int_q
        # Concrete compressive strength in base units
        fc = self.design.fc_q
        # Longitudinal steel yield strength in base units
        fsyl = self.design.fsyl_q
        # Concrete cover
        cover = self.design.cover_q
        # Horizontal (stirrup) reinforcement diameter
        dbh = self.design.dbh_q
        # Compressive axial load (+)
        Nu = max(-self.axial_force, 0)
        # Normalized axial load ratio (dimensionless)
        nu = Nu / (self.design.Ag * fc)
        # Concrete modulus of elasticity
        Ec = self.Ecm_q
        # Steel modulus of elasticity
        Es = self.design.Es

        # Reinforcement layout (top to bottom)
        y_ct = cover + dbh + dbl_cor / 2
        y_it = cover + dbh + dbl_int / 2
        y_cb = h - (cover + dbh + dbl_cor / 2)
        y_ib = h - (cover + dbh + dbl_int / 2)
        dv = (y_cb - y_ct) / (nbl_v + 1)
        y_layers = [y_it, y_ct] + [y_ct + (i + 1) * dv for i in range(nbl_v)
                                   ] + [y_cb, y_ib]
        # Reinforcement area per layer (top to bottom)
        Ab_c = 0.25*np.pi*dbl_cor**2
        Ab_i = 0.25*np.pi*dbl_int**2
        As_c = nbl_cor * Ab_c
        As_i = nbl_int * Ab_i
        As_web = 2 * Ab_i  # on both sides
        As_layers = [As_i, As_c] + [As_web for _ in range(nbl_v)
                                    ] + [As_c, As_i]
        # Cracking and yield moments
        _, _, _, My, phi_y, cy = get_moments(
            h=h, b=b, fc=fc, Ec=Ec,
            Pext=Nu, fyL=fsyl, Es=Es,
            As_layers=As_layers,
            y_layers=y_layers,
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
        # gE = 10.0  # suitable for low to moderate ductility
        gE = 0.0  # No degradation
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

        # Save neutral axis depth for shear hinge calculations
        if axis == 'x':
            self._cy = cy
        elif axis == 'y':
            self._cx = cy

        # Save effective moment inertia for elastic section
        EIeff = My / phi_y
        Ieff = EIeff / Ec
        if axis == 'x':
            self._Ix_eff = Ieff
        elif axis == 'y':
            self._Iy_eff = Ieff

        return flex_mat_inputs, minmax_mat_inputs
