# Existing-Record Ranking Report

## Summary

- Ranking rows: 3955
- Models used for out-of-fold predictions: ridge, random_forest, gradient_boosting
- Cross-validation folds: 5
- Median model agreement standard deviation: 2.9629
- Domain warning count: 0

## Safety Scope

This is a retrospective existing-record ranking of public dataset records. It is not a synthetic recipe recommendation, not a wet-lab protocol, and not a lab-ready condition list.

## Quality Gates

- ranking_contains_existing_records_only: True
- uncertainty_or_confidence_included: True
- domain_warning_included: True
- limitations_included: True
- no_lab_ready_claim: True

## Limitations

- Ranking is based on out-of-fold predictions for existing public records only.
- The table omits component labels to avoid recipe-style public output.
- Scores are decision-support diagnostics for retrospective analysis, not lab-ready conditions.
