# EGFR CADD And QSAR Decision Workflow

## 1. Overview

Built a retrospective EGFR CADD and QSAR workflow from public ChEMBL IC50 records. The project keeps the full path together: activity curation, RDKit descriptors, Morgan fingerprints, baseline QSAR, scaffold-aware validation, uncertainty checks, simple drug-likeness and model-risk triage, SAR-style error analysis, active-learning simulation, a GPU GCN benchmark, and one co-crystal redocking check.

Portfolio role: primary pharma-facing QSAR and CADD decision-workflow case study.

## 2. Scientific And Technical Problem

Random molecular train/test splits can look better than they should when close analogs appear in both train and test sets. Public ChEMBL activities also combine measurements from different assays and papers. The useful question was not only whether a QSAR model can fit EGFR pIC50, but where that model becomes risky.

## 3. Dataset Or System

- Target: EGFR, ChEMBL target CHEMBL203.
- Raw ChEMBL EGFR IC50 rows: 26,600.
- Clean molecule-level pIC50 rows: 10,834.
- Model-ready molecules after broad sanity filters: 10,593.
- Main structure check: EGFR PDB 5UG9 with ligand 8AM.

The portfolio page reports aggregate counts and figures.

## 4. Methods

- ChEMBL IC50 retrieval and curation.
- Exact nM IC50 filtering, pIC50 conversion, and molecule-level median aggregation.
- RDKit descriptors, Morgan fingerprints, and combined features.
- Random split, scaffold split, random KFold, scaffold GroupKFold, assay-aware split, and document-aware split.
- Conformal-style pIC50 uncertainty checks.
- Applicability-domain analysis using max Tanimoto similarity.
- SAR-support/error analysis: descriptor importance, Morgan bit importance, activity cliffs, and scaffold-level errors.
- ADMET-style and model-risk triage over existing molecules.
- EGFR co-crystal contact analysis across 1M17, 2ITY, 4HJO, and 5UG9.
- Vina redocking for 5UG9 with ligand 8AM.

## 5. Validation Strategy

The main model comparison uses Morgan fingerprint Random Forest baselines. Random split is retained as a conventional reference, while scaffold split, assay grouping, and document grouping are used to show how performance changes under harder validation contexts.

## 6. Key Results

| Check | Result |
|---|---:|
| Morgan RF, random split | RMSE 0.712, R2 0.719 |
| Morgan RF, scaffold split | RMSE 0.871, R2 0.550 |
| High-similarity applicability-domain MAE | 0.513 |
| Low-similarity applicability-domain MAE | 0.957 |
| Assay-aware validation | completed, zero group overlap |
| Document-aware validation | completed, zero group overlap |
| Activity-cliff candidates | 607 |
| GPU GCN benchmark | scaffold-split R2 0.198 |
| Redocking | 5UG9 with ligand 8AM, RMSD 0.968 A |

The scaffold and applicability-domain results are the main takeaways: the model is useful in familiar chemistry and less reliable farther from its training domain.

## 7. Figures

- `docs/assets/figures/egfr_random_vs_scaffold.png`: original random versus scaffold split summary.
- `docs/assets/figures/egfr_validation_contexts.png`: random, scaffold, assay, and document validation contexts.
- `docs/assets/figures/egfr_conformal_coverage.png`: conformal-style uncertainty coverage summary.
- `docs/assets/figures/egfr_redocking_overlay.png`: 5UG9 co-crystal versus redocked 8AM pose overlay.

## 8. Interpretation Context

- Public ChEMBL IC50 values combine assays and papers, so scaffold, assay, document, and applicability-domain checks carry the main interpretation.
- ADMET-style triage uses simple drug-likeness and model-risk proxy rules.
- Redocking is used as a co-crystal pose-recovery check alongside QSAR and applicability-domain analysis.

## 9. Reproducibility

- Repo: <https://github.com/eva-mitropoulou/egfr-cadd-qsar-admet>
- Portfolio artifacts: `artifacts/`.
- Final report: `artifacts/reports/final_egfr_cadd_qsar_report.md`.
- Notebook: `notebooks/02_egfr_qsar_cadd_benchmark.ipynb`.
- Light reproduction command: `bash scripts/reproduce_egfr_final_reports.sh` in the standalone repo.

## 10. What This Demonstrates

- RDKit and ChEMBL cheminformatics workflow construction.
- Model-risk-aware validation beyond one random split.
- Clear communication of applicability-domain and uncertainty behavior.
- Structure-based evidence used as a retrospective pose-recovery check.
