"""Global Fishing Watch (GFW) API Python Client - Vessels Insights API Resource."""

from typing import Any, Dict, List, Optional

from gfwapiclient.http.resources import BaseResource
from gfwapiclient.resources.fourwings.report.endpoints import FourWingsReportEndPoint
from gfwapiclient.resources.fourwings.report.models.request import (
    FourWingsReportBody,
    FourWingsReportDataset,
    FourWingsReportFormat,
    FourWingsReportGroupBy,
    FourWingsReportParams,
    FourWingsReportRegion,
    FourWingsReportSpatialResolution,
    FourWingsReportTemporalResolution,
    Geometry,
)
from gfwapiclient.resources.fourwings.report.models.response import (
    FourWingsReportResult,
)


class FourWingsResource(BaseResource):
    """4Wings data API resource."""

    async def aget_report(
        self,
        spatial_resolution: Optional[
            FourWingsReportSpatialResolution
        ] = FourWingsReportSpatialResolution.HIGH,
        format: Optional[FourWingsReportFormat] = FourWingsReportFormat.JSON,
        group_by: Optional[FourWingsReportGroupBy] = None,
        temporal_resolution: Optional[FourWingsReportTemporalResolution] = None,
        datasets: Optional[List[FourWingsReportDataset]] = None,
        filters: Optional[List[str]] = None,
        # TODO: use start_date, end_date
        date_range: Optional[str] = None,
        spatial_aggregation: Optional[bool] = None,
        geojson: Optional[Geometry] = None,
        region: Optional[FourWingsReportRegion] = None,
        **kwargs: Dict[str, Any],
    ) -> FourWingsReportResult:
        """Asynchronously get 4Wings report for a specified region."""
        # TODO: _prepare_request_params|_build_request_params
        # TODO: _prepare_request_body|_build_request_body
        request_params = FourWingsReportParams(
            spatial_resolution=spatial_resolution,
            format=format,
            group_by=group_by,
            temporal_resolution=temporal_resolution,
            datasets=datasets,
            filters=filters,
            date_range=date_range,
            spatial_aggregation=spatial_aggregation,
        )  # type: ignore[call-arg]
        request_body = FourWingsReportBody(geojson=geojson, region=region)
        endpoint = FourWingsReportEndPoint(
            request_params=request_params,
            request_body=request_body,
            http_client=self._http_client,
        )
        result = await endpoint.arequest()
        return result

    def get_report(
        self,
        spatial_resolution: Optional[
            FourWingsReportSpatialResolution
        ] = FourWingsReportSpatialResolution.HIGH,
        format: Optional[FourWingsReportFormat] = FourWingsReportFormat.JSON,
        group_by: Optional[FourWingsReportGroupBy] = None,
        temporal_resolution: Optional[FourWingsReportTemporalResolution] = None,
        datasets: Optional[List[FourWingsReportDataset]] = None,
        filters: Optional[List[str]] = None,
        date_range: Optional[str] = None,
        spatial_aggregation: Optional[bool] = None,
        geojson: Optional[Geometry] = None,
        region: Optional[FourWingsReportRegion] = None,
        **kwargs: Dict[str, Any],
    ) -> FourWingsReportResult:
        """Synchronously get 4Wings report for a specified region."""
        request_params = FourWingsReportParams(
            spatial_resolution=spatial_resolution,
            format=format,
            group_by=group_by,
            temporal_resolution=temporal_resolution,
            datasets=datasets,
            filters=filters,
            date_range=date_range,
            spatial_aggregation=spatial_aggregation,
        )  # type: ignore[call-arg]
        request_body = FourWingsReportBody(geojson=geojson, region=region)
        endpoint = FourWingsReportEndPoint(
            request_params=request_params,
            request_body=request_body,
            http_client=self._http_client,
        )
        result = endpoint.request()
        return result
