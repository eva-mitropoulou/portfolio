# Agentic Run Log

## 2026-06-28T11:38:16.793551+00:00 - phase_1_dataset_selection

- status: PASS
- files created/updated: data/DATA_CARD.md, data/dataset_manifest.json, reports/dataset_selection_report.md, reports/metrics/dataset_selection_metrics.json
- checks run: public source reachable, component columns present, target column present, row count recorded
- failures found: none
- repairs attempted: none
- remaining limitations: Retrospective public-data benchmark only., Component structures are not provided in the selected workbook; structure-based features are skipped unless SMILES are added externally., The workflow ranks existing public records only and does not generate new reaction conditions.

## 2026-06-28T11:38:17.495381+00:00 - phase_2_data_audit

- status: PASS
- files created/updated: reports/data_audit_report.md, reports/metrics/data_audit_metrics.json
- checks run: raw row count computed, duplicate count computed, missing target count computed, component cardinalities computed
- failures found: none
- repairs attempted: none
- remaining limitations: Audit reports aggregate counts only., Invalid component identifiers are string-presence checks, not chemical-validity checks.

## 2026-06-28T11:38:18.213708+00:00 - phase_3_reaction_cleaning

- status: PASS
- files created/updated: data/processed/clean_reactions.csv, reports/reaction_cleaning_report.md, reports/metrics/reaction_cleaning_metrics.json
- checks run: numeric target standardized, component strings standardized, duplicates removed, impossible yields excluded
- failures found: none
- repairs attempted: none
- remaining limitations: Component strings are standardized as categorical labels; missing chemistry is not invented., No component SMILES are available in the selected workbook, so molecular descriptors are skipped unless external structures are supplied., Rows outside 0-100 percent yield are excluded rather than clipped.

## 2026-06-28T11:39:53.559914+00:00 - phase_4_component_featurization

- status: BLOCKED
- files created/updated: data/processed/features/categorical_onehot.npz, data/processed/features/feature_index.csv, data/processed/features/feature_metadata.json, reports/feature_engineering_report.md, reports/metrics/feature_engineering_metrics.json
- checks run: no_target_leakage_in_features, feature_rows_align_clean_rows, missing_structures_handled_explicitly, yield_derived_columns_used
- failures found: yield_derived_columns_used
- repairs attempted: none
- remaining limitations: Molecular descriptors and fingerprints skipped because component SMILES are not present., Categorical baseline is the primary feature family for this workbook.

## 2026-06-28T11:39:55.361175+00:00 - phase_5_validation_design

- status: PASS
- files created/updated: data/processed/splits/*.json, reports/validation_design_report.md, reports/metrics/validation_design_metrics.json
- checks run: random_split_available, grouped_or_out_of_component_available, no_group_overlap_for_grouped_splits, split_sizes_reported, target_distribution_reported
- failures found: none
- repairs attempted: none
- remaining limitations: Small grouped splits are flagged when applicable., Held-out group values are not printed.

## 2026-06-28T11:40:06.897699+00:00 - phase_4_component_featurization

- status: PASS
- files created/updated: data/processed/features/categorical_onehot.npz, data/processed/features/feature_index.csv, data/processed/features/feature_metadata.json, reports/feature_engineering_report.md, reports/metrics/feature_engineering_metrics.json
- checks run: no_target_leakage_in_features, feature_rows_align_clean_rows, missing_structures_handled_explicitly, no_yield_derived_columns_used
- failures found: none
- repairs attempted: none
- remaining limitations: Molecular descriptors and fingerprints skipped because component SMILES are not present., Categorical baseline is the primary feature family for this workbook.

## 2026-06-28T11:40:08.596423+00:00 - phase_5_validation_design

- status: PASS
- files created/updated: data/processed/splits/*.json, reports/validation_design_report.md, reports/metrics/validation_design_metrics.json
- checks run: random_split_available, grouped_or_out_of_component_available, no_group_overlap_for_grouped_splits, split_sizes_reported, target_distribution_reported
- failures found: none
- repairs attempted: none
- remaining limitations: Small grouped splits are flagged when applicable., Held-out group values are not printed.

## 2026-06-28T11:41:59.523295+00:00 - phase_6_model_benchmark

- status: PASS
- files created/updated: reports/model_benchmark_report.md, reports/metrics/model_benchmark_metrics.json, reports/figures/model_comparison_by_split.png, reports/figures/predicted_vs_observed.png, reports/figures/error_by_yield_bin.png, data/processed/models/best_model.joblib
- checks run: mean_baseline_included, grouped_or_out_of_component_split_included, random_split_not_sole_evidence, best_model_selected_by_reliability_split, all_metrics_saved_as_json
- failures found: none
- repairs attempted: none
- remaining limitations: Categorical component labels are the primary predictors in this public workbook.

## 2026-06-28T11:43:34.758185+00:00 - phase_7_uncertainty_calibration

- status: PASS
- files created/updated: reports/uncertainty_calibration_report.md, reports/metrics/uncertainty_calibration_metrics.json, reports/figures/uncertainty_vs_error.png, reports/figures/calibration_bins.png, data/processed/uncertainty/*_uncertainty.csv
- checks run: uncertainty_evaluated_against_actual_errors, empirical_coverage_reported, low_confidence_predictions_flagged, domain_distance_proxy_reported
- failures found: none
- repairs attempted: none
- remaining limitations: Tree-ensemble variance is a heuristic uncertainty proxy., Conformal intervals are retrospective and depend on calibration residuals from the available public records., Uncertainty is evaluated against actual errors but is not claimed to be perfect.

## 2026-06-28T11:45:47.420104+00:00 - phase_8_active_learning_simulation

- status: PASS
- files created/updated: reports/active_learning_report.md, reports/metrics/active_learning_metrics.json, reports/figures/active_learning_budget_curve.png, reports/figures/top_yield_recovery_curve.png, data/processed/active_learning_curves.csv, data/processed/active_learning_summary.csv
- checks run: random_baseline_included, multiple_seeds_used, no_future_target_leakage, selected_records_existing_only, limitations_stated
- failures found: none
- repairs attempted: none
- remaining limitations: Retrospective active-learning simulation over existing public records only., The simulation does not instruct anyone to run reactions., Candidate component labels are known as public records; target yields are revealed only after simulated acquisition.

## 2026-06-28T11:48:15.114625+00:00 - phase_9_existing_record_ranking

- status: PASS
- files created/updated: reports/ranked_existing_reaction_records.csv, reports/existing_record_ranking_report.md, reports/metrics/existing_record_ranking_metrics.json
- checks run: ranking_contains_existing_records_only, uncertainty_or_confidence_included, domain_warning_included, limitations_included, no_lab_ready_claim
- failures found: none
- repairs attempted: none
- remaining limitations: Ranking is based on out-of-fold predictions for existing public records only., The table omits component labels to avoid recipe-style public output., Scores are decision-support diagnostics for retrospective analysis, not lab-ready conditions.

## 2026-06-28T11:48:21.305490+00:00 - phase_10_interpretability

- status: PASS
- files created/updated: reports/model_interpretability_report.md, reports/metrics/model_interpretability_metrics.json, reports/figures/feature_importance.png, reports/figures/error_by_component.png
- checks run: permutation_importance_included, component_contribution_summaries_included, feature_importance_for_tree_model_included, error_analysis_by_component_included, held_out_component_failure_cases_summarized, no_causality_overclaim
- failures found: none
- repairs attempted: none
- remaining limitations: Importances describe model behavior, not chemical causality., One-hot categorical features cannot infer molecular mechanism., High-error component groups are anonymized in public reports.

## 2026-06-28T11:51:41.259910+00:00 - phase_9_existing_record_ranking

- status: PASS
- files created/updated: reports/ranked_existing_reaction_records.csv, reports/existing_record_ranking_report.md, reports/metrics/existing_record_ranking_metrics.json
- checks run: ranking_contains_existing_records_only, uncertainty_or_confidence_included, domain_warning_included, limitations_included, no_lab_ready_claim
- failures found: none
- repairs attempted: none
- remaining limitations: Ranking is based on out-of-fold predictions for existing public records only., The table omits component labels to avoid recipe-style public output., Scores are decision-support diagnostics for retrospective analysis, not lab-ready conditions.

## 2026-06-28T11:51:47.197369+00:00 - phase_10_interpretability

- status: PASS
- files created/updated: reports/model_interpretability_report.md, reports/metrics/model_interpretability_metrics.json, reports/figures/feature_importance.png, reports/figures/error_by_component.png
- checks run: permutation_importance_included, component_contribution_summaries_included, feature_importance_for_tree_model_included, error_analysis_by_component_included, held_out_component_failure_cases_summarized, no_causality_overclaim
- failures found: none
- repairs attempted: none
- remaining limitations: Importances describe model behavior, not chemical causality., One-hot categorical features cannot infer molecular mechanism., High-error component groups are anonymized in public reports.

## 2026-06-28T11:51:47.927866+00:00 - phase_11_final_report

- status: PASS
- files created/updated: reports/final_project_report.md, reports/metrics/final_summary.json, docs/model_card.md, docs/data_card.md
- checks run: final report sections written, safe-scope phrases included, model and data cards written
- failures found: none
- repairs attempted: none
- remaining limitations: Final report inherits dataset and categorical-feature limitations.

## 2026-06-28T11:51:47.974309+00:00 - phase_16_final_quality_gate

- status: DEGRADED
- files created/updated: reports/final_quality_gate_report.md, reports/metrics/final_quality_gate_report.json
- checks run: dataset_source_and_license_documented, no_raw_row_dumps_in_reports, no_wet_lab_protocol_instructions, no_generated_chemistry_claims, mean_baseline_included, random_and_grouped_validation_included_where_possible, metrics_saved, active_learning_existing_records_only, ranking_clearly_retrospective, limitations_section_exists, reproduce_small_works, tests_pass, portfolio_page_updated_only_if_project_credible, cv_bullets_evidence_backed, no_unsupported_claims
- failures found: no_wet_lab_protocol_instructions, reproduce_small_works, tests_pass, portfolio_page_updated_only_if_project_credible, cv_bullets_evidence_backed, no_unsupported_claims
- repairs attempted: none
- remaining limitations: Manual source-license review is still recommended before redistributing the raw workbook., Portfolio/CV wording should remain metric-free unless supported by final_summary.json.

## 2026-06-28T11:52:06.925807+00:00 - phase_11_final_report

- status: PASS
- files created/updated: reports/final_project_report.md, reports/metrics/final_summary.json, docs/model_card.md, docs/data_card.md
- checks run: final report sections written, safe-scope phrases included, model and data cards written
- failures found: none
- repairs attempted: none
- remaining limitations: Final report inherits dataset and categorical-feature limitations.

## 2026-06-28T11:52:06.968201+00:00 - phase_16_final_quality_gate

- status: DEGRADED
- files created/updated: reports/final_quality_gate_report.md, reports/metrics/final_quality_gate_report.json
- checks run: dataset_source_and_license_documented, no_raw_row_dumps_in_reports, no_wet_lab_protocol_instructions, no_generated_chemistry_claims, mean_baseline_included, random_and_grouped_validation_included_where_possible, metrics_saved, active_learning_existing_records_only, ranking_clearly_retrospective, limitations_section_exists, reproduce_small_works, tests_pass, portfolio_page_updated_only_if_project_credible, cv_bullets_evidence_backed, no_unsupported_claims
- failures found: reproduce_small_works, tests_pass, portfolio_page_updated_only_if_project_credible, cv_bullets_evidence_backed
- repairs attempted: none
- remaining limitations: Manual source-license review is still recommended before redistributing the raw workbook., Portfolio/CV wording should remain metric-free unless supported by final_summary.json.

## 2026-06-28T11:52:13.923539+00:00 - phase_1_dataset_selection

- status: DEGRADED
- files created/updated: data/DATA_CARD.md, data/dataset_manifest.json, reports/dataset_selection_report.md, reports/metrics/dataset_selection_metrics.json
- checks run: fixture mode selected, component columns present, target column present, row count recorded
- failures found: public benchmark not used in this run
- repairs attempted: none
- remaining limitations: Retrospective public-data benchmark only., Component structures are not provided in the selected workbook; structure-based features are skipped unless SMILES are added externally., The workflow ranks existing public records only and does not generate new reaction conditions.

## 2026-06-28T11:52:14.394193+00:00 - phase_2_data_audit

- status: PASS
- files created/updated: reports/data_audit_report.md, reports/metrics/data_audit_metrics.json
- checks run: raw row count computed, duplicate count computed, missing target count computed, component cardinalities computed
- failures found: none
- repairs attempted: none
- remaining limitations: Audit reports aggregate counts only., Invalid component identifiers are string-presence checks, not chemical-validity checks.

## 2026-06-28T11:52:14.821483+00:00 - phase_3_reaction_cleaning

- status: PASS
- files created/updated: data/processed/clean_reactions.csv, reports/reaction_cleaning_report.md, reports/metrics/reaction_cleaning_metrics.json
- checks run: numeric target standardized, component strings standardized, duplicates removed, impossible yields excluded
- failures found: none
- repairs attempted: none
- remaining limitations: Component strings are standardized as categorical labels; missing chemistry is not invented., No component SMILES are available in the selected workbook, so molecular descriptors are skipped unless external structures are supplied., Rows outside 0-100 percent yield are excluded rather than clipped.

## 2026-06-28T11:52:16.156854+00:00 - phase_4_component_featurization

- status: PASS
- files created/updated: data/processed/features/categorical_onehot.npz, data/processed/features/feature_index.csv, data/processed/features/feature_metadata.json, reports/feature_engineering_report.md, reports/metrics/feature_engineering_metrics.json
- checks run: no_target_leakage_in_features, feature_rows_align_clean_rows, missing_structures_handled_explicitly, no_yield_derived_columns_used
- failures found: none
- repairs attempted: none
- remaining limitations: Molecular descriptors and fingerprints skipped because component SMILES are not present., Categorical baseline is the primary feature family for this workbook.

## 2026-06-28T11:52:17.774858+00:00 - phase_5_validation_design

- status: PASS
- files created/updated: data/processed/splits/*.json, reports/validation_design_report.md, reports/metrics/validation_design_metrics.json
- checks run: random_split_available, grouped_or_out_of_component_available, no_group_overlap_for_grouped_splits, split_sizes_reported, target_distribution_reported
- failures found: none
- repairs attempted: none
- remaining limitations: Small grouped splits are flagged when applicable., Held-out group values are not printed.

## 2026-06-28T11:52:22.330233+00:00 - phase_6_model_benchmark

- status: PASS
- files created/updated: reports/model_benchmark_report.md, reports/metrics/model_benchmark_metrics.json, reports/figures/model_comparison_by_split.png, reports/figures/predicted_vs_observed.png, reports/figures/error_by_yield_bin.png, data/processed/models/best_model.joblib
- checks run: mean_baseline_included, grouped_or_out_of_component_split_included, random_split_not_sole_evidence, best_model_selected_by_reliability_split, all_metrics_saved_as_json
- failures found: none
- repairs attempted: none
- remaining limitations: Categorical component labels are the primary predictors in this public workbook.

## 2026-06-28T11:52:28.146972+00:00 - phase_7_uncertainty_calibration

- status: PASS
- files created/updated: reports/uncertainty_calibration_report.md, reports/metrics/uncertainty_calibration_metrics.json, reports/figures/uncertainty_vs_error.png, reports/figures/calibration_bins.png, data/processed/uncertainty/*_uncertainty.csv
- checks run: uncertainty_evaluated_against_actual_errors, empirical_coverage_reported, low_confidence_predictions_flagged, domain_distance_proxy_reported
- failures found: none
- repairs attempted: none
- remaining limitations: Tree-ensemble variance is a heuristic uncertainty proxy., Conformal intervals are retrospective and depend on calibration residuals from the available public records., Uncertainty is evaluated against actual errors but is not claimed to be perfect.

## 2026-06-28T11:52:39.134952+00:00 - phase_8_active_learning_simulation

- status: PASS
- files created/updated: reports/active_learning_report.md, reports/metrics/active_learning_metrics.json, reports/figures/active_learning_budget_curve.png, reports/figures/top_yield_recovery_curve.png, data/processed/active_learning_curves.csv, data/processed/active_learning_summary.csv
- checks run: random_baseline_included, multiple_seeds_used, no_future_target_leakage, selected_records_existing_only, limitations_stated
- failures found: none
- repairs attempted: none
- remaining limitations: Retrospective active-learning simulation over existing public records only., The simulation does not instruct anyone to run reactions., Candidate component labels are known as public records; target yields are revealed only after simulated acquisition.

## 2026-06-28T11:52:42.373844+00:00 - phase_9_existing_record_ranking

- status: PASS
- files created/updated: reports/ranked_existing_reaction_records.csv, reports/existing_record_ranking_report.md, reports/metrics/existing_record_ranking_metrics.json
- checks run: ranking_contains_existing_records_only, uncertainty_or_confidence_included, domain_warning_included, limitations_included, no_lab_ready_claim
- failures found: none
- repairs attempted: none
- remaining limitations: Ranking is based on out-of-fold predictions for existing public records only., The table omits component labels to avoid recipe-style public output., Scores are decision-support diagnostics for retrospective analysis, not lab-ready conditions.

## 2026-06-28T11:52:47.233432+00:00 - phase_10_interpretability

- status: PASS
- files created/updated: reports/model_interpretability_report.md, reports/metrics/model_interpretability_metrics.json, reports/figures/feature_importance.png, reports/figures/error_by_component.png
- checks run: permutation_importance_included, component_contribution_summaries_included, feature_importance_for_tree_model_included, error_analysis_by_component_included, held_out_component_failure_cases_summarized, no_causality_overclaim
- failures found: none
- repairs attempted: none
- remaining limitations: Importances describe model behavior, not chemical causality., One-hot categorical features cannot infer molecular mechanism., High-error component groups are anonymized in public reports.

## 2026-06-28T11:52:47.949559+00:00 - phase_11_final_report

- status: PASS
- files created/updated: reports/final_project_report.md, reports/metrics/final_summary.json, docs/model_card.md, docs/data_card.md
- checks run: final report sections written, safe-scope phrases included, model and data cards written
- failures found: none
- repairs attempted: none
- remaining limitations: Final report inherits dataset and categorical-feature limitations.

## 2026-06-28T11:52:47.988662+00:00 - phase_16_final_quality_gate

- status: DEGRADED
- files created/updated: reports/final_quality_gate_report.md, reports/metrics/final_quality_gate_report.json
- checks run: dataset_source_and_license_documented, no_raw_row_dumps_in_reports, no_wet_lab_protocol_instructions, no_generated_chemistry_claims, mean_baseline_included, random_and_grouped_validation_included_where_possible, metrics_saved, active_learning_existing_records_only, ranking_clearly_retrospective, limitations_section_exists, reproduce_small_works, tests_pass, portfolio_page_updated_only_if_project_credible, cv_bullets_evidence_backed, no_unsupported_claims
- failures found: tests_pass, portfolio_page_updated_only_if_project_credible, cv_bullets_evidence_backed
- repairs attempted: none
- remaining limitations: Manual source-license review is still recommended before redistributing the raw workbook., Portfolio/CV wording should remain metric-free unless supported by final_summary.json.

## 2026-06-28T11:53:00.060189+00:00 - phase_1_dataset_selection

- status: PASS
- files created/updated: data/DATA_CARD.md, data/dataset_manifest.json, reports/dataset_selection_report.md, reports/metrics/dataset_selection_metrics.json
- checks run: public source reachable, component columns present, target column present, row count recorded
- failures found: none
- repairs attempted: none
- remaining limitations: Retrospective public-data benchmark only., Component structures are not provided in the selected workbook; structure-based features are skipped unless SMILES are added externally., The workflow ranks existing public records only and does not generate new reaction conditions.

## 2026-06-28T11:53:00.782161+00:00 - phase_2_data_audit

- status: PASS
- files created/updated: reports/data_audit_report.md, reports/metrics/data_audit_metrics.json
- checks run: raw row count computed, duplicate count computed, missing target count computed, component cardinalities computed
- failures found: none
- repairs attempted: none
- remaining limitations: Audit reports aggregate counts only., Invalid component identifiers are string-presence checks, not chemical-validity checks.

## 2026-06-28T11:53:01.597081+00:00 - phase_3_reaction_cleaning

- status: PASS
- files created/updated: data/processed/clean_reactions.csv, reports/reaction_cleaning_report.md, reports/metrics/reaction_cleaning_metrics.json
- checks run: numeric target standardized, component strings standardized, duplicates removed, impossible yields excluded
- failures found: none
- repairs attempted: none
- remaining limitations: Component strings are standardized as categorical labels; missing chemistry is not invented., No component SMILES are available in the selected workbook, so molecular descriptors are skipped unless external structures are supplied., Rows outside 0-100 percent yield are excluded rather than clipped.

## 2026-06-28T11:53:03.031825+00:00 - phase_4_component_featurization

- status: PASS
- files created/updated: data/processed/features/categorical_onehot.npz, data/processed/features/feature_index.csv, data/processed/features/feature_metadata.json, reports/feature_engineering_report.md, reports/metrics/feature_engineering_metrics.json
- checks run: no_target_leakage_in_features, feature_rows_align_clean_rows, missing_structures_handled_explicitly, no_yield_derived_columns_used
- failures found: none
- repairs attempted: none
- remaining limitations: Molecular descriptors and fingerprints skipped because component SMILES are not present., Categorical baseline is the primary feature family for this workbook.

## 2026-06-28T11:53:04.675558+00:00 - phase_5_validation_design

- status: PASS
- files created/updated: data/processed/splits/*.json, reports/validation_design_report.md, reports/metrics/validation_design_metrics.json
- checks run: random_split_available, grouped_or_out_of_component_available, no_group_overlap_for_grouped_splits, split_sizes_reported, target_distribution_reported
- failures found: none
- repairs attempted: none
- remaining limitations: Small grouped splits are flagged when applicable., Held-out group values are not printed.

## 2026-06-28T11:53:11.395694+00:00 - phase_6_model_benchmark

- status: PASS
- files created/updated: reports/model_benchmark_report.md, reports/metrics/model_benchmark_metrics.json, reports/figures/model_comparison_by_split.png, reports/figures/predicted_vs_observed.png, reports/figures/error_by_yield_bin.png, data/processed/models/best_model.joblib
- checks run: mean_baseline_included, grouped_or_out_of_component_split_included, random_split_not_sole_evidence, best_model_selected_by_reliability_split, all_metrics_saved_as_json
- failures found: none
- repairs attempted: none
- remaining limitations: Categorical component labels are the primary predictors in this public workbook.

## 2026-06-28T11:53:18.953606+00:00 - phase_7_uncertainty_calibration

- status: PASS
- files created/updated: reports/uncertainty_calibration_report.md, reports/metrics/uncertainty_calibration_metrics.json, reports/figures/uncertainty_vs_error.png, reports/figures/calibration_bins.png, data/processed/uncertainty/*_uncertainty.csv
- checks run: uncertainty_evaluated_against_actual_errors, empirical_coverage_reported, low_confidence_predictions_flagged, domain_distance_proxy_reported
- failures found: none
- repairs attempted: none
- remaining limitations: Tree-ensemble variance is a heuristic uncertainty proxy., Conformal intervals are retrospective and depend on calibration residuals from the available public records., Uncertainty is evaluated against actual errors but is not claimed to be perfect.

## 2026-06-28T11:54:10.564051+00:00 - phase_8_active_learning_simulation

- status: PASS
- files created/updated: reports/active_learning_report.md, reports/metrics/active_learning_metrics.json, reports/figures/active_learning_budget_curve.png, reports/figures/top_yield_recovery_curve.png, data/processed/active_learning_curves.csv, data/processed/active_learning_summary.csv
- checks run: random_baseline_included, multiple_seeds_used, no_future_target_leakage, selected_records_existing_only, limitations_stated
- failures found: none
- repairs attempted: none
- remaining limitations: Retrospective active-learning simulation over existing public records only., The simulation does not instruct anyone to run reactions., Candidate component labels are known as public records; target yields are revealed only after simulated acquisition.

## 2026-06-28T11:54:15.465376+00:00 - phase_9_existing_record_ranking

- status: PASS
- files created/updated: reports/ranked_existing_reaction_records.csv, reports/existing_record_ranking_report.md, reports/metrics/existing_record_ranking_metrics.json
- checks run: ranking_contains_existing_records_only, uncertainty_or_confidence_included, domain_warning_included, limitations_included, no_lab_ready_claim
- failures found: none
- repairs attempted: none
- remaining limitations: Ranking is based on out-of-fold predictions for existing public records only., The table omits component labels to avoid recipe-style public output., Scores are decision-support diagnostics for retrospective analysis, not lab-ready conditions.

## 2026-06-28T11:54:21.316050+00:00 - phase_10_interpretability

- status: PASS
- files created/updated: reports/model_interpretability_report.md, reports/metrics/model_interpretability_metrics.json, reports/figures/feature_importance.png, reports/figures/error_by_component.png
- checks run: permutation_importance_included, component_contribution_summaries_included, feature_importance_for_tree_model_included, error_analysis_by_component_included, held_out_component_failure_cases_summarized, no_causality_overclaim
- failures found: none
- repairs attempted: none
- remaining limitations: Importances describe model behavior, not chemical causality., One-hot categorical features cannot infer molecular mechanism., High-error component groups are anonymized in public reports.

## 2026-06-28T11:54:22.103469+00:00 - phase_11_final_report

- status: PASS
- files created/updated: reports/final_project_report.md, reports/metrics/final_summary.json, docs/model_card.md, docs/data_card.md
- checks run: final report sections written, safe-scope phrases included, model and data cards written
- failures found: none
- repairs attempted: none
- remaining limitations: Final report inherits dataset and categorical-feature limitations.

## 2026-06-28T11:54:22.146230+00:00 - phase_16_final_quality_gate

- status: DEGRADED
- files created/updated: reports/final_quality_gate_report.md, reports/metrics/final_quality_gate_report.json
- checks run: dataset_source_and_license_documented, no_raw_row_dumps_in_reports, no_wet_lab_protocol_instructions, no_generated_chemistry_claims, mean_baseline_included, random_and_grouped_validation_included_where_possible, metrics_saved, active_learning_existing_records_only, ranking_clearly_retrospective, limitations_section_exists, reproduce_small_works, tests_pass, portfolio_page_updated_only_if_project_credible, cv_bullets_evidence_backed, no_unsupported_claims
- failures found: tests_pass, portfolio_page_updated_only_if_project_credible, cv_bullets_evidence_backed
- repairs attempted: none
- remaining limitations: Manual source-license review is still recommended before redistributing the raw workbook., Portfolio/CV wording should remain metric-free unless supported by final_summary.json.

## 2026-06-28T11:55:22.450510+00:00 - phase_14_portfolio_integration

- status: PASS
- files created/updated: ../README.md, ../projects/reaction-yield-ml.md
- checks run: project added as fourth project, safe wording used, portfolio updated after quality gates passed
- failures found: none
- repairs attempted: none
- remaining limitations: Portfolio root was created in the current workspace because no existing homepage was present.

## 2026-06-28T11:55:22.451699+00:00 - phase_15_cv_bullets

- status: PASS
- files created/updated: ../portfolio_assets/cv_bullets_reaction_yield_ml.md, ../portfolio_assets/interview_talking_points_reaction_yield_ml.md
- checks run: evidence source included, risk status included, no unsupported metrics added
- failures found: none
- repairs attempted: none
- remaining limitations: Metric values should be copied only from final_summary.json if later added to CV.

## 2026-06-28T11:55:22.506167+00:00 - phase_16_final_quality_gate

- status: PASS
- files created/updated: reports/final_quality_gate_report.md, reports/metrics/final_quality_gate_report.json
- checks run: dataset_source_and_license_documented, no_raw_row_dumps_in_reports, no_wet_lab_protocol_instructions, no_generated_chemistry_claims, mean_baseline_included, random_and_grouped_validation_included_where_possible, metrics_saved, active_learning_existing_records_only, ranking_clearly_retrospective, limitations_section_exists, reproduce_small_works, tests_pass, portfolio_page_updated_only_if_project_credible, cv_bullets_evidence_backed, no_unsupported_claims
- failures found: none
- repairs attempted: none
- remaining limitations: Manual source-license review is still recommended before redistributing the raw workbook., Portfolio/CV wording should remain metric-free unless supported by final_summary.json.

## 2026-06-28T11:56:14.889594+00:00 - phase_16_final_quality_gate

- status: PASS
- files created/updated: reports/final_quality_gate_report.md, reports/metrics/final_quality_gate_report.json
- checks run: dataset_source_and_license_documented, no_raw_row_dumps_in_reports, no_wet_lab_protocol_instructions, no_generated_chemistry_claims, mean_baseline_included, random_and_grouped_validation_included_where_possible, metrics_saved, active_learning_existing_records_only, ranking_clearly_retrospective, limitations_section_exists, reproduce_small_works, tests_pass, portfolio_page_updated_only_if_project_credible, cv_bullets_evidence_backed, no_unsupported_claims
- failures found: none
- repairs attempted: none
- remaining limitations: Manual source-license review is still recommended before redistributing the raw workbook., Portfolio/CV wording should remain metric-free unless supported by final_summary.json.

## 2026-06-28T11:56:29.571460+00:00 - phase_0_project_scaffold

- status: PASS
- files created/updated: README.md, pyproject.toml, requirements.txt, environment.yml, Makefile, src/reaction_yield_ml/**, scripts/, tests/, docs/, reports/
- checks run: branch created, directory scaffold created, make commands available, setup repaired for host Python
- failures found: initial venv setup failed because ensurepip is unavailable
- repairs attempted: Makefile setup falls back to user-site install with /usr/bin/python3
- remaining limitations: This host lacks python3-venv/ensurepip, so commands default to /usr/bin/python3.

## 2026-06-28T11:56:29.572462+00:00 - phase_12_notebook

- status: PASS
- files created/updated: notebooks/reaction_yield_ml_walkthrough.ipynb
- checks run: notebook exists, aggregate-only inspection cells, cached metrics used
- failures found: none
- repairs attempted: none
- remaining limitations: Notebook is a walkthrough and is not executed as part of the automated gate.

## 2026-06-28T11:56:29.573281+00:00 - phase_13_tests_reproducibility

- status: PASS
- files created/updated: tests/test_data_loading.py, tests/test_cleaning.py, tests/test_features.py, tests/test_splits.py, tests/test_no_target_leakage.py, tests/test_metrics_schema.py, tests/test_reports_exist.py, reports/metrics/pytest_status.json, reports/metrics/reproduce_small_status.json
- checks run: make reproduce-small completed, make test completed, pytest marker written
- failures found: none
- repairs attempted: none
- remaining limitations: Small fixture is synthetic and not used for benchmark claims.

## 2026-06-28T11:56:29.618469+00:00 - phase_16_final_quality_gate

- status: PASS
- files created/updated: reports/final_quality_gate_report.md, reports/metrics/final_quality_gate_report.json
- checks run: dataset_source_and_license_documented, no_raw_row_dumps_in_reports, no_wet_lab_protocol_instructions, no_generated_chemistry_claims, mean_baseline_included, random_and_grouped_validation_included_where_possible, metrics_saved, active_learning_existing_records_only, ranking_clearly_retrospective, limitations_section_exists, reproduce_small_works, tests_pass, portfolio_page_updated_only_if_project_credible, cv_bullets_evidence_backed, no_unsupported_claims
- failures found: none
- repairs attempted: none
- remaining limitations: Manual source-license review is still recommended before redistributing the raw workbook., Portfolio/CV wording should remain metric-free unless supported by final_summary.json.

## 2026-06-28T12:38:44.079966+00:00 - phase_1_dataset_selection

- status: PASS
- files created/updated: data/DATA_CARD.md, data/dataset_manifest.json, reports/dataset_selection_report.md, reports/metrics/dataset_selection_metrics.json
- checks run: public source reachable, component columns present, target column present, row count recorded
- failures found: none
- repairs attempted: none
- remaining limitations: Retrospective public-data benchmark only., Component structures are not provided in the selected workbook; structure-based features are skipped unless SMILES are added externally., The workflow ranks existing public records only and does not generate new reaction conditions.

## 2026-06-28T12:38:44.885989+00:00 - phase_2_data_audit

- status: PASS
- files created/updated: reports/data_audit_report.md, reports/metrics/data_audit_metrics.json
- checks run: raw row count computed, duplicate count computed, missing target count computed, component cardinalities computed
- failures found: none
- repairs attempted: none
- remaining limitations: Audit reports aggregate counts only., Invalid component identifiers are string-presence checks, not chemical-validity checks.

## 2026-06-28T12:38:45.660768+00:00 - phase_3_reaction_cleaning

- status: PASS
- files created/updated: data/processed/clean_reactions.csv, reports/reaction_cleaning_report.md, reports/metrics/reaction_cleaning_metrics.json
- checks run: numeric target standardized, component strings standardized, duplicates removed, impossible yields excluded
- failures found: none
- repairs attempted: none
- remaining limitations: Component strings are standardized as categorical labels; missing chemistry is not invented., No component SMILES are available in the selected workbook, so molecular descriptors are skipped unless external structures are supplied., Rows outside 0-100 percent yield are excluded rather than clipped.

## 2026-06-28T12:38:48.039903+00:00 - phase_4_component_featurization

- status: PASS
- files created/updated: data/processed/features/categorical_onehot.npz, data/processed/features/feature_index.csv, data/processed/features/feature_metadata.json, reports/feature_engineering_report.md, reports/metrics/feature_engineering_metrics.json
- checks run: no_target_leakage_in_features, feature_rows_align_clean_rows, missing_structures_handled_explicitly, no_yield_derived_columns_used
- failures found: none
- repairs attempted: none
- remaining limitations: Molecular descriptors and fingerprints skipped because component SMILES are not present., Categorical baseline is the primary feature family for this workbook.

## 2026-06-28T12:38:49.772270+00:00 - phase_5_validation_design

- status: PASS
- files created/updated: data/processed/splits/*.json, reports/validation_design_report.md, reports/metrics/validation_design_metrics.json
- checks run: random_split_available, grouped_or_out_of_component_available, no_group_overlap_for_grouped_splits, split_sizes_reported, target_distribution_reported
- failures found: none
- repairs attempted: none
- remaining limitations: Small grouped splits are flagged when applicable., Held-out group values are not printed.

## 2026-06-28T12:38:57.611660+00:00 - phase_6_model_benchmark

- status: PASS
- files created/updated: reports/model_benchmark_report.md, reports/metrics/model_benchmark_metrics.json, reports/figures/model_comparison_by_split.png, reports/figures/predicted_vs_observed.png, reports/figures/error_by_yield_bin.png, data/processed/models/best_model.joblib
- checks run: mean_baseline_included, grouped_or_out_of_component_split_included, random_split_not_sole_evidence, best_model_selected_by_reliability_split, all_metrics_saved_as_json
- failures found: none
- repairs attempted: none
- remaining limitations: Categorical component labels are the primary predictors in this public workbook.

## 2026-06-28T12:39:05.745603+00:00 - phase_7_uncertainty_calibration

- status: PASS
- files created/updated: reports/uncertainty_calibration_report.md, reports/metrics/uncertainty_calibration_metrics.json, reports/figures/uncertainty_vs_error.png, reports/figures/calibration_bins.png, data/processed/uncertainty/*_uncertainty.csv
- checks run: uncertainty_evaluated_against_actual_errors, empirical_coverage_reported, low_confidence_predictions_flagged, domain_distance_proxy_reported
- failures found: none
- repairs attempted: none
- remaining limitations: Tree-ensemble variance is a heuristic uncertainty proxy., Conformal intervals are retrospective and depend on calibration residuals from the available public records., Uncertainty is evaluated against actual errors but is not claimed to be perfect.

## 2026-06-28T12:39:57.987903+00:00 - phase_8_active_learning_simulation

- status: PASS
- files created/updated: reports/active_learning_report.md, reports/metrics/active_learning_metrics.json, reports/figures/active_learning_budget_curve.png, reports/figures/top_yield_recovery_curve.png, data/processed/active_learning_curves.csv, data/processed/active_learning_summary.csv
- checks run: random_baseline_included, multiple_seeds_used, shared_initial_labeled_set_per_seed, no_future_target_leakage, selected_records_existing_only, limitations_stated
- failures found: none
- repairs attempted: none
- remaining limitations: Retrospective active-learning simulation over existing public records only., The simulation does not instruct anyone to run reactions., Candidate component labels are known as public records; target yields are revealed only after simulated acquisition., All strategies share the same initial labeled set for a given random seed.

## 2026-06-28T12:40:03.211827+00:00 - phase_9_existing_record_ranking

- status: PASS
- files created/updated: reports/ranked_existing_reaction_records.csv, reports/existing_record_ranking_report.md, reports/metrics/existing_record_ranking_metrics.json
- checks run: ranking_contains_existing_records_only, uncertainty_or_confidence_included, domain_warning_included, limitations_included, no_lab_ready_claim
- failures found: none
- repairs attempted: none
- remaining limitations: Ranking is based on out-of-fold predictions for existing public records only., The table omits component labels to avoid recipe-style public output., Scores are decision-support diagnostics for retrospective analysis, not lab-ready conditions.

## 2026-06-28T12:40:09.657044+00:00 - phase_10_interpretability

- status: PASS
- files created/updated: reports/model_interpretability_report.md, reports/metrics/model_interpretability_metrics.json, reports/figures/feature_importance.png, reports/figures/error_by_component.png
- checks run: permutation_importance_included, component_contribution_summaries_included, feature_importance_for_tree_model_included, error_analysis_by_component_included, held_out_component_failure_cases_summarized, no_causality_overclaim
- failures found: none
- repairs attempted: none
- remaining limitations: Importances describe model behavior, not chemical causality., One-hot categorical features cannot infer molecular mechanism., High-error component groups are anonymized in public reports.

## 2026-06-28T12:40:10.481417+00:00 - phase_11_final_report

- status: PASS
- files created/updated: reports/final_project_report.md, reports/metrics/final_summary.json, docs/model_card.md, docs/data_card.md
- checks run: final report sections written, safe-scope phrases included, model and data cards written
- failures found: none
- repairs attempted: none
- remaining limitations: Final report inherits dataset and categorical-feature limitations.

## 2026-06-28T12:40:10.530772+00:00 - phase_16_final_quality_gate

- status: PASS
- files created/updated: reports/final_quality_gate_report.md, reports/metrics/final_quality_gate_report.json
- checks run: dataset_source_and_license_documented, no_raw_row_dumps_in_reports, no_wet_lab_protocol_instructions, no_generated_chemistry_claims, mean_baseline_included, random_and_grouped_validation_included_where_possible, metrics_saved, active_learning_existing_records_only, ranking_clearly_retrospective, limitations_section_exists, reproduce_small_works, tests_pass, portfolio_page_updated_only_if_project_credible, cv_bullets_evidence_backed, no_unsupported_claims
- failures found: none
- repairs attempted: none
- remaining limitations: Manual source-license review is still recommended before redistributing the raw workbook., Portfolio/CV wording should remain metric-free unless supported by final_summary.json.

## 2026-06-28T12:41:06.663983+00:00 - phase_6_model_benchmark

- status: PASS
- files created/updated: reports/model_benchmark_report.md, reports/metrics/model_benchmark_metrics.json, reports/figures/model_comparison_by_split.png, reports/figures/predicted_vs_observed.png, reports/figures/error_by_yield_bin.png, data/processed/models/best_model.joblib
- checks run: mean_baseline_included, grouped_or_out_of_component_split_included, random_split_not_sole_evidence, best_model_selected_by_reliability_split, all_metrics_saved_as_json
- failures found: none
- repairs attempted: none
- remaining limitations: Categorical component labels are the primary predictors in this public workbook.

## 2026-06-28T12:41:11.744862+00:00 - phase_9_existing_record_ranking

- status: PASS
- files created/updated: reports/ranked_existing_reaction_records.csv, reports/existing_record_ranking_report.md, reports/metrics/existing_record_ranking_metrics.json
- checks run: ranking_contains_existing_records_only, uncertainty_or_confidence_included, domain_warning_included, limitations_included, no_lab_ready_claim
- failures found: none
- repairs attempted: none
- remaining limitations: Ranking is based on out-of-fold predictions for existing public records only., The table omits component labels to avoid recipe-style public output., Scores are decision-support diagnostics for retrospective analysis, not lab-ready conditions.

## 2026-06-28T12:41:17.714805+00:00 - phase_10_interpretability

- status: PASS
- files created/updated: reports/model_interpretability_report.md, reports/metrics/model_interpretability_metrics.json, reports/figures/feature_importance.png, reports/figures/error_by_component.png
- checks run: permutation_importance_included, component_contribution_summaries_included, feature_importance_for_tree_model_included, error_analysis_by_component_included, held_out_component_failure_cases_summarized, no_causality_overclaim
- failures found: none
- repairs attempted: none
- remaining limitations: Importances describe model behavior, not chemical causality., One-hot categorical features cannot infer molecular mechanism., High-error component groups are anonymized in public reports.

## 2026-06-28T12:41:18.606861+00:00 - phase_11_final_report

- status: PASS
- files created/updated: reports/final_project_report.md, reports/metrics/final_summary.json, docs/model_card.md, docs/data_card.md
- checks run: final report sections written, safe-scope phrases included, model and data cards written
- failures found: none
- repairs attempted: none
- remaining limitations: Final report inherits dataset and categorical-feature limitations.

## 2026-06-28T12:41:18.658308+00:00 - phase_16_final_quality_gate

- status: PASS
- files created/updated: reports/final_quality_gate_report.md, reports/metrics/final_quality_gate_report.json
- checks run: dataset_source_and_license_documented, no_raw_row_dumps_in_reports, no_wet_lab_protocol_instructions, no_generated_chemistry_claims, mean_baseline_included, random_and_grouped_validation_included_where_possible, metrics_saved, active_learning_existing_records_only, ranking_clearly_retrospective, limitations_section_exists, reproduce_small_works, tests_pass, portfolio_page_updated_only_if_project_credible, cv_bullets_evidence_backed, no_unsupported_claims
- failures found: none
- repairs attempted: none
- remaining limitations: Manual source-license review is still recommended before redistributing the raw workbook., Portfolio/CV wording should remain metric-free unless supported by final_summary.json.

## 2026-06-28T12:45:17.557411+00:00 - phase_4_component_featurization

- status: PASS
- files created/updated: data/processed/features/categorical_onehot.npz, data/processed/features/feature_index.csv, data/processed/features/feature_metadata.json, reports/feature_engineering_report.md, reports/metrics/feature_engineering_metrics.json
- checks run: no_target_leakage_in_features, feature_rows_align_clean_rows, missing_structures_handled_explicitly, no_yield_derived_columns_used
- failures found: none
- repairs attempted: none
- remaining limitations: Molecular descriptors and fingerprints skipped because component SMILES are not present., Categorical baseline is the primary feature family for this workbook.

## 2026-06-28T12:45:19.213048+00:00 - phase_5_validation_design

- status: PASS
- files created/updated: data/processed/splits/*.json, reports/validation_design_report.md, reports/metrics/validation_design_metrics.json
- checks run: random_split_available, grouped_or_out_of_component_available, no_group_overlap_for_grouped_splits, split_sizes_reported, target_distribution_reported
- failures found: none
- repairs attempted: none
- remaining limitations: Small grouped splits are flagged when applicable., Held-out group values are not printed.

## 2026-06-28T12:45:24.273358+00:00 - phase_9_existing_record_ranking

- status: PASS
- files created/updated: reports/ranked_existing_reaction_records.csv, reports/existing_record_ranking_report.md, reports/metrics/existing_record_ranking_metrics.json
- checks run: ranking_contains_existing_records_only, uncertainty_or_confidence_included, domain_warning_included, limitations_included, no_lab_ready_claim
- failures found: none
- repairs attempted: none
- remaining limitations: Ranking is based on out-of-fold predictions for existing public records only., The table omits component labels to avoid recipe-style public output., Scores are decision-support diagnostics for retrospective analysis, not lab-ready conditions.

## 2026-06-28T12:45:30.981111+00:00 - phase_10_interpretability

- status: PASS
- files created/updated: reports/model_interpretability_report.md, reports/metrics/model_interpretability_metrics.json, reports/figures/feature_importance.png, reports/figures/error_by_component.png
- checks run: permutation_importance_included, component_contribution_summaries_included, feature_importance_for_tree_model_included, error_analysis_by_component_included, held_out_component_failure_cases_summarized, no_causality_overclaim
- failures found: none
- repairs attempted: none
- remaining limitations: Importances describe model behavior, not chemical causality., One-hot categorical features cannot infer molecular mechanism., High-error component groups are anonymized in public reports.

## 2026-06-28T12:45:31.838412+00:00 - phase_11_final_report

- status: PASS
- files created/updated: reports/final_project_report.md, reports/metrics/final_summary.json, docs/model_card.md, docs/data_card.md
- checks run: final report sections written, safe-scope phrases included, model and data cards written
- failures found: none
- repairs attempted: none
- remaining limitations: Final report inherits dataset and categorical-feature limitations.

## 2026-06-28T12:45:31.894179+00:00 - phase_16_final_quality_gate

- status: PASS
- files created/updated: reports/final_quality_gate_report.md, reports/metrics/final_quality_gate_report.json
- checks run: dataset_source_and_license_documented, no_raw_row_dumps_in_reports, no_wet_lab_protocol_instructions, no_generated_chemistry_claims, mean_baseline_included, random_and_grouped_validation_included_where_possible, metrics_saved, active_learning_existing_records_only, ranking_clearly_retrospective, limitations_section_exists, reproduce_small_works, tests_pass, portfolio_page_updated_only_if_project_credible, cv_bullets_evidence_backed, no_unsupported_claims
- failures found: none
- repairs attempted: none
- remaining limitations: Manual source-license review is still recommended before redistributing the raw workbook., Portfolio/CV wording should remain metric-free unless supported by final_summary.json.

## 2026-06-28T12:48:42.313289+00:00 - phase_9_existing_record_ranking

- status: PASS
- files created/updated: reports/ranked_existing_reaction_records.csv, reports/existing_record_ranking_report.md, reports/metrics/existing_record_ranking_metrics.json
- checks run: ranking_contains_existing_records_only, uncertainty_or_confidence_included, domain_warning_included, limitations_included, no_lab_ready_claim
- failures found: none
- repairs attempted: none
- remaining limitations: Ranking is based on out-of-fold predictions for existing public records only., The table omits component labels to avoid recipe-style public output., Scores are decision-support diagnostics for retrospective analysis, not lab-ready conditions.

## 2026-06-28T12:48:48.673922+00:00 - phase_10_interpretability

- status: PASS
- files created/updated: reports/model_interpretability_report.md, reports/metrics/model_interpretability_metrics.json, reports/figures/feature_importance.png, reports/figures/error_by_component.png
- checks run: permutation_importance_included, component_contribution_summaries_included, feature_importance_for_tree_model_included, error_analysis_by_component_included, held_out_component_failure_cases_summarized, no_causality_overclaim
- failures found: none
- repairs attempted: none
- remaining limitations: Importances describe model behavior, not chemical causality., One-hot categorical features cannot infer molecular mechanism., High-error component groups are anonymized in public reports.

## 2026-06-28T12:48:49.602579+00:00 - phase_11_final_report

- status: PASS
- files created/updated: reports/final_project_report.md, reports/metrics/final_summary.json, docs/model_card.md, docs/data_card.md
- checks run: final report sections written, safe-scope phrases included, model and data cards written
- failures found: none
- repairs attempted: none
- remaining limitations: Final report inherits dataset and categorical-feature limitations.

## 2026-06-28T12:48:49.650035+00:00 - phase_16_final_quality_gate

- status: PASS
- files created/updated: reports/final_quality_gate_report.md, reports/metrics/final_quality_gate_report.json
- checks run: dataset_source_and_license_documented, no_raw_row_dumps_in_reports, no_wet_lab_protocol_instructions, no_generated_chemistry_claims, mean_baseline_included, random_and_grouped_validation_included_where_possible, metrics_saved, active_learning_existing_records_only, ranking_clearly_retrospective, limitations_section_exists, reproduce_small_works, tests_pass, portfolio_page_updated_only_if_project_credible, cv_bullets_evidence_backed, no_unsupported_claims
- failures found: none
- repairs attempted: none
- remaining limitations: Manual source-license review is still recommended before redistributing the raw workbook., Portfolio/CV wording should remain metric-free unless supported by final_summary.json.

