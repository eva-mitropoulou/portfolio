# Antibody Sequence ML And Existing-Record Prioritization

## 1. Overview

Built a public-data antibody sequence ML workflow for retrospective benchmarking and existing-record prioritization. The work is framed as benchmark evidence and record triage, not therapeutic antibody design.

## 2. Scientific And Technical Problem

Public antibody datasets contain heterogeneous assay labels, target annotations, sequence completeness, and source metadata. The technical question was whether sequence-based baseline models, antibody-specific representations, and validation controls could support a reproducible retrospective benchmark without overstating prospective biological utility.

## 3. Dataset Or System

Evidence source: mirrored portfolio artifacts under `antibody-sequence-ml/`, plus the portfolio evidence audit.

- CoV-AbDab-derived public-data workflow.
- Strict labeled dataset: 5,573 records in `reports/metrics/core_dataset_audit.json`.
- Broader prepared records: 11,748 records in `reports/metrics/core_dataset_audit.json`.
- Annotated paired subset: 5,092 paired CDR-annotated candidates in `reports/metrics/core_dataset_audit.json`.
- OAS background retrieval was treated as unknown-target background rather than assayed neutralization controls.

No raw biological sequences are shown in this portfolio layer.

## 4. Methods

- Sequence cleaning and prepared-table generation from public CoV-AbDab-derived records.
- Character k-mer TF-IDF baselines with logistic regression.
- Grouped validation using available grouping columns where meaningful.
- Source-holdout validation and source-robust model selection.
- Calibration and threshold analysis for high-confidence review cutoffs.
- CDR and region annotation for paired records.
- Antibody embedding and pretrained antibody model benchmarks, including AbLang2-style embeddings and IgBert-family benchmark artifacts where present.
- OAS background retrieval as a separate background-retrieval analysis with explicit label semantics.
- Diversity-aware existing-record shortlist from broader prepared records.

## 5. Validation Strategy

- Primary validation used grouped evaluation where the group feature was meaningful.
- Random-split results were retained as a baseline but not used as the strongest public claim.
- Matched CDR feature comparisons were used to compare whole-pair versus region-local k-mer features on the same paired subset.
- Source-holdout validation was used as a skeptical control for source and study effects.
- Source-robust model selection compared conservative k-mer variants and selected `whole_pair_kmer`.
- OAS retrieval was kept separate from neutralization benchmarking because OAS records are unknown-target background records, not assay-confirmed non-neutralizers.

## 6. Key Results

- Final selected model: `whole_pair_kmer`, a compact whole-pair k-mer TF-IDF logistic-regression scorer.
- V-gene grouped whole-pair k-mer validation: ROC-AUC 0.7800 and PR-AUC 0.8233.
- Source-robust weighted leave-source-out validation: ROC-AUC 0.6095 and PR-AUC 0.6363.
- Threshold 0.7 gave precision 0.8266, recall 0.3062, and coverage 0.3051 for high-confidence review.
- Final consistency audit: PASS, with zero missing expected packaging artifacts.
- Tests: 8 passed.
- Pretrained antibody model outputs are retained as benchmark evidence rather than the primary scorer.
- Diversity-aware existing-record prioritization produced a 23-record shortlist in `diversity_aware_shortlist_summary.json`.

## 7. Figures

- `docs/assets/figures/antibody_pipeline.svg`: public-safe workflow diagram.
- `docs/assets/figures/antibody_benchmark_pr_auc.png`: aggregate benchmark figure.
- `docs/assets/figures/antibody_source_robust_model_comparison.png`: source-robust model-selection comparison.
- `docs/assets/figures/antibody_calibration_curve.png`: calibration curve.
- Source evidence includes benchmark and prioritization figures under `reports/figures/` in the antibody project.

## 8. Limitations

- Retrospective public labels only.
- Heterogeneous assays and sources.
- Source and study effects limit cross-source generalization.
- Existing-record prioritization only.
- Not a sequence-design, mutation, or optimization workflow.
- No prospective validation.
- OAS, where used, is unknown-target background rather than assayed neutralization controls.
- Model probabilities are prioritization signals, not calibrated prospective neutralisation probabilities.

## 9. Reproducibility

Public-safe reproduction in this portfolio is limited to a small cached-report path.

- Summary metrics: `antibody-sequence-ml/reports/metrics/summary.json`.
- Standalone repo: <https://github.com/eva-mitropoulou/antibody-prioritization>.
- Final report: `antibody-sequence-ml/reports/final_report.md`.
- Data card: `antibody-sequence-ml/docs/DATA_CARD.md`.
- Model card: `antibody-sequence-ml/docs/MODEL_CARD.md`.
- Artifact map: `antibody-sequence-ml/reports/final_artifact_map.md`.
- Consistency audit: `antibody-sequence-ml/reports/final_consistency_audit.md`.
- Small command: `make reproduce-small` from `antibody-sequence-ml/`.
- Full reproduction may require raw public-data downloads, model weights, embeddings, and more compute than a recruiter review should assume.

## 10. What This Demonstrates

- Ability to build an evidence-bounded ML benchmark from noisy public biological data.
- Awareness of leakage, grouping, source and study effects, label semantics, calibration, and benchmark interpretation.
- Practical sequence-feature engineering with k-mer, CDR-local, embedding, and pretrained-model comparisons.
- Pharma-facing communication discipline: prioritization and benchmarking are kept separate from design or optimization claims.
