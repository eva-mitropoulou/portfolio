# Initial Hardening Audit: portfolio

- Default branch: `master`
- Hardening branch: `portfolio-hardening-final`
- Start commit: `48da3885e63d`
- Tracked files: 248
- Markdown files: 55
- Metrics JSON files: 0
- Reports: 0
- Tests detected: 7
- CI workflows: 1

## Public-Facing Surfaces

- README, docs, projects, portfolio assets, reports, model/data cards where present.
- Public claim scan hits for manual review: 24
- Raw sequence-like public files found: 0

## Immediate Fixes Needed

- Normalize flagship order to EGFR, antibody, reaction yield across all public pages.
- Replace synthesis-aware wording with component-label reaction-yield wording.
- Add cross-repo consistency audit after fixes.

## Reproducibility Files

- Makefile present: False
- pyproject present: False
- requirements present: False
- environment.yml present: False
- CI workflows: .github/workflows/reaction-yield-ml.yml

## Notes

This audit records file and claim-scan metadata only. It does not include raw rows, raw sequences, or raw molecule tables.
