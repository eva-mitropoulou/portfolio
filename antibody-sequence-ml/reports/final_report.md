# Final Report: Antibody Sequence ML And Existing-Record Prioritization

## Purpose

Create a public-data antibody sequence ML workflow for retrospective benchmarking and existing-record prioritization, while keeping claims separate from therapeutic design or prospective validation.

## Evidence Used

- `core_dataset_audit.json`
- `grouped_validation_metrics.json`
- `matched_kmer_benchmark_audit.json`
- `pretrained_frozen_baseline_metrics.json`
- `lm_benchmark_registry.json`
- `oas_matched_background_retrieval_metrics.json`
- `diversity_aware_shortlist_summary.json`

## Methods

The workflow used prepared public antibody records, character k-mer TF-IDF features, logistic-regression baselines, grouped validation, matched CDR/region comparisons, antibody representation benchmarks, OAS background retrieval, and diversity-aware existing-record prioritization.

## Key Results

| Result | Value |
|---|---:|
| Strict labeled records | 5,573 |
| Broader prepared records | 11,748 |
| Grouped k-mer pair-text PR-AUC | 0.824 |
| Grouped k-mer pair-text ROC-AUC | 0.781 |
| Region-local PR-AUC delta vs whole-pair k-mers | 0.044 |
| Region-local ROC-AUC delta vs whole-pair k-mers | 0.042 |
| Diversity-aware shortlist size | 23 |

## Interpretation

The safest public interpretation is that sparse k-mer and CDR-local sequence features provide strong, reproducible baselines for noisy public-label retrospective benchmarking. Pretrained antibody model outputs are presented as benchmark evidence, not as therapeutic design tools.

## Limitations

- Retrospective public labels.
- Heterogeneous assays and source records.
- OAS background records are unknown-target background, not true negatives.
- No prospective validation.
- No therapeutic design, sequence generation, mutation, or optimization claim.
