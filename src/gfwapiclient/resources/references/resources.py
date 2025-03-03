"""Global Fishing Watch (GFW) API Python Client - References Resources."""

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


class ReferenceResource(BaseResource):
    """References data API resource."""

    async def aget_eez_regions(self, **kwargs: Dict[str, Any]) -> EEZRegionResult:
        """Asynchronously get available Exclusive Economic Zone (EEZ) regions data."""
        endpoint = EEZRegionEndPoint(http_client=self._http_client)
        result = await endpoint.arequest()
        return result

    def get_eez_regions(self, **kwargs: Dict[str, Any]) -> EEZRegionResult:
        """Synchronously get available Exclusive Economic Zone (EEZ) regions data."""
        endpoint = EEZRegionEndPoint(http_client=self._http_client)
        result = endpoint.request()
        return result

    async def aget_mpa_regions(self, **kwargs: Dict[str, Any]) -> MPARegionResult:
        """Asynchronously get available Marine Protected Area (MPA) regions data."""
        endpoint = MPARegionEndPoint(http_client=self._http_client)
        result = await endpoint.arequest()
        return result

    def get_mpa_regions(self, **kwargs: Dict[str, Any]) -> MPARegionResult:
        """Synchronously get available Marine Protected Area (MPA) regions data."""
        endpoint = MPARegionEndPoint(http_client=self._http_client)
        result = endpoint.request()
        return result

    async def aget_rfmo_regions(self, **kwargs: Dict[str, Any]) -> RFMORegionResult:
        """Asynchronously get available Regional Fisheries Management Organization (RFMO) regions data."""
        endpoint = RFMORegionEndPoint(http_client=self._http_client)
        result = await endpoint.arequest()
        return result

    def get_rfmo_regions(self, **kwargs: Dict[str, Any]) -> RFMORegionResult:
        """Synchronously get available Regional Fisheries Management Organization (RFMO) regions data."""
        endpoint = RFMORegionEndPoint(http_client=self._http_client)
        result = endpoint.request()
        return result
