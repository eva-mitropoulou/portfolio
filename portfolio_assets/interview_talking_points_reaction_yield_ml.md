# Interview Talking Points: Reaction Yield Prediction From Public HTE Data

## Project Framing

- Retrospective public-data benchmark for reaction-yield modeling from HTE records.
- Focused on public HTE component-label yield modeling: components, validation leakage, uncertainty, and decision-support ranking over existing records.
- Portfolio role: reaction-informatics and ML-validation case study.

## Technical Decisions

- Used the public Buchwald-Hartwig HTE benchmark because it has component columns and measured yields.
- Treated the workbook as categorical component data because component structures were not available.
- Evaluated random, grouped, and out-of-component splits to compare interpolation with component generalization.
- Selected the best model using the reliability-oriented grouped split.
- Added uncertainty analysis and conformal interval coverage as diagnostics.
- Simulated active learning as budgeted selection over existing records.

## Files To Reference

- Final report: `projects/reaction-yield-ml/artifacts/reports/final_project_report.md`
- Model benchmark metrics: `projects/reaction-yield-ml/artifacts/reports/metrics/model_benchmark_metrics.json`
- Final quality gate: `projects/reaction-yield-ml/artifacts/reports/metrics/final_quality_gate_report.json`
- Reproduction commands: `projects/reaction-yield-ml/artifacts/Makefile`

## Interview Emphasis

- Retrospective benchmark, existing-record ranking, validation, and uncertainty diagnostics.
- Component-label scope in the current workbook.
- Extension path through public component structures, RDKit descriptors, and reaction fingerprints.
