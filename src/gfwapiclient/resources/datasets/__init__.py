"""Global Fishing Watch (GFW) API Python Client - Datasets API Resource.

This module provides the `DatasetResource` class for interacting with the GFW
Datasets API. It offers functionalities to access various datasets,
including SAR fixed infrastructure data.

For detailed information about the Datasets API, please refer to the official
Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/datasets

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/datasets/fixed-infra-context-layer
"""

from gfwapiclient.resources.datasets.resources import DatasetResource


__all__ = ["DatasetResource"]
