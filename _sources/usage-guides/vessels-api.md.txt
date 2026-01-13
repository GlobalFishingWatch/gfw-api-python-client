# Vessels API

<a href="https://colab.research.google.com/github/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/usage-guides/vessels-api.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

This guide provides detailed instructions on how to use the [gfw-api-python-client](https://github.com/GlobalFishingWatch/gfw-api-python-client) to access information about vessels. The [Vessels API](https://globalfishingwatch.org/our-apis/documentation#vessels-api) allows you to search for vessels, retrieve lists of vessels by their IDs, and get detailed information for a specific vessel, drawing from various datasets like identity, authorizations, and ownership. Here is a [Jupyter Notebook](https://github.com/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/usage-guides/vessels-api.ipynb) version of this guide with more usage examples.

> **Note:** See the [Datasets](https://globalfishingwatch.org/our-apis/documentation#api-dataset), [Vessel Data Caveats](https://globalfishingwatch.org/our-apis/documentation#vessel-api-vessel-identity-information), and [Terms of Use](https://globalfishingwatch.org/our-apis/documentation#terms-of-use) pages in the [GFW API documentation](https://globalfishingwatch.org/our-apis/documentation#introduction) for details on GFW data, API licenses, and rate limits.

## Prerequisites

- Before using the `gfw-api-python-client`, ensure it is installed (see the [Getting Started](../getting-started) guide) and that you have obtained an API access token from the [Global Fishing Watch API portal](https://globalfishingwatch.org/our-apis/tokens).

## Getting Started

To interact with the Vessels endpoints, you first need to instantiate the `gfw.Client` and then access the `vessels` resource:

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

The `gfw_client.vessels` object provides methods to search for and retrieve vessel information. Each of these methods returns a `result` object, which offers convenient ways to access the data as Pydantic models using `.data()` or as pandas DataFrames using `.df()`.

> **Tip:** Use [IPython](https://ipython.readthedocs.io/en/stable/) or Python 3.11+ with `python -m asyncio` to run `gfw-api-python-client` code interactively, as these environments support executing `async` / `await` expressions directly in the console.

## Searching for Vessels (`search_vessels`)

The `search_vessels()` method allows you to find vessels based on a query and various filters within specified datasets.

```python
vessel_search_result = await gfw_client.vessels.search_vessels(
    where="ssvid='775998121' AND shipname='DON TITO'",
    includes=["MATCH_CRITERIA", "OWNERSHIP"],
)
```

### Access the list of vessel as Pydantic models

```python
vessel_search_data = vessel_search_result.data()
vessel = vessel_search_data[-1]
print((vessel.dataset, vessel.self_reported_info[-1].id))
print(vessel.model_dump())
```

**Output:**

```
('public-global-vessel-identity:v3.0', 'c54923e64-46f3-9338-9dcb-ff09724077a3')
```

### Access the vessels as a DataFrame

```python
vessel_search_df = vessel_search_result.df()
print(vessel_search_df.info())
print(vessel_search_df.head())
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2 entries, 0 to 1
Data columns (total 8 columns):
 #   Column                          Non-Null Count  Dtype
---  ------                          --------------  -----
 0   dataset                         2 non-null      object
 1   registry_info_total_records     2 non-null      int64
 2   registry_info                   2 non-null      object
 3   registry_owners                 2 non-null      object
 4   registry_public_authorizations  0 non-null      object
 5   combined_sources_info           2 non-null      object
 6   self_reported_info              2 non-null      object
 7   matchCriteria                   2 non-null      object
dtypes: int64(1), object(7)
memory usage: 260.0+ bytes
```

## Getting a List of Vessels by IDs (`get_vessels_by_ids`)

The `get_vessels_by_ids()` method retrieves information for a list of vessels given their GFW Vessel IDs.

```python
vessels_result = await gfw_client.vessels.get_vessels_by_ids(
    ids=[
        "8c7304226-6c71-edbe-0b63-c246734b3c01",
        "6583c51e3-3626-5638-866a-f47c3bc7ef7c",
        "71e7da672-2451-17da-b239-857831602eca",
    ],
)
```

### Access the list of vessel as Pydantic models

```python
vessels_data = vessels_result.data()
vessel = vessels_data[-1]
print((vessel.dataset, vessel.self_reported_info[-1].id))
print(vessel.model_dump())
```

**Output:**

```
('public-global-vessel-identity:v3.0', 'aca119c29-95dd-f5c4-2057-ee45268dcd6f')
```

### Access the vessels as a DataFrame

```python
vessel_search_df = vessels_result.df()
print(vessel_search_df.info())
print(vessel_search_df.head())
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 7 columns):
 #   Column                          Non-Null Count  Dtype
---  ------                          --------------  -----
 0   dataset                         3 non-null      object
 1   registry_info_total_records     3 non-null      int64
 2   registry_info                   3 non-null      object
 3   registry_owners                 3 non-null      object
 4   registry_public_authorizations  3 non-null      object
 5   combined_sources_info           3 non-null      object
 6   self_reported_info              3 non-null      object
dtypes: int64(1), object(6)
memory usage: 300.0+ bytes
```

## Getting a Vessel by ID (`get_vessel_by_id`)

The `get_vessel_by_id()` method retrieves detailed information for a specific vessel using its GFW Vessel ID.

```python
vessel_result = await gfw_client.vessels.get_vessel_by_id(
    id="c54923e64-46f3-9338-9dcb-ff09724077a3",
)
```

### Access the vessel as Pydantic model

```python
vessel = vessel_result.data()
print((vessel.dataset, vessel.self_reported_info[-1].id))
print(vessel.model_dump())
```

**Output:**

```
('public-global-vessel-identity:v3.0', 'c54923e64-46f3-9338-9dcb-ff09724077a3')
```

### Access the vessel as a DataFrame

```python
vessel_df = vessel_result.df()
print(vessel_df.info())
print(vessel_df.head())
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1 entries, 0 to 0
Data columns (total 7 columns):
 #   Column                          Non-Null Count  Dtype
---  ------                          --------------  -----
 0   dataset                         1 non-null      object
 1   registry_info_total_records     1 non-null      int64
 2   registry_info                   1 non-null      object
 3   registry_owners                 1 non-null      object
 4   registry_public_authorizations  1 non-null      object
 5   combined_sources_info           1 non-null      object
 6   self_reported_info              1 non-null      object
dtypes: int64(1), object(6)
memory usage: 188.0+ bytes
```

## Next Steps

Explore the [Usage Guides](index) and [Workflow Guides](../workflow-guides/index) for other API resources to understand how you can combine vessel data with information about events, and more. Check out the following resources:

- [4Wings API](4wings-api)
- [Events API](events-api)
- [Insights API](insights-api)
- [Datasets API](datasets-api)
- [Bulk Download API](bulk-downloads-api)
- [Reference Data API](references-data-api)
