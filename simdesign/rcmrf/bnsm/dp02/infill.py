"""This module provides the infill class implementation for the ``DP02`` model
in the BNSM layer.
"""
# Imports from installed packages
from typing import Tuple, List

# Imports from bnsm base library
from ..baselib.infill import InfillBase

# Imports from utils library
from ....utils.misc import PRECISION, round_list


class Infill(InfillBase):
    """Masonry infill wall implementation for the ``DP02`` model.

    This class extends ``InfillBase`` with the material modelling
    strategy suggested in O'Reilly (2016) for the struts.

    See Also
    --------
    :class:`~InfillBase`
        Infill class definition extended by this class.
    """

    def _get_mat_inputs(self) -> Tuple[List[str | float | int], float]:
        """
        Compute the uniaxial material definition for the equivalent diagonal
        strut and the corresponding strut cross-sectional area based on
        O'Reilly 2016.

        Returns
        -------
        mat_inputs : List[str | float | int]
            OpenSees `uniaxialMaterial` argument list.
        Aw : float
            Equivalent digaonal strut area (m2).

        References
        ----------
        O'Reilly, G. J. (2016). Performance-based seismic assessment and
        retrofit of existing RC frame buildings in Italy (Doctoral
        dissertation, IUSS Pavia).
        https://github.com/gerardjoreilly/Numerical-Modelling-of-GLD-RC-Frames/blob/master/infill.tcl
        """
        mat_inputs, Aw = super()._get_mat_inputs()
        # Strengths based on O'Reilly, 2016
        # TODO: Ask about residual strength
        sig2 = -mat_inputs[2]  # Peak strength (kPa)
        sig1 = 0.80 * sig2  # Cracking strength, Equation 2.66
        sig4 = 0.10 * sig2  # Residual strength, Equation 2.67

        # Drift limits based on O'Reilly 2016, from Table 2.14
        # TODO: Unclear, ask Gerard about these values
        theta1 = 0.0018  # DS1
        theta2 = 0.0046  # DS2
        theta4 = 0.0188  # DS4

        # Dimensions
        h = self.design.height  # infill height, between joints
        L = self.design.length  # infill length, between joints

        def eps_from_theta(theta):
            # Compute epsilon based on Equation 10 of Hak et al. 2012
            return (
                1.0
                - ((1.0 + (L / h - theta) ** 2) / (1.0 + (L / h) ** 2))
                ** 0.5
            )

        # Axial strains in struts corresponding to a interstory drift value
        eps1 = eps_from_theta(theta1)
        eps2 = eps_from_theta(theta2)
        eps4 = eps_from_theta(theta4)

        # Pinching4 material parameters
        ePf1, ePf2, ePf3, ePf4 = 0.001, 0.002, 0.001, 0.001
        ePd1, ePd2, ePd3, ePd4 = eps1, eps2, eps4, eps4
        eNf1, eNf2, eNf3, eNf4 = -sig1, -sig2, -sig4, -sig4
        eNd1, eNd2, eNd3, eNd4 = -eps1, -eps2, -eps4, -eps4
        rDispP, fFoceP, uForceP = 0.8, 0.1, 0.0
        rDispN, fFoceN, uForceN = 0.8, 0.1, 0.0
        gK1, gK2, gK3, gK4, gKLim = 0.0, 0.0, 0.0, 0.0, 0.0
        gD1, gD2, gD3, gD4, gDLim = 0.0, 0.0, 0.0, 0.0, 0.0
        gF1, gF2, gF3, gF4, gFLim = 0.0, 0.0, 0.0, 0.0, 0.0
        gE, dmgType = 0.0, "energy"
        mat_inputs = [
            'Pinching4', self.design.rectangle.tag,
            ePf1, ePd1, ePf2, ePd2, ePf3, ePd3, ePf4, ePd4,
            eNf1, eNd1, eNf2, eNd2, eNf3, eNd3, eNf4, eNd4,
            rDispP, fFoceP, uForceP,
            rDispN, fFoceN, uForceN,
            gK1, gK2, gK3, gK4, gKLim,
            gD1, gD2, gD3, gD4, gDLim,
            gF1, gF2, gF3, gF4, gFLim,
            gE, dmgType
        ]
        mat_inputs = round_list(mat_inputs, PRECISION)

        # These terms are calibrated by Cavalieri et al. [2005]
        # and listed in Landi et al. DBA chapter
        # pinchX = 0.8
        # pinchY = 0.1
        # damage1 = 0.0
        # damage2 = 0.0
        # beta = 0.5
        # mat_inputs = [
        #     'Hysteretic', self.design.rectangle.tag,
        #     ePf1, ePd1, ePf2, ePd2, ePf3, ePd3,
        #     eNf1, eNd1, eNf2, eNd2, eNf3, eNd3,
        #     pinchX, pinchY, damage1, damage2, beta
        # ]
        # mat_inputs = round_list(mat_inputs, PRECISION)

        return mat_inputs, Aw
