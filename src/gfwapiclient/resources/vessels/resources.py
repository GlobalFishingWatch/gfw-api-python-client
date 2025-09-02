"""Global Fishing Watch (GFW) API Python Client - Vessels API Resource.

This module defines the resource for interacting with the Vessels API,
providing methods to retrieve vessel information.
"""

from typing import Any, Dict, List, Optional, Union

import pydantic

from gfwapiclient.exceptions.validation import RequestParamsValidationError
from gfwapiclient.http.resources import BaseResource
from gfwapiclient.resources.vessels.base.models.request import (
    VesselDataset,
    VesselInclude,
    VesselMatchField,
    VesselRegistryInfoData,
)
from gfwapiclient.resources.vessels.detail.endpoints import VesselDetailEndPoint
from gfwapiclient.resources.vessels.detail.models.request import (
    VESSEL_DETAIL_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
    VesselDetailParams,
)
from gfwapiclient.resources.vessels.detail.models.response import VesselDetailResult
from gfwapiclient.resources.vessels.list.endpoints import VesselListEndPoint
from gfwapiclient.resources.vessels.list.models.request import (
    VESSEL_LIST_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
    VesselListParams,
)
from gfwapiclient.resources.vessels.list.models.response import (
    VesselListResult,
)
from gfwapiclient.resources.vessels.search.endpoints import VesselSearchEndPoint
from gfwapiclient.resources.vessels.search.models.request import (
    VESSEL_SEARCH_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
    VesselSearchInclude,
    VesselSearchParams,
)
from gfwapiclient.resources.vessels.search.models.response import VesselSearchResult


__all__ = ["VesselResource"]


class VesselResource(BaseResource):
    """Vessels data API resource.

    This resource provides methods to interact with the Vessels API,
    allowing retrieval of vessel information including search, list by IDs,
    and retrieval by ID.
    """

    async def search_vessels(
        self,
        *,
        since: Optional[str] = None,
        limit: Optional[int] = 20,
        datasets: Optional[Union[List[VesselDataset], List[str]]] = None,
        query: Optional[str] = None,
        where: Optional[str] = None,
        match_fields: Optional[Union[List[VesselMatchField], List[str]]] = None,
        includes: Optional[Union[List[VesselSearchInclude], List[str]]] = None,
        **kwargs: Dict[str, Any],
    ) -> VesselSearchResult:
        """Search vessels based on provided parameters.

        Args:
            since (Optional[str], default=None):
                The token to send to get more results.
                Defaults to `None`.

            limit (Optional[int], default=20):
                Amount of search results to return. Defaults to `20`.
                Maximum `50`.
                Example: `20`.

            datasets (Optional[Union[List[VesselDataset], List[str]]], default=["public-global-vessel-identity:latest"]):
                Specify the datasets that will be used to search the vessel.
                Defaults to `["public-global-vessel-identity:latest"]`.
                Allowed values: `"public-global-vessel-identity:latest"`.
                Example: `["public-global-vessel-identity:latest"]`.

            query (Optional[str], default=None):
                Free form query that allows you to search a vessel by sending some identifier,
                for example: MMSI, IMO, CALL SIGN, Shipname, etc. Minimum 3 characters.
                Defaults to `None`.
                Example: `"Don tito"`.

            where (Optional[str], default=None):
                Advanced query that allows you to search a vessel by sending several identifiers.
                Defaults to `None`.
                Example: `"(shipname = 'SEIN PHOENIX' OR mmsi = '441618000') AND flag = 'KOR'"`

            match_fields (Optional[Union[List[VesselMatchField], List[str]]], default=None):
                This query param allows to filter by matchFields levels. Defaults to `None`.
                Allowed values: `"SEVERAL_FIELDS"`, `"NO_MATCH"`, `"ALL"`.
                Example: `["ALL"]`.

            includes (Optional[Union[List[VesselSearchInclude], List[str]]], default=["OWNERSHIP", "AUTHORIZATIONS", "MATCH_CRITERIA"]):
                This query param allows to add extra information to the response.
                Defaults to `["OWNERSHIP", "AUTHORIZATIONS", "MATCH_CRITERIA"]`.
                Allowed values: "OWNERSHIP", "AUTHORIZATIONS", "MATCH_CRITERIA".
                Example: `["OWNERSHIP", "AUTHORIZATIONS"]`.

            **kwargs (Dict[str, Any]):
                Additional keyword arguments.

        Returns:
            VesselSearchResult:
                The search results.

        Raises:
            GFWAPIClientError:
                If the API request fails.

            RequestParamsValidationError:
                If the request parameters are invalid.
        """
        request_params: VesselSearchParams = (
            self._prepare_search_vessels_request_params(
                since=since,
                limit=limit,
                datasets=datasets,
                query=query,
                where=where,
                match_fields=match_fields,
                includes=includes,
            )
        )
        endpoint: VesselSearchEndPoint = VesselSearchEndPoint(
            request_params=request_params,
            http_client=self._http_client,
        )
        result: VesselSearchResult = await endpoint.request()
        return result

    async def get_vessels_by_ids(
        self,
        *,
        ids: List[str],
        datasets: Optional[Union[List[VesselDataset], List[str]]] = None,
        registries_info_data: Optional[VesselRegistryInfoData] = None,
        includes: Optional[List[VesselInclude]] = None,
        match_fields: Optional[List[VesselMatchField]] = None,
        vessel_groups: Optional[List[str]] = None,
        **kwargs: Dict[str, Any],
    ) -> VesselListResult:
        """Get a list of vessels by their IDs.

        Args:
            ids (List[str]):
                List of vessel IDs to retrieve.
                Example: `["6583c51e3-3626-5638-866a-f47c3bc7ef7c"]`.

            datasets (Optional[Union[List[VesselDataset], List[str]]], default=["public-global-vessel-identity:latest"]):
                Specify the datasets that will be used to search the vessel.
                Defaults to `["public-global-vessel-identity:latest"]`.
                Allowed values: `"public-global-vessel-identity:latest"`.
                Example: `["public-global-vessel-identity:latest"]`.

            registries_info_data (Optional[Union[VesselRegistryInfoData, str]], default="ALL"):
                The response doesn't include all registry info data by default.
                It means, the default value is `"NONE"`. You can use `"DELTA"` to get only the data
                that changes in the time or `"ALL"` to get all data from the registries.
                Defaults to `"ALL"`.
                Allowed values: "NONE", "DELTA", "ALL".
                Example: `"ALL"`.

            includes (Optional[Union[List[VesselInclude], List[str]]], default=["POTENTIAL_RELATED_SELF_REPORTED_INFO"]):
                This query param allows to add extra information to the response. Defaults to `["POTENTIAL_RELATED_SELF_REPORTED_INFO"]`.
                Allowed values: `"POTENTIAL_RELATED_SELF_REPORTED_INFO"`.
                Example: `["POTENTIAL_RELATED_SELF_REPORTED_INFO"]`.

            match_fields (Optional[Union[List[VesselMatchField], List[str]]], default=None):
                This query param allows to filter by matchFields levels. Defaults to `None`.
                Allowed values: `"SEVERAL_FIELDS"`, `"NO_MATCH"`, `"ALL"`.
                Example: `["ALL"]`.

            vessel_groups (Optional[List[str]], default=None):
                List of vessel-groups. Defaults to `None`
                Example: `["my-vessel-group"]`.

            **kwargs (Dict[str, Any]):
                Additional keyword arguments.

        Returns:
            VesselListResult:
                The list of vessel details.

        Raises:
            GFWAPIClientError:
                If the API request fails.

            RequestParamsValidationError:
                If the request parameters are invalid.
        """
        request_params: VesselListParams = (
            self._prepare_get_vessels_by_ids_request_params(
                ids=ids,
                datasets=datasets,
                registries_info_data=registries_info_data,
                includes=includes,
                match_fields=match_fields,
                vessel_groups=vessel_groups,
            )
        )

        endpoint: VesselListEndPoint = VesselListEndPoint(
            request_params=request_params,
            http_client=self._http_client,
        )
        result: VesselListResult = await endpoint.request()
        return result

    async def get_vessel_by_id(
        self,
        *,
        id: str,
        dataset: Optional[Union[VesselDataset, str]] = None,
        registries_info_data: Optional[Union[VesselRegistryInfoData, str]] = None,
        includes: Optional[Union[List[VesselInclude], List[str]]] = None,
        match_fields: Optional[Union[List[VesselMatchField], List[str]]] = None,
        **kwargs: Dict[str, Any],
    ) -> VesselDetailResult:
        """Get vessel details by ID.

        Args:
            id (str):
                The ID of the vessel to retrieve.
                Example: `"6583c51e3-3626-5638-866a-f47c3bc7ef7c"`.

            dataset (Optional[Union[VesselDataset, str]], default="public-global-vessel-identity:latest"):
                Specify the dataset that will be used to search the vessel. Defaults to `"public-global-vessel-identity:latest"`.
                Allowed values: `"public-global-vessel-identity:latest"`.
                Example: `"public-global-vessel-identity:latest"`.

            registries_info_data (Optional[Union[VesselRegistryInfoData, str]], default="ALL"):
                The response doesn't include all registry info data by default.
                It means, the default value is `"NONE"`. You can use `"DELTA"` to get only the data
                that changes in the time or `"ALL"` to get all data from the registries.
                Defaults to `"ALL"`.
                Allowed values: `"NONE"`, `"DELTA"`, `"ALL"`.
                Example: `"ALL"`.

            includes (Optional[Union[List[VesselInclude], List[str]]], default=["POTENTIAL_RELATED_SELF_REPORTED_INFO"]):
                This query param allows to add extra information to the response. Defaults to `["POTENTIAL_RELATED_SELF_REPORTED_INFO"]`.
                Allowed values: `"POTENTIAL_RELATED_SELF_REPORTED_INFO"`.
                Example: `["POTENTIAL_RELATED_SELF_REPORTED_INFO"]`.

            match_fields (Optional[Union[List[VesselMatchField], List[str]]], default=None):
                This query param allows to filter by matchFields levels. Defaults to `None`.
                Allowed values: `"SEVERAL_FIELDS"`, `"NO_MATCH"`, `"ALL"`.
                Example: `["ALL"]`.

            **kwargs (Dict[str, Any]):
                Additional keyword arguments.

        Returns:
            VesselDetailResult:
                The vessel details.

        Raises:
            GFWAPIClientError:
                If the API request fails.

            RequestParamsValidationError:
                If the request parameters are invalid.
        """
        request_params: VesselDetailParams = (
            self._prepare_get_vessel_by_id_request_params(
                dataset=dataset,
                registries_info_data=registries_info_data,
                includes=includes,
                match_fields=match_fields,
            )
        )

        endpoint: VesselDetailEndPoint = VesselDetailEndPoint(
            vessel_id=id,
            request_params=request_params,
            http_client=self._http_client,
        )
        result: VesselDetailResult = await endpoint.request()
        return result

    def _prepare_search_vessels_request_params(
        self,
        *,
        since: Optional[str] = None,
        limit: Optional[int] = 20,
        datasets: Optional[Union[List[VesselDataset], List[str]]] = None,
        query: Optional[str] = None,
        where: Optional[str] = None,
        match_fields: Optional[Union[List[VesselMatchField], List[str]]] = None,
        includes: Optional[Union[List[VesselSearchInclude], List[str]]] = None,
    ) -> VesselSearchParams:
        """Prepare and return search vessels request parameters."""
        try:
            _request_params: Dict[str, Any] = {
                "since": since,
                "limit": limit,
                "datasets": datasets or [VesselDataset.VESSEL_IDENTITY_LATEST],
                "query": query,
                "where": where,
                "includes": (
                    includes
                    or [
                        VesselSearchInclude.OWNERSHIP,
                        VesselSearchInclude.AUTHORIZATIONS,
                        VesselSearchInclude.MATCH_CRITERIA,
                    ]
                ),
                "binary": False,
                "match_fields": match_fields,
            }
            request_params: VesselSearchParams = VesselSearchParams(**_request_params)
        except pydantic.ValidationError as exc:
            raise RequestParamsValidationError(
                message=VESSEL_SEARCH_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
                error=exc,
            ) from exc

        return request_params

    def _prepare_get_vessels_by_ids_request_params(
        self,
        *,
        ids: List[str],
        datasets: Optional[Union[List[VesselDataset], List[str]]] = None,
        registries_info_data: Optional[Union[VesselRegistryInfoData, str]] = None,
        includes: Optional[Union[List[VesselInclude], List[str]]] = None,
        match_fields: Optional[Union[List[VesselMatchField], List[str]]] = None,
        vessel_groups: Optional[List[str]] = None,
    ) -> VesselListParams:
        """Prepare and return get vessels by IDs request parameters."""
        try:
            _request_params: Dict[str, Any] = {
                "ids": ids,
                "datasets": datasets or [VesselDataset.VESSEL_IDENTITY_LATEST],
                "registries_info_data": (
                    registries_info_data or VesselRegistryInfoData.ALL
                ),
                "includes": (
                    includes or [VesselInclude.POTENTIAL_RELATED_SELF_REPORTED_INFO]
                ),
                "binary": False,
                "match_fields": match_fields,
                "vessel_groups": vessel_groups,
            }
            request_params: VesselListParams = VesselListParams(**_request_params)
        except pydantic.ValidationError as exc:
            raise RequestParamsValidationError(
                message=VESSEL_LIST_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
                error=exc,
            ) from exc

        return request_params

    def _prepare_get_vessel_by_id_request_params(
        self,
        *,
        dataset: Optional[Union[VesselDataset, str]] = None,
        registries_info_data: Optional[Union[VesselRegistryInfoData, str]] = None,
        includes: Optional[Union[List[VesselInclude], List[str]]] = None,
        match_fields: Optional[Union[List[VesselMatchField], List[str]]] = None,
    ) -> VesselDetailParams:
        """Prepare and return get vessel by ID request parameters."""
        try:
            _request_params: Dict[str, Any] = {
                "dataset": dataset or VesselDataset.VESSEL_IDENTITY_LATEST,
                "registries_info_data": (
                    registries_info_data or VesselRegistryInfoData.ALL
                ),
                "includes": (
                    includes or [VesselInclude.POTENTIAL_RELATED_SELF_REPORTED_INFO]
                ),
                "binary": False,
                "match_fields": match_fields,
            }
            request_params: VesselDetailParams = VesselDetailParams(**_request_params)
        except pydantic.ValidationError as exc:
            raise RequestParamsValidationError(
                message=VESSEL_DETAIL_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE,
                error=exc,
            ) from exc

        return request_params
