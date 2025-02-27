"""Global Fishing Watch (GFW) API Python Client.

This package provides a Python client for interacting with the Global Fishing Watch (GFW) API,
specifically `version 3 <https://globalfishingwatch.org/our-apis/documentation#version-3-api>`_.
It enables access to publicly available API resources.

Features:
    - **4Wings**: Enables fast visualization, navigation, and analysis of gridded spatiotemporal datasets.
    - **Vessels**: Provides vessel search and identification details.
    - **Events**: Allows exploration of various vessel activities.
    - **Insights**: Identifies vessel activities, identities, and public authorizations.
    - **Datasets**: Grants access to Synthetic-Aperture Radar (SAR) fixed infrastructure data.
    - **References**: Supplies supporting metadata and reference information.

For more details, visit the official
`Global Fishing Watch API Documentation <https://globalfishingwatch.org/our-apis/documentation#version-3-api>`_.
"""

from gfwapiclient.exceptions import BaseUrlError, GFWError


__all__ = ["BaseUrlError", "GFWError"]
