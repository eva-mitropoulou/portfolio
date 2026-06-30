# Antibody Sequence ML And Existing-Record Prioritization

## 1. Overview

Built a public-data antibody sequence ML workflow for retrospective benchmarking, unsupervised sequence-space analysis, OAS background controls, and existing-record prioritization. The project centers on validation quality, label semantics, calibration, representation checks, model selection, and record triage.

Portfolio role: primary pharma-facing antibody and protein-informatics case study.

## 2. Scientific And Technical Problem

Public antibody datasets contain heterogeneous assay labels, target annotations, sequence completeness, and source metadata. The technical question was whether sequence-based baseline models, antibody-specific representations, and validation controls could support a reproducible retrospective benchmark without overstating prospective biological utility.

## 3. Dataset Or System

Project sources: the standalone antibody repository and copied public artifacts in `artifacts/`.

- CoV-AbDab-derived public-data workflow.
- Strict labeled dataset: 5,573 records in `reports/metrics/core_dataset_audit.json`.
- Broader prepared records: 11,748 records in `reports/metrics/core_dataset_audit.json`.
- Annotated paired subset: 5,092 paired CDR-annotated candidates in `reports/metrics/core_dataset_audit.json`.
- OAS retrieval and existing-record prioritization used unknown-target natural antibody background records.
- Unsupervised landscape analysis used cached pair embeddings for the strict labeled records, with labels overlaid after clustering.

The portfolio layer reports aggregate metrics and public-safe identifiers.

## 4. Methods

- Sequence cleaning and prepared-table generation from public CoV-AbDab-derived records.
- Character k-mer TF-IDF baselines with logistic regression.
- Grouped validation using available grouping columns where meaningful.
- Source-holdout validation and source-robust model selection.
- Calibration and threshold analysis for high-confidence review cutoffs.
- CDR and region annotation for paired records.
- Antibody embedding and pretrained antibody model benchmarks, including AbLang2-style embeddings, IgBert fine-tuning, five-seed checks, and matched k-mer comparisons.
- Unsupervised antibody sequence-landscape analysis from cached pair embeddings, with label/source metadata used after clustering for interpretation.
- OAS background retrieval as a separate background-retrieval analysis with explicit label semantics.
- Diversity-filtered OAS existing-record shortlist from unknown-target natural antibody background records.

## 5. Validation Strategy

- Primary validation used grouped evaluation where the group feature was meaningful.
- Random-split results were retained as a baseline; grouped and source-holdout results carry the main interpretation.
- Matched CDR feature comparisons were used to compare whole-pair versus region-local k-mer features on the same paired subset.
- Source-holdout validation was used as a skeptical control for source and study effects.
- Source-robust model selection compared conservative k-mer variants and selected `whole_pair_kmer`.
- Pretrained alternatives were retained as benchmark evidence because they did not consistently improve both ROC-AUC and PR-AUC over the matched k-mer baseline.
- Unsupervised clustering did not use neutralisation labels; labels were overlaid after clustering to inspect enrichment and possible representation artifacts.
- OAS retrieval was analyzed as a separate unknown-target background enrichment task.

## 6. Key Results

- Final selected model: `whole_pair_kmer`, a compact whole-pair k-mer TF-IDF logistic-regression scorer.
- V-gene grouped whole-pair k-mer validation: ROC-AUC 0.7800 and PR-AUC 0.8233.
- Source-robust weighted leave-source-out validation: ROC-AUC 0.6095 and PR-AUC 0.6363.
- Threshold 0.7 gave precision 0.8266, recall 0.3062, and coverage 0.3051 for high-confidence review.
- Final consistency audit: PASS, with zero missing expected packaging artifacts.
- Lightweight integrity checks passed.
- Pretrained antibody model outputs are retained as benchmark comparisons rather than the primary scorer.
- Unsupervised sequence-landscape analysis produced 9 clusters from cached pair embeddings, with labels used only after clustering for enrichment summaries.
- Broader CoV-AbDab review prioritization produced a 23-record shortlist from missing/conflict-label records.
- OAS existing-record scoring evaluated 17,882 unknown-target natural antibody rows and produced a top-25 diverse expert-review shortlist.

## 7. Figures

- `docs/assets/figures/antibody_project_workflow.png`: workflow from public antibody records to validation and review outputs.
- `docs/assets/figures/antibody_broad_model_benchmark.png`: broad model benchmark.
- `docs/assets/figures/antibody_kmer_vs_igbert_followup.png`: k-mer versus IgBert follow-up checks.
- `docs/assets/figures/antibody_selected_model_robustness.png`: selected model robustness and threshold behavior.
- `docs/assets/figures/antibody_unsupervised_landscape.png`: unsupervised sequence-space landscape from cached pair embeddings.
- `docs/assets/figures/antibody_oas_existing_record_score_distribution.png`: OAS existing-record score distribution.
- `docs/assets/figures/antibody_oas_existing_record_similarity_vs_score.png`: OAS similarity versus score.
- `docs/assets/figures/antibody_oas_existing_record_diversity_map.png`: OAS shortlist diversity map.
- Source project figures include benchmark and prioritization outputs under `reports/figures/`.

## 8. Interpretation Context

- Public antibody labels combine heterogeneous assays, sources, and target annotations.
- Grouped and source-holdout validation are central to interpreting model behavior across sources.
- OAS records are unknown-target natural antibody background; retrieval metrics measure background enrichment and domain separation.
- Model scores are used as prioritization signals for reviewing existing public records.

## 9. Reproducibility

Public-safe reproduction in this portfolio is limited to a small cached-report path.

- Summary metrics: `artifacts/reports/metrics/summary.json`.
- Final project report: `artifacts/reports/final_project_report.md`.
- Model registry: `artifacts/reports/model_registry.md`.
- OAS shortlist report: `artifacts/reports/oas_existing_record_shortlist_report.md`.
- Unsupervised landscape metrics: `artifacts/reports/metrics/unsupervised_antibody_landscape_metrics.json`.
- Unsupervised landscape report: `artifacts/reports/unsupervised_antibody_landscape_report.md`.
- Repo: <https://github.com/eva-mitropoulou/antibody-prioritization>.
- Final report: `artifacts/reports/final_report.md`.
- Data card: `artifacts/docs/DATA_CARD.md`.
- Model card: `artifacts/docs/MODEL_CARD.md`.
- Artifact map: `artifacts/reports/final_artifact_map.md`.
- Notebook: `notebooks/01_antibody_sequence_ml_workflow.ipynb`.
- Small command: `make reproduce-small` from `artifacts/`.

## 10. Technical Focus

- Public biological-sequence ML benchmark construction.
- Awareness of leakage, grouping, source and study effects, label semantics, calibration, and benchmark interpretation.
- Practical sequence-feature engineering with k-mer, CDR-local, embedding, pretrained-model, and unsupervised sequence-landscape comparisons.
- Communication around validation, prioritization, and benchmark interpretation.
