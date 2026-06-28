# CV Bullets: Materials / Molecular Simulation

## Recommended Safe Bullets

| Bullet text | Supporting repository/report | Metric source | Risk level |
|---|---|---|---|
| Analyzed polypropylene/brucite molecular dynamics interfaces using aggregate contact-count and interaction-energy summaries for coated versus uncoated filler surfaces. | `polymer-md/reports/final_report.md` | `polymer-md/reports/metrics/summary.json` | safe |
| Interpreted coated filler simulations as reduced direct PP-brucite contact with interaction shifted toward the coating layer, while stating force-field and sampling limitations. | `projects/polymer-filler-md.md` | `polymer-md/reports/metrics/summary.json` | safe |
| Maintained public-facing GROMACS portfolio artifacts including thermodynamic traces, cached reports, small Makefile checks, and reproducibility notes. | `polymer-md/README.md`, `polymer-md/Makefile` | `polymer-md/reports/metrics/summary.json` | safe |
| Developed ORCA/CREST and periodic Quantum ESPRESSO project assets for flame-retardant and inorganic materials modeling. | `flame-retardants/README.md`, `periodic-dft/README.md` | Artifact inventory in `portfolio_audit/evidence_map.json` | safe |
| Used Linux, Git, SLURM-oriented scripts, and cached analysis outputs to organize molecular simulation and DFT workflows for reviewable scientific reporting. | `portfolio_audit/evidence_map.md` | Repository inventory and project files | safe |

## Needs Review Before Use

| Bullet text | Supporting repository/report | Metric source | Risk level |
|---|---|---|---|
| Linked MD results directly to experimental flame-retardant performance. | Simulation outputs support interpretation, but standalone experimental-performance claims need reviewed thesis/publication evidence. | `portfolio_audit/evidence_map.md` | needs review |

## Excluded Unsupported Claims

| Claim | Reason | Risk level |
|---|---|---|
| Predicted final flame-retardant material performance from simulation alone. | Evidence supports computational interpretation, not standalone property prediction. | unsupported |
| Built a force-field-independent materials screening platform. | Force-field limitations are explicit. | unsupported |
