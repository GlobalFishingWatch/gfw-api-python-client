"""Integration tests for the `gfwapiclient` Events API.

These tests verify the functionality of the Events API endpoints, ensuring they
correctly retrieve and process data related to maritime events like fishing,
encounters, and port visits. They cover various filtering scenarios based on
curl command examples, including geometry, region, and statistical queries.

For more details on the Events API, please refer to the official
Global Fishing Watch API documentation:

- `Events API Documentation <https://globalfishingwatch.org/our-apis/documentation#introduction-events-api>`_
"""

from typing import List, cast

import pandas as pd
import pytest

import gfwapiclient as gfw

from gfwapiclient.resources.events.detail.models.response import (
    EventDetailItem,
    EventDetailResult,
)
from gfwapiclient.resources.events.list.models.response import (
    EventListItem,
    EventListResult,
)
from gfwapiclient.resources.events.stats.models.response import (
    EventStatsItem,
    EventStatsResult,
)


@pytest.mark.integration
@pytest.mark.asyncio
async def test_events_get_all_events_get_fishing_events(gfw_client: gfw.Client) -> None:
    """Test retrieving fishing events with geometry and flags filters.

    This test verifies that the `get_all_events` method correctly retrieves
    fishing event data for a specified geographic area (polygon) and vessel
    flags. It checks the structure and content of the returned data, ensuring
    it's a valid `EventListResult` and that the data can be converted to a
    pandas DataFrame.
    """
    result: EventListResult = await gfw_client.events.get_all_events(
        datasets=["public-global-fishing-events:latest"],
        start_date="2017-01-01",
        end_date="2017-01-31",
        flags=["CHN"],
        geometry={
            "type": "Polygon",
            "coordinates": [
                [
                    [120.36621093749999, 26.725986812271756],
                    [122.36572265625, 26.725986812271756],
                    [122.36572265625, 28.323724553546015],
                    [120.36621093749999, 28.323724553546015],
                    [120.36621093749999, 26.725986812271756],
                ]
            ],
        },
        limit=1,
    )

    data: List[EventListItem] = cast(List[EventListItem], result.data())
    assert isinstance(result, EventListResult)
    assert len(data) >= 1, "Expected at least one event."
    assert isinstance(data[0], EventListItem)

    df: pd.DataFrame = cast(pd.DataFrame, result.df())
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 1, "Expected at least one row in the DataFrame."
    assert list(df.columns) == list(dict(data[0]).keys())


@pytest.mark.integration
@pytest.mark.asyncio
async def test_events_get_all_events_get_encounter_events(
    gfw_client: gfw.Client,
) -> None:
    """Test retrieving encounter events with geometry, vessels, and flags filters.

    This test verifies that the `get_all_events` method correctly retrieves
    encounter event data for a specified geographic area (polygon), vessel IDs,
    and flags. It checks the structure and content of the returned data, ensuring
    it's a valid `EventListResult` and that the data can be converted to a
    pandas DataFrame.
    """
    result: EventListResult = await gfw_client.events.get_all_events(
        datasets=["public-global-encounters-events:latest"],
        start_date="2017-01-01",
        end_date="2017-01-31",
        vessels=["55d38c0ee-e0d7-cb32-ac9c-8b3680d213b3"],
        flags=["TWN"],
        duration=60,
        geometry={
            "type": "Polygon",
            "coordinates": [
                [
                    [-130.9735107421875, -17.691128657307427],
                    [-130.4901123046875, -17.691128657307427],
                    [-130.4901123046875, -17.209017141391765],
                    [-130.9735107421875, -17.209017141391765],
                    [-130.9735107421875, -17.691128657307427],
                ]
            ],
        },
        limit=1,
    )

    data: List[EventListItem] = cast(List[EventListItem], result.data())
    assert isinstance(result, EventListResult)
    assert len(data) >= 1, "Expected at least one event."
    assert isinstance(data[0], EventListItem)

    df: pd.DataFrame = cast(pd.DataFrame, result.df())
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 1, "Expected at least one row in the DataFrame."
    assert list(df.columns) == list(dict(data[0]).keys())


@pytest.mark.integration
@pytest.mark.asyncio
async def test_events_get_all_events_get_loitering_events(
    gfw_client: gfw.Client,
) -> None:
    """Test retrieving loitering events with geometry, vessels, and flags filters.

    This test verifies that the `get_all_events` method correctly retrieves
    loitering event data for a specified geographic area (polygon), vessel IDs,
    and flags. It checks the structure and content of the returned data, ensuring
    it's a valid `EventListResult` and that the data can be converted to a
    pandas DataFrame.
    """
    result: EventListResult = await gfw_client.events.get_all_events(
        datasets=["public-global-loitering-events:latest"],
        start_date="2017-01-01",
        end_date="2017-01-31",
        vessels=["4850da803-3fd9-59ca-3683-8daa7b16d444"],
        flags=["KOR"],
        duration=60,
        geometry={
            "type": "Polygon",
            "coordinates": [
                [
                    [-60.6208, -45.5047],
                    [-60.5612, -45.5047],
                    [-60.5612, -45.4609],
                    [-60.6208, -45.4609],
                    [-60.6208, -45.5047],
                ]
            ],
        },
        limit=1,
    )

    data: List[EventListItem] = cast(List[EventListItem], result.data())
    assert isinstance(result, EventListResult)
    assert len(data) >= 1, "Expected at least one event."
    assert isinstance(data[0], EventListItem)

    df: pd.DataFrame = cast(pd.DataFrame, result.df())
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 1, "Expected at least one row in the DataFrame."
    assert list(df.columns) == list(dict(data[0]).keys())


@pytest.mark.integration
@pytest.mark.asyncio
async def test_events_get_all_events_get_port_visits(gfw_client: gfw.Client) -> None:
    """Test retrieving port visit events with geometry, vessels, and flags filters.

    This test verifies that the `get_all_events` method correctly retrieves
    port visit event data for a specified geographic area (polygon), vessel IDs,
    and flags. It checks the structure and content of the returned data, ensuring
    it's a valid `EventListResult` and that the data can be converted to a
    pandas DataFrame.
    """
    result: EventListResult = await gfw_client.events.get_all_events(
        datasets=["public-global-port-visits-events:latest"],
        start_date="2017-01-01",
        end_date="2017-01-31",
        vessels=["e0248aed9-99b4-bae7-6b87-ff0a3c464676"],
        flags=["ATG"],
        duration=60,
        geometry={
            "type": "Polygon",
            "coordinates": [
                [
                    [30.552978515625, 46.255846818480315],
                    [31.22314453125, 46.255846818480315],
                    [31.22314453125, 46.59661864884465],
                    [30.552978515625, 46.59661864884465],
                    [30.552978515625, 46.255846818480315],
                ]
            ],
        },
        limit=1,
    )

    data: List[EventListItem] = cast(List[EventListItem], result.data())
    assert isinstance(result, EventListResult)
    assert len(data) >= 1, "Expected at least one event."
    assert isinstance(data[0], EventListItem)

    df: pd.DataFrame = cast(pd.DataFrame, result.df())
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 1, "Expected at least one row in the DataFrame."
    assert list(df.columns) == list(dict(data[0]).keys())


@pytest.mark.integration
@pytest.mark.asyncio
async def test_events_get_all_events_get_fishing_events_senegal_eez(
    gfw_client: gfw.Client,
) -> None:
    """Test retrieving fishing events within Senegal EEZ.

    This test verifies that the `get_all_events` method correctly retrieves
    fishing event data within the EEZ of Senegal using a region filter.
    It checks the structure and content of the returned data, ensuring it's a
    valid `EventListResult` and that the data can be converted to a
    pandas DataFrame.
    """
    result: EventListResult = await gfw_client.events.get_all_events(
        datasets=["public-global-fishing-events:latest"],
        start_date="2020-10-01",
        end_date="2020-12-31",
        flags=["CHN"],
        region={
            "dataset": "public-eez-areas",
            "id": "8371",
        },
        limit=1,
    )

    data: List[EventListItem] = cast(List[EventListItem], result.data())
    assert isinstance(result, EventListResult)
    assert len(data) >= 1, "Expected at least one event."
    assert isinstance(data[0], EventListItem)

    df: pd.DataFrame = cast(pd.DataFrame, result.df())
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 1, "Expected at least one row in the DataFrame."
    assert list(df.columns) == list(dict(data[0]).keys())


@pytest.mark.integration
@pytest.mark.asyncio
async def test_events_get_event_by_id_get_port_visit(gfw_client: gfw.Client) -> None:
    """Test retrieving a port visit event by its ID.

    This test verifies that the `get_event_by_id` method correctly retrieves
    details for a specific port visit event using its unique ID. It checks the
    structure and content of the returned data, ensuring it's a valid
    `EventDetailResult` and that the data can be converted to a pandas DataFrame.
    """
    event_id = "c2f0967e061f99a01793edac065de003"
    result: EventDetailResult = await gfw_client.events.get_event_by_id(
        id=event_id,
        dataset="public-global-port-visits-events:latest",
    )

    data: EventDetailItem = cast(EventDetailItem, result.data())
    assert isinstance(result, EventDetailResult)
    assert isinstance(data, EventDetailItem)

    df: pd.DataFrame = cast(pd.DataFrame, result.df())
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1, "Expected one row in the DataFrame."
    assert list(df.columns) == list(dict(data).keys())


@pytest.mark.integration
@pytest.mark.asyncio
async def test_events_get_events_stats_get_encounters_stats(
    gfw_client: gfw.Client,
) -> None:
    """Test retrieving encounters statistics.

    This test verifies that the `get_events_stats` method correctly retrieves
    statistics for encounter events based on specified filters, including
    encounter types, vessel types, time range, flags, and duration. It checks
    the structure and content of the returned data, ensuring it's a valid
    `EventStatsResult` and that the data can be converted to a pandas DataFrame.
    """
    result: EventStatsResult = await gfw_client.events.get_events_stats(
        datasets=["public-global-encounters-events:latest"],
        encounter_types=["CARRIER-FISHING", "FISHING-CARRIER"],
        vessel_types=["CARRIER"],
        start_date="2018-01-01",
        end_date="2023-01-31",
        timeseries_interval="YEAR",
        flags=["RUS"],
        duration=60,
    )

    data: EventStatsItem = cast(EventStatsItem, result.data())
    assert isinstance(result, EventStatsResult)
    assert isinstance(data, EventStatsItem)

    df: pd.DataFrame = cast(pd.DataFrame, result.df())
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 1, "Expected at least one row in the DataFrame."
    assert list(df.columns) == list(dict(data).keys())


@pytest.mark.integration
@pytest.mark.asyncio
async def test_events_get_events_stats_get_port_visits_stats_senegal_eez(
    gfw_client: gfw.Client,
) -> None:
    """Test retrieving port visits statistics in Senegal EEZ.

    This test verifies that the `get_events_stats` method correctly retrieves
    statistics for port visit events within the Exclusive Economic Zone (EEZ)
    of Senegal, based on specified filters, including time range, timeseries
    interval, region, and confidence levels. It checks the structure and
    content of the returned data, ensuring it's a valid `EventStatsResult` and
    that the data can be converted to a pandas DataFrame.
    """
    result: EventStatsResult = await gfw_client.events.get_events_stats(
        datasets=["public-global-port-visits-events:latest"],
        start_date="2018-01-01",
        end_date="2019-01-31",
        timeseries_interval="YEAR",
        region={"dataset": "public-eez-areas", "id": "8371"},
        confidences=["3", "4"],
    )

    data: EventStatsItem = cast(EventStatsItem, result.data())
    assert isinstance(result, EventStatsResult)
    assert isinstance(data, EventStatsItem)

    df: pd.DataFrame = cast(pd.DataFrame, result.df())
    assert isinstance(df, pd.DataFrame)
    assert len(df) >= 1, "Expected at least one row in the DataFrame."
    assert list(df.columns) == list(dict(data).keys())
