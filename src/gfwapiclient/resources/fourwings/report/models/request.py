"""Global Fishing Watch (GFW) API Python Client - 4Wings Report API Request Models."""

from enum import Enum
from typing import Any, ClassVar, List, Optional

from pydantic import Field

from gfwapiclient.base.models import BaseModel
from gfwapiclient.http.models import RequestBody, RequestParams


__all__ = ["FourWingsReportBody", "FourWingsReportParams"]


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
    # TODO: add missing


# TODO: use shapely.Geometry???
# TODO: rename FourWingsGeometry???
class Geometry(BaseModel):
    """4Wings report GeoJSON-like geometry input."""

    type: str
    coordinates: Any
    # FIX: Should ideally be `List[List[List[float]]]` for MultiPolygon


# TODO: extend base Region
class FourWingsReportRegion(BaseModel):
    """4Wings report region of interest."""

    dataset: Optional[str] = Field(None, alias="dataset")
    id: Optional[str] = Field(None, alias="id")  # Union[str, int]
    buffer_operation: Optional[FourWingsReportBufferOperation] = Field(
        None, alias="bufferOperation"
    )
    buffer_unit: Optional[FourWingsReportBufferUnit] = Field(None, alias="bufferUnit")
    buffer_value: Optional[str] = Field(None, alias="bufferValue")


class FourWingsReportParams(RequestParams):
    """4Wings report request params."""

    indexed_fields: ClassVar[Optional[List[str]]] = ["datasets", "filters"]

    spatial_resolution: Optional[FourWingsReportSpatialResolution] = Field(
        None, alias="spatial-resolution", description="Spatial resolution."
    )
    format: Optional[FourWingsReportFormat] = Field(
        FourWingsReportFormat.JSON, alias="format", description="Report result format."
    )
    group_by: Optional[FourWingsReportGroupBy] = Field(
        None, alias="group-by", description="Grouped by criteria."
    )
    temporal_resolution: Optional[FourWingsReportTemporalResolution] = Field(
        None, alias="temporal-resolution", description="Temporal resolution."
    )
    datasets: Optional[List[FourWingsReportDataset]] = Field(
        None,
        alias="datasets",
        description="Datasets that will be used to create the report (style).",
    )
    filters: Optional[List[str]] = Field(
        None, alias="filters", description="Filters are applied to the dataset."
    )
    # TODO: use start_date, end_date
    date_range: Optional[str] = Field(
        None,
        alias="date-range",
        description="Start date and end date to filter the data.",
    )
    spatial_aggregation: Optional[bool] = Field(
        None,
        alias="spatial-aggregation",
        description="Whether to spatial aggregate the report.",
    )


class FourWingsReportBody(RequestBody):
    """4Wings report request body."""

    geojson: Optional[Geometry] = Field(
        None, alias="geojson", description="Geometry to filter the data."
    )

    region: Optional[FourWingsReportRegion] = Field(
        None, description="Region information."
    )
