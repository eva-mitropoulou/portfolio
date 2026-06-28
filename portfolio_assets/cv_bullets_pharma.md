# CV Bullets: Pharma / Cheminformatics

## Recommended Safe Bullets

| Bullet text | Supporting repository/report | Metric source | Risk level |
|---|---|---|---|
| Built a retrospective EGFR QSAR benchmark from ChEMBL IC50 records using RDKit descriptors, Morgan fingerprints, random split evaluation, and Bemis-Murcko scaffold split validation. | `egfr-cadd-qsar-admet/reports/final_report.md` | `egfr-cadd-qsar-admet/reports/metrics/summary.json` | safe |
| Demonstrated validation-risk awareness by comparing Morgan random forest performance under random split and scaffold split, with RMSE/R2 changing from 0.712/0.719 to 0.871/0.550. | `projects/egfr-qsar-cadd.md` | `egfr-cadd-qsar-admet/reports/metrics/summary.json` | safe |
| Built a retrospective public-data HTE reaction-yield prediction workflow with reaction cleaning, categorical component featurization, random and out-of-component validation, uncertainty/error diagnostics, active-learning simulation, and existing-record ranking. | `reaction-yield-ml/reports/final_project_report.md` | `reaction-yield-ml/reports/metrics/final_summary.json` | safe |
| Demonstrated reaction-yield validation-risk awareness by selecting the final model on an additive-held-out grouped split rather than relying only on random-split performance. | `projects/reaction-yield-ml.md` | `reaction-yield-ml/reports/metrics/model_benchmark_metrics.json` | safe |
| Built a validation-aware antibody sequence ML workflow using public CoV-AbDab and OAS data, including strict label curation, k-mer and antibody-language-model benchmarks, CDR/region analysis, source-holdout validation, calibration/threshold analysis, OAS background retrieval, and diversity-aware existing-record prioritization; selected a whole-pair k-mer TF-IDF logistic model as the most defensible broad scorer, with grouped ROC-AUC 0.780/PR-AUC 0.823 and source-robust ROC-AUC 0.610/PR-AUC 0.636, explicitly identifying source/study effects and calibration scope. | `antibody-sequence-ml/reports/final_report.md`, `antibody-sequence-ml/docs/MODEL_CARD.md` | `antibody-sequence-ml/reports/metrics/summary.json` | safe |
| Framed antibody outputs as retrospective benchmarking and existing-record prioritization, explicitly separating public-label model triage from therapeutic design or prospective validation. | `projects/antibody-sequence-ml.md` | `portfolio_audit/evidence_map.json` | safe |
| Created recruiter-readable notebooks and cached metric summaries for antibody sequence ML and EGFR QSAR workflows without exposing raw biological sequences or raw molecule rows. | `notebooks/01_antibody_sequence_ml_workflow.ipynb`, `notebooks/02_egfr_qsar_cadd_benchmark.ipynb` | Notebook JSON and project summaries | safe |

## Needs Review Before Use

| Bullet text | Supporting repository/report | Metric source | Risk level |
|---|---|---|---|
| Applied antibody language models to improve public antibody neutralization prediction. | Antibody benchmark registry exists, but comparisons are mixed and noisy. | `antibody-sequence-ml/reports/metrics/summary.json` | needs review |

## Excluded Unsupported Claims

| Claim | Reason | Risk level |
|---|---|---|
| Designed therapeutic antibodies with AI. | No therapeutic design evidence; prohibited framing for this portfolio. | unsupported |
| Built a production-grade EGFR predictor. | Evidence supports retrospective baseline QSAR only. | unsupported |
| Generated operational reaction conditions. | Evidence supports retrospective reaction-yield benchmarking and existing-record ranking only. | unsupported |
| Demonstrated clinical utility for EGFR or antibody models. | No prospective or clinical validation evidence. | unsupported |
