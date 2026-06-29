"""This module provides the column class implementation for the ``DP03`` model
in the BNSM layer.
"""
# Imports from installed packages
import numpy as np
import openseespy.opensees as ops
from typing import Literal, List

# Imports from bnsm base library
from ..baselib.column import ColumnBase

# Imports from utils library
from ....utils.units import MPa, mm
from ....utils.misc import round_list
from ....utils.rcsection import (
    get_mander_confinement, build_column_rebar_layout
)


class Column(ColumnBase):
    """Column implementation for the ``DP03`` model.

    This class extends ``ColumnBase`` by defining fiber sections at the plastic
    hinge regions. The column is modeled using a force-based beam-column
    element with a plastic hinge integration scheme. Nonlinear behavior is
    distributed over specified hinge lengths at the member ends, while the
    interior region remains elastic.

    The hinge sections are discretized into concrete and steel fibers, where
    each fiber is associated with a uniaxial material model. The section
    response is obtained by integrating stresses over the fibers, enabling
    axial force-bending moment interaction to be captured. The interior region
    is modeled as elastic using cracked section properties. The shear response
    is represented as in the base class.

    Attributes
    ----------
    concrete_material : Literal['Concrete01', 'Concrete04'], optional
        Uniaxial material type for concrete, by default 'Concrete04'.
    interior_section : Literal['Elastic', 'Inelastic'], optional
        Interior section used in the plastic hinge integration formulation,
        by default 'Inelastic'.

    See Also
    --------
    :class:`~ColumnBase`
        Base column definition extended by this class.
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
        return (4700 * (fc_mpa**0.5)) * MPa

    @property
    def steel_mat_tag_(self) -> int:
        """Steel material tag."""
        return int(str(self.design.line.tag) + '990')

    @property
    def steel_mat_tag(self) -> int:
        """MinMax material tag for the steel fibers. Used to simulate
        bar buckling or rupture."""
        return int(str(self.design.line.tag) + '991')

    @property
    def uconf_conc_mat_tag(self) -> int:
        """Material tag for the unconfined concrete fibers."""
        return int(str(self.design.line.tag) + '992')

    @property
    def conf_conc_mat_tag(self) -> int:
        """Material tag for the confined concrete fibers."""
        return int(str(self.design.line.tag) + '993')

    @property
    def inelastic_fiber_sec_tag(self) -> int:
        """Section tag for the inelastic fiber section."""
        return int(str(self.design.line.tag) + '991')

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
        ops.uniaxialMaterial(*self._get_steel_mat_inputs())
        ops.uniaxialMaterial(*self._get_steel_minmax_mat_inputs())
        ops.uniaxialMaterial(*self._get_unconfined_concrete_mat_inputs())
        ops.uniaxialMaterial(*self._get_confined_concrete_mat_inputs())
        if not self.capacity_design:
            vy_mat, minmax_vy = self._get_shear_hinge_mat_inputs('y')
            vz_mat, minmax_vz = self._get_shear_hinge_mat_inputs('x')
            ops.uniaxialMaterial(*vy_mat)
            ops.uniaxialMaterial(*vz_mat)
            ops.uniaxialMaterial(*minmax_vy)
            ops.uniaxialMaterial(*minmax_vz)

        # Create element sections
        section, fibers, patches = self._get_inelastic_fiber_sec_inputs()
        if self.interior_section == 'Elastic':  # use elastic interior
            ops.section(*self._get_elastic_sec_inputs())
        # Fiber section
        ops.section(*section)
        for fiber in fibers:
            ops.fiber(*fiber)
        for patch in patches:
            ops.patch(*patch)
        if not self.capacity_design:  # Aggregated section
            ops.section(*self._get_inelastic_aggregated_sec_inputs())

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
        # Fiber section materials
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
        conc = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in self._get_confined_concrete_mat_inputs()
        )
        content.append(f"ops.uniaxialMaterial({steel})")
        content.append(f"ops.uniaxialMaterial({steel_minmax})")
        content.append(f"ops.uniaxialMaterial({unconc})")
        content.append(f"ops.uniaxialMaterial({conc})")
        # Uniaxial shear materials
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
        # Interior Section - Elastic
        if self.interior_section == 'Elastic':  # use elastic interior
            elastic_sec_inputs = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in self._get_elastic_sec_inputs()
            )
            content.append(f"ops.section({elastic_sec_inputs})")
        # End Sections - Fiber
        fb_section, fibers, patches = self._get_inelastic_fiber_sec_inputs()
        fb_section = ', '.join(
            repr(item) if isinstance(item, str) else str(item)
            for item in fb_section
        )
        content.append(f"ops.section({fb_section})")
        for fiber in fibers:
            fiber = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in fiber
            )
            content.append(f"ops.fiber({fiber})")
        for patch in patches:
            patch = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in patch
            )
            content.append(f"ops.patch({patch})")
        # End Sections - Aggregate(Fiber + Uniaxial shear)
        if not self.capacity_design:
            agg_section = ', '.join(
                repr(item) if isinstance(item, str) else str(item)
                for item in self._get_inelastic_aggregated_sec_inputs()
            )
            content.append(f"ops.section({agg_section})")

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
        # Fiber section materials
        steel = ' '.join(
            f"{item}" for item in self._get_steel_mat_inputs()
        )
        steel_minmax = ' '.join(
            f"{item}" for item in self._get_steel_minmax_mat_inputs()
        )
        unconc = ' '.join(
            f"{item}" for item in self._get_unconfined_concrete_mat_inputs()
        )
        conc = ' '.join(
            f"{item}" for item in self._get_confined_concrete_mat_inputs()
        )
        content.append(f"uniaxialMaterial {steel}")
        content.append(f"uniaxialMaterial {steel_minmax}")
        content.append(f"uniaxialMaterial {unconc}")
        content.append(f"uniaxialMaterial {conc}")
        # Uniaxial shear materials
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
        # Interior Section - Elastic
        if self.interior_section == 'Elastic':  # use elastic interior
            elastic_sec_inputs = ' '.join(
                f"{item}" for item in self._get_elastic_sec_inputs())
            content.append(f"section {elastic_sec_inputs}")
        # End Sections - Fiber
        fb_section, fibers, patches = self._get_inelastic_fiber_sec_inputs()
        fb_section = ' '.join(f"{item}" for item in fb_section)
        content.append(f"section {fb_section} " + "{")
        for fiber in fibers:
            fiber = ' '.join(f"{item}" for item in fiber)
            content.append(f"    fiber {fiber}")
        for patch in patches:
            patch = ' '.join(f"{item}" for item in patch)
            content.append(f"    patch {patch}")
        content.append("}")
        # End Sections - Aggregate(Fiber + Uniaxial shear)
        if not self.capacity_design:
            agg_section = ' '.join(
                f"{item}" for item in
                self._get_inelastic_aggregated_sec_inputs()
            )
            content.append(f"section {agg_section}")

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

    def _get_inelastic_fiber_sec_inputs(self) -> List[str | float | int]:
        """Retrieves inputs for inelastic fiber column section.

        Returns
        -------
        List[str | float | int]
            List of inputs for inelastic fiber column section.
        """
        # Section and material tags
        sec_tag = self.inelastic_fiber_sec_tag
        conf_con = self.conf_conc_mat_tag
        uconf_con = self.uconf_conc_mat_tag
        steel = self.steel_mat_tag
        # Section geometry
        lx = self.design.bx
        ly = self.design.by
        cv = self.design.cover_q
        # Shear reinforcement
        dbh = self.design.dbh_q
        # Longitudinal reinforcement
        nbl_int_x = int(self.design.nblx_int_q)
        nbl_int_y = int(self.design.nbly_int_q)
        dbl_cor = self.design.dbl_cor_q
        dbl_int = self.design.dbl_int_q

        # Get reinforcement layout
        layout = build_column_rebar_layout(
            dbl_cor, dbl_int, nbl_int_x, nbl_int_y, dbh, lx, ly, cv
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
        cover_y = float(ly / 2)  # The distance from y-axis to the cover edge
        cover_z = float(lx / 2)  # The distance from z-axis to the cover edge
        core_y = float(ly / 2 - cv)  # The dist. from y-axis to the core edge
        core_z = float(lx / 2 - cv)  # The dist. from z-axis to the core edge
        nf_core_y = 8  # num. of fibers for concrete in y-direction - core
        nf_core_z = 8  # num. of fibers for concrete in z-direction - core
        nf_cover_y = 10  # num.r of fibers for concrete in y-direction - cover
        nf_cover_z = 10  # num. of fibers for concrete in z-direction - cover
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

        # Rounding
        section = round_list(section)
        concrete_patches = round_list(concrete_patches)
        steel_fibers = round_list(steel_fibers)

        return section, steel_fibers, concrete_patches

    def _get_inelastic_aggregated_sec_inputs(self) -> List[str | float | int]:
        """Retrieves inputs for inelastic aggregated column section.

        Returns
        -------
        List[str | float | int]
            List of inputs for inelastic aggregated column section.
        """
        sec_inputs = [
            'Aggregator', self.inelastic_sec_tag,
            self.vy_mat_tag, 'Vy',
            self.vz_mat_tag, 'Vz',
            '-section', self.inelastic_fiber_sec_tag
        ]
        return sec_inputs

    def _get_int_inputs(self) -> List[str | float | int]:
        """Retrieves column integration inputs.

        Returns
        -------
        List[str | float | int]
            List of column integration inputs.
        """
        # Inputs for aggregated section with elastic interior
        int_inputs = super()._get_int_inputs()

        if self.capacity_design:
            # Use fiber section
            int_inputs[2], int_inputs[4] = (self.inelastic_fiber_sec_tag,) * 2
            if self.interior_section == 'Inelastic':  # use inelastic interior
                int_inputs[-1] = self.inelastic_fiber_sec_tag
        elif self.interior_section == 'Inelastic':  # use inelastic interior
            int_inputs[-1] = self.inelastic_sec_tag

        return int_inputs

    def _get_confined_concrete_mat_inputs(self) -> List[str | float | int]:
        """Builds OpenSees confined concrete material inputs for the end
        sections.

        Returns
        -------
        List[str | float | int]
            Arguments for ``ops.uniaxialMaterial`` defining a confined concrete
            material ('Concrete01' or 'Concrete04') in OpenSees.

        See Also
        --------
        ``get_mander_confinement``: Computes confined peak stress and strains
        using the Mander model.
        ``build_column_rebar_layout``: Sets rebar coordinates and diameters
        for the column section.

        Notes
        -----
        - Concrete confinement parameters are computed using the Mander model.
        - For Concrete01, residual (crushing) stress is taken as
          ``fpcu = 0.2 * fpc``.
        """
        # Materials [MPa]
        fc = self.design.fc_q / MPa
        fsyh = self.design.fsyh_q / MPa
        # Section geometry [mm]
        lx = self.design.bx / mm
        ly = self.design.by / mm
        cv = self.design.cover_q / mm
        # Shear reinforcement [mm]
        dbh = self.design.dbh_q / mm
        sbh = self.design.sbh_q / mm
        legs_x = int(self.design.nbh_x_q)
        legs_y = int(self.design.nbh_y_q)
        # Longitudinal reinforcement [mm]
        nbl_int_x = int(self.design.nblx_int_q)
        nbl_int_y = int(self.design.nbly_int_q)
        dbl_cor = self.design.dbl_cor_q / mm
        dbl_int = self.design.dbl_int_q / mm

        # Get reinforcement layout
        layout = build_column_rebar_layout(
            dbl_cor, dbl_int, nbl_int_x, nbl_int_y, dbh, lx, ly, cv
        )
        # Determine confinement based on Mander model
        params = get_mander_confinement(
            fc=fc, Lx=lx, Ly=ly, cover=cv, db_v=dbh, s=sbh,
            legs_x=legs_x, legs_y=legs_y, fy_v=fsyh,
            rein_x=layout['rein_x'], rein_y=layout['rein_y'],
            rein_d=layout['rein_d']
        )  # note that strength parameters are in MPa

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
        mat_tags = [self.concrete_material, self.conf_conc_mat_tag]
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

    def _get_steel_mat_inputs(self) -> List[str | float]:
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
