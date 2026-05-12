"""This module provides the column class implementation for the ``CP03`` model
in the BNSM layer.
"""
# Imports from installed packages
import openseespy.opensees as ops
from typing import Literal, List, Tuple

# Imports from bnsm cp01 library
from ..cp01.column import Column as ColumnCP01

# Imports from bnsm base library
from ..baselib.node import Node
from ..baselib.constants import PDELTA_TRANSF_Z

# Imports from utils library
from ....utils.misc import round_list


class Column(ColumnCP01):
    """Column implementation for the ``CP03`` model.

    The column is modeled based on a concentrated plasticity approach.
    An elastic interior member (``elasticBeamColumn``) is connected to
    nonlinear rotational hinges at both ends. Each hinge is implemented
    as a ``zeroLengthSection`` element between the original column-end node
    and an auxiliary element node.

    The hinge response is defined by a uniaxial ``Hysteretic`` material
    assigned to the rotational degree of freedom about the local z-axis.
    All other translational and rotational degrees of freedom across the
    hinge are constrained to behave rigidly using rigid materials, so the
    hinge represents concentrated flexural nonlinearity.

    Since the hinge and elastic column elements act in series, the elastic
    stiffness of the interior member is modified following the recommendations
    by Ibarra & Krawinkler (2005) and Zareian & Medina (2010).

    References
    ---------
    Ibarra, L. F. and Krawinkler, H. (2005). Global collapse of frame
    structures under seismic excitations. Technical Report 152,
    Stanford University.

    Zareian, F. and Medina R. A. (2010). A practical method for proper
    modeling of structural damping in inelastic plane structural systems.
    Computers and Structures, 88(1-2), 45-53.
    https://doi.org/10.1016/j.compstruc.2009.08.001

    Attributes
    ----------
    hinge_node_i : Node
        Extra node considered for hinge definition at the start of column.
    hinge_node_j : Node
        Extra node considered for hinge definition at the end of column.

    See Also
    --------
    :class:`~ColumnCP01`
        Base column definition extended by this class.
    """
    hinge_node_i: Node
    hinge_node_j: Node

    @property
    def hinge_i_tag(self) -> int:
        """
        Returns
        -------
        int
            Tag of hinge element at the start of the column.
        """
        return self.ele_node_i.tag

    @property
    def hinge_j_tag(self) -> int:
        """
        Returns
        -------
        int
            Tag of hinge element at the end of the column.
        """
        return self.ele_node_j.tag

    def set_ele_node_i(self) -> None:
        """Initialize and set ele_node_i based on hinge_node_i.
        """
        coords = self.hinge_node_i.coordinates.copy()
        tag = int(self.hinge_node_i.tag + 100000)
        self.ele_node_i = Node(tag, coords)

    def set_ele_node_j(self) -> None:
        """Initialize and set ele_node_j based on hinge_node_j.
        """
        coords = self.hinge_node_j.coordinates.copy()
        tag = int(self.hinge_node_j.tag + 100000)
        self.ele_node_j = Node(tag, coords)

    def add_to_ops(self) -> None:
        """Adds column components to the OpenSees domain
        (i.e, plastic hinges, elastic column element and nodes).

        Notes
        -----
        Same hinge materials are used at both ends.
        """
        # Create column element nodes
        self.ele_node_i.add_to_ops()
        self.ele_node_j.add_to_ops()

        # Create elastic column element
        ops.element(*self._get_elastic_ele_inputs())

        # Create plastic hinge materials
        ops.uniaxialMaterial(*self._get_rot_hinge_mat_inputs('x'))
        ops.uniaxialMaterial(*self._get_rot_hinge_mat_inputs('y'))
        if not self.capacity_design:
            vy_mat, vy_curve = self._get_shear_hinge_mat_inputs('y')
            vz_mat, vz_curve = self._get_shear_hinge_mat_inputs('x')
            ops.limitCurve(*vy_curve)
            ops.uniaxialMaterial(*vy_mat)
            ops.limitCurve(*vz_curve)
            ops.uniaxialMaterial(*vz_mat)

        # Create plastic hinge section
        ops.section(*self._get_inelastic_sec_inputs())

        # Create plastic hinge elements at both ends
        hinge_i_ele_inputs, hinge_j_ele_inputs = self._get_hinge_ele_inputs()
        ops.element(*hinge_i_ele_inputs)
        ops.element(*hinge_j_ele_inputs)

    def to_py(self) -> List[str]:
        """Gets the Python commands to construct beam components in OpenSees
        domain (i.e, plastic hinges, elastic beam element and nodes).

        Returns
        -------
        List[str]
            List of Python commands for constructing the components of beam
            object in OpenSees.
        """
        # Create beam element nodes
        content = ['# Create elastic beam element nodes']
        content.append(self.ele_node_i.to_py())
        content.append(self.ele_node_j.to_py())

        # Create elastic beam element
        content.append('# Create elastic beam element')
        elastic_ele_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_elastic_ele_inputs()
        )
        content.append(f"ops.element({elastic_ele_inputs})")

        # Create plastic hinge materials
        content.append('# Create plastic hinge materials')
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
        if not self.capacity_design:  # New shear materials
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

        # Create plastic hinge section
        content.append('# Create plastic hinge section')
        inelastic_sec_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_inelastic_sec_inputs()
        )
        content.append(f"ops.section({inelastic_sec_inputs})")

        # Create plastic hinge elements
        content.append('# Create plastic hinge elements')
        hinge_i_ele_inputs, hinge_j_ele_inputs = self._get_hinge_ele_inputs()
        hinge_i_ele_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in hinge_i_ele_inputs
        )
        hinge_j_ele_inputs = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in hinge_j_ele_inputs
        )
        content.append(f"ops.element({hinge_i_ele_inputs})")
        content.append(f"ops.element({hinge_j_ele_inputs})")

        return content

    def to_tcl(self) -> List[str]:
        """Gets the Tcl commands to construct beam components in OpenSees
        domain (i.e, plastic hinges, elastic beam element and nodes).

        Returns
        -------
        List[str]
            List of Tcl commands for constructing the components of beam
            object in OpenSees.
        """
        # Create beam element nodes
        content = ['# Create elastic beam element nodes']
        content.append(self.ele_node_i.to_tcl())
        content.append(self.ele_node_j.to_tcl())

        # Create elastic beam element
        content.append('# Create elastic beam element')
        elastic_ele_inputs = ' '.join(
            f'{item}' for item in self._get_elastic_ele_inputs()
        )
        content.append(f"element {elastic_ele_inputs}")

        # Create plastic hinge materials
        content.append('# Create plastic hinge materials')
        mz_mat_inputs = ' '.join(
            f"{item}" for item in self._get_rot_hinge_mat_inputs('x'))
        my_mat_inputs = ' '.join(
            f"{item}" for item in self._get_rot_hinge_mat_inputs('y'))
        content.append(f"uniaxialMaterial {mz_mat_inputs}")
        content.append(f"uniaxialMaterial {my_mat_inputs}")
        if not self.capacity_design:  # New shear materials
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

        # Create plastic hinge section
        content.append('# Create plastic hinge section')
        inelastic_sec_inputs = ' '.join(
            f"{item}" for item in self._get_inelastic_sec_inputs())
        content.append(f"section {inelastic_sec_inputs}")

        # Create plastic hinge elements at both ends
        content.append('# Create plastic hinge elements')
        hinge_i_ele_inputs, hinge_j_ele_inputs = self._get_hinge_ele_inputs()
        hinge_i_ele_inputs = ' '.join(f"{item}" for item in hinge_i_ele_inputs)
        hinge_j_ele_inputs = ' '.join(f"{item}" for item in hinge_j_ele_inputs)
        content.append(f"element {hinge_i_ele_inputs}")
        content.append(f"element {hinge_j_ele_inputs}")

        return content

    def _get_hinge_ele_inputs(self) -> Tuple[List[str | float | int],
                                             List[str | float | int]]:
        """Retrieves plastic hinge element inputs (zero-length spring).

        Returns
        -------
        hinge_i_ele_inputs : List[str | float | int]
            Element inputs for the hinge at the start section.
        hinge_j_ele_inputs : List[str | float | int]
            Element inputs for the hinge at the end section.
        """
        # Nodes
        hinge_i_nodes = [self.hinge_node_i.tag, self.ele_node_i.tag]
        hinge_j_nodes = [self.ele_node_j.tag, self.hinge_node_j.tag]
        # Section orientation
        vecx = [0.0, 0.0, 1.0]
        vecyp = [0.0, 1.0, 0.0]
        orientation = [*vecx, *vecyp]  # cross product is vecz = [-1, 0, 0]
        # Element inputs
        hinge_i_inputs = [
            'zeroLengthSection', self.hinge_i_tag, *hinge_i_nodes,
            self.inelastic_sec_tag, '-orient', *orientation
        ]
        hinge_j_inputs = [
            'zeroLengthSection', self.hinge_j_tag, *hinge_j_nodes,
            self.inelastic_sec_tag, '-orient', *orientation
        ]
        return hinge_i_inputs, hinge_j_inputs

    def _get_elastic_ele_inputs(self) -> List[float]:
        """Retrieves elastic column element inputs.

        Returns
        -------
        List[float]
            List of elastic column element inputs.
        """
        # Ibarra and Krawinkler (2005) - Equation B.3
        n_factor = 10  # n=10 is used in the reference
        if self.cracked_section:
            Iz_mod = self._Ix_eff * (n_factor + 1) / n_factor
            Iy_mod = self._Iy_eff * (n_factor + 1) / n_factor
        else:
            Iz_mod = self.design.Ix * (n_factor + 1) / n_factor
            Iy_mod = self.design.Iy * (n_factor + 1) / n_factor
        # List of elasticBeamColumn element inputs
        ele_inputs = round_list([
            'elasticBeamColumn', self.design.line.tag,
            self.ele_node_i.tag, self.ele_node_j.tag,
            self.design.Ag, self.Ecm_q, self.Gcm_q,
            self.design.J, Iy_mod, Iz_mod, PDELTA_TRANSF_Z
        ])

        return ele_inputs

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

        # Elastic stiffness modification factor
        n_factor = 10  # n=10 is used in Ibarra and Krawinkler (2005)

        # Rotation values
        theta_1 = theta_y / n_factor
        theta_2 = (theta_y / n_factor) + theta_cap_pl
        theta_3 = (theta_y / n_factor) + theta_cap_pl + theta_pc

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
