"""Global Fishing Watch (GFW) API Python Client - Insights API Resource."""

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

    This resource provides methods to interact with the Insights API, specifically
    for retrieving insights data for specified vessels.

    For detailed information about the Insights API, please refer to the official
    Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#insights-api

    For more details on the Insights data caveats, please refer to the official
    Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#insights-api-fishing-detected-in-no-take-mpas

    See: https://globalfishingwatch.org/our-apis/documentation#what-does-it-mean-that-an-api-dataset-is-in-prototype-stage

    See: https://globalfishingwatch.org/our-apis/documentation#insights-api-fishing-event-detected-outside-known-authorized-areas

    See: https://globalfishingwatch.org/our-apis/documentation#insights-api-coverage

    See: https://globalfishingwatch.org/our-apis/documentation#insights-api-rfmo-iuu-vessel-list
    """

    async def get_vessel_insights(
        self,
        *,
        includes: Union[List[VesselInsightInclude], List[str]],
        start_date: Union[datetime.date, str],
        end_date: Union[datetime.date, str],
        vessels: Union[
            List[VesselInsightDatasetVessel], List[Dict[str, Any]], List[str]
        ],
        **kwargs: Dict[str, Any],
    ) -> VesselInsightResult:
        """Get insights for one or several vessels.

        Retrieves insights data for specified vessels based on the provided
        request parameters.

        The following insight types are supported:

        - Any apparent fishing events in no-take MPAs (`"FISHING"`)
        - Any apparent fishing events detected in areas with no known RFMO authorization (`"FISHING"`)
        - The vessel's AIS coverage metric (`"COVERAGE"`)
        - Any AIS off/disabling events (`"GAP"`)
        - If the vessel is present on an RFMO IUU vessel list (`"VESSEL-IDENTITY-IUU-VESSEL-LIST"`)
        - The vessel's flag changes (`"VESSEL-IDENTITY-FLAG-CHANGES"`)
        - The vessel's flag state presence under the Tokyo/Paris MOU black or grey lists (`"VESSEL-IDENTITY-MOU-LIST"`)

        For detailed information about the Get Vessels Insights API endpoint, please
        refer to the official Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#insights-by-vessels

        For more details on the Get Vessels Insights data caveats, please refer to the
        official Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#insights-api-fishing-detected-in-no-take-mpas

        See: https://globalfishingwatch.org/our-apis/documentation#what-does-it-mean-that-an-api-dataset-is-in-prototype-stage

        See: https://globalfishingwatch.org/our-apis/documentation#insights-api-fishing-event-detected-outside-known-authorized-areas

        See: https://globalfishingwatch.org/our-apis/documentation#insights-api-coverage

        See: https://globalfishingwatch.org/our-apis/documentation#insights-api-rfmo-iuu-vessel-list

        Args:
            includes (Union[List[VesselInsightInclude], List[str]], default=["FISHING"]):
                List of insight types to include in the response.
                Allowed values are `"COVERAGE"`, `"FISHING"`, `"GAP"`, `"VESSEL-IDENTITY-FLAG-CHANGES"`,
                `"VESSEL-IDENTITY-IUU-VESSEL-LIST"`, `"VESSEL-IDENTITY-MOU-LIST"`.
                Example: `["FISHING", "GAP"]`.

            start_date (Union[datetime.date, str], default=None):
                The start date for the insights period.
                Allowed values: A string in `ISO 8601 format` or `datetime.date` instance.
                Example: "2020-01-01" or `datetime.date(2020, 1, 1)`.

            end_date (Union[datetime.date, str], default=None):
                The end date for the insights period.
                Allowed values: A string in `ISO 8601 format` or `datetime.date` instance.
                Example: `"2025-03-03"` or `datetime.date(2025, 3, 3)`.

            vessels (Union[List[VesselInsightDatasetVessel], List[Dict[str, Any]], List[str]], default=None):
                List of vessel identifiers to retrieve insights for.
                Example: `[{"vessel_id": "785101812-2127-e5d2-e8bf-7152c5259f5f", "dataset_id": "public-global-vessel-identity:latest"}]`
                or `["785101812-2127-e5d2-e8bf-7152c5259f5f"]`.

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
        vessels: Union[
            List[VesselInsightDatasetVessel], List[Dict[str, Any]], List[str]
        ],
        **kwargs: Dict[str, Any],
    ) -> VesselInsightBody:
        """Prepare and returns get vessel insights request body."""
        try:
            _vessels: List[Union[VesselInsightDatasetVessel, Dict[str, Any]]] = [
                {"vessel_id": vessel} if isinstance(vessel, str) else vessel
                for vessel in vessels
            ]
            _request_body: Dict[str, Any] = {
                "includes": includes,
                "start_date": start_date,
                "end_date": end_date,
                "vessels": _vessels,
            }
            request_body: VesselInsightBody = VesselInsightBody(**_request_body)
        except pydantic.ValidationError as exc:
            raise RequestBodyValidationError(
                message=VESSEL_INSIGHT_REQUEST_BODY_VALIDATION_ERROR_MESSAGE, error=exc
            ) from exc

        return request_body
