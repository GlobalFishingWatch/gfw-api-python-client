"""Global Fishing Watch (GFW) API Python Client.

This package provides a Python client for interacting with the Global Fishing Watch
(GFW) API version 3.

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3

It enables access to publicly available API resources, and facilitating the retrieval
of the following APIs data:

- **Map Visualization (4Wings API)**: Access AIS apparent fishing activity,
AIS vessel presence, and SAR vessel detections between 2017 to ~5 days ago.

- **Vessels API**: Search and retrieve vessel identity based on AIS self-reported data,
combined with authorization and registry data from regional and national registries.

- **Events API**: Retrieve vessel activity events such as encounters, loitering, port
visits, fishing events, and AIS off (aka GAPs).

- **Insights API**: Access vessel insights that combine AIS activity, vessel identity,
and public authorizations. Designed to support risk-based decision-making, operational
planning, and due diligence—particularly for assessing risks of
IUU (Illegal, Unreported, or Unregulated) fishing.

- **Datasets API**: Retrieve fixed offshore infrastructure detections (e.g.,
oil platforms, wind farms etc.) from Sentinel-1 and Sentinel-2 satellite imagery,
from 2017 up to 3 months ago, classified using deep learning.

- **Bulk Download API**: Efficiently access and download large-scale datasets to
integrate with big data platforms and tools used by data engineers and researchers.
Unlike our other APIs (4Wings API, Datasets API, etc.), these datasets may include
some **noisy** that are not filtered out.

- **References**: Access metadata for EEZs, MPAs, and RFMOs to use in Events API and
4Wings API requests and analyses.

For more details on the data, API licenses, and rate limits, please refer to
the official Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation/

For more details on the datasets, data caveats and terms of use, please refer to the
official Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/key-concepts#api-dataset

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats

See: https://globalfishingwatch.org/our-apis/documentation/docs/license-rate-limits#terms-of-use
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
