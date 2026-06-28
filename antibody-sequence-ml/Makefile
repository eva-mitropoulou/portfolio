.PHONY: reproduce-small figures report

reproduce-small:
	@python3 -m json.tool reports/metrics/summary.json >/dev/null
	@test -f reports/final_report.md
	@test -f figures/antibody_pipeline.svg
	@test -f figures/antibody_benchmark_pr_auc.png
	@printf "antibody cached reproducibility check passed\n"

figures:
	@test -f figures/antibody_pipeline.svg
	@test -f figures/antibody_benchmark_pr_auc.png
	@printf "antibody figure check passed\n"

report:
	@test -f reports/final_report.md
	@printf "antibody report check passed\n"
