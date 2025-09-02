"""Global Fishing Watch (GFW) API Python Client - Vessels Insights API Resource."""

import datetime

from typing import Any, Dict, List, Union

import pydantic

from gfwapiclient.exceptions import RequestBodyValidationError
from gfwapiclient.http.resources import BaseResource
from gfwapiclient.resources.insights.endpoints import VesselInsightEndPoint
from gfwapiclient.resources.insights.models.request import (
    VESSEL_INSIGHT_REQUEST_BODY_VALIDATION_ERROR_MESSAGE,
    VesselInsightBody,
    VesselInsightDatasetVessel,
    VesselInsightInclude,
)
from gfwapiclient.resources.insights.models.response import VesselInsightResult


__all__ = ["InsightResource"]


class InsightResource(BaseResource):
    """Insights data API resource.

    This resource provides methods to interact with the insights data API endpoints.
    """

    async def get_vessel_insights(
        self,
        *,
        includes: Union[List[VesselInsightInclude], List[str]],
        start_date: Union[datetime.date, str],
        end_date: Union[datetime.date, str],
        vessels: Union[List[VesselInsightDatasetVessel], List[Dict[str, Any]]],
        **kwargs: Dict[str, Any],
    ) -> VesselInsightResult:
        """Get vessels insights data.

        Retrieves insights data for specified vessels based on the provided
        request parameters.

        Args:
            includes (Union[List[VesselInsightInclude], List[str]]):
                List of insight types to include in the response.
                Allowed values are `"FISHING"`, `"GAP"`, `"COVERAGE"`, `"IDENTITY"`.
                Example: `["FISHING", "GAP"]`.

            start_date (Union[datetime.date, str]):
                The start date for the insights period.
                Allowed values: A string in `ISO 8601 format` or `datetime.date` instance.
                Example: "2020-01-01" or `datetime.date(2020, 1, 1)`.

            end_date (Union[datetime.date, str]):
                The end date for the insights period.
                Allowed values: A string in `ISO 8601 format` or `datetime.date` instance.
                Example: `"2025-03-03"` or `datetime.date(2025, 3, 3)`.

            vessels (Union[List[VesselInsightDatasetVessel], List[Dict[str, Any]]]):
                List of vessel identifiers to retrieve insights for.
                Example: `[{"vessel_id": "785101812-2127-e5d2-e8bf-7152c5259f5f", "dataset_id": "public-global-vessel-identity:latest",}]`.

            **kwargs (Dict[str, Any]):
                Additional keyword arguments.

        Returns:
            VesselInsightResult:
                The vessel insights result.

        Raises:
            GFWAPIClientError:
                If the API request fails.

            RequestBodyValidationError:
                If the request body is invalid.
        """
        request_body: VesselInsightBody = (
            self._prepare_get_vessel_insights_request_body(
                includes=includes,
                start_date=start_date,
                end_date=end_date,
                vessels=vessels,
                **kwargs,
            )
        )
        endpoint: VesselInsightEndPoint = VesselInsightEndPoint(
            request_body=request_body,
            http_client=self._http_client,
        )
        result: VesselInsightResult = await endpoint.request()
        return result

    def _prepare_get_vessel_insights_request_body(
        self,
        *,
        includes: Union[List[VesselInsightInclude], List[str]],
        start_date: Union[datetime.date, str],
        end_date: Union[datetime.date, str],
        vessels: Union[List[VesselInsightDatasetVessel], List[Dict[str, Any]]],
        **kwargs: Dict[str, Any],
    ) -> VesselInsightBody:
        """Prepare and returns get vessel insights request body."""
        try:
            _request_body: Dict[str, Any] = {
                "includes": includes,
                "start_date": start_date,
                "end_date": end_date,
                "vessels": vessels,
            }
            request_body: VesselInsightBody = VesselInsightBody(**_request_body)
        except pydantic.ValidationError as exc:
            raise RequestBodyValidationError(
                message=VESSEL_INSIGHT_REQUEST_BODY_VALIDATION_ERROR_MESSAGE, error=exc
            ) from exc

        return request_body
