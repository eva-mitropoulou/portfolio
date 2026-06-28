# Antibody Sequence ML And Existing-Record Prioritization

Public-data antibody sequence ML workflow for retrospective benchmarking and existing-record prioritization.

## Claim Boundary

This project is a benchmarking and triage workflow. It makes no therapeutic antibody design, sequence generation, mutation optimization, prospective validation, or clinical utility claim.

## Evidence Summary

- CoV-AbDab-derived public-data workflow.
- Strict labeled dataset: 5,573 records.
- Broader prepared-record set: 11,748 records.
- Grouped k-mer pair-text baseline: PR-AUC 0.824 and ROC-AUC 0.781.
- Matched paired-subset audit: region-local k-mers improved PR-AUC by 0.044 and ROC-AUC by 0.042 over whole-pair k-mers.
- Frozen pretrained representation benchmarks did not beat the grouped k-mer reference on both primary metrics.
- Diversity-aware existing-record shortlist: 23 records.

## Public Artifacts

- `reports/final_report.md`
- `reports/metrics/summary.json`
- `figures/antibody_pipeline.svg`
- `figures/antibody_benchmark_pr_auc.png`
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
- OAS background records are unknown-target records, not true negatives.
- Prioritization only; no therapeutic design or prospective validation.
