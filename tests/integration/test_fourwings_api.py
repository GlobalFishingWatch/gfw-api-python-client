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
async def test_fourwings_create_report_generate_fishing_effort_report_yearly_grouped_by_flag_custom_polygon(
    gfw_client: gfw.Client,
) -> None:
    """Test generating yearly fishing effort report by year and custom polygon.

    This test verifies that the `create_report` method correctly retrieves
    yearly fishing effort data grouped by flag for a specified custom polygon.
    It checks the structure and content of the returned data, ensuring it's a
    valid `FourWingsReportResult` and that the data can be converted to a pandas DataFrame.
    """
    result: FourWingsReportResult = await gfw_client.fourwings.create_report(
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
async def test_fourwings_create_report_generate_fishing_effort_report_monthly_grouped_by_gear_type_russian_eez(
    gfw_client: gfw.Client,
) -> None:
    """Test generating monthly fishing effort report grouped by gear type in Russian EEZ.

    This test verifies that the `create_report` method correctly retrieves
    monthly fishing effort data grouped by gear type within the Exclusive Economic Zone
    (EEZ) of Russia. It checks the structure and content of the returned data,
    ensuring it's a valid `FourWingsReportResult` and that the data can be
    converted to a pandas DataFrame.
    """
    result: FourWingsReportResult = await gfw_client.fourwings.create_report(
        spatial_resolution="LOW",
        temporal_resolution="MONTHLY",
        group_by="GEARTYPE",
        datasets=["public-global-fishing-effort:latest"],
        start_date="2022-01-01",
        end_date="2022-05-01",
        region={
            "dataset": "public-eez-areas",
            "id": "5690",
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
async def test_fourwings_create_report_generate_total_fishing_hours_per_grid_cell_mpa_dorsal_de_nasca(
    gfw_client: gfw.Client,
) -> None:
    """Test generating report with total fishing hours per grid cell in MPA Dorsal de Nasca.

    This test verifies that the `create_report` method correctly retrieves
    total fishing hours per latitude/longitude grid cell within the Marine
    Protected Area (MPA) Dorsal de Nasca. It checks the structure and content
    of the returned data, ensuring it's a valid `FourWingsReportResult` and
    that the data can be converted to a pandas DataFrame.
    """
    result: FourWingsReportResult = await gfw_client.fourwings.create_report(
        spatial_resolution="LOW",
        temporal_resolution="ENTIRE",
        spatial_aggregation=False,
        datasets=["public-global-fishing-effort:latest"],
        start_date="2022-01-01",
        end_date="2022-12-01",
        region={
            "dataset": "public-mpa-all",
            "id": "555745302",
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
@pytest.mark.skip
async def test_fourwings_create_report_generate_total_fishing_hours_per_grid_cell_mpa_dorsal_de_nasca_with_buffer(
    gfw_client: gfw.Client,
) -> None:
    """Test generating report with total fishing hours per grid cell in MPA Nasca with buffer.

    This test verifies that the `create_report` method correctly retrieves
    total fishing hours per latitude/longitude grid cell within the Marine
    Protected Area (MPA) Dorsal de Nasca, including a specified buffer.
    It checks the structure and content of the returned data, ensuring it's a
    valid `FourWingsReportResult` and that the data can be converted to a pandas DataFrame.
    """
    result: FourWingsReportResult = await gfw_client.fourwings.create_report(
        spatial_resolution="LOW",
        temporal_resolution="ENTIRE",
        spatial_aggregation=False,
        datasets=["public-global-fishing-effort:latest"],
        start_date="2022-01-01",
        end_date="2022-12-01",
        region={
            "dataset": "public-mpa-all",
            "id": "555745302",
            "buffer_operation": "DISSOLVE",
            "buffer_unit": "NAUTICALMILES",
            "buffer_value": "4",
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
async def test_fourwings_create_report_generate_region_daily_gridded_sar_presence_unmatched_chile(
    gfw_client: gfw.Client,
) -> None:
    """Test generating daily gridded SAR presence data with unmatched detections in Chile.

    This test verifies that the `create_report` method correctly retrieves
    daily gridded data for SAR (Search and Rescue) presence within the
    Exclusive Economic Zone (EEZ) of Chile, filtered to include only unmatched
    detections. It checks the structure and content of the returned data,
    ensuring it's a valid `FourWingsReportResult` and that the data can be
    converted to a pandas DataFrame.
    """
    result: FourWingsReportResult = await gfw_client.fourwings.create_report(
        spatial_resolution="HIGH",
        temporal_resolution="HOURLY",
        datasets=["public-global-sar-presence:latest"],
        start_date="2022-01-01",
        end_date="2022-01-06",
        filters=["matched='false'"],
        region={
            "dataset": "public-eez-areas",
            "id": "8465",
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
async def test_fourwings_create_report_generate_sar_vessel_detection_matched_eez(
    gfw_client: gfw.Client,
) -> None:
    """Test generating SAR vessel detection report filtered by matched=true in EEZ.

    This test verifies that the `create_report` method correctly retrieves SAR vessel
    detection data filtered by matched='true' within the Exclusive Economic Zone (EEZ).
    It checks the structure and content of the returned data, ensuring it's a valid
    `FourWingsReportResult` and that the data can be converted to a pandas DataFrame.
    """
    result: FourWingsReportResult = await gfw_client.fourwings.create_report(
        spatial_resolution="HIGH",
        temporal_resolution="HOURLY",
        group_by="VESSEL_ID",
        datasets=["public-global-sar-presence:latest"],
        start_date="2017-01-01",
        end_date="2017-01-02",
        filters=["matched='true'"],
        region={
            "dataset": "public-eez-areas",
            "id": "8492",
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
@pytest.mark.skip
async def test_fourwings_create_report_generate_ais_vessel_presence_daily_grouped_by_vessel_type(
    gfw_client: gfw.Client,
) -> None:
    """Test generating AIS vessel presence report grouped by vessel type in EEZ.

    This test verifies that the `create_report` method correctly retrieves daily AIS
    vessel presence data grouped by vessel type within the Exclusive Economic Zone (EEZ).
    It checks the structure and content of the returned data, ensuring it's a valid
    `FourWingsReportResult` and that the data can be converted to a pandas DataFrame.
    """
    result: FourWingsReportResult = await gfw_client.fourwings.create_report(
        spatial_resolution="LOW",
        temporal_resolution="DAILY",
        group_by="VESSEL_TYPE",
        datasets=["public-global-presence:latest"],
        start_date="2022-01-01",
        end_date="2022-05-01",
        region={
            "dataset": "public-eez-areas",
            "id": "5690",
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
async def test_fourwings_create_report_ais_vessel_presence_daily_filtered_by_cargo_and_carrier(
    gfw_client: gfw.Client,
) -> None:
    """Test retrieving AIS vessel presence report filtered by cargo and carrier vessel types via GET.

    This test verifies that the `create_report` method correctly retrieves AIS vessel presence data
    filtered by vessel types 'cargo' and 'carrier' within the Exclusive Economic Zone (EEZ).
    It checks the structure and content of the returned data, ensuring it's a valid
    `FourWingsReportResult` and that the data can be converted to a pandas DataFrame.
    """
    result: FourWingsReportResult = await gfw_client.fourwings.create_report(
        spatial_resolution="LOW",
        temporal_resolution="DAILY",
        group_by="FLAG",
        datasets=["public-global-presence:latest"],
        start_date="2022-01-01",
        end_date="2022-05-01",
        filters=["vessel_type in ('cargo','carrier')"],
        region={
            "dataset": "public-eez-areas",
            "id": "5690",
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
