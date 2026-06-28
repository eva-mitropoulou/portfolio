# Model Card

## Intended Use

Retrospective public-data benchmark for reaction-yield modeling and existing-record ranking.

## Not Intended For

- Wet-lab protocol generation
- Operational condition recommendation
- Yield guarantees
- New chemistry generation

## Data And Features

- Dataset: Buchwald-Hartwig HTE yield benchmark (Ahneman/Dreher/Doyle lineage)
- Source mode: public_benchmark
- Feature family: categorical_onehot
- Valid splits: grouped_high_cardinality_component, out_of_additive, out_of_base, out_of_ligand, out_of_substrate, random_split
- Primary selection split: additive-held-out grouped split

## Model

- Selected model: random_forest
- Selection split: grouped_high_cardinality_component

## Metrics

{'mae': 10.7537, 'r2': 0.7262, 'rmse': 14.2371, 'spearman': 0.8597, 'top_10pct_enrichment': 7.3333}

## Limitations

The model uses categorical component labels because component structures are not available in the selected workbook. Interpretability outputs describe model behavior, not chemical causality.
