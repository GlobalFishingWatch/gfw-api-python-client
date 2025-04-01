# Integration Tests

These tests verify the functionality of the `gfwapiclient` by making actual API calls to the Global Fishing Watch (GFW) API.

## Prerequisites

To run the integration tests, you must have the following environment variables set:

* `GFW_API_BASE_URL`: The base URL of the GFW API (i.e., stage or production base URL).
* `GFW_API_ACCESS_TOKEN`: A valid access token for the GFW API.

### Example Setup (Linux/macOS)

```bash
export GFW_API_BASE_URL="https://gateway.api.globalfishingwatch.org/v3/"
export GFW_API_ACCESS_TOKEN="<YOUR_GFW_API_ACCESS_TOKEN>"
```

### Example Setup (Windows)

```powershell
$env:GFW_API_BASE_URL = "https://gateway.api.globalfishingwatch.org/v3/"
$env:GFW_API_ACCESS_TOKEN = "<YOUR_GFW_API_ACCESS_TOKEN>"
```

## Running the Tests

To execute the integration tests, use the following `make` command:

```bash
make test-integration
```

This command will run all tests located within the `tests/integration` directory.

## Adding New Integration Tests

When adding new integration tests, please follow these guidelines:

1.  **Test Function Signature:**

    All integration tests **must** have the following signature:

    ```python
    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_{resource_name}_{resource_method}_{suffix}(gfw_client: gfw.Client) -> None:
        """Short description or title for the integration test.

        Brief description of the integration test.
        """
        # Implement integration tests
        # ...
    ```

    * `@pytest.mark.integration`: Marks the test as an integration test.
    * `@pytest.mark.asyncio`: Marks the test as an asynchronous test.
    * `gfw_client: gfw.Client`: An instance of the `gfw.Client` class, which provides access to the API resources.
    * `test_{resource_name}_{resource_method}_{suffix}`: Follows the naming convention described below.

2.  **Test Naming Convention:**

    All integration test function names **must** follow the following convention:

    `test_{resource_name}_{resource_method}_xxx`

    Where:

    * `{resource_name}`: Specifies the API resource being tested (e.g., `vessels`, `references`, `insights`, `fourwings`, etc.).
    * `{resource_method}`: Indicates the specific method within the resource being tested (e.g., `search_vessels`, etc.).
    * `xxx`: A descriptive suffix that provides more context about the test case (e.g., `basic`, etc.).

    **Example:**

    * `test_vessels_search_vessels_basic`: Tests a basic search operation for vessels.
    * `test_vessels_get_vessels_by_ids`: Tests the retrieval of multiple vessels by their IDs.

    This naming convention ensures consistency, readability, and maintainability of the integration tests.
