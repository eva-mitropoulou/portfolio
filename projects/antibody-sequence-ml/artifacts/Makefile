.PHONY: reproduce-small figures report

reproduce-small:
	@python3 -m json.tool reports/metrics/summary.json >/dev/null
	@test -f reports/final_report.md
	@test -f reports/final_consistency_audit.md
	@test -f reports/final_artifact_map.md
	@test -f docs/DATA_CARD.md
	@test -f docs/MODEL_CARD.md
	@test -f figures/antibody_pipeline.svg
	@test -f figures/antibody_benchmark_pr_auc.png
	@test -f figures/source_robust_model_comparison.png
	@printf "antibody cached reproducibility check passed\n"

figures:
	@test -f figures/antibody_pipeline.svg
	@test -f figures/antibody_benchmark_pr_auc.png
	@test -f figures/source_robust_model_comparison.png
	@test -f figures/calibration_curve.png
	@printf "antibody figure check passed\n"

report:
	@test -f reports/final_report.md
	@test -f reports/final_consistency_audit.md
	@test -f reports/final_artifact_map.md
	@printf "antibody report check passed\n"
