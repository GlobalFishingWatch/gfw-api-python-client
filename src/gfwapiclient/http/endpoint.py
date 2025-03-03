"""Global Fishing Watch (GFW) API Python Client - HTTP EndPoint."""

import http
import json
import logging

from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, Optional, Type, override

import httpx
import pydantic

from gfwapiclient.exceptions.base import (
    APIConnectionError,
    APIResponseValidationError,
    APIStatusError,
)
from gfwapiclient.exceptions.http import (
    APITimeoutError,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    UnprocessableEntityError,
)
from gfwapiclient.http.client import HTTPClient
from gfwapiclient.http.models import (
    _RequestBodyT,
    _RequestParamsT,
    _ResultItemT,
    _ResultT,
)


__all__ = ["BaseEndPoint"]

log: logging.Logger = logging.getLogger(__name__)


class AbstractBaseEndPoint(
    ABC,
    Generic[_RequestParamsT, _RequestBodyT, _ResultItemT, _ResultT],
):
    """Abstract base class for an API resource endpoint.

    It provides a structured way to define API endpoints with request handling capabilities.
    """

    _request_params_class: Type[_RequestParamsT]
    _request_body_class: Type[_RequestBodyT]
    _result_item_class: Type[_ResultItemT]
    _result_class: Type[_ResultT]

    def __init__(
        self,
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

            result_class (Type[_ResultItemT]):
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
        """Custom endpoint request headers."""
        return {}

    def _prepare_request_method(self) -> str:
        """Prepare HTTP method (i.e, GET, POST, PUT, DELETE, etc.) to be used for the request."""
        _method = self._method.value
        return _method

    def _prepare_request_url(self) -> httpx.URL:
        """Prepare HTTP url to be used for the request.

        This merge a endpoint `path` together with `HTTPClient` 'base_url',
        to create the URL used for the outgoing request.
        """
        _url = self._http_client._merge_url(self._path)
        return _url

    def _prepare_request_headers(self) -> httpx.Headers:
        """Prepare HTTP request headers to be used for the request."""
        _headers = self._http_client._merge_headers(dict(**self.headers))
        return httpx.Headers(_headers)

    def _prepare_request_query_params(self) -> Optional[httpx.QueryParams]:
        """Prepare HTTP request query parameters to be used for the request."""
        if self._request_params:
            _query_params = self._request_params.to_query_params()
            return httpx.QueryParams(dict(**_query_params))
        return None

    def _prepare_request_json_body(self) -> Optional[Dict[str, Any]]:
        """Prepare HTTP request json body to be used for the request."""
        if self._request_body:
            _json_body = self._request_body.to_json_body()
            return dict(**_json_body)
        return None

    @abstractmethod
    def _build_request(self) -> httpx.Request:
        """Build and return an `httpx.Request` instance for this endpoint."""
        raise NotImplementedError()


class BaseEndPoint(
    AbstractBaseEndPoint[_RequestParamsT, _RequestBodyT, _ResultItemT, _ResultT],
):
    """Base class for an API resource endpoint implementing request handling."""

    def __init__(
        self,
        method: http.HTTPMethod,
        path: str,
        request_params: Optional[_RequestParamsT],
        request_body: Optional[_RequestBodyT],
        result_item_class: Type[_ResultItemT],
        result_class: Type[_ResultT],
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `BaseEndPoint`."""
        super().__init__(
            method=method,
            path=path,
            request_params=request_params,
            request_body=request_body,
            result_item_class=result_item_class,
            result_class=result_class,
            http_client=http_client,
        )

    def request(
        self,
        **kwargs: Any,
    ) -> _ResultT:
        """Synchronously send an HTTP request for this endpoint."""
        # TODO: improve implementation
        coro = self.arequest(**kwargs)
        return self._http_client.event_loop.run_until_complete(coro)

    async def arequest(
        self,
        **kwargs: Any,
    ) -> _ResultT:
        """Asynchronously send an HTTP request for this endpoint."""
        return await self._request(**kwargs)

    async def _request(
        self,
        **kwargs: Any,
    ) -> _ResultT:
        """Perform request - response flow for this endpoint."""
        request = self._build_request()
        try:
            response = await self._http_client.send(
                request,
                **kwargs,
            )
        except httpx.TimeoutException as exc:
            log.debug("Encountered httpx.TimeoutException", exc_info=True)
            raise APITimeoutError(request=request) from exc
        except Exception as exc:
            log.debug("Encountered Exception", exc_info=True)
            raise APIConnectionError(request=request) from exc

        log.debug(
            'HTTP Request: %s %s "%i %s"',
            request.method,
            request.url,
            response.status_code,
            response.reason_phrase,
        )

        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:  # thrown on 4xx and 5xx status code
            log.debug("Encountered httpx.HTTPStatusError", exc_info=True)
            raise self._process_response_error(exc.response) from None

        # TODO: log response
        return self._process_response_data(response=response)

    @override
    def _build_request(self) -> httpx.Request:
        """Build and return an `httpx.Request` instance for this endpoint."""
        # Prepare request method, url, json body, query params, headers etc
        _method: str = self._prepare_request_method()
        _url: httpx.URL = self._prepare_request_url()
        _json_body: Optional[Dict[str, Any]] = self._prepare_request_json_body()
        _params: Optional[httpx.QueryParams] = self._prepare_request_query_params()
        _headers: httpx.Headers = self._prepare_request_headers()

        # Build http request
        _request = self._http_client.build_request(
            method=_method,
            url=_url,
            json=_json_body,
            params=_params,
            headers=_headers,
        )
        log.debug("Request: %s", _request)
        return _request

    def _process_response_data(
        self,
        response: httpx.Response,
    ) -> _ResultT:
        """Parse and cast response data."""
        content_type, *_ = response.headers.get("content-type", "*").split(";")
        if content_type != "application/json":
            raise APIResponseValidationError(
                response=response,
                message=f"Expected Content-Type response header to be `application/json` but received `{content_type}` instead.",
                body=response.text,
            )

        try:
            raw_data = response.json()
            # TODO: handle single item and list data
            # TODO: handle single item with list data [i.e entries]
            parsed_data = (
                [self._result_item_class(**rd) for rd in raw_data]
                if isinstance(raw_data, list)
                else self._result_item_class(**raw_data)
            )
            result = self._result_class(data=parsed_data)
            return result
        except pydantic.ValidationError as exc:
            raise APIResponseValidationError(response=response, body=raw_data) from exc

    def _process_response_error(
        self,
        response: httpx.Response,
    ) -> APIStatusError:
        """Parse error response status errors."""
        if response.is_closed and not response.is_stream_consumed:
            # We can't read the response body as it has been closed
            body = None
            err_msg = f"Error code: {response.status_code}"
        else:
            err_text = response.text.strip()
            body = err_text

            try:
                body = json.loads(err_text)
                err_msg = f"Error code: {response.status_code} - {body}"
            except Exception:
                err_msg = err_text or f"Error code: {response.status_code}"

        return self._make_api_status_error(err_msg, body=body, response=response)

    def _make_api_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        """Make `APIStatusError` from API response."""
        match response.status_code:
            case 400:
                return BadRequestError(err_msg, response=response, body=body)

            case 401:
                return AuthenticationError(err_msg, response=response, body=body)

            case 403:
                return PermissionDeniedError(err_msg, response=response, body=body)

            case 404:
                return NotFoundError(err_msg, response=response, body=body)

            case 409:
                return ConflictError(err_msg, response=response, body=body)

            case 422:
                return UnprocessableEntityError(err_msg, response=response, body=body)

            case 429:
                return RateLimitError(err_msg, response=response, body=body)

            case _:
                return APIStatusError(err_msg, response=response, body=body)


class GetEndPoint(
    BaseEndPoint[_RequestParamsT, _RequestBodyT, _ResultItemT, _ResultT],
):
    """Get API resource endpoint."""

    def __init__(
        self,
        path: str,
        request_params: Optional[_RequestParamsT],
        result_item_class: Type[_ResultItemT],
        result_class: Type[_ResultT],
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `GetEndPoint`."""
        super().__init__(
            http.HTTPMethod.GET,
            path=path,
            request_params=request_params,
            request_body=None,
            result_item_class=result_item_class,
            result_class=result_class,
            http_client=http_client,
        )


class PostEndPoint(
    BaseEndPoint[_RequestParamsT, _RequestBodyT, _ResultItemT, _ResultT],
):
    """Post API resource endpoint."""

    def __init__(
        self,
        path: str,
        request_params: Optional[_RequestParamsT],
        request_body: Optional[_RequestBodyT],
        result_item_class: Type[_ResultItemT],
        result_class: Type[_ResultT],
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `PostEndPoint`."""
        super().__init__(
            http.HTTPMethod.POST,
            path=path,
            request_params=request_params,
            request_body=request_body,
            result_item_class=result_item_class,
            result_class=result_class,
            http_client=http_client,
        )
