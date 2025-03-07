"""Global Fishing Watch (GFW) API Python Client - 4Wings Report API Request Models."""

import datetime

from typing import Any, List, Optional, Type

from pydantic import Field, field_validator

from gfwapiclient.http.models import Result, ResultItem


__all__ = ["FourWingsReportItem", "FourWingsReportResult"]


class FourWingsReportItem(ResultItem):
    """4Wings report entry."""

    date: Optional[str] = Field(None, alias="date")
    detections: Optional[int] = Field(None, alias="detections")
    flag: Optional[str] = Field(None, alias="flag")
    gear_type: Optional[str] = Field(None, alias="geartype")
    hours: Optional[float] = Field(None, alias="hours")
    vessel_ids: Optional[int] = Field(None, alias="vesselIDs")
    vessel_id: Optional[str] = Field(None, alias="vesselId")
    vessel_type: Optional[str] = Field(None, alias="vesselType")
    entry_timestamp: Optional[datetime.datetime] = Field(None, alias="entryTimestamp")
    exit_timestamp: Optional[datetime.datetime] = Field(None, alias="exitTimestamp")
    first_transmission_date: Optional[datetime.datetime] = Field(
        None, alias="firstTransmissionDate"
    )
    last_transmission_date: Optional[datetime.datetime] = Field(
        None, alias="lastTransmissionDate"
    )
    imo: Optional[str] = Field(None, alias="imo")
    mmsi: Optional[str] = Field(None, alias="mmsi")
    call_sign: Optional[str] = Field(None, alias="callsign")
    dataset: Optional[str] = Field(None, alias="dataset")
    report_dataset: Optional[str] = Field(
        None, alias="report_dataset"
    )  # used dataset to create the style (report)
    ship_name: Optional[str] = Field(None, alias="shipName")
    lat: Optional[float] = Field(None, alias="lat")
    lon: Optional[float] = Field(None, alias="lon")
    # TODO: derive geometry (lat, lon) to shapely.Point

    @field_validator(
        "entry_timestamp",
        "exit_timestamp",
        "first_transmission_date",
        "last_transmission_date",
        mode="before",
    )
    @classmethod
    def empty_datetime_str_to_none(cls, value: Any) -> Optional[Any]:
        """Convert any empty datetime string to `None`."""
        if isinstance(value, str) and value.strip() == "":
            return None
        return value


class FourWingsReportResult(Result[FourWingsReportItem]):
    """Result for 4Wings Report API endpoint."""

    _result_item_class: Type[FourWingsReportItem]
    _data: List[FourWingsReportItem]

    def __init__(self, data: List[FourWingsReportItem]) -> None:
        """Initializes a new `FourWingsReportResult`."""
        self._data = data
