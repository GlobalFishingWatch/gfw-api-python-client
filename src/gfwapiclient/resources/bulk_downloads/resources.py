"""Global Fishing Watch (GFW) API Python Client - Bulk Download API Resource."""

from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import pydantic

from gfwapiclient.base.models import GeoJson, Geometry, SupportsGeoJsonInterface
from gfwapiclient.exceptions import (
    RequestBodyValidationError,
    RequestParamsValidationError,
)
from gfwapiclient.http.resources import BaseResource
from gfwapiclient.resources.bulk_downloads.base.models.request import (
    BulkReportDataset,
    BulkReportFileType,
    BulkReportFormat,
    BulkReportRegion,
)
from gfwapiclient.resources.bulk_downloads.base.models.response import BulkReportStatus
from gfwapiclient.resources.bulk_downloads.create.endpoints import (
    BulkReportCreateEndPoint,
)
from gfwapiclient.resources.bulk_downloads.create.models.request import (
    BULK_REPORT_CREATE_BODY_VALIDATION_ERROR_MESSAGE,
    BulkReportCreateBody,
)
from gfwapiclient.resources.bulk_downloads.create.models.response import (
    BulkReportCreateResult,
)
from gfwapiclient.resources.bulk_downloads.detail.endpoints import (
    BulkReportDetailEndPoint,
)
from gfwapiclient.resources.bulk_downloads.detail.models.response import (
    BulkReportDetailResult,
)
from gfwapiclient.resources.bulk_downloads.file.endpoints import BulkReportFileEndPoint
from gfwapiclient.resources.bulk_downloads.file.models.request import (
    BULK_REPORT_FILE_PARAMS_VALIDATION_ERROR_MESSAGE,
    BulkReportFileParams,
)
from gfwapiclient.resources.bulk_downloads.file.models.response import (
    BulkReportFileResult,
)
from gfwapiclient.resources.bulk_downloads.list.endpoints import BulkReportListEndPoint
from gfwapiclient.resources.bulk_downloads.list.models.request import (
    BULK_REPORT_LIST_PARAMS_VALIDATION_ERROR_MESSAGE,
    BulkReportListParams,
)
from gfwapiclient.resources.bulk_downloads.list.models.response import (
    BulkReportListResult,
)
from gfwapiclient.resources.bulk_downloads.query.endpoints import (
    BulkFixedInfrastructureDataQueryEndPoint,
)
from gfwapiclient.resources.bulk_downloads.query.models.base.request import (
    BULK_REPORT_QUERY_PARAMS_VALIDATION_ERROR_MESSAGE,
    BulkReportQueryParams,
)
from gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response import (
    BulkFixedInfrastructureDataQueryResult,
)


__all__ = ["BulkDownloadResource"]


class BulkDownloadResource(BaseResource):
    """Bulk download API resource.

    This resource provides methods to interact with the Bulk Download API,
    specifically to:

    - Create bulk reports based on specific filters and spatial parameters.
    - Monitor previously created bulk report generation status.
    - Get signed URL to download previously created bulk report data, metadata and
    region geometry (in GeoJSON format) files.
    - Query previously created bulk report data records in JSON format.

    For detailed information about the Bulk Download API, please refer to the official
    Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#bulk-download-api

    For more details on the Bulk Download API data caveats, please refer to the
    official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#sar-fixed-infrastructure-data-caveats
    """

    async def create_bulk_report(
        self,
        *,
        name: str,
        dataset: Optional[Union[BulkReportDataset, str]] = None,
        geojson: Optional[
            Union[GeoJson, str, Path, Dict[str, Any], SupportsGeoJsonInterface]
        ] = None,
        format: Optional[Union[BulkReportFormat, str]] = None,
        region: Optional[Union[BulkReportRegion, Dict[str, Any]]] = None,
        filters: Optional[List[str]] = None,
        **kwargs: Dict[str, Any],
    ) -> BulkReportCreateResult:
        """Create a bulk report based on specified filters and spatial parameters.

        For detailed information about the Create a Bulk Report API endpoint, please
        refer to the official Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#create-a-bulk-report

        For more details on the Create a Bulk Report data caveats, please refer to the
        official Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#sar-fixed-infrastructure-data-caveats

        **Disclaimer:**

        Depending on the complexity and size of your request (e.g., large geojson or region,
        long date range etc), generating the bulk report can take several minutes to
        several hours.

        Attributes:
            name (str):
                Human-readable name of the bulk report.
                Example: `"sar-fixed-infrastructure-data-20240903"`.

            dataset (Optional[Union[BulkReportDataset, str]], default="public-fixed-infrastructure-data:latest"):
                Dataset that will be used to create the bulk report.
                Defaults to `"public-fixed-infrastructure-data:latest"`.
                Allowed values: `"public-fixed-infrastructure-data:latest"`.
                Example: `"public-fixed-infrastructure-data:latest"`.

            geojson (Optional[Union[GeoJson, str, Path, Dict[str, Any], SupportsGeoJsonInterface]], default=None):
                Custom GeoJSON geometry to filter the bulk report. Either a path to a
                spatial file (e.g., GeoJSON, Shapefile, etc.), GeoJSON-like object
                (e.g., JSON string or dictionary) or `GeoJson` model instance. Defaults to `None`.
                Example: `{"type": "Polygon", "coordinates": [...]}`, or `/path/to/your/custom/region.shp`.

            format (Optional[Union[BulkReportFormat, str]], default="JSON"):
                Bulk report result format. Defaults to `"JSON"`.
                Allowed values: `"JSON"`, `"CSV"`.
                Example: `"JSON"`.

            region (Optional[Union[BulkReportRegion, Dict[str, Any]]], default=None):
                Predefined region information to filter the bulk report.
                Defaults to `None`.
                Example: `{"dataset": "public-eez-areas", "id": 8466}`.

            filters (Optional[List[str]], default=None):
                Filters to apply when generating the bulk report. Default to `None`.
                Example: `["label = 'oil'"]`

            **kwargs (Dict[str, Any]):
                Additional keyword arguments.

        Returns:
            BulkReportCreateResult:
                The created bulk report metadata and status.

        Raises:
            GFWAPIClientError:
                If the API request fails.

            RequestBodyValidationError:
                If the request body is invalid.
        """
        request_body: BulkReportCreateBody = (
            self._prepare_create_bulk_report_request_body(
                name=name,
                dataset=dataset,
                geojson=geojson,
                format=format,
                region=region,
                filters=filters,
            )
        )

        endpoint: BulkReportCreateEndPoint = BulkReportCreateEndPoint(
            request_body=request_body,
            http_client=self._http_client,
        )

        result: BulkReportCreateResult = await endpoint.request()
        return result

    async def get_bulk_report_by_id(
        self,
        *,
        id: str,
        **kwargs: Dict[
            str, Any
        ],  # TODO: polling logics (throttled retry based on status)
    ) -> BulkReportDetailResult:
        """Get a bulk report by ID.

        Retrieves metadata and status of the previously created bulk report based on the
        provided bulk report ID.

        For more details on the Get Bulk Report by ID API endpoint, please refer to the
        official Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#get-bulk-report-by-id

        For more details on the Get Bulk Report by ID data caveats, please refer
        to the official Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#sar-fixed-infrastructure-data-caveats

        **Important:**

        We recommend to use this method to poll the status of previously created
        bulk report, if it takes several minutes or hours to generate until it status
        is `"done"` or `"failed"`.

        Args:
            id (str):
                Unique identifier (ID) of the bulk report.
                Example: `"adbb9b62-5c08-4142-82e0-b2b575f3e058"`

            **kwargs (Dict[str, Any]):
                Additional keyword arguments.

        Returns:
            BulkReportDetailResult:
                The previously created bulk report metadata and status.

        Raises:
            GFWAPIClientError:
                If the API request fails.
        """
        endpoint: BulkReportDetailEndPoint = BulkReportDetailEndPoint(
            bulk_report_id=id, http_client=self._http_client
        )

        result: BulkReportDetailResult = await endpoint.request()
        return result

    async def get_all_bulk_reports(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        status: Optional[Union[BulkReportStatus, str]] = None,
        **kwargs: Dict[str, Any],
    ) -> BulkReportListResult:
        """Get all bulk reports created by user or application.

        Retrieves a list of metadata and status of the previously created
        bulk reports based on specified pagination, sorting, and filtering criteria.

        For detailed information about the Get All Bulk Reports API endpoint, please
        refer to the official Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#get-all-bulk-reports-by-user

        For more details on the Get All Bulk Reports data caveats, please refer to the
        official Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#sar-fixed-infrastructure-data-caveats

        Args:
            limit (Optional[int], default=99999):
                Maximum number of bulk reports to return. Defaults to `99999`.
                Example: `99999`.

            offset (Optional[int], default=0):
                Number of bulk reports to skip before returning results.
                Defaults to `0`.
                Example: `0`.

            sort (Optional[str], default="-createdAt"):
                Property to sort the bulk reports by. Defaults to `"-createdAt"`.
                Example: `"-createdAt"`.

            status (Optional[Union[BulkReportStatus, str]], default=None):
                Current status of the bulk report generation process.
                Defaults to `None`.
                Allowed values: `"pending"`, `"processing"`, `"done"`, `"failed"`.
                Example: `"done"`.

            **kwargs (Dict[str, Any]):
                Additional keyword arguments.

        Returns:
            BulkReportListResult:
                The result containing the list of previously created bulk report
                metadata and status.

        Raises:
            GFWAPIClientError:
                If the API request fails.

            RequestParamsValidationError:
                If the request parameters are invalid.
        """
        request_params: BulkReportListParams = self._prepare_get_all_bulk_report_params(
            limit=limit,
            offset=offset,
            sort=sort,
            status=status,
        )

        endpoint: BulkReportListEndPoint = BulkReportListEndPoint(
            request_params=request_params,
            http_client=self._http_client,
        )

        result: BulkReportListResult = await endpoint.request()
        return result

    async def get_bulk_report_file_download_url(
        self,
        *,
        id: str,
        file: Optional[Union[BulkReportFileType, str]] = None,
        **kwargs: Dict[str, Any],
    ) -> BulkReportFileResult:
        """Get signed URL to download file of the previously created bulk report.

        Retrieves signed URL that points to a downloadable file hosted on Global Fishing
        Watch's cloud infrastructure to download file(s) (i.e., `"DATA"`, `"README"`, or
        `"GEOM"`) of the previously created bulk report.

        For more details on the Download bulk Report (URL File) API endpoint, please
        refer to the official Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#download-bulk-report-url-file

        For more details on the Download bulk Report (URL File) data caveats, please
        refer to the official Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#sar-fixed-infrastructure-data-caveats

        Args:
            id (str):
                Unique identifier (ID) of the bulk report.
                Example: `"adbb9b62-5c08-4142-82e0-b2b575f3e058"`.

            file (Optional[Union[BulkReportFileType, str]], default="DATA"):
                Type of bulk report file. Defaults to `"DATA"`.
                Allowed values: `"DATA"`, `"README"`, `"GEOM"`.
                Example: `"DATA"`

            **kwargs (Dict[str, Any]):
                Additional keyword arguments.

        Returns:
            BulkReportFileResult:
                The signed URL to download bulk report file.

        Raises:
            GFWAPIClientError:
                If the API request fails.

            RequestParamsValidationError:
                If the request parameters are invalid.
        """
        request_params: BulkReportFileParams = (
            self._prepare_get_bulk_report_file_download_url_params(file=file)
        )

        endpoint: BulkReportFileEndPoint = BulkReportFileEndPoint(
            bulk_report_id=id,
            request_params=request_params,
            http_client=self._http_client,
        )

        result: BulkReportFileResult = await endpoint.request()
        return result

    async def query_bulk_fixed_infrastructure_data_report(
        self,
        *,
        id: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        includes: Optional[List[str]] = None,
        **kwargs: Dict[str, Any],
    ) -> BulkFixedInfrastructureDataQueryResult:
        """Get bulk fixed infrastructure data report in JSON Format.

        Retrieves data records of a previously created fixed infrastructure data (i.e.,
        `public-fixed-infrastructure-data:latest` dataset) bulk report data in JSON format
        based on specified pagination, sorting, and including criteria.

        For detailed information about the Query Bulk Report API endpoint, please
        refer to the official Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#get-data-in-json-format

        For more details on the Query Bulk Report data caveats, please refer to the
        official Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#sar-fixed-infrastructure-data-caveats

        Args:
            id (str):
                Unique identifier (ID) of the bulk report.
                Example: `"adbb9b62-5c08-4142-82e0-b2b575f3e058"`.

            limit (Optional[int], default=99999):
                Maximum number of bulk report records to return. Defaults to `99999`.
                Example: `99999`.

            offset (Optional[int], default=0):
                Number of bulk report records to skip before returning results.
                Defaults to `0`.
                Example: `0`.

            sort (Optional[str], default=None):
                Property to sort the bulk report records by. Defaults to `None`.
                Allowed fields: `"detection_date"`, `"structure_start_date"`,
                `"structure_end_date"`, `"label"`, `"label_confidence"`. Use `-` prefix
                for descending order.
                Example: `"-structure_start_date"`.

            includes (Optional[List[str]], default=None):
                List of bulk report record fields to include in the result.
                Defaults to `None`.
                Allowed values: `"detection_id"`, `"detection_date"`, `"structure_id"`,
                `"lon"`, `"lat"`, `"structure_start_date"`, `"structure_end_date"`,
                `"label"`, `"label_confidence"`.
                Example: `["structure_id", "lat", "lon", "label", "label_confidence"]`.

            **kwargs (Dict[str, Any]):
                Additional keyword arguments.

        Returns:
            BulkFixedInfrastructureDataQueryResult:
                The result containing the list of bulk fixed infrastructure data report items.

        Raises:
            GFWAPIClientError:
                If the API request fails.

            RequestParamsValidationError:
                If the request parameters are invalid.
        """
        request_params: BulkReportQueryParams = self._prepare_query_bulk_report_params(
            limit=limit,
            offset=offset,
            sort=sort,
            includes=includes,
        )

        endpoint: BulkFixedInfrastructureDataQueryEndPoint = (
            BulkFixedInfrastructureDataQueryEndPoint(
                bulk_report_id=id,
                request_params=request_params,
                http_client=self._http_client,
            )
        )

        result: BulkFixedInfrastructureDataQueryResult = await endpoint.request()
        return result

    def _prepare_create_bulk_report_request_body(
        self,
        *,
        name: str,
        dataset: Optional[Union[BulkReportDataset, str]] = None,
        geojson: Optional[
            Union[GeoJson, str, Path, Dict[str, Any], SupportsGeoJsonInterface]
        ] = None,
        format: Optional[Union[BulkReportFormat, str]] = None,
        region: Optional[Union[BulkReportRegion, Dict[str, Any]]] = None,
        filters: Optional[List[str]] = None,
    ) -> BulkReportCreateBody:
        """Prepare and return create a bulk report request body."""
        try:
            _dataset: Union[BulkReportDataset, str] = (
                dataset or BulkReportDataset.FIXED_INFRASTRUCTURE_DATA_LATEST
            )
            _geojson: Optional[Geometry] = (
                self._prepare_create_bulk_report_request_body_geojson(geojson=geojson)
            )
            _request_body: Dict[str, Any] = {
                "name": name,  # TODO: generate based on dataset name and timestamp (YYYMMDDHHmmss) / uuidv4
                "dataset": _dataset,
                "geojson": _geojson,
                "format": format or BulkReportFormat.JSON,
                "region": region or None,
                "filters": filters or None,
            }
            request_body: BulkReportCreateBody = BulkReportCreateBody(**_request_body)
        except pydantic.ValidationError as exc:
            raise RequestBodyValidationError(
                message=BULK_REPORT_CREATE_BODY_VALIDATION_ERROR_MESSAGE,
                error=exc,
            ) from exc

        return request_body

    def _prepare_get_all_bulk_report_params(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        status: Optional[Union[BulkReportStatus, str]] = None,
    ) -> BulkReportListParams:
        """Prepare and return get all bulk report request parameters."""
        try:
            _request_params: Dict[str, Any] = {
                "limit": limit or 99999,
                "offset": offset or 0,
                "sort": sort or "-createdAt",
                "status": status or None,
            }
            request_params: BulkReportListParams = BulkReportListParams(
                **_request_params
            )
        except pydantic.ValidationError as exc:
            raise RequestParamsValidationError(
                message=BULK_REPORT_LIST_PARAMS_VALIDATION_ERROR_MESSAGE,
                error=exc,
            ) from exc

        return request_params

    def _prepare_get_bulk_report_file_download_url_params(
        self, *, file: Optional[Union[BulkReportFileType, str]] = None
    ) -> BulkReportFileParams:
        """Prepare and return get bulk report file download url request parameters."""
        try:
            _request_params: Dict[str, Any] = {
                "file": file or BulkReportFileType.DATA,
            }
            request_params: BulkReportFileParams = BulkReportFileParams(
                **_request_params
            )
        except pydantic.ValidationError as exc:
            raise RequestParamsValidationError(
                message=BULK_REPORT_FILE_PARAMS_VALIDATION_ERROR_MESSAGE,
                error=exc,
            ) from exc

        return request_params

    def _prepare_query_bulk_report_params(
        self,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
        includes: Optional[List[str]] = None,
    ) -> BulkReportQueryParams:
        """Prepare and return query bulk report request parameters."""
        try:
            _request_params: Dict[str, Any] = {
                "limit": limit or 99999,
                "offset": offset or 0,
                "sort": sort or None,
                "includes": includes or None,
            }
            request_params: BulkReportQueryParams = BulkReportQueryParams(
                **_request_params
            )
        except pydantic.ValidationError as exc:
            raise RequestParamsValidationError(
                message=BULK_REPORT_QUERY_PARAMS_VALIDATION_ERROR_MESSAGE,
                error=exc,
            ) from exc

        return request_params

    def _prepare_create_bulk_report_request_body_geojson(
        self,
        *,
        geojson: Optional[
            Union[GeoJson, str, Path, Dict[str, Any], SupportsGeoJsonInterface]
        ] = None,
    ) -> Optional[Geometry]:
        """Prepare and return create a bulk report request body geojson."""
        if geojson is not None:
            _geojson: GeoJson = GeoJson.from_file_or_geojson(source=geojson)
            return _geojson.to_geometry()

        return None
