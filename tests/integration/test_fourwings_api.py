"""Integration tests for the `gfwapiclient` 4Wings API.

These tests verify the functionality of the 4Wings API endpoints, ensuring they
correctly retrieve and process data related to fishing effort and other metrics.
They cover scenarios involving custom polygons and existing regions.

For more details on the 4Wings API, please refer to the official
Global Fishing Watch API documentation:

- `4Wings API Documentation <https://globalfishingwatch.org/our-apis/documentation#map-visualization-4wings-api>`_
"""

from typing import List, cast

import pandas as pd
import pytest

import gfwapiclient as gfw

from gfwapiclient.resources.fourwings.report.models.response import (
    FourWingsReportItem,
    FourWingsReportResult,
)


@pytest.mark.integration
@pytest.mark.asyncio
async def test_fourwings_get_report_related_to_fishing_effort_by_custom_polygon_success(
    gfw_client: gfw.Client,
) -> None:
    """Test retrieving 4Wings report related to fishing effort by custom polygon.

    This test verifies that the `get_report` method correctly retrieves fishing
    effort data for a specified custom polygon. It checks the structure and
    content of the returned data, ensuring it's a valid `FourWingsReportResult`
    and that the data can be converted to a pandas DataFrame.
    """
    result: FourWingsReportResult = await gfw_client.fourwings.get_report(
        spatial_resolution="LOW",
        temporal_resolution="YEARLY",
        group_by="FLAG",
        datasets=["public-global-fishing-effort:latest"],
        start_date="2021-01-01",
        end_date="2022-01-01",
        geojson={
            "type": "Polygon",
            "coordinates": [
                [
                    [-76.11328125, -26.273714024406416],
                    [-76.201171875, -26.980828590472093],
                    [-76.376953125, -27.527758206861883],
                    [-76.81640625, -28.30438068296276],
                    [-77.255859375, -28.767659105691244],
                    [-77.87109375, -29.152161283318918],
                    [-78.486328125, -29.45873118535532],
                    [-79.189453125, -29.61167011519739],
                    [-79.892578125, -29.6880527498568],
                    [-80.595703125, -29.61167011519739],
                    [-81.5625, -29.382175075145277],
                    [-82.177734375, -29.07537517955835],
                    [-82.705078125, -28.6905876542507],
                    [-83.232421875, -28.071980301779845],
                    [-83.49609375, -27.683528083787756],
                    [-83.759765625, -26.980828590472093],
                    [-83.84765625, -26.35249785815401],
                    [-83.759765625, -25.64152637306576],
                    [-83.583984375, -25.16517336866393],
                    [-83.232421875, -24.447149589730827],
                    [-82.705078125, -23.966175871265037],
                    [-82.177734375, -23.483400654325635],
                    [-81.5625, -23.241346102386117],
                    [-80.859375, -22.998851594142906],
                    [-80.15625, -22.917922936146027],
                    [-79.453125, -22.998851594142906],
                    [-78.662109375, -23.1605633090483],
                    [-78.134765625, -23.40276490540795],
                    [-77.431640625, -23.885837699861995],
                    [-76.9921875, -24.28702686537642],
                    [-76.552734375, -24.846565348219727],
                    [-76.2890625, -25.48295117535531],
                    [-76.11328125, -26.273714024406416],
                ]
            ],
        },
    )
    data: List[FourWingsReportItem] = cast(List[FourWingsReportItem], result.data())
    assert isinstance(result, FourWingsReportResult)
    assert len(data) >= 1, "Expected at least one FourWingsReportItem."
    assert isinstance(data[0], FourWingsReportItem)

    df: pd.DataFrame = cast(pd.DataFrame, result.df())
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 1, "Expected at least one row in the DataFrame."
    assert list(df.columns) == list(dict(data[0]).keys())


@pytest.mark.integration
@pytest.mark.asyncio
async def test_fourwings_get_report_related_to_fishing_effort_by_existing_region_success(
    gfw_client: gfw.Client,
) -> None:
    """Test retrieving 4Wings report related to fishing effort by existing region.

    This test verifies that the `get_report` method correctly retrieves fishing
    effort data for a specified existing region. It checks the structure and
    content of the returned data, ensuring it's a valid `FourWingsReportResult`
    and that the data can be converted to a pandas DataFrame.
    """
    result: FourWingsReportResult = await gfw_client.fourwings.get_report(
        spatial_resolution="LOW",
        temporal_resolution="MONTHLY",
        group_by="GEARTYPE",
        datasets=["public-global-fishing-effort:latest"],
        start_date="2022-01-01",
        end_date="2022-05-01",
        region={"dataset": "public-eez-areas", "id": "5690"},
    )
    data: List[FourWingsReportItem] = cast(List[FourWingsReportItem], result.data())
    assert isinstance(result, FourWingsReportResult)
    assert len(data) >= 1, "Expected at least one FourWingsReportItem."
    assert isinstance(data[0], FourWingsReportItem)

    df: pd.DataFrame = cast(pd.DataFrame, result.df())
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 1, "Expected at least one row in the DataFrame."
    assert list(df.columns) == list(dict(data[0]).keys())
