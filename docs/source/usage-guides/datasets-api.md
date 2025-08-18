# Datasets API

<a href="https://colab.research.google.com/github/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/usage-guides/datasets-api.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

This guide provides detailed instructions on how to use the [gfw-api-python-client](https://github.com/GlobalFishingWatch/gfw-api-python-client) to access various datasets available through the Global Fishing Watch API. Currently, it focuses on retrieving SAR (Synthetic Aperture Radar) fixed infrastructure data. The Datasets API allows you to retrieve this information, either by specifying `tile coordinates` or a `geographic geometry`. Here is a [Jupyter Notebook](https://github.com/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/usage-guides/datasets-api.ipynb) version of this guide with more usage examples.

> **Note:** See the [Data Caveats](https://globalfishingwatch.org/our-apis/documentation#data-caveat) and [Terms of Use](https://globalfishingwatch.org/our-apis/documentation#terms-of-use) pages in the [GFW API documentation](https://globalfishingwatch.org/our-apis/documentation#introduction) for details on GFW data, API licenses, and rate limits.

## Prerequisites

- You have installed the `gfw-api-python-client`. Refer to the [Getting Started](../getting-started) guide for installation instructions.

## Getting Started

To interact with the Datasets endpoints, you first need to instantiate the `gfw.Client` and then access the `datasets` resource:

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

The `gfw_client.datasets` object provides methods to retrieve data from various datasets. The `get_sar_fixed_infrastructure` method allows you to access SAR fixed infrastructure data. This method returns a `result` object, which offers convenient ways to access the data as Pydantic models using `.data()` or as pandas DataFrames using `.df()`.

## Retrieving SAR Fixed Infrastructure Data by Tile Coordinates (`get_sar_fixed_infrastructure` with z, x, y)

You can retrieve SAR fixed infrastructure data for a specific tile using its zoom level (`z`), x-coordinate (`x`), and y-coordinate (`y`).

```python
z = 1
x = 0
y = 1

sar_infrastructure_result = await gfw_client.datasets.get_sar_fixed_infrastructure(
    z=z, x=x, y=y
)
```

### Access the list of SAR fixed infrastructure items as Pydantic models

```python
sar_infrastructure_data = sar_infrastructure_result.data()
sar_infrastructure = sar_infrastructure_data[-1]
print(
    (
        sar_infrastructure.structure_id,
        sar_infrastructure.label,
        sar_infrastructure.lat,
        sar_infrastructure.lon,
    )
)
print(sar_infrastructure.model_dump())
```

**Output:**

```
(646348, 'oil', -39.15082587013905, 177.96658840984458)
```

### Access the SAR fixed infrastructure items as a DataFrame

```python
sar_infrastructure_df = sar_infrastructure_result.df()
print(sar_infrastructure_df.info())
print(sar_infrastructure_df.head())
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1106 entries, 0 to 1105
Data columns (total 7 columns):
 #   Column                Non-Null Count  Dtype
---  ------                --------------  -----
 0   structure_id          1106 non-null   int64
 1   lat                   1106 non-null   float64
 2   lon                   1106 non-null   float64
 3   label                 1106 non-null   object
 4   structure_start_date  1106 non-null   datetime64[ns, UTC]
 5   structure_end_date    831 non-null    datetime64[ns, UTC]
 6   label_confidence      1106 non-null   object
dtypes: datetime64[ns, UTC](2), float64(2), int64(1), object(2)
memory usage: 60.6+ KB
```

## Retrieving SAR Fixed Infrastructure Data by Geometry (`get_sar_fixed_infrastructure` with geometry)

You can also retrieve SAR fixed infrastructure data for a specific geographic area defined by a GeoJSON geometry.

```python
geometry = {
    "type": "Polygon",
    "coordinates": [
        [
            [-180.0, -85.0511287798066],
            [-180.0, 0.0],
            [0.0, 0.0],
            [0.0, -85.0511287798066],
            [-180.0, -85.0511287798066],
        ]
    ],
}

sar_infrastructure_result = await gfw_client.datasets.get_sar_fixed_infrastructure(
    geometry=geometry
)
```

### Access the list of SAR fixed infrastructure items as Pydantic models

```python
sar_infrastructure_data = sar_infrastructure_result.data()
sar_infrastructure = sar_infrastructure_data[-1]
print(
    (
        sar_infrastructure.structure_id,
        sar_infrastructure.label,
        sar_infrastructure.lat,
        sar_infrastructure.lon,
    )
)
print(sar_infrastructure.model_dump())
```

**Output:**

```
(646348, 'oil', -39.15082587013905, 177.96658840984458)
```

### Access the SAR fixed infrastructure items as a DataFrame

```python
sar_infrastructure_df = sar_infrastructure_result.df()
print(sar_infrastructure_df.info())
print(sar_infrastructure_df.head())
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1106 entries, 0 to 1105
Data columns (total 7 columns):
 #   Column                Non-Null Count  Dtype
---  ------                --------------  -----
 0   structure_id          1106 non-null   int64
 1   lat                   1106 non-null   float64
 2   lon                   1106 non-null   float64
 3   label                 1106 non-null   object
 4   structure_start_date  1106 non-null   datetime64[ns, UTC]
 5   structure_end_date    831 non-null    datetime64[ns, UTC]
 6   label_confidence      1106 non-null   object
dtypes: datetime64[ns, UTC](2), float64(2), int64(1), object(2)
memory usage: 60.6+ KB
```

## Next Steps

Explore the [Usage Guides](index) for other API resources. Check out the following resources:

- [4Wings API](4wings-api)
- [Vessels API](vessels-api)
- [Events API](events-api)
- [Insights API](insights-api)
- [Reference Data API](references-data-api)
