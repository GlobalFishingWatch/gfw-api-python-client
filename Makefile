.DEFAULT_GOAL := help
sources = src tests

.PHONY: install  ## Install the package, dependencies, and pre-commit for local development
install:
	python -m pip install -U pip
	python -m pip install -e .[lint,test,dev,build,docs,notebooks]
	python -m pre_commit install --install-hooks
	python -m pre_commit install --hook-type commit-msg

.PHONY: format  ## Auto-format python source files
format:
	python -m black $(sources)
	python -m ruff check --fix $(sources)
	python -m ruff format $(sources)

.PHONY: lint  ## Lint python source files
lint:
	python -m ruff check $(sources)
	python -m ruff format --check $(sources)
	python -m black $(sources) --check --diff

.PHONY: codespell  ## Use Codespell to do spellchecking
codespell:
	python -m codespell_lib

.PHONY: typecheck  ## Perform type-checking
typecheck:
	python -m mypy

.PHONY: audit  ## Use pip-audit to scan for known vulnerabilities
audit:
	python -m pip_audit .

.PHONY: test  ## Run all tests and generate a coverage report
test:
	python -m pytest --cov-report term --cov-report=xml --cov=$(sources)

.PHONY: pre-commit  ## Run all pre-commit hooks
pre-commit:
	python -m pre_commit run --all-files

.PHONY: all  ## Run the standard set of checks performed in CI
all: lint codespell typecheck audit test

.PHONY: clean  ## Clear local caches and build artifacts
clean:
	# remove Python file artifacts
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]'`
	rm -f `find . -type f -name '*~'`
	rm -f `find . -type f -name '.*~'`
	rm -rf .cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	# remove build artifacts
	rm -rf build
	rm -rf dist
	rm -rf `find . -name '*.egg-info'`
	rm -rf `find . -name '*.egg'`
	# remove test and coverage artifacts
	rm -rf .tox/
	rm -f .coverage
	rm -f .coverage.*
	rm -rf coverage.*
	rm -rf htmlcov/
	rm -rf .pytest_cache
	rm -rf htmlcov

.PHONY: docs  ## Generate HTML documentation
docs:
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

.PHONY: servedocs  ## Build, watch and serve documentation with live reload in the browser
servedocs:
	$(MAKE) -C docs livehtml

.PHONY: notebooks  ## Run notebooks
notebooks:
	PYTHONHASHSEED=42 python -m jupyterlab

.PHONY: build  ## Build a source distribution and a wheel distribution
build: all clean
	python -m build

.PHONY: publish  ## Publish the distribution to PyPI
publish: build
	python -m twine upload dist/* --verbose

.PHONY: help  ## Display this message
help:
	@grep -E \
		'^.PHONY: .*?## .*$$' $(MAKEFILE_LIST) | \
		sort | \
		awk 'BEGIN {FS = ".PHONY: |## "}; {printf "\033[36m%-19s\033[0m %s\n", $$2, $$3}'
