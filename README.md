# Eva Mitropoulou

Computational chemist working on CADD/QSAR, antibody sequence ML, reaction-yield modeling, molecular simulation, and DFT workflows.

GitHub Pages site: <https://eva-mitropoulou.github.io/portfolio/>

## Main Work

### 1. EGFR CADD/QSAR

This project builds an EGFR CADD/QSAR workflow using public ChEMBL IC50 records. I curated molecule-level activity data, standardized molecules, generated RDKit descriptor and Morgan fingerprint features, benchmarked QSAR models under multiple validation settings, and used the trained scoring workflow to review existing EGFR inhibitor-like records.

This project tests how much useful modeling can be done from public EGFR IC50 data, while also checking where the model becomes unreliable.

- Repo: <https://github.com/eva-mitropoulou/egfr-cadd-qsar-admet>
- Project folder: `projects/egfr-cadd-qsar/`


### 2. Antibody Sequence ML

This project builds an antibody sequence ML pipeline using public SARS-CoV-2 antibody records. I curated labeled public records, trained ML models to learn patterns associated with neutralising versus non-neutralising sequences, and then used the trained model scoring workflow to prioritize existing OAS antibody records that look most similar to known neutralizing antibodies. The goal is finding existing records that may be worth closer expert review.

- Repo: <https://github.com/eva-mitropoulou/antibody-prioritization>
- Project folder: `projects/antibody-sequence-ml/`

### 3. Reaction-Yield Prediction

This project builds a reaction-yield modeling workflow using public high-throughput experimentation (HTE) data. I curated public Buchwald-Hartwig reaction-yield records, built categorical component-label features, benchmarked simple ML models, and tested whether performance holds when reaction components are held out rather than only shuffling rows.

The goal is to evaluate how far public HTE records can support yield prediction, uncertainty checks, out-of-component validation, active-learning simulation, and existing-record ranking without generating new chemistry or claiming experimental success.

- Repo: <https://github.com/eva-mitropoulou/reaction-yield-prediction>
- Project folder: `projects/reaction-yield-ml/`

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

- **Cheminformatics:** RDKit, ChEMBL, Morgan fingerprints, molecular descriptors, scaffold-aware splitting, applicability-domain analysis.
- **Antibody / biologics ML:** CoV-AbDab, OAS, antibody sequence curation, CDR-region features, k-mer TF-IDF features, AbLang2 and IgBERT representation benchmarks, IgBERT fine-tuning, grouped validation, source/study holdout, calibration and threshold analysis.
- **Molecular simulation and electronic structure:** GROMACS, ORCA, CREST, Quantum ESPRESSO, SLURM-based HPC workflows.
- **Machine learning and evaluation:** scikit-learn, PyTorch, logistic regression, random forest, ROC-AUC, PR-AUC, RMSE, R², calibration and uncertainty diagnostics.

## Repository Layout

- `docs/`: GitHub Pages website.
- `projects/`: project folders with notes, notebooks, and public artifacts.
- `portfolio_assets/`: CV bullets, summaries, and interview notes.

## Contact

- Email: evangelia.mitr@gmail.com
- GitHub: <https://github.com/eva-mitropoulou>
