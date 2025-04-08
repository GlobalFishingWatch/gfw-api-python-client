"""Integration tests for the `gfwapiclient` Vessels API.

These tests verify the functionality of the `VesselResource` within the `gfwapiclient` library,
ensuring that vessel data can be searched and retrieved correctly.

For more details on the Vessels API, please refer to the official
`Global Fishing Watch Vessels API Documentation <https://globalfishingwatch.org/our-apis/documentation#vessels-api>`_.
"""

from typing import List, cast

import pandas as pd
import pytest

import gfwapiclient as gfw

from gfwapiclient.resources.vessels.detail.models.response import (
    VesselDetailItem,
    VesselDetailResult,
)
from gfwapiclient.resources.vessels.list.models.response import (
    VesselListItem,
    VesselListResult,
)
from gfwapiclient.resources.vessels.search.models.response import (
    VesselSearchItem,
    VesselSearchResult,
)


@pytest.mark.integration
@pytest.mark.asyncio
async def test_vessels_search_vessels_basic_success(gfw_client: gfw.Client) -> None:
    """Test basic vessel search by keyword (MMSI).

    This test verifies that the `search_vessels` method correctly retrieves vessel data
    based on a basic keyword search (MMSI in this case). It checks the structure and
    content of the returned data, ensuring it's a valid `VesselSearchResult` and that
    the data can be converted to a pandas DataFrame.
    """
    result: VesselSearchResult = await gfw_client.vessels.search_vessels(
        query="368045130",
        datasets=["public-global-vessel-identity:latest"],
        includes=["MATCH_CRITERIA", "OWNERSHIP", "AUTHORIZATIONS"],
    )
    data: List[VesselSearchItem] = cast(List[VesselSearchItem], result.data())
    assert isinstance(result, VesselSearchResult)
    assert len(data) >= 1, "Expected at least one vessel in search results."
    assert isinstance(data[0], VesselSearchItem)

    df: pd.DataFrame = cast(pd.DataFrame, result.df())
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 1, "Expected at least one row in the DataFrame."
    assert list(df.columns) == list(dict(data[0]).keys())


@pytest.mark.integration
@pytest.mark.asyncio
async def test_vessels_search_vessels_advanced_success(gfw_client: gfw.Client) -> None:
    """Test advanced vessel search by keyword (MMSI and shipname).

    This test verifies that the `search_vessels` method correctly retrieves vessel data
    based on an advanced keyword search (MMSI and shipname). It checks the structure
    and content of the returned data, ensuring it's a valid `VesselSearchResult` and
    that the data can be converted to a pandas DataFrame.
    """
    result: VesselSearchResult = await gfw_client.vessels.search_vessels(
        where='ssvid="775998121" AND shipname="DON TITO"',
        datasets=["public-global-vessel-identity:latest"],
        includes=["MATCH_CRITERIA", "OWNERSHIP"],
    )
    data: List[VesselSearchItem] = cast(List[VesselSearchItem], result.data())
    assert isinstance(result, VesselSearchResult)
    assert len(data) >= 1, "Expected at least one vessel in search results."
    assert isinstance(data[0], VesselSearchItem)

    df: pd.DataFrame = cast(pd.DataFrame, result.df())
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 1, "Expected at least one row in the DataFrame."
    assert list(df.columns) == list(dict(data[0]).keys())


@pytest.mark.integration
@pytest.mark.asyncio
async def test_vessels_get_vessels_by_ids_success(gfw_client: gfw.Client) -> None:
    """Test retrieving details of multiple vessels by IDs.

    This test verifies that the `get_vessels_by_ids` method correctly retrieves
    details for multiple vessels based on their IDs. It checks the structure and
    content of the returned data, ensuring it's a valid `VesselListResult` and that
    the data can be converted to a pandas DataFrame.
    """
    result: VesselListResult = await gfw_client.vessels.get_vessels_by_ids(
        ids=[
            "8c7304226-6c71-edbe-0b63-c246734b3c01",
            "6583c51e3-3626-5638-866a-f47c3bc7ef7c",
            "71e7da672-2451-17da-b239-857831602eca",
        ],
        datasets=["public-global-vessel-identity:latest"],
    )
    data: List[VesselListItem] = cast(List[VesselListItem], result.data())
    assert isinstance(result, VesselListResult)
    assert len(data) == 3, "Expected details for three vessels."
    assert isinstance(data[0], VesselListItem)

    df: pd.DataFrame = cast(pd.DataFrame, result.df())
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 3, "Expected three rows in the DataFrame."
    assert list(df.columns) == list(dict(data[0]).keys())


@pytest.mark.integration
@pytest.mark.asyncio
async def test_vessels_gget_vessel_by_id_success(gfw_client: gfw.Client) -> None:
    """Test retrieving details of a single vessel by ID.

    This test verifies that the `get_vessel_by_id` method correctly retrieves
    details for a single vessel based on its ID. It checks the structure and
    content of the returned data, ensuring it's a valid `VesselDetailResult` and
    that the data can be converted to a pandas DataFrame.
    """
    vessel_id = "c54923e64-46f3-9338-9dcb-ff09724077a3"
    result: VesselDetailResult = await gfw_client.vessels.get_vessel_by_id(
        id=vessel_id, dataset="public-global-vessel-identity:latest"
    )
    data: VesselDetailItem = cast(VesselDetailItem, result.data())
    assert isinstance(result, VesselDetailResult)
    assert isinstance(data, VesselDetailItem)

    df: pd.DataFrame = cast(pd.DataFrame, result.df())
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1, "Expected one row in the DataFrame."
    assert list(df.columns) == list(dict(data).keys())
