"""Global Fishing Watch (GFW) API Python Client - Bulk Download API Base Request Models.

This module defines base Pydantic request models, parameters and enumerations for
various Bulk Download API endpoints.
"""

from enum import Enum

from gfwapiclient.base.models import GeoJson, Region


__all__ = [
    "BulkReportDataset",
    "BulkReportFileType",
    "BulkReportFormat",
    "BulkReportGeometry",
    "BulkReportRegion",
]


class BulkReportDataset(str, Enum):
    """Bulk report dataset.

    For more details on the Bulk Download API supported datasets, please refer
    to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#bulk-report-body-only-for-post-request

    See: https://globalfishingwatch.org/our-apis/documentation#supported-bulk-download-api-datasets

    See: https://globalfishingwatch.org/our-apis/documentation#api-dataset

    Attributes:
        FIXED_INFRASTRUCTURE_DATA_LATEST (str):
            Latest public fixed infrastructure data dataset.
            See data caveats: https://globalfishingwatch.org/our-apis/documentation#sar-fixed-infrastructure-data-caveats
    """

    FIXED_INFRASTRUCTURE_DATA_LATEST = "public-fixed-infrastructure-data:latest"


class BulkReportFormat(str, Enum):
    """Bulk report result format.

    For more details on the Bulk Download API supported result formats, please refer
    to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#bulk-report-body-only-for-post-request

    Attributes:
        CSV (str):
            CSV (Comma Separated Values) result format.

        JSON (str):
            JSON (JavaScript Object Notation) result format.
    """

    CSV = "CSV"
    JSON = "JSON"


class BulkReportGeometry(GeoJson):
    """Bulk report GeoJSON-like geometry input.

    Represents a GeoJSON-compatible custom area of interest used for filtering
    bulk report data.

    For more details on the Bulk Download API supported geojson/geometries, please
    refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#bulk-report-body-only-for-post-request
    """

    pass


class BulkReportRegion(Region):
    """Bulk report region of interest.

    Represents a predefined area of interest used for filtering bulk report data.

    For more details on the Bulk Download API supported regions, please refer to the
    official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#bulk-report-body-only-for-post-request

    See: https://globalfishingwatch.org/our-apis/documentation#regions
    """

    pass


class BulkReportFileType(str, Enum):
    """Bulk report file type.

    For more details on the Bulk Download API supported file types, please refer to the
    official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#download-bulk-report-url-parameters-for-get-requests

    Attributes:
        DATA (str):
            Bulk report dataset file.

        README (str):
            Bulk report metadata documentation file.

        GEOM (str):
            Bulk report region geometry (in GeoJSON format) file.
    """

    DATA = "DATA"
    README = "README"
    GEOM = "GEOM"
