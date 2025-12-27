.PHONY: help doctor preflight test lint format security coverage

help:
	@echo "Targets:"
	@echo "  doctor     - sanity checks (no mutation)"
	@echo "  preflight  - full local CI-equivalent run"
	@echo "  test       - pytest"
	@echo "  lint       - ruff static checks"
	@echo "  format     - black formatting check"
	@echo "  security   - pip-audit + bandit"
	@echo "  coverage   - pytest coverage report"

doctor:
	./setup.sh --doctor

test:
	pytest -q

lint:
	ruff check .

format:
	black --check .

security:
	pip-audit
	bandit -r . -x tests

coverage:
	pytest --cov=. --cov-report=term-missing

preflight:
	python3 -m compileall .
	pytest -q
	ruff check .
	black --check .
	pip-audit
