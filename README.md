# Eva Mitropoulou

Computational chemist focused on pharma-facing cheminformatics, QSAR and CADD, antibody and protein informatics, reaction informatics, and validation-aware molecular ML.

This public portfolio is organized for computational drug-discovery, cheminformatics, molecular ML validation, and scientific Python roles. Molecular simulation and DFT projects are included as supporting computational chemistry depth.

## Pharma-Facing Flagship Projects

### 1. EGFR CADD And QSAR Decision Workflow

Retrospective EGFR workflow from ChEMBL IC50 records with RDKit descriptors, Morgan fingerprints, scaffold validation, uncertainty checks, SAR and error analysis, ADMET-style triage, and one redocking check.

- Methods: ChEMBL curation, pIC50 aggregation, RDKit descriptors, Morgan fingerprints, random, scaffold, assay, and document validation, conformal-style uncertainty checks, Tanimoto applicability domain, exploratory custom PyTorch GCN benchmarking, active-learning simulation, and Vina redocking on 5UG9 with ligand 8AM.
- Links: repo <https://github.com/eva-mitropoulou/egfr-cadd-qsar-admet>, case study `projects/egfr-cadd-qsar/README.md`, final report <https://github.com/eva-mitropoulou/egfr-cadd-qsar-admet/blob/main/reports/final_egfr_cadd_qsar_report.md>, notebook `projects/egfr-cadd-qsar/notebooks/02_egfr_qsar_cadd_benchmark.ipynb`.
- Key result: Morgan RF scaffold split RMSE 0.871 and R2 0.550; applicability-domain MAE changed from 0.513 for high-similarity chemistry to 0.957 for low-similarity chemistry; 5UG9 redocking recovered the 8AM co-crystal pose at 0.968 A RMSD.
- What it shows: validation-aware QSAR, applicability-domain analysis, and practical CADD decision support.

### 2. Antibody Sequence ML And Existing-Record Prioritization

Public-data antibody sequence workflow for retrospective benchmarking and existing-record prioritization.

- Methods: CoV-AbDab-derived records, strict and broader dataset handling, grouped validation, source holdout, whole-pair k-mer TF-IDF, CDR analysis, antibody representation benchmarks, calibration analysis, and OAS background retrieval.
- Links: repo <https://github.com/eva-mitropoulou/antibody-prioritization>, case study `projects/antibody-sequence-ml/README.md`, model card <https://github.com/eva-mitropoulou/antibody-prioritization/blob/main/docs/MODEL_CARD.md>, notebook `projects/antibody-sequence-ml/notebooks/01_antibody_sequence_ml_workflow.ipynb`.
- Key result: selected `whole_pair_kmer` as the most defensible broad scorer, with grouped ROC-AUC 0.780 and PR-AUC 0.823, plus source-robust ROC-AUC 0.610 and PR-AUC 0.636.
- What it shows: source-aware antibody sequence benchmarking and public-record prioritization.

### 3. Reaction Yield Prediction From Public HTE Data

Retrospective public-data HTE reaction-yield workflow for reaction cleaning, categorical component-based featurization, leakage-aware validation, uncertainty diagnostics, active-learning simulation, and existing-record ranking.

- Methods: Buchwald-Hartwig public HTE benchmark, component one-hot features, random and out-of-component validation, additive-held-out grouped model selection, mean, linear, and tree baselines, uncertainty diagnostics, and budgeted existing-record selection simulation.
- Links: repo <https://github.com/eva-mitropoulou/reaction-yield-prediction>, case study `projects/reaction-yield-ml/README.md`, final report <https://github.com/eva-mitropoulou/reaction-yield-prediction/blob/main/reports/final_project_report.md>, notebook `projects/reaction-yield-ml/notebooks/04_reaction_yield_ml_walkthrough.ipynb`.
- Key result: selected random forest on the additive-held-out grouped split with MAE 10.754, RMSE 14.237, R2 0.726, Spearman 0.860, and top-10% enrichment 7.333.
- What it shows: reaction-yield modeling from public HTE component labels, with grouped validation and ranking diagnostics.

## Supporting Computational Chemistry Depth

### Polymer-Filler MD And Flame-Retardant Molecular Modeling

GROMACS workflow for polypropylene and brucite interface analysis with coated versus uncoated aggregate contact and interaction-energy summaries.

- Methods: molecular dynamics, contact counts, short-range interaction energies, density checks, and force-field-aware interpretation.
- Links: case study `projects/polymer-filler-md/README.md`, metrics `projects/polymer-filler-md/artifacts/reports/metrics/summary.json`, notebook `projects/polymer-filler-md/notebooks/03_polymer_filler_md_analysis.ipynb`.
- Interpretation: surface coating reduced direct PP-brucite contact and shifted interaction toward the coating layer in available aggregate MD outputs.
- What it shows: molecular simulation depth and careful interpretation of polymer-filler interfaces.

## Technical Stack

- Cheminformatics and reaction informatics: RDKit, ChEMBL, QSAR, public HTE records, Morgan fingerprints, descriptors, scaffold and out-of-component splits.
- ML validation: grouped validation, scaffold split, out-of-component validation, ROC-AUC, PR-AUC, RMSE, R2, and uncertainty calibration.
- Antibody and protein informatics: CoV-AbDab, OAS, CDR annotation, k-mer features, antibody representation benchmarking.
- Scientific Python: pandas, NumPy, scikit-learn, matplotlib, notebooks, metrics summaries.
- Molecular simulation: GROMACS, force fields, MD analysis, polymer-filler interfaces.
- Quantum chemistry: ORCA, CREST, DFT, conformers, Quantum ESPRESSO utilities.
- Reproducibility: Git, Linux, SLURM, environments, Makefiles, scripts, reports.

## Repository Layout

- `docs/`: GitHub Pages website files.
- `projects/`: one folder per project, including case-study text, notebooks, and copied public artifacts where useful.
- `portfolio_assets/`: CV bullets, recruiter summaries, and interview talking points.

## Contact

- Email: evangelia.mitr@gmail.com
- GitHub: <https://github.com/eva-mitropoulou>
