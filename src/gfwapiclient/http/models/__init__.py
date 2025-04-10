"""Global Fishing Watch (GFW) API Python Client - HTTP Models.

This module contains the core models for handling API request parameters,
request bodies, and response results in a structured manner.
"""

from gfwapiclient.http.models.request import RequestBody, RequestParams
from gfwapiclient.http.models.response import Result, ResultItem


__all__ = ["RequestBody", "RequestParams", "Result", "ResultItem"]
