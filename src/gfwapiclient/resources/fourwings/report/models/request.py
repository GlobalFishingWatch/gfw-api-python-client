"""Global Fishing Watch (GFW) API Python Client - 4Wings Report API Request Models."""

from enum import Enum
from typing import Any, ClassVar, Final, List, Optional

from pydantic import Field

from gfwapiclient.base.models import BaseModel
from gfwapiclient.http.models import RequestBody, RequestParams


__all__ = ["FourWingsReportBody", "FourWingsReportParams"]


FOURWINGS_REPORT_REQUEST_BODY_VALIDATION_ERROR_MESSAGE: Final[str] = (
    "4Wings report request body validation failed."
)

FOURWINGS_REPORT_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE: Final[str] = (
    "4Wings report request params validation failed."
)

FOURWINGS_REPORT_REQUEST_PARAM_VALIDATION_ERROR_MESSAGE: Final[str] = (
    f"{FOURWINGS_REPORT_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE} `start_date` or `end_date` has an invalid format or missing. Use date objects or strings in 'YYYY-MM-DD' format."
)


class FourWingsReportFormat(str, Enum):
    """4Wings report result format.

    For more details on the 4Wings API supported report result formats, please refer to
    the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#report-url-parameters-for-both-post-and-get-requests

    Attributes:
        JSON (str):
            JSON (JavaScript Object Notation) result format.
    """

    JSON = "JSON"


class FourWingsReportSpatialResolution(str, Enum):
    """4Wings report spatial resolution.

    For more details on the 4Wings API supported report spatial resolutions, please
    refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#report-url-parameters-for-both-post-and-get-requests

    Attributes:
        LOW (str):
            Coarse resolution (~10th degree).

        HIGH (str):
            Fine resolution (~100th degree).
    """

    LOW = "LOW"
    HIGH = "HIGH"


class FourWingsReportGroupBy(str, Enum):
    """4Wings report grouped by criteria.

    For more details on the 4Wings API supported report grouped by criteria, please
    refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#report-url-parameters-for-both-post-and-get-requests

    Attributes:
        VESSEL_ID (str):
            Group by vessel ID.

        FLAG (str):
            Group by vessel flag.

        GEARTYPE (str):
            Group by gear type.

        FLAGANDGEARTYPE (str):
            Group by both flag and gear type.

        MMSI (str):
            Group by MMSI (Maritime Mobile Service Identity).
    """

    VESSEL_ID = "VESSEL_ID"
    FLAG = "FLAG"
    GEARTYPE = "GEARTYPE"
    FLAGANDGEARTYPE = "FLAGANDGEARTYPE"
    MMSI = "MMSI"


class FourWingsReportTemporalResolution(str, Enum):
    """4Wings report temporal resolution.

    For more details on the 4Wings API supported report temporal resolutions, please
    refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#report-url-parameters-for-both-post-and-get-requests

    Attributes:
        HOURLY (str):
            Aggregate by hour.

        DAILY (str):
            Aggregate by day.

        MONTHLY (str):
            Aggregate by month.

        YEARLY (str):
            Aggregate by year.

        ENTIRE (str):
            Aggregate over the entire time period.
    """

    HOURLY = "HOURLY"
    DAILY = "DAILY"
    MONTHLY = "MONTHLY"
    YEARLY = "YEARLY"
    ENTIRE = "ENTIRE"


class FourWingsReportBufferOperation(str, Enum):
    """4Wings report buffer operation.

    For more details on the 4Wings API supported report buffer operations, please
    refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#report-body-only-for-post-request

    Attributes:
        DIFFERENCE (str):
            Compute the difference between geometries.

        DISSOLVE (str):
            Merge geometries into a single shape.
    """

    DIFFERENCE = "DIFFERENCE"
    DISSOLVE = "DISSOLVE"


class FourWingsReportBufferUnit(str, Enum):
    """4Wings report buffer value unit.

    For more details on the 4Wings API supported report buffer value units, please
    refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#report-body-only-for-post-request

    Attributes:
        MILES (str):
            Miles.

        NAUTICALMILES (str):
            Nautical miles.

        KILOMETERS (str):
            Kilometers.

        RADIANS (str):
            Radians.

        DEGREES (str):
            Degrees.
    """

    MILES = "MILES"
    NAUTICALMILES = "NAUTICALMILES"
    KILOMETERS = "KILOMETERS"
    RADIANS = "RADIANS"
    DEGREES = "DEGREES"


class FourWingsReportDataset(str, Enum):
    """4Wings report dataset.

    For more details on the 4Wings API supported datasets, please refer to
    the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#supported-datasets

    See: https://globalfishingwatch.org/our-apis/documentation#api-dataset

    Attributes:
        FISHING_EFFORT_LATEST (str):
            Latest global fishing effort dataset.
            See data caveats: https://globalfishingwatch.org/our-apis/documentation#apparent-fishing-effort

        SAR_PRESENCE_LATEST (str):
            Latest global SAR presence dataset.
            See data caveats: https://globalfishingwatch.org/our-apis/documentation#sar-vessel-detections-data-caveats

        PRESENCE_LATEST (str):
            Latest global vessel presence dataset.
            See data caveats: https://globalfishingwatch.org/our-apis/documentation#ais-vessel-presence-caveats
    """

    FISHING_EFFORT_LATEST = "public-global-fishing-effort:latest"
    SAR_PRESENCE_LATEST = "public-global-sar-presence:latest"
    PRESENCE_LATEST = "public-global-presence:latest"


class FourWingsGeometry(BaseModel):
    """4Wings report GeoJSON-like geometry input.

    Represents a GeoJSON-compatible area of interest used for filtering report data.

    For more details on the 4Wings API supported report geojson/geometries, please
    refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#report-body-only-for-post-request

    Attributes:
        type (str):
            The type of geometry (e.g., "Polygon").

        coordinates (Any):
            Geometry coordinates as a list or nested lists.
    """

    type: str = Field(...)
    coordinates: Any = Field(...)


class FourWingsReportRegion(BaseModel):
    """4Wings report region of interest.

    Represents a predefined region of interest used for filtering report data.

    For more details on the 4Wings API supported report regions, please
    refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#report-body-only-for-post-request

    Attributes:
        dataset (Optional[str]):
            Dataset containing the region.

        id (Optional[str]):
            Region identifier (ID).

        buffer_operation (Optional[FourWingsReportBufferOperation]):
            Operation to apply on buffer geometry.

        buffer_unit (Optional[FourWingsReportBufferUnit]):
            Unit used for buffer distance.

        buffer_value (Optional[str]):
            Value for the buffer distance.
    """

    dataset: Optional[str] = Field(None, alias="dataset")
    id: Optional[str] = Field(None, alias="id")
    buffer_operation: Optional[FourWingsReportBufferOperation] = Field(
        None, alias="bufferOperation"
    )
    buffer_unit: Optional[FourWingsReportBufferUnit] = Field(None, alias="bufferUnit")
    buffer_value: Optional[str] = Field(None, alias="bufferValue")


class FourWingsReportParams(RequestParams):
    """4Wings report request parameters.

    Represents the query parameters for the 4Wings report request.

    For more details on the 4Wings API supported report request parameters, please
    refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#report-url-parameters-for-both-post-and-get-requests

    Attributes:
        spatial_resolution (Optional[FourWingsReportSpatialResolution]):
            Spatial resolution of the report.

        format (Optional[FourWingsReportFormat]):
            Report result format.

        group_by (Optional[FourWingsReportGroupBy]):
            Grouping criteria for the report.

        temporal_resolution (Optional[FourWingsReportTemporalResolution]):
            Temporal resolution of the report.

        datasets (Optional[List[FourWingsReportDataset]]):
            Datasets that will be used to create the report.

        filters (Optional[List[str]]):
            Filters to apply to the report datasets.

        date_range (Optional[str]):
            Start date and end date to filter the data as a comma-separated string
            in `"YYYY-MM-DD,YYYY-MM-DD"` format.

        spatial_aggregation (Optional[bool]):
            Whether to spatially aggregate the report.
    """

    indexed_fields: ClassVar[Optional[List[str]]] = ["datasets", "filters"]

    spatial_resolution: Optional[FourWingsReportSpatialResolution] = Field(
        FourWingsReportSpatialResolution.HIGH, alias="spatial-resolution"
    )
    format: Optional[FourWingsReportFormat] = Field(
        FourWingsReportFormat.JSON, alias="format"
    )
    group_by: Optional[FourWingsReportGroupBy] = Field(None, alias="group-by")
    temporal_resolution: Optional[FourWingsReportTemporalResolution] = Field(
        FourWingsReportTemporalResolution.HOURLY, alias="temporal-resolution"
    )
    datasets: Optional[List[FourWingsReportDataset]] = Field(
        [FourWingsReportDataset.FISHING_EFFORT_LATEST], alias="datasets"
    )
    filters: Optional[List[str]] = Field(None, alias="filters")
    date_range: Optional[str] = Field(None, alias="date-range")
    spatial_aggregation: Optional[bool] = Field(None, alias="spatial-aggregation")


class FourWingsReportBody(RequestBody):
    """4Wings report request body.

    Represents the request body for the 4Wings report request.

    For more details on the 4Wings API supported report request body, please
    refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#report-body-only-for-post-request

    Attributes:
        geojson (Optional[FourWingsGeometry]):
            Custom GeoJSON geometry to filter the report.

        region (Optional[FourWingsReportRegion]):
            Predefined region information to filter the report.
    """

    geojson: Optional[FourWingsGeometry] = Field(None, alias="geojson")
    region: Optional[FourWingsReportRegion] = Field(None, alias="region")
