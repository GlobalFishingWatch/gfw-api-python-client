"""Global Fishing Watch (GFW) API Python Client - Datasets API Resource.

This module provides the `DatasetResource` class for interacting with the GFW
Datasets API. It offers functionalities to access various datasets,
including SAR fixed infrastructure data.

For detailed information, see the official documentation:

`Datasets API Documentation <https://globalfishingwatch.org/our-apis/documentation#datasets-api>`_
"""

from gfwapiclient.resources.datasets.resources import DatasetResource


__all__ = ["DatasetResource"]
