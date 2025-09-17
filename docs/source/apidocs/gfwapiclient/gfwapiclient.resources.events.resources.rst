:py:mod:`gfwapiclient.resources.events.resources`
=================================================

.. py:module:: gfwapiclient.resources.events.resources

.. autodoc2-docstring:: gfwapiclient.resources.events.resources
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`EventResource <gfwapiclient.resources.events.resources.EventResource>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.resources.EventResource
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.events.resources.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.resources.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.events.resources.__all__
   :value: ['EventResource']

   .. autodoc2-docstring:: gfwapiclient.resources.events.resources.__all__

.. py:class:: EventResource(*, http_client: gfwapiclient.http.client.HTTPClient)
   :canonical: gfwapiclient.resources.events.resources.EventResource

   Bases: :py:obj:`gfwapiclient.http.resources.BaseResource`

   .. autodoc2-docstring:: gfwapiclient.resources.events.resources.EventResource

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.resources.EventResource.__init__

   .. py:method:: get_all_events(*, datasets: typing.Union[typing.List[gfwapiclient.resources.events.base.models.request.EventDataset], typing.List[str]], vessels: typing.Optional[typing.List[str]] = None, types: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.events.base.models.request.EventType], typing.List[str]]] = None, start_date: typing.Optional[typing.Union[datetime.date, str]] = None, end_date: typing.Optional[typing.Union[datetime.date, str]] = None, confidences: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.events.base.models.request.EventConfidence], typing.List[str]]] = None, encounter_types: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.events.base.models.request.EventEncounterType], typing.List[str]]] = None, duration: typing.Optional[int] = None, vessel_types: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.events.base.models.request.EventVesselType], typing.List[str]]] = None, vessel_groups: typing.Optional[typing.List[str]] = None, flags: typing.Optional[typing.List[str]] = None, geometry: typing.Optional[typing.Union[gfwapiclient.resources.events.base.models.request.EventGeometry, typing.Dict[str, typing.Any]]] = None, region: typing.Optional[typing.Union[gfwapiclient.resources.events.base.models.request.EventRegion, typing.Dict[str, typing.Any]]] = None, limit: typing.Optional[int] = None, offset: typing.Optional[int] = None, sort: typing.Optional[str] = None, **kwargs: typing.Dict[str, typing.Any]) -> gfwapiclient.resources.events.list.models.response.EventListResult
      :canonical: gfwapiclient.resources.events.resources.EventResource.get_all_events
      :async:

      .. autodoc2-docstring:: gfwapiclient.resources.events.resources.EventResource.get_all_events

   .. py:method:: get_event_by_id(*, id: str, dataset: typing.Union[gfwapiclient.resources.events.base.models.request.EventDataset, str], **kwargs: typing.Dict[str, typing.Any]) -> gfwapiclient.resources.events.detail.models.response.EventDetailResult
      :canonical: gfwapiclient.resources.events.resources.EventResource.get_event_by_id
      :async:

      .. autodoc2-docstring:: gfwapiclient.resources.events.resources.EventResource.get_event_by_id

   .. py:method:: get_events_stats(*, datasets: typing.Union[typing.List[gfwapiclient.resources.events.base.models.request.EventDataset], typing.List[str]], timeseries_interval: typing.Union[gfwapiclient.resources.events.stats.models.request.EventStatsTimeSeriesInterval, str], vessels: typing.Optional[typing.List[str]] = None, types: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.events.base.models.request.EventType], typing.List[str]]] = None, start_date: typing.Optional[typing.Union[datetime.date, str]] = None, end_date: typing.Optional[typing.Union[datetime.date, str]] = None, confidences: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.events.base.models.request.EventConfidence], typing.List[str]]] = None, encounter_types: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.events.base.models.request.EventEncounterType], typing.List[str]]] = None, duration: typing.Optional[int] = None, vessel_types: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.events.base.models.request.EventVesselType], typing.List[str]]] = None, vessel_groups: typing.Optional[typing.List[str]] = None, flags: typing.Optional[typing.List[str]] = None, geometry: typing.Optional[typing.Union[gfwapiclient.resources.events.base.models.request.EventGeometry, typing.Dict[str, typing.Any]]] = None, region: typing.Optional[typing.Union[gfwapiclient.resources.events.base.models.request.EventRegion, typing.Dict[str, typing.Any]]] = None, includes: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.events.stats.models.request.EventStatsInclude], typing.List[str]]] = None, **kwargs: typing.Dict[str, typing.Any]) -> gfwapiclient.resources.events.stats.models.response.EventStatsResult
      :canonical: gfwapiclient.resources.events.resources.EventResource.get_events_stats
      :async:

      .. autodoc2-docstring:: gfwapiclient.resources.events.resources.EventResource.get_events_stats

   .. py:method:: _prepare_get_all_events_request_params(*, limit: typing.Optional[int] = None, offset: typing.Optional[int] = None, sort: typing.Optional[str] = None) -> gfwapiclient.resources.events.list.models.request.EventListParams
      :canonical: gfwapiclient.resources.events.resources.EventResource._prepare_get_all_events_request_params

      .. autodoc2-docstring:: gfwapiclient.resources.events.resources.EventResource._prepare_get_all_events_request_params

   .. py:method:: _prepare_get_all_events_request_body(*, datasets: typing.Union[typing.List[gfwapiclient.resources.events.base.models.request.EventDataset], typing.List[str]], vessels: typing.Optional[typing.List[str]] = None, types: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.events.base.models.request.EventType], typing.List[str]]] = None, start_date: typing.Optional[typing.Union[datetime.date, str]] = None, end_date: typing.Optional[typing.Union[datetime.date, str]] = None, confidences: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.events.base.models.request.EventConfidence], typing.List[str]]] = None, encounter_types: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.events.base.models.request.EventEncounterType], typing.List[str]]] = None, duration: typing.Optional[int] = None, vessel_types: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.events.base.models.request.EventVesselType], typing.List[str]]] = None, vessel_groups: typing.Optional[typing.List[str]] = None, flags: typing.Optional[typing.List[str]] = None, geometry: typing.Optional[typing.Union[gfwapiclient.resources.events.base.models.request.EventGeometry, typing.Dict[str, typing.Any]]] = None, region: typing.Optional[typing.Union[gfwapiclient.resources.events.base.models.request.EventRegion, typing.Dict[str, typing.Any]]] = None) -> gfwapiclient.resources.events.list.models.request.EventListBody
      :canonical: gfwapiclient.resources.events.resources.EventResource._prepare_get_all_events_request_body

      .. autodoc2-docstring:: gfwapiclient.resources.events.resources.EventResource._prepare_get_all_events_request_body

   .. py:method:: _prepare_get_event_by_id_request_params(*, dataset: typing.Union[gfwapiclient.resources.events.base.models.request.EventDataset, str]) -> gfwapiclient.resources.events.detail.models.request.EventDetailParams
      :canonical: gfwapiclient.resources.events.resources.EventResource._prepare_get_event_by_id_request_params

      .. autodoc2-docstring:: gfwapiclient.resources.events.resources.EventResource._prepare_get_event_by_id_request_params

   .. py:method:: _prepare_get_events_stats_request_body(*, datasets: typing.Union[typing.List[gfwapiclient.resources.events.base.models.request.EventDataset], typing.List[str]], timeseries_interval: typing.Union[gfwapiclient.resources.events.stats.models.request.EventStatsTimeSeriesInterval, str], vessels: typing.Optional[typing.List[str]] = None, types: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.events.base.models.request.EventType], typing.List[str]]] = None, start_date: typing.Optional[typing.Union[datetime.date, str]] = None, end_date: typing.Optional[typing.Union[datetime.date, str]] = None, confidences: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.events.base.models.request.EventConfidence], typing.List[str]]] = None, encounter_types: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.events.base.models.request.EventEncounterType], typing.List[str]]] = None, duration: typing.Optional[int] = None, vessel_types: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.events.base.models.request.EventVesselType], typing.List[str]]] = None, vessel_groups: typing.Optional[typing.List[str]] = None, flags: typing.Optional[typing.List[str]] = None, geometry: typing.Optional[typing.Union[gfwapiclient.resources.events.base.models.request.EventGeometry, typing.Dict[str, typing.Any]]] = None, region: typing.Optional[typing.Union[gfwapiclient.resources.events.base.models.request.EventRegion, typing.Dict[str, typing.Any]]] = None, includes: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.events.stats.models.request.EventStatsInclude], typing.List[str]]] = None) -> gfwapiclient.resources.events.stats.models.request.EventStatsBody
      :canonical: gfwapiclient.resources.events.resources.EventResource._prepare_get_events_stats_request_body

      .. autodoc2-docstring:: gfwapiclient.resources.events.resources.EventResource._prepare_get_events_stats_request_body
