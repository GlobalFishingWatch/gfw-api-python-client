# Global Fishing Watch API Python Client

<!-- start: badges -->
[![ci](https://github.com/GlobalFishingWatch/gfw-api-python-client/actions/workflows/ci.yaml/badge.svg)](https://github.com/GlobalFishingWatch/gfw-api-python-client/actions/workflows/ci.yaml)
[![codecov](https://codecov.io/gh/GlobalFishingWatch/gfw-api-python-client/branch/develop/graph/badge.svg?token=w4R4VZB5RY)](https://codecov.io/gh/GlobalFishingWatch/gfw-api-python-client)
[![license](https://img.shields.io/badge/license-Apache%202-blue)](https://github.com/GlobalFishingWatch/gfw-api-python-client/blob/main/LICENSE)

[![pre-commit action](https://github.com/GlobalFishingWatch/gfw-api-python-client/actions/workflows/pre-commit.yaml/badge.svg)](https://github.com/GlobalFishingWatch/gfw-api-python-client/actions/workflows/pre-commit.yaml)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![conventional commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)
<!-- end: badges -->

Python package for accessing data from Global Fishing Watch (GFW) APIs.

> **Important:**
The `gfw-api-python-client` version 1 directly corresponds to Global Fishing Watch API [version 3](https://globalfishingwatch.org/our-apis/documentation#version-3-api). As of April 30th, 2024, API version 3 is the standard. For the most recent API updates, refer to our [API release notes](https://globalfishingwatch.org/our-apis/documentation#api-release-notes).


The `gfw-api-python-client` simplifies access to Global Fishing Watch (GFW) data through [our APIs](https://globalfishingwatch.org/our-apis/documentation#introduction]). It offers straightforward functions for retrieving GFW data. For R users, we also provide the gfwr package; learn more [here](https://globalfishingwatch.github.io/gfwr/)

The Global Fishing Watch Python package currently works with the following APIs:

- [Vessels API](https://globalfishingwatch.org/our-apis/documentation#vessels-api): vessel search and identity based on AIS self reported data and public registry information

- [Events API](https://globalfishingwatch.org/our-apis/documentation#events-api): encounters, loitering, port visits, AIS-disabling events and fishing events based on AIS data

- [Gridded fishing effort (4Wings API)](https://globalfishingwatch.org/our-apis/documentation#map-visualization-4wings-api): apparent fishing effort based on AIS data and SAR vessel detections.

- [Insights API](https://globalfishingwatch.org/our-apis/documentation#insights-api): The Insights API is a set of indicators or 'vessel insights' that bring together important information on a vessel's known activity (based on AIS), vessel identity information and public authorizations. The objective of the insights is to support risk-based decision-making, operational planning, and other due diligence activities by making it easier for a user to identify vessel characteristics that can indicate an increased potential or opportunity for a vessel to engage in IUU (Illegal, Unreported, or Unregulated) fishing.

> **Note**: See the [Terms of Use](https://globalfishingwatch.org/our-apis/documentation#reference-data) page for GFW APIs for information on our API licenses and rate limits.

## Installation

To start using `gfw-api-python-client`, ensure you have [Python 3.12+](https://realpython.com/installing-python/) installed on your system. It's recommended to install the package in a [virtual environment](https://docs.python.org/3/library/venv.html) using [pip](https://pip.pypa.io/en/stable/).

### Linux/macOS

```bash
python3.12 -m venv .venv
source venv/bin/activate
pip install gfw-api-python-client
```

### Windows

```batch
python3.12 -m venv .venv
venv\Scripts\activate
pip install gfw-api-python-client
```

## Usage

Once installed, you can import and use `gfw-api-python-client` in your code:

```python
import gfwapiclient as gfw

gfw_client = gfw.Client(
    access_token="<PASTE_YOUR_GFW_API_ACCESS_TOKEN_HERE>",
)
```

## Authorization

To use the `gfw-api-python-client`, you need a GFW API access token. You can request this access token from the [GFW API Portal](https://globalfishingwatch.org/our-apis/tokens). Once you have your access token, export it as an environment variable.


### Linux/macOS

```bash
export GFW_API_ACCESS_TOKEN="<PASTE_YOUR_GFW_API_ACCESS_TOKEN_HERE>"
```

### Windows

```powershell
$env:GFW_API_ACCESS_TOKEN = "<PASTE_YOUR_GFW_API_ACCESS_TOKEN_HERE>"
```

## Contributing

We welcome all contributions to improve the package!. Please read our [Contribution Guide](https://github.com/GlobalFishingWatch/gfw-api-python-client/blob/develop/CONTRIBUTING.md) and reach out!.
