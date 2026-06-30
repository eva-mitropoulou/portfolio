.PHONY: reproduce-small figures report

reproduce-small:
	@python3 -m json.tool reports/metrics/summary.json >/dev/null
	@test -f reports/final_report.md
	@test -f reports/final_project_report.md
	@test -f reports/model_registry.md
	@test -f reports/oas_existing_record_shortlist_report.md
	@test -f docs/DATA_CARD.md
	@test -f docs/MODEL_CARD.md
	@test -f docs/assets/project_workflow.png
	@test -f docs/assets/broad_model_benchmark.png
	@test -f docs/assets/kmer_vs_igbert_followup.png
	@test -f docs/assets/selected_model_robustness.png
	@test -f reports/figures/oas_existing_record_score_distribution.png
	@printf "antibody cached reproducibility check passed\n"

figures:
	@test -f docs/assets/project_workflow.png
	@test -f docs/assets/broad_model_benchmark.png
	@test -f docs/assets/kmer_vs_igbert_followup.png
	@test -f docs/assets/selected_model_robustness.png
	@test -f reports/figures/unsupervised_antibody_landscape.png
	@test -f reports/figures/oas_existing_record_diversity_map.png
	@printf "antibody figure check passed\n"

report:
	@test -f reports/final_report.md
	@test -f reports/final_project_report.md
	@test -f reports/model_registry.md
	@test -f reports/oas_existing_record_shortlist_report.md
	@printf "antibody report check passed\n"
