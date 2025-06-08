# 4Wings API

This guide provides detailed instructions on how to use the [gfw-api-python-client](https://github.com/GlobalFishingWatch/gfw-api-python-client) to access the 4Wings API, which is designed for generating reports and statistics on activities within specified regions. This API is particularly useful for creating data visualizations related to fishing effort and other vessel activities. Here is a [Jupyter Notebook](https://github.com/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/usage-guides/4wings-api.ipynb) version of this guide with more usage examples.


## Prerequisites

- You have installed the `gfw-api-python-client`. Refer to the [Getting Started](../getting-started) guide for installation instructions.


## Getting Started

To interact with the 4Wings endpoints, you first need to instantiate the `gfw.Client` and then access the `fourwings` resource:


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

The `gfw_client.fourwings` object provides methods to generate reports, retrieve the last generated report, and get global fishing effort statistics. These methods return a `result` object, which offers convenient ways to access the data as Pydantic models using `.data()` or as pandas DataFrames using `.df()`.


## Creating a Report (`create_report`)

The `create_report()` method allows you to generate a report for a specified geographic region, based on the provided datasets and parameters.


```python
report_result = await gfw_client.fourwings.create_report(
    spatial_resolution="LOW",
    temporal_resolution="MONTHLY",
    group_by="GEARTYPE",
    datasets=["public-global-fishing-effort:latest"],
    start_date="2022-01-01",
    end_date="2022-05-01",
    region={
        "dataset": "public-eez-areas",
        "id": "5690",
    },
)
```

### Access the report data as Pydantic models

```python
report_data = report_result.data()
report = report_data[-1]
print((report.date, report.hours, report.lat, report.lon))
print(report.model_dump())
```

**Output:**

```
('2022-04', 3.126388888888889, 52.0, 155.2)
```

### Access the report data as a DataFrame

```python
report_df = report_result.df()
print(report_df.info())
print(report_df[["date", "hours", "lat", "lon"]].head())
```

**Output:**

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 39715 entries, 0 to 39714
Data columns (total 20 columns):
 #   Column                   Non-Null Count  Dtype
---  ------                   --------------  -----
 0   date                     39715 non-null  object
 1   detections               0 non-null      object
 2   flag                     0 non-null      object
 3   gear_type                39715 non-null  object
 4   hours                    39715 non-null  float64
 5   vessel_ids               39715 non-null  int64
 6   vessel_id                0 non-null      object
 7   vessel_type              0 non-null      object
 8   entry_timestamp          0 non-null      object
 9   exit_timestamp           0 non-null      object
 10  first_transmission_date  0 non-null      object
 11  last_transmission_date   0 non-null      object
 12  imo                      0 non-null      object
 13  mmsi                     0 non-null      object
 14  call_sign                0 non-null      object
 15  dataset                  0 non-null      object
 16  report_dataset           39715 non-null  object
 17  ship_name                0 non-null      object
 18  lat                      39715 non-null  float64
 19  lon                      39715 non-null  float64
dtypes: float64(3), int64(1), object(16)
memory usage: 6.1+ MB
```

## Reference Data

The 4Wings API often requires specifying geographic regions. You can use the [Reference Data API](references-data-api) to retrieve the `dataset` and `id` of various regions (e.g., EEZs, MPAs, RFMOs) that can then be used in the `create_report()` method.

## Next Steps

Explore the [Usage Guides](index) for other API resources to understand how you can combine the reporting and statistical capabilities of the 4Wings API with vessel information, event data, and more. Check out the following resources:

  - [Vessels API](vessels-api)
  - [Events API](events-api)
  - [Insights API](insights-api)
  - [Datasets API](datasets-api)
  - [Reference Data API](references-data-api)
