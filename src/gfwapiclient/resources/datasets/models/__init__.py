"""Global Fishing Watch (GFW) API Python Client - Datasets API Models.

This module contains Pydantic models for data structures used with the
Datasets API. These models define the schema for request parameters and
the expected structure of the API responses.

For detailed information about the Datasets API, please refer to the official
Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/datasets

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/datasets/fixed-infra-context-layer
"""

from gfwapiclient.resources.datasets.models.response import (
    SARFixedInfrastructureItem,
    SARFixedInfrastructureResult,
)


__all__ = ["SARFixedInfrastructureItem", "SARFixedInfrastructureResult"]
