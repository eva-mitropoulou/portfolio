# Final Quality-Gate Report

Audit date: 2026-06-28  
Branch: `portfolio-hardening-final`
Overall status: **pass**

## Checks

| # | Gate | Status | Evidence |
|---:|---|---|---|
| 1 | No unsupported claims | Pass | Unsafe-phrase scan passed with explicit allowance for negative contexts such as `must_not_claim`, `unsupported`, and no/not claim boundaries. |
| 2 | No raw private data committed | Pass | Changed-file scan found no added raw-data or large-artifact extensions. |
| 3 | No raw sequence strings shown on public pages | Pass | Long amino-acid-like sequence pattern scan passed across public pages, summaries, reports, and notebooks. |
| 4 | All project links work | Pass | Local HTML internal links and assets passed. After branch push and Pages build, homepage, headline project pages, supporting project pages, and key figure assets returned HTTP 200. |
| 5 | Each headline flagship has page, README, figure, metrics table, limitations, reproducibility | Pass | Verified for antibody sequence ML, EGFR QSAR/CADD, and reaction-yield ML. Polymer-filler MD remains complete as supporting simulation/materials depth. |
| 6 | Homepage can be understood in 30 seconds | Pass | Identity, skills, tools, and three pharma-facing flagship projects are visible, with materials projects moved to a supporting section. |
| 7 | Recruiter can identify domain, tools, and outputs in 60 seconds | Pass | Homepage, skills page, CV page, README, and recruiter summary expose domain, tools, outputs, and limits. |
| 8 | No state-of-the-art claim unless supported | Pass | No state-of-the-art claim is used. |
| 9 | No sequence-design or optimization claims for antibody work | Pass | Antibody outputs are framed as public-data benchmarking and existing-record prioritization. |
| 10 | No deployment claims for baseline ML projects | Pass | EGFR and reaction-yield outputs are framed as retrospective benchmarks and triage workflows. |

## Portfolio Asset Status

| Role | Project | Page | README | Figure | Metrics | Notebook | Reproducibility |
|---|---|---|---|---|---|---|---|
| Headline pharma flagship | EGFR QSAR / CADD | `projects/egfr-qsar-cadd.md` | `egfr-cadd-qsar-admet/README.md` | `docs/assets/figures/egfr_random_vs_scaffold.png` | `egfr-cadd-qsar-admet/reports/metrics/summary.json` | `notebooks/02_egfr_qsar_cadd_benchmark.ipynb` | `make reproduce-small` |
| Headline pharma flagship | Antibody sequence ML | `projects/antibody-sequence-ml.md` | `antibody-sequence-ml/README.md` | `antibody-sequence-ml/figures/antibody_pipeline.svg` | `antibody-sequence-ml/reports/metrics/summary.json` | `notebooks/01_antibody_sequence_ml_workflow.ipynb` | `make reproduce-small` |
| Headline pharma flagship | Reaction yield prediction | `projects/reaction-yield-ml.md` | `reaction-yield-ml/README.md` | `docs/assets/figures/reaction_yield_model_comparison.png` | `reaction-yield-ml/reports/metrics/final_summary.json` | `notebooks/04_reaction_yield_ml_walkthrough.ipynb` | `make reproduce-small` |
| Supporting simulation depth | Polymer-filler MD | `projects/polymer-filler-md.md` | `polymer-md/README.md` | `polymer-md/figures/polymer_contact_energy_summary.svg` | `polymer-md/reports/metrics/summary.json` | `notebooks/03_polymer_filler_md_analysis.ipynb` | `make reproduce-small` |

## Commands Run

- JSON and notebook validity checks with `jq`.
- `make reproduce-small`, `make figures`, and `make report` for each headline/supporting project with a reproducibility target.
- Local HTML internal link and asset check.
- Long amino-acid-like sequence pattern scan.
- Unsafe-phrase context scan.
- Changed-file raw/large artifact extension scan.

## Unsupported Claims Removed Or Marked

- Antibody sequence-design and optimization claims are explicitly excluded.
- EGFR deployment claims are explicitly excluded.
- Clinical-use claims are explicitly excluded.
- Standalone materials property-prediction claims are explicitly excluded.
- Operational reaction-synthesis guidance and generated-chemistry claims are explicitly excluded.
- OAS-as-assayed-control framing is explicitly excluded.

## Recommended Manual Review Items

- Confirm preferred public contact email before final publishing.
- Add a verified LinkedIn URL if Eva wants it public.
- Review `phd-notes` assets before using unpublished thesis/manuscript content publicly.
- Review raw-source license terms before publicly redistributing any raw reaction-yield workbook or full row-level table.
- Run a browser visual review of the GitHub Pages URL after Pages finishes deployment.
