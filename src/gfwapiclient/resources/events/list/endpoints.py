"""Global Fishing Watch (GFW) API Python Client - Events List API EndPoint."""

from typing import Any, Dict, List, Union, override

import pydantic

from pydantic_core import ErrorDetails

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
    PostEndPoint[
        EventListParams,
        EventListBody,
        EventListItem,
        EventListResult,
    ],
):
    """Get list of events API endpoint."""

    def __init__(
        self,
        request_params: EventListParams,
        request_body: EventListBody,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `EventListEndPoint` API endpoint."""
        super().__init__(
            path="events",
            request_params=request_params,
            request_body=request_body,
            result_item_class=EventListItem,
            result_class=EventListResult,
            http_client=http_client,
        )

    @override
    def _transform_response_body(
        self,
        body: Union[List[Dict[str, Any]], Dict[str, Any]],
    ) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        """Transform and reshape response body and yield data."""
        # expected: {entries: [{"key": [{}]}]}
        if not isinstance(body, dict) or "entries" not in body:
            # TODO: raise APIResponseDataError | APIResultItemValidationError | APIResultValidationError
            errors = [
                ErrorDetails(
                    type="value_error",
                    loc=("entries",),
                    msg="Expected a list of entries, but got an empty list.",
                    input=None,
                )
            ]
            raise pydantic.ValidationError(errors, EventListResult)

        # TODO: update pagination options|params(since:str, limit:int)

        # Transforming and reshaping entries
        event_entries: List[Dict[str, Any]] = body.get("entries", [])
        transformed_data: List[Dict[str, Any]] = []

        # Loop through "entries" list i.e {"entries": [{"dataset": [{...}]}]}
        for event_entry in event_entries:
            # Append extracted dictionaries
            transformed_data.append(event_entry)

        return transformed_data
