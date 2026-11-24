"""Global Fishing Watch (GFW) API Python Client - Events API Resource.

This module provides the `EventResource` class for interacting with the GFW Events API.
It retrieves different vessel activities, such as fishing activity, encounters, and port visits,
filtered by various criteria.

For detailed information about the Events API, please refer to the official
Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/events

For more details on the Events data caveats, please refer to the official
Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#how-are-the-events-estimated

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#encounter-event

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#loitering-event

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#port-visit-events

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#apparent-fishing-events

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#ais-off-event-aka-gap
"""

from gfwapiclient.resources.events.resources import EventResource


__all__ = ["EventResource"]
