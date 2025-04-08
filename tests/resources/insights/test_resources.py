"""Tests for `gfwapiclient.resources.insights.resources`."""

from typing import Any, Dict, cast

import pytest
import respx

from gfwapiclient.exceptions.validation import RequestBodyValidationError
from gfwapiclient.http.client import HTTPClient
from gfwapiclient.resources.insights.models.request import (
    VESSEL_INSIGHT_REQUEST_BODY_VALIDATION_ERROR_MESSAGE,
)
from gfwapiclient.resources.insights.models.response import (
    VesselInsightItem,
    VesselInsightResult,
)
from gfwapiclient.resources.insights.resources import InsightResource


@pytest.mark.asyncio
@pytest.mark.respx
async def test_insight_resource_get_vessel_insights(
    mock_http_client: HTTPClient,
    mock_raw_vessel_insight_request_body: Dict[str, Any],
    mock_raw_vessel_insight_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `InsightResource` get vessel insights succeeds with valid response."""
    mock_responsex.post("/insights/vessels").respond(
        200, json=mock_raw_vessel_insight_item
    )
    resource = InsightResource(http_client=mock_http_client)
    result = await resource.get_vessel_insights(
        includes=mock_raw_vessel_insight_request_body["includes"],
        start_date=mock_raw_vessel_insight_request_body["startDate"],
        end_date=mock_raw_vessel_insight_request_body["endDate"],
        vessels=mock_raw_vessel_insight_request_body["vessels"],
    )
    data = cast(VesselInsightItem, result.data())
    assert isinstance(result, VesselInsightResult)
    assert isinstance(data, VesselInsightItem)


@pytest.mark.asyncio
async def test_insight_resource_get_vessel_insights_validation_error_raises(
    mock_http_client: HTTPClient,
    mock_raw_vessel_insight_request_body: Dict[str, Any],
) -> None:
    """Test `InsightResource` get vessel insights raises `RequestBodyValidationError` with invalid parameters."""
    resource = InsightResource(http_client=mock_http_client)

    with pytest.raises(
        RequestBodyValidationError,
        match=VESSEL_INSIGHT_REQUEST_BODY_VALIDATION_ERROR_MESSAGE,
    ):
        await resource.get_vessel_insights(
            includes=["INVALID_INCLUDE"],
            start_date=mock_raw_vessel_insight_request_body["startDate"],
            end_date=mock_raw_vessel_insight_request_body["endDate"],
            vessels=mock_raw_vessel_insight_request_body["vessels"],
        )
