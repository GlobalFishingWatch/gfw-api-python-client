"""Global Fishing Watch (GFW) API Python Client.

This module provides the main entry point for interacting with the
Global Fishing Watch (GFW) API, specifically Version 3. It encapsulates the HTTP client
and resources, providing a unified interface for accessing GFW's data.

For more details on the GFW API and available data, please refer to the official
Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation/

See: https://globalfishingwatch.org/global-fishing-watch-data-availability/

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/key-concepts#api-dataset

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats
"""

from gfwapiclient.client.client import Client


__all__ = ["Client"]
