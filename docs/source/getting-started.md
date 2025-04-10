# Getting Started

This guide introduces you to the basics of using the [gfw-api-python-client](https://github.com/GlobalFishingWatch/gfw-api-python-client). For detailed and alternative installation instructions, please refer to the [Installation](installation) section. Here is a [Jupyter Notebook](https://github.com/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/getting-started.ipynb) version for this guide.

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

## Installation

The `gfw-api-python-client` can be easily installed using pip:

```bash
pip install gfw-api-python-client
```

For more detailed installation instructions, including setting up a virtual environment, please see the dedicated [Installation](installation) section.

## Basic Usage

Once installed, you can import and use `gfw-api-python-client` in your Python codes:

```python
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

## Making API Requests

### Searching for a Vessel by MMSI

```python
vessel_search_result = await gfw_client.vessels.search_vessels(
    query="368045130",
    datasets=["public-global-vessel-identity:latest"],
    includes=["MATCH_CRITERIA", "OWNERSHIP", "AUTHORIZATIONS"],
)

vessel_ids = [
    self_reported_info.id
    for vessel in vessel_search_result.data()
    for self_reported_info in vessel.self_reported_info
]

print(vessel_ids)
```

**Output:**

```
["3312b30d6-65b6-1bdb-6a78-3f5eb3977e58", "126221ace-e3b5-f4ed-6150-394809737c55"]
```

### Getting Fishing Events for the Searched Vessels

```python
events_result = await gfw_client.events.get_all_events(
    datasets=["public-global-fishing-events:latest"],
    start_date="2024-03-01",
    end_date="2025-03-31",
    vessels=vessel_ids,
)

events_df = events_result.df()

print(events_df.info())
```

Output:
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 14 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   start         3 non-null      datetime64[ns, UTC]
 1   end           3 non-null      datetime64[ns, UTC]
 2   id            3 non-null      object
 3   type          3 non-null      object
 4   position      3 non-null      object
 5   regions       3 non-null      object
 6   bounding_box  3 non-null      object
 7   distances     3 non-null      object
 8   vessel        3 non-null      object
 9   encounter     0 non-null      object
 10  fishing       3 non-null      object
 11  gap           0 non-null      object
 12  loitering     0 non-null      object
 13  port_visit    0 non-null      object
dtypes: datetime64[ns, UTC](2), object(12)
memory usage: 468.0+ bytes
```

## Next Steps

This guide has provided you with the fundamental steps to install and use the `gfw-api-python-client` for making basic API requests.

To further explore the capabilities of our APIs (`4Wings`, `Vessels`, `Events`, `Insights`, `References`, etc.), please refer to the detailed [Usage Guides](usage-guides/index). These guides delve into specific use cases and demonstrate how to effectively leverage the `gfw-api-python-client` for your data exploration needs.

Happy coding and data exploring!
