"""Global Fishing Watch (GFW) API Python Client - Regions API Models.

This module defines Pydantic data models used for interacting with the
Regions API endpoints. These models are used to represent response data
when retrieving Exclusive Economic Zones (EEZs), Marine Protected Areas (MPAs),
and Regional Fisheries Management Organizations (RFMOs).

These models are used to deserialize the JSON responses from the Regions API endpoints,
ensuring type safety and data validation.

For detailed information about the Regions API endpoints, please refer to the official
Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation#reference-data

See: https://globalfishingwatch.org/our-apis/documentation#regions

For more details on the Regions data caveats, please refer to the official
Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation#exclusive-economic-zone-boundaries-definition

See: https://globalfishingwatch.org/our-apis/documentation#marine-protected-area-boundaries-definition

See: https://globalfishingwatch.org/our-apis/documentation#what-does-it-mean-if-an-event-is-within-a-specific-geographic-area-such-as-an-eez-mpa-or-rfmo

See: https://globalfishingwatch.org/our-apis/documentation#how-does-gfw-calculate-that-an-event-has-a-publicly-listed-authorization

See: https://globalfishingwatch.org/our-apis/documentation#exclusive-economic-zone-boundaries-definitions

See: https://globalfishingwatch.org/our-apis/documentation#marine-protected-area-boundaries-definition-2
"""
