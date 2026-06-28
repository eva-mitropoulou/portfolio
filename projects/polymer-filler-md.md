# Polymer-Filler MD And Flame-Retardant Molecular Modeling

## 1. Overview

Built and analyzed molecular simulation workflows for polypropylene/brucite filler interfaces and related flame-retardant molecular modeling assets. The public portfolio focuses on reproducible interface analysis, contact summaries, interaction-energy summaries, and force-field-aware interpretation.

## 2. Scientific / Technical Problem

Mineral fillers can alter polymer compatibility and flame-retardant material behavior, but the molecular role of surface treatment must be interpreted carefully. The modeling question was how bare versus surface-coated brucite interfaces change direct polymer-filler contact and interaction patterns.

## 3. Dataset Or System

Evidence source: `Computational-Chemistry/MD/GROMACS/pp_melt_martini` and curated `polymer-md` assets.

- Polypropylene/brucite interface simulations.
- Coated and uncoated filler-surface models.
- Contact-count summary tables.
- Interaction-energy summary tables.
- Density/profile and visual-check artifacts.
- Related DFT and conformer assets for flame-retardant candidate analysis.

## 4. Methods

- GROMACS-based molecular dynamics setup and analysis.
- Atomistic interface-target extraction where available.
- Coarse-grained and calibration workflows where available.
- Contact counts using distance thresholds around brucite and coating groups.
- Short-range interaction-energy summaries.
- Density/profile checks and visual inspection figures.
- SLURM and shell workflow scripts for HPC execution and restart management.

## 5. Validation Strategy

- Compared coated versus uncoated contact and energy summaries.
- Used density/profile outputs and visual checks as simulation sanity checks.
- Treated results as model-supported interpretation, not standalone experimental proof.
- Kept force-field and parameterization limits explicit.

## 6. Key Results

- Available contact and interaction-energy summaries support the interpretation that surface coating reduced direct PP-brucite contact.
- Coated analyses show substantial PP interaction with the stearic-acid layer, shifting the interface away from direct PP-brucite contact.
- These outputs support a compatibility interpretation for surface treatment, within force-field and model limitations.

## 7. Figures

- `docs/assets/figures/polymer_contact_energy_summary.svg`: public-safe contact and interaction-energy summary generated from committed aggregate tables.
- Existing portfolio figures include temperature, density, pressure, and volume traces under `polymer-md/figures/`.

## 8. Limitations

- Force-field-dependent computational model.
- Not standalone property prediction.
- Does not replace experimental characterization.
- Coating and interface conclusions depend on model setup, parameter choices, and sampling.
- Connected to experimental interpretation rather than a final screening platform.

## 9. Reproducibility

- Summary metrics: `polymer-md/reports/metrics/summary.json`.
- Final report: `polymer-md/reports/final_report.md`.
- Small command: `make reproduce-small` from `polymer-md/`.
- Recruiter notebook: `notebooks/03_polymer_filler_md_analysis.ipynb`.
- Full MD reproduction may require GROMACS, force-field files, trajectories, large storage, and HPC resources.

## 10. What This Demonstrates

- Ability to connect molecular simulation setup, analysis scripts, and scientific interpretation.
- Practical MD analysis across contacts, energies, density/profile checks, and workflow infrastructure.
- Materials-facing communication discipline around what simulations can and cannot support.
