"""This module provides the beam class implementation for the ``DP03`` model in
the BNSM layer.
"""
# Imports from installed packages
import numpy as np
import openseespy.opensees as ops
from typing import List, Literal, Tuple

# Imports from bnsm base library
from ..baselib.beam import BeamBase

# Imports from utils library
from ....utils.units import MPa, mm
from ....utils.misc import round_list
from ....utils.rcsection import get_mander_confinement, build_beam_rebar_layout


class Beam(BeamBase):
    """Beam implementation for the ``DP03`` model.

    This class extends ``BeamBase`` by defining fiber sections at the plastic
    hinge regions. The beam is modeled using a force-based beam-column element
    with a plastic hinge integration scheme. Nonlinear behavior is distributed
    over specified hinge lengths at the member ends, while the interior region
    remains elastic.

    The hinge sections are discretized into concrete and steel fibers, where
    each fiber is associated with a uniaxial material model. The section
    response is obtained by integrating stresses over the fibers, enabling
    axial force-bending moment interaction to be captured. The interior region
    is modeled as elastic using cracked section properties.

    Attributes
    ----------
    concrete_material : Literal['Concrete01', 'Concrete04'], optional
        Uniaxial material type for concrete, by default 'Concrete04'.
    interior_section : Literal['Elastic', 'Inelastic'], optional
        Interior section used in the plastic hinge integration formulation,
        by default 'Inelastic'.

    See Also
    --------
    :class:`~simdesign.rcmrf.bnsm.baselib.beam.BeamBase`
        Base beam definition extended by this class.
    """
    concrete_material: Literal['Concrete01', 'Concrete04'] = 'Concrete04'
    interior_section: Literal['Elastic', 'Inelastic'] = 'Inelastic'

    @property
    def Ecm_q(self) -> float:
        """
        Returns
        -------
        float
            Elastic young's modulus of concrete (in base units).

        References
        ----------
        Priestley, M. J. N., Calvi, G. M., & Kowalsky, M. J. (2007).
        *Displacement-based seismic design of structures*. IUSS Press.
        """
        # Use quality adjusted elastic youngs modulus
        fc_mpa = self.design.fc_q / MPa  # convert to MPa
        return (4700 * (fc_mpa**0.5)) * MPa  # Mander et al. 1988

    @property
    def steel_mat_tag_(self) -> int:
        """Steel material tag."""
        return int(str(self.design.line.tag) + '990')

    @property
    def steel_mat_tag(self) -> int:
        """MinMax material tag for the steel fibers. Used to simulate
        bar buckling or rupture."""
        return int(str(self.design.line.tag) + '992')

    @property
    def uconf_conc_mat_tag(self) -> int:
        """Material tag for the unconfined concrete fibers."""
        return int(str(self.design.line.tag) + '993')

    @property
    def conf_conc_mat_tag_i(self) -> int:
        """Material tag for the confined concrete fibers at the *i-end*."""
        return int(str(self.design.line.tag) + '994')

    @property
    def conf_conc_mat_tag_j(self) -> int:
        """Material tag for the confined concrete fibers at the *j-end*."""
        return int(str(self.design.line.tag) + '995')

    @property
    def conf_conc_mat_tag_m(self) -> int:
        """Material tag for the confined concrete fibers at the *mid-section*.
        """
        return int(str(self.design.line.tag) + '996')

    @property
    def inelastic_sec_m_tag(self) -> int:
        """Section tag for the inelastic middle (interior) section."""
        return int(str(self.design.line.tag) + '993')

    def add_to_ops(self) -> None:
        """Adds beam components to the OpenSees domain
        (i.e, elastic beam element and nodes).
        """
        # Define geometric transformation
        ops.geomTransf(*self._get_geo_transf_inputs())

        # Create the section materials
        ops.uniaxialMaterial(*self._get_steel_mat_inputs())
        ops.uniaxialMaterial(*self._get_steel_minmax_mat_inputs())
        ops.uniaxialMaterial(*self._get_unconfined_concrete_mat_inputs())
        ops.uniaxialMaterial(*self._get_confined_concrete_mat_inputs('i'))
        ops.uniaxialMaterial(*self._get_confined_concrete_mat_inputs('j'))
        if self.interior_section == 'Inelastic':  # use inelastic interior
            ops.uniaxialMaterial(*self._get_confined_concrete_mat_inputs('m'))

        # Create element sections
        sectionI, fibersI, patchesI = self._get_inelastic_sec_inputs('i')
        sectionJ, fibersJ, patchesJ = self._get_inelastic_sec_inputs('j')
        # Section-I
        ops.section(*sectionI)
        for fiber in fibersI:
            ops.fiber(*fiber)
        for patch in patchesI:
            ops.patch(*patch)
        # Section-J
        ops.section(*sectionJ)
        for fiber in fibersJ:
            ops.fiber(*fiber)
        for patch in patchesJ:
            ops.patch(*patch)
        # Section-M / interior section
        if self.interior_section == 'Inelastic':  # use inelastic interior
            sectionM, fibersM, patchesM = self._get_inelastic_sec_inputs('m')
            ops.section(*sectionM)
            for fiber in fibersM:
                ops.fiber(*fiber)
            for patch in patchesM:
                ops.patch(*patch)
        elif self.interior_section == 'Elastic':  # use Elastic interior
            ops.section(*self._get_elastic_sec_inputs())

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
        steel = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_steel_mat_inputs()
        )
        steel_minmax = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_steel_minmax_mat_inputs()
        )
        unconc = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_unconfined_concrete_mat_inputs()
        )
        conc_i = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_confined_concrete_mat_inputs('i')
        )
        conc_j = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_confined_concrete_mat_inputs('j')
        )
        content.append(f"ops.uniaxialMaterial({steel})")
        content.append(f"ops.uniaxialMaterial({steel_minmax})")
        content.append(f"ops.uniaxialMaterial({unconc})")
        content.append(f"ops.uniaxialMaterial({conc_i})")
        content.append(f"ops.uniaxialMaterial({conc_j})")
        if self.interior_section == 'Inelastic':  # use inelastic interior
            conc_m = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in self._get_confined_concrete_mat_inputs('m')
            )
            content.append(f"ops.uniaxialMaterial({conc_m})")

        # Create sections
        content.append('# Create element sections')
        sectionI, fibersI, patchesI = self._get_inelastic_sec_inputs('i')
        sectionJ, fibersJ, patchesJ = self._get_inelastic_sec_inputs('j')
        sectionI = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in sectionI
        )
        sectionJ = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in sectionJ
        )
        # Section-I
        content.append(f"ops.section({sectionI})")
        for fiber in fibersI:
            fiber = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in fiber
            )
            content.append(f"ops.fiber({fiber})")
        for patch in patchesI:
            patch = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in patch
            )
            content.append(f"ops.patch({patch})")
        # Section-J
        content.append(f"ops.section({sectionJ})")
        for fiber in fibersJ:
            fiber = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in fiber
            )
            content.append(f"ops.fiber({fiber})")
        for patch in patchesJ:
            patch = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in patch
            )
            content.append(f"ops.patch({patch})")
        # Section-M / interior section
        if self.interior_section == 'Inelastic':  # use inelastic interior
            sectionM, fibersM, patchesM = self._get_inelastic_sec_inputs('m')
            sectionM = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in sectionM
            )
            content.append(f"ops.section({sectionM})")
            for fiber in fibersM:
                fiber = ', '.join(
                    repr(item) if isinstance(item, str) else str(item)
                    for item in fiber
                )
                content.append(f"ops.fiber({fiber})")
            for patch in patchesM:
                patch = ', '.join(
                    repr(item) if isinstance(item, str) else str(item)
                    for item in patch
                )
                content.append(f"ops.patch({patch})")
        elif self.interior_section == 'Elastic':  # use elastic interior
            elastic_sec_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in self._get_elastic_sec_inputs()
            )
            content.append(f"ops.section({elastic_sec_inputs})")

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
        steel = ' '.join(
            f"{item}" for item in self._get_steel_mat_inputs()
        )
        steel_minmax = ' '.join(
            f"{item}" for item in self._get_steel_minmax_mat_inputs()
        )
        unconc = ' '.join(
            f"{item}" for item in self._get_unconfined_concrete_mat_inputs()
        )
        conc_i = ' '.join(
            f"{item}" for item in self._get_confined_concrete_mat_inputs('i')
        )
        conc_j = ' '.join(
            f"{item}" for item in self._get_confined_concrete_mat_inputs('j')
        )
        content.append(f"uniaxialMaterial {steel}")
        content.append(f"uniaxialMaterial {steel_minmax}")
        content.append(f"uniaxialMaterial {unconc}")
        content.append(f"uniaxialMaterial {conc_i}")
        content.append(f"uniaxialMaterial {conc_j}")
        if self.interior_section == 'Inelastic':  # use inelastic interior
            conc_m = ' '.join(
                f"{item}" for item in
                self._get_confined_concrete_mat_inputs('m')
            )
            content.append(f"uniaxialMaterial {conc_m}")

        # Create sections
        content.append('# Create element sections')
        sectionI, fibersI, patchesI = self._get_inelastic_sec_inputs('i')
        sectionJ, fibersJ, patchesJ = self._get_inelastic_sec_inputs('j')
        sectionI = ' '.join(f"{item}" for item in sectionI)
        sectionJ = ' '.join(f"{item}" for item in sectionJ)
        # Section-I
        content.append(f"section {sectionI} " + "{")
        for fiber in fibersI:
            fiber = ' '.join(f"{item}" for item in fiber)
            content.append(f"    fiber {fiber}")
        for patch in patchesI:
            patch = ' '.join(f"{item}" for item in patch)
            content.append(f"    patch {patch}")
        content.append("}")
        # Section-J
        content.append(f"section {sectionJ} " + "{")
        for fiber in fibersJ:
            fiber = ' '.join(f"{item}" for item in fiber)
            content.append(f"    fiber {fiber}")
        for patch in patchesJ:
            patch = ' '.join(f"{item}" for item in patch)
            content.append(f"    patch {patch}")
        content.append("}")
        # Section-M / interior section
        if self.interior_section == 'Inelastic':  # use inelastic interior
            sectionM, fibersM, patchesM = self._get_inelastic_sec_inputs('m')
            sectionM = ' '.join(f"{item}" for item in sectionM)
            content.append(f"section {sectionM} " + "{")
            for fiber in fibersM:
                fiber = ' '.join(f"{item}" for item in fiber)
                content.append(f"    fiber {fiber}")
            for patch in patchesM:
                patch = ' '.join(f"{item}" for item in patch)
                content.append(f"    patch {patch}")
            content.append("}")
        elif self.interior_section == 'Elastic':  # use elastic interior
            elastic_sec_inputs = ' '.join(
                f"{item}" for item in self._get_elastic_sec_inputs()
            )
            content.append(f"section {elastic_sec_inputs}")
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

    def _get_inelastic_sec_inputs(self, section: Literal['i', 'm', 'j']
                                  ) -> Tuple[list, list, list]:
        """Builds fiber-section inputs for an inelastic beam end section.

        Constructs an OpenSees ``Fiber`` section for the specified beam section
        (i-end, mid-section, j-end), including:
        - the fiber section header (with torsional stiffness ``-GJ``),
        - discrete steel fibers for each longitudinal bar, and
        - rectangular concrete patches for confined core and unconfined cover.

        The rebar coordinates are obtained from ``build_beam_rebar_layout`` and
        then shifted so the section local origin is at the section centroid,
        consistent with OpenSees fiber section conventions (yLoc, zLoc).

        Parameters
        ----------
        section : Literal['i', 'm', 'j']
            Which section to use.

        Returns
        -------
        Tuple[list, list, list]:
            A tuple ``(section, steel_fibers, concrete_patches)`` where:

                **section**: list[str | float | int]
                Inputs for ``ops.section`` defining a fiber section, e.g.::

                    ['Fiber', sec_tag, '-GJ', GJ]

                **steel_fibers**: list[list[str | float | int]]
                Each entry defines a steel fiber for ``ops.fiber`` as::

                    [yLoc, zLoc, area, steel_mat_tag]

                **concrete_patches**: list[list[str | float | int]]
                Patch definitions for ``ops.patch`` using ``'rect'``
                geometry. Includes one confined core patch and four
                unconfined cover patches (bottom/right/top/left).

        Notes
        -----
        - The discretization counts are currently hard-coded.
        """
        # Material and section tags
        if section == 'i':
            idx = 0
            sec_tag = self.inelastic_sec_i_tag
            conf_con = self.conf_conc_mat_tag_i
        elif section == 'm':
            idx = 1
            sec_tag = self.inelastic_sec_m_tag
            conf_con = self.conf_conc_mat_tag_m
        elif section == 'j':
            idx = 2
            sec_tag = self.inelastic_sec_j_tag
            conf_con = self.conf_conc_mat_tag_j
        uconf_con = self.uconf_conc_mat_tag
        steel = self.steel_mat_tag

        # Section geometry [mm]
        lx = self.design.b
        ly = self.design.h
        cv = self.design.cover_q

        # Shear reinforcement [mm]
        dbh = self.design.dbh_q[idx]

        # Longitudinal reinforcement [mm]
        nbl_b1 = int(self.design.nbl_b1_q[idx])
        nbl_b2 = int(self.design.nbl_b2_q[idx])
        dbl_b1 = self.design.dbl_b1_q[idx]
        dbl_b2 = self.design.dbl_b2_q[idx]
        nbl_t1 = int(self.design.nbl_t1_q[idx])
        nbl_t2 = int(self.design.nbl_t2_q[idx])
        dbl_t1 = self.design.dbl_t1_q[idx]
        dbl_t2 = self.design.dbl_t2_q[idx]

        # Set the reinforcement layout
        layout = build_beam_rebar_layout(
            dbl_b1, dbl_b2, dbl_t1, dbl_t2, nbl_b1, nbl_b2, nbl_t1, nbl_t2,
            dbh, lx, ly, cv
        )

        # Steel fibers
        steel_fibers = []
        for x, y, d in zip(layout['rein_x'], layout['rein_y'],
                           layout['rein_d']):
            area = 0.25 * np.pi * d**2
            yLoc = y - ly/2  # Origin is the section center
            zLoc = x - lx/2  # Origin is the section center
            inputs = [float(yLoc), float(zLoc), float(area), steel]
            steel_fibers.append(inputs)

        # Concrete patches
        cover_y = float(ly/2)  # The distance from y-axis to the cover edge
        cover_z = float(lx/2)  # The distance from z-axis to the cover edge
        core_y = float(ly/2 - cv)  # The distance from y-axis to the core edge
        core_z = float(lx/2 - cv)  # The distance from z-axis to the core edge
        nf_core_y = 12  # num. of fibers for concrete in y-direction - core
        nf_core_z = 4  # num. of fibers for concrete in z-direction - core
        nf_cover_y = 12  # num.r of fibers for concrete in y-direction - cover
        nf_cover_z = 4  # num. of fibers for concrete in z-direction - cover
        # Uncofined concrete
        patch_bottom = ['rect', uconf_con, 1, nf_cover_z,
                        -cover_y, -cover_z, -core_y, cover_z]
        patch_right = ['rect', uconf_con, nf_cover_y, 1,
                       -core_y, core_z, core_y, cover_z]
        patch_top = ['rect', uconf_con, 1, nf_cover_z,
                     core_y, -cover_z, cover_y, cover_z]
        patch_left = ['rect', uconf_con, nf_cover_y, 1,
                      -core_y, -cover_z, core_y, -core_z]
        # Confined concrete
        core_patch = ['rect', conf_con, nf_core_y, nf_core_z,
                      -core_y, -core_z, core_y, core_z]
        concrete_patches = [
           core_patch, patch_bottom, patch_right, patch_top, patch_left
        ]
        # Fiber section
        GJ = self.Gcm_q * self.design.J
        section = ['Fiber', sec_tag, '-GJ', GJ]

        section = round_list(section)
        concrete_patches = round_list(concrete_patches)
        steel_fibers = round_list(steel_fibers)

        return section, steel_fibers, concrete_patches

    def _get_int_inputs(self) -> List[str | float]:
        """Retrieves beam integration inputs.

        Returns
        -------
        List[str | int | float]
            List of beam integration inputs.
        """
        int_inputs = super()._get_int_inputs()
        if self.interior_section == 'Inelastic':
            int_inputs[-1] = self.inelastic_sec_m_tag

        return int_inputs

    def _get_confined_concrete_mat_inputs(self, section: Literal['i', 'm', 'j']
                                          ) -> List[str | float | int]:
        """Builds OpenSees confined concrete material inputs for an end
        section.

        Parameters
        ----------
        section : Literal['i', 'm', 'j']
            Which section to use.

        Returns
        -------
        List[str | float | int]
            Arguments for ``ops.uniaxialMaterial`` defining a confined concrete
            material ('Concrete01' or 'Concrete04') in OpenSees.

        See Also
        --------
        ``get_mander_confinement``: Computes confined peak stress and strains
        using the Mander model.
        ``build_beam_rebar_layout``: Sets rebar coordinates and diameters
        for the beam section.

        Notes
        -----
        - Concrete confinement parameters are computed using the Mander model.
        - For Concrete01, residual (crushing) stress is taken as
          ``fpcu = 0.2 * fpc``.
        """
        # Index for the specified end section
        if section == 'i':
            idx = 0
            tag = self.conf_conc_mat_tag_i
        if section == 'm':
            idx = 1
            tag = self.conf_conc_mat_tag_m
        elif section == 'j':
            idx = 2
            tag = self.conf_conc_mat_tag_j

        # Materials [MPa]
        fc = self.design.fc_q / MPa
        fsyh = self.design.fsyh_q / MPa

        # Section geometry [mm]
        lx = self.design.b / mm
        ly = self.design.h / mm
        cv = self.design.cover_q / mm

        # Shear reinforcement [mm]
        dbh = self.design.dbh_q[idx] / mm
        sbh = self.design.sbh_q[idx] / mm
        legs_x = int(self.design.nbh_b_q[idx])
        legs_y = int(self.design.nbh_h_q[idx])

        # Longitudinal reinforcement [mm]
        nbl_b1 = int(self.design.nbl_b1_q[idx])
        nbl_b2 = int(self.design.nbl_b2_q[idx])
        dbl_b1 = self.design.dbl_b1_q[idx] / mm
        dbl_b2 = self.design.dbl_b2_q[idx] / mm
        nbl_t1 = int(self.design.nbl_t1_q[idx])
        nbl_t2 = int(self.design.nbl_t2_q[idx])
        dbl_t1 = self.design.dbl_t1_q[idx] / mm
        dbl_t2 = self.design.dbl_t2_q[idx] / mm

        layout = build_beam_rebar_layout(
            dbl_b1, dbl_b2, dbl_t1, dbl_t2, nbl_b1, nbl_b2, nbl_t1, nbl_t2,
            dbh, lx, ly, cv
        )

        params = get_mander_confinement(
            fc=fc, Lx=lx, Ly=ly, cover=cv, db_v=dbh, s=sbh,
            legs_x=legs_x, legs_y=legs_y, fy_v=fsyh,
            rein_x=layout['rein_x'], rein_y=layout['rein_y'],
            rein_d=layout['rein_d']
        )  # strength parameters are in MPa

        # Set concrete01 material parameters
        if self.concrete_material == 'Concrete01':
            fpc = -params['fcc'] * MPa  # concrete compressive strength
            epsc0 = -params['eps_cc']  # concrete strain at comp. strength
            fpcu = 0.2*fpc  # concrete crushing strength
            epsU = -params['eps_cu']  # concrete strain at crushing strength
            mat_inputs = [fpc, epsc0, fpcu, epsU]
        elif self.concrete_material == 'Concrete04':
            fpc = -params['fcc'] * MPa  # concrete compressive strength
            epsc = -params['eps_cc']  # concrete strain at compressive strength
            epscu = -params['eps_cu']  # concrete strain at crushing strength
            Ec = self.Ecm_q  # elastic modulus
            mat_inputs = [fpc, epsc, epscu, Ec]

        # Rounding
        mat_tags = [self.concrete_material, tag]
        mat_inputs = round_list(mat_tags + mat_inputs)

        return mat_inputs

    def _get_unconfined_concrete_mat_inputs(self) -> List[str | float | int]:
        """Builds cover (unconfined) concrete material inputs for OpenSees.

        Returns
        -------
        List[str | float | int]
            Arguments for ``ops.uniaxialMaterial`` defining an unconfined
            concrete material ('Concrete01' or 'Concrete04') in OpenSees.

        Notes
        -----
        - Peak strain is taken as ``epsc0 = -0.002``.
        - Crushing strain is taken as ``epsU = -0.006``.
        - For Concrete01, residual (crushing) stress is taken as
          ``fpcu = 0.2 * fpc``.
        """
        # Set concrete01 material parameters
        if self.concrete_material == 'Concrete01':
            fpc = -self.design.fc_q  # concrete compressive strength
            epsc0 = -0.002  # concrete strain at compressive strength
            fpcu = 0.2*fpc  # concrete crushing strength
            epsU = -0.006  # concrete strain at crushing strength
            mat_inputs = [fpc, epsc0, fpcu, epsU]
        elif self.concrete_material == 'Concrete04':
            fpc = -self.design.fc_q  # concrete compressive strength
            epsc = -0.002  # concrete strain at compressive strength
            epscu = -0.006  # concrete strain at crushing strength
            Ec = self.Ecm_q  # elastic modulus
            mat_inputs = [fpc, epsc, epscu, Ec]

        # Rounding
        mat_tags = [self.concrete_material, self.uconf_conc_mat_tag]
        mat_inputs = round_list(mat_tags + mat_inputs)

        return mat_inputs

    def _get_steel_mat_inputs(self) -> List[str | float | int]:
        """Builds OpenSees reinforcing steel material inputs.

        Returns
        -------
        List[str | float | int]
            Arguments for ``ops.uniaxialMaterial`` defining a ``Steel01``
            material in OpenSees

        Notes
        -----
        - The strain-hardening ratio is assumed to be 0.005.
        """
        b = 0.005  # strain-hardening ratio - assumed
        Fy = self.design.fsyl_q  # yield strength
        E0 = self.design.Es  # initial elastic tangent
        mat_inputs = ['Steel01', self.steel_mat_tag_, Fy, E0, b]
        mat_inputs = round_list(mat_inputs)

        return mat_inputs

    def _get_steel_minmax_mat_inputs(self) -> List[str | float | int]:
        """Builds OpenSees MinMax wrapper material inputs for reinforcing
        steel.

        Wraps the underlying steel material to cap strains in
        tension/compression, enabling a simple representation of bar rupture or
        buckling limits.

        Returns
        -------
        List[str | float | int]
            Arguments for ``ops.uniaxialMaterial`` defining a ``MinMax``
            material in OpenSees.

        Notes
        -----
        - The same absolute strain limit is used in tension and compression.
        - Here ``epsU = 0.08`` is used per Priestley et al. 2007.
        """
        epsU = 0.08  # bar buckling or bar rupture
        mat_inputs = ['MinMax', self.steel_mat_tag, self.steel_mat_tag_,
                      '-min', -epsU, '-max', epsU]
        mat_inputs = round_list(mat_inputs)

        return mat_inputs
