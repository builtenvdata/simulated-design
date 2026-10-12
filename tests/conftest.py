"""Shared fixtures of the test suite."""
import sys
from pathlib import Path
import pytest

# Add the project root to sys.path
sys.path.append(str(Path(__file__).parents[1]))

from simdesign import rcmrf  # noqa
from simdesign.rcmrf import StandardGeometry  # noqa

# Design classes with (eu_cdh) and without (eu_cdl) capacity-designed
# columns, i.e., without and with column shear springs
MATERIALS = {'eu_cdh': ('C25/30', 'S400'), 'eu_cdl': ('B225', 'A40')}


def make_design(design_class: str) -> rcmrf.BDIM:
    """Design a 2-storey, 2x2-bay frame with a stair bay and infills."""
    frame = StandardGeometry(2, 3.0, 2, 3.5, 2, 3.5)
    frame.set_continuous_stairs_rectangles((0, 0), 4, 4)
    frame.add_infills(exterior=True, interior=False, ext_type='Weak',
                      int_type='Weak')
    frame.add_new_elements_for_stairs(infills=True)
    concrete, steel = MATERIALS[design_class]
    taxonomy = rcmrf.TaxonomyData(
        beta=0.07, beam_type=2, column_section=1, slab_type=1,
        concrete_grade=concrete, design_class=design_class, quality=1,
        slab_orientation=3, steel_grade=steel, geometry=frame)
    bdim = rcmrf.BDIM(taxonomy)
    bdim.set_seed_for_quality_adjustments(1)
    bdim.run_iterative_design_algorithm()
    assert bdim.ok
    return bdim


@pytest.fixture(scope='session')
def designs():
    """Designs shared by the BNSM tests (one per design class)."""
    return {dc: make_design(dc) for dc in MATERIALS}
