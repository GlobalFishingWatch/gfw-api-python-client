"""Global Fishing Watch (GFW) API Python Client - Regions API endpoints."""

from gfwapiclient.http.client import HTTPClient
from gfwapiclient.http.endpoints import GetEndPoint
from gfwapiclient.http.models import RequestBody, RequestParams
from gfwapiclient.resources.references.regions.models.response import (
    EEZRegionItem,
    EEZRegionResult,
    MPARegionItem,
    MPARegionResult,
    RFMORegionItem,
    RFMORegionResult,
)


__all__ = ["EEZRegionEndPoint", "MPARegionEndPoint", "RFMORegionEndPoint"]


class EEZRegionEndPoint(
    GetEndPoint[RequestParams, RequestBody, EEZRegionItem, EEZRegionResult],
):
    """Get Exclusive Economic Zone (EEZ) regions API endpoint.

    This endpoint retrieves a list of Exclusive Economic Zone (EEZ) regions.

    For more details on the EEZ regions API endpoint, please refer to the official
    Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#regions
    """

    def __init__(
        self,
        *,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `EEZRegionEndPoint`.

        Args:
            http_client (HTTPClient):
                The HTTP client to send requests.
        """
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
    """Get Marine Protected Area (MPA) regions API endpoint.

    This endpoint retrieves a list of Marine Protected Area (MPA) regions.

    For more details on the MPA regions API endpoint, please refer to the official
    Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#regions
    """

    def __init__(
        self,
        *,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `MPARegionEndPoint`.

        Args:
            http_client (HTTPClient):
                The HTTP client to send requests.
        """
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
    """Get Regional Fisheries Management Organization (RFMO) regions API endpoint.

    This endpoint retrieves a list of Regional Fisheries Management Organization (RFMO) regions.

    For more details on the RFMO regions API endpoint, please refer to the official
    Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#regions
    """

    def __init__(
        self,
        *,
        http_client: HTTPClient,
    ) -> None:
        """Initializes a new `RFMORegionEndPoint`.

        Args:
            http_client (HTTPClient):
                The HTTP client to send requests.
        """
        super().__init__(
            path="datasets/public-rfmo/context-layers",
            request_params=None,
            result_item_class=RFMORegionItem,
            result_class=RFMORegionResult,
            http_client=http_client,
        )
