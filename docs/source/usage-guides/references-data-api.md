# Reference Data API

This guide provides detailed instructions on how to use the [gfw-api-python-client](https://github.com/GlobalFishingWatch/gfw-api-python-client) to access reference data, specifically geographic regions. The Reference Data API offers access to static datasets, currently focusing on Exclusive Economic Zones (EEZs), Marine Protected Areas (MPAs), and Regional Fisheries Management Organizations (RFMOs). Here is a [Jupyter Notebook](https://github.com/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/usage-guides/references-data-api.ipynb) version of this guide with more usage examples.

## Prerequisites

- You have installed the `gfw-api-python-client`. Refer to the [Getting Started](../getting-started) guide for installation instructions.

## Getting Started

To interact with the Regions endpoints, you first need to instantiate the `gfw.Client` and then access the `references` resource:

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

The `gfw_client.references` object provides methods to retrieve different types of geographic regions. Each of these methods returns a `result` object, which offers convenient ways to access the data as Pydantic models using `.data()` or as pandas DataFrames using `.df()`.

## Retrieving Exclusive Economic Zones (EEZs)

To get a list of available Exclusive Economic Zone (EEZ) regions, use the `get_eez_regions()` method:

```python
eez_regions_result = await gfw_client.references.get_eez_regions()
```

### Access the list of EEZ region as Pydantic models

```python
eez_regions_data = eez_regions_result.data()
eez_region = eez_regions_data[-1]
print((eez_region.id, eez_region.dataset))
print(eez_region.model_dump())
```

**Output:**

```
(26523, 'public-eez-areas')
{'id': 26523, 'label': 'Turkmenistan', 'iso3': 'TKM', 'dataset': 'public-eez-areas'}
```

### Access the EEZ regions as a DataFrame

```python
eez_regions_df = eez_regions_result.df()
print(eez_regions_df.info())
print(eez_regions_df[["id", "dataset"]].head())
```

**Output:**

```
class 'pandas.core.frame.DataFrame'>
RangeIndex: 282 entries, 0 to 281
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   id       281 non-null    float64
 1   label    282 non-null    object
 2   iso3     282 non-null    object
 3   dataset  282 non-null    object
dtypes: float64(1), object(3)
memory usage: 8.9+ KB
```

## Retrieving Marine Protected Areas (MPAs)

To get a list of available Marine Protected Area (MPA) regions, use the `get_mpa_regions()` method:

```python
mpa_regions_result = await gfw_client.references.get_mpa_regions()
```

### Access the list of MPA region as Pydantic models

```python
mpa_regions_data = mpa_regions_result.data()
mpa_region = mpa_regions_data[-1]
print((mpa_region.id, mpa_region.dataset))
print(mpa_region.model_dump())
```

**Output:**

```
('555790281', 'public-mpa-all')
{'id': '555790281', 'label': 'Iles Barren - Aire protegee', 'name': 'Iles Barren', 'dataset': 'public-mpa-all'}
```

### Access the MPA regions as a DataFrame

```python
mpa_regions_df = mpa_regions_result.df()
print(mpa_regions_df.info())
print(mpa_regions_df[["id", "dataset"]].head())
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 16621 entries, 0 to 16620
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   id       16621 non-null  object
 1   label    16621 non-null  object
 2   name     16621 non-null  object
 3   dataset  16621 non-null  object
dtypes: object(4)
memory usage: 519.5+ K
```

## Retrieving Regional Fisheries Management Organizations (RFMOs)

To get a list of available Regional Fisheries Management Organization (RFMO) regions, use the `get_rfmo_regions()` method:

```python
rfmo_regions_result = await gfw_client.references.get_rfmo_regions()
```

### Access the list of RFMO region as Pydantic models

```python
rfmo_regions_data = rfmo_regions_result.data()
rfmo_region = rfmo_regions_data[-1]
print((rfmo_region.id, rfmo_region.dataset))
print(rfmo_region.model_dump())
```

**Output:**

```
('WCPFC', 'public-rfmo')
{'id': 'WCPFC', 'label': 'WCPFC', 'rfb': None, 'dataset': 'public-rfmo'}
```

### Access the RFMO regions as a DataFrame

```python
rfmo_regions_df = rfmo_regions_result.df()
print(rfmo_regions_df.info())
print(rfmo_regions_df[["id", "dataset"]].head())
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 42 entries, 0 to 41
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   id       42 non-null     object
 1   label    42 non-null     object
 2   rfb      35 non-null     object
 3   dataset  42 non-null     object
dtypes: object(4)
memory usage: 1.4+ KB
```

## Next Steps

Explore the [Usage Guides](index) for other API resources to understand how you can combine reference data with dynamic information about events, vessels, and more. Check out the following resources:

  - [4Wings API](4wings-api)
  - [Vessels API](vessels-api)
  - [Events API](events-api)
  - [Insights API](insights-api)
  - [Datasets API](datasets-api)
