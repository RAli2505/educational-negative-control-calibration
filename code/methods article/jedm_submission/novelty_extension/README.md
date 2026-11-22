# Boundary benchmark and scientific supplement

Start with `RESULTS_RU.md`. The article-ready English supplement is `paper_supplement/main.pdf`; `manuscript_with_extension.pdf` appends it to the unchanged earlier manuscript. The original manuscript abstract was not regenerated. No claim of a new causal method or journal readiness is made.

## Reproduction

1. `python run_boundary_benchmark.py --verify-only`
2. `python run_boundary_benchmark.py --replications 1000`
3. `python verify_saved_results.py`
4. `python build_outputs.py`
5. Run pdflatex twice on `paper_supplement/main.tex` from that directory.

The benchmark needs NumPy and pandas with a parquet engine; the figure generator also needs matplotlib. Python, NumPy and pandas versions are in `results/config.json`. Source and protocol hashes are fixed there. Input parquet hashes and population aggregates are in `results/population_inventory.json`; file locations follow the existing local `ednet-mars` project relative to this workspace. Individual student data are not included. Use the same directory layout or explicitly adapt input paths for a different machine and record the change.

The compressed replicate table is synthetic. It contains 928000 estimate records for 58000 generated experiments and 16 method/interval variants. The median is a point-only comparator and has missing interval endpoints by design. True-loading orientation uses the first active target factor as its reference, with the known second-factor signs as a fallback; this is not an optimal-bias oracle in multifactor models. The known-full-assignment IPW comparator uses hidden information. The finite-sample interval uses an oracle structural bias bound and known marginal propensity; it is not a feasible estimate of that bound from controls.

`PROTOCOL.md` was written locally before executing the new series, after earlier exploratory/editorial work. It is not an external preregistration. All 58 specified cells are included. `THEORY.md` contains the model, proofs and limitations; `PRIOR_ART_RU.md` records the targeted literature comparison and search limitations. Full published COCA/NC-DiD/positive-control empirical CI calibration were not implemented, so the package establishes no superiority over those methods.

The earlier manuscript and abstract remain byte-identical. The merged PDF is a convenience reading copy, not a claim that the earlier text has been fully integrated with this supplement. Only aggregate outputs are packaged, and input student records are excluded.
