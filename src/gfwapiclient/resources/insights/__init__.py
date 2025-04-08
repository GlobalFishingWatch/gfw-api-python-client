"""Global Fishing Watch (GFW) API Python Client - Vessels Insights API Resource.

This module provides the `InsightResource` class, which allows you to interact with the
Global Fishing Watch Vessels Insights API. It provides methods for retrieving
insights data for specified vessels.

For more details, please refer to the official
`Global Fishing Watch Insights API Documentation <https://globalfishingwatch.org/our-apis/documentation#insights-api>`_.
"""

from gfwapiclient.resources.insights.resources import InsightResource


__all__ = ["InsightResource"]
