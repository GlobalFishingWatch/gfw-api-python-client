# Getting Started

We're pleased that you are interested in contributing to `gfw-api-python-client`.

This document is designed to help you set up your development environment for `gfw-api-python-client` and serve as a guide and reference for the development process. If you encounter any issues, please [open an issue](https://github.com/GlobalFishingWatch/gfw-api-python-client/issues) on the issue tracker.

## Get Source Code

To begin working on `gfw-api-python-client`, you'll need to obtain the source code. The source code is available on [GitHub](https://github.com/GlobalFishingWatch/gfw-api-python-client).

```bash
git clone https://github.com/GlobalFishingWatch/gfw-api-python-client.git
cd gfw-api-python-client
```

## Development Environment

`gfw-api-python-client` is a Python package. For development, ensure you have [Python installed](https://realpython.com/installing-python/) on your machine.

It's highly recommended to use a [virtual environment](https://docs.python.org/3/tutorial/venv.html) to manage dependencies.

Here's how to set up your development environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

## Running From Source Tree

To run the `gfw-api-python-client` executable directly from your source tree during development, perform an editable install of `gfw-api-python-client` within your active virtual environment:

```bash
make install
```

This allows you to develop and test your changes without needing to reinstall the package each time.

## Running Tests

`gfw-api-python-client` uses the [pytest](https://pypi.org/project/pytest/) testing framework.

To execute the tests:

```bash
make test
```

## Running Linters and Code Formatting

`gfw-api-python-client` utilizes [pre-commit](https://pypi.org/project/pre-commit/) to manage code linting and formatting. `pre-commit` automates various checks across all files, ensuring a consistent code style throughout the codebase.

To run the linters locally:

```bash
make pre-commit
```

## Building Documentation

The `gfw-api-python-client` documentation is built using [Sphinx](https://pypi.org/project/Sphinx/). The documentation is written in reStructuredText and Markdown.

To build the documentation locally:

```bash
make docs
```

The generated documentation will be located in the `docs/build` directory. Open `docs/build/index.html` in your browser to view it.

To build, watch, and serve the documentation with live reload in your browser:

```bash
make servedocs
```

## What Next?

The following resources will help you navigate and contribute to `gfw-api-python-client`.

### Project Specific Resources

- [GitHub Issues](https://github.com/GlobalFishingWatch/gfw-api-python-client/issues): Find tasks, bug reports, and feature requests.
- [Code of Conduct](https://github.com/GlobalFishingWatch/gfw-api-python-client/blob/develop/CODE_OF_CONDUCT.md): Understand community expectations for respectful collaboration.
- [Contributing Guide](https://github.com/GlobalFishingWatch/gfw-api-python-client/blob/develop/CONTRIBUTING.md): Learn the specific contribution process.

### General Python Development

- [Python Packaging User Guide](https://packaging.python.org/en/latest/): Understand Python package structure and distribution.
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html): Manage project dependencies effectively.
- [Learn about Git](https://docs.github.com/en/get-started/using-git/about-git): Master version control.
- [Learn about GitHub](https://docs.github.com/en/get-started/start-your-journey/hello-world): Familiarize yourself with GitHub's features.
- [Understanding the GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow): Learn the standard collaboration workflow.

### Dependencies

- [httpx](https://www.python-httpx.org/): Modern HTTP client.
- [Pydantic](https://docs.pydantic.dev/latest/): Data validation and settings management.
- [pandas](https://pandas.pydata.org/docs/): Data analysis and manipulation.
- [geopandas](https://geopandas.org/en/stable/): Spatial data analysis.

### Linting and Code Quality

- [Black](https://black.readthedocs.io/en/stable/): Code formatting.
- [isort](https://pycqa.github.io/isort/): Import sorting.
- [MyPy](https://mypy.readthedocs.io/en/stable/): Static type checking.
- [pydocstyle](http://www.pydocstyle.org/en/stable/): Docstring style checking.
- [Ruff](https://docs.astral.sh/ruff/): Extremely fast linter and formatter.
- [codespell](https://github.com/codespell-project/codespell): Typo checking.

### Testing

- [pytest](https://docs.pytest.org/en/stable/): Testing framework.
- [pytest-asyncio](https://pytest-asyncio.readthedocs.io/en/stable/): Asynchronous testing.
- [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/): Test coverage.
- [pytest-mock](https://pytest-mock.readthedocs.io/en/stable/): Mocking utilities.
- [pytest-xdist](https://pytest-xdist.readthedocs.io/en/stable/): Parallel testing.
- [pytest-timeout](https://pypi.org/project/pytest-timeout/): Test timeouts.
- [Coverage.py](https://coverage.readthedocs.io/en/stable/): Coverage measurement.
- [respx](https://lundberg.github.io/respx/): Mocking HTTPX requests.

### Development Workflow

- [commitizen](https://commitizen-tools.github.io/commitizen/): Commit message formatting.
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/): Structured commit messages.
- [pre-commit](https://pre-commit.com/): Git hook manager.
- [pip-audit](https://pypi.org/project/pip-audit/): Dependency vulnerability scanning.

### Build and Deployment

- [build](https://pypa-build.readthedocs.io/en/stable/): Python build system.
- [setuptools](https://setuptools.pypa.io/en/latest/): Package building.
- [twine](https://twine.readthedocs.io/en/stable/): PyPI uploading.
- [GitHub Actions](https://docs.github.com/en/actions): Workflow automation.

### Documentation

- [Sphinx](https://www.sphinx-doc.org/en/master/): Documentation generation.
- [MyST - Markedly Structured Text](https://myst-parser.readthedocs.io/en/latest/): Markdown-like Sphinx syntax.
