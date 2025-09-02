"""Global Fishing Watch (GFW) API Python Client.

This package provides a Python client for interacting with the Global Fishing Watch (GFW) API,
specifically `version 3 <https://globalfishingwatch.org/our-apis/documentation#version-3-api>`_.
It enables access to publicly available API resources, and facilitating the retrieval of the data.

Features:

- **4Wings**: Access AIS apparent fishing effort, AIS vessel presence, and SAR vessel detections between 2017 to ~5 days ago.

- **Vessels**: Search and retrieve vessel identity based on AIS self-reported data, combined with authorization and registry data from regional and national registries.

- **Events**: Retrieve vessel activity events such as encounters, loitering, port visits, fishing events, and AIS off (aka GAPs).

- **Insights**: Access vessel insights that combine AIS activity, vessel identity, and public authorizations. Designed to support risk-based decision-making, operational planning, and due diligence—particularly for assessing risks of IUU (Illegal, Unreported, or Unregulated) fishing.

- **Datasets**: Retrieve fixed offshore infrastructure detections (e.g., oil platforms, wind farms) from Sentinel-1 and Sentinel-2 satellite imagery, from 2017 up to 3 months ago, classified using deep learning.

- **References**: Access metadata for EEZs, MPAs, and RFMOs to use in `Events API <https://globalfishingwatch.org/our-apis/documentation#events-api>`_ and `Map Visualization (4Wings API) <https://globalfishingwatch.org/our-apis/documentation#map-visualization-4wings-api>`_ requests and analyses.

For comprehensive details, please refer to the official
`Global Fishing Watch API Documentation <https://globalfishingwatch.org/our-apis/documentation#version-3-api>`_.
"""

from gfwapiclient.__version__ import __version__
from gfwapiclient.client import Client
from gfwapiclient.exceptions import (
    AccessTokenError,
    APIError,
    APIStatusError,
    BaseUrlError,
    GFWAPIClientError,
    ModelValidationError,
    ResultItemValidationError,
    ResultValidationError,
)


__all__ = [
    "APIError",
    "APIStatusError",
    "AccessTokenError",
    "BaseUrlError",
    "Client",
    "GFWAPIClientError",
    "ModelValidationError",
    "ResultItemValidationError",
    "ResultValidationError",
    "__version__",
]
