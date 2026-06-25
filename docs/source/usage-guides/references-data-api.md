# Reference Data API

<a href="https://colab.research.google.com/github/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/usage-guides/references-data-api.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

This guide provides detailed instructions on how to use the [gfw-api-python-client](https://github.com/GlobalFishingWatch/gfw-api-python-client) to access reference data, specifically geographic regions. The [Reference Data API](https://globalfishingwatch.org/our-apis/documentation#regions) offers access to static datasets, currently focusing on Exclusive Economic Zones (EEZs), Marine Protected Areas (MPAs), and Regional Fisheries Management Organizations (RFMOs). Here is a [Jupyter Notebook](https://github.com/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/usage-guides/references-data-api.ipynb) version of this guide with more usage examples.

> **Note:** See the [Datasets](https://globalfishingwatch.org/our-apis/documentation#api-dataset), [Reference Data Caveats](https://globalfishingwatch.org/our-apis/documentation#reference-data), and [Terms of Use](https://globalfishingwatch.org/our-apis/documentation#terms-of-use) pages in the [GFW API documentation](https://globalfishingwatch.org/our-apis/documentation#introduction) for details on GFW data, API licenses, and rate limits.

## Prerequisites

- Before using the `gfw-api-python-client`, ensure it is installed (see the [Getting Started](../getting-started) guide) and that you have obtained an API access token from the [Global Fishing Watch API portal](https://globalfishingwatch.org/our-apis/tokens).

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

**Note:** Use `gfw_client.references` methods to obtain the **Region of Interest (ROI)**, i.e., `region`, which can then be passed directly to the [4Wings API](https://globalfishingwatch.org/our-apis/documentation#map-visualization-4wings-api), [Bulk Download API](https://globalfishingwatch.org/our-apis/documentation#bulk-download-api), [Insights API](https://globalfishingwatch.org/our-apis/documentation#insights-api), and [Events API](https://globalfishingwatch.org/our-apis/documentation#events-api) methods.

> **Tip:** Use [IPython](https://ipython.readthedocs.io/en/stable/) or Python 3.11+ with `python -m asyncio` to run `gfw-api-python-client` code interactively, as these environments support executing `async` / `await` expressions directly in the console.

## Retrieving Exclusive Economic Zones (EEZs)

To get a list of available Exclusive Economic Zone (EEZ) regions, use the `get_eez_regions()` method:

```python
eez_regions_result = await gfw_client.references.get_eez_regions()
```

### Access the list of EEZ region as Pydantic models

```python
eez_regions_data = eez_regions_result.data()
eez_region = eez_regions_data[-1]
print((eez_region.id, eez_region.dataset, eez_region.label, eez_region.iso3))
```

**Output:**

```
('8489', 'public-eez-areas', 'Antartic 200NM zone beyond the coastline', 'ATA')
```

### Access the EEZ regions as a DataFrame

```python
eez_regions_df = eez_regions_result.df()
print(eez_regions_df.info())
```

**Output:**

```
<class 'pandas.DataFrame'>
RangeIndex: 286 entries, 0 to 285
Data columns (total 8 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   dataset      286 non-null    str
 1   id           286 non-null    str
 2   label        286 non-null    str
 3   iso3         235 non-null    str
 4   iso_sov_1    285 non-null    str
 5   iso_sov_2    56 non-null     str
 6   iso_sov_3    6 non-null      str
 7   territory_1  285 non-null    str
dtypes: str(8)
memory usage: 18.0 KB
```

### Filter the list of EEZ regions to Obtain the Region of Interest (ROI)

```python
eez_rois_result = await gfw_client.references.get_eez_regions(iso3="SEN")

eez_roi = eez_rois_result.data()[0]

print((eez_roi.id, eez_roi.dataset, eez_roi.label, eez_roi.iso3))
```

**Output:**

```
('8371', 'public-eez-areas', 'Senegalese Exclusive Economic Zone', 'SEN')
```

> **Note:** Pass `eez_roi` directly to `region` parameter of the [4Wings API](https://globalfishingwatch.org/our-apis/documentation#map-visualization-4wings-api), [Bulk Download API](https://globalfishingwatch.org/our-apis/documentation#bulk-download-api), [Insights API](https://globalfishingwatch.org/our-apis/documentation#insights-api), and [Events API](https://globalfishingwatch.org/our-apis/documentation#events-api) methods.

## Retrieving Marine Protected Areas (MPAs)

To get a list of available Marine Protected Area (MPA) regions, use the `get_mpa_regions()` method:

```python
mpa_regions_result = await gfw_client.references.get_mpa_regions()
```

### Access the list of MPA region as Pydantic models

```python
mpa_regions_data = mpa_regions_result.data()
mpa_region = mpa_regions_data[-1]
print((mpa_region.id, mpa_region.dataset, mpa_region.label))
```

**Output:**

```
('555882474',
 'public-mpa-all',
 'Humedal Tubul Raqui - Santuario de la Naturaleza')
```

### Access the MPA regions as a DataFrame

```python
mpa_regions_df = mpa_regions_result.df()
print(mpa_regions_df.info())
```

**Output:**

```
<class 'pandas.DataFrame'>
RangeIndex: 17172 entries, 0 to 17171
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   dataset  17172 non-null  str
 1   id       17172 non-null  str
 2   label    17172 non-null  str
dtypes: str(3)
memory usage: 402.6 KB
```

### Filter the list of MPA regions to Obtain the Region of Interest (ROI)

```python
mpa_rois_result = await gfw_client.references.get_mpa_regions(id="555745302")

mpa_roi = mpa_rois_result.data()[0]

print((mpa_roi.id, mpa_roi.dataset, mpa_roi.label))
```

**Output:**

```
('555745302', 'public-mpa-all', 'Dorsal de Nasca - Reserva Nacional')
```

> **Note:** Pass `mpa_roi` directly to `region` parameter of the [4Wings API](https://globalfishingwatch.org/our-apis/documentation#map-visualization-4wings-api), [Bulk Download API](https://globalfishingwatch.org/our-apis/documentation#bulk-download-api), [Insights API](https://globalfishingwatch.org/our-apis/documentation#insights-api), and [Events API](https://globalfishingwatch.org/our-apis/documentation#events-api) methods.

## Retrieving Regional Fisheries Management Organizations (RFMOs)

To get a list of available Regional Fisheries Management Organization (RFMO) regions, use the `get_rfmo_regions()` method:

```python
rfmo_regions_result = await gfw_client.references.get_rfmo_regions()
```

### Access the list of RFMO region as Pydantic models

```python
rfmo_regions_data = rfmo_regions_result.data()
rfmo_region = rfmo_regions_data[-1]
print((rfmo_region.id, rfmo_region.dataset, rfmo_region.label))
```

**Output:**

```
('BOBP-IGO', 'public-rfmo', 'BOBP-IGO')
```

### Access the RFMO regions as a DataFrame

```python
rfmo_regions_df = rfmo_regions_result.df()
print(rfmo_regions_df.info())
```

**Output:**

```
<class 'pandas.DataFrame'>
RangeIndex: 42 entries, 0 to 41
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   dataset  42 non-null     str
 1   id       42 non-null     str
 2   label    42 non-null     str
 3   id_      42 non-null     str
dtypes: str(4)
memory usage: 1.4 KB
```

### Filter the list of RFMO regions to Obtain the Region of Interest (ROI)

```python
rfmo_rois_result = await gfw_client.references.get_rfmo_regions(id="WCPFC")

rfmo_roi = rfmo_rois_result.data()[0]

print((rfmo_roi.id, rfmo_roi.dataset, rfmo_roi.label))
```

**Output:**

```
('WCPFC', 'public-rfmo', 'WCPFC')
```

> **Note:** Pass `rfmo_roi` directly to `region` parameter of the [4Wings API](https://globalfishingwatch.org/our-apis/documentation#map-visualization-4wings-api), [Bulk Download API](https://globalfishingwatch.org/our-apis/documentation#bulk-download-api), [Insights API](https://globalfishingwatch.org/our-apis/documentation#insights-api), and [Events API](https://globalfishingwatch.org/our-apis/documentation#events-api) methods.

## Next Steps

Explore the [Usage Guides](index) and [Workflow Guides](../workflow-guides/index) for other API resources to understand how you can combine reference data with dynamic information about events, vessels, and more. Check out the following resources:

- [4Wings API](4wings-api)
- [Vessels API](vessels-api)
- [Events API](events-api)
- [Insights API](insights-api)
- [Datasets API](datasets-api)
- [Bulk Download API](bulk-downloads-api)
