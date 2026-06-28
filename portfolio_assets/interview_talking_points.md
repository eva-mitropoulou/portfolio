# Interview Talking Points

## Positioning

Eva is a computational chemist focused on pharma-facing cheminformatics, QSAR and CADD, antibody and protein informatics, reaction informatics, and validation-aware molecular ML. DFT and molecular dynamics provide supporting computational chemistry depth, but the interview narrative should lead with drug-discovery, assay-data, sequence-ML, and synthesis-facing workflows.

## Antibody Sequence ML

- Emphasize public-data benchmarking and existing-record prioritization, not therapeutic design.
- Explain why OAS background records are unknown-target background and not true negatives.
- Discuss grouped validation, source-holdout validation, and source-robust model selection as leakage-aware controls.
- Use the final result: whole-pair k-mer TF-IDF logistic regression was the most defensible broad scorer, with strong grouped validation and modest source-holdout robustness.
- Explain threshold 0.7 as a high-confidence review cutoff, not a calibrated prospective neutralisation probability.

## EGFR QSAR and CADD

- Lead with validation discipline: random split versus scaffold split.
- Use the supported metric pair: random split Morgan random forest RMSE 0.712 and R2 0.719; scaffold split RMSE 0.871 and R2 0.550.
- Explain that the performance drop is a good portfolio signal because it shows awareness of scaffold leakage and model risk.
- Keep the claim retrospective and baseline-oriented.

## Reaction Yield ML

- Frame this as a synthesis-facing ML benchmark on public high-throughput reaction data.
- Emphasize reaction-condition features, baseline model comparison, and readable error analysis rather than production prediction.
- Connect the project to pharma workflows through reaction screening, route development support, and validation-aware modeling.
- Keep the limitation explicit: retrospective public-data benchmark, not an autonomous synthesis optimizer.

## Supporting Materials and Simulation Depth

- Explain the system: polypropylene/brucite interface with coated versus uncoated filler surfaces.
- Discuss contact counts, interaction energies, and density checks as complementary simulation evidence.
- Use the safe interpretation: surface coating reduced direct PP-brucite contact and shifted interaction toward the coating layer in the aggregate outputs.
- State limitations before being asked: force-field dependence, sampling, and need for experimental context.

## Questions To Prepare

- How would you redesign the EGFR benchmark for prospective validation?
- How would you prevent leakage in antibody sequence benchmarks with public labels?
- What would you need before claiming predictive utility for a QSAR model?
- How would you evaluate a reaction-yield model before using it to guide experimental prioritization?
- Which parts of the antibody workflow are reusable for other public protein sequence datasets?
- How would you validate a force field or coating model for polymer-filler interfaces?
