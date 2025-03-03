"""Global Fishing Watch (GFW) API Python Client - Vessels Insights API Resource."""

import datetime

from typing import Any, Dict, List

from gfwapiclient.http.resources import BaseResource
from gfwapiclient.resources.insights.endpoints import VesselInsightEndPoint
from gfwapiclient.resources.insights.models.request import (
    VesselInsightBody,
    VesselInsightIdBody,
    VesselInsightInclude,
)
from gfwapiclient.resources.insights.models.response import VesselInsightResult


class InsightResource(BaseResource):
    """Insights data API resource."""

    async def aget_vessel_insights(
        self,
        includes: List[VesselInsightInclude],
        start_date: datetime.date,
        end_date: datetime.date,
        vessels: List[VesselInsightIdBody],
        **kwargs: Dict[str, Any],
    ) -> VesselInsightResult:
        """Asynchronously get vessels insights data."""
        request_body = VesselInsightBody(
            includes=includes,
            start_date=start_date,
            end_date=end_date,
            vessels=vessels,
        )
        endpoint = VesselInsightEndPoint(
            request_body=request_body,
            http_client=self._http_client,
        )
        result = await endpoint.arequest()
        return result

    def get_vessel_insights(
        self,
        includes: List[VesselInsightInclude],
        start_date: datetime.date,
        end_date: datetime.date,
        vessels: List[VesselInsightIdBody],
        **kwargs: Dict[str, Any],
    ) -> VesselInsightResult:
        """Synchronously  get vessels insights data."""
        request_body = VesselInsightBody(
            includes=includes,
            start_date=start_date,
            end_date=end_date,
            vessels=vessels,
        )
        endpoint = VesselInsightEndPoint(
            request_body=request_body,
            http_client=self._http_client,
        )
        result = endpoint.request()
        return result
