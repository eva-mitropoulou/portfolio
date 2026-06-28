# Model Interpretability Report

## Summary

- Primary split: grouped_high_cardinality_component
- Highest tree-importance component role: component_aryl_halide
- Held-out group column: component_additive
- Held-out split MAE for interpreted model: 10.7433

## Included Analyses

- Permutation importance by component role.
- Tree feature importance aggregated by component role.
- Error analysis by anonymized component group.
- Held-out component failure summary.

## Quality Gates

- permutation_importance_included: True
- component_contribution_summaries_included: True
- feature_importance_for_tree_model_included: True
- error_analysis_by_component_included: True
- held_out_component_failure_cases_summarized: True
- no_causality_overclaim: True

## Limitations

- Importances describe model behavior, not chemical causality.
- One-hot categorical features cannot infer molecular mechanism.
- High-error component groups are anonymized in public reports.
