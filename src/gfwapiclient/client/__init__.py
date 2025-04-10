"""Global Fishing Watch (GFW) API Python Client.

This module provides the main entry point for interacting with the Global Fishing Watch (GFW) API, specifically Version 3.
It encapsulates the HTTP client and resources, providing a unified interface
for accessing GFW's data.

For more details on the GFW API and available data, please refer to the
official documentation:

See: https://globalfishingwatch.org/our-apis/documentation#introduction

See: https://globalfishingwatch.org/our-apis/documentation#data-available

See: https://globalfishingwatch.org/our-apis/documentation#version-3-api
"""

from gfwapiclient.client.client import Client


__all__ = ["Client"]
