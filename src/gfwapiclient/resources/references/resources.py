"""Global Fishing Watch (GFW) API Python Client - References Data API Resource."""

from typing import Any, Dict

from gfwapiclient.http.resources import BaseResource
from gfwapiclient.resources.references.regions.endpoints import (
    EEZRegionEndPoint,
    MPARegionEndPoint,
    RFMORegionEndPoint,
)
from gfwapiclient.resources.references.regions.models import (
    EEZRegionResult,
    MPARegionResult,
    RFMORegionResult,
)


__all__ = ["ReferenceResource"]


class ReferenceResource(BaseResource):
    """References data API resource.

    This resource provides access to reference data endpoints, such as EEZ, MPA, and RFMO regions.
    See the API documentation for more details:
    https://globalfishingwatch.org/our-apis/documentation#regions
    """

    async def get_eez_regions(self, **kwargs: Dict[str, Any]) -> EEZRegionResult:
        """Get available Exclusive Economic Zone (EEZ) regions data.

        Retrieves a list of Exclusive Economic Zone (EEZ) regions.

        Args:
            **kwargs (Dict[str, Any]):
                Additional keyword arguments to pass to the EEZ region endpoint's request.

        Returns:
            EEZRegionResult:
                An `EEZRegionResult` instance containing the EEZ regions data.
        """
        endpoint: EEZRegionEndPoint = EEZRegionEndPoint(http_client=self._http_client)
        result: EEZRegionResult = await endpoint.request(**kwargs)
        return result

    async def get_mpa_regions(self, **kwargs: Dict[str, Any]) -> MPARegionResult:
        """Get available Marine Protected Area (MPA) regions data.

        Retrieves a list of Marine Protected Area (MPA) regions.

        Args:
            **kwargs (Dict[str, Any]):
                Additional keyword arguments to pass to the MPA region endpoint's request.

        Returns:
            MPARegionResult:
                An `MPARegionResult` instance containing the MPA regions data.
        """
        endpoint: MPARegionEndPoint = MPARegionEndPoint(http_client=self._http_client)
        result: MPARegionResult = await endpoint.request(**kwargs)
        return result

    async def get_rfmo_regions(self, **kwargs: Dict[str, Any]) -> RFMORegionResult:
        """Get available Regional Fisheries Management Organization (RFMO) regions data.

        Retrieves a list of Regional Fisheries Management Organization (RFMO) regions.

        Args:
            **kwargs (Dict[str, Any]):
                Additional keyword arguments to pass to the RFMO region endpoint's request.

        Returns:
            RFMORegionResult:
                An `RFMORegionResult` instance containing the RFMO regions data.
        """
        endpoint: RFMORegionEndPoint = RFMORegionEndPoint(http_client=self._http_client)
        result: RFMORegionResult = await endpoint.request(**kwargs)
        return result
