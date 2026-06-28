# Final Project Report

## 1. Executive Summary

Reaction Yield Prediction and Synthesis-Aware Triage from Public HTE Data is a retrospective public-data benchmark for reaction-yield modeling. It covers data curation, categorical component featurization, leakage-aware validation, uncertainty-aware prioritization, active-learning simulation, and existing-record ranking only.

This is not a wet-lab protocol, not a guarantee of experimental success, includes no new chemistry generation, and does not provide operational condition guidance.

## 2. Why Reaction-Yield Prediction Matters

Reaction-yield modeling helps evaluate whether machine-learning workflows can learn from historical high-throughput reaction records under validation designs that reflect component generalization rather than only random interpolation.

## 3. Dataset

- Dataset: Buchwald-Hartwig HTE yield benchmark (Ahneman/Dreher/Doyle lineage)
- Source mode: public_benchmark
- Raw row count: 3955
- Clean row count: 3955
- Target: reaction yield percentage
- Components: ligand, additive, base, aryl halide labels

## 4. Cleaning And Standardization

The pipeline standardizes the target as numeric percentage, normalizes component labels as strings, removes impossible target values, and removes exact duplicate component-target records. It does not invent missing chemistry.

## 5. Feature Engineering

- Primary feature family: categorical one-hot component encoding
- Feature count: 44
- Molecular descriptors/fingerprints: skipped because the selected workbook provides labels but no component SMILES
- Leakage audit: yield-derived columns are excluded from predictors

## 6. Validation Strategy

Valid splits: grouped_high_cardinality_component, out_of_additive, out_of_base, out_of_ligand, out_of_substrate, random_split

The benchmark includes random validation and grouped/out-of-component validation where possible. Random split performance is not treated as sole evidence.

## 7. Model Benchmark

- Selected model: random_forest
- Primary selection split: additive-held-out grouped split
- Internal split id: grouped_high_cardinality_component
- MAE: 10.7537
- RMSE: 14.2371
- R2: 0.7262
- Spearman: 0.8597
- Top-10% enrichment: 7.3333

Validation note: In this dataset, grouped_high_cardinality_component uses component_additive; it is therefore the additive-held-out grouped split and shares the same held-out group design as out_of_additive.

## 8. Uncertainty And Calibration

- Method: random-forest ensemble variance plus split conformal interval
- Primary split coverage: 0.7978
- Uncertainty-error Spearman: 0.6296

Uncertainty is evaluated against actual errors and low-confidence predictions are flagged. It is not claimed to be perfect.

## 9. Active-Learning Simulation

The active-learning simulation is a budgeted selection workflow over existing public records. It uses multiple seeds and includes a random baseline. It is not lab automation and does not instruct anyone to run reactions.

## 10. Existing-Record Ranking

The ranking table contains existing records only. It includes predicted yield, confidence/model-agreement diagnostics, domain warnings, and component-diversity score without operational synthesis instructions.

## 11. Limitations

- Component structures are unavailable in the selected workbook.
- Categorical features cannot support mechanistic claims.
- Out-of-component validation is more reliable than random split performance for generalization claims.
- Active-learning curves are retrospective simulations over existing records.
- Existing-record ranking is decision-support analysis, not lab-ready condition recommendation.

## 12. Reproducibility

```bash
make setup
make data
make features
make train
make evaluate
make active-learning
make report
make test
```

Small fixture smoke test:

```bash
make reproduce-small
```

The fixture is synthetic and does not support benchmark claims.

## 13. Portfolio/CV Wording

Built a retrospective public-data HTE reaction-yield prediction workflow with reaction cleaning, categorical component featurization, random and out-of-component validation, uncertainty/error diagnostics, active-learning simulation, and existing-record ranking for synthesis-aware ML.
