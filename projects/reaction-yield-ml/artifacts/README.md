# Reaction Yield Prediction From Public HTE Component Labels

Retrospective public-data benchmark for reaction-yield modeling on public high-throughput experimentation (HTE) data.

This project demonstrates data curation, reaction-component featurization, leakage-aware validation, model benchmarking, uncertainty-aware prioritization, active-learning simulation, and existing-record ranking over public records.

## Project Role

Public HTE component-label yield modeling with grouped validation, uncertainty diagnostics, and existing-record ranking.

## Reproduction

```bash
make setup
make data
make features
make train
make evaluate
make active-learning
make report
make test
```

Small fixture path for fast checks:

```bash
make reproduce-small
```

The portfolio GitHub Actions workflow runs this small fixture path and the test suite on project changes.

The small fixture tests code paths. Benchmark metrics come from committed reports and metric summaries.

## Project Layout

```text
data/                 fixtures, manifests, and dataset documentation
src/reaction_yield_ml package code
scripts/              executable workflow stages
reports/              metrics, figures, and reports
tests/                reproducibility and quality-gate tests
docs/                 model and data cards
notebooks/            walkthrough notebook
```

## Dataset

Primary target dataset: public Buchwald-Hartwig HTE yield data distributed in the IBM rxn_yields repository as `Dreher_and_Doyle_input_data.xlsx`, derived from the Ahneman/Dreher/Doyle high-throughput C-N cross-coupling benchmark.

The workflow records source, citation, access notes, row count, columns, and limitations in:

- `data/DATA_CARD.md`
- `data/dataset_manifest.json`
- `reports/dataset_selection_report.md`
