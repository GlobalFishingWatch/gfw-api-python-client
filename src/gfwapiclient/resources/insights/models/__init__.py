"""Global Fishing Watch (GFW) API Python Client - Vessels Insights API Models.

This module contains the Pydantic models used for interacting with the Global Fishing Watch
Vessels Insights API. These models define the structure of the request and response data
for the API endpoints, ensuring type safety and data validation.

For more information on the Vessels Insights API, please refer to the
`Global Fishing Watch API documentation <https://globalfishingwatch.org/our-apis/documentation#insights-api>`_.
"""

from gfwapiclient.resources.insights.models.request import VesselInsightBody
from gfwapiclient.resources.insights.models.response import (
    VesselInsightItem,
    VesselInsightResult,
)


__all__ = ["VesselInsightBody", "VesselInsightItem", "VesselInsightResult"]
