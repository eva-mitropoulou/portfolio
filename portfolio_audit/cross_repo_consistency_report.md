# Cross-Repo Consistency Report

Branch: `portfolio-hardening-final`

## Status

Overall status: pass.

## Hierarchy

Flagship pharma-facing projects are consistent across the portfolio README, homepage, projects page, recruiter summary, and CV assets:

1. EGFR CADD and QSAR Decision Workflow
2. Antibody Sequence ML and Existing-Record Prioritization
3. Reaction Yield Prediction from Public HTE Data

Supporting computational chemistry depth remains visible below the flagships:

- Polymer-Filler MD
- DFT Flame-Retardant Modeling
- Periodic DFT / Quantum ESPRESSO Utilities
- HPC / SLURM Workflow Infrastructure

## Consistency Checks

- Portfolio homepage uses EGFR, antibody, and reaction-yield as top three flagships.
- Polymer MD is supporting depth, not the third flagship.
- Standalone repo links point to the four public project repositories.
- Standalone repo links resolved with `git ls-remote`.
- Antibody paired-region scorer is corrected to region-only compact k-mer.
- Antibody broad scorer remains whole-pair k-mer.
- OAS is framed as unknown-target background rather than assayed controls.
- EGFR final status is `DONE`.
- EGFR uncertainty wording is conformal-style and retrospective.
- EGFR GNN wording is exploratory negative benchmark evidence.
- EGFR redocking wording is retrospective pose-recovery audit.
- Reaction-yield wording emphasizes public HTE component-label modeling.
- Reaction-yield structure-aware work is marked as future extension only.
- Public keyword scans passed for unsupported claim terms.
- Portfolio HTML internal links passed with zero missing internal links.

## Tests And Checks

- Antibody: `make reproduce-small`, `make test`, sequence-publication scan, and `git diff --check` passed.
- EGFR: `make reproduce-small`, `make test`, SMILES-header scan, public-claim scan, and `git diff --check` passed.
- Reaction yield: temp-copy `make reproduce-small` followed by `make test`, public-claim scan, and `git diff --check` passed.
- Portfolio: internal HTML link scan, external repo-link check, project hierarchy scan, keyword scan, and `git diff --check` passed.

## Blockers

None.

## Manual Review

- Apply GitHub repo metadata manually or with another authenticated tool because `gh` is unavailable in this environment.
- Run one browser visual pass on the published GitHub Pages site after merge.
- Confirm Eva's preferred public contact email and optional LinkedIn URL.
