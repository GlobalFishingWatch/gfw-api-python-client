"""Global Fishing Watch (GFW) API Python Client - 4Wings API Resource.

This module provides the `FourWingsResource` class, which allows users to interact
with the 4Wings API for generating reports on AIS apparent fishing activity,
AIS vessel presence and SAR vessel detections.

For detailed information about the 4Wings API, refer to the official
Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation#map-visualization-4wings-api

For more details on the 4Wings data caveats, please refer to the official
Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation#apparent-fishing-effort

See: https://globalfishingwatch.org/our-apis/documentation#sar-vessel-detections-data-caveats

See: https://globalfishingwatch.org/our-apis/documentation#ais-vessel-presence-caveats
"""

from gfwapiclient.resources.fourwings.resources import FourWingsResource


__all__ = ["FourWingsResource"]
