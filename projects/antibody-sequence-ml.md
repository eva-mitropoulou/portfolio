# Antibody Sequence ML And Existing-Record Prioritization

## 1. Overview

Built a public-data antibody sequence ML workflow for retrospective benchmarking and existing-record prioritization. The work is framed as benchmark evidence and record triage, not therapeutic antibody design.

## 2. Scientific / Technical Problem

Public antibody datasets contain heterogeneous assay labels, target annotations, sequence completeness, and source metadata. The technical question was whether sequence-based baseline models, antibody-specific representations, and validation controls could support a reproducible retrospective benchmark without overstating prospective biological utility.

## 3. Dataset Or System

Evidence source: `Computational-Chemistry/antibody_project/antibody-prioritization`.

- CoV-AbDab-derived public-data workflow.
- Strict labeled dataset: 5,573 records in `reports/metrics/core_dataset_audit.json`.
- Broader prepared records: 11,748 records in `reports/metrics/core_dataset_audit.json`.
- Annotated paired subset: 5,092 paired CDR-annotated candidates in `reports/metrics/core_dataset_audit.json`.
- OAS background retrieval was treated as unknown-target background, not true negative neutralization data.

No raw biological sequences are shown in this portfolio layer.

## 4. Methods

- Sequence cleaning and prepared-table generation from public CoV-AbDab-derived records.
- Character k-mer TF-IDF baselines with logistic regression.
- Grouped validation using available grouping columns where meaningful.
- CDR and region annotation for paired records.
- Antibody embedding and pretrained antibody/protein model benchmarks, including AbLang2-style embeddings and IgBert/BERT-family benchmark artifacts where present.
- OAS background retrieval as a separate background-retrieval analysis with explicit label semantics.
- Diversity-aware existing-record shortlist from broader prepared records.

## 5. Validation Strategy

- Primary validation used grouped evaluation where the group feature was meaningful.
- Random-split results were retained as a baseline but not used as the strongest public claim.
- Matched CDR/region feature comparisons were used to compare whole-pair versus region-local k-mer features on the same paired subset.
- OAS retrieval was kept separate from neutralization benchmarking because OAS records are unknown-target background records, not assay-confirmed non-neutralizers.

## 6. Key Results

- Grouped k-mer pair-text baseline: PR-AUC 0.824 and ROC-AUC 0.781 in `grouped_validation_metrics.json`.
- Matched paired-subset audit: region-local k-mer features improved PR-AUC by 0.044 and ROC-AUC by 0.042 relative to whole-pair k-mers in `matched_kmer_benchmark_audit.json`.
- Frozen pretrained representation benchmarks did not beat the grouped k-mer reference on both primary metrics in `pretrained_frozen_baseline_metrics.json`.
- The language-model benchmark registry marks pretrained/embedding models as benchmark evidence, not the primary scorer; `lm_benchmark_registry.json` reports that pretrained models did not beat matched k-mer baselines.
- Diversity-aware existing-record prioritization produced a 23-record shortlist in `diversity_aware_shortlist_summary.json`.

## 7. Figures

- `docs/assets/figures/antibody_pipeline.svg`: public-safe workflow diagram.
- `docs/assets/figures/antibody_benchmark_pr_auc.png`: aggregate benchmark figure.
- Source evidence includes benchmark and prioritization figures under `reports/figures/` in the antibody project.

## 8. Limitations

- Retrospective public labels only.
- Heterogeneous assays and sources.
- Existing-record prioritization only.
- No therapeutic design, sequence generation, mutation, or optimization claim.
- No prospective validation.
- OAS, where used, is unknown-target background and not true negative neutralization data.

## 9. Reproducibility

Public-safe reproduction in this portfolio is limited to a small cached-report path.

- Summary metrics: `antibody-sequence-ml/reports/metrics/summary.json`.
- Final report: `antibody-sequence-ml/reports/final_report.md`.
- Small command: `make reproduce-small` from `antibody-sequence-ml/`.
- Full reproduction may require raw public-data downloads, model weights, embeddings, and more compute than a recruiter review should assume.

## 10. What This Demonstrates

- Ability to build an evidence-bounded ML benchmark from noisy public biological data.
- Awareness of leakage, grouping, label semantics, and benchmark interpretation.
- Practical sequence-feature engineering with k-mer, CDR-local, embedding, and pretrained-model comparisons.
- Pharma-facing communication discipline: prioritization and benchmarking are kept separate from therapeutic design claims.
