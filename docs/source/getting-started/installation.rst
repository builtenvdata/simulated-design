.. SimDesign documentation master file, created by
   sphinx-quickstart on Mon Jan 12 13:30:12 2026.
   You can adapt this file completely to your liking.


1. Installation
===============

Follow the steps below to install the ``simdesign`` package.


1.1. Clone the Repository
----------------------

Open your terminal and run:

.. code-block:: bash

   git clone https://github.com/builtenvdata/simulated-design.git
   cd simulated-design



1.2. Set Up a Virtual Environment (Recommended)
---------------------------------------------

Create a virtual environment to manage dependencies:

.. code-block:: bash

   python -m venv .venv       # On Windows
   python3 -m venv .venv      # On Linux


Activate the virtual environment:

.. code-block:: bash

   .venv\Scripts\activate        # On Windows
   source .venv/Scripts/activate # On Linux



1.3. Install Dependencies
-----------------------

Install the required packages listed in ``requirements.txt``.


**For Windows users:** install the appropriate requirements file based on your Python version:

.. code-block:: bash

   pip install -r requirements-py311-win64.txt  # Python 3.11
   pip install -r requirements-py312-win64.txt  # Python 3.12


**For Linux users:** install the appropriate requirements file based on your Python version:

.. code-block:: bash

   pip install -r requirements-py311-linux64.txt  # Python 3.11
   pip install -r requirements-py312-linux64.txt  # Python 3.12


**For macOS users:**

OpenSeesPy is currently incompatible with macOS systems running on ``arm64`` processors
(e.g., Apple M1 and M2 chips). As a result, newer OpenSeesPy versions are not released
for macOS platforms. It is recommended to use a virtual machine running Linux or Windows
on Mac computers to use OpenSeesPy.



1.4. Install the Package
----------------------

Install the ``simdesign`` package:

.. code-block:: bash

   pip install .


Alternatively, to install in editable mode (useful for development):

.. code-block:: bash

   pip install -e .
