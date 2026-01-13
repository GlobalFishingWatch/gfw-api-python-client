# Getting Started

<a href="https://colab.research.google.com/github/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/getting-started.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

This guide introduces you to the basics of using the [gfw-api-python-client](https://github.com/GlobalFishingWatch/gfw-api-python-client). For detailed and alternative installation instructions, please refer to the [Installation](installation) section. Here is a [Jupyter Notebook](https://github.com/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/getting-started.ipynb) version for this guide.

> **Note:** See the [Datasets](https://globalfishingwatch.org/our-apis/documentation#api-dataset), [Data Caveats](https://globalfishingwatch.org/our-apis/documentation#data-caveat), and [Terms of Use](https://globalfishingwatch.org/our-apis/documentation#terms-of-use) pages in the [GFW API documentation](https://globalfishingwatch.org/our-apis/documentation#introduction) for details on GFW data, API licenses, and rate limits.

## Authorization

Before using the `gfw-api-python-client`, you need to obtain an API access token from the [Global Fishing Watch API portal](https://globalfishingwatch.org/our-apis/tokens). This token is crucial for authenticating your requests. For security and convenience, it's highly recommended to set your access token as an environment variable.

### Linux/macOS

```bash
export GFW_API_ACCESS_TOKEN="<PASTE_YOUR_GFW_API_ACCESS_TOKEN_HERE>"
```

### Windows

```powershell
$env:GFW_API_ACCESS_TOKEN = "<PASTE_YOUR_GFW_API_ACCESS_TOKEN_HERE>"
```

### Google Colaboratory

1.  Click the **key icon** (🔑) in the left sidebar to open **Secrets**.
2.  Add a new secret named `GFW_API_ACCESS_TOKEN`.
3.  Paste your API access token as the **value** and enable **Notebook access**.

![Google Colaboratory Authorization](_static/google-colaboratory-authorization.png)

## Installation

The `gfw-api-python-client` can be easily installed using pip:

```bash
pip install gfw-api-python-client
```

For more detailed installation instructions, including setting up a virtual environment, please see the dedicated [Installation](installation) section.

## Basic Usage

<a href="https://colab.research.google.com/github/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/getting-started.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

Once installed, you can import and use `gfw-api-python-client` in your Python codes:

```python
import datetime
import os

import gfwapiclient as gfw


access_token = os.environ.get(
    "GFW_API_ACCESS_TOKEN",
    "<OR_PASTE_YOUR_GFW_API_ACCESS_TOKEN_HERE>",
)

gfw_client = gfw.Client(
    access_token=access_token,
)
```

> **Important:** The `gfw-api-python-client` is **async-first**: all API methods are asynchronous and must be executed using Python's `async` / `await` syntax. **Environments with built-in async support** (e.g., _Jupyter Notebook_, _Google Colab_, and async web frameworks such as _FastAPI_) can call client methods directly using `await`, with no additional setup. **Environments without built-in async support** (e.g., _plain Python scripts_, _Python modules_, or synchronous web frameworks such as _Flask_ and _Django_) must explicitly run asynchronous code using an event loop. This can be done with tools such as [`asyncio.run`](https://docs.python.org/3/library/asyncio.html), [`trio.run`](https://trio.readthedocs.io/en/stable/), [`anyio.run`](https://anyio.readthedocs.io/en/stable/), or framework-specific async integration.

> **Tip:** Use [IPython](https://ipython.readthedocs.io/en/stable/) or Python 3.11+ with `python -m asyncio` to run `gfw-api-python-client` code interactively, as these environments support executing `async` / `await` expressions directly in the console.

## Making API Requests

### Searching for a Vessel by MMSI

```python
vessel_search_result = await gfw_client.vessels.search_vessels(
    query="412331038",
)

vessel_search_ids = [
    self_reported_info.id
    for vessel_search_item in vessel_search_result.data()
    if vessel_search_item.registry_info_total_records >= 1
    for self_reported_info in vessel_search_item.self_reported_info
]

print(vessel_search_ids)
```

**Output:**

```
['755a48dd4-4bee-4bcf-7b5f-9baea058fc7b', '3dad49b0b-b2e0-9347-0c4c-e39fea560f9f']
```

**Note:** It is recommended to prioritize vessels that include both `registry_info` and `self_reported_info` (AIS), as this indicates a successful match between registry data and AIS information.

### Getting Details of Vessels Filtered by Vessel Searched IDs

```python
vessels_result = await gfw_client.vessels.get_vessels_by_ids(
    ids=vessel_search_ids,
)

vessel_self_reported_infos = [
    self_reported_info
    for vessel_item in vessels_result.data()
    for self_reported_info in vessel_item.self_reported_info
]

vessel_ids = [
    self_reported_info.id for self_reported_info in vessel_self_reported_infos
]

print(vessel_ids)
```

**Output:**

```
['755a48dd4-4bee-4bcf-7b5f-9baea058fc7b', '3dad49b0b-b2e0-9347-0c4c-e39fea560f9f']
```

### Getting Insights Related to Fishing Events for the Vessel Searched

**Important:** `start_date` must be on or after `January 1, 2020`

```python
start_datetime = min(
    [
        self_reported_info.transmission_date_from
        for self_reported_info in vessel_self_reported_infos
    ]
)
start_date = start_datetime.date()
start_date = max(start_date, datetime.date.fromisoformat("2020-01-01"))


end_datetime = max(
    [
        self_reported_info.transmission_date_to
        for self_reported_info in vessel_self_reported_infos
    ]
)
end_date = end_datetime.date()

dataset_id = "public-global-vessel-identity:latest"
dataset_ids_vessel_ids = [
    {"dataset_id": dataset_id, "vessel_id": vessel_id} for vessel_id in vessel_ids
]

insights_result = await gfw_client.insights.get_vessel_insights(
    includes=["FISHING"],
    start_date=start_date,
    end_date=end_date,
    vessels=dataset_ids_vessel_ids,
)

insights_df = insights_result.df()

print(insights_df.info())
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1 entries, 0 to 0
Data columns (total 6 columns):
 #   Column                       Non-Null Count  Dtype
---  ------                       --------------  -----
 0   period                       1 non-null      object
 1   vessel_ids_without_identity  0 non-null      object
 2   gap                          0 non-null      object
 3   coverage                     0 non-null      object
 4   apparent_fishing             1 non-null      object
 5   vessel_identity              0 non-null      object
dtypes: object(6)
memory usage: 180.0+ bytes
```

```python
insights_data = insights_result.data()

print(dict(insights_data.apparent_fishing.period_selected_counters))
```

**Output:**

```
{'events': 398, 'events_gap_off': None, 'events_in_rfmo_without_known_authorization': 144, 'events_in_no_take_mpas': 0}
```

### Getting Fishing Events for the Vessels Searched

```python
events_result = await gfw_client.events.get_all_events(
    datasets=["public-global-fishing-events:latest"],
    start_date=start_date,
    end_date=end_date,
    vessels=vessel_ids,
)

events_df = events_result.df()

print(events_df.info())
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 398 entries, 0 to 397
Data columns (total 14 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   start         398 non-null    datetime64[ns, UTC]
 1   end           398 non-null    datetime64[ns, UTC]
 2   id            398 non-null    object
 3   type          398 non-null    object
 4   position      398 non-null    object
 5   regions       398 non-null    object
 6   bounding_box  398 non-null    object
 7   distances     398 non-null    object
 8   vessel        398 non-null    object
 9   encounter     0 non-null      object
 10  fishing       398 non-null    object
 11  gap           0 non-null      object
 12  loitering     0 non-null      object
 13  port_visit    0 non-null      object
dtypes: datetime64[ns, UTC](2), object(12)
memory usage: 43.7+ KB
```

## Next Steps

This guide has provided you with the fundamental steps to install and use the `gfw-api-python-client` for making basic API requests.

To further explore the capabilities of our APIs (`4Wings`, `Vessels`, `Events`, `Insights`, `Datasets`, `Bulk Download`, `References`, etc.), please refer to the detailed [Usage Guides](usage-guides/index) and [Workflow Guides](workflow-guides/index). These guides delve into specific use cases and demonstrate how to effectively leverage the `gfw-api-python-client` for your data exploration needs.

Happy coding and data exploring!
