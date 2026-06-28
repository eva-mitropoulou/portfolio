# CV Bullets: Reaction Yield Prediction And Synthesis-Aware ML

## Short Version

- Built a retrospective public-data HTE reaction-yield prediction workflow with reaction cleaning, categorical component featurization, random and out-of-component validation, uncertainty diagnostics, active-learning simulation, and existing-record ranking for synthesis-aware ML.
  - Evidence source: `reaction-yield-ml/reports/final_project_report.md`
  - Risk status: safe

## Technical Version

- Developed a reproducible categorical component-based reaction-yield modeling benchmark on public HTE records, including leakage-aware split design, mean and ML baselines, uncertainty diagnostics with empirical coverage analysis, budgeted existing-record selection simulation, and safe ranking diagnostics for public portfolio review.
  - Evidence source: `reaction-yield-ml/reports/metrics/final_summary.json`
  - Risk status: safe

## Evidence Source

- `reaction-yield-ml/reports/metrics/model_benchmark_metrics.json`
- `reaction-yield-ml/reports/metrics/uncertainty_calibration_metrics.json`
- `reaction-yield-ml/reports/metrics/active_learning_metrics.json`
- `reaction-yield-ml/reports/metrics/final_quality_gate_report.json`

## Risk Notes

- Do not add metric values to a CV unless they are copied directly from `final_summary.json`.
- Do not describe this project as lab automation, procedural synthesis instruction, or a guarantee of experimental success.
