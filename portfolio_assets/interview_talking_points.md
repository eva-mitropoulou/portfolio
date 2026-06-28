# Interview Talking Points

## Positioning

Eva is a computational chemist focused on pharma-facing cheminformatics, QSAR and CADD, antibody and protein informatics, reaction informatics, and validation-aware molecular ML. DFT and molecular dynamics provide supporting computational chemistry depth, but the interview narrative should lead with drug-discovery, assay-data, sequence-ML, and synthesis-facing workflows.

## Antibody Sequence ML

- Emphasize public-data benchmarking, label semantics, and existing-record prioritization.
- Explain OAS background records as unknown-target natural antibody background.
- Discuss grouped validation, source-holdout validation, and source-robust model selection as leakage-aware controls.
- Use the final result: whole-pair k-mer TF-IDF logistic regression was the selected broad scorer, with strong grouped validation and modest source-holdout robustness.
- Explain threshold 0.7 as a high-confidence review cutoff for existing records.

## EGFR CADD and QSAR

- Lead with validation discipline: random split versus scaffold split, then assay and document checks.
- Use the supported metric pair: random split Morgan RF RMSE 0.712 and R2 0.719; scaffold split RMSE 0.871 and R2 0.550.
- Explain applicability domain: high-similarity chemistry had MAE 0.513, while low-similarity chemistry had MAE 0.957.
- Mention structure work as retrospective pose recovery: 5UG9 redocking recovered the 8AM co-crystal ligand pose at 0.968 A RMSD.
- Keep the discussion centered on existing-record benchmarking and model-risk triage.

## Reaction Yield ML

- Frame this as a synthesis-facing ML benchmark on public high-throughput reaction data.
- Emphasize reaction-condition features, baseline model comparison, and readable error analysis.
- Connect the project to pharma workflows through reaction screening, route development support, and validation-aware modeling.
- Keep the framing focused on retrospective public-data benchmarking with existing-record ranking.

## Supporting Materials and Simulation Depth

- Explain the system: polypropylene/brucite interface with coated versus uncoated filler surfaces.
- Discuss contact counts, interaction energies, and density checks as complementary simulation outputs.
- Use the safe interpretation: surface coating reduced direct PP-brucite contact and shifted interaction toward the coating layer in the aggregate outputs.
- Be ready to discuss force-field dependence, sampling, and experimental context.

## Questions To Prepare

- How would you extend the EGFR benchmark for prospective validation?
- How would you prevent leakage in antibody sequence benchmarks with public labels?
- What would you need before claiming predictive utility for a QSAR model?
- How would you evaluate a reaction-yield model before using it to guide experimental prioritization?
- Which parts of the antibody workflow are reusable for other public protein sequence datasets?
- How would you validate a force field or coating model for polymer-filler interfaces?
