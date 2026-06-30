# Public Portfolio Artifact Map

This portfolio folder is a public-safe mirror of the antibody sequence ML project. It intentionally includes reports, aggregate metrics, selected figures, a notebook walkthrough, and a representative analysis script, but does not mirror raw sequence tables, downloaded OAS files, trained model weights, or large embedding arrays.

Full source repository: <https://github.com/eva-mitropoulou/antibody-prioritization>

## Included In This Portfolio

### Reports

- `reports/final_report.md`
- `reports/final_project_report.md`
- `reports/model_registry.md`
- `reports/oas_existing_record_shortlist_report.md`
- `reports/unsupervised_antibody_clusters.csv`
- `reports/source_robust_model_comparison.csv`
- `reports/oas_existing_record_scores_public.csv`
- `reports/oas_existing_record_shortlist_top25.csv`
- `reports/oas_existing_record_shortlist_top100.csv`

### Metrics

- `reports/metrics/summary.json`
- `reports/metrics/source_robust_model_selection_metrics.json`
- `reports/metrics/oas_existing_record_shortlist_metrics.json`
- `reports/metrics/pretrained_finetune_seed_check_metrics.json`
- `reports/metrics/pretrained_finetune_metrics.json`
- `reports/metrics/calibration_threshold_metrics.json`
- `reports/metrics/core_dataset_audit.json`
- `reports/metrics/final_consistency_audit.json`
- `reports/metrics/model_registry.json`
- `reports/metrics/unsupervised_antibody_landscape_metrics.json`

### Figures

- `docs/assets/project_workflow.png`
- `docs/assets/broad_model_benchmark.png`
- `docs/assets/kmer_vs_igbert_followup.png`
- `docs/assets/selected_model_robustness.png`
- `reports/figures/source_robust_model_comparison.png`
- `reports/figures/unsupervised_antibody_landscape.png`
- `reports/figures/oas_existing_record_score_distribution.png`
- `reports/figures/oas_existing_record_similarity_vs_score.png`
- `reports/figures/oas_existing_record_diversity_map.png`
- `reports/figures/pretrained_finetune_seed_check_roc_pr.png`

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
- Non-public or sequence-bearing diagnostic CSVs
- Full source tree from the standalone repository

These omissions are deliberate public-portfolio boundaries, not missing project work.
