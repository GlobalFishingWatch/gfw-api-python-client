"""Global Fishing Watch (GFW) API Python Client - Event Detail API Request Models."""

from pydantic import Field

from gfwapiclient.http.models import RequestParams
from gfwapiclient.resources.events.base.enums import (
    EventDataset,
)


__all__ = ["EventDetailParams"]


class EventDetailParams(RequestParams):
    """Request query parameters for get event by id API endpoint."""

    dataset: EventDataset = Field(
        ...,
        serialization_alias="dataset",
        description="Dataset that will be used to search the vessel event.",
    )
    # raw: Optional[bool] = Field(
    #     False,
    #     description="Whether to return all content of the event without parsing.",
    # )
