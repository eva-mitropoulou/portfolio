# Deployment Notes

Audit date: 2026-06-28

## Recommended Deployment

Use GitHub Pages with the static site in `/docs`.

Repository: `eva-mitropoulou/portfolio`  
Branch: `master`  
Pages source path: `/docs`  
Portfolio URL: `https://eva-mitropoulou.github.io/portfolio/`

## Deployment Verification

GitHub Pages was enabled from `/docs` on 2026-06-28 and is now configured to serve from `master` with source path `/docs`.

Verified HTTP 200 URLs:

- `https://eva-mitropoulou.github.io/portfolio/`
- `https://eva-mitropoulou.github.io/portfolio/projects/antibody-sequence-ml.html`
- `https://eva-mitropoulou.github.io/portfolio/projects/egfr-qsar-cadd.html`
- `https://eva-mitropoulou.github.io/portfolio/projects/reaction-yield-ml.html`
- `https://eva-mitropoulou.github.io/portfolio/projects/polymer-filler-md.html`
- `https://eva-mitropoulou.github.io/portfolio/assets/figures/antibody_pipeline.svg`
- `https://eva-mitropoulou.github.io/portfolio/assets/figures/egfr_random_vs_scaffold.png`
- `https://eva-mitropoulou.github.io/portfolio/assets/figures/reaction_yield_model_comparison.png`
- `https://eva-mitropoulou.github.io/portfolio/assets/figures/polymer_contact_energy_summary.svg`

## Why `/docs`

- The site is static HTML/CSS with no build step.
- The portfolio is easy to maintain without a package manager or theme dependency.
- The root repository can continue to hold project folders, reports, notebooks, audit files, and recruiter assets.

## Deployment Steps

1. Push changes to `master`.
2. Keep GitHub Pages source set to branch `master` and folder `/docs`.
3. After deployment, verify:
   - Homepage loads.
   - Project pages load.
   - Figure assets load.
   - GitHub links point to `master`.

## Workflow Decision

No `.github/workflows/pages.yml` is required because the site has no build step. A Pages workflow should be added only if the repository switches to a generated static-site framework or needs automated link checking/build validation.
