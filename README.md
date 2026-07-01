# Eva Mitropoulou

Chemistry PhD candidate focused on molecular machine learning for antibody and drug-discovery datasets. Builds end-to-end Python workflows for sequence and bioactivity-data curation, protein language model embeddings, PyTorch/scikit-learn modeling, and validation on grouped or held-out data. Portfolio includes antibody neutralisation benchmarking, antibody-record prioritization, and ChEMBL/RDKit QSAR work, supported by computational chemistry and molecular simulation experience.

website: <https://eva-mitropoulou.github.io/>

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

- Project folder: `projects/polymer-filler-md/`
- Notebook: `projects/polymer-filler-md/notebooks/03_polymer_filler_md_analysis.ipynb`
- Selected result: coating shifted interaction toward the surface layer in the aggregate interface analysis.

### DFT, Periodic DFT, And HPC Workflows

- DFT flame-retardant modeling: `projects/dft-flame-retardants/`
- Periodic DFT and Quantum ESPRESSO utilities: `projects/periodic-dft/`
- SLURM and workflow scripts are included with the project folders that use them.

## Skills

* **Machine Learning & Model Evaluation:** supervised and unsupervised learning, neural networks, model fine-tuning, molecular/biological data curation, benchmark design, model validation, and held-out testing.
* **Protein & Antibody Sequence ML:** antibody/protein sequence ML, protein language models (PLMs), sequence embeddings, and Hugging Face Transformers.
* **Cheminformatics & CADD:** RDKit, ChEMBL, molecular descriptors, molecular fingerprints, QSAR modeling, scaffold-aware validation, drug-likeness/ADMET filtering, limited docking/redocking sanity checks, and compound ranking/prioritization.
* **Scientific Python & Research Computing:** Python, PyTorch, scikit-learn, pandas, NumPy, SciPy, Matplotlib, Linux, Bash, SLURM, Git/GitHub, Docker, and cloud/VM environments.

## Contact

- Email: evangelia.mitr@gmail.com
