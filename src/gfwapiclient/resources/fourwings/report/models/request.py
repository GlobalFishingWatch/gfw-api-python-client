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
    """4Wings report format."""

    JSON = "JSON"


class FourWingsReportSpatialResolution(str, Enum):
    """4Wings report spatial resolution.

    Low means at 10th degree resolution and High means at 100th degree resolution.
    """

    LOW = "LOW"
    HIGH = "HIGH"


class FourWingsReportGroupBy(str, Enum):
    """4Wings report grouped by criteria."""

    VESSEL_ID = "VESSEL_ID"
    FLAG = "FLAG"
    GEARTYPE = "GEARTYPE"
    FLAGANDGEARTYPE = "FLAGANDGEARTYPE"
    MMSI = "MMSI"


class FourWingsReportTemporalResolution(str, Enum):
    """4Wings report temporal resolution."""

    HOURLY = "HOURLY"
    DAILY = "DAILY"
    MONTHLY = "MONTHLY"
    YEARLY = "YEARLY"
    ENTIRE = "ENTIRE"


class FourWingsReportBufferOperation(str, Enum):
    """4Wings report buffer operation."""

    DIFFERENCE = "DIFFERENCE"
    DISSOLVE = "DISSOLVE"


class FourWingsReportBufferUnit(str, Enum):
    """4Wings report buffer value unit."""

    MILES = "MILES"
    NAUTICALMILES = "NAUTICALMILES"
    KILOMETERS = "KILOMETERS"
    RADIANS = "RADIANS"
    DEGREES = "DEGREES"


class FourWingsReportDataset(str, Enum):
    """4Wings report dataset."""

    FISHING_EFFORT_LATEST = "public-global-fishing-effort:latest"
    SAR_PRESENCE_LATEST = "public-global-sar-presence:latest"


class FourWingsGeometry(BaseModel):
    """4Wings report GeoJSON-like geometry input.

    Represents a GeoJSON-like geometry object used to filter the report data.

    Attributes:
        type (str):
            Geometry type (e.g., Polygon).

        coordinates (Any):
            Geometry coordinates.
    """

    type: str = Field(...)
    coordinates: Any = Field(...)


class FourWingsReportRegion(BaseModel):
    """4Wings report region of interest.

    Represents a region of interest used to filter the report data.

    Attributes:
        dataset (Optional[str]):
            Dataset containing the region.

        id (Optional[str]):
            Region ID.

        buffer_operation (Optional[FourWingsReportBufferOperation]):
            Buffer operation.

        buffer_unit (Optional[FourWingsReportBufferUnit]):
            Buffer unit.

        buffer_value (Optional[str]):
            Buffer value.
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

    Attributes:
        spatial_resolution (Optional[FourWingsReportSpatialResolution]):
            Spatial resolution.

        format (Optional[FourWingsReportFormat]):
            Report result format.

        group_by (Optional[FourWingsReportGroupBy]):
            Grouped by criteria.

        temporal_resolution (Optional[FourWingsReportTemporalResolution]):
            Temporal resolution.

        datasets (Optional[List[FourWingsReportDataset]]):
            Datasets that will be used to create the report.

        filters (Optional[List[str]]):
            Filters are applied to the dataset.

        date_range (Optional[str]):
            Start date and end date to filter the data.

        spatial_aggregation (Optional[bool]):
            Whether to spatially aggregate the report.
    """

    indexed_fields: ClassVar[Optional[List[str]]] = ["datasets", "filters"]

    spatial_resolution: Optional[FourWingsReportSpatialResolution] = Field(
        None, alias="spatial-resolution"
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

    Attributes:
        geojson (Optional[FourWingsGeometry]): Geometry to filter the data.
        region (Optional[FourWingsReportRegion]): Region information.
    """

    geojson: Optional[FourWingsGeometry] = Field(None, alias="geojson")

    region: Optional[FourWingsReportRegion] = Field(None, alias="region")
