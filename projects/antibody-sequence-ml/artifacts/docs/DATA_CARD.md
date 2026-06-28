# Data Card

## Local Dataset Artifacts

This repository uses local public-record artifacts only. Key files include:

- `data/processed/neutral_sequence_classification_ml.csv`
- `data/processed/neutral_prepared_sequences.csv`
- `data/processed/bioaware_paired_cdr_annotated.csv`
- `data/processed/oas/oas_paired_standardized.csv`
- `data/raw/oas/*.csv.gz`

Reports use aggregate counts, metrics, and public-safe identifiers.

## Strict Labeled Dataset

The strict labeled ML table is `data/processed/neutral_sequence_classification_ml.csv`. It contains 5,573 labeled rows with label balance 0=2,292 and 1=3,281. This table is used for matched broad benchmarking, source-holdout validation, calibration analysis, model selection, and unsupervised sequence-space analysis.

## Broader Record Table

The broader prepared table is `data/processed/neutral_prepared_sequences.csv`. It keeps existing project records beyond the strict supervised subset so prioritization can preserve missing-label and conflict-label records. The broader prioritization output is `reports/broader_existing_record_prioritization_table.csv`.

## Missing And Conflict Labels

Missing-label and conflict-label records are preserved for scoring and review categorization in the broader table. Strict supervised metrics are computed on rows with usable binary labels.

## Source And Study Metadata

Publication/source metadata are heterogeneous. Source fields may combine multiple identifiers, dates, or publication-like metadata. Validation modules sanitize source identifiers before reporting and use leave-source-out or source-grouped splits to measure whether model behavior survives study-level shifts.

## Label Heterogeneity

Neutralisation labels are public record labels from heterogeneous assays. Label definitions, assay conditions, target-region annotations, and sequence completeness vary across records. Metrics are interpreted as retrospective record-classification evidence.

## OAS Background Semantics

OAS paired records are treated as unknown-target natural antibody background. OAS retrieval reports measure whether project records are distinguishable from local natural background under broad and matched controls.

## Record Handling

The workflow uses public records and preserves source sequence fields in the underlying data pipeline. Public reports use aggregate summaries and figures.
