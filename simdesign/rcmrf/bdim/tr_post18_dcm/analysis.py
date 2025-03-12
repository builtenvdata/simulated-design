# Imports from installed packages
from typing import List
from itertools import product

# Imports from the design class (tr_post18_dcm) library
from .beam import Beam
from .column import Column

# Imports from bdim base library
from ..baselib.analysis import ElasticModelBase
from ..baselib.beam import BeamForces
from ..baselib.column import ColumnForces

"""
Notes
-----
1- Cracked stiffness has been considered in design since 2018.
2- The method named "analyze_for_all" has been overwritten here
to include an overstrength factor of 2.5, which is the value for
RCMRF buildings with high ductility in the case of DTS3 and DTS4.
"""


class ElasticModel(ElasticModelBase):
    """Elastic model builder in OpenSees for design class tr_post18_dcm.
    """
    beams: List[Beam]
    """Beam objects of the building."""
    columns: List[Column]
    """Column objects of the building."""
    OVERSTRENGTH_FACTOR = 2.5

    def build_ops_model_seismic(self) -> None:
        """Builds the model for load cases of seismic load combos.
        """
        self._init_ops_model()
        self._add_ops_nodes()
        self._add_ops_beam_column_elements(True)
        self._add_ops_sp_constraints()
        self._add_ops_mp_constraints()

    def analyze_for_all(self):
        """Analyzes the building all load cases and combinations.

        Stores element forces for each.
        """
        # Seismic load cases
        seismic_load_cases = ["E+X", "E-X", "E+Y", "E-Y"]
        # Distinguish gravity and seismic load combinations
        seismic_combos = self.loads.get_seismic_load_combos()
        # Run all load cases
        self._run_gravity_load_cases()
        if any(seismic_combos):
            self._run_seismic_load_cases()

        # Accidental eccentricity
        ecc = self.loads.eccentricity
        ecc_factors = [ecc / 100, 0.0, -ecc / 100] if ecc != 0 else [0.0]

        # Start combining forces for BEAMS
        for beam in self.beams:
            # Restart combo forces
            beam.design_forces = []
            beam.design_forces_overstrength_adjusted = []
            # Loop through combinations
            for combo in self.loads.combinations:
                # Initialize total combined forces
                forces = BeamForces(0, 0, 0, 0, 0, 0)
                # Determine type of the load combination
                if combo in seismic_combos:
                    combo_type = "seismic"
                else:
                    combo_type = "gravity"
                # Permanent Loads
                if 'G' in combo.loads:
                    gfactor = combo.loads['G']
                    forces += gfactor * beam.forces[f"G/{combo_type}/alpha"]
                # Variable Loads
                if 'Q' in combo.loads:
                    qfactor = combo.loads['Q']
                    forces += qfactor * beam.forces[f"Q/{combo_type}/alpha"]

                if combo_type == 'gravity':
                    # Set the loading case (type)
                    forces.case = combo_type
                    # Append the combined forces
                    beam.design_forces.append(forces)
                else:   # seismic
                    # Add the forces from seismic loading
                    forces_ov = BeamForces(*forces.__dict__.values())
                    ecc_forces = []  # forces due to eccentric loading
                    ecc_forces_ov = []
                    gfactor = combo.masses['G']  # permanent loads factor
                    qfactor = combo.masses['Q']  # variable loads factor
                    for load_case in seismic_load_cases:
                        if load_case in combo.loads:
                            tag = f"{load_case}/{gfactor}G/{qfactor}Q"
                            fact = combo.loads[load_case]
                            forces += fact * beam.forces[tag]
                            forces_ov += self.OVERSTRENGTH_FACTOR * \
                                fact * beam.forces[tag]
                            tmp, tmp_ov = [], []
                            for ecc in ecc_factors:
                                if ecc == 0:
                                    tmp.append(BeamForces(0, 0, 0, 0, 0, 0))
                                    tmp_ov.append(BeamForces(0, 0, 0, 0, 0, 0))
                                else:
                                    tag_e = tag + f"/{ecc}ecc"
                                    tmp.append(fact * beam.forces[tag_e])
                                    tmp_ov.append(self.OVERSTRENGTH_FACTOR *
                                                  fact * beam.forces[tag_e])
                            ecc_forces.append(tmp)
                            ecc_forces_ov.append(tmp_ov)

                    # Possible combinations with eccentric loadings
                    ecc_combos = list(product(*ecc_forces))
                    ecc_combos_ov = list(product(*ecc_forces_ov))
                    for ecc_combo, ecc_combo_ov in zip(ecc_combos,
                                                       ecc_combos_ov):
                        # Add the forces due to ecc. loading
                        forces_ = sum(ecc_combo, forces)
                        forces_ov_ = sum(ecc_combo_ov, forces_ov)
                        # Set the loading case (type)
                        forces_.case = combo_type
                        forces_ov_.case = combo_type
                        # Append the combined forces
                        beam.design_forces.append(forces_)
                        beam.design_forces_overstrength_adjusted.append(
                            forces_ov_)

        # Start combining forces for COLUMNS
        for column in self.columns:
            # Restart combo forces
            column.design_forces = []
            column.design_forces_overstrength_adjusted = []
            # Loop through combinations
            for combo in self.loads.combinations:
                # Initialize total combined forces
                forces = ColumnForces(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                # Determine type of the load combination
                if combo in seismic_combos:
                    combo_type = "seismic"
                else:
                    combo_type = "gravity"
                # Permanent Loads
                if 'G' in combo.loads:
                    gfactor = combo.loads['G']
                    forces += gfactor * column.forces[f"G/{combo_type}"]
                # Variable Loads
                if 'Q' in combo.loads:
                    qfactor = combo.loads['Q']
                    forces += qfactor * column.forces[f"Q/{combo_type}"]

                if combo_type == 'gravity':
                    # Set the loading case (type)
                    forces.case = combo_type
                    # Append the combined forces
                    column.design_forces.append(forces)
                else:   # seismic
                    # Add the forces from seismic loading
                    forces_ov = ColumnForces(*forces.__dict__.values())
                    ecc_forces = []  # forces due to eccentric loading
                    ecc_forces_ov = []  # forces due to eccentric loading
                    gfactor = combo.masses['G']  # permanent loads factor
                    qfactor = combo.masses['Q']  # variable loads factor
                    for load_case in seismic_load_cases:
                        if load_case in combo.loads:
                            tag = f"{load_case}/{gfactor}G/{qfactor}Q"
                            fact = combo.loads[load_case]
                            forces += fact * column.forces[tag]
                            forces_ov += self.OVERSTRENGTH_FACTOR * fact * \
                                column.forces[tag]
                            tmp, tmp_ov = [], []  # ecc. forces per load_case
                            for ecc in ecc_factors:
                                tag_e = tag + f"/{ecc}ecc"
                                if ecc == 0:
                                    tmp.append(ColumnForces(0, 0, 0, 0, 0,
                                                            0, 0, 0, 0, 0))
                                    tmp_ov.append(ColumnForces(0, 0, 0, 0, 0,
                                                               0, 0, 0, 0, 0))
                                else:
                                    tmp.append(fact * column.forces[tag_e])
                                    tmp_ov.append(self.OVERSTRENGTH_FACTOR *
                                                  fact * column.forces[tag_e])
                            ecc_forces.append(tmp)
                            ecc_forces_ov.append(tmp_ov)

                    # Possible combinations with eccentric loadings
                    ecc_combos = list(product(*ecc_forces))
                    ecc_combos_ov = list(product(*ecc_forces_ov))
                    for ecc_combo, ecc_combo_ov in zip(ecc_combos,
                                                       ecc_combos_ov):
                        # Add the forces due to ecc. loading
                        forces_ = sum(ecc_combo, forces)
                        forces_ov_ = sum(ecc_combo_ov, forces_ov)
                        # Set the loading case (type)
                        forces_.case = combo_type
                        forces_ov_.case = combo_type
                        # Append the combined forces
                        column.design_forces.append(forces_)
                        column.design_forces_overstrength_adjusted.append(
                            forces_ov_)
