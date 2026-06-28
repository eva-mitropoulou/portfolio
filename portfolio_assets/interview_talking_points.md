# Interview Talking Points

## Positioning

Eva is a computational chemist building reproducible molecular simulation and machine-learning workflows for materials and drug-discovery problems. The strongest pharma-facing framing is a transition into cheminformatics and AI-assisted drug discovery with evidence in DFT, molecular dynamics, RDKit workflows, antibody sequence ML, and leakage-aware QSAR validation.

## Antibody Sequence ML

- Emphasize public-data benchmarking and existing-record prioritization, not therapeutic design.
- Explain why OAS background records are unknown-target background and not true negatives.
- Discuss grouped validation, source-holdout validation, and source-robust model selection as leakage-aware controls.
- Use the final result: whole-pair k-mer TF-IDF logistic regression was the most defensible broad scorer, with strong grouped validation and modest source-holdout robustness.
- Explain threshold 0.7 as a high-confidence review cutoff, not a calibrated prospective neutralisation probability.

## EGFR QSAR / CADD

- Lead with validation discipline: random split versus scaffold split.
- Use the supported metric pair: random split Morgan random forest RMSE 0.712 / R2 0.719; scaffold split RMSE 0.871 / R2 0.550.
- Explain that the performance drop is a good portfolio signal because it shows awareness of scaffold leakage and model risk.
- Keep the claim retrospective and baseline-oriented.

## Polymer-Filler MD

- Explain the system: polypropylene/brucite interface with coated versus uncoated filler surfaces.
- Discuss contact counts, interaction energies, and density/profile checks as complementary simulation evidence.
- Use the safe interpretation: surface coating reduced direct PP-brucite contact and shifted interaction toward the coating layer in the aggregate outputs.
- State limitations before being asked: force-field dependence, sampling, and need for experimental context.

## Questions To Prepare

- How would you redesign the EGFR benchmark for prospective validation?
- How would you prevent leakage in antibody sequence benchmarks with public labels?
- What would you need before claiming predictive utility for a QSAR model?
- How would you validate a force field or coating model for polymer-filler interfaces?
- Which parts of the antibody workflow are reusable for other public protein/sequence datasets?
