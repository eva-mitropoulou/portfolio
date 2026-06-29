# Public Portfolio Artifact Map

This portfolio folder is a public-safe mirror of the antibody sequence ML project. It intentionally includes reports, aggregate metrics, selected figures, a notebook walkthrough, and a representative analysis script, but does not mirror raw sequence tables, downloaded OAS files, trained model weights, or large embedding arrays.

Full source repository: <https://github.com/eva-mitropoulou/antibody-prioritization>

## Included In This Portfolio

### Reports

- `reports/final_report.md`
- `reports/final_flagship_project_report.md`
- `reports/final_consistency_audit.md`
- `reports/unsupervised_antibody_landscape_report.md`

### Metrics

- `reports/metrics/summary.json`
- `reports/metrics/source_robust_public_plot_metrics.json`
- `reports/metrics/unsupervised_antibody_landscape_metrics.json`

### Figures

- `figures/antibody_pipeline.svg`
- `figures/antibody_benchmark_pr_auc.png`
- `figures/source_robust_model_comparison.png`
- `figures/source_robust_pr_auc_by_model.png`
- `figures/source_robust_roc_auc_by_model.png`
- `figures/calibration_curve.png`
- `reports/figures/unsupervised_antibody_landscape.png`

### Documentation

- `docs/DATA_CARD.md`
- `docs/MODEL_CARD.md`
- `README.md`
- `environment.yml`
- `Makefile`
- `../notebooks/01_antibody_sequence_ml_workflow.ipynb`

### Representative Code

- `code/build_unsupervised_antibody_landscape.py`

The representative code is copied to document the unsupervised sequence-landscape method. Full execution uses the standalone source repository, where helper modules, raw-data preparation, embeddings, and model artifacts are managed.

## Not Mirrored Here

- Raw CoV-AbDab and OAS sequence files
- Processed sequence tables containing row-level sequence data
- Numpy embedding arrays
- Trained model weights and serialized models
- Large diagnostic CSVs
- Full source tree from the standalone repository

These omissions are deliberate public-portfolio boundaries, not missing project work.
