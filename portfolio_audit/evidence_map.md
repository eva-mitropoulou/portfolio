# Evidence Map

Audit date: 2026-06-28  
Working branch: `master`  
GitHub owner resolved through API: `eva-mitropoulou`

This audit treats committed reports, metrics, notebooks, scripts, figures, and cached processed outputs as evidence. Raw biological sequences, raw CSV rows, DOI/source rows, private data, and heavyweight simulation artifacts are not reproduced here.

## Repository-Level Evidence

| Repository | Type | Main tools | Public-ready | Claims supported | Recommended role |
|---|---|---|---:|---|---|
| `Computational-Chemistry` | Computational chemistry evidence monorepo | Python, GROMACS, Quantum ESPRESSO, ORCA, CREST, RDKit, scikit-learn, SLURM | No | Yes, when tied to reports/metrics/figures/scripts | Private evidence base / archive |
| `portfolio` | Public portfolio and curated project assets | Markdown, Python, static HTML/CSS | Yes | Yes, after this branch adds evidence-backed site layers | Flagship public site |
| `cv-versions` | CV and LinkedIn source materials | Quarto, Markdown, HTML/CSS, Python | No | Useful for wording only; scientific claims need project evidence | Secondary private source |
| `phd-notes` | Private thesis/manuscript notes | Python, RDKit, Markdown, LaTeX, Jupyter | No | Use only after public-clearance review | Private/archive |
| `learning-python` | Python learning exercises | Python, pandas, scikit-learn | No | Supports general Python learning only | Archive |

## Flagship Evidence

### Antibody Sequence ML And Existing-Record Prioritization

Evidence status: supported with strict safety framing.

Verified artifact classes:

- Public CoV-AbDab-derived workflow reports and processed-data audit.
- Strict labeled dataset and broader prepared-record dataset counts in `core_dataset_audit.json`.
- Grouped validation and k-mer TF-IDF baseline metrics.
- Source-holdout validation and source-robust model selection.
- Calibration and threshold analysis.
- Matched k-mer/CDR benchmark audit.
- Antibody embedding and language-model benchmark registry.
- CDR/region annotation reports.
- OAS background retrieval reports, with explicit unknown-target-background semantics.
- Diversity-aware existing-record shortlist summary.
- Final data card, model card, artifact map, consistency audit, tests, benchmark figures, and prioritization figures.

Supported public interpretation:

Built a public-data antibody sequence ML workflow for retrospective benchmarking and existing-record prioritization. Whole-pair k-mer TF-IDF logistic regression remained the most defensible broad scorer: strong under V-gene grouped validation and modest under source-holdout validation, exposing source/study effects in public antibody neutralisation labels.

Safety boundaries:

- No therapeutic design claim.
- No generated, mutated, or optimized antibody sequence claim.
- No prospective validation claim.
- No clinical utility claim.
- OAS, where used, is an unknown-target background set, not true negatives.
- Model scores are prioritization signals, not calibrated prospective neutralisation probabilities.

### EGFR QSAR / CADD Benchmark

Evidence status: supported.

Verified artifact classes:

- ChEMBL EGFR IC50 curation scripts.
- RDKit descriptor and Morgan-fingerprint workflows.
- Random split and Bemis-Murcko scaffold split metrics.
- Baseline model reports and figures.
- Applicability-domain summary.
- Recruiter-readable notebooks.

Supported metrics:

- Random split Morgan random forest: RMSE 0.712 / R2 0.719.
- Scaffold split Morgan random forest: RMSE 0.871 / R2 0.550.

Safety boundaries:

- Baseline retrospective QSAR only.
- No production-grade predictor claim.
- No prospective validation claim.
- No clinical utility claim.
- No binding-mechanism claim unless new evidence is added.

### Polymer-Filler MD And Flame-Retardant Molecular Modeling

Evidence status: supported with model/force-field limitations.

Verified artifact classes:

- Polypropylene/brucite interface simulation reports.
- Coated and uncoated filler surface analyses.
- Contact-count and interaction-energy summaries.
- Density/profile outputs and visual checks.
- GROMACS, shell, and Python workflow scripts.
- DFT/conformer and periodic DFT assets for secondary materials positioning.

Supported public interpretation:

Surface coating reduced direct PP-brucite contact and shifted interactions toward the stearic-acid layer in the available analysis tables, supporting the role of surface treatment in polymer-filler compatibility.

Safety boundaries:

- Force-field-dependent computational model.
- Not standalone property prediction.
- Simulation supports interpretation; it does not replace experimental validation.

## Missing Or Review-Required Assets

- Confirm which contact/energy figures from the MD work should be public versus regenerated from sanitized summary tables.
- Review `phd-notes` before using any unpublished thesis/manuscript content publicly.
- Decide whether the public `portfolio` repo should include any code copied from private repos or only curated summaries.
- Confirm the preferred contact email before publishing the Contact page.
