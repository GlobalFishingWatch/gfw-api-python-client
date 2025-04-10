"""Global Fishing Watch (GFW) API Python Client - Reference Data API Resource.

This module provides the base resource for accessing static reference data from the
Global Fishing Watch (GFW) API. It includes functionality for retrieving
various types of reference information, such as regions, and other
contextual data.

For more details on the Reference Data API, please refer to the official
Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation#reference-data
"""

from gfwapiclient.resources.references.resources import ReferenceResource


__all__ = ["ReferenceResource"]
