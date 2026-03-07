"""Tests for `gfwapiclient.resources.references.resources`."""

import re

from typing import Any, Callable, Dict, List, Optional, Pattern, Union, cast

import pytest
import respx

from gfwapiclient.http.client import HTTPClient
from gfwapiclient.resources.references.regions.models.response import (
    EEZRegionItem,
    EEZRegionResult,
    MPARegionItem,
    MPARegionResult,
    RFMORegionItem,
    RFMORegionResult,
)
from gfwapiclient.resources.references.resources import ReferenceResource


@pytest.mark.asyncio
@pytest.mark.respx
async def test_reference_resource_get_eez_regions_success(
    mock_http_client: HTTPClient,
    mock_raw_eez_region_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `ReferenceResource` get eez regions succeeds with valid response."""
    mock_responsex.get("/datasets/public-eez-areas/context-layers").respond(
        200, json=[mock_raw_eez_region_item]
    )
    resource = ReferenceResource(http_client=mock_http_client)
    result = await resource.get_eez_regions()
    data = cast(List[EEZRegionItem], result.data())
    assert isinstance(result, EEZRegionResult)
    assert len(data) == 1
    assert isinstance(data[0], EEZRegionItem)


@pytest.mark.parametrize(
    "item_filters,matched_id,matched_size",
    [
        ({}, "8371", 1),
        ({"id": "8371"}, "8371", 1),
        ({"label": "Senegalese"}, "8371", 1),
        ({"iso3": "SEN"}, "8371", 1),
        ({"predicate": lambda item: item.id == "8371"}, "8371", 1),
        ({"id": " "}, None, 0),
        ({"id": "INVALID_VALUE"}, None, 0),
    ],
)
@pytest.mark.asyncio
@pytest.mark.respx
async def test_reference_resource_get_eez_regions_filter_success(
    mock_http_client: HTTPClient,
    mock_raw_eez_region_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
    item_filters: Dict[
        str,
        Union[
            str,
            Pattern[str],
            List[str],
            List[Pattern[str]],
            Callable[[EEZRegionItem], bool],
        ],
    ],
    matched_id: Optional[str],
    matched_size: int,
) -> None:
    """Test `ReferenceResource` get filtered eez regions succeeds with valid response."""
    mock_responsex.get("/datasets/public-eez-areas/context-layers").respond(
        200, json=[mock_raw_eez_region_item]
    )
    resource = ReferenceResource(http_client=mock_http_client)
    result = await resource.get_eez_regions(**item_filters)  # type: ignore[arg-type]
    data = cast(List[EEZRegionItem], result.data())
    assert isinstance(result, EEZRegionResult)
    assert len(data) == matched_size
    if matched_size >= 1:
        assert isinstance(data[0], EEZRegionItem)
        assert data[0].id == matched_id


@pytest.mark.asyncio
@pytest.mark.respx
async def test_reference_resource_get_mpa_regions_success(
    mock_http_client: HTTPClient,
    mock_raw_mpa_region_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `ReferenceResource` get mpa regions succeeds with valid response."""
    mock_responsex.get("/datasets/public-mpa-all/context-layers").respond(
        200, json=[mock_raw_mpa_region_item]
    )
    resource = ReferenceResource(http_client=mock_http_client)
    result = await resource.get_mpa_regions()
    data = cast(List[MPARegionItem], result.data())
    assert isinstance(result, MPARegionResult)
    assert len(data) == 1
    assert isinstance(data[0], MPARegionItem)


@pytest.mark.parametrize(
    "item_filters,matched_id,matched_size",
    [
        ({}, "555745302", 1),
        ({"id": "555745302"}, "555745302", 1),
        ({"label": "Dorsal de Nasca"}, "555745302", 1),
        ({"predicate": lambda item: item.id == "555745302"}, "555745302", 1),
        ({"id": " "}, None, 0),
        ({"id": "INVALID_VALUE"}, None, 0),
    ],
)
@pytest.mark.asyncio
@pytest.mark.respx
async def test_reference_resource_get_mpa_regions_filter_success(
    mock_http_client: HTTPClient,
    mock_raw_mpa_region_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
    item_filters: Dict[
        str,
        Union[
            str,
            Pattern[str],
            List[str],
            List[Pattern[str]],
            Callable[[MPARegionItem], bool],
        ],
    ],
    matched_id: Optional[str],
    matched_size: int,
) -> None:
    """Test `ReferenceResource` get filtered mpa regions succeeds with valid response."""
    mock_responsex.get("/datasets/public-mpa-all/context-layers").respond(
        200, json=[mock_raw_mpa_region_item]
    )
    resource = ReferenceResource(http_client=mock_http_client)
    result = await resource.get_mpa_regions(**item_filters)  # type: ignore[arg-type]
    data = cast(List[MPARegionItem], result.data())
    assert isinstance(result, MPARegionResult)
    assert len(data) == matched_size
    if matched_size >= 1:
        assert isinstance(data[0], MPARegionItem)
        assert data[0].id == matched_id


@pytest.mark.asyncio
@pytest.mark.respx
async def test_reference_resource_get_rfmo_regions_success(
    mock_http_client: HTTPClient,
    mock_raw_rfmo_region_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> None:
    """Test `ReferenceResource` get rfmo regions succeeds with valid response."""
    mock_responsex.get("/datasets/public-rfmo/context-layers").respond(
        200, json=[mock_raw_rfmo_region_item]
    )
    resource = ReferenceResource(http_client=mock_http_client)
    result = await resource.get_rfmo_regions()
    data = cast(List[RFMORegionItem], result.data())
    assert isinstance(result, RFMORegionResult)
    assert len(data) == 1
    assert isinstance(data[0], RFMORegionItem)


@pytest.mark.parametrize(
    "item_filters,matched_id,matched_size",
    [
        ({}, "ICCAT", 1),
        ({"id": "ICCAT"}, "ICCAT", 1),
        ({"label": "ICCAT"}, "ICCAT", 1),
        ({"predicate": lambda item: item.id == "ICCAT"}, "ICCAT", 1),
        ({"id": " "}, None, 0),
        ({"id": "INVALID_VALUE"}, None, 0),
    ],
)
@pytest.mark.asyncio
@pytest.mark.respx
async def test_reference_resource_get_rfmo_regions_filter_success(
    mock_http_client: HTTPClient,
    mock_raw_rfmo_region_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
    item_filters: Dict[
        str,
        Union[
            str,
            Pattern[str],
            List[str],
            List[Pattern[str]],
            Callable[[RFMORegionItem], bool],
        ],
    ],
    matched_id: Optional[str],
    matched_size: int,
) -> None:
    """Test `ReferenceResource` get filtered rfmo regions succeeds with valid response."""
    mock_responsex.get("/datasets/public-rfmo/context-layers").respond(
        200, json=[mock_raw_rfmo_region_item]
    )
    resource = ReferenceResource(http_client=mock_http_client)
    result = await resource.get_rfmo_regions(**item_filters)  # type: ignore[arg-type]
    data = cast(List[RFMORegionItem], result.data())
    assert isinstance(result, RFMORegionResult)
    assert len(data) == matched_size
    if matched_size >= 1:
        assert isinstance(data[0], RFMORegionItem)
        assert data[0].id == matched_id


@pytest.mark.parametrize(
    "item_filters,expected_match",
    [
        ({"id": "8371"}, True),
        ({"iso3": "SEN"}, True),
        ({"label": "Senegalese"}, True),
        ({"territory_1": "Senegal"}, True),
        ({"label": re.compile("senegal", re.I)}, True),
        ({"id": "8371", "iso3": "SEN"}, True),
        ({"id": "INVALID_VALUE"}, False),
        ({"iso3": "INVALID_VALUE"}, False),
        ({"id": "8371", "iso3": "INVALID_VALUE"}, False),
        ({"id": None}, False),
        ({"id": None, "iso3": None}, False),
        ({}, True),
    ],
)
def test_build_field_filters_predicate_correctly(
    mock_http_client: HTTPClient,
    mock_raw_eez_region_item: Dict[str, Any],
    item_filters: Dict[str, Union[str, Pattern[str], List[str], List[Pattern[str]]]],
    expected_match: bool,
) -> None:
    """Test that `ReferenceResource` build field filters predicate correctly."""
    resource = ReferenceResource(http_client=mock_http_client)
    region = EEZRegionItem(**mock_raw_eez_region_item)
    field_filters_predicate = resource._build_field_filters_predicate(
        item_filters=item_filters
    )

    assert field_filters_predicate(region) == expected_match


@pytest.mark.parametrize(
    "field_value,field_filters,expected_match",
    [
        ("SEN", "SEN", True),
        (" SEN ", ["SEN"], True),
        ("SEN", re.compile("SEN", re.I), True),
        ("SEN", [re.compile("SEN", re.I)], True),
        ("Senegalese", "SEN", True),
        ("SEN", ["INVALID_VALUE"], False),
        ("SEN", None, False),
        (None, ["SEN"], False),
        (None, [], False),
        (None, None, False),
    ],
)
def test_match_field_filters_correctly(
    mock_http_client: HTTPClient,
    field_value: Optional[str],
    field_filters: Union[str, Pattern[str], List[str], List[Pattern[str]]],
    expected_match: bool,
) -> None:
    """Test that `ReferenceResource` match field filters correctly."""
    resource = ReferenceResource(http_client=mock_http_client)
    match = resource._match_field_filters(
        field_value=field_value, field_filters=field_filters
    )

    assert match == expected_match


@pytest.mark.parametrize(
    "field_filter,expected_field_filters",
    [
        ("SEN", [re.compile("SEN", re.I)]),
        (["SEN"], [re.compile("SEN", re.I)]),
        (" SEN ", [re.compile("SEN", re.I)]),
        (re.compile("SEN", re.I), [re.compile("SEN", re.I)]),
        ([re.compile("SEN", re.I)], [re.compile("SEN", re.I)]),
        (None, []),
        (" ", []),
        ([None], []),
        ([" "], []),
    ],
)
def test_normalize_field_filter_correctly(
    mock_http_client: HTTPClient,
    field_filter: Union[str, Pattern[str], List[str], List[Pattern[str]]],
    expected_field_filters: List[Union[str, Pattern[str]]],
) -> None:
    """Test that `ReferenceResource` normalize field filter correctly."""
    resource = ReferenceResource(http_client=mock_http_client)
    field_filters = resource._normalize_field_filter(field_filter=field_filter)

    assert field_filters == expected_field_filters
    assert all(isinstance(field_filter, re.Pattern) for field_filter in field_filters)
