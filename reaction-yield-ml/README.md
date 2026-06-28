# Reaction Yield Prediction and Synthesis-Aware Triage from Public HTE Data

Retrospective public-data benchmark for reaction-yield modeling on public high-throughput experimentation (HTE) data.

This project demonstrates data curation, reaction-component featurization, leakage-aware validation, model benchmarking, uncertainty-aware prioritization, active-learning simulation, and existing-record ranking over public records.

Safety scope:

- This is not a wet-lab protocol.
- This is not a guarantee of experimental success.
- This project does not generate new chemistry.
- Ranked outputs are retrospective existing-record ranking only.
- Reports avoid operational synthesis instructions, raw row dumps, long chemical lists, and recipe-style output.

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

The small fixture is synthetic and exists only to test code paths. It is not used to claim benchmark performance.

## Project Layout

```text
data/                 raw, processed, external fixtures, and dataset documentation
src/reaction_yield_ml package code
scripts/              executable workflow stages
reports/              metrics, figures, reports, agentic state
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
