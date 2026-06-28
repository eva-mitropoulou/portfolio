# Final Report: Antibody Sequence ML And Existing-Record Prioritization

## Purpose

Create a public-data antibody sequence ML workflow for retrospective benchmarking, source-aware validation, calibration analysis, OAS background retrieval, and existing-record prioritization.

## Final Status

| Packaging item | Status |
|---|---|
| Final selected model | `whole_pair_kmer` |
| Final consistency audit | PASS |
| Missing final packaging artifacts | 0 |
| Tests | 8 passed |
| Final report reproduction script | PASS |

## Artifacts Used

- `docs/DATA_CARD.md`
- `docs/MODEL_CARD.md`
- `reports/final_artifact_map.md`
- `reports/final_consistency_audit.md`
- `reports/final_flagship_project_report.md`
- `reports/metrics/source_robust_model_selection_metrics.json`
- `reports/metrics/final_consistency_audit.json`
- `reports/metrics/oas_matched_background_retrieval_metrics.json`

## Methods

The workflow used public CoV-AbDab-derived records, strict/broader dataset handling, k-mer TF-IDF baselines, pretrained antibody-model benchmarking, CDR/region analysis, source-holdout validation, source-robust model selection, calibration/threshold analysis, OAS broad and matched background retrieval, and diversity-aware existing-record prioritization.

## Key Results

| Result | Value |
|---|---:|
| Strict labeled records | 5,573 |
| Broader prepared records | 11,748 |
| Selected broad scorer | `whole_pair_kmer` |
| V-gene grouped ROC-AUC | 0.7800 |
| V-gene grouped PR-AUC | 0.8233 |
| Source-holdout macro ROC-AUC | 0.5605 |
| Source-holdout macro PR-AUC | 0.6454 |
| Source-robust weighted ROC-AUC | 0.6095 |
| Source-robust weighted PR-AUC | 0.6363 |
| Threshold 0.7 precision | 0.8266 |
| Threshold 0.7 recall | 0.3062 |
| Threshold 0.7 coverage | 0.3051 |
| Matched OAS retrieval ROC-AUC | 0.9911 |
| Matched OAS retrieval PR-AUC | 0.9893 |
| Diversity-aware shortlist size | 23 |

## Interpretation

Whole-pair k-mer TF-IDF logistic regression remained the most defensible broad scorer. It performed strongly under V-gene grouped validation but only modestly under source-holdout validation, showing that public antibody neutralisation labels contain source/study effects.

The workflow supports retrospective prioritization and high-confidence review of existing public records.

## OAS Background Retrieval

OAS retrieval showed that curated coronavirus antibody records were highly separable from sampled unknown-target natural antibody background, including matched controls. This module measures background enrichment and domain separation.

## Interpretation Context

- Public labels combine heterogeneous assays and source records.
- Source and study effects shape cross-source generalization.
- Scores are ranking and prioritization signals for reviewing existing records.
- OAS records are unknown-target natural antibody background.
