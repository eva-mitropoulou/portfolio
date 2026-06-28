# Active-Learning Simulation Report

## Summary

- Workflow: retrospective budgeted selection over existing public records.
- Row count: 3955
- Strategies: random_selection, highest_predicted_yield, uncertainty_sampling, diversity_aware_selection, exploitation_plus_uncertainty, component_diverse_high_score
- Seed count: 5
- Initial seed size: 79
- Batch size: 79
- Rounds: 5
- Random baseline final best-yield mean: 97.9582
- Random baseline approximate 95% CI half-width: 1.7106

## Quality Gates

- random_baseline_included: True
- multiple_seeds_used: True
- no_future_target_leakage: True
- selected_records_existing_only: True
- limitations_stated: True

## Safety Scope

This is an active-learning simulation over existing dataset records. It is not lab automation and does not provide instructions to run reactions.

## Limitations

- Retrospective active-learning simulation over existing public records only.
- The simulation does not instruct anyone to run reactions.
- Candidate component labels are known as public records; target yields are revealed only after simulated acquisition.
