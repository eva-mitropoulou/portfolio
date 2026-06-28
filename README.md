# Eva Mitropoulou

Computational chemist working on CADD/QSAR, antibody sequence ML, reaction-yield modeling, molecular simulation, and DFT workflows.

GitHub Pages site: <https://eva-mitropoulou.github.io/portfolio/>

## Main Work

### 1. EGFR CADD/QSAR

Public ChEMBL EGFR IC50 workflow with RDKit descriptors, Morgan fingerprints, scaffold validation, applicability-domain analysis, ADMET-style triage, and a redocking audit.

- Repo: <https://github.com/eva-mitropoulou/egfr-cadd-qsar-admet>
- Site page: `docs/projects/egfr-qsar-cadd.html`
- Project folder: `projects/egfr-cadd-qsar/`
- Notebook: `projects/egfr-cadd-qsar/notebooks/02_egfr_qsar_cadd_benchmark.ipynb`
- Selected results: 10,593 model-ready molecules; scaffold split R2 0.550; 5UG9 redocking RMSD 0.968 A.

### 2. Antibody Sequence ML

Public antibody sequence-record workflow with k-mer baselines, CDR/region analysis, source-holdout validation, OAS background retrieval, and existing-record prioritization.

- Repo: <https://github.com/eva-mitropoulou/antibody-prioritization>
- Site page: `docs/projects/antibody-sequence-ml.html`
- Project folder: `projects/antibody-sequence-ml/`
- Notebook: `projects/antibody-sequence-ml/notebooks/01_antibody_sequence_ml_workflow.ipynb`
- Selected results: 5,573 strict labeled records; grouped ROC-AUC 0.780; grouped PR-AUC 0.823.

### 3. Reaction-Yield Prediction

Public Buchwald-Hartwig HTE benchmark with reaction cleaning, categorical component features, out-of-component validation, uncertainty diagnostics, and active-learning simulation.

- Repo: <https://github.com/eva-mitropoulou/reaction-yield-prediction>
- Site page: `docs/projects/reaction-yield-ml.html`
- Project folder: `projects/reaction-yield-ml/`
- Notebook: `projects/reaction-yield-ml/notebooks/04_reaction_yield_ml_walkthrough.ipynb`
- Selected results: 3,955 public HTE records; additive-held-out R2 0.726; Spearman 0.860.

## Additional Computational Chemistry

### Polymer-Filler MD

GROMACS analysis of polypropylene and brucite interfaces with coated and uncoated filler configurations.

- Site page: `docs/projects/polymer-filler-md.html`
- Project folder: `projects/polymer-filler-md/`
- Notebook: `projects/polymer-filler-md/notebooks/03_polymer_filler_md_analysis.ipynb`
- Selected result: coating shifted interaction toward the surface layer in the aggregate interface analysis.

### DFT, Periodic DFT, And HPC Workflows

- DFT flame-retardant modeling: `projects/dft-flame-retardants/`
- Periodic DFT and Quantum ESPRESSO utilities: `projects/periodic-dft/`
- SLURM and workflow scripts are included with the project folders that use them.

## Methods And Tools

- Cheminformatics: RDKit, ChEMBL, Morgan fingerprints, descriptors, scaffold split, applicability-domain analysis.
- Biologics: CoV-AbDab, OAS, CDR regions, k-mer features, grouped validation, source holdout.
- Reaction informatics: public HTE data, component labels, grouped validation, active-learning simulation.
- Simulation: GROMACS, ORCA, CREST, Quantum ESPRESSO, SLURM.
- ML validation: scikit-learn, ROC-AUC, PR-AUC, RMSE, R2, uncertainty diagnostics.

## Repository Layout

- `docs/`: GitHub Pages website.
- `projects/`: project folders with notes, notebooks, and public artifacts.
- `portfolio_assets/`: CV bullets, summaries, and interview notes.

## Contact

- Email: evangelia.mitr@gmail.com
- GitHub: <https://github.com/eva-mitropoulou>
