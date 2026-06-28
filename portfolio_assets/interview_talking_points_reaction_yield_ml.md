# Interview Talking Points: Reaction Yield Prediction And Synthesis-Aware ML

## Project Framing

- Retrospective public-data benchmark for reaction-yield modeling from HTE records.
- Focused on synthesis-aware machine learning: components, validation leakage, uncertainty, and decision-support ranking over existing records.
- Safe boundary: no new chemistry generation and no operational synthesis guidance.

## Technical Decisions

- Used the public Buchwald-Hartwig HTE benchmark because it has component columns and measured yields.
- Treated the workbook as categorical component data because component structures were not available.
- Evaluated random, grouped, and out-of-component splits so random split performance was not the only evidence.
- Selected the best model using the reliability-oriented grouped split rather than only the random split.
- Added uncertainty analysis and conformal interval coverage as diagnostics, not guarantees.
- Simulated active learning as budgeted selection over existing records only.

## Evidence To Reference

- Final report: `reaction-yield-ml/reports/final_project_report.md`
- Model benchmark metrics: `reaction-yield-ml/reports/metrics/model_benchmark_metrics.json`
- Final quality gate: `reaction-yield-ml/reports/metrics/final_quality_gate_report.json`
- Reproduction commands: `reaction-yield-ml/Makefile`

## Risk Status

- Safe: retrospective benchmark, existing-record ranking, validation and uncertainty diagnostics.
- Needs review: any public redistribution of the raw workbook beyond source/citation notes.
- Unsupported: claims of guaranteed experimental success, operational condition guidance, or generated chemistry.
