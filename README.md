# Eva Mitropoulou

Computational chemist focused on pharma-facing cheminformatics, QSAR and CADD, antibody and protein informatics, reaction informatics, and validation-aware molecular ML.

This public portfolio is organized for computational drug-discovery, cheminformatics, molecular ML validation, and scientific Python roles. Molecular simulation and DFT projects are included as supporting computational chemistry depth. Project pages link to the relevant reports, metrics, notebooks, figures, and scripts.

## Pharma-Facing Flagship Projects

### 1. EGFR CADD And QSAR Decision Workflow

Retrospective EGFR workflow from ChEMBL IC50 records with RDKit descriptors, Morgan fingerprints, scaffold validation, uncertainty checks, SAR and error analysis, ADMET-style triage, and one redocking check.

- Methods: ChEMBL curation, pIC50 aggregation, RDKit descriptors, Morgan fingerprints, random, scaffold, assay, and document validation, conformal-style uncertainty checks, Tanimoto applicability domain, exploratory custom PyTorch GCN benchmarking, active-learning simulation, and Vina redocking on 5UG9 with ligand 8AM.
- Links: repo <https://github.com/eva-mitropoulou/egfr-cadd-qsar-admet>, case study `projects/egfr-qsar-cadd.md`, final report <https://github.com/eva-mitropoulou/egfr-cadd-qsar-admet/blob/main/reports/final_egfr_cadd_qsar_report.md>, notebook `notebooks/02_egfr_qsar_cadd_benchmark.ipynb`.
- Key result: Morgan RF scaffold split RMSE 0.871 and R2 0.550; applicability-domain MAE changed from 0.513 for high-similarity chemistry to 0.957 for low-similarity chemistry; 5UG9 redocking recovered the 8AM co-crystal pose at 0.968 A RMSD.
- Project frame: retrospective existing-record benchmarking and triage for QSAR and CADD decision support.

### 2. Antibody Sequence ML And Existing-Record Prioritization

Public-data antibody sequence workflow for retrospective benchmarking and existing-record prioritization.

- Methods: CoV-AbDab-derived records, strict and broader dataset handling, grouped validation, source holdout, whole-pair k-mer TF-IDF, CDR analysis, antibody representation benchmarks, calibration analysis, and OAS background retrieval.
- Links: repo <https://github.com/eva-mitropoulou/antibody-prioritization>, case study `projects/antibody-sequence-ml.md`, model card <https://github.com/eva-mitropoulou/antibody-prioritization/blob/main/docs/MODEL_CARD.md>, notebook `notebooks/01_antibody_sequence_ml_workflow.ipynb`.
- Key result: selected `whole_pair_kmer` as the most defensible broad scorer, with grouped ROC-AUC 0.780 and PR-AUC 0.823, plus source-robust ROC-AUC 0.610 and PR-AUC 0.636.
- Project frame: public-data benchmarking and existing-record prioritization with source-aware validation.

### 3. Reaction Yield Prediction From Public HTE Data

Retrospective public-data HTE reaction-yield workflow for reaction cleaning, categorical component-based featurization, leakage-aware validation, uncertainty diagnostics, active-learning simulation, and existing-record ranking.

- Methods: Buchwald-Hartwig public HTE benchmark, component one-hot features, random and out-of-component validation, additive-held-out grouped model selection, mean, linear, and tree baselines, uncertainty diagnostics, and budgeted existing-record selection simulation.
- Links: repo <https://github.com/eva-mitropoulou/reaction-yield-prediction>, case study `projects/reaction-yield-ml.md`, final report <https://github.com/eva-mitropoulou/reaction-yield-prediction/blob/main/reports/final_project_report.md>, notebook `notebooks/04_reaction_yield_ml_walkthrough.ipynb`.
- Key result: selected random forest on the additive-held-out grouped split with MAE 10.754, RMSE 14.237, R2 0.726, Spearman 0.860, and top-10% enrichment 7.333.
- Project frame: retrospective public HTE component-label benchmark with existing-record ranking.

## Supporting Computational Chemistry Depth

### Polymer-Filler MD And Flame-Retardant Molecular Modeling

GROMACS workflow for polypropylene and brucite interface analysis with coated versus uncoated aggregate contact and interaction-energy summaries.

- Methods: molecular dynamics, contact counts, short-range interaction energies, density checks, and force-field-aware interpretation.
- Links: case study `projects/polymer-filler-md.md`, metrics `polymer-md/reports/metrics/summary.json`, notebook `notebooks/03_polymer_filler_md_analysis.ipynb`.
- Interpretation: surface coating reduced direct PP-brucite contact and shifted interaction toward the coating layer in available aggregate MD outputs.
- Project frame: force-field-aware molecular simulation analysis for materials interpretation.

## Technical Stack

- Cheminformatics and reaction informatics: RDKit, ChEMBL, QSAR, public HTE records, Morgan fingerprints, descriptors, scaffold and out-of-component splits.
- ML validation: grouped validation, scaffold split, out-of-component validation, ROC-AUC, PR-AUC, RMSE, R2, and uncertainty calibration.
- Antibody and protein informatics: CoV-AbDab, OAS, CDR annotation, k-mer features, antibody representation benchmarking.
- Scientific Python: pandas, NumPy, scikit-learn, matplotlib, notebooks, metrics summaries.
- Molecular simulation: GROMACS, force fields, MD analysis, polymer-filler interfaces.
- Quantum chemistry: ORCA, CREST, DFT, conformers, Quantum ESPRESSO utilities.
- Reproducibility: Git, Linux, SLURM, environments, Makefiles, scripts, reports.

## Selected Outputs

- GitHub Pages site: `docs/`
- Portfolio audit: `portfolio_audit/evidence_map.md`
- Recruiter assets: `portfolio_assets/`
- Flagship notebooks: `notebooks/`
- Project case studies: `projects/`

## Contact

- Email: evangelia.mitr@gmail.com
- GitHub: <https://github.com/eva-mitropoulou>
