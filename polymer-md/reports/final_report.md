# Final Report: Polymer-Filler MD And Flame-Retardant Molecular Modeling

## Purpose

Summarize public-safe molecular simulation evidence for polypropylene/brucite interfaces and coated versus uncoated filler-surface analysis.

## Evidence Used

- Contact-count summaries from `aa_interface_targets`.
- Interaction-energy summaries from `aa_interface_targets`.
- Coated-slab calibration summaries from `brucite_slab` analysis folders.
- Existing thermodynamic traces in `polymer-md/figures`.
- Related DFT and periodic DFT portfolio assets.

## Methods

The workflow used GROMACS molecular dynamics, interface target extraction, contact-count analysis, short-range interaction-energy summaries, density/profile checks, and HPC-oriented scripts.

## Key Results

| Aggregate evidence | Value |
|---|---:|
| Uncoated direct PP-BRC contacts within 0.60 nm | 6,827.0 |
| Coated direct PP-BRC contacts within 0.60 nm | 1,676.9 |
| Coated PP-coating/UNK contacts within 0.60 nm | 57,322.8 |
| Uncoated direct PP-BRC LJ energy, kJ/mol | -6,030.6 |
| Coated direct PP-BRC LJ energy, kJ/mol | -1,388.4 |
| Coated PP-coating/UNK LJ energy, kJ/mol | -32,703.9 |

## Interpretation

Surface coating reduced direct PP-brucite contact and shifted interaction toward the coating layer in the available aggregate MD outputs. This supports a molecular interpretation of surface treatment effects on polymer-filler compatibility.

## Limitations

- Force-field-dependent computational model.
- Not standalone property prediction.
- Does not replace experimental characterization.
- Conclusions depend on model setup, parameter choices, and sampling.
