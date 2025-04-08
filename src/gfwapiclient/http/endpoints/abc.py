"""Global Fishing Watch (GFW) API Python Client - Abstract Base HTTP EndPoint."""

import http

from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, Optional, Type

import httpx

from gfwapiclient.http.client import HTTPClient
from gfwapiclient.http.models.request import _RequestBodyT, _RequestParamsT
from gfwapiclient.http.models.response import _ResultItemT, _ResultT


__all__ = ["AbstractBaseEndPoint"]


class AbstractBaseEndPoint(
    ABC, Generic[_RequestParamsT, _RequestBodyT, _ResultItemT, _ResultT]
):
    """Abstract base class for an API resource endpoint.

    Provides a structured way to define API endpoints and their result format.

    This class handles:
        - Preparing request method, URL, headers, query parameters, and JSON body.
        - Building the HTTP request.
    """

    _request_params_class: Type[_RequestParamsT]
    _request_body_class: Type[_RequestBodyT]
    _result_item_class: Type[_ResultItemT]
    _result_class: Type[_ResultT]

    def __init__(
        self,
        *,
        method: http.HTTPMethod,
        path: str,
        request_params: Optional[_RequestParamsT],
        request_body: Optional[_RequestBodyT],
        result_item_class: Type[_ResultItemT],
        result_class: Type[_ResultT],
        http_client: HTTPClient,
    ) -> None:
        """Initialize an API endpoint.

        Args:
            method (http.HTTPMethod):
                The HTTP method used by the endpoint.

            path (str):
                The relative path of the API endpoint.

            request_params (Optional[_RequestParamsT]):
                Query parameters for the request.

            request_body (Optional[_RequestBodyT]):
                The request body.

            result_item_class (Type[_ResultItemT]):
                Pydantic model for the expected response item.

            result_class (Type[_ResultT]):
                Pydantic model for the expected response result.

            http_client (HTTPClient):
                The HTTP client to send requests.
        """
        self._method = method
        self._path = path
        self._request_params = request_params
        self._request_body = request_body
        self._result_item_class = result_item_class
        self._result_class = result_class
        self._http_client = http_client

    @property
    def headers(self) -> Dict[str, str]:
        """Custom endpoint request headers.

        Returns:
            Dict[str, str]:
                A dictionary containing custom headers for the request.
        """
        return {}

    def _prepare_request_method(self) -> str:
        """Prepare the endpoint's HTTP method (e.g., GET, POST, PUT, DELETE) for the request.

        Returns:
            str:
                The endpoint's HTTP method as a string.
        """
        return self._method.value

    def _prepare_request_path(self) -> str:
        """Prepare the endpoint's path for the request.

        Returns:
            str:
                The endpoint's path as a string.
        """
        return self._path

    def _prepare_request_url(self) -> httpx.URL:
        """Prepare the endpoint's full HTTP URL for the request.

        Merges the endpoint's path with the HTTPClient's `base_url` to create the request URL.

        Returns:
            httpx.URL:
                The endpoint's full HTTP URL as an `httpx.URL` object.
        """
        return self._http_client._merge_url(self._prepare_request_path())

    def _prepare_request_headers(self) -> httpx.Headers:
        """Prepare the endpoint's HTTP request headers for the request.

        Returns:
            httpx.Headers:
                The endpoint's HTTP request headers as an `httpx.Headers` object.
        """
        return httpx.Headers(self._http_client._merge_headers(dict(**self.headers)))

    def _prepare_request_query_params(self) -> Optional[httpx.QueryParams]:
        """Prepare the endpoint's HTTP request query parameters for the request.

        Returns:
            Optional[httpx.QueryParams]:
                The endpoint's HTTP request query parameters as an `httpx.QueryParams` object,
                or `None` if no query parameters are present.
        """
        if self._request_params:
            return httpx.QueryParams(self._request_params.to_query_params())
        return None

    def _prepare_request_json_body(self) -> Optional[Dict[str, Any]]:
        """Prepare HTTP request JSON body for the request."""
        if self._request_body:
            return self._request_body.to_json_body()
        return None

    def _build_request(self) -> httpx.Request:
        """Build and return an `httpx.Request` instance for this endpoint.

        Returns:
            httpx.Request:
                An `httpx.Request` instance representing the HTTP request.
        """
        method: str = self._prepare_request_method()
        url: httpx.URL = self._prepare_request_url()
        json: Optional[Dict[str, Any]] = self._prepare_request_json_body()
        params: Optional[httpx.QueryParams] = self._prepare_request_query_params()
        headers: httpx.Headers = self._prepare_request_headers()

        request: httpx.Request = self._http_client.build_request(
            method=method,
            url=url,
            json=json,
            params=params,
            headers=headers,
        )
        return request

    @abstractmethod
    async def request(self, **kwargs: Any) -> _ResultT:
        """Send an HTTP request for this endpoint.

        Args:
            **kwargs (Any):
                Additional keyword arguments to pass to the `httpx.Client.send()` method.

        Returns:
            _ResultT:
                The result of the API request as a `_ResultT` instance.
        """
        raise NotImplementedError()
