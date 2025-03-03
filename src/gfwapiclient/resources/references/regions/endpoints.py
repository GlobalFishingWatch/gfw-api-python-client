"""Global Fishing Watch (GFW) API Python Client - Region API EndPoints."""

from gfwapiclient.http.client import HTTPClient
from gfwapiclient.http.endpoint import GetEndPoint
from gfwapiclient.http.models import RequestBody, RequestParams
from gfwapiclient.resources.references.regions.models import (
    EEZRegionItem,
    EEZRegionResult,
    MPARegionItem,
    MPARegionResult,
    RFMORegionItem,
    RFMORegionResult,
)


__all__ = ["EEZRegionEndPoint"]


class EEZRegionEndPoint(
    GetEndPoint[RequestParams, RequestBody, EEZRegionItem, EEZRegionResult],
):
    """Get Exclusive Economic Zone (EEZ) regions API endpoint."""

    def __init__(
        self,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `EEZRegionEndPoint` API endpoint."""
        super().__init__(
            path="datasets/public-eez-areas/context-layers",
            request_params=None,
            result_item_class=EEZRegionItem,
            result_class=EEZRegionResult,
            http_client=http_client,
        )


class MPARegionEndPoint(
    GetEndPoint[RequestParams, RequestBody, MPARegionItem, MPARegionResult],
):
    """Get Marine Protected Area (MPA) regions API endpoint."""

    def __init__(
        self,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `MPARegionEndPoint` API endpoint."""
        super().__init__(
            path="datasets/public-mpa-all/context-layers",
            request_params=None,
            result_item_class=MPARegionItem,
            result_class=MPARegionResult,
            http_client=http_client,
        )


class RFMORegionEndPoint(
    GetEndPoint[RequestParams, RequestBody, RFMORegionItem, RFMORegionResult],
):
    """Get Regional Fisheries Management Organization (RFMO) regions API endpoint."""

    def __init__(
        self,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `RFMORegionEndPoint` API endpoint."""
        super().__init__(
            path="datasets/public-rfmo/context-layers",
            request_params=None,
            result_item_class=RFMORegionItem,
            result_class=RFMORegionResult,
            http_client=http_client,
        )
