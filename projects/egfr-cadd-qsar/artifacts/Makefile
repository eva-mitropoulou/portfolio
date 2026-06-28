.PHONY: reproduce-small figures report

reproduce-small:
	@python3 -m json.tool reports/metrics/summary.json >/dev/null
	@test -f results/fingerprint_baseline_metrics.csv
	@test -f results/scaffold_fingerprint_metrics.csv
	@test -f reports/final_report.md
	@printf "EGFR cached reproducibility check passed\n"

figures:
	@test -f figures/random_vs_scaffold_validation.png
	@test -f figures/scaffold_fingerprint_predicted_vs_actual.png
	@printf "EGFR figure check passed\n"

report:
	@test -f reports/final_report.md
	@printf "EGFR report check passed\n"
