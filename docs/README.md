# Built Environmenta Data (BED) - SimDesign Framework

[![Documentation](https://img.shields.io/badge/docs-builtenvdata.github.io-blue)](https://builtenvdata.github.io/simulated-design/)
[![PyPI](https://img.shields.io/pypi/v/simdesign)](https://pypi.org/project/simdesign/)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-31210/)
[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL%203.0-blue.svg)](https://opensource.org/licenses/AGPL-3.0)
[![DOI](https://img.shields.io/badge/DOI-10.1002%2Feqe.4378-blue)](https://doi.org/10.1002/eqe.4378)

A Python package for the modeling the seismic vulnerability of buildings using the simulated design. Currently, it focuses on Reinforced Concrete (RC) Moment Resisting Frames (MRFs), but the workflow is adaptable to other structural systems. To ensure modularity and scalability for future extensions, the **rcmrf** framework is integrated within the broader **simdesign** library. The framework can accommodate the design of buildings using both historical and modern seismic design procedures and regulations, while capturing building-to-building variability. It generates Building Class Information Models (BCIM), Building Design Information Models (BDIM), and Building Nonlinear Structural Models (BNSM) that are analyzable in OpenSees.
![Service](https://raw.githubusercontent.com/builtenvdata/simulated-design/refs/heads/main/docs/source/_static/general/Workflow.svg)

## Installation

Follow the steps below to install the ``simdesign`` package.

**Note:** Python 3.12 is required. Ensure that correct version is installed:
```bash
python --version  # should be 3.12.x
```

### Create a Virtual Environment (Recommended)

Create a virtual environment to manage dependencies:
```bash
python -m venv .venv
```

Activate the virtual environment:
```bash
.venv\Scripts\activate     # On Windows
source .venv/bin/activate  # Linux / macOS
```

### Option 1: Install via PyPI 

Open the terminal and simply run:
```bash
pip install simdesign
```

### Option 2: Install from Source

Clone the repository:
```bash
git clone https://github.com/builtenvdata/simulated-design.git
cd simulated-design
```

Install the `simdesign` package:
```bash
pip install .
```

Alternatively, to install in editable mode (useful for development), run:
```bash
pip install -e .
```


## Usage

Once installed, you can import and use the package in Python:

```python
# Example usage
from simdesign import rcmrf

# The main inputs for each design class
inputs = {
    "bcim": {
        "design_class": "eu_cdl",
        "sample_size": 30,
        "num_storeys": 4,
        "beta": 0.1,
        "seed": 2
    },
    "bnsm": {
        "model": "DP01",
        "scheme": "EQL",
        "dincr": 1e-3,
        "max_drift": 0.1,
        "opensees": "py",
        "include_infills": False
    }
}
# Run the bed-workflow for rcmrf systems and save the outputs
bcim, bdim, bnsm = rcmrf.generate(inputs=inputs, outdir="Outputs")
```

For more examples please see the scripts folder or see full [documentation](https://builtenvdata.github.io/simulated-design/) for advanced use.

It is also possible to visualise and design buildings with specific geometries. See an [example of a specific design](https://htmlpreview.github.io/?https://raw.githubusercontent.com/builtenvdata/simulated-design/blob/main/docs/source/_static/design/specific-design.html).

## Contributing

Contributions are welcome! If you’d like to contribute, follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Update the test files (`test_rcmrf.py`) for new features.
5. Run pytest and check if all tests pass (`pytest tests`).
6. Commit the changes (`git commit -m 'Add new feature'`).
7. Push to the branch (`git push origin feature-branch`).
8. Open a pull request.

## References
If you use the SimDesign tool, please be sure to cite the reference publication:

Ozsarac, V., Pereira, N., Mohamed, H., Romão, X., & O’Reilly, G. J. (2025). The Built Environment Data Framework for Simulated Design and Vulnerability Modelling in Earthquake Engineering. Earthquake Engineering & Structural Dynamics, 54(11), 2651-2670. https://doi.org/10.1002/eqe.4378

Hasanoğlu, S., Ozsarac, V., & O’Reilly, G. J. (2025). A model for the simulated design of Turkish RC frame buildings in seismic vulnerability analysis. Bulletin of Earthquake Engineering, 23(15), 6829-6856. https://doi.org/10.1007/s10518-025-02301-y

## License
This project is licensed under the AGPL-3.0 license. See the LICENSE file for details.
