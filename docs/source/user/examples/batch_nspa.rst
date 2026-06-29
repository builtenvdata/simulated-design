NSPA
----

This example demonstrates the full step-by-step pipeline — from portfolio
generation to pushover analysis — using the
:class:`~simdesign.rcmrf.bcim.factory.BCIM`,
:class:`~simdesign.rcmrf.bdim.baselib.building.BDIM`, and
:class:`~simdesign.rcmrf.bnsm.baselib.building.BNSM` classes directly rather
than through the high-level :func:`simdesign.rcmrf.generate` convenience
function. It also shows an adaptive convergence strategy that retries the
pushover with progressively finer displacement increments when the default
increment fails.

.. code-block:: python

    import matplotlib.pyplot as plt
    from pathlib import Path
    from simdesign import rcmrf
    from simdesign.utils.misc import make_dir

    model = "CP03"
    scheme = "EQL"
    max_drift = 0.1
    include_infills = True

    design_classes = [
        "eu_cdn", "eu_cdl", "eu_cdm", "eu_cdh",
        "tr_7599", "tr_0018_dcm", "tr_0018_dch",
        "tr_post18_dcm", "tr_post18_dch",
    ]

    outdir_main = Path("Outputs-NSPA-Batch")
    make_dir(outdir_main)

    for design_class in design_classes:
        outdir_class = outdir_main / design_class
        make_dir(outdir_class)

        # Generate the building portfolio
        bcim = rcmrf.BCIM()
        bcim.generate(
            sample_size=1,
            design_class=design_class,
            num_storeys=4,
            beta=0.1,
        )
        bcim.to_csv(outdir_class / "BCIM_initial.csv")

        for i, taxonomy in enumerate(bcim.taxonomy):
            print(f"Designing {design_class.upper()} building "
                  f"{i + 1}/{len(bcim.taxonomy)}")
            outdir_building = outdir_class / f"Building_{i + 1}"

            # Simulated design
            bdim = rcmrf.BDIM(taxonomy)
            bdim.set_seed_for_quality_adjustments(bcim.inputs.seed)
            bdim.run_iterative_design_algorithm()

            if not bdim.ok:
                continue

            # Update BCIM attributes that may be adjusted during design
            bcim.column_section[i] = bdim.column_section
            bcim.beam_type[i]      = bdim.beam_type
            bcim.concrete_grade[i] = bdim.concrete_grade
            bcim.steel_grade[i]    = bdim.steel_grade
            bdim.to_csv(outdir_building / "BDIM-Data")

            # Modal analysis and model visualisation
            bnsm = rcmrf.BNSM(
                design=bdim, scheme=scheme, dincr=1e-3,
                max_drift=max_drift, model=model,
                include_infills=include_infills,
            )
            bnsm.do_modal(num_modes=6, out_dir=outdir_building / "Modal-Results")
            bnsm.plot_model(directory=outdir_building, show=False)
            bnsm.plot_mode_shape(
                mode_number=1, contour="x", show=False, directory=outdir_building
            )
            bnsm.plot_mode_shape(
                mode_number=2, contour="y", show=False, directory=outdir_building
            )

            # Pushover in X — retry with finer increments on convergence failure
            dincr_x = 1e-3
            dx, vx, ok_x = bnsm.do_nspa(
                ctrl_dof=1, out_dir=outdir_building / "NSPA-Results-X"
            )
            for dincr_try in [1e-4, 1e-5]:
                if ok_x != 0:
                    dincr_x = dincr_try
                    bnsm = rcmrf.BNSM(
                        design=bdim, scheme=scheme, dincr=dincr_x,
                        max_drift=max_drift, model=model,
                        include_infills=include_infills,
                    )
                    dx, vx, ok_x = bnsm.do_nspa(
                        ctrl_dof=1, out_dir=outdir_building / "NSPA-Results-X"
                    )

            # Pushover in Y — same adaptive strategy
            dincr_y = 1e-3
            dy, vy, ok_y = bnsm.do_nspa(
                ctrl_dof=2, out_dir=outdir_building / "NSPA-Results-Y"
            )
            for dincr_try in [1e-4, 1e-5]:
                if ok_y != 0:
                    dincr_y = dincr_try
                    bnsm = rcmrf.BNSM(
                        design=bdim, scheme=scheme, dincr=dincr_y,
                        max_drift=max_drift, model=model,
                        include_infills=include_infills,
                    )
                    dy, vy, ok_y = bnsm.do_nspa(
                        ctrl_dof=2, out_dir=outdir_building / "NSPA-Results-Y"
                    )

            # Rebuild BNSM with the finest increment that worked for both directions
            bnsm = rcmrf.BNSM(
                design=bdim, scheme=scheme,
                dincr=min(dincr_x, dincr_y),
                max_drift=max_drift, model=model,
                include_infills=include_infills,
            )
            bnsm.to_py(outdir_building / "OpsPy-Model")
            bnsm.to_tcl(outdir_building / "OpsTcl-Model")

            # Plot pushover curves
            plt.plot(dx, vx, label="X-dir")
            plt.plot(dy, vy, label="Y-dir")
            plt.xlabel("Control Node Displacement [m]")
            plt.ylabel("Base Shear [kN]")
            plt.legend()
            plt.savefig(outdir_building / "nspa.png", dpi=300)
            plt.close()

        bcim.to_csv(outdir_class / "BCIM_final.csv")

.. rubric:: Key points

**Adaptive convergence**
   :meth:`~simdesign.rcmrf.bnsm.baselib.building.BNSM.do_nspa` returns a
   status flag as its third return value. A non-zero value indicates that the
   analysis did not converge. The example retries with successively finer
   increments (``1e-3`` → ``1e-4`` → ``1e-5``) before proceeding. A new
   :class:`~simdesign.rcmrf.bnsm.baselib.building.BNSM` instance must be
   constructed for each retry because OpenSees state is not reset between runs.

**BCIM update after design**
   Attributes such as ``column_section`` and ``concrete_grade`` may be adjusted
   by the design algorithm. Writing them back to the BCIM object ensures that
   the final CSV reflects the as-designed properties rather than the initially
   sampled values.

**Final model export**
   The OpenSees model is exported only once, using the smallest displacement
   increment that successfully converged in both directions.
