Installation
------------

Follow the steps below to install the ``simdesign`` package.

.. note:: *Python 3.12* is required. Ensure that correct version is installed.
   

   .. code-block:: console

      python --version  # should be 3.12.x

**Create a Virtual Environment (Recommended)**

Create a virtual environment to manage dependencies:

.. code-block:: console

   python -m venv .venv


Activate the virtual environment:

.. code-block:: console

   .venv\Scripts\activate     # On Windows
   source .venv/bin/activate  # Linux / macOS

**Option 1: Install via PyPI**

Open the terminal and simply run:

.. code-block:: console

   pip install simdesign

**Option 2: Install from Source**

Clone the repository:

.. code-block:: console

   git clone https://github.com/builtenvdata/simulated-design.git
   cd simulated-design

Install the dependencies using requirements file:

.. code-block:: console

   pip install -r requirements.txt

Install the ``simdesign`` package:

.. code-block:: console

   pip install .


Alternatively, to install in editable mode (useful for development):

.. code-block:: console

   pip install -e .
