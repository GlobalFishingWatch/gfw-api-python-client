"""Global Fishing Watch (GFW) API Python Client - 4Wings API Resource.

This module provides the `FourWingsResource` class, which allows users to interact
with the 4Wings API for generating reports on fishing activity and SAR vessel
detections.

For detailed information about the 4Wings API, refer to the official
Global Fishing Watch API documentation:

- `4Wings API Documentation <https://globalfishingwatch.org/our-apis/documentation#map-visualization-4wings-api>`_
"""

from gfwapiclient.resources.fourwings.resources import FourWingsResource


__all__ = ["FourWingsResource"]
