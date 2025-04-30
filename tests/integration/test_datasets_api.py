"""Integration tests for the `gfwapiclient` Datasets API.

These tests verify the functionality of the `DatasetResource` within the
`gfwapiclient` library, ensuring that dataset-related data can be retrieved
correctly. Currently, they focus on retrieving SAR fixed infrastructure data
in MVT format.

For more details on the Datasets API, please refer to the official
`Global Fishing Watch API documentation <https://globalfishingwatch.org/our-apis/documentation#datasets-api>`_.
"""

from typing import Any, Dict, List, cast

import pandas as pd
import pytest

import gfwapiclient as gfw

from gfwapiclient.resources.datasets.models.response import (
    SARFixedInfrastructureItem,
    SARFixedInfrastructureResult,
)


@pytest.mark.integration
@pytest.mark.asyncio
async def test_datasets_get_sar_fixed_infrastructure_mvt_by_tile_coordinates(
    gfw_client: gfw.Client,
) -> None:
    """Test retrieving SAR fixed infrastructure data in MVT format by tile coordinates (z, x, y).

    This test verifies that the `get_sar_fixed_infrastructure` method can
    correctly retrieve Mapbox Vector Tile (MVT) data for a specific z/x/y tile.
    It checks the structure and content of the returned data, ensuring
    it's a valid `SARFixedInfrastructureResult` and that the data can be converted to a
    pandas DataFrame.
    """
    z: int = 1
    x: int = 0
    y: int = 1
    result: SARFixedInfrastructureResult = (
        await gfw_client.datasets.get_sar_fixed_infrastructure(
            z=z,
            x=x,
            y=y,
        )
    )

    data: List[SARFixedInfrastructureItem] = cast(
        List[SARFixedInfrastructureItem], result.data()
    )
    assert isinstance(result, SARFixedInfrastructureResult)
    assert len(data) >= 1, "Expected at least one SAR fixed infrastructure item."
    assert isinstance(data[0], SARFixedInfrastructureItem)

    df: pd.DataFrame = cast(pd.DataFrame, result.df())
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 1, "Expected at least one row in the DataFrame."
    assert list(df.columns) == list(dict(data[0]).keys())


@pytest.mark.integration
@pytest.mark.asyncio
async def test_datasets_get_sar_fixed_infrastructure_mvt_by_geometry(
    gfw_client: gfw.Client,
) -> None:
    """Test retrieving SAR fixed infrastructure data in MVT format by geometry.

    This test verifies that the `get_sar_fixed_infrastructure` method can
    correctly retrieve Mapbox Vector Tile (MVT) data for a specified geometry.
    It checks the structure and content of the returned data, ensuring
    it's a valid `SARFixedInfrastructureResult` and that the data can be converted to a
    pandas DataFrame.
    """
    geometry: Dict[str, Any] = {
        "type": "Polygon",
        "coordinates": [
            [
                [-180.0, -85.0511287798066],
                [-180.0, 0.0],
                [0.0, 0.0],
                [0.0, -85.0511287798066],
                [-180.0, -85.0511287798066],
            ]
        ],
    }
    result: SARFixedInfrastructureResult = (
        await gfw_client.datasets.get_sar_fixed_infrastructure(geometry=geometry)
    )
    data: List[SARFixedInfrastructureItem] = cast(
        List[SARFixedInfrastructureItem], result.data()
    )
    assert isinstance(result, SARFixedInfrastructureResult)
    assert len(data) >= 1, "Expected at least one SAR fixed infrastructure item."
    assert isinstance(data[0], SARFixedInfrastructureItem)

    df: pd.DataFrame = cast(pd.DataFrame, result.df())
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 1, "Expected at least one row in the DataFrame."
    assert list(df.columns) == list(dict(data[0]).keys())
