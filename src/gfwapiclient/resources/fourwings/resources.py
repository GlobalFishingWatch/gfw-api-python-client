"""Global Fishing Watch (GFW) API Python Client - 4Wings Report API Resource."""

import datetime

from typing import Any, Dict, List, Optional, Union, cast

import pydantic

from gfwapiclient.exceptions import (
    RequestBodyValidationError,
    RequestParamsValidationError,
)
from gfwapiclient.http.resources import BaseResource
from gfwapiclient.resources.fourwings.report.endpoints import FourWingsReportEndPoint
from gfwapiclient.resources.fourwings.report.models.request import (
    FOURWINGS_REPORT_REQUEST_BODY_VALIDATION_ERROR_MESSAGE,
    FOURWINGS_REPORT_REQUEST_PARAM_VALIDATION_ERROR_MESSAGE,
    FOURWINGS_REPORT_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
    FourWingsGeometry,
    FourWingsReportBody,
    FourWingsReportDataset,
    FourWingsReportFormat,
    FourWingsReportGroupBy,
    FourWingsReportParams,
    FourWingsReportRegion,
    FourWingsReportSpatialResolution,
    FourWingsReportTemporalResolution,
)
from gfwapiclient.resources.fourwings.report.models.response import (
    FourWingsReportResult,
)


__all__ = ["FourWingsResource"]


class FourWingsResource(BaseResource):
    """4Wings data API resource.

    This resource provides methods to interact with the 4Wings API, specifically
    for generating reports.
    """

    async def create_report(
        self,
        *,
        spatial_resolution: Optional[
            Union[FourWingsReportSpatialResolution, str]
        ] = None,
        group_by: Optional[Union[FourWingsReportGroupBy, str]] = None,
        temporal_resolution: Optional[
            Union[FourWingsReportTemporalResolution, str]
        ] = None,
        datasets: Optional[Union[List[FourWingsReportDataset], List[str]]] = None,
        filters: Optional[List[str]] = None,
        start_date: Optional[Union[datetime.date, str]] = None,
        end_date: Optional[Union[datetime.date, str]] = None,
        spatial_aggregation: Optional[bool] = None,
        geojson: Optional[Union[FourWingsGeometry, Dict[str, Any]]] = None,
        region: Optional[Union[FourWingsReportRegion, Dict[str, Any]]] = None,
        **kwargs: Dict[str, Any],
    ) -> FourWingsReportResult:
        """Create 4Wings report for a specified region.

        Generates a report from the 4Wings API based on the provided parameters.

        Args:
            spatial_resolution (Optional[Union[FourWingsReportSpatialResolution, str]]):
                Spatial resolution of the report. Defaults to `HIGH`.
                Allowed values: `HIGH`, `LOW`.
                Example: `"LOW"`.

            group_by (Optional[Union[FourWingsReportGroupBy, str]]):
                Grouping criteria for the report.
                Allowed values: `VESSEL_ID`, `FLAG`, `GEARTYPE`, `FLAGANDGEARTYPE`, `MMSI`.
                Example: `"FLAG"`.

            temporal_resolution (Optional[Union[FourWingsReportTemporalResolution, str]]):
                Temporal resolution of the report. Defaults to `HOURLY`
                Allowed values: `HOURLY`, `DAILY`, `MONTHLY`, `YEARLY`, `ENTIRE`.
                Example: `"MONTHLY"`.

            datasets (Optional[Union[List[FourWingsReportDataset], List[str]]]):
                Datasets to include in the report. Defaults to `public-global-fishing-effort:latest`.
                Allowed values: `public-global-fishing-effort:latest`, `public-global-sar-presence:latest`.
                Example: `["public-global-fishing-effort:latest"]`.

            filters (Optional[List[str]]):
                Filters to apply to the report.
                Example: `["flag in ('ESP', 'FRA')]`.

            start_date (Optional[Union[datetime.date, str]]):
                Start date for the report. Used to build `date_range`.
                Example: `datetime.date(2021, 1, 1)` or `"2021-01-01"`.

            end_date (Optional[Union[datetime.date, str]]):
                End date for the report. Used to build `date_range`.
                Example: `datetime.date(2021, 1, 15)` or `"2021-01-15"`.

            spatial_aggregation (Optional[bool]):
                Whether to spatially aggregate the report.
                Example: `True`.

            geojson (Optional[Union[FourWingsGeometry, Dict[str, Any]]]):
                GeoJSON geometry to filter the report.
                Example: `{"type": "Polygon", "coordinates": [...]}`.

            region (Optional[Union[FourWingsReportRegion, Dict[str, Any]]]):
                Region information to filter the report.
                Example: `{"dataset": "public-eez-areas", "id": "5690"}`.

            **kwargs (Dict[str, Any]):
                Additional keyword arguments.

        Returns:
            FourWingsReportResult:
                The generated 4Wings report.

        Raises:
            GFWAPIClientError:
                If the API request fails.

            RequestParamsValidationError:
                If the request parameters are invalid.

            RequestBodyValidationError:
                If the request body is invalid.
        """
        request_params: FourWingsReportParams = (
            self._prepare_create_report_request_params(
                spatial_resolution=spatial_resolution,
                group_by=group_by,
                temporal_resolution=temporal_resolution,
                datasets=datasets,
                filters=filters,
                start_date=start_date,
                end_date=end_date,
                spatial_aggregation=spatial_aggregation,
            )
        )
        request_body: FourWingsReportBody = self._prepare_create_report_request_body(
            geojson=geojson,
            region=region,
        )

        endpoint: FourWingsReportEndPoint = FourWingsReportEndPoint(
            request_params=request_params,
            request_body=request_body,
            http_client=self._http_client,
        )
        result: FourWingsReportResult = await endpoint.request()
        return result

    def _prepare_create_report_request_body(
        self,
        *,
        geojson: Optional[Union[FourWingsGeometry, Dict[str, Any]]] = None,
        region: Optional[Union[FourWingsReportRegion, Dict[str, Any]]] = None,
    ) -> FourWingsReportBody:
        """Prepare request body for the 4Wings report endpoint."""
        try:
            _request_body: Dict[str, Any] = {
                "geojson": geojson,
                "region": region,
            }
            request_body: FourWingsReportBody = FourWingsReportBody(**_request_body)
        except pydantic.ValidationError as exc:
            raise RequestBodyValidationError(
                message=FOURWINGS_REPORT_REQUEST_BODY_VALIDATION_ERROR_MESSAGE,
                error=exc,
            ) from exc

        return request_body

    def _prepare_create_report_request_params(
        self,
        *,
        spatial_resolution: Optional[
            Union[FourWingsReportSpatialResolution, str]
        ] = None,
        group_by: Optional[Union[FourWingsReportGroupBy, str]] = None,
        temporal_resolution: Optional[
            Union[FourWingsReportTemporalResolution, str]
        ] = None,
        datasets: Optional[Union[List[FourWingsReportDataset], List[str]]] = None,
        filters: Optional[List[str]] = None,
        start_date: Optional[Union[datetime.date, str]] = None,
        end_date: Optional[Union[datetime.date, str]] = None,
        spatial_aggregation: Optional[bool] = None,
    ) -> FourWingsReportParams:
        """Prepare request parameters for the 4Wings report endpoint."""
        date_range: Optional[str] = (
            self._prepare_create_report_date_range_request_param(
                start_date=start_date, end_date=end_date
            )
        )
        try:
            _request_params: Dict[str, Any] = {
                "format": FourWingsReportFormat.JSON,
                "spatial_resolution": (
                    spatial_resolution or FourWingsReportSpatialResolution.HIGH
                ),
                "group_by": group_by or None,
                "temporal_resolution": (
                    temporal_resolution or FourWingsReportTemporalResolution.HOURLY
                ),
                "datasets": datasets or [FourWingsReportDataset.FISHING_EFFORT_LATEST],
                "filters": filters or None,
                "spatial_aggregation": spatial_aggregation or None,
                "date_range": date_range or None,
            }
            request_params: FourWingsReportParams = FourWingsReportParams(
                **_request_params
            )
        except pydantic.ValidationError as exc:
            raise RequestParamsValidationError(
                message=FOURWINGS_REPORT_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
                error=exc,
            ) from exc

        return request_params

    def _prepare_create_report_date_range_request_param(
        self,
        *,
        start_date: Optional[Union[datetime.date, str]] = None,
        end_date: Optional[Union[datetime.date, str]] = None,
    ) -> Optional[str]:
        """Prepare and return `date_range` request parameter."""
        date_range: Optional[str] = None
        if start_date or end_date:
            try:
                _start_date: datetime.date = (
                    start_date
                    if isinstance(start_date, datetime.date)
                    else datetime.date.fromisoformat(cast(str, start_date))
                )
                _end_date: datetime.date = (
                    end_date
                    if isinstance(end_date, datetime.date)
                    else datetime.date.fromisoformat(cast(str, end_date))
                )
                date_range = f"{_start_date.isoformat()},{_end_date.isoformat()}"
            except Exception as exc:
                raise RequestParamsValidationError(
                    message=FOURWINGS_REPORT_REQUEST_PARAM_VALIDATION_ERROR_MESSAGE,
                ) from exc

        return date_range
