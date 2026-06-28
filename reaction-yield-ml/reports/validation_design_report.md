# Validation Design Report

## Summary

- Rows available: 3955
- Valid split count: 6
- Valid splits: grouped_high_cardinality_component, out_of_additive, out_of_base, out_of_ligand, out_of_substrate, random_split

## Split Status

- random_split: valid, train=3164, test=791, group_column=None
- out_of_substrate: valid, train=3164, test=791, group_column=component_aryl_halide
- out_of_ligand: valid, train=2966, test=989, group_column=component_ligand
- out_of_base: valid, train=2638, test=1317, group_column=component_base
- out_of_additive: valid, train=3055, test=900, group_column=component_additive
- grouped_high_cardinality_component: valid, train=3055, test=900, group_column=component_additive

## Quality Gates

- random_split_available: True
- grouped_or_out_of_component_available: True
- no_group_overlap_for_grouped_splits: True
- split_sizes_reported: True
- target_distribution_reported: True

Held-out group values are not listed to avoid long component lists.
