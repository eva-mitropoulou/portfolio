# Validation Design Report

## Summary

- Rows available: 3955
- Valid split count: 6
- Valid splits: grouped_high_cardinality_component, out_of_additive, out_of_base, out_of_ligand, out_of_substrate, random_split

## Split Status

- random_split: valid, label=random split, train=3164, test=791, group_column=None
- out_of_substrate: valid, label=aryl-halide-held-out split, train=3164, test=791, group_column=component_aryl_halide
- out_of_ligand: valid, label=ligand-held-out split, train=2966, test=989, group_column=component_ligand
- out_of_base: valid, label=base-held-out split, train=2638, test=1317, group_column=component_base
- out_of_additive: valid, label=additive-held-out split, train=3055, test=900, group_column=component_additive
- grouped_high_cardinality_component: valid, label=additive-held-out grouped split, train=3055, test=900, group_column=component_additive

## Split Equivalence Note

In this dataset, grouped_high_cardinality_component uses component_additive; it is therefore the additive-held-out grouped split and shares the same held-out group design as out_of_additive.

## Quality Gates

- random_split_available: True
- grouped_or_out_of_component_available: True
- no_group_overlap_for_grouped_splits: True
- split_sizes_reported: True
- target_distribution_reported: True

Held-out group values are not listed to avoid long component lists.
