"""Global Fishing Watch (GFW) API Python Client - Reference Data API Resource.

This module provides the base resource for accessing static reference data from the
Global Fishing Watch (GFW) API. It includes functionality for retrieving various types
of reference information, such as regions, and other contextual data.

For detailed information about the Reference Data API, please refer to the official
Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation#reference-data

See: https://globalfishingwatch.org/our-apis/documentation#regions

For more details on the Reference Data data caveats, please refer to the official
Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation#exclusive-economic-zone-boundaries-definition

See: https://globalfishingwatch.org/our-apis/documentation#marine-protected-area-boundaries-definition

See: https://globalfishingwatch.org/our-apis/documentation#what-does-it-mean-if-an-event-is-within-a-specific-geographic-area-such-as-an-eez-mpa-or-rfmo

See: https://globalfishingwatch.org/our-apis/documentation#how-does-gfw-calculate-that-an-event-has-a-publicly-listed-authorization

See: https://globalfishingwatch.org/our-apis/documentation#exclusive-economic-zone-boundaries-definitions

See: https://globalfishingwatch.org/our-apis/documentation#marine-protected-area-boundaries-definition-2
"""

from gfwapiclient.resources.references.resources import ReferenceResource


__all__ = ["ReferenceResource"]
