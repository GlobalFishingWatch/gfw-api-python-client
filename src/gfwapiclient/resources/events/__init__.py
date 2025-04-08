"""Global Fishing Watch (GFW) API Python Client - Events API Resource.

This module provides the `EventResource` class for interacting with the GFW Events API.
It retrieves different vessel activities, such as fishing activity, encounters, and port visits,
filtered by various criteria.

For detailed information, see the official documentation:

-   `Events API Documentation <https://globalfishingwatch.org/our-apis/documentation#introduction-events-api>`_
"""

from gfwapiclient.resources.events.resources import EventResource


__all__ = ["EventResource"]
