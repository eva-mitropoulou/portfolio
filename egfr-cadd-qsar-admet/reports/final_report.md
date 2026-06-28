# Final Report: EGFR QSAR / CADD Benchmark

## Purpose

Build a retrospective EGFR QSAR baseline from ChEMBL IC50 records and compare random-split performance with Bemis-Murcko scaffold split performance.

## Evidence Used

- `results/fingerprint_baseline_metrics.csv`
- `results/scaffold_fingerprint_metrics.csv`
- `results/descriptor_baseline_metrics.csv`
- `results/combined_baseline_metrics.csv`
- `results/applicability_domain_summary.csv`
- `figures/random_vs_scaffold_validation.png`
- `figures/scaffold_fingerprint_predicted_vs_actual.png`

## Methods

The workflow curated ChEMBL EGFR IC50 records, transformed activity values to pIC50, computed RDKit descriptors and Morgan fingerprints, trained baseline regressors, and compared random split with scaffold split validation.

## Key Results

| Model / split | RMSE | R2 |
|---|---:|---:|
| Morgan random forest, random split | 0.712 | 0.719 |
| Morgan random forest, scaffold split | 0.871 | 0.550 |

## Interpretation

The performance drop under scaffold split is the central result because it demonstrates leakage-aware validation. The model is presented as a retrospective baseline benchmark, not a production-grade predictor.

## Limitations

- Baseline retrospective QSAR.
- No production-grade model claim.
- No prospective validation.
- No clinical utility claim.
- No binding-mechanism claim.
