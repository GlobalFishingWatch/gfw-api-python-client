"""Integration tests for the `gfwapiclient` References Data API.

These tests verify the functionality of the `ReferenceResource` within the `gfwapiclient` library,
ensuring that reference data (EEZ, MPA, RFMO regions) can be retrieved correctly.

For more details on the Regions API, please refer to the official
`Global Fishing Watch Regions API Documentation <https://globalfishingwatch.org/our-apis/documentation#regions>`_.
"""

from typing import List, cast

import pandas as pd
import pytest

import gfwapiclient as gfw

from gfwapiclient.resources.references.regions.models.response import (
    EEZRegionItem,
    EEZRegionResult,
    MPARegionItem,
    MPARegionResult,
    RFMORegionItem,
    RFMORegionResult,
)


@pytest.mark.integration
@pytest.mark.asyncio
async def test_references_get_eez_regions_success(gfw_client: gfw.Client) -> None:
    """Test retrieving available Exclusive Economic Zone (EEZ) regions data.

    This test verifies that the `get_eez_regions` method can successfully fetch EEZ region data from the API,
    that the returned data conforms to the expected model, and that it can be converted to a Pandas DataFrame.
    """
    result: EEZRegionResult = await gfw_client.references.get_eez_regions()

    data: List[EEZRegionItem] = cast(List[EEZRegionItem], result.data())
    assert isinstance(result, EEZRegionResult)
    assert len(data) >= 1, "Expected at least one EEZ region."
    assert isinstance(data[0], EEZRegionItem)

    df: pd.DataFrame = cast(pd.DataFrame, result.df())
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 1, "Expected at least one row in the DataFrame."
    assert list(df.columns) == list(dict(data[-1]).keys())


@pytest.mark.integration
@pytest.mark.asyncio
async def test_references_get_mpa_regions(gfw_client: gfw.Client) -> None:
    """Test retrieving available Marine Protected Area (MPA) regions data.

    This test verifies that the `get_mpa_regions` method can successfully fetch MPA region data from the API,
    that the returned data conforms to the expected model, and that it can be converted to a Pandas DataFrame.
    """
    result: MPARegionResult = await gfw_client.references.get_mpa_regions()

    data: List[MPARegionItem] = cast(List[MPARegionItem], result.data())
    assert isinstance(result, MPARegionResult)
    assert len(data) >= 1, "Expected at least one MPA region."
    assert isinstance(data[0], MPARegionItem)

    df: pd.DataFrame = cast(pd.DataFrame, result.df())
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 1, "Expected at least one row in the DataFrame."
    assert list(df.columns) == list(dict(data[-1]).keys())


@pytest.mark.integration
@pytest.mark.asyncio
async def test_references_get_rfmo_regions(gfw_client: gfw.Client) -> None:
    """Test retrieving available Regional Fisheries Management Organization (RFMO) regions data.

    This test verifies that the `get_rfmo_regions` method can successfully fetch RFMO region data from the API,
    that the returned data conforms to the expected model, and that it can be converted to a Pandas DataFrame.
    """
    result: RFMORegionResult = await gfw_client.references.get_rfmo_regions()

    data: List[RFMORegionItem] = cast(List[RFMORegionItem], result.data())
    assert isinstance(result, RFMORegionResult)
    assert len(data) >= 1, "Expected at least one RFMO region."
    assert isinstance(data[0], RFMORegionItem)

    df: pd.DataFrame = cast(pd.DataFrame, result.df())
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 1, "Expected at least one row in the DataFrame."
    assert list(df.columns) == list(dict(data[-1]).keys())
