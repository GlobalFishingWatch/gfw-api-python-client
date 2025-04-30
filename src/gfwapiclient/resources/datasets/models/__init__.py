"""Global Fishing Watch (GFW) API Python Client - Datasets API Models.

This module contains Pydantic models for data structures used with the
Datasets API. These models define the schema for request parameters and
the expected structure of the API responses.

For more details on the Datasets API, please refer to the official
`Global Fishing Watch Datasets API Documentation
<https://globalfishingwatch.org/our-apis/documentation#datasets-api>`_.
"""

from gfwapiclient.resources.datasets.models.response import (
    SARFixedInfrastructureItem,
    SARFixedInfrastructureResult,
)


__all__ = ["SARFixedInfrastructureItem", "SARFixedInfrastructureResult"]
