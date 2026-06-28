# Antibody Sequence ML And Existing-Record Prioritization

Public-data antibody sequence ML workflow for retrospective benchmarking and existing-record prioritization.

## Claim Boundary

This project is a benchmarking and triage workflow. It makes no therapeutic antibody design, sequence generation, mutation optimization, prospective validation, or clinical utility claim.

## Final Status

- Final selected model: `whole_pair_kmer`.
- Final consistency audit: PASS.
- Tests: 8 passed.
- Missing final packaging artifacts: none.

## Evidence Summary

- CoV-AbDab-derived public-data workflow with strict and broader dataset handling.
- Strict labeled dataset: 5,573 records.
- Broader prepared-record set: 11,748 records.
- Whole-pair k-mer TF-IDF logistic regression remained the most defensible broad scorer.
- V-gene grouped validation: ROC-AUC 0.7800 and PR-AUC 0.8233.
- Source-robust weighted leave-source-out validation: ROC-AUC 0.6095 and PR-AUC 0.6363.
- Threshold 0.7: precision 0.8266, recall 0.3062, coverage 0.3051.
- OAS broad and matched retrieval remained a background-enrichment diagnostic, not binder-vs-non-binder prediction.
- Diversity-aware existing-record shortlist: 23 records.

## Public Artifacts

- `reports/final_report.md`
- `reports/final_flagship_project_report.md`
- `reports/final_consistency_audit.md`
- `reports/final_artifact_map.md`
- `reports/metrics/summary.json`
- `docs/DATA_CARD.md`
- `docs/MODEL_CARD.md`
- `figures/antibody_pipeline.svg`
- `figures/antibody_benchmark_pr_auc.png`
- `figures/source_robust_model_comparison.png`
- `figures/calibration_curve.png`
- `../notebooks/01_antibody_sequence_ml_workflow.ipynb`

## Reproduce Small

```bash
make reproduce-small
make figures
make report
```

The small path validates cached public-safe artifacts. Full reproduction may require raw public-data downloads, embeddings, model weights, and heavier compute.

## Limitations

- Retrospective public labels.
- Heterogeneous assays and sources.
- Source/study effects limit cross-source generalization.
- Scores are prioritization signals, not calibrated prospective neutralisation probabilities.
- OAS background records are unknown-target records, not true negatives.
- Prioritization only; no therapeutic design or prospective validation.
