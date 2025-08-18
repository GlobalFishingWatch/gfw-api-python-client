"""Global Fishing Watch (GFW) API Python Client - Client."""

import os

from typing import Any, Final, Optional, Union

import httpx

from gfwapiclient.http import HTTPClient
from gfwapiclient.resources import (
    DatasetResource,
    EventResource,
    FourWingsResource,
    InsightResource,
    ReferenceResource,
    VesselResource,
)


__all__ = ["Client"]


GFW_API_BASE_URL: Final[str] = "https://gateway.api.globalfishingwatch.org/v3/"


class Client:
    """Global Fishing Watch (GFW) API Client.

    This class serves as the main entry point for interacting with the GFW API.
    It encapsulates the HTTP client and resources, providing a unified interface
    for accessing GFW's data.

    For more details on the GFW API and available data, please refer to the
    official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#introduction

    See: https://globalfishingwatch.org/our-apis/documentation#data-available

    See: https://globalfishingwatch.org/our-apis/documentation#data-caveat

    Attributes:
        fourwings (FourWingsResource):
            Access to the 4Wings data API resources.

        vessels (VesselResource):
            Access to the Vessels data API resources.

        events (EventResource):
            Access to the Events data API resources.

        insights (InsightResource):
            Access to the vessel insights data resources.

        datasets (DatasetResource):
            Access to the datasets data resources.

        references (ReferenceResource):
            Access to the reference data resources.
    """

    _fourwings: FourWingsResource
    _vessels: VesselResource
    _events: EventResource
    _insights: InsightResource
    _datasets: DatasetResource
    _references: ReferenceResource

    def __init__(
        self,
        *,
        access_token: Optional[str] = None,
        base_url: Optional[str] = None,
        follow_redirects: Optional[bool] = True,
        timeout: Optional[float] = 60.0,
        connect_timeout: Optional[float] = 5.0,
        max_connections: Optional[int] = 100,
        max_keepalive_connections: Optional[int] = 20,
        max_redirects: Optional[int] = 2,
        **kwargs: Any,
    ) -> None:
        """Initializes a new Global Fishing Watch (GFW) API `Client` with specified configurations.

        Args:
            base_url (Optional[Union[str, httpx.URL]], default="https://gateway.api.globalfishingwatch.org/v3/"):
                The base URL for API requests. If not provided, the value is taken from
                the `GFW_API_BASE_URL` environment variable. Default to `"https://gateway.api.globalfishingwatch.org/v3/"`.

            access_token (Optional[str], default=None):
                The access token for API request authentication. If not provided, the value is taken from
                the `GFW_API_ACCESS_TOKEN` environment variable. Raises `AccessTokenError` if neither is set.

            follow_redirects (Optional[bool], default=True):
                Whether the client should automatically follow redirects.
                Defaults to `True`.

            timeout (Optional[float], default=60.0):
                The default timeout (in seconds) for all operations (`connect`, `read`, `pool`, etc.).
                Defaults to `60.0` seconds.

            connect_timeout (Optional[float], default=5.0):
                Timeout (in seconds) for establishing a connection.
                Defaults to `5.0` seconds.

            max_connections (Optional[int], default=100):
                Maximum number of concurrent connections.
                Defaults to `100`.

            max_keepalive_connections (Optional[int], default=20):
                Maximum number of keep-alive connections in the connection pool.
                Should not exceed `max_connections`. Defaults to `20`.

            max_redirects (Optional[int], default=2):
                Maximum number of redirects to follow before raising an error.
                Defaults to `2`.

            **kwargs (Any):
                Additional parameters passed to `httpx.AsyncClient`.

        Raises:
            AccessTokenError:
                If `access_token` is not provided and the `GFW_API_ACCESS_TOKEN` environment
                variable is also not set.
        """
        # Ensure a base URL is set, either via argument or environment variable
        # or use default.
        _base_url: Union[str, httpx.URL] = (
            base_url
            if base_url is not None
            else os.environ.get(
                "GFW_API_BASE_URL",
                GFW_API_BASE_URL,
            )
        )

        self._http_client = HTTPClient(
            base_url=_base_url,
            access_token=access_token,
            follow_redirects=follow_redirects,
            timeout=timeout,
            connect_timeout=connect_timeout,
            max_connections=max_connections,
            max_keepalive_connections=max_keepalive_connections,
            max_redirects=max_redirects,
            **kwargs,
        )

    @property
    def fourwings(self) -> FourWingsResource:
        """4Wings data API resource.

        Provides access to the 4Wings API resources, which allow users to retrieve
        reports on AIS apparent fishing effort, AIS vessel presence and SAR vessel detections.

        For more details on the 4Wings API, please refer to the official
        Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#map-visualization-4wings-api

        Returns:
            FourWingsResource:
                The 4Wings data resource instance.
        """
        if not hasattr(self, "_fourwings"):
            self._fourwings = FourWingsResource(http_client=self._http_client)
        return self._fourwings

    @property
    def vessels(self) -> VesselResource:
        """Vessels data API resource.

        Provides access to the Vessels API resources, which allow users to search for
        and retrieve information about vessels using various criteria.

        For more details on the Vessels API, please refer to the official
        Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#vessels-api

        Returns:
            VesselResource:
                The Vessels data resource instance.
        """
        if not hasattr(self, "_vessels"):
            self._vessels = VesselResource(http_client=self._http_client)
        return self._vessels

    @property
    def events(self) -> EventResource:
        """Events data API resource.

        Provides access to the Events API resources, which allow users to retrieve
        information about various vessel activities.

        For more details on the Events API, refer to the official
        Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#events-api

        Returns:
            EventResource:
                The Events data resource instance.
        """
        if not hasattr(self, "_events"):
            self._events = EventResource(http_client=self._http_client)
        return self._events

    @property
    def insights(self) -> InsightResource:
        """Insights data API resource.

        Provides access to the Insights API resources, which allow users to retrieve
        insights data for specified vessels.

        For more details on the Insights API, please refer to the official
        Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#insights-api

        Returns:
            InsightResource:
                The insights data resource instance.
        """
        if not hasattr(self, "_insights"):
            self._insights = InsightResource(http_client=self._http_client)
        return self._insights

    @property
    def datasets(self) -> DatasetResource:
        """Datasets data API resource.

        Provides access to the Datasets API resources, which allow users to
        retrieve SAR fixed infrastructure data and other datasets.

        For more details on the Datasets API, please refer to the official
        Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#datasets-api>

        Returns:
            DatasetResource:
                The datasets data resource instance.
        """
        if not hasattr(self, "_datasets"):
            self._datasets = DatasetResource(http_client=self._http_client)
        return self._datasets

    @property
    def references(self) -> ReferenceResource:
        """References data API resource.

        Provides access to the reference data resources, specifically regions.

        Regions provide geographic data, such as Exclusive Economic Zones (EEZs),
        Marine Protected Areas (MPAs), and Regional Fisheries Management
        Organizations (RFMOs).

        For more details on the Regions API, please refer to the official
        Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#regions

        Returns:
            ReferenceResource:
                The reference data resource instance.
        """
        if not hasattr(self, "_references"):
            self._references = ReferenceResource(http_client=self._http_client)
        return self._references
