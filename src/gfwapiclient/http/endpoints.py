"""Global Fishing Watch (GFW) API Python Client - HTTP EndPoint."""

import http
import json
import logging

from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, List, Optional, Type, Union, override

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

    def _prepare_request_path(self) -> str:
        """Prepare endpoint `path` to be used for the request."""
        _path = self._path
        return _path

    def _prepare_request_url(self) -> httpx.URL:
        """Prepare HTTP url to be used for the request.

        This merge a endpoint `path` together with `HTTPClient` 'base_url',
        to create the URL used for the outgoing request.
        """
        _path = self._prepare_request_path()
        _url = self._http_client._merge_url(_path)
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

    def _parse_response_body(
        self,
        response: httpx.Response,
    ) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        """Parse response and yield data."""
        # TODO: _parse_response_data
        # TODO: _parse_response_json_data
        content_type, *_ = response.headers.get("content-type", "*").split(";")
        if content_type != "application/json":
            raise APIResponseValidationError(
                response=response,
                message=f"Expected Content-Type response header to be `application/json` but received `{content_type}` instead.",
                body=response.text,
            )
        # TODO: set _update_pagination_params [attr, value]
        _parsed_data: Union[List[Dict[str, Any]], Dict[str, Any]] = response.json()
        return _parsed_data

    def _transform_response_body(
        self,
        body: Union[List[Dict[str, Any]], Dict[str, Any]],
    ) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        """Transform and reshape response body and yield data."""
        # TODO: _transform_response_data
        # TODO: handle single item and list data
        # TODO: handle single item with list data [i.e entries]
        return body

    def _cast_response_body(
        self,
        body: Union[List[Dict[str, Any]], Dict[str, Any]],
    ) -> Union[List[_ResultItemT], _ResultItemT]:
        """Cast response body and yield result item."""
        # _cast_response_data
        _casted_data = (
            [self._result_item_class(**data) for data in body]
            if isinstance(body, list)
            else self._result_item_class(**body)
        )
        return _casted_data

    def _build_result(self, data: Union[List[_ResultItemT], _ResultItemT]) -> _ResultT:
        """Build and return a `_ResultT` instance for this endpoint."""
        # _build_response_result
        return self._result_class(data=data)

    @abstractmethod
    def _process_response(self, response: httpx.Response) -> _ResultT:
        """Process `httpx.Response` instance and return `_ResultT` for this endpoint."""
        # TODO: _process_response_data
        # TODO: _process_response_error [_parse_response_error, _transform_response_error, _cast_response_error, _cast_api_status_error|_cast_status_error]
        # TODO: _process_response_error [_parse_response_error_data, _transform_response_error_data, _cast_response_error_data]
        # TODO: _parse_response_body -> _transform_response_body -> _cast_response_body -> _build_result
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
        # TODO: _process_request
        # TODO: handle pagination properly
        request = self._build_request()
        try:
            response = await self._http_client.send(
                request,
                **kwargs,
            )
        except httpx.TimeoutException as exc:
            # TODO: InvalidURL (URL is improperly formed or cannot be parsed.)
            # TODO: RequestError (all exceptions that may occur when issuing a `.request()`.)
            # TODO: TransportError (all exceptions that occur at the level of the Transport API.)
            # TODO: TimeoutException* (timeout errors. An operation has timed out.)
            # TODO: NetworkError (network-related errors. An error occurred while interacting with the network.)
            # TODO: ConnectError (Failed to establish a connection.)
            log.debug("Encountered httpx.TimeoutException", exc_info=True)
            raise APITimeoutError(request=request) from exc
        except Exception as exc:
            log.debug("Encountered Exception", exc_info=True)
            raise APIConnectionError(request=request) from exc

        # TODO: improve request, response [request_id]
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
            # TODO: HTTPStatusError (response had an error HTTP status of 4xx or 5xx.)
            log.debug("Encountered httpx.HTTPStatusError", exc_info=True)
            raise self._process_response_error(exc.response) from None

        return self._process_response(response=response)

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

    @override
    def _process_response(
        self,
        response: httpx.Response,
    ) -> _ResultT:
        """Parse and cast response data."""
        _parsed_data = self._parse_response_body(response=response)
        try:
            _transformed_data = self._transform_response_body(body=_parsed_data)
            _casted_data = self._cast_response_body(body=_transformed_data)
            result = self._build_result(data=_casted_data)
            return result
        except pydantic.ValidationError as exc:
            # TODO: handle custom APIResultValidationError | APIResultItemValidationError | APIResponseDataError
            raise APIResponseValidationError(
                response=response, body=_parsed_data
            ) from exc

    def _process_response_error(
        self,
        response: httpx.Response,
    ) -> APIStatusError:
        """Parse error response status errors."""
        # TODO: _process_response_error [_cast_response_status_error]
        if response.is_closed and not response.is_stream_consumed:
            # We can't read the response body as it has been closed
            body = None
            err_msg = f"Error code: {response.status_code}"
        else:
            err_text = response.text.strip()
            body = err_text
            # TODO: handle HTML responses

            try:
                body = json.loads(err_text)
                err_msg = f"Error code: {response.status_code} - {body}"
            except Exception:
                # TODO: log
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
