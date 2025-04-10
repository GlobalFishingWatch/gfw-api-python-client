"""Global Fishing Watch (GFW) API Python Client - Vessels API Resource.

This module provides the `VesselResource` class, which serves as the primary
interface for interacting with the Global Fishing Watch Vessels API. It
encapsulates the functionality for searching vessels, retrieving vessel
details by ID or IDs, and provides a convenient way to access vessel data.

For detailed information about the Vessels API, please refer to the official
`Global Fishing Watch Vessels API Documentation
<https://globalfishingwatch.org/our-apis/documentation#vessels-api>`_.
"""

from gfwapiclient.resources.vessels.resources import VesselResource


__all__ = ["VesselResource"]
