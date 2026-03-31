"""Global Fishing Watch (GFW) API Python Client - Create a Bulk Report Request Models."""

from typing import Final, List, Optional

from pydantic import Field

from gfwapiclient.base.models import Geometry
from gfwapiclient.http.models import RequestBody
from gfwapiclient.resources.bulk_downloads.base.models.request import (
    BulkReportDataset,
    BulkReportFormat,
    BulkReportRegion,
)


__all__ = ["BulkReportCreateBody"]


BULK_REPORT_CREATE_BODY_VALIDATION_ERROR_MESSAGE: Final[str] = (
    "Create bulk report request body validation failed."
)


class BulkReportCreateBody(RequestBody):
    """Request body for Create a Bulk Report API endpoint.

    Represents dataset, filters, spatial parameters etc. for creating bulk reports.

    For more details on the Create a Bulk Report API endpoint supported request body,
    please refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#bulk-report-body-only-for-post-request

    See: https://globalfishingwatch.org/our-apis/documentation#create-a-bulk-report

    Attributes:
        name (Optional[str]):
            Human-readable name of the bulk report.
            If not provided, it will be generate using format
            `"{dataset}-{uuidv4}"`.

        dataset (Optional[BulkReportDataset]):
            Dataset that will be used to create the bulk report.
            Defaults to `"public-fixed-infrastructure-data:v1.1"`.

        geojson (Optional[Geometry]):
            Custom GeoJSON geometry to filter the bulk report.

        format (Optional[BulkReportFormat]):
            Bulk report result format.

        region (Optional[BulkReportRegion]):
            Predefined region information to filter the bulk report.

        filters (Optional[List[str]]):
            List of filters to apply when generating the bulk report.
    """

    name: Optional[str] = Field(None, alias="name")
    dataset: Optional[BulkReportDataset] = Field(
        BulkReportDataset.FIXED_INFRASTRUCTURE_DATA_LATEST, alias="dataset"
    )
    geojson: Optional[Geometry] = Field(None, alias="geojson")  # TODO: use GeoJson
    format: Optional[BulkReportFormat] = Field(BulkReportFormat.JSON, alias="format")
    region: Optional[BulkReportRegion] = Field(None, alias="region")
    filters: Optional[List[str]] = Field(None, alias="filters")
