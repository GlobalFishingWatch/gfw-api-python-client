# Global Fishing Watch API Python Client

<!-- start: badges -->

[![ci](https://github.com/GlobalFishingWatch/gfw-api-python-client/actions/workflows/ci.yaml/badge.svg)](https://github.com/GlobalFishingWatch/gfw-api-python-client/actions/workflows/ci.yaml)
[![codecov](https://codecov.io/gh/GlobalFishingWatch/gfw-api-python-client/branch/develop/graph/badge.svg?token=w4R4VZB5RY)](https://codecov.io/gh/GlobalFishingWatch/gfw-api-python-client)
[![pypi - version](https://img.shields.io/pypi/v/gfw-api-python-client)](https://pypi.org/project/gfw-api-python-client/)
[![pypi - python versions](https://img.shields.io/pypi/pyversions/gfw-api-python-client)](https://pypi.org/project/gfw-api-python-client/)
[![license](https://img.shields.io/badge/license-Apache%202-blue)](https://github.com/GlobalFishingWatch/gfw-api-python-client/blob/main/LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15617433.svg)](https://doi.org/10.5281/zenodo.15617433)

[![pre-commit action](https://github.com/GlobalFishingWatch/gfw-api-python-client/actions/workflows/pre-commit.yaml/badge.svg)](https://github.com/GlobalFishingWatch/gfw-api-python-client/actions/workflows/pre-commit.yaml)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![conventional commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)

<!-- end: badges -->

Python package for accessing data from Global Fishing Watch (GFW) APIs.

> **Important:**
> The `gfw-api-python-client` version 1 directly corresponds to Global Fishing Watch API [version 3](https://globalfishingwatch.org/our-apis/documentation#version-3-api). As of April 30th, 2024, API version 3 is the standard. For the most recent API updates, refer to our [API release notes](https://globalfishingwatch.org/our-apis/documentation#api-release-notes).

## Introduction

The `gfw-api-python-client` simplifies access to Global Fishing Watch (GFW) data through [our APIs](https://globalfishingwatch.org/our-apis/documentation#introduction]). It offers straightforward functions for retrieving GFW data. For R users, we also provide the gfwr package; learn more [here](https://globalfishingwatch.github.io/gfwr/)

The Global Fishing Watch Python package currently works with the following APIs:

- [Map Visualization (4Wings API)](https://globalfishingwatch.org/our-apis/documentation#map-visualization-4wings-api): Access AIS apparent fishing effort, AIS vessel presence, and SAR vessel detections between 2017 to ~5 days ago.

- [Vessels API](https://globalfishingwatch.org/our-apis/documentation#vessels-api): Search and retrieve vessel identity based on AIS self-reported data, combined with authorization and registry data from regional and national registries.

- [Events API](https://globalfishingwatch.org/our-apis/documentation#events-api): Retrieve vessel activity events such as encounters, loitering, port visits, fishing events, and AIS off (aka GAPs).

- [Insights API](https://globalfishingwatch.org/our-apis/documentation#insights-api): Access vessel insights that combine AIS activity, vessel identity, and public authorizations. Designed to support risk-based decision-making, operational planning, and due diligence—particularly for assessing risks of IUU (Illegal, Unreported, or Unregulated) fishing.

- [Datasets API](https://globalfishingwatch.org/our-apis/documentation#datasets-api): Retrieve fixed offshore infrastructure detections (e.g., oil platforms, wind farms) from Sentinel-1 and Sentinel-2 satellite imagery, from 2017 up to 3 months ago, classified using deep learning.

- [References API](https://globalfishingwatch.org/our-apis/documentation#regions): Access metadata for EEZs, MPAs, and RFMOs to use in [Events API](https://globalfishingwatch.org/our-apis/documentation#events-api) and [Map Visualization (4Wings API)](https://globalfishingwatch.org/our-apis/documentation#map-visualization-4wings-api) requests and analyses.

> **Note:** See the [Data Caveats](https://globalfishingwatch.org/our-apis/documentation#data-caveat) and [Terms of Use](https://globalfishingwatch.org/our-apis/documentation#terms-of-use) pages in the [GFW API documentation](https://globalfishingwatch.org/our-apis/documentation#introduction) for details on GFW data, API licenses, and rate limits.

## Requirements

- [Python >= 3.11](https://www.python.org/downloads/)
- [pip >= 25](https://pip.pypa.io/en/stable/installation/)
- [venv - Python's built-in virtual environment tool](https://docs.python.org/3/library/venv.html)
- [API access token from the Global Fishing Watch API portal](https://globalfishingwatch.org/our-apis/tokens)

## Installation

You can install `gfw-api-python-client` using `pip`:

```bash
pip install gfw-api-python-client
```

For detailed instructions—including how to set up a virtual environment—refer to the [Installation Guide](https://globalfishingwatch.github.io/gfw-api-python-client/installation.html) in the documentation.

## Usage

After installation, you can start using `gfw-api-python-client` by importing it into your Python code:

```python
import gfwapiclient as gfw

gfw_client = gfw.Client(
    access_token="<PASTE_YOUR_GFW_API_ACCESS_TOKEN_HERE>",
)
```

For step-by-step instructions and examples, see the [Getting Started](https://globalfishingwatch.github.io/gfw-api-python-client/getting-started.html) and [Usage Guides](https://globalfishingwatch.github.io/gfw-api-python-client/usage-guides/index.html) in the documentation.

## Documentation

The full project documentation is available at [globalfishingwatch.github.io/gfw-api-python-client](https://globalfishingwatch.github.io/gfw-api-python-client/index.html).

To get started with the basics, head over to the [Getting Started](https://globalfishingwatch.github.io/gfw-api-python-client/getting-started.html) guide.

For detailed instructions and examples on interacting with the various APIs offered by Global Fishing Watch, explore the [Usage Guides](https://globalfishingwatch.github.io/gfw-api-python-client/usage-guides/index.html) section.

For a complete reference of all available classes, methods, and modules, see the [API Reference](https://globalfishingwatch.github.io/gfw-api-python-client/apidocs/index.html) section.

## Contributing

We welcome and appreciate contributions of all kinds to help improve this package!

Before getting started, please take a moment to review the following guides:

- [Contribution Guide](https://globalfishingwatch.github.io/gfw-api-python-client/development-guides/contributing.html) – Learn how to propose changes, submit pull requests, and understand our development process.

- [Setup Guide](https://globalfishingwatch.github.io/gfw-api-python-client/development-guides/setup.html) – Get your development environment up and running.

- [Git Workflow](https://globalfishingwatch.github.io/gfw-api-python-client/development-guides/git-workflow.html) – Understand our branching strategy and commit conventions.

If you have questions, ideas, or run into issues, feel free to [open an issue](https://github.com/GlobalFishingWatch/gfw-api-python-client/issues) or reach out — we’d love to hear from you!
