"""Global Fishing Watch (GFW) API Python Client - Get All Events API Endpoint."""

from typing import Any, Dict, List, Union

from typing_extensions import override

from gfwapiclient.exceptions.validation import ResultValidationError
from gfwapiclient.http.client import HTTPClient
from gfwapiclient.http.endpoints import PostEndPoint
from gfwapiclient.resources.events.list.models.request import (
    EventListBody,
    EventListParams,
)
from gfwapiclient.resources.events.list.models.response import (
    EventListItem,
    EventListResult,
)


__all__ = ["EventListEndPoint"]


class EventListEndPoint(
    PostEndPoint[EventListParams, EventListBody, EventListItem, EventListResult]
):
    """Get All Events API endpoint.

    This endpoint allows you to retrieve a list of events based on specified
    request parameters and body.
    """

    def __init__(
        self,
        *,
        request_params: EventListParams,
        request_body: EventListBody,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `EventListEndPoint` API endpoint.

        Args:
            request_params (EventListParams):
                The request parameters.

            request_body (EventListBody):
                The request body.

            http_client (HTTPClient):
                The HTTP client.
        """
        super().__init__(
            path="events",
            request_params=request_params,
            request_body=request_body,
            result_item_class=EventListItem,
            result_class=EventListResult,
            http_client=http_client,
        )

    @override
    def _transform_response_data(
        self,
        *,
        body: Union[List[Dict[str, Any]], Dict[str, Any]],
    ) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        """Transforms and reshapes the response body to extract event data.

        The API response contains event data within an "entries" list.
        This method extracts and returns the event data from this list.

        Args:
            body (Union[List[Dict[str, Any]], Dict[str, Any]]):
                The response body from the API.

        Returns:
            Union[List[Dict[str, Any]], Dict[str, Any]]:
                The transformed event data.

        Raises:
            ResultValidationError:
                If the response body does not contain the expected "entries" list.
        """
        # expected: {entries: [{"key": ...}, ...]}
        if not isinstance(body, dict) or "entries" not in body:
            raise ResultValidationError(
                message="Expected a list of entries, but got an empty list.",
                body=body,
            )

        # Transforming and reshaping entries
        event_entries: List[Dict[str, Any]] = body.get("entries", [])
        transformed_data: List[Dict[str, Any]] = []

        # Loop through "entries" list i.e [{"key": ...}, ...]}
        for event_entry in event_entries:
            # Append extracted event entry, if not empty
            if event_entry:
                transformed_data.append(dict(**event_entry))

        return transformed_data
