"""Global Fishing Watch (GFW) API Python Client - Get Vessels Insights API Models.

This module defines Pydantic data models used for interacting with the
Vessels Insights API endpoint. These models are used to represent request bodies
and response data when retrieving insights data for specified vessels.

For detailed information about the Get Vessels Insights API endpoint, please
refer to the official Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/insights/insights-vessels

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/insights/insights-vessels#request-body

For more details on the Get Vessels Insights data caveats, please refer to the
official Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#insights-api-fishing-detected-in-no-take-mpas

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#insights-api-fishing-event-detected-outside-known-authorized-areas

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#insights-api-coverage

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#insights-api---ais-off-event-aka-gap

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#insights-api---longline-set-events

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#insights-api---rfmo-iuu-vessel-list
"""
