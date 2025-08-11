"""Global Fishing Watch (GFW) API Python Client - Regions API Models.

This module defines the data models for the Regions API within the GFW API Python Client.
It provides Pydantic models for the response objects related to Exclusive Economic Zones (EEZs),
Marine Protected Areas (MPAs), and Regional Fisheries Management Organizations (RFMOs).

These models are used to deserialize the JSON responses from the GFW API's regions endpoints,
ensuring type safety and data validation.

For more information on the GFW API and its regions endpoints, please refer to the
official Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation#reference-data

See: https://globalfishingwatch.org/our-apis/documentation#regions
"""

from gfwapiclient.resources.references.regions.models.response import (
    EEZRegionItem,
    EEZRegionResult,
    MPARegionItem,
    MPARegionResult,
    RFMORegionItem,
    RFMORegionResult,
)


__all__ = [
    "EEZRegionItem",
    "EEZRegionResult",
    "MPARegionItem",
    "MPARegionResult",
    "RFMORegionItem",
    "RFMORegionResult",
]
