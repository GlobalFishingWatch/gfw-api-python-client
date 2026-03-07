"""Global Fishing Watch (GFW) API Python Client - Insights API Resource.

This module provides the `InsightResource` class, which allows to interact with the
Insights API. It provides methods for retrieving insights data for specified vessels.

For detailed information about the Insights API, please refer to the official
Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation#insights-api

For more details on the Insights data caveats, please refer to the official
Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation#insights-api-fishing-detected-in-no-take-mpas

See: https://globalfishingwatch.org/our-apis/documentation#what-does-it-mean-that-an-api-dataset-is-in-prototype-stage

See: https://globalfishingwatch.org/our-apis/documentation#insights-api-fishing-event-detected-outside-known-authorized-areas

See: https://globalfishingwatch.org/our-apis/documentation#insights-api-coverage

See: https://globalfishingwatch.org/our-apis/documentation#insights-api-rfmo-iuu-vessel-list
"""

from gfwapiclient.resources.insights.resources import InsightResource


__all__ = ["InsightResource"]
