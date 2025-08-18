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
    for generating AIS apparent fishing activity, AIS vessel presence
    and SAR vessel detections reports.

    For detailed information about the 4Wings API, refer to the official
    Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#map-visualization-4wings-api

    For more details on the 4Wings data caveats, please refer to the official
    Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#apparent-fishing-effort

    See: https://globalfishingwatch.org/our-apis/documentation#sar-vessel-detections-data-caveats

    See: https://globalfishingwatch.org/our-apis/documentation#ais-vessel-presence-caveats
    """

    async def create_fishing_effort_report(
        self,
        *,
        spatial_resolution: Optional[
            Union[FourWingsReportSpatialResolution, str]
        ] = None,
        group_by: Optional[Union[FourWingsReportGroupBy, str]] = None,
        temporal_resolution: Optional[
            Union[FourWingsReportTemporalResolution, str]
        ] = None,
        filters: Optional[List[str]] = None,
        start_date: Optional[Union[datetime.date, str]] = None,
        end_date: Optional[Union[datetime.date, str]] = None,
        spatial_aggregation: Optional[bool] = None,
        geojson: Optional[Union[FourWingsGeometry, Dict[str, Any]]] = None,
        region: Optional[Union[FourWingsReportRegion, Dict[str, Any]]] = None,
        **kwargs: Dict[str, Any],
    ) -> FourWingsReportResult:
        """Create 4Wings AIS apparent fishing effort report for a specified region.

        Generates AIS (Automatic Identification System) apparent fishing effort report
        from the 4Wings API based on the provided parameters to visualize apparent
        fishing activity based on AIS data.

        Generated report can serves following analytical needs:

        - Fisheries compliance monitoring
        - Fleet management
        - Supply chain visibility

        For more details on the 4Wings AIS apparent fishing effort data caveats,
        please refer to the official Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#apparent-fishing-effort

        Args:
            spatial_resolution (Optional[Union[FourWingsReportSpatialResolution, str]], default="HIGH"):
                Spatial resolution of the report. Defaults to `"HIGH"`.
                Allowed values: `"HIGH"`, `"LOW"`.
                Example: `"HIGH"`.

            group_by (Optional[Union[FourWingsReportGroupBy, str]], default=None):
                Grouping criteria for the report. Defaults to `None`.
                Allowed values: `"VESSEL_ID"`, `"FLAG"`, `"GEARTYPE"`, `"FLAGANDGEARTYPE"`, `"MMSI"`.
                Example: `"FLAG"`.

            temporal_resolution (Optional[Union[FourWingsReportTemporalResolution, str]], default="HOURLY"):
                Temporal resolution of the report. Defaults to `"HOURLY"`
                Allowed values: `"HOURLY"`, `"DAILY"`, `"MONTHLY"`, `"YEARLY"`, `"ENTIRE"`.
                Example: `"HOURLY"`.

            filters (Optional[List[str]], default=None):
                Filters to apply to the report. Defaults to `None`.
                Allowed filters: `flag`, `geartype` and `vessel_id`.
                Example: `["flag in ('ESP', 'FRA')"]`.

            start_date (Optional[Union[datetime.date, str]], default=None):
                Start date for the report. Used to build `date_range`. Defaults to `None`.
                Allowed values: A string in `ISO 8601 format` or `datetime.date` instance.
                Example: `datetime.date(2021, 1, 1)` or `"2021-01-01"`.

            end_date (Optional[Union[datetime.date, str]], default=None):
                End date for the report. Used to build `date_range`. Defaults to `None`.
                Allowed values: A string in `ISO 8601 format` or `datetime.date` instance.
                Example: `datetime.date(2021, 1, 15)` or `"2021-01-15"`.

            spatial_aggregation (Optional[bool], default=None):
                Whether to spatially aggregate the report. Defaults to `None`.
                Example: `True`.

            geojson (Optional[Union[FourWingsGeometry, Dict[str, Any]]], default=None):
                Custom GeoJSON geometry to filter the report. Defaults to `None`.
                Example: `{"type": "Polygon", "coordinates": [...]}`.

            region (Optional[Union[FourWingsReportRegion, Dict[str, Any]]], default=None):
                Predefined region information to filter the report. Defaults to `None`.
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
        result: FourWingsReportResult = await self.create_report(
            spatial_resolution=spatial_resolution,
            group_by=group_by,
            temporal_resolution=temporal_resolution,
            datasets=[FourWingsReportDataset.FISHING_EFFORT_LATEST],
            filters=filters,
            start_date=start_date,
            end_date=end_date,
            spatial_aggregation=spatial_aggregation,
            geojson=geojson,
            region=region,
            **kwargs,
        )
        return result

    async def create_ais_presence_report(
        self,
        *,
        spatial_resolution: Optional[
            Union[FourWingsReportSpatialResolution, str]
        ] = None,
        group_by: Optional[Union[FourWingsReportGroupBy, str]] = None,
        temporal_resolution: Optional[
            Union[FourWingsReportTemporalResolution, str]
        ] = None,
        filters: Optional[List[str]] = None,
        start_date: Optional[Union[datetime.date, str]] = None,
        end_date: Optional[Union[datetime.date, str]] = None,
        spatial_aggregation: Optional[bool] = None,
        geojson: Optional[Union[FourWingsGeometry, Dict[str, Any]]] = None,
        region: Optional[Union[FourWingsReportRegion, Dict[str, Any]]] = None,
        **kwargs: Dict[str, Any],
    ) -> FourWingsReportResult:
        """Create 4Wings AIS vessel presence report for a specified region.

        Generates AIS (Automatic Identification System) apparent fishing effort report
        from the 4Wings API based on the provided parameters to visualize any vessel
        type presence and movement patterns based on AIS data.

        Generated report can serves following analytical needs:

        - Port traffic analysis
        - Fleet management
        - Supply chain visibility

        For more details on the 4Wings AIS vessel presence data caveats,
        please refer to the official Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#ais-vessel-presence-caveats

        **Disclaimer:**

        AIS vessel presence is one of the largest datasets available. To prevent timeouts
        and ensure optimal performance, keep requests manageable: prefer simple, small
        regions and shorter time ranges (e.g., a few days).

        Args:
            spatial_resolution (Optional[Union[FourWingsReportSpatialResolution, str]], default="HIGH"):
                Spatial resolution of the report. Defaults to `"HIGH"`.
                Allowed values: `"HIGH"`, `"LOW"`.
                Example: `"HIGH"`.

            group_by (Optional[Union[FourWingsReportGroupBy, str]], default=None):
                Grouping criteria for the report. Defaults to `None`.
                Allowed values: `"VESSEL_ID"`, `"FLAG"`, `"GEARTYPE"`, `"FLAGANDGEARTYPE"`, `"MMSI"`.
                Example: `"FLAG"`.

            temporal_resolution (Optional[Union[FourWingsReportTemporalResolution, str]], default="HOURLY"):
                Temporal resolution of the report. Defaults to `"HOURLY"`
                Allowed values: `"HOURLY"`, `"DAILY"`, `"MONTHLY"`, `"YEARLY"`, `"ENTIRE"`.
                Example: `"HOURLY"`.

            filters (Optional[List[str]], default=None):
                Filters to apply to the report. Defaults to `None`.
                Allowed filters: `flag`, `vessel_type`, and `speed`.
                Example: `["flag in ('ESP', 'FRA')"]`.

            start_date (Optional[Union[datetime.date, str]], default=None):
                Start date for the report. Used to build `date_range`. Defaults to `None`.
                Allowed values: A string in `ISO 8601 format` or `datetime.date` instance.
                Example: `datetime.date(2021, 1, 1)` or `"2021-01-01"`.

            end_date (Optional[Union[datetime.date, str]], default=None):
                End date for the report. Used to build `date_range`. Defaults to `None`.
                Allowed values: A string in `ISO 8601 format` or `datetime.date` instance.
                Example: `datetime.date(2021, 1, 15)` or `"2021-01-15"`.

            spatial_aggregation (Optional[bool], default=None):
                Whether to spatially aggregate the report. Defaults to `None`.
                Example: `True`.

            geojson (Optional[Union[FourWingsGeometry, Dict[str, Any]]], default=None):
                Custom GeoJSON geometry to filter the report. Defaults to `None`.
                Example: `{"type": "Polygon", "coordinates": [...]}`.

            region (Optional[Union[FourWingsReportRegion, Dict[str, Any]]], default=None):
                Predefined region information to filter the report. Defaults to `None`.
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
        result: FourWingsReportResult = await self.create_report(
            spatial_resolution=spatial_resolution,
            group_by=group_by,
            temporal_resolution=temporal_resolution,
            datasets=[FourWingsReportDataset.PRESENCE_LATEST],
            filters=filters,
            start_date=start_date,
            end_date=end_date,
            spatial_aggregation=spatial_aggregation,
            geojson=geojson,
            region=region,
            **kwargs,
        )
        return result

    async def create_sar_presence_report(
        self,
        *,
        spatial_resolution: Optional[
            Union[FourWingsReportSpatialResolution, str]
        ] = None,
        group_by: Optional[Union[FourWingsReportGroupBy, str]] = None,
        temporal_resolution: Optional[
            Union[FourWingsReportTemporalResolution, str]
        ] = None,
        filters: Optional[List[str]] = None,
        start_date: Optional[Union[datetime.date, str]] = None,
        end_date: Optional[Union[datetime.date, str]] = None,
        spatial_aggregation: Optional[bool] = None,
        geojson: Optional[Union[FourWingsGeometry, Dict[str, Any]]] = None,
        region: Optional[Union[FourWingsReportRegion, Dict[str, Any]]] = None,
        **kwargs: Dict[str, Any],
    ) -> FourWingsReportResult:
        """Create 4Wings SAR vessel detections report for a specified region.

        Generates SAR (Synthetic-Aperture Radar) vessel detections report.

        Generated report can serves following analytical needs:

        - Dark vessel detection
        - Remote area surveillance

        For more details on the 4Wings SAR vessel detections data caveats,
        please refer to the official Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#sar-vessel-detections-data-caveats

        Args:
            spatial_resolution (Optional[Union[FourWingsReportSpatialResolution, str]], default="HIGH"):
                Spatial resolution of the report. Defaults to `"HIGH"`.
                Allowed values: `"HIGH"`, `"LOW"`.
                Example: `"HIGH"`.

            group_by (Optional[Union[FourWingsReportGroupBy, str]], default=None):
                Grouping criteria for the report. Defaults to `None`.
                Allowed values: `"VESSEL_ID"`, `"FLAG"`, `"GEARTYPE"`, `"FLAGANDGEARTYPE"`, `"MMSI"`.
                Example: `"FLAG"`.

            temporal_resolution (Optional[Union[FourWingsReportTemporalResolution, str]], default="HOURLY"):
                Temporal resolution of the report. Defaults to `"HOURLY"`
                Allowed values: `"HOURLY"`, `"DAILY"`, `"MONTHLY"`, `"YEARLY"`, `"ENTIRE"`.
                Example: `"HOURLY"`.

            filters (Optional[List[str]], default=None):
                Filters to apply to the report. Defaults to `None`.
                Allowed filters: `matched`, `flag`, `vessel_id`, `geartype`,
                `neural_vessel_type` and `shiptype`.
                Example: `["flag in ('ESP', 'FRA')"]`.

            start_date (Optional[Union[datetime.date, str]], default=None):
                Start date for the report. Used to build `date_range`. Defaults to `None`.
                Allowed values: A string in `ISO 8601 format` or `datetime.date` instance.
                Example: `datetime.date(2021, 1, 1)` or `"2021-01-01"`.

            end_date (Optional[Union[datetime.date, str]], default=None):
                End date for the report. Used to build `date_range`. Defaults to `None`.
                Allowed values: A string in `ISO 8601 format` or `datetime.date` instance.
                Example: `datetime.date(2021, 1, 15)` or `"2021-01-15"`.

            spatial_aggregation (Optional[bool], default=None):
                Whether to spatially aggregate the report. Defaults to `None`.
                Example: `True`.

            geojson (Optional[Union[FourWingsGeometry, Dict[str, Any]]], default=None):
                Custom GeoJSON geometry to filter the report. Defaults to `None`.
                Example: `{"type": "Polygon", "coordinates": [...]}`.

            region (Optional[Union[FourWingsReportRegion, Dict[str, Any]]], default=None):
                Predefined region information to filter the report. Defaults to `None`.
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
        result: FourWingsReportResult = await self.create_report(
            spatial_resolution=spatial_resolution,
            group_by=group_by,
            temporal_resolution=temporal_resolution,
            datasets=[FourWingsReportDataset.SAR_PRESENCE_LATEST],
            filters=filters,
            start_date=start_date,
            end_date=end_date,
            spatial_aggregation=spatial_aggregation,
            geojson=geojson,
            region=region,
            **kwargs,
        )
        return result

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

        Generated report can serves following analytical needs:

        - Fisheries compliance monitoring
        - Fleet management
        - Supply chain visibility
        - Port traffic analysis
        - Fleet management
        - Supply chain visibility
        - Dark vessel detection
        - Remote area surveillance

        For more details on the 4Wings data caveats, please refer to the official
        Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#apparent-fishing-effort

        See: https://globalfishingwatch.org/our-apis/documentation#sar-vessel-detections-data-caveats

        See: https://globalfishingwatch.org/our-apis/documentation#ais-vessel-presence-caveats

        **Disclaimer:**

        AIS vessel presence is one of the largest datasets available. To prevent timeouts
        and ensure optimal performance, keep requests manageable: prefer simple, small
        regions and shorter time ranges (e.g., a few days).

        Args:
            spatial_resolution (Optional[Union[FourWingsReportSpatialResolution, str]], default="HIGH"):
                Spatial resolution of the report. Defaults to `"HIGH"`.
                Allowed values: `"HIGH"`, `"LOW"`.
                Example: `"HIGH"`.

            group_by (Optional[Union[FourWingsReportGroupBy, str]], default=None):
                Grouping criteria for the report. Defaults to `None`.
                Allowed values: `"VESSEL_ID"`, `"FLAG"`, `"GEARTYPE"`, `"FLAGANDGEARTYPE"`, `"MMSI"`.
                Example: `"FLAG"`.

            temporal_resolution (Optional[Union[FourWingsReportTemporalResolution, str]], default="HOURLY"):
                Temporal resolution of the report. Defaults to `"HOURLY"`
                Allowed values: `"HOURLY"`, `"DAILY"`, `"MONTHLY"`, `"YEARLY"`, `"ENTIRE"`.
                Example: `"HOURLY"`.

            datasets (Optional[Union[List[FourWingsReportDataset], List[str]]], default=["public-global-fishing-effort:latest"]):
                Datasets that will be used to create the report. Defaults to `["public-global-fishing-effort:latest"]`.
                Allowed values: `"public-global-fishing-effort:latest"`, `"public-global-sar-presence:latest"`,
                `"public-global-presence:latest"`.
                Example: `["public-global-fishing-effort:latest"]`.

            filters (Optional[List[str]], default=None):
                Filters to apply to the report. Defaults to `None`.
                Example: `["flag in ('ESP', 'FRA')"]`.

            start_date (Optional[Union[datetime.date, str]], default=None):
                Start date for the report. Used to build `date_range`. Defaults to `None`.
                Allowed values: A string in `ISO 8601 format` or `datetime.date` instance.
                Example: `datetime.date(2021, 1, 1)` or `"2021-01-01"`.

            end_date (Optional[Union[datetime.date, str]], default=None):
                End date for the report. Used to build `date_range`. Defaults to `None`.
                Allowed values: A string in `ISO 8601 format` or `datetime.date` instance.
                Example: `datetime.date(2021, 1, 15)` or `"2021-01-15"`.

            spatial_aggregation (Optional[bool], default=None):
                Whether to spatially aggregate the report. Defaults to `None`.
                Example: `True`.

            geojson (Optional[Union[FourWingsGeometry, Dict[str, Any]]], default=None):
                Custom GeoJSON geometry to filter the report. Defaults to `None`.
                Example: `{"type": "Polygon", "coordinates": [...]}`.

            region (Optional[Union[FourWingsReportRegion, Dict[str, Any]]], default=None):
                Predefined region information to filter the report. Defaults to `None`.
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
