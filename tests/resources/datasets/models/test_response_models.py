"""Tests for `gfwapiclient.resources.datasets.models.response`."""

from typing import Any, Dict, List, cast

from gfwapiclient.resources.datasets.models.response import (
    SARFixedInfrastructureItem,
    SARFixedInfrastructureResult,
)


def test_datasets_sar_fixed_infrastructure_item_deserializes_all_fields(
    mock_raw_sar_fixed_infrastructure_item: Dict[str, Any],
) -> None:
    """Test that `SARFixedInfrastructureItem` correctly deserializes all defined fields."""
    sar_fixed_infrastructure_item: SARFixedInfrastructureItem = (
        SARFixedInfrastructureItem(**mock_raw_sar_fixed_infrastructure_item)
    )
    assert sar_fixed_infrastructure_item.structure_id is not None
    assert sar_fixed_infrastructure_item.lat is not None
    assert sar_fixed_infrastructure_item.lon is not None
    assert sar_fixed_infrastructure_item.label is not None
    assert sar_fixed_infrastructure_item.label_confidence is not None
    assert sar_fixed_infrastructure_item.structure_start_date is not None
    assert sar_fixed_infrastructure_item.structure_end_date is not None


def test_datasets_sar_fixed_infrastructure_item_deserializes_empty_epoch_fields(
    mock_raw_sar_fixed_infrastructure_item: Dict[str, Any],
) -> None:
    """Test that `SARFixedInfrastructureItem` correctly handles and deserializes empty epoch time fields."""
    sar_fixed_infrastructure_item: SARFixedInfrastructureItem = (
        SARFixedInfrastructureItem(
            **{
                **mock_raw_sar_fixed_infrastructure_item,
                "structure_start_date": " ",
                "structure_end_date": None,
            }
        )
    )
    assert sar_fixed_infrastructure_item.structure_id is not None
    assert sar_fixed_infrastructure_item.lat is not None
    assert sar_fixed_infrastructure_item.lon is not None
    assert sar_fixed_infrastructure_item.label is not None
    assert sar_fixed_infrastructure_item.label_confidence is not None
    assert sar_fixed_infrastructure_item.structure_start_date is None
    assert sar_fixed_infrastructure_item.structure_end_date is None


def test_datasets_sar_fixed_infrastructure_result_deserializes_all_fields(
    mock_raw_sar_fixed_infrastructure_item: Dict[str, Any],
) -> None:
    """Test that `SARFixedInfrastructureResult` correctly deserializes its data field."""
    data: List[SARFixedInfrastructureItem] = [
        SARFixedInfrastructureItem(**mock_raw_sar_fixed_infrastructure_item)
    ]
    result = SARFixedInfrastructureResult(data=data)
    assert cast(List[SARFixedInfrastructureItem], result.data()) == data
