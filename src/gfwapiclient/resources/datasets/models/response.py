"""Global Fishing Watch (GFW) API Python Client - Datasets API Response Models."""

import datetime

from typing import Any, List, Optional, Type

from pydantic import Field, field_validator

from gfwapiclient.http.models.response import Result, ResultItem


__all__ = ["SARFixedInfrastructureItem", "SARFixedInfrastructureResult"]


class SARFixedInfrastructureItem(ResultItem):
    """SAR fixed infrastructure item.

    Attributes:
        structure_id (int):
            Unique identifier for all detections of the same structure.

        lat (Optional[float]):
            Latitude of the structure.

        lon (Optional[float]):
            Longitude of the structure.

        label (Optional[str]):
            Predicted structure type: `oil`, `wind`, or `unknown`.

        structure_start_date (Optional[datetime.datetime]):
            The first date the structure was detected.

        structure_end_date (Optional[datetime.datetime]):
            The last date the structure was detected.

        label_confidence (Optional[str]):
            Label confidence level: `high`, `medium`, or `low`.
    """

    structure_id: Optional[int] = Field(None)
    lat: Optional[float] = Field(None)
    lon: Optional[float] = Field(None)
    label: Optional[str] = Field(None)
    structure_start_date: Optional[datetime.datetime] = Field(None)
    structure_end_date: Optional[datetime.datetime] = Field(None)
    label_confidence: Optional[str] = None

    @field_validator("structure_start_date", "structure_end_date", mode="before")
    @classmethod
    def epoch_to_utc_datetime_or_none(cls, value: Any) -> Optional[Any]:
        """Convert an epoch timestamp (milliseconds) to a UTC `datetime` object or `None`.

        Args:
            value (Any):
                The epoch value (in milliseconds) to validate.

        Returns:
            Optional[datetime.datetime]:
                The validated and parsed UTC `datetime`, or `None` if the input was empty or None-like.
        """
        if not value:
            return None
        if isinstance(value, str) and value.strip() == "":
            return None

        # epoch to UTC datetime
        _timestamp = int(value) / 1000
        _datetime = datetime.datetime.fromtimestamp(
            _timestamp, tz=datetime.timezone.utc
        )
        return _datetime


class SARFixedInfrastructureResult(Result[SARFixedInfrastructureItem]):
    """Result for Get SAR fixed infrastructure API endpoint."""

    _result_item_class: Type[SARFixedInfrastructureItem]
    _data: List[SARFixedInfrastructureItem]

    def __init__(self, data: List[SARFixedInfrastructureItem]) -> None:
        """Initializes a new `FixedInfrastructureResult`.

        Args:
            data (List[SARFixedInfrastructureItem]):
                The list of SAR fixed infrastructure items.
        """
        super().__init__(data=data)
