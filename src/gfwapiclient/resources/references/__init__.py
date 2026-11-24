"""Global Fishing Watch (GFW) API Python Client - Reference Data API Resource.

This module provides the base resource for accessing static reference data from the
Global Fishing Watch (GFW) API. It includes functionality for retrieving various types
of reference information, such as regions, and other contextual data.

For detailed information about the Reference Data API, please refer to the official
Global Fishing Watch API documentation:

See: globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/reference-data

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/reference-data#regions

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/datasets/regions

For more details on the Reference Data data caveats, please refer to the official
Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#exclusive-economic-zone-boundaries-definition

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#marine-protected-area-boundaries-definition

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#what-does-it-mean-if-an-event-is-within-a-specific-geographic-area-such-as-an-eezmpa-or-rfmo

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#how-does-gfw-calculate-that-an-event-has-a-publicly-listed-authorization

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#insights-api---rfmo-iuu-vessel-list

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#exclusive-economic-zone-boundaries-definitions

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#marine-protected-area-boundaries-definition-1
"""

from gfwapiclient.resources.references.resources import ReferenceResource


__all__ = ["ReferenceResource"]
