"""Global Fishing Watch (GFW) API Python Client - Query Bulk Fixed Infrastructure Data Response Models."""

import datetime

from typing import Any, List, Optional, Type, Union

from pydantic import Field, field_validator

from gfwapiclient.resources.bulk_downloads.query.models.base.response import (
    BulkReportQueryItem,
    BulkReportQueryResult,
)


__all__ = [
    "BulkFixedInfrastructureDataQueryItem",
    "BulkFixedInfrastructureDataQueryResult",
]


class BulkFixedInfrastructureDataQueryItem(BulkReportQueryItem):
    """Result item for the fixed infrastructure data dataset.

    Represents a data record of a previously created fixed infrastructure data (i.e.,
    `public-fixed-infrastructure-data:latest` dataset) bulk report.

    For more details on the Query Bulk Report API endpoint supported response bodies,
    please refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/bulk-download/query-bulk-report

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/bulk-download/query-bulk-report#get-data-in-json-format---response-fields

    Attributes:
        detection_id (Optional[str]):
            Unique identifier (ID) of the satellite detection (e.g.,
            `"1AB_AD_MEDIAN_COMP"`).

        detection_date (Optional[datetime.datetime]):
            Date of the detection (e.g., `"2021-07-01"`).

        structure_id (Optional[Union[str, int]]):
            Unique identifier (ID) for all detections of the same structure (e.g.,
            `"162013"`).

        lat (Optional[float]):
            Latitude of the structure (e.g., `-151.608786096245`).

        lon (Optional[float]):
            Longitude of the structure (e.g., `60.8646485096125`).

        structure_start_date (Optional[datetime.datetime]):
            The first date the structure was detected (e.g., `"2017-01-01"`).

        structure_end_date (Optional[datetime.datetime]):
            The last date the structure was detected (e.g., `"2021-10-01"`).

        label (Optional[str]):
            Predicted structure type: `oil`, `wind`, or `unknown` (e.g., `"oil"`).

        label_confidence (Optional[str]):
            Label classification confidence level: `high`, `medium`, or `low` (e.g., `"high"`).
    """

    detection_id: Optional[str] = Field(None, alias="detection_id")
    detection_date: Optional[datetime.datetime] = Field(None, alias="detection_date")
    structure_id: Optional[Union[str, int]] = Field(None, alias="structure_id")
    lat: Optional[float] = Field(None, alias="lat")
    lon: Optional[float] = Field(None, alias="lon")
    structure_start_date: Optional[datetime.datetime] = Field(
        None, alias="structure_start_date"
    )
    structure_end_date: Optional[datetime.datetime] = Field(
        None, alias="structure_end_date"
    )
    label: Optional[str] = Field(None, alias="label")
    label_confidence: Optional[str] = Field(None, alias="label_confidence")

    @field_validator(
        "detection_date",
        "structure_start_date",
        "structure_end_date",
        mode="before",
    )
    @classmethod
    def empty_datetime_str_to_none(cls, value: Any) -> Optional[Any]:
        """Convert any empty datetime string to `None`.

        Args:
            value (Any):
                The value to validate.

        Returns:
            Optional[Any]:
                The validated datetime object or `None` if input is empty.
        """
        if isinstance(value, str) and value.strip() == "":
            return None
        return value


class BulkFixedInfrastructureDataQueryResult(
    BulkReportQueryResult[BulkFixedInfrastructureDataQueryItem]
):
    """Result for the Query Bulk fixed infrastructure data.

    Represents data records of a previously created fixed infrastructure data (i.e.,
    `public-fixed-infrastructure-data:latest` dataset) bulk report.

    For more details on the Query Bulk Report API endpoint supported response bodies,
    please refer to the official Global Fishing Watch API documentation:

    See: https://globalfishingwatch.org/our-apis/documentation/docs/v3/bulk-download/query-bulk-report

    Attributes:
        _result_item_class (Type[BulkFixedInfrastructureDataQueryItem]):
            The model used for individual result items.

        _data (List[BulkFixedInfrastructureDataQueryItem]):
            The bulk fixed infrastructure data report items returned in the response.
    """

    _result_item_class: Type[BulkFixedInfrastructureDataQueryItem]
    _data: List[BulkFixedInfrastructureDataQueryItem]

    def __init__(self, data: List[BulkFixedInfrastructureDataQueryItem]) -> None:
        """Initializes a new `FixedInfrastructureDataResult`.

        Args:
            data (List[BulkFixedInfrastructureDataQueryItem]):
                The list of bulk fixed infrastructure data report items.
        """
        super().__init__(data=data)
