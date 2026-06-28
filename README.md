# Eva Mitropoulou

Computational chemist building reproducible molecular simulation and machine-learning workflows for materials and drug-discovery problems.

This public portfolio is organized for computational chemistry, molecular simulation, cheminformatics, QSAR/CADD, and ML validation roles. Claims are tied to committed reports, metrics, notebooks, figures, scripts, or audit files.

## Flagship Projects

### 1. Antibody Sequence ML And Existing-Record Prioritization

Public-data antibody sequence workflow for retrospective benchmarking and existing-record prioritization.

- Methods: CoV-AbDab-derived records, strict/broader dataset handling, grouped and source-holdout validation, whole-pair k-mer TF-IDF, CDR/region analysis, antibody representation benchmarks, calibration/threshold analysis, OAS background retrieval.
- Evidence: `antibody-sequence-ml/reports/metrics/summary.json`, `antibody-sequence-ml/docs/MODEL_CARD.md`, `projects/antibody-sequence-ml.md`, `notebooks/01_antibody_sequence_ml_workflow.ipynb`.
- Key result: selected `whole_pair_kmer` as the most defensible broad scorer, with grouped ROC-AUC 0.780 / PR-AUC 0.823 and source-robust ROC-AUC 0.610 / PR-AUC 0.636.
- Boundary: prioritization and benchmarking only; no therapeutic design, sequence generation, mutation optimization, or prospective validation claim.

### 2. EGFR QSAR / CADD Benchmark

Retrospective EGFR pIC50 baseline from ChEMBL using RDKit descriptors, Morgan fingerprints, and random versus Bemis-Murcko scaffold split validation.

- Methods: ChEMBL curation, RDKit descriptors, Morgan fingerprints, baseline regressors, scaffold split.
- Evidence: `egfr-cadd-qsar-admet/reports/metrics/summary.json`, `projects/egfr-qsar-cadd.md`, `notebooks/02_egfr_qsar_cadd_benchmark.ipynb`.
- Key result: Morgan random forest changed from RMSE 0.712 / R2 0.719 under random split to RMSE 0.871 / R2 0.550 under scaffold split.
- Boundary: retrospective baseline QSAR only; no production-grade prediction or clinical utility claim.

### 3. Polymer-Filler MD And Flame-Retardant Molecular Modeling

GROMACS workflow evidence for polypropylene/brucite interface analysis with coated versus uncoated aggregate contact and interaction-energy summaries.

- Methods: molecular dynamics, contact counts, short-range interaction energies, density/profile checks, force-field-aware interpretation.
- Evidence: `polymer-md/reports/metrics/summary.json`, `projects/polymer-filler-md.md`, `notebooks/03_polymer_filler_md_analysis.ipynb`.
- Interpretation: surface coating reduced direct PP-brucite contact and shifted interaction toward the coating layer in available aggregate MD outputs.
- Boundary: force-field-dependent computational model; not standalone property prediction.

## Technical Stack

- Molecular simulation: GROMACS, force fields, MD analysis, polymer/filler interfaces.
- Quantum chemistry: ORCA, CREST, DFT, conformers, Quantum ESPRESSO utilities.
- Cheminformatics: RDKit, ChEMBL, QSAR, Morgan fingerprints, descriptors, scaffold splits.
- ML validation: grouped validation, scaffold split, ROC-AUC, PR-AUC, RMSE, R2.
- Antibody/protein informatics: CoV-AbDab, OAS, CDR annotation, k-mer features, antibody representation benchmarking.
- Scientific Python: pandas, NumPy, scikit-learn, matplotlib, notebooks, metrics summaries.
- Reproducibility: Git, Linux, SLURM, environments, Makefiles, scripts, reports.

## Selected Outputs

- GitHub Pages site: `docs/`
- Evidence audit: `portfolio_audit/evidence_map.md`
- Recruiter assets: `portfolio_assets/`
- Flagship notebooks: `notebooks/`
- Project case studies: `projects/`

## Contact

- Email: evangelia.mitr@gmail.com
- GitHub: <https://github.com/eva-mitropoulou>
