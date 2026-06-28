# EGFR QSAR / CADD Benchmark

## 1. Overview

Built a retrospective EGFR QSAR/CADD benchmark from ChEMBL IC50 records using RDKit descriptors, Morgan fingerprints, baseline models, and leakage-aware validation.

## 2. Scientific / Technical Problem

Random train/test splits can overstate molecular-property model performance when close chemical analogs appear in both train and test sets. This project uses EGFR pIC50 modeling as a practical baseline to compare random-split performance with Bemis-Murcko scaffold split performance.

## 3. Dataset Or System

Evidence source: `egfr-cadd-qsar-admet` in the portfolio and `Computational-Chemistry/pharma_project`.

- ChEMBL EGFR IC50 workflow.
- Cleaned EGFR activity records: 10,834 rows.
- Model-ready records: 10,593 rows.
- RDKit descriptor table: 10,834 rows.

Raw molecule rows are not reproduced in this portfolio summary.

## 4. Methods

- ChEMBL EGFR IC50 activity retrieval and curation.
- pIC50 transformation and model-ready filtering.
- RDKit physicochemical descriptors.
- Morgan fingerprints.
- Baseline models including random forest, gradient boosting, ridge regression, and dummy mean baselines.
- Applicability-domain summary using similarity bins where available.

## 5. Validation Strategy

- Random split baseline for conventional retrospective comparison.
- Bemis-Murcko scaffold split to test generalization across chemical scaffolds.
- Model comparisons are reported as retrospective baselines, not production predictors.

## 6. Key Results

Committed metrics support the following public numbers:

| Model / split | RMSE | R2 |
|---|---:|---:|
| Morgan random forest, random split | 0.712 | 0.719 |
| Morgan random forest, scaffold split | 0.871 | 0.550 |

The scaffold split drop is the key portfolio result because it demonstrates leakage-aware validation practice.

## 7. Figures

- `docs/assets/figures/egfr_random_vs_scaffold.png`: random versus scaffold split performance.
- `docs/assets/figures/egfr_predicted_vs_actual.png`: predicted versus experimental pIC50 for the scaffold baseline.
- Source evidence includes `egfr-cadd-qsar-admet/figures/random_vs_scaffold_validation.png` and `egfr-cadd-qsar-admet/figures/scaffold_fingerprint_predicted_vs_actual.png`.

## 8. Limitations

- Baseline retrospective QSAR.
- No production-grade model claim.
- No prospective validation.
- No clinical utility claim.
- No binding-mechanism claim without additional structure or mechanistic evidence.

## 9. Reproducibility

- Summary metrics: `egfr-cadd-qsar-admet/reports/metrics/summary.json`.
- Final report: `egfr-cadd-qsar-admet/reports/final_report.md`.
- Small command: `make reproduce-small` from `egfr-cadd-qsar-admet/`.
- Recruiter notebook: `notebooks/02_egfr_qsar_cadd_benchmark.ipynb`.
- Full reproduction may require network access to ChEMBL and the original data-curation path; the public portfolio includes cached summaries.

## 10. What This Demonstrates

- Practical cheminformatics workflow construction with RDKit and ChEMBL.
- Clear distinction between random split and scaffold split validation.
- Ability to communicate model performance drops as evidence of validation rigor rather than as a failure.
- Pharma-facing caution around retrospective QSAR baselines.
