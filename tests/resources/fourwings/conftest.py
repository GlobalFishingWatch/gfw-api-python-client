"""Test configurations for `gfwapiclient.resources.fourwings`."""

from typing import Any, Callable, Dict, Optional

import pytest
import respx


@pytest.fixture
def mock_raw_fourwings_report_request_params(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for mock raw four wings report request params.

    Returns:
        Dict[str, Any]:
            Raw `FourWingsReportParams` sample data.
    """
    raw_fourwings_report_request_params: Dict[str, Any] = load_json_fixture(
        "fourwings/fourwings_report_request_params.json"
    )
    return raw_fourwings_report_request_params


@pytest.fixture
def mock_raw_fourwings_report_request_body(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for mock raw four wings report request body.

    Returns:
        Dict[str, Any]:
            Raw `FourWingsReportBody` sample data.
    """
    raw_fourwings_report_request_body: Dict[str, Any] = load_json_fixture(
        "fourwings/fourwings_report_request_body.json"
    )
    return raw_fourwings_report_request_body


@pytest.fixture
def mock_raw_fourwings_report_item(
    load_json_fixture: Callable[[str], Dict[str, Any]],
) -> Dict[str, Any]:
    """Fixture for mock raw four wings report item.

    Returns:
        Dict[str, Any]:
            Raw `FourWingsReportItem` sample data.
    """
    raw_four_wings_report_item: Dict[str, Any] = load_json_fixture(
        "fourwings/fourwings_report_item.json"
    )
    return raw_four_wings_report_item


@pytest.fixture
def mock_raw_fourwings_report_standard_request_params(
    mock_raw_fourwings_report_request_params: Dict[str, Any],
    mock_raw_fourwings_report_request_body: Dict[str, Any],
) -> Dict[str, Any]:
    """Fixture for mock standard combined raw four wings report request params.

    Provides a standard combined mock raw four wings report request parameters,
    excluding the `"datasets"` key from the original parameters and adding fixed
    start and end dates.

    Args:
        mock_raw_fourwings_report_request_params (Dict[str, Any]):
            Mock raw `FourWingsReportParams` sample data.

        mock_raw_fourwings_report_request_body (Dict[str, Any]):
            Mock raw `FourWingsReportBody` sample data.

    Returns:
        Dict[str, Any]:
            Combined raw `FourWingsReportParams` and `FourWingsReportBody` sample data.
    """
    start_date: str = "2021-01-01"
    end_date: str = "2021-01-15"

    mock_raw_fourwings_report_filtered_request_params: Dict[str, Any] = {
        k: v
        for k, v in mock_raw_fourwings_report_request_params.items()
        if k != "datasets"
    }

    mock_raw_fourwings_report_combined_request_params: Dict[str, Any] = {
        **mock_raw_fourwings_report_filtered_request_params,
        **mock_raw_fourwings_report_request_body,
        "start_date": start_date,
        "end_date": end_date,
    }

    return mock_raw_fourwings_report_combined_request_params


@pytest.fixture
def mock_raw_fourwings_report_standard_response(
    mock_raw_fourwings_report_item: Dict[str, Any],
    mock_responsex: respx.MockRouter,
) -> Callable[[Optional[str]], None]:
    """Fixture for mock standard raw four wings report response body.

    Returns a function to mock a standard four wings report HTTP response body
    for the given dataset. Uses the `"dataset"` from the mock report item if none is provided.

    Args:
        mock_raw_fourwings_report_item (Dict[str, Any]):
            Mock raw `FourWingsReportItem` sample data.

        mock_responsex (respx.MockRouter):
            Mock respx router instance.

    Returns:
        Callable[[Optional[str]], None]:
            A function which when called with an optional dataset,
            sets up a mocked HTTP response.
    """

    def _mock_raw_fourwings_report_standard_response(
        dataset: Optional[str] = None,
    ) -> None:
        """Mocks the HTTP POST response for the four wings report endpoint.

        Args:
            dataset (Optional[str]):
                The dataset to use in the mock response.
                Defaults to the dataset from the mock report item if `None`.

        Returns:
            None
        """
        _dataset: str = dataset or mock_raw_fourwings_report_item["report_dataset"]
        mock_responsex.post("4wings/report").respond(
            status_code=200,
            json={
                "entries": [
                    {
                        _dataset: [
                            {
                                **mock_raw_fourwings_report_item,
                                "report_dataset": _dataset,
                            }
                        ]
                    }
                ]
            },
        )

    return _mock_raw_fourwings_report_standard_response
