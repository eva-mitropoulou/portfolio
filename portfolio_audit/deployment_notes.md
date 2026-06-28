# Deployment Notes

Audit date: 2026-06-28

## Recommended Deployment

Use GitHub Pages with the static site in `/docs`.

Repository: `eva-mitropoulou/portfolio`  
Branch: `portfolio-professionalization` during review, then `master` after merge  
Pages source path: `/docs`  
Expected URL after Pages is enabled: `https://eva-mitropoulou.github.io/portfolio/`

## Deployment Verification

GitHub Pages was enabled from `/docs` on `portfolio-professionalization` on 2026-06-28.

Verified HTTP 200 URLs:

- `https://eva-mitropoulou.github.io/portfolio/`
- `https://eva-mitropoulou.github.io/portfolio/projects/antibody-sequence-ml.html`
- `https://eva-mitropoulou.github.io/portfolio/projects/egfr-qsar-cadd.html`
- `https://eva-mitropoulou.github.io/portfolio/projects/polymer-filler-md.html`
- `https://eva-mitropoulou.github.io/portfolio/assets/figures/antibody_pipeline.svg`
- `https://eva-mitropoulou.github.io/portfolio/assets/figures/egfr_random_vs_scaffold.png`
- `https://eva-mitropoulou.github.io/portfolio/assets/figures/polymer_contact_energy_summary.svg`

## Why `/docs`

- The site is static HTML/CSS with no build step.
- The portfolio is easy to maintain without a package manager or theme dependency.
- The root repository can continue to hold project folders, reports, notebooks, audit files, and recruiter assets.

## Deployment Steps

1. Push `portfolio-professionalization`.
2. Enable GitHub Pages for `eva-mitropoulou/portfolio`.
3. Select source branch `portfolio-professionalization` and folder `/docs` for branch preview, or merge to `master` and select `master` with `/docs`.
4. After deployment, verify:
   - Homepage loads.
   - Project pages load.
   - Figure assets load.
   - GitHub links point to the branch or final merged branch.

## Workflow Decision

No `.github/workflows/pages.yml` is required for this branch because the site has no build step. A Pages workflow should be added only if the repository switches to a generated static-site framework or needs automated link checking/build validation.
