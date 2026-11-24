"""Global Fishing Watch (GFW) API Python Client - 4Wings API Resource.

This module provides the `FourWingsResource` class, which allows users to interact
with the 4Wings API for generating reports on AIS apparent fishing activity,
AIS vessel presence and SAR vessel detections.

For detailed information about the 4Wings API, refer to the official
Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/4wings

For more details on the 4Wings data caveats, please refer to the official
Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#apparent-fishing-activity

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#sar-vessel-detections-data-caveats

See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#ais-vessel-presence-caveats
"""

from gfwapiclient.resources.fourwings.resources import FourWingsResource


__all__ = ["FourWingsResource"]
