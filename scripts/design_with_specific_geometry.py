from pathlib import Path
import sys
import matplotlib.pyplot as plt


"""
Assumptions on the building:
    RC-MRF with Moderate ductility level (CD”B”)
    First Period = C1*H**(3/4), from NTC2008
    C1 = 0.075, H = 24.4, T1 = 0.82
    q = KR * q0; Equation [7.3.1]
    where KR = 1.0 for regular structure
    q0 = 3 * au/a1;  from Tab. 7.3.II
    au/a1 = 1.3; from section 7.4.3.2, a)

Assumptions on the site:
    Soil Class B
    Topography type Flat (T1); from Tab. 3.2.III
    City: L'Aquila
    Tc: 0.346
    a0: 0.261
    F0: 2.363

Beta coefficient:
    Beta = Sd(T1)*Lambda / g from equation [7.3.7]
    Lambda = 0.85 if T1 < 2Tc else 1.0
    Sd(T1) = Se(T1) / q

Se(T1) cn be computed from
https://apps.djura.it/hazard/record-selector/uhs
"""


# Add the src directory to sys.path
sys.path.append(str(Path(__file__).parents[1]))

from simdesign.rcmrf import StandardGeometry  # noqa
from simdesign import rcmrf  # noqa


outdir = Path(__file__).parents[1] / 'tmp' / 'specific-frame'

# Initial bay widths and storey heights
num_storeys = 8
storey_height = 3.0  # NOTE: Should be for 9LAB height
num_bays_x = 7
num_bays_y = 5
bay_width_x = 5
bay_width_y = 5

# Modify the ground floor height
h_ground = 3.4
floor_id = 1
# Initialise the frame object
regular_frame = StandardGeometry(
    num_storeys, storey_height, num_bays_x, bay_width_x,
    num_bays_y, bay_width_y)
# Set stairs locations
stair_loc1 = (1, 2)  # Grid ID of left bottom point (or bay ID in x and y)
stair_loc2 = (5, 2)  # Grid ID of left bottom point (or bay ID in x and y)
stairs_width_x = 2.5
stairs_width_y = 3.3
regular_frame.set_continuous_stairs_rectangles(
    stair_loc1, stairs_width_x, stairs_width_y)
regular_frame.set_continuous_stairs_rectangles(
    stair_loc2, stairs_width_x, stairs_width_y)
# Modifying a floor height (ground floors are usually modified)
regular_frame.modify_floor_height(floor_id, h_ground)
# Modifying a bay_width (ground floors are usually modified)
"""
NOTE: Test room corresponds to bays ids: bay_x=4 and bay_y=3.
Example ERIES test room has dimensions (lx=3.3m, ly=3.3m, h=3.4m)
While the 9LAB shake table has dimensions lx=4.8m, ly=4.8m
for now the test room has the same dimensions as the ERIES room,
except the ground floor where the storey height is 4m.
"""
regular_frame.modify_bay_width(bay_id=2, width=3.3, direction="x")
regular_frame.modify_bay_width(bay_id=4, width=3.3, direction="x")
regular_frame.modify_bay_width(bay_id=6, width=3.3, direction="x")
regular_frame.modify_bay_width(bay_id=3, width=3.3, direction="y")
# Add infills
regular_frame.add_infills(
    exterior=True, interior=False, ext_type='Medium', int_type='Weak'
)
# Save the basic frame
path = outdir / "geometry.xlsx"
regular_frame.write_mesh_to_xlsx(path=path)
# Add the new lines and points for stairs (For now do this in the end)
regular_frame.add_new_elements_for_stairs(infills=True)
# regular_frame.show_mesh()
path = outdir / "geometry.html"
regular_frame.export_mesh_to_html(path=str(path))


grids_x = [
    (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0),
    (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5)
]
grids_y = [
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 1), (1, 2), (1, 3), (1, 4),
    (2, 1), (2, 2), (2, 3), (2, 4),
    (5, 1), (5, 2), (5, 3), (5, 4),
    (6, 1), (6, 2), (6, 3), (6, 4),
    (7, 1), (7, 2), (7, 3), (7, 4),
]
grids_s = [
    (0, 0), (7, 0), (0, 5), (7, 5),
    (3, 1), (4, 1), (3, 2), (4, 2),
    (3, 3), (4, 3), (3, 4), (4, 4)
]

for grid, lines in regular_frame.continuous_lines_along_z.items():
    for line in lines:
        if grid in grids_x:
            line.rot_angle = 0.0
        elif grid in grids_y:
            line.rot_angle = 90.0

# Set beta for 3 cases
if h_ground == 3 and storey_height == 3:
    beta = 0.091  # For SONATA
elif h_ground == 3.4 and storey_height == 3:
    beta = 0.090  # This is a more realistic case
elif h_ground == 3.4 and storey_height == 3.4:
    beta = 0.084  # For ERIES

taxonomy_data = {
    "beta": beta,
    "beam_type": 2,
    "column_section": 1,
    "slab_type": 1,
    "concrete_grade": "C30/37",
    "design_class": "eu_cdh",
    "quality": 0,
    "slab_orientation": 3,
    "slab_type": 1,
    "steel_grade": "S500",
    "geometry": regular_frame
}


taxonomy = rcmrf.TaxonomyData(**taxonomy_data)
# Initialize BDIM
bdim = rcmrf.BDIM(taxonomy)
for grid, columns_list in bdim.continuous_columns.items():
    for columns in columns_list:
        for column in columns:
            if grid in grids_x + grids_y:  # rectangle
                column.section = 2
            else:  # Square
                column.section = 1
# Make simumlated design
bdim.run_iterative_design_algorithm()
bdim.to_csv(outdir / 'design')

if bdim.ok:  # Design solution is found
    include_infills = True
    model = "DP04"
    scheme = "EQL"
    max_drift = 0.1

    # Initialize BNSM
    bnsm = rcmrf.BNSM(
        design=bdim, scheme=scheme, dincr=1e-3,
        max_drift=max_drift, model=model, include_infills=include_infills)
    # Export numerical models for OpenSeesPy
    bnsm.to_py(outdir / "OpsPy-Model")
    # Export numerical models for OpenSeesTcl
    bnsm.to_tcl(outdir / "OpsTcl-Model")
    # Do modal analysis
    modal_dir = outdir / "Modal-Results"
    bnsm.do_modal(num_modes=3, out_dir=modal_dir)
    # Plot the model and save
    bnsm.plot_model(directory=outdir, show=False)
    # Plot the first two mode shapes and save
    bnsm.plot_mode_shape(mode_number=1, contour="y", show=False,
                         directory=outdir, set_view='yz')
    bnsm.plot_mode_shape(mode_number=2, contour="x", show=False,
                         directory=outdir, set_view='xz')
    bnsm.plot_mode_shape(mode_number=3, contour="y", show=False,
                         directory=outdir)
    # Perform the pushover directly
    push_dir = outdir / "NSPA-Results"
    dx, vx, _ = bnsm.do_nspa(ctrl_dof=1, out_dir=push_dir)
    push_dir = outdir / "NSPA-Results"
    dy, vy, _ = bnsm.do_nspa(ctrl_dof=2, out_dir=push_dir)
    plt.plot(dx, vx, label="X-dir")
    plt.plot(dy, vy, label="Y-dir")
    plt.xlabel("Control Node Displacement [m]")
    plt.ylabel("Base Shear [kN]")
    plt.legend()
    plt.savefig(outdir / "nspa.svg", dpi=300)
    plt.close()
