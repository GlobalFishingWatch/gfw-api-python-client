"""Global Fishing Watch (GFW) API Python Client - HTTP Endpoints.

This module provides implementations for various HTTP endpoints used to interact with the GFW API.
It includes classes for handling GET and POST requests, offering a structured approach to
API communication.
"""

from gfwapiclient.http.endpoints.get import GetEndPoint
from gfwapiclient.http.endpoints.post import PostEndPoint


__all__ = ["GetEndPoint", "PostEndPoint"]
