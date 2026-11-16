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
    """Bulk download (report) API dataset.

    For more details about the Bulk Download API supported datasets, dataset versioning,
    and data caveats, refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/bulk-download#supported-bulk-download-api-datasets

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/key-concepts#api-dataset

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/bulk-download

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats

    **Important:**

    We recommend using the `latest` dataset alias to ensure access
    to the latest data improvements. When requesting a dataset using
    the `latest` alias, the API returns the resolved, specific dataset
    version in the `x-datasets` response header. This allows callers
    to identify the exact dataset version used to generate the response.

    For reproducibility, callers may alternatively request a specific
    dataset version using its corresponding version tag.

    Attributes:
        FIXED_INFRASTRUCTURE_DATA_LATEST (str):
            The latest version of the public fixed infrastructure data dataset.
            See data caveats: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#sar-fixed-infrastructure-data-caveats

        FIXED_INFRASTRUCTURE_DATA_V1_1 (str):
            Version 1.1 of the public fixed infrastructure data dataset.
            See data caveats: https://globalfishingwatch.org/our-apis/documentation/docs/v3/general-api-doc/data-caveats#sar-fixed-infrastructure-data-caveats
    """

    FIXED_INFRASTRUCTURE_DATA_LATEST = "public-fixed-infrastructure-data:latest"
    FIXED_INFRASTRUCTURE_DATA_V1_1 = "public-fixed-infrastructure-data:v1.1"


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
