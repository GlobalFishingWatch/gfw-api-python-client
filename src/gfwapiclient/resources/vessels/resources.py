"""Global Fishing Watch (GFW) API Python Client - Vessels Insights API Resource."""

from typing import Any, Dict, List, Optional

from gfwapiclient.http.resources import BaseResource
from gfwapiclient.resources.vessels.base.enums import (
    VesselDataset,
    VesselInclude,
    VesselMatchField,
    VesselRegistryInfoData,
)
from gfwapiclient.resources.vessels.list.endpoints import VesselListEndPoint
from gfwapiclient.resources.vessels.list.models.request import VesselListParams
from gfwapiclient.resources.vessels.list.models.response import (
    VesselListResult,
)


__all__ = ["VesselResource"]


class VesselResource(BaseResource):
    """Vessels data API resource."""

    async def aget_vessels(
        self,
        ids: List[str],
        datasets: Optional[List[VesselDataset]] = None,
        registries_info_data: Optional[VesselRegistryInfoData] = None,
        includes: Optional[List[VesselInclude]] = None,
        match_fields: Optional[List[VesselMatchField]] = None,
        vessel_groups: Optional[List[str]] = None,
        **kwargs: Dict[str, Any],
    ) -> VesselListResult:
        """Asynchronously get list of vessels filtered by ids."""
        endpoint = self._make_vessel_list_endpoint(
            datasets=datasets,
            ids=ids,
            registries_info_data=registries_info_data,
            includes=includes,
            match_fields=match_fields or [VesselMatchField.ALL],
            vessel_groups=vessel_groups,
            **kwargs,
        )
        result = await endpoint.arequest()
        return result

    def get_vessels(
        self,
        ids: List[str],
        datasets: Optional[List[VesselDataset]] = None,
        registries_info_data: Optional[VesselRegistryInfoData] = None,
        includes: Optional[List[VesselInclude]] = None,
        match_fields: Optional[List[VesselMatchField]] = None,
        vessel_groups: Optional[List[str]] = None,
        **kwargs: Dict[str, Any],
    ) -> VesselListResult:
        """Synchronously get list of vessels filtered by ids."""
        endpoint = self._make_vessel_list_endpoint(
            ids=ids,
            datasets=datasets,
            registries_info_data=registries_info_data,
            includes=includes,
            match_fields=match_fields or [VesselMatchField.ALL],
            vessel_groups=vessel_groups,
            **kwargs,
        )
        result = endpoint.request()
        return result

    def _make_vessel_list_endpoint(
        self,
        ids: List[str],
        datasets: Optional[List[VesselDataset]] = None,
        registries_info_data: Optional[VesselRegistryInfoData] = None,
        includes: Optional[List[VesselInclude]] = None,
        match_fields: Optional[List[VesselMatchField]] = None,
        vessel_groups: Optional[List[str]] = None,
        **kwargs: Dict[str, Any],
    ) -> VesselListEndPoint:
        """Initializes a new `VesselListEndPoint` API endpoint."""
        request_params = VesselListParams(
            datasets=datasets or [VesselDataset.VESSEL_IDENTITY_LATEST],
            registries_info_data=registries_info_data or VesselRegistryInfoData.ALL,
            includes=includes or [VesselInclude.POTENTIAL_RELATED_SELF_REPORTED_INFO],
            binary=False,
            match_fields=match_fields or [VesselMatchField.ALL],
            ids=ids,
            vessel_groups=vessel_groups,
        )

        endpoint = VesselListEndPoint(
            request_params=request_params,
            http_client=self._http_client,
        )

        return endpoint
