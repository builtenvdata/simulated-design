"""This module provides base classes for representing beam-column joints
within the BNSM layer.

The module includes:

- ``JointBase``: abstract interface for joint objects, including access to
  design properties and common functionality.
- ``StairsJointBase``: mid-storey (stairs) joint implementation that creates
  a central joint node used to connect offset beam and column elements.
- ``FloorJointBase``: floor-level joint implementation that can optionally
  model joint flexibility (rigid, elastic, or inelastic).
"""
# Imports from installed packages
from abc import ABC, abstractmethod
import numpy as np
import openseespy.opensees as ops
from typing import Dict, List, Literal

# Imports from bdim base library
from ...bdim.baselib.joint import JointBase as JointDesign

# Imports from bnsm library
from .node import Node
from .constants import RIGID_MAT

# Imports from utils library
from ....utils.misc import PRECISION, round_list


class JointBase(ABC):
    """Abstract base class for beam-column joint implementations in the BNSM
    layer.

    Attributes
    ----------
    design : JointDesign
        Instance of joint design information model.
    """
    design: JointDesign

    @property
    def bx(self) -> float:
        """Joint width along global x-axis.

        Returns
        -------
        float
            Joint width along global x-axis (based on columns' section widths).
        """
        bx = 0.0
        if self.design.top_column:
            bx = max(bx, self.design.top_column.bx)
        if self.design.bottom_column:
            bx = max(bx, self.design.bottom_column.bx)
        return bx

    @property
    def by(self) -> float:
        """Joint width along global y-axis.

        Returns
        -------
        float
            Joint width along global y-axis (based on columns' section widths).
        """
        by = 0.0
        if self.design.top_column:
            by = max(by, self.design.top_column.by)
        if self.design.bottom_column:
            by = max(by, self.design.bottom_column.by)
        return by

    @property
    def h(self) -> float:
        """Joint height based on all beam section heights.

        Returns
        -------
        float
            Joint height based on all beam section heights.

        Notes
        -----
        The largest of the beam heights is selected.
        """
        h = 0.0
        if self.design.left_beam:
            h = max(h, self.design.left_beam.h)
        if self.design.right_beam:
            h = max(h, self.design.right_beam.h)
        if self.design.rear_beam:
            h = max(h, self.design.rear_beam.h)
        if self.design.front_beam:
            h = max(h, self.design.front_beam.h)

        return h

    @property
    def fcm(self) -> float:
        """Mean concrete compressive strength.

        Returns
        -------
        float
            Mean value of concrete compressive strength (in base units).
        """
        return self.design.fcm

    @abstractmethod
    def add_to_ops(self) -> None:
        """Adds joint model objects to the OpenSees domain.
        """
        pass

    @abstractmethod
    def to_py(self) -> List[str]:
        """Gets the Python commands to define joint model objects in
        the OpenSees domain.

        Returns
        -------
        List[str]
            List of Python commands for constructing the components of joint
            in OpenSees.
        """
        pass

    @abstractmethod
    def to_tcl(self) -> List[str]:
        """Gets the Tcl commands to define joint model objects in
        the OpenSees domain.

        Returns
        -------
        List[str]
            List of Tcl commands for constructing the components of joint
            in OpenSees.
        """
        pass


class StairsJointBase(JointBase):
    """Base class implementation used in the BNSM layer to represent
    beam-column joints at a mid-storey level (stairs joint). It provides
    methods to define a stairs joint in the OpenSees domain and to export
    equivalent Python and Tcl commands.

    The mid-storey joint modelling approach follows macro-model formulations,
    where joint behaviour is represented through rotational springs based on
    O'Reilly 2016.

    References
    ----------
    O'Reilly, G. J. (2016). Performance-based seismic assessment and
    retrofit of existing RC frame buildings in Italy
    (Doctoral dissertation, IUSS Pavia).

    Attributes
    ----------
    center_node : Node
        Central joint node for connecting nodes at joint offset distances.

    See Also
    --------
    :class:`~JointBase`
        Base class joint definition extended by this class.
    """
    center_node: Node

    def __init__(self, design: JointDesign, mass: float) -> None:
        """Initialize StairsJointBase object.

        Parameters
        ----------
        design : JointDesign
            Reference design information of joint.
        mass : float
            Total mass assigned to joint.
        """
        # Save reference design information of joint
        self.design = design
        # Set reference node properties
        ref_point = self.design.elastic_node
        ref_tag = ref_point.tag
        ref_coords = ref_point.coordinates
        # Initialize center node
        masses = [mass, mass, mass, 0.0, 0.0, 0.0]
        self.center_node = Node(ref_tag, ref_coords, masses)

    def add_to_ops(self) -> None:
        """Adds stairs joint model objects to the OpenSees domain
        (i.e., nodes).
        """
        # Central joint node
        self.center_node.add_to_ops()

    def to_py(self) -> List[str]:
        """Gets the Python commands to define stairs joint model objects in
        the OpenSees domain (i.e., joint node).

        Returns
        -------
        List[str]
            List of Python commands for constructing the components of stairs
            joint in OpenSees.
        """
        grids = ', '.join([f"{i}" for i in self.design.elastic_node.grid_ids])
        content = [f'# Joint grid ids (x, y, z): ({grids})']
        content.append(self.center_node.to_py())

        return content

    def to_tcl(self) -> List[str]:
        """Gets the Tcl commands to define stairs joint model objects in
        the OpenSees domain (i.e., joint node).

        Returns
        -------
        List[str]
            List of Tcl commands for constructing the components of stairs
            joint in OpenSees.
        """
        grids = ', '.join([f"{i}" for i in self.design.elastic_node.grid_ids])
        content = [f'# Joint grid ids (x, y, z): ({grids})']
        content.append(self.center_node.to_tcl())

        return content


class FloorJointBase(StairsJointBase):
    """Base class implementation used in the BNSM layer to represent
    beam-column joints at a floor level. It provides methods to define an
    floor-level joint in the OpenSees domain and to export equivalent
    Python and Tcl commands.

    Attributes
    ----------
    floor_node : Node
        Floor node which is constrained by the floor diaphragm.
    flexibility_model : Literal['inelastic', 'elastic', 'rigid']
        Joint flexibility model.
    axial_force : float
        Axial force acting on joint.

    See Also
    --------
    :class:`~StairsJointBase`
        Mid-storey (stairs) joint definition that this class extends.
    """
    floor_node: Node
    flexibility_model: Literal["inelastic", "elastic", "rigid"]
    axial_force: float

    @property
    def mz_tag(self) -> int:
        """Material tag for the joint hinge about global-z (Mz).

        Returns
        -------
        int
            Material tag for the joint hinge about global-z (Mz).
        """
        return int(300000 + self.center_node.tag)

    @property
    def my_tag(self) -> int:
        """Material tag for the joint hinge about global-y (My).

        Returns
        -------
        int
            Material tag for the joint hinge about global-y (My).
        """
        return int(400000 + self.center_node.tag)

    @property
    def sec_tag(self) -> int:
        """Tag of aggregated beam-column joint element section.

        Returns
        -------
        int
            Tag of aggregated beam-column joint element section.
        """
        return int(self.floor_node.tag)

    @property
    def ele_tag(self) -> int:
        """Tag of beam-column joint element.

        Returns
        -------
        int
            Tag of beam-column joint element.
        """
        return int(self.floor_node.tag)

    @property
    def fcm(self) -> float:
        """Mean concrete compressive strength.

        Returns
        -------
        float
            Mean value of concrete compressive strength (in base units).
        """
        return self.design.fcm

    @property
    def hstorey(self) -> float:
        """Internal storey height.

        Returns
        -------
        float
            Internal storey height.

        Notes
        -----
        The equations were derived using constant storey height.
        If possible the average one is used.
        """
        if self.design.top_column is None:
            return self.design.bottom_column.H
        elif self.design.bottom_column is None:
            return self.design.top_column.H
        else:
            return self.design.top_column.H

    def __init__(self, design: JointDesign, mass: float,
                 model: Literal["inelastic", "elastic", "rigid"],
                 load_factors: Dict[Literal['G', 'Q'], float]) -> None:
        """Initialize FloorJointBase object.

        Parameters
        ----------
        design : JointDesign
            Reference design information of joint.
        mass : float
            Total mass assigned to joint.
        model : Literal["inelastic", "elastic", "rigid"]
            Joint flexibility model.
        load_factors : Dict[Literal['G', 'Q'], float]
            Load factors used to compute axial load on joint.
        """
        # Save joint flexibility model option
        self.flexibility_model = model
        # Initialize the nodes in stairs joint
        super().__init__(design, mass)
        # Set the joint node constrained by the floor diaphragm
        if model == 'rigid':
            # There is no need to create additional joint node
            self.floor_node = self.center_node
        else:
            # Initialize the new node to account for joint flexibility
            self.floor_node = Node(
                self.design.elastic_node.tag + 10000,
                self.design.elastic_node.coordinates
            )
        # Axial force on the joint
        if self.design.bottom_column:
            self.axial_force = (
                load_factors['G'] * self.design.bottom_column.hinge_Ng
                + load_factors['Q'] * self.design.bottom_column.hinge_Nq
            )
            # forces = (
            #     load_factors['G'] *
            #     self.design.bottom_column.forces['G/seismic'] +
            #     load_factors['Q'] *
            #     self.design.bottom_column.forces['Q/seismic']
            # )
            # self.axial_load = -forces.N9
        else:
            raise ValueError(
                "Bottom column is missing, joint model won't work here.")

    def add_to_ops(self) -> None:
        """Adds floor joint model objects to the OpenSees domain
        (i.e., joint nodes and flexibility element).
        """
        # Add center joint node connected to beam-column elements
        super().add_to_ops()
        # Add joint flexibility element for no-rigid joint cases
        if self.flexibility_model != 'rigid':
            # Add floor joint node constrained by the floor diaphragm
            self.floor_node.add_to_ops()
            # Materials defining flexible rotation behaviour
            ops.uniaxialMaterial(*self._get_mat_inputs('X'))
            ops.uniaxialMaterial(*self._get_mat_inputs('Y'))
            # Create the new section with flexible rotation behaviour
            ops.section(*self._get_agg_sec_inputs())
            # Create the joint flexibility element
            ops.element(*self._get_ele_inputs())

    def to_py(self) -> List[str]:
        """Gets the Python commands to define floor joint model objects in
        the OpenSees domain (i.e., joint nodes and flexibility element).

        Returns
        -------
        List[str]
            List of Python commands for constructing the components of floor
            joint in OpenSees.
        """
        content = super().to_py()
        content.append(f"# Joint flexibility model: {self.flexibility_model}")
        # Add joint flexibility element for no-rigid joint cases
        if self.flexibility_model != 'rigid':
            # Add floor joint node constrained by the floor diaphragm
            note = ' # Constrained floor node'
            content.append(self.floor_node.to_py() + note)
            # Materials defining flexible rotation behaviour
            mz_mat_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in self._get_mat_inputs('X')
            )
            my_mat_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in self._get_mat_inputs('Y')
            )
            content.append(f"ops.uniaxialMaterial({mz_mat_inputs})")
            content.append(f"ops.uniaxialMaterial({my_mat_inputs})")
            # Create the new section with flexible rotation behaviour
            sec_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in self._get_agg_sec_inputs()
            )
            content.append(f"ops.section({sec_inputs})")
            # Create the joint flexibility element
            ele_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in self._get_ele_inputs()
            )
            content.append(f"ops.element({ele_inputs})")

        return content

    def to_tcl(self) -> List[str]:
        """Gets the Tcl commands to define floor joint model objects in
        the OpenSees domain (i.e., joint nodes and flexibility element).

        Returns
        -------
        List[str]
            List of Tcl commands for constructing the components of floor
            joint in OpenSees.
        """
        content = super().to_tcl()
        content.append(f"# Joint flexibility model: {self.flexibility_model}")
        # Add joint flexibility element for no-rigid joint cases
        if self.flexibility_model != 'rigid':
            # Add floor joint node constrained by the floor diaphragm
            note = ' # Constrained floor node'
            content.append(self.floor_node.to_tcl() + note)
            # Materials defining flexible rotation behaviour
            mz_mat_inputs = ' '.join(
                f'{item}' for item in self._get_mat_inputs('X')
            )
            my_mat_inputs = ' '.join(
                f'{item}' for item in self._get_mat_inputs('Y')
            )
            content.append(f"uniaxialMaterial {mz_mat_inputs}")
            content.append(f"uniaxialMaterial {my_mat_inputs}")
            # Create the new section with flexible rotation behaviour
            sec_inputs = ' '.join(
                f'{item}' for item in self._get_agg_sec_inputs()
            )
            content.append(f"section {sec_inputs}")
            # Create the joint flexibility element
            ele_inputs = ' '.join(
                f'{item}' for item in self._get_ele_inputs()
            )
            content.append(f"element {ele_inputs} ")
        return content

    def _get_mat_inputs(self, axis: Literal['X', 'Y']
                        ) -> List[str | float | int]:
        """Gets the inputs for joint material around the specified global axis.

        Parameters
        ----------
        axis : Literal['X', 'Y']
            The axis about which the rotational behaviour is represented.

        Returns
        -------
        mat_inputs : List[str | float | int]
            List of inputs for the material representing rotational behaviour
            around the specified global axis.
        """
        # Materials defining flexible rotation behaviour
        if self.flexibility_model == 'elastic':  # Elastic rotation
            return self._get_elastic_joint_params(axis)
        elif self.flexibility_model == 'inelastic':  # Inelastic rotation
            return self._get_inelastic_joint_params(axis)

    def _get_elastic_joint_params(self, axis: Literal['X', 'Y']
                                  ) -> List[str | float | int]:
        """Gets the parameters for elastic joint materials.

        Parameters
        ----------
        axis : Literal['X', 'Y']
            The axis about which the rotational behaviour is represented.

        Returns
        -------
        mat_inputs : List[str | float | int]
            List of inputs for the material representing elastic rotational
            behaviour around the specified global axis.

        Notes
        -----
        Even though original implementation by Gerard O'Reilly used the
        expression for interior joints, I believe this was done for the
        sake of simplicity. Herein, we use the corresponding equations.
        """
        # Get the hysteretic material inputs
        params = self._get_inelastic_joint_params(axis)

        # Compute elastic stiffness values
        k_el = params[2] / params[3]

        # Material inputs
        mat_inputs = ['Elastic', params[1], round(float(k_el), PRECISION)]

        return mat_inputs

    def _get_inelastic_joint_params(self, axis: Literal['X', 'Y'] = 'X'
                                    ) -> List[str | float | int]:
        """Gets the material properties for inelastic joint behaviour, i.e.,
        hysteretic material model parameters.

        Parameters
        ----------
        axis : Literal['X', 'Y']
            The axis about which the rotational behaviour is represented.

        Returns
        -------
        mat_inputs : List[str | float | int]
            List of inputs for the material representing inelastic rotational
            behaviour around the specified global axis.

        Notes
        -----
        The constants are slightly different than those in the references.
        The new calibrated values were directly provided by Gerard O'Reilly.

        References
        ----------
        O'Reilly, G. J. (2016). Performance-based seismic assessment and
        retrofit of existing RC frame buildings in Italy
        (Doctoral dissertation, IUSS Pavia).

        O'Reilly, G. J., & Sullivan, T. J. (2019). Modeling techniques for
        the seismic assessment of the existing Italian RC frame structures.
        Journal of Earthquake Engineering, 23(8), 1262-1296.

        GitHub - gerardjoreilly/Numerical-Modelling-of-GLD-RC-Frames: Set of
        OpenSees procedures used to model RC frames designed prior to the 1970s
        in Italy, as outlined and calibrated in O'Reilly & Sullivan [2019].
        https://github.com/gerardjoreilly/Numerical-Modelling-of-GLD-RC-Frames.
        Accessed 21 Oct 2024.

        TODO
        ----
        Due to the lack of data, equation described for roof was not validated.
        However, we rarely expect nonlinearity for joints at the last floor.
        So, this has the least significance.
        """
        # Flexural material around global X direction, beams are in global Y
        if axis == 'X':
            # Beam width
            bb = 0.0
            if self.design.rear_beam:
                bb = max(bb, self.design.rear_beam.b)
            if self.design.front_beam:
                bb = max(bb, self.design.front_beam.b)
            # Beam height
            hb = 0.0
            if self.design.rear_beam:
                hb = max(hb, self.design.rear_beam.h)
            if self.design.front_beam:
                hb = max(hb, self.design.front_beam.h)
            # Column width
            bc = self.bx
            # Column height
            hc = self.by
            # Joint type (location)
            if None in [self.design.front_beam, self.design.rear_beam]:
                jnt_type = 'exterior'
            else:
                jnt_type = 'interior'
            # Material tag
            mat_tag = self.mz_tag

        # Flexural material around global Y direction, beams are in global X
        if axis == 'Y':
            # Beam width
            bb = 0.0
            if self.design.left_beam:
                bb = max(bb, self.design.left_beam.b)
            if self.design.right_beam:
                bb = max(bb, self.design.right_beam.b)
            # Beam height
            hb = 0.0
            if self.design.left_beam:
                hb = max(hb, self.design.left_beam.h)
            if self.design.right_beam:
                hb = max(hb, self.design.right_beam.h)
            # Column width
            bc = self.by
            # Column height
            hc = self.bx
            # Joint type (location)
            if None in [self.design.left_beam, self.design.right_beam]:
                jnt_type = 'exterior'
            else:
                jnt_type = 'interior'
            # Material tag
            mat_tag = self.my_tag

        # Joint type (location) - Roof case
        if self.design.top_column is None:
            jnt_type = 'roof'

        # Lever arm, i.e., distance between comp. and tens. forces
        jd = 0.9 * (0.9 * hb)

        # Joint width definition Equation 2.48 (O'Reilly, 2016)
        # NZS 3101-1 (2006) 15.3.4 Equations A2(a) and A2(b)
        if bc >= bb:
            bj = min(bc, bb + 0.5 * hc)
        else:
            bj = min(bb, bc + 0.5 * hc)

        # Get Hysteretic material parameters
        if jnt_type == 'roof':
            # Shear strength coefficients for each LS: cracking, peak, ultimate
            kappa = 2 * [0.132, 0.132, 0.053]
            # Principle tensile stress values Equation 2.34 (O'Reilly, 2016)
            pt = np.array(kappa) * (self.fcm**0.5)
            # Stress values for material, comes from the model on GitHub.
            mj = (
                2 * (pt * bj * hc) * jd
                * (
                    (hb / (2 * hc))
                    + (
                        (hb / (2 * hc)) ** 2
                        + 1
                        + (self.axial_force / (pt * bj * hc))
                    )
                    ** 0.5
                )
            )
            # Shear deformations for each limit state: cracking, peak, ultimate
            gamma = 2 * [0.0002, 0.0132, 0.0270]  # strain values
            # Hysteretic parameters (pinchx, pinchy, damage1, damage2, beta)
            hyst_params = [0.6, 0.2, 0.0, 0.0, 0.3]

        elif jnt_type == 'exterior':
            # Shear strength coefficients for each LS: cracking, peak, ultimate
            kappa = 2 * [0.132, 0.132, 0.053]
            # Principle tensile stress values Equation 2.34 (O'Reilly, 2016)
            pt = np.array(kappa) * (self.fcm**0.5)
            # Stress values for material, Equation 2.33 (O'Reilly, 2016)
            mj = (
                (pt * bj * hc)
                * (self.hstorey * jd)
                / (self.hstorey - jd)
                * (
                    (hb / (2 * hc))
                    + (
                        (hb / (2 * hc)) ** 2
                        + 1
                        + (self.axial_force / (pt * bj * hc))
                    )
                    ** 0.5
                )
            )
            # Shear deformations for each limit state: cracking, peak, ultimate
            gamma = 2 * [0.0002, 0.0132, 0.0270]  # strain values
            # Hysteretic parameters (pinchx, pinchy, damage1, damage2, beta)
            hyst_params = [0.6, 0.2, 0.0, 0.0, 0.3]

        else:
            # Shear strength coefficients for each LS: cracking, peak, ultimate
            kappa = 2 * [0.29, 0.42, 0.42]
            # Principle tensile stress values Equation 2.34 (O'Reilly, 2016)
            pt = np.array(kappa) * (self.fcm**0.5)
            # Stress values for material, Equation 2.55 (O'Reilly, 2016)
            mj = (
                (pt * bj * hc)
                * (self.hstorey * jd)
                / (self.hstorey - jd)
                * (1 + (self.axial_force / (pt * bj * hc))) ** 0.5
            )
            # Shear deformations for each limit state: cracking, peak, ultimate
            gamma = 2 * [0.0002, 0.0090, 0.0200]  # strain values
            # Hysteretic parameters (pinchx, pinchy, damage1, damage2, beta)
            hyst_params = [0.6, 0.2, 0.0, 0.01, 0.3]

        # Inputs for material representing rotational behaviour
        mat_params = []
        for i in range(6):
            if i < 3:
                mat_params.extend([mj[i], gamma[i]])
            else:
                mat_params.extend([-mj[i], -gamma[i]])
        # Add hysteretic parameters
        mat_params.extend(hyst_params)
        # Rounding to precision
        mat_inputs = round_list(['Hysteretic', mat_tag] + mat_params)

        return mat_inputs

    def _get_agg_sec_inputs(self) -> List[str | int]:
        """Retrieves aggregation section inputs.

        Returns
        -------
        sec_inputs : List[str | int]
            List of aggregation section inputs.
        """
        sec_inputs = [
            'Aggregator', self.sec_tag,
            RIGID_MAT, 'P', RIGID_MAT, 'Vy', RIGID_MAT, 'Vz',
            self.my_tag, 'My', self.mz_tag, 'Mz', RIGID_MAT, 'T'
        ]
        # Rounding
        sec_inputs = round_list(sec_inputs)

        return sec_inputs

    def _get_ele_inputs(self) -> List[str | int | float]:
        """Retrieves joint element inputs.

        Returns
        -------
        ele_inputs : List[str | int | float]
            List of joint element inputs.
        """
        # Vector components in global coordinates defining local x-axis
        x1, x2, x3 = 0, 0, 1
        # Vector components in global coordinates defining vector yp which
        # lies in the local x-y plane for the element
        yp1, yp2, yp3 = 0, 1, 0
        # Flag for rayleigh damping
        rFlag = 0

        ele_inputs = [
            'zeroLengthSection', self.ele_tag,
            self.center_node.tag, self.floor_node.tag,
            self.sec_tag, '-orient', x1, x2, x3, yp1, yp2, yp3,
            '-doRayleigh', rFlag
        ]

        return ele_inputs
