Quickstart
----------

The following example demonstrates how to run a SimDesign workflow for reinforced concrete moment-resisting frame (RCMRF) buildings with minimal inputs.
To run the RCMRF framework, an input dictionary must be defined. This dictionary contains the configuration parameters for the workflow.

Two main keys are required:

- **bcim**: configuration parameters controlling the generation of the building portfolio
  and the simulated design process.
- **bnsm**: configuration parameters defining the nonlinear structural modelling strategy
  used to generate the numerical models.

.. code-block:: python

    from simdesign import rcmrf

    # The main inputs for each design class
    inputs = {
        'bcim': {
            'design_class': 'eu_cdl',  # Design Class
            'sample_size': 30,  # Number of buildings in portfolio
            'num_storeys': 4,  # Number of storeys in each building
            'beta': 0.1,  # Design lateral load coefficient
        },
        'bnsm': {
            'model': 'DP01',  # Numerical modelling strategy
            'opensees': 'py'  # OpenSees Interpreter
        }
    }

    # Run the workflow for rcmrf systems and save the outputs
    bcim, bdim, bnsm = rcmrf.generate(inputs=inputs, outdir="Outputs")

Running this script generates three outputs:

- **BCIM** — *Building Class Information Model*:  
  contains the generated building portfolio taxonomy attributes and geometry variables
  (exported as a CSV file).

- **BDIM** — *Building Design Information Model*:  
  contains the simulated structural design details for each building
  (exported as multiple CSV files).

- **BNSM** — *Building Nonlinear Structural Model*:  
  contains OpenSees computational models of the designed buildings
  (exported as Tcl or Python scripts).

All generated files are stored in the specified output directory.