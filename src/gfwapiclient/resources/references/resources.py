"""Global Fishing Watch (GFW) API Python Client - References Data API Resource."""

from typing import Any, Dict

from gfwapiclient.http.resources import BaseResource
from gfwapiclient.resources.references.regions.endpoints import (
    EEZRegionEndPoint,
    MPARegionEndPoint,
    RFMORegionEndPoint,
)
from gfwapiclient.resources.references.regions.models.response import (
    EEZRegionResult,
    MPARegionResult,
    RFMORegionResult,
)


__all__ = ["ReferenceResource"]


class ReferenceResource(BaseResource):
    """References data API resource.

    This resource provides methods to interact with the Reference Data API,
    specifically to:

    - Retrieves a list of Exclusive Economic Zone (EEZ) regions.
    - Retrieves a list of Marine Protected Area (MPA) regions.
    - Retrieves a list of Regional Fisheries Management Organization (RFMO) regions.

    For detailed information about the Reference Data API, please refer to the official
    Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#reference-data

    See: https://globalfishingwatch.org/our-apis/documentation#regions

    For more details on the Reference Data API data caveats, please refer to the
    official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation#exclusive-economic-zone-boundaries-definition

    See: https://globalfishingwatch.org/our-apis/documentation#marine-protected-area-boundaries-definition

    See: https://globalfishingwatch.org/our-apis/documentation#what-does-it-mean-if-an-event-is-within-a-specific-geographic-area-such-as-an-eez-mpa-or-rfmo

    See: https://globalfishingwatch.org/our-apis/documentation#how-does-gfw-calculate-that-an-event-has-a-publicly-listed-authorization

    See: https://globalfishingwatch.org/our-apis/documentation#exclusive-economic-zone-boundaries-definitions

    See: https://globalfishingwatch.org/our-apis/documentation#marine-protected-area-boundaries-definition-2
    """

    async def get_eez_regions(self, **kwargs: Dict[str, Any]) -> EEZRegionResult:
        """Get available Exclusive Economic Zone (EEZ) regions data.

        Retrieves a list of Exclusive Economic Zone (EEZ) regions.

        For detailed information about the EEZ regions API endpoint, please refer to the official
        Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#regions

        For more details on the EEZ regions data caveats, please refer to the official
        Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#exclusive-economic-zone-boundaries-definition

        See: https://globalfishingwatch.org/our-apis/documentation#what-does-it-mean-if-an-event-is-within-a-specific-geographic-area-such-as-an-eez-mpa-or-rfmo

        See: https://globalfishingwatch.org/our-apis/documentation#exclusive-economic-zone-boundaries-definitions

        Args:
            **kwargs (Dict[str, Any]):
                Additional keyword arguments to pass to the EEZ region endpoint's request.

        Returns:
            EEZRegionResult:
                The result containing the list of EEZ regions data items.

        Raises:
            GFWAPIClientError:
                If the API request fails.
        """
        endpoint: EEZRegionEndPoint = EEZRegionEndPoint(http_client=self._http_client)
        result: EEZRegionResult = await endpoint.request(**kwargs)
        return result

    async def get_mpa_regions(self, **kwargs: Dict[str, Any]) -> MPARegionResult:
        """Get available Marine Protected Area (MPA) regions data.

        Retrieves a list of Marine Protected Area (MPA) regions.

        For detailed information about the MPA regions API endpoint, please refer to the official
        Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#regions

        For more details on the MPA regions data caveats, please refer to the official
        Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#marine-protected-area-boundaries-definition

        See: https://globalfishingwatch.org/our-apis/documentation#what-does-it-mean-if-an-event-is-within-a-specific-geographic-area-such-as-an-eez-mpa-or-rfmo

        See: https://globalfishingwatch.org/our-apis/documentation#marine-protected-area-boundaries-definition-2

        Args:
            **kwargs (Dict[str, Any]):
                Additional keyword arguments to pass to the MPA region endpoint's request.

        Returns:
            MPARegionResult:
                The result containing the list of MPA regions data items.

        Raises:
            GFWAPIClientError:
                If the API request fails.
        """
        endpoint: MPARegionEndPoint = MPARegionEndPoint(http_client=self._http_client)
        result: MPARegionResult = await endpoint.request(**kwargs)
        return result

    async def get_rfmo_regions(self, **kwargs: Dict[str, Any]) -> RFMORegionResult:
        """Get available Regional Fisheries Management Organization (RFMO) regions data.

        Retrieves a list of Regional Fisheries Management Organization (RFMO) regions.

        For detailed information about the RFMO regions API endpoint, please refer to the official
        Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#regions

        For more details on the RFMO regions data caveats, please refer to the official
        Global Fishing Watch API documentation:

        See: https://globalfishingwatch.org/our-apis/documentation#what-does-it-mean-if-an-event-is-within-a-specific-geographic-area-such-as-an-eez-mpa-or-rfmo

        See: https://globalfishingwatch.org/our-apis/documentation#how-does-gfw-calculate-that-an-event-has-a-publicly-listed-authorization

        Args:
            **kwargs (Dict[str, Any]):
                Additional keyword arguments to pass to the RFMO region endpoint's request.

        Returns:
            RFMORegionResult:
                The result containing the list of RFMO regions data items.

        Raises:
            GFWAPIClientError:
                If the API request fails.
        """
        endpoint: RFMORegionEndPoint = RFMORegionEndPoint(http_client=self._http_client)
        result: RFMORegionResult = await endpoint.request(**kwargs)
        return result
