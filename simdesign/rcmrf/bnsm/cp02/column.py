"""This module provides the column class implementation for the ``CP02`` model
in the BNSM layer.
"""
# Imports from installed packages
import numpy as np
from typing import Literal, List

# Imports from bnsm base library
from ..cp01.column import Column as ColumnCP01

# Imports from utils library
from ....utils.units import MPa
from ....utils.misc import round_list


class Column(ColumnCP01):
    """Column implementation for the ``CP02`` model.

    This class directly uses the behaviour defined in ``ColumnCP01``,
    but overrides the plastic hinge material definition for rotational
    degrees of freedoms based on the PhD Thesis of Serkan Hasanoglu.

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.cp01.column.Column`
        CP01 column model definition extended by this class.
    """

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
            HystereticSM material model inputs for the plastic hinge describing
            behaviour in flexure around `axis`.

        References
        ----------
        Hasanoglu, S. and O'Reilly G. J. (2026). A hysteretic energy–based
        framework for seismic fragility assessment of ductile reinforced
        concrete frame buildings
        """
        if axis == 'x':
            # The integer tag for the material describing flexure behaviour
            # around local -x (corresponds to z in ops)
            flex_mat_tag = self.mz_mat_tag
            # Section height
            h = self.design.by  # along y
            # Transverse reinforcement ratio
            rhoh = self.rhoh_y_q  # Stirrups are along -y axis
            # Gross flexural rigidity of column section
            EI_gross = self.Ecm_q * self.design.Ix
        elif axis == 'y':
            # The integer tag for the material describing flexure behaviour
            # around local -y axis (corresponds to y in ops)
            flex_mat_tag = self.my_mat_tag
            # Section height
            h = self.design.bx  # along x
            # Transverse reinforcement ratio
            rhoh = self.rhoh_x_q  # Stirrups are along -x axis
            # Gross flexural rigidity of column section
            EI_gross = self.Ecm_q * self.design.Iy

        # Concrete compressive strength in base units
        fc = self.design.fc_q
        # Concrete compressive strength in MPa
        fc_mpa = self.design.fc_q / MPa  # convert to MPa
        # Longitudinal steel yield strength in MPa
        fsyl_mpa = self.design.fsyl_q / MPa  # convert to MPa
        # Concrete cover
        cover = self.design.cover_q
        # Diameter of corner reinforcement
        dbl_cor = self.design.dbl_cor_q
        # Horizontal (stirrup) reinforcement diameter
        dbh = self.design.dbh_q
        # Longitudinal reinforcement ratio
        rhol = self.rhol_q
        # Compressive axial load (+)
        Nu = max(-self.axial_force, 0)
        # Axial load ratio
        niu = Nu / (self.design.Ag * fc)
        # Distance from top fiber to bottom rebars
        dd = h - cover - dbh - 0.5 * dbl_cor
        # Nominal length of column
        Ln = self.design.H
        # Shear span, assuming equal to 50% of the free length of the element
        Ls = Ln / 2
        # Shear span to effective depth ratio
        rSsD = Ls / dd

        # Yield moment
        My = self._get_rot_hinge_props(axis)[1]

        # Capping moment capacity
        Mc_My = (1.08 ** niu) * (1.38 ** (10*rhol)) * (1.14 ** (0.1*rSsD))
        Mc = Mc_My * My

        # Ultimate moment capacity
        Mu_Mc = (0.91 ** (0.01*fc_mpa)) * (0.8 ** (0.1*rSsD))
        Mu = Mu_Mc * Mc

        # Yield rotation capacity
        EI_ratio = np.clip(0.08 * (1.25 ** (10*niu)) * (1.2 ** rSsD), 0.2, 0.8)
        EIy = EI_gross * EI_ratio
        theta_y = My * Ls / (3 * EIy)

        # Plastic rotation capacity
        theta_cap_pl = 0.009 * (0.25 ** (0.01*fc_mpa)) * (0.23 ** niu) * \
            (2.17 ** (100*rhol))

        # Post-capping rotation capacity
        theta_pc = 0.01 * (0.07 ** niu) * (1.78 ** (100*rhoh)) * \
            (1.18 ** (0.01*fsyl_mpa))

        # Post-ultimate rotation capacity
        theta_pu = 0.0023 * (1.96 ** (0.1*fc_mpa)) * (2.74 ** (100*rhoh))
        theta_pu = np.minimum(theta_pu, 4*theta_pc)

        # Rotation values for cyclic loading
        if self.cyclic_model:
            moment_1 = My
            moment_2 = Mc
            moment_3 = Mu
            moment_4 = 0.1 * My
            theta_1 = theta_y
            theta_2 = theta_y + theta_cap_pl
            theta_3 = theta_y + theta_cap_pl + theta_pc
            theta_4 = theta_y + theta_cap_pl + theta_pc + theta_pu
        else:
            # These modifiers were determined based on the suggested
            # values in ATC 72-1 report
            moment_1 = My
            moment_2 = 1.1 * Mc
            moment_3 = 1.1 * Mu
            moment_4 = 0.1 * My
            theta_1 = theta_y
            theta_2 = theta_y + 1.4*theta_cap_pl
            theta_3 = theta_y + 1.4*theta_cap_pl + 2*theta_pc
            theta_4 = theta_y + 1.4*theta_cap_pl + 2*theta_pc + 2*theta_pu

        # Pinching factor for strain (or deformation) during reloading
        pinchx = 1.0
        # Pinching factor for stress (or force) during reloading
        pinchy = 1.0
        # Damage due to ductility: D1(mu-1)
        damage1 = 0.0
        # Damage due to energy: D2(Eii/Eult)
        damage2 = 0.2
        # Power used to determine the degraded unloading stiffness
        beta = 0.4

        # Material inputs other than tag and type
        rot_mat_inputs = [
            'HystereticSM',
            flex_mat_tag,
            moment_1, theta_1,
            moment_2, theta_2,
            moment_3, theta_3,
            moment_4, theta_4,
            -moment_1, -theta_1,
            -moment_2, -theta_2,
            -moment_3, -theta_3,
            -moment_4, -theta_4,
            pinchx, pinchy, damage1, damage2, beta
        ]

        # Rounding to precision
        rot_mat_inputs = round_list(rot_mat_inputs)

        return rot_mat_inputs
