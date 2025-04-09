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
async def test_insights_get_vessel_insights_get_insights_for_fishing_events(
    gfw_client: gfw.Client,
) -> None:
    """Test getting vessel insights related to fishing events.

    This test verifies that the `get_vessel_insights` method correctly retrieves
    insights for a specific vessel related to fishing activity within a given
    date range. It checks the structure and content of the returned data,
    ensuring it's a valid `VesselInsightResult` and that the data can be
    converted to a pandas DataFrame.
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
async def test_insights_get_vessel_insights_get_insights_for_ais_off_events(
    gfw_client: gfw.Client,
) -> None:
    """Test getting vessel insights related to AIS off events (gaps).

    This test verifies that the `get_vessel_insights` method correctly retrieves
    insights for a specific vessel related to AIS off events (gaps) within a
    given date range. It checks the structure and content of the returned data,
    ensuring it's a valid `VesselInsightResult` and that the data can be
    converted to a pandas DataFrame.
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
async def test_insights_get_vessel_insights_get_insights_for_ais_coverage_events(
    gfw_client: gfw.Client,
) -> None:
    """Test getting vessel insights related to related to AIS coverage events.

    This test verifies that the `get_vessel_insights` method correctly retrieves
    insights for a specific vessel related to AIS coverage events within a
    given date range. It checks the structure and content of the returned data,
    ensuring it's a valid `VesselInsightResult` and that the data can be
    converted to a pandas DataFrame.
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
async def test_insights_get_vessel_insights_get_insights_for_iuu_list(
    gfw_client: gfw.Client,
) -> None:
    """Test getting vessel insights related to being listed in the IUU list.

    This test verifies that the `get_vessel_insights` method correctly retrieves
    insights for a specific vessel related to its presence on an IUU (Illegal,
    Unreported, and Unregulated) vessel list within a given date range.
    It checks the structure and content of the returned data, ensuring it's a
    valid `VesselInsightResult` and that the data can be converted to a
    pandas DataFrame.
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
async def test_insights_get_vessel_insights_get_insights_for_multiple_insight_types(
    gfw_client: gfw.Client,
) -> None:
    """Test getting vessel insights for multiple insight types.

    This test verifies that the `get_vessel_insights` method correctly retrieves
    insights for a specific vessel for multiple insight types within a
    given date range. It checks the structure and content of the returned data,
    ensuring it's a valid `VesselInsightResult` and that the data can be
    converted to a pandas DataFrame.
    """
    result: VesselInsightResult = await gfw_client.insights.get_vessel_insights(
        includes=["FISHING", "GAP", "VESSEL-IDENTITY-IUU-VESSEL-LIST", "COVERAGE"],
        start_date="2020-01-01",
        end_date="2025-03-03",
        vessels=[
            {
                "dataset_id": "public-global-vessel-identity:latest",
                "vessel_id": "785101812-2127-e5d2-e8bf-7152c5259f5f",
            },
            {
                "dataset_id": "public-global-vessel-identity:latest",
                "vessel_id": "2339c52c3-3a84-1603-f968-d8890f23e1ed",
            },
            {
                "dataset_id": "public-global-vessel-identity:latest",
                "vessel_id": "2d26aa452-2d4f-4cae-2ec4-377f85e88dcb",
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
