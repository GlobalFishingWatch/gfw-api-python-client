"""Global Fishing Watch (GFW) API Python Client - 4Wings Report API Models.

This module defines the data models used for interacting with the 4Wings Report API.
It includes models for request parameters, request bodies, and response data.
These models are designed to facilitate the creation and parsing of API requests
and responses, ensuring type safety and data validation.

For detailed information about the 4Wings Report API, refer to the official
Global Fishing Watch API documentation:

See: https://globalfishingwatch.org/our-apis/documentation#create-a-report-of-a-specified-region
"""

from gfwapiclient.resources.fourwings.report.models.request import (
    FourWingsReportBody,
    FourWingsReportParams,
)
from gfwapiclient.resources.fourwings.report.models.response import (
    FourWingsReportItem,
    FourWingsReportResult,
)


__all__ = [
    "FourWingsReportBody",
    "FourWingsReportItem",
    "FourWingsReportParams",
    "FourWingsReportResult",
]
