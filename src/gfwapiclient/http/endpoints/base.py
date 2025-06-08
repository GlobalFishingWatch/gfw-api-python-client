"""Global Fishing Watch (GFW) API Python Client - Base HTTP EndPoint."""

import http
import json
import logging

from typing import Any, Dict, List, Optional, Type, Union

import httpx
import mapbox_vector_tile
import pydantic

from typing_extensions import override

from gfwapiclient.exceptions.http import (
    APIConnectionError,
    APIStatusError,
    APITimeoutError,
    AuthenticationError,
    BadGatewayError,
    BadRequestError,
    ConflictError,
    GatewayTimeoutError,
    InternalServerError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    RequestTimeoutError,
    ServiceUnavailableError,
    UnprocessableEntityError,
)
from gfwapiclient.exceptions.validation import (
    ResultItemValidationError,
    ResultValidationError,
)
from gfwapiclient.http.client import HTTPClient
from gfwapiclient.http.endpoints.abc import AbstractBaseEndPoint
from gfwapiclient.http.models.request import _RequestBodyT, _RequestParamsT
from gfwapiclient.http.models.response import _ResultItemT, _ResultT


__all__ = ["BaseEndPoint"]

log: logging.Logger = logging.getLogger(__name__)


class BaseEndPoint(
    AbstractBaseEndPoint[_RequestParamsT, _RequestBodyT, _ResultItemT, _ResultT]
):
    """Base class for an API resource endpoint implementing request handling.

    This class handles:
        - Building the endpoint request.
        - Sending the request to the API endpoint.
        - Parsing, transforming, and casting successful response data to a result.
        - Parsing, transforming, and casting error responses to errors.
    """

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
        """Initialize a new `BaseEndPoint`.

        Args:
            method (http.HTTPMethod):
                The HTTP method used by the endpoint (e.g., GET, POST, PUT, DELETE).

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
        super().__init__(
            method=method,
            path=path,
            request_params=request_params,
            request_body=request_body,
            result_item_class=result_item_class,
            result_class=result_class,
            http_client=http_client,
        )

    @override
    async def request(self, **kwargs: Any) -> _ResultT:
        """Send an HTTP request for this endpoint.

        Args:
            **kwargs (Any):
                Additional keyword arguments to pass to the `httpx.Client.send()` method.

        Returns:
            _ResultT:
                The result of the API request as a `_ResultT` instance.
        """
        return await self._request(**kwargs)

    async def _request(self, **kwargs: Any) -> _ResultT:
        """Perform request-response flow for this endpoint.

        Args:
            **kwargs (Any):
                Additional keyword arguments to pass to the `httpx.Client.send()` method.

        Returns:
            _ResultT:
                The result of the API request as a `_ResultT` instance.

        Raises:
            APITimeoutError:
                If the request times out.

            APIConnectionError:
                If a connection error occurs.

            APIStatusError:
                If the API returns an HTTP status error.
        """
        request: httpx.Request = self._build_request()
        log.debug("Request: %s", request)

        try:
            response: httpx.Response = await self._http_client.send(request, **kwargs)
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
        except httpx.HTTPStatusError as exc:
            log.debug("Encountered httpx.HTTPStatusError", exc_info=True)
            raise self._process_api_status_error(response=exc.response) from None

        return self._process_response_data(response=response)

    def _process_response_data(self, *, response: httpx.Response) -> _ResultT:
        """Parse, transform and cast response data.

        Args:
            response (httpx.Response):
                The `httpx.Response` object to process.

        Returns:
            _ResultT:
                The processed response data as a `_ResultT` instance.

        Raises:
            ResultValidationError:
                If the response's Content-Type is invalid.

            ResultItemValidationError:
                If the response data cannot be casted to the `_ResultItemT` model.
        """
        parsed_data: Union[List[Dict[str, Any]], Dict[str, Any]] = (
            self._parse_response_data(response=response)
        )
        transformed_data: Union[List[Dict[str, Any]], Dict[str, Any]] = (
            self._transform_response_data(body=parsed_data)
        )
        casted_data: Union[List[_ResultItemT], _ResultItemT] = self._cast_response_data(
            body=transformed_data, response=response
        )
        result: _ResultT = self._build_api_result(data=casted_data)
        return result

    def _parse_response_data(
        self, *, response: httpx.Response
    ) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        """Parse response and return data.

        Args:
            response (httpx.Response):
                The `httpx.Response` object to parse.

        Returns:
            Union[List[Dict[str, Any]], Dict[str, Any]]:
                The parsed response data as a dictionary or a list of dictionaries.

        Raises:
            ResultValidationError:
                If the response's Content-Type is invalid or unsupported.
        """
        content_type, *_ = response.headers.get("content-type", "*").split(";")
        match content_type:
            case "application/json":
                return self._parse_response_json_data(response=response)
            case "application/vnd.mapbox-vector-tile":
                return self._parse_response_mvt_data(response=response)
            case _:
                raise ResultValidationError(
                    message=f"Expected Content-Type response header to be `application/json` or `application/vnd.mapbox-vector-tile` but received `{content_type}` instead.",
                    response=response,
                    body=response.text,
                )

    def _parse_response_json_data(
        self, *, response: httpx.Response
    ) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        """Parse JSON response and return data.

        Args:
            response (httpx.Response):
                The `httpx.Response` object to parse.

        Returns:
            Union[List[Dict[str, Any]], Dict[str, Any]]:
                The parsed JSON response data as a dictionary or a list of
                dictionaries.
        """
        parsed_data: Union[List[Dict[str, Any]], Dict[str, Any]] = response.json()
        return parsed_data

    def _parse_response_mvt_data(
        self, *, response: httpx.Response
    ) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        """Parse Mapbox Vector Tile (MVT) response and return data.

        Args:
            response (httpx.Response):
                The `httpx.Response` object containing MVT data to parse.

        Returns:
            Union[List[Dict[str, Any]], Dict[str, Any]]:
                The parsed response data as a list of dictionaries,
                where each dictionary represents feature properties.
        """
        try:
            tile: Dict[str, Any] = mapbox_vector_tile.decode(response.content)
            features: List[Dict[str, Any]] = tile.get("main", {}).get("features", [])
            parsed_data: Union[List[Dict[str, Any]], Dict[str, Any]] = [
                feature.get("properties", {}) for feature in features
            ]
            return parsed_data
        except Exception as exc:
            raise ResultValidationError(
                message="Failed to decode Mapbox Vector Tile data.",
                response=response,
                body=response.content,
            ) from exc

    def _transform_response_data(
        self, *, body: Union[List[Dict[str, Any]], Dict[str, Any]]
    ) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        """Transform and reshape response body and return data.

        Args:
            body (Union[List[Dict[str, Any]], Dict[str, Any]]):
                The parsed response body to transform.

        Returns:
            Union[List[Dict[str, Any]], Dict[str, Any]]:
                The transformed response body as a dictionary or a list of dictionaries.
        """
        return body

    def _cast_response_data(
        self,
        *,
        body: Union[List[Dict[str, Any]], Dict[str, Any]],
        response: httpx.Response,
    ) -> Union[List[_ResultItemT], _ResultItemT]:
        """Cast response body and return result item.

        Args:
            body (Union[List[Dict[str, Any]], Dict[str, Any]]):
                The transformed response body to cast.

            response (httpx.Response):
                The `httpx.Response` object.

        Returns:
            Union[List[_ResultItemT], _ResultItemT]:
                The casted response data as a `_ResultItemT` or a list of `_ResultItemT`.

        Raises:
            ResultItemValidationError:
                If the response data cannot be casted to the `_ResultItemT` model.
        """
        try:
            return (
                [self._result_item_class(**data) for data in body]
                if isinstance(body, list)
                else self._result_item_class(**body)
            )
        except pydantic.ValidationError as exc:
            raise ResultItemValidationError(
                error=exc,
                response=response,
                body=body,
            ) from exc

    def _build_api_result(
        self, *, data: Union[List[_ResultItemT], _ResultItemT]
    ) -> _ResultT:
        """Build and return result for this API endpoint.

        Args:
            data (Union[List[_ResultItemT], _ResultItemT]):
                The casted response data.

        Returns:
            _ResultT:
                The result of the API request as a `_ResultT` instance.
        """
        return self._result_class(data=data)

    def _process_api_status_error(self, *, response: httpx.Response) -> APIStatusError:
        """Processes raised HTTP status error.

        This function:
            - Parses response data from raised HTTP status error.
            - Transforms it to text or JSON.
            - Casts the raised HTTP status error to a specific `APIStatusError` subclass.

        Args:
            response (httpx.Response):
                The `httpx.Response` object representing the error response.

        Returns:
            APIStatusError:
                An `APIStatusError` instance representing the error.
        """
        if response.is_closed and not response.is_stream_consumed:
            body: Any = None
            error_message: str = f"Error code: {response.status_code}"
        else:
            error_text: Any = response.text.strip()
            body = error_text
            try:
                body = json.loads(error_text)
                error_message = f"Error code: {response.status_code} - {body}"
            except Exception:
                error_message = error_text or f"Error code: {response.status_code}"

        return self._cast_api_status_error(
            error_message=error_message, body=body, response=response
        )

    def _cast_api_status_error(
        self, *, error_message: str, body: Any, response: httpx.Response
    ) -> APIStatusError:
        """Converts raised HTTP status error to specific `APIStatusError`.

        Args:
            error_message (str):
                The error message.

            body (Any):
                The error body.

            response (httpx.Response):
                The `httpx.Response` object representing the error response.

        Returns:
            APIStatusError:
                An `APIStatusError` instance representing the error.
        """
        match response.status_code:
            case 400:
                return BadRequestError(error_message, response=response, body=body)
            case 401:
                return AuthenticationError(error_message, response=response, body=body)
            case 403:
                return PermissionDeniedError(
                    error_message, response=response, body=body
                )
            case 404:
                return NotFoundError(error_message, response=response, body=body)
            case 408:
                return RequestTimeoutError(error_message, response=response, body=body)
            case 409:
                return ConflictError(error_message, response=response, body=body)
            case 422:
                return UnprocessableEntityError(
                    error_message, response=response, body=body
                )
            case 429:
                return RateLimitError(error_message, response=response, body=body)
            case 500:
                return InternalServerError(error_message, response=response, body=body)
            case 502:
                return BadGatewayError(error_message, response=response, body=body)
            case 503:
                return ServiceUnavailableError(
                    error_message, response=response, body=body
                )
            case 504:
                return GatewayTimeoutError(error_message, response=response, body=body)
            case _:
                return APIStatusError(error_message, response=response, body=body)
