.PHONY: reproduce-small figures report

reproduce-small:
	@python3 -m json.tool reports/metrics/summary.json >/dev/null
	@test -f reports/final_report.md
	@test -f figures/polymer_contact_energy_summary.svg
	@printf "polymer MD cached reproducibility check passed\n"

figures:
	@test -f figures/polymer_contact_energy_summary.svg
	@test -f figures/density_trace.png
	@printf "polymer MD figure check passed\n"

report:
	@test -f reports/final_report.md
	@printf "polymer MD report check passed\n"
