# Evidence Map

Audit date: 2026-06-28  
Working branch: `master`  
GitHub owner resolved through API: `eva-mitropoulou`

This audit treats committed reports, metrics, notebooks, scripts, figures, and cached processed outputs as evidence. Raw biological sequences, raw CSV rows, DOI/source rows, private data, wet-lab procedural instructions, and heavyweight simulation artifacts are not reproduced here.

## Repository-Level Evidence

| Repository | Type | Main tools | Public-ready | Claims supported | Recommended role |
|---|---|---|---:|---|---|
| `Computational-Chemistry` | Computational chemistry evidence monorepo | Python, GROMACS, Quantum ESPRESSO, ORCA, CREST, RDKit, scikit-learn, SLURM | No | Yes, when tied to reports/metrics/figures/scripts | Private evidence base / archive |
| `portfolio` | Public portfolio and curated project assets | Markdown, Python, static HTML/CSS | Yes | Yes, after this branch adds evidence-backed site layers | Flagship public site |
| `cv-versions` | CV and LinkedIn source materials | Quarto, Markdown, HTML/CSS, Python | No | Useful for wording only; scientific claims need project evidence | Secondary private source |
| `phd-notes` | Private thesis/manuscript notes | Python, RDKit, Markdown, LaTeX, Jupyter | No | Use only after public-clearance review | Private/archive |
| `learning-python` | Python learning exercises | Python, pandas, scikit-learn | No | Supports general Python learning only | Archive |

## Portfolio Evidence

Public positioning note: the headline portfolio should lead with three pharma-facing projects: antibody sequence ML, EGFR QSAR/CADD, and reaction-yield ML. Polymer-filler MD and related DFT/materials work remain public, but they are supporting computational chemistry depth rather than the main recruiter-facing narrative.

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

### Supporting Polymer-Filler MD And Flame-Retardant Molecular Modeling

Evidence status: supported with model/force-field limitations.

Recommended public role: supporting molecular simulation and materials depth.

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

### Reaction Yield Prediction And Synthesis-Aware ML

Evidence status: supported with retrospective public-data boundaries.

Standalone source repo: <https://github.com/eva-mitropoulou/reaction-yield-prediction>.

Verified artifact classes:

- Public Buchwald-Hartwig HTE dataset manifest and data card.
- Aggregate-only data audit and reaction-cleaning reports.
- Component one-hot feature metadata with target-leakage checks.
- Random and out-of-component validation split metrics.
- Mean baseline, regularized linear, random forest, and gradient boosting benchmark metrics.
- Uncertainty calibration report with empirical coverage and uncertainty/error diagnostics.
- Retrospective active-learning simulation over existing records with random baseline and multiple seeds.
- Existing-record ranking report with confidence and domain-warning fields.
- Final project report, model card, data card, tests, figures, and recruiter notebook.

Supported public interpretation:

Built a retrospective public-data HTE reaction-yield modeling workflow with reaction cleaning, categorical component featurization, random and out-of-component validation, uncertainty-aware prioritization, active-learning simulation, and existing-record ranking. The final model was selected on an additive-held-out grouped split, not only random split performance. In this dataset, that split shares the same held-out group design as `out_of_additive`.

Supported metrics:

- Clean public records: 3,955.
- Categorical feature count: 44.
- Selected model: random forest.
- Primary split: additive-held-out grouped split.
- Primary split metrics: MAE 10.754, RMSE 14.237, R2 0.726, Spearman 0.860, top-10% enrichment 7.333.
- Primary split empirical 90% interval coverage: 0.798.

Safety boundaries:

- Retrospective public-data benchmark only.
- Existing-record ranking only.
- No wet-lab protocol or operational synthesis guidance.
- No generated chemistry claim.
- No guarantee of experimental success.
- Component structures are unavailable in the selected workbook, so structure-based featurization is limited.

## Missing Or Review-Required Assets

- Confirm which contact/energy figures from the MD work should be public versus regenerated from sanitized summary tables.
- Review raw-source redistribution terms before committing any raw reaction-yield workbook or full row-level public tables.
- Review `phd-notes` before using any unpublished thesis/manuscript content publicly.
- Decide whether the public `portfolio` repo should include any code copied from private repos or only curated summaries.
- Confirm the preferred contact email before publishing the Contact page.
