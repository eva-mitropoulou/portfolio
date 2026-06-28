# CV Bullets: Pharma and Cheminformatics

## Recommended Safe Bullets

| Bullet text | Supporting repository/report | Metric source | Risk level |
|---|---|---|---|
| Built a retrospective EGFR CADD/QSAR decision workflow from ChEMBL, curating 26,600 IC50 records into 10,593 model-ready molecules; benchmarked RDKit descriptor, Morgan fingerprint, and GPU PyTorch GCN models under random and scaffold splits, with Morgan RF achieving scaffold-split RMSE 0.871/R2 0.550; quantified applicability-domain degradation from high-similarity MAE 0.513 to low-similarity MAE 0.957; added assay-aware validation, split-conformal uncertainty, ADMET-style/model-risk triage, SAR/error analysis, active-learning simulation, CLI prediction, ligand-contact analysis across four EGFR PDB structures, and 5UG9 redocking validation recovering the co-crystal ligand pose at 0.968 A RMSD. | `egfr-cadd-qsar-admet/reports/final_egfr_cadd_qsar_report.md` | `egfr-cadd-qsar-admet/reports/metrics/egfr_final_hardening_status.json` | safe |
| Demonstrated validation-risk awareness in EGFR QSAR by comparing Morgan Random Forest random-split performance with scaffold, assay, document, and applicability-domain checks. | `projects/egfr-qsar-cadd.md` | `egfr-cadd-qsar-admet/reports/metrics/egfr_assay_aware_validation_metrics.json` | safe |
| Built a retrospective public-data HTE reaction-yield prediction workflow with reaction cleaning, categorical component featurization, random and out-of-component validation, uncertainty diagnostics, active-learning simulation, and existing-record ranking. | `reaction-yield-ml/reports/final_project_report.md` | `reaction-yield-ml/reports/metrics/final_summary.json` | safe |
| Demonstrated reaction-yield validation-risk awareness by selecting the final model on an additive-held-out grouped split rather than relying only on random-split performance. | `projects/reaction-yield-ml.md` | `reaction-yield-ml/reports/metrics/model_benchmark_metrics.json` | safe |
| Built a validation-aware antibody sequence ML workflow using public CoV-AbDab and OAS data, including strict label curation, k-mer and antibody-language-model benchmarks, CDR analysis, source-holdout validation, calibration analysis, OAS background retrieval, and diversity-aware existing-record prioritization; selected a whole-pair k-mer TF-IDF logistic model as the most defensible broad scorer, with grouped ROC-AUC 0.780 and PR-AUC 0.823 plus source-robust ROC-AUC 0.610 and PR-AUC 0.636, explicitly identifying source and study effects and calibration scope. | `antibody-sequence-ml/reports/final_report.md`, `antibody-sequence-ml/docs/MODEL_CARD.md` | `antibody-sequence-ml/reports/metrics/summary.json` | safe |
| Framed antibody outputs as retrospective benchmarking and existing-record prioritization, explicitly separating public-label model triage from therapeutic design or prospective validation. | `projects/antibody-sequence-ml.md` | `portfolio_audit/evidence_map.json` | safe |

## Excluded Unsupported Claims

| Claim | Reason | Risk level |
|---|---|---|
| Designed therapeutic antibodies with AI. | No therapeutic design evidence; prohibited framing for this portfolio. | unsupported |
| Built a production-grade EGFR predictor. | Evidence supports retrospective benchmarking and triage only. | unsupported |
| Generated operational reaction conditions. | Evidence supports retrospective reaction-yield benchmarking and existing-record ranking only. | unsupported |
| Demonstrated clinical utility for EGFR or antibody models. | No prospective or clinical validation evidence. | unsupported |
