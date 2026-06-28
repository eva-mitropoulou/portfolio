# Reaction Yield Prediction And Synthesis-Aware ML

## 1. Overview

Built a retrospective public-data HTE reaction-yield workflow with reaction cleaning, categorical component-based featurization, random and out-of-component validation, uncertainty diagnostics, active-learning simulation, and existing-record ranking.

## 2. Scientific And Technical Problem

Reaction-yield models need validation that tests component generalization, not only random interpolation. This project treats public HTE records as a benchmark for leakage-aware reaction-yield modeling and uncertainty-aware decision support.

## 3. Dataset

Evidence source: `reaction-yield-ml/data/dataset_manifest.json`.

- Public Buchwald-Hartwig HTE reaction-yield benchmark from the Ahneman, Dreher, and Doyle lineage.
- 3,955 clean records.
- Component columns: ligand, additive, base, aryl halide.
- Target: measured yield percentage.

## 4. Methods

- Aggregate-only data audit and reaction cleaning.
- Categorical component one-hot featurization; no structure-based reaction features are claimed for this workbook.
- Random, grouped, and out-of-component splits.
- Mean baseline, regularized linear models, random forest, and gradient boosting.
- Ensemble-variance and conformal-style uncertainty diagnostics with empirical coverage analysis.
- Budgeted active-learning simulation over existing records.
- Existing-record ranking with confidence and domain warnings.

## 5. Validation Strategy

Primary model selection used an additive-held-out grouped split. In this dataset, additive values form the highest-cardinality chemically meaningful grouping, so the grouped component split and the held-out additive split use the same held-out design. Random split performance is reported but not treated as sole evidence.

## 6. Key Results

Selected model: random forest.

Primary split: additive-held-out grouped split.

Supported metrics from `reaction-yield-ml/reports/metrics/final_summary.json`:

- MAE: 10.754
- RMSE: 14.237
- R2: 0.726
- Spearman: 0.860
- Top-10% enrichment: 7.333
- Primary-split 90% interval empirical coverage: 0.798

## 7. Figures

- `docs/assets/figures/reaction_yield_model_comparison.png`
- `docs/assets/figures/reaction_yield_active_learning_budget_curve.png`
- `docs/assets/figures/reaction_yield_uncertainty_vs_error.png`

## 8. Limitations

- Retrospective public-data benchmark only.
- No wet-lab protocol or operational synthesis guidance.
- No new chemistry generation.
- Existing-record ranking only.
- Component structures are unavailable in the selected workbook, so structure-based featurization is explicitly limited.
- Uncertainty diagnostics are evaluated against observed errors but are not guarantees.

## 9. Reproducibility

- Source and scripts: `reaction-yield-ml/src/`, `reaction-yield-ml/scripts/`.
- Reports: `reaction-yield-ml/reports/`.
- Metrics: `reaction-yield-ml/reports/metrics/`.
- Notebook: `notebooks/04_reaction_yield_ml_walkthrough.ipynb`.
- Small command: `make reproduce-small` from `reaction-yield-ml/`.
- Standalone repo: <https://github.com/eva-mitropoulou/reaction-yield-prediction>.

The raw public workbook is downloaded during reproduction and is not committed to the public portfolio.

## 10. What This Demonstrates

- Reaction-yield modeling and synthesis-aware ML framing.
- Data leakage audit and out-of-component validation.
- Uncertainty-aware prioritization.
- Active-learning simulation over existing public records.
- Clear public-portfolio boundaries around benchmark evidence and limitations.
