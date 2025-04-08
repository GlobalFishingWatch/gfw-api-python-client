"""Global Fishing Watch (GFW) API Python Client - POST HTTP EndPoint."""

import http

from typing import Optional, Type

from gfwapiclient.http.client import HTTPClient
from gfwapiclient.http.endpoints.base import BaseEndPoint
from gfwapiclient.http.models.request import _RequestBodyT, _RequestParamsT
from gfwapiclient.http.models.response import _ResultItemT, _ResultT


__all__ = ["PostEndPoint"]


class PostEndPoint(
    BaseEndPoint[_RequestParamsT, _RequestBodyT, _ResultItemT, _ResultT],
):
    """Post API resource endpoint.

    This class extends `BaseEndPoint` to provide functionality for making `POST` requests to API endpoints.
    It encapsulates the logic for handling POST requests, including request preparation and response processing.
    """

    def __init__(
        self,
        *,
        path: str,
        request_params: Optional[_RequestParamsT],
        request_body: Optional[_RequestBodyT],
        result_item_class: Type[_ResultItemT],
        result_class: Type[_ResultT],
        http_client: HTTPClient,
    ) -> None:
        """Initialize a new `PostEndPoint`.

        Args:
            path (str):
                The relative path of the API endpoint.

            request_params (Optional[_RequestParamsT]):
                Query parameters for the POST request.

            request_body (Optional[_RequestBodyT]):
                The request body for the POST request.

            result_item_class (Type[_ResultItemT]):
                Pydantic model for the expected response item.

            result_class (Type[_ResultT]):
                Pydantic model for the expected response result.

            http_client (HTTPClient):
                The HTTP client to send requests.
        """
        super().__init__(
            method=http.HTTPMethod.POST,
            path=path,
            request_params=request_params,
            request_body=request_body,
            result_item_class=result_item_class,
            result_class=result_class,
            http_client=http_client,
        )
