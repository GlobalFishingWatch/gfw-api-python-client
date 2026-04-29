"""Integration tests for the `gfwapiclient` Bulk Download API.

These tests verify the functionality of the `BulkDownloadResource` within the
`gfwapiclient` library, ensuring that bulk reports can be created, retrieved,
queried and downloaded correctly.

For more details on the Bulk Download API, please refer to the official
`Global Fishing Watch API documentation <https://globalfishingwatch.org/our-apis/documentation#bulk-download-api>`_.
"""

import time

from pathlib import Path
from typing import Union, cast

import pandas as pd
import pytest

import gfwapiclient as gfw

from gfwapiclient.resources.bulk_downloads.create.models.response import (
    BulkReportCreateItem,
    BulkReportCreateResult,
)


@pytest.mark.parametrize(
    "geojson",
    [
        "tests/fixtures/bulk_downloads/geojson/geojson.json",
        Path("tests/fixtures/bulk_downloads/geojson/geojson.json"),
        "tests/fixtures/bulk_downloads/geojson/geojson.shp",
        Path("tests/fixtures/bulk_downloads/geojson/geojson.shp"),
    ],
)
@pytest.mark.integration
@pytest.mark.asyncio
async def test_bulk_downloads_create_sar_fixed_infrastructure_data_bulk_report_by_geojson_from_spatial_file(
    geojson: Union[str, Path],
    gfw_client: gfw.Client,
) -> None:
    """Test create SAR (Sentinel-1 and Sentinel-2) fixed infrastructure bulk report by geojson from spatial file.

    This test verifies that the `create_bulk_report` method can correctly generate
    SAR (Sentinel-1 and Sentinel-2) fixed infrastructure bulk report for a specified
    geojson from spatial file. It checks the structure and content of the returned data,
    ensuring it's a valid `BulkReportCreateResult` and that the data can be converted to a
    pandas DataFrame.
    """
    timestamp = int(time.time() * 1000)
    result: BulkReportCreateResult = await gfw_client.bulk_downloads.create_bulk_report(
        name=f"sar-vessel-detection-python-package-example-{timestamp}-custom-geojson",
        dataset="public-fixed-infrastructure-data:latest",
        geojson=geojson,
        format="JSON",
        filters=[
            "structure_start_date between '2020-01-01' and '2023-01-01'",
            "structure_end_date between '2022-01-01' and '2025-01-01'",
        ],
    )
    data: BulkReportCreateItem = cast(BulkReportCreateItem, result.data())

    assert isinstance(result, BulkReportCreateResult)
    assert isinstance(data, BulkReportCreateItem)

    df: pd.DataFrame = cast(pd.DataFrame, result.df())
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 1, "Expected at least one row in the DataFrame."
    assert list(df.columns) == list(dict(data).keys())
