"""Integration tests for the `gfwapiclient` Insights API.

These tests verify the functionality of the `InsightResource` within the `gfwapiclient` library,
ensuring that vessel insights data can be retrieved correctly for various insight types.

For more details on the Insights API, please refer to the official
`Global Fishing Watch Insights API Documentation <https://globalfishingwatch.org/our-apis/documentation#insights-api>`_.
"""

from typing import cast

import pandas as pd
import pytest

import gfwapiclient as gfw

from gfwapiclient.resources.insights.models.response import (
    VesselInsightItem,
    VesselInsightResult,
)


@pytest.mark.integration
@pytest.mark.asyncio
async def test_insights_get_vessel_insights_related_to_fishing_events_success(
    gfw_client: gfw.Client,
) -> None:
    """Test retrieving vessel insights related to fishing activity events.

    This test verifies that the `get_vessel_insights` method can successfully retrieve
    vessel insights data for fishing activity events.
    """
    result: VesselInsightResult = await gfw_client.insights.get_vessel_insights(
        includes=["FISHING"],
        start_date="2020-01-01",
        end_date="2025-03-03",
        vessels=[
            {
                "dataset_id": "public-global-vessel-identity:latest",
                "vessel_id": "785101812-2127-e5d2-e8bf-7152c5259f5f",
            }
        ],
    )
    data: VesselInsightItem = cast(VesselInsightItem, result.data())
    assert isinstance(result, VesselInsightResult)
    assert isinstance(data, VesselInsightItem)

    df: pd.DataFrame = cast(pd.DataFrame, result.df())
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 1, "Expected at least one row in the DataFrame."
    assert list(df.columns) == list(dict(data).keys())


@pytest.mark.integration
@pytest.mark.asyncio
async def test_insights_get_vessel_insights_related_to_ais_off_events_success(
    gfw_client: gfw.Client,
) -> None:
    """Test retrieving vessel insights related to AIS off (gap) events.

    This test verifies that the `get_vessel_insights` method can successfully retrieve
    vessel insights data for AIS off (gap) events.
    """
    result: VesselInsightResult = await gfw_client.insights.get_vessel_insights(
        includes=["GAP"],
        start_date="2020-01-01",
        end_date="2025-03-03",
        vessels=[
            {
                "dataset_id": "public-global-vessel-identity:latest",
                "vessel_id": "2339c52c3-3a84-1603-f968-d8890f23e1ed",
            }
        ],
    )
    data: VesselInsightItem = cast(VesselInsightItem, result.data())
    assert isinstance(result, VesselInsightResult)
    assert isinstance(data, VesselInsightItem)

    df: pd.DataFrame = cast(pd.DataFrame, result.df())
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 1, "Expected at least one row in the DataFrame."
    assert list(df.columns) == list(dict(data).keys())


@pytest.mark.integration
@pytest.mark.asyncio
async def test_insights_get_vessel_insights_related_to_ais_coverage_events_success(
    gfw_client: gfw.Client,
) -> None:
    """Test retrieving vessel insights related to AIS coverage events.

    This test verifies that the `get_vessel_insights` method can successfully retrieve
    vessel insights data for AIS coverage events.
    """
    result: VesselInsightResult = await gfw_client.insights.get_vessel_insights(
        includes=["COVERAGE"],
        start_date="2020-01-01",
        end_date="2025-03-03",
        vessels=[
            {
                "dataset_id": "public-global-vessel-identity:latest",
                "vessel_id": "2339c52c3-3a84-1603-f968-d8890f23e1ed",
            }
        ],
    )
    data: VesselInsightItem = cast(VesselInsightItem, result.data())
    assert isinstance(result, VesselInsightResult)
    assert isinstance(data, VesselInsightItem)

    df: pd.DataFrame = cast(pd.DataFrame, result.df())
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 1, "Expected at least one row in the DataFrame."
    assert list(df.columns) == list(dict(data).keys())


@pytest.mark.integration
@pytest.mark.asyncio
async def test_insights_get_vessel_insights_related_to_vessels_listed_in_iuu_lists_success(
    gfw_client: gfw.Client,
) -> None:
    """Test retrieving vessel insights related to vessels listed in IUU lists.

    This test verifies that the `get_vessel_insights` method can successfully retrieve
    vessel insights data for vessels listed in IUU lists.
    """
    result: VesselInsightResult = await gfw_client.insights.get_vessel_insights(
        includes=["VESSEL-IDENTITY-IUU-VESSEL-LIST"],
        start_date="2020-01-01",
        end_date="2025-03-03",
        vessels=[
            {
                "dataset_id": "public-global-vessel-identity:latest",
                "vessel_id": "2d26aa452-2d4f-4cae-2ec4-377f85e88dcb",
            }
        ],
    )
    data: VesselInsightItem = cast(VesselInsightItem, result.data())
    assert isinstance(result, VesselInsightResult)
    assert isinstance(data, VesselInsightItem)

    df: pd.DataFrame = cast(pd.DataFrame, result.df())
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 1, "Expected at least one row in the DataFrame."
    assert list(df.columns) == list(dict(data).keys())


@pytest.mark.integration
@pytest.mark.asyncio
async def test_insights_get_vessel_insights_all_types_success(
    gfw_client: gfw.Client,
) -> None:
    """Test retrieving vessel insights for all types.

    This test verifies that the `get_vessel_insights` method can successfully retrieve
    vessel insights data for multiple insight types.
    """
    result: VesselInsightResult = await gfw_client.insights.get_vessel_insights(
        includes=["FISHING", "GAP", "VESSEL-IDENTITY-IUU-VESSEL-LIST", "COVERAGE"],
        start_date="2020-01-01",
        end_date="2025-03-03",
        vessels=[
            {
                "datasetId": "public-global-vessel-identity:latest",
                "vesselId": "785101812-2127-e5d2-e8bf-7152c5259f5f",
            },
            {
                "datasetId": "public-global-vessel-identity:latest",
                "vesselId": "2339c52c3-3a84-1603-f968-d8890f23e1ed",
            },
            {
                "datasetId": "public-global-vessel-identity:latest",
                "vesselId": "2d26aa452-2d4f-4cae-2ec4-377f85e88dcb",
            },
        ],
    )
    data: VesselInsightItem = cast(VesselInsightItem, result.data())
    assert isinstance(result, VesselInsightResult)
    assert isinstance(data, VesselInsightItem)

    df: pd.DataFrame = cast(pd.DataFrame, result.df())
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 1, "Expected at least one row in the DataFrame."
    assert list(df.columns) == list(dict(data).keys())
