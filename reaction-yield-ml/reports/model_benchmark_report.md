# Model Benchmark Report

## Summary

- Models evaluated: mean_baseline, onehot_ridge, onehot_elastic_net, random_forest, gradient_boosting
- Primary reliability split for model selection: grouped_high_cardinality_component
- Selected model: random_forest
- Selected model MAE on primary split: 10.7537
- Selected model RMSE on primary split: 14.2371
- Selected model R2 on primary split: 0.7262
- Selected model Spearman correlation on primary split: 0.8597
- Selected model top-10% enrichment on primary split: 7.3333

## Optional Models

- xgboost: skipped_not_installed
- lightgbm: skipped_not_installed
- neural_baseline: skipped_scope_controlled_reproducibility

## Quality Gates

- mean_baseline_included: True
- grouped_or_out_of_component_split_included: True
- random_split_not_sole_evidence: True
- best_model_selected_by_reliability_split: True
- all_metrics_saved_as_json: True

## Interpretation Boundary

Random split performance is not presented as sole evidence. Grouped and out-of-component splits are included where possible. Model selection prioritizes the reliability-oriented grouped split.
