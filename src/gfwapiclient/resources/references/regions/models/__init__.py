"""Global Fishing Watch (GFW) API Python Client - Regions API Models.

This module defines Pydantic data models used for interacting with the
Regions API endpoints. These models are used to represent response data
when retrieving Exclusive Economic Zones (EEZs), Marine Protected Areas (MPAs),
and Regional Fisheries Management Organizations (RFMOs).

These models are used to deserialize the JSON responses from the Regions API endpoints,
ensuring type safety and data validation.

For detailed information about the Regions API endpoints, please refer to the official
Global Fishing Watch API documentation:

See: globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/reference-data

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/reference-data#regions

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/datasets/regions

For more details on the Regions data caveats, please refer to the official
Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#exclusive-economic-zone-boundaries-definition

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#marine-protected-area-boundaries-definition

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#what-does-it-mean-if-an-event-is-within-a-specific-geographic-area-such-as-an-eezmpa-or-rfmo

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#how-does-gfw-calculate-that-an-event-has-a-publicly-listed-authorization

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#insights-api---rfmo-iuu-vessel-list

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#exclusive-economic-zone-boundaries-definitions

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#marine-protected-area-boundaries-definition-1
"""
