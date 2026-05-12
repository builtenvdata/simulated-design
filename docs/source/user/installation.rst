Installation
------------

Follow the steps below to install the ``simdesign`` package.


**1. Clone the repository**

Open your terminal and run:

.. code-block:: console

   git clone https://github.com/builtenvdata/simulated-design.git
   cd simulated-design



**2. Set up a virtual environment (recommended)**

Create a virtual environment to manage dependencies:

.. code-block:: console

   python -m venv .venv


Activate the virtual environment:

.. code-block:: console

   .venv\Scripts\activate     # On Windows
   source .venv/bin/activate  # Linux / macOS



**3. Install dependencies**

Install the dependencies using requirements file:

.. code-block:: console

   pip install -r requirements.txt

**4. Install the Package**

Install the ``simdesign`` package:

.. code-block:: console

   pip install .


Alternatively, to install in editable mode (useful for development):

.. code-block:: console

   pip install -e .


.. note:: *Python 3.12* is required. Ensure that correct version is installed.
   

   .. code-block:: console

      python --version  # should be 3.12.x
