# Polymer-Filler MD And Flame-Retardant Molecular Modeling

## 1. Overview

Built and analyzed molecular simulation workflows for polypropylene and brucite filler interfaces and related flame-retardant molecular modeling assets. The public portfolio focuses on reproducible interface analysis, contact summaries, interaction-energy summaries, and force-field-aware interpretation.

Portfolio role: supporting computational chemistry depth through molecular simulation and materials modeling.

## 2. Scientific And Technical Problem

Mineral fillers can alter polymer compatibility and flame-retardant material behavior, but the molecular role of surface treatment must be interpreted carefully. The modeling question was how bare versus surface-coated brucite interfaces change direct polymer-filler contact and interaction patterns.

## 3. Dataset Or System

Project source: curated portfolio artifacts in `artifacts/`.

- Polypropylene and brucite interface simulations.
- Coated and uncoated filler-surface models.
- Contact-count summary tables.
- Interaction-energy summary tables.
- Density and visual-check artifacts.
- Related DFT and conformer assets for flame-retardant candidate analysis.

## 4. Methods

- GROMACS-based molecular dynamics setup and analysis.
- Atomistic interface-target extraction where available.
- Coarse-grained and calibration workflows where available.
- Contact counts using distance thresholds around brucite and coating groups.
- Short-range interaction-energy summaries.
- Density checks and visual inspection figures.
- SLURM and shell workflow scripts for HPC execution and restart management.

## 5. Validation Strategy

- Compared coated versus uncoated contact and energy summaries.
- Used density outputs and visual checks as simulation sanity checks.
- Interpreted the outputs alongside force-field, parameterization, and sampling assumptions.

## 6. Key Results

- Available contact and interaction-energy summaries support the interpretation that surface coating reduced direct PP-brucite contact.
- Coated analyses show substantial PP interaction with the stearic-acid layer, shifting the interface away from direct PP-brucite contact.
- These outputs support a compatibility interpretation for surface treatment within the modeled setup.

## 7. Figures

- `docs/assets/figures/polymer_contact_energy_summary.svg`: public-safe contact and interaction-energy summary generated from committed aggregate tables.
- Existing portfolio figures include temperature, density, pressure, and volume traces under `projects/polymer-filler-md/artifacts/figures/`.

## 8. Interpretation Context

- The interpretation comes from force-field-dependent molecular models.
- Coating and interface conclusions depend on model setup, parameter choices, and sampling.
- The outputs support molecular interpretation of polymer-filler compatibility.

## 9. Reproducibility

- Summary metrics: `artifacts/reports/metrics/summary.json`.
- Final report: `artifacts/reports/final_report.md`.
- Small command: `make reproduce-small` from `artifacts/`.
- Recruiter notebook: `notebooks/03_polymer_filler_md_analysis.ipynb`.

## 10. Technical Focus

- Ability to connect molecular simulation setup, analysis scripts, and scientific interpretation.
- Practical MD analysis across contacts, energies, density checks, and workflow infrastructure.
- Materials-facing communication around force-field-aware simulation interpretation.
