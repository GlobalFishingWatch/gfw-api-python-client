# Insights API

<a href="https://colab.research.google.com/github/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/usage-guides/insights-api.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

This guide provides detailed instructions on how to use the [gfw-api-python-client](https://github.com/GlobalFishingWatch/gfw-api-python-client) to access aggregated insights about vessel activities. Currently, the Insights API focuses on providing summaries related to specific vessels over a defined time range. Here is a [Jupyter Notebook](https://github.com/GlobalFishingWatch/gfw-api-python-client/blob/develop/notebooks/usage-guides/insights-api.ipynb) version of this guide with more usage examples.

> **Note:** See the [Insights Data Caveats](https://globalfishingwatch.org/our-apis/documentation#insights-api-fishing-detected-in-no-take-mpas)—it is critical to avoid misinterpreting the insights. You can find the [Terms of Use](https://globalfishingwatch.org/our-apis/documentation#terms-of-use) page in the [GFW API documentation](https://globalfishingwatch.org/our-apis/documentation#introduction), for details on GFW data, API licenses, and rate limits.

## Prerequisites

- You have installed the `gfw-api-python-client`. Refer to the [Getting Started](../getting-started) guide for installation instructions.

- You will need a valid `Vessel ID` to retrieve insights for a specific vessel. You can obtain these IDs using the [Vessels API](vessels-api).

## Getting Started

To interact with the Insights endpoints, you first need to instantiate the `gfw.Client` and then access the `insights` resource:

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

## Getting Insights by Vessel (`get_vessel_insights`)

The `get_vessel_insights()` method allows you to retrieve aggregated insights for a specific vessel within a given time range.

```python
insights_result = await gfw_client.insights.get_vessel_insights(
    includes=["FISHING"],
    start_date="2020-01-01",
    end_date="2025-03-03",
    vessels=[
        {
            "dataset_id": "public-global-vessel-identity:latest",
            "vessel_id": "785101812-2127-e5d2-e8bf-7152c5259f5f",
        }
    ],
)
```

### Access the insights data as Pydantic model

```python
insights = insights_result.data()
print(
    (
        insights.period.start_date,
        insights.period.end_date,
        insights.apparent_fishing.period_selected_counters.events,
    )
)
print(insights.model_dump())
```

**Output:**

```
(datetime.date(2020, 1, 1), datetime.date(2025, 3, 3), 2829)
```

### Access the insights data as a DataFrame

```python
insights_df = insights_result.df()
print(insights_df.info())
print(insights_df.head())
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

## Next Steps

Explore the [Usage Guides](index) for other API resources to understand how you can combine vessel insights with event data, vessel details, and more. Check out the following resources:

- [Vessels API](vessels-api)
- [Events API](events-api)
- [4Wings API](4wings-api)
- [Datasets API](datasets-api)
- [Reference Data API](references-data-api)
