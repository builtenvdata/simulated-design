SimDesign Library
=================

SimDesign is an open-source `Python <https://www.python.org/>`_ framework which enables the simulated design of buildings
following historical and modern seismic design procedures in Europe. The source code is maintained in a
`GitHub repository <https://github.com/builtenvdata/simulated-design>`_ under the `Built Environment Data (BED) <https://www.builtenvdata.eu/>`_
initiative, allowing the earthquake engineering community to contribute to a growing database of seismic design practices
encompassing a wide range of design codes in European countries.

Workflow
--------
The framework generates a
`Building Class Information Model (BCIM) <https://github.com/builtenvdata/simulated-design/blob/main/data/core-article-data/figures%208%20and%209/BCIM.csv>`_
database for a given building taxonomy, described through attributes such as
`lateral load coefficient and design class <https://maps.eu-risk.eucentre.it/map/european-seismic-design-levels/#4/51.33/6.78>`_,
to represent multiple possible building realisations and explicitly capture building-to-building variability within a portfolio
of buildings.

Each realisation is processed through an iterative simulated design and quality-based modification procedures, with the resulting design details stored in the 
`Building Design Information Model (BDIM) <https://github.com/builtenvdata/simulated-design/tree/main/data/core-article-data/figures%208%20and%209/BDIM>`_
database. Following the design stage, the framework generates
`Building Nonlinear Structural Models (BNSM) <https://github.com/builtenvdata/simulated-design/tree/main/data/core-article-data/figures%208%20and%209/BNSM>`_
that can be readily used for structural analysis in `OpenSees <https://opensees.berkeley.edu/>`_.

These outputs ultimately support the development of probabilistic seismic demand
models, fragility functions, and vulnerability models for large-scale seismic risk
assessment studies, such as the `European Seismic Risk Model (ESRM20) <https://eu-risk.eucentre.it/esrm20/>`_.

.. figure:: _static/images/Workflow.svg
   :width: 600px
   :align: center

   General overview of the SimDesign frramework

License
-------

This work is licensed under the **GNU Affero General Public License Version 3**.
To view a copy of the license, visit:

https://www.gnu.org/licenses/agpl-3.0.html


References
----------

If you make use of the SimDesign framework in academic or professional work, please cite following publications:

- Ozsarac, V., Pereira, N., Mohamed, H., Romão, X. and O'Reilly, G.J. (2025). *The Built Environment Data Framework for Simulated Design and Vulnerability Modelling in Earthquake Engineering*. **Earthquake Engineering & Structural Dynamics**, 54, 2651–2670. https://doi.org/10.1002/eqe.4378
- Hasanoğlu, S., Ozsarac, V., and O'Reilly, G.J. (2025). *A model for the simulated design of Turkish RC frame buildings in seismic vulnerability analysis*. **Bulletin of Earthquake Engineering**, 23, 6829–6856. https://doi.org/10.1007/s10518-025-02301-y

Contributions
-------------

Contributions are welcome! If you would like to contribute to this project,
please follow the steps below:

1. Fork the repository.
2. Create a new branch::

      git checkout -b feature-branch

3. Make your changes.
4. Update or add tests (e.g. ``test_rcmrf.py``) for new features.
5. Run the test suite and ensure all tests pass::

      pytest tests

6. Commit your changes::

      git commit -m "Add new feature"

7. Push the branch to your fork::

      git push origin feature-branch

8. Open a pull request on GitHub.

.. toctree::
   :maxdepth: 2
   :caption: Contents

   getting-started/index
   api/index