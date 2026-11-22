# Code for negative-control calibration in educational data

The working manuscript and recent simulation scripts are in `methods article/jedm_submission/manuscript_20/`. The editorial audit and earlier simulations are in adjacent directories. OULAD models and data-loading code are in `ednet-mars/`.

Original relative paths are retained. Raw datasets, processed parquet files, trained models and CSV results are excluded. Reproduction requires the original OULAD and XES3G5M inputs and the appropriate processed data files. The scripts expect these inputs at the paths they specify.

The package has not been validated as a standalone reproducible environment. Consult `methods article/jedm_submission/editorial_revision/README_RU.md` and the experiment protocols before running analyses. Python dependencies include NumPy, pandas, scikit-learn, XGBoost, pyarrow, matplotlib and threadpoolctl. Building the manuscript requires a LaTeX installation.
