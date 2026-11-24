"""Global Fishing Watch (GFW) API Python Client - Vessels API Resource.

This module provides the `VesselResource` class, which serves as the primary
interface for interacting with the Global Fishing Watch Vessels API. It
encapsulates the functionality for searching vessels, retrieving vessel
details by ID or IDs, and provides a convenient way to access vessel data.

For detailed information about the Vessels API, please refer to the official
Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/vessels

For more details on the Vessels data caveats, please refer to the official
Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#vessel-api---vessel-identity-information
"""

from gfwapiclient.resources.vessels.resources import VesselResource


__all__ = ["VesselResource"]
