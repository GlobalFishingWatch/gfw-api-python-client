:py:mod:`gfwapiclient.resources.events.stats.models.response`
=============================================================

.. py:module:: gfwapiclient.resources.events.stats.models.response

.. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.response
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`EventStatsTimeSeries <gfwapiclient.resources.events.stats.models.response.EventStatsTimeSeries>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.response.EventStatsTimeSeries
          :summary:
   * - :py:obj:`EventStatsItem <gfwapiclient.resources.events.stats.models.response.EventStatsItem>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.response.EventStatsItem
          :summary:
   * - :py:obj:`EventStatsResult <gfwapiclient.resources.events.stats.models.response.EventStatsResult>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.response.EventStatsResult
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.events.stats.models.response.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.response.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.events.stats.models.response.__all__
   :value: ['EventStatsItem', 'EventStatsResult']

   .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.response.__all__

.. py:class:: EventStatsTimeSeries(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.events.stats.models.response.EventStatsTimeSeries

   Bases: :py:obj:`pydantic.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.response.EventStatsTimeSeries

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.response.EventStatsTimeSeries.__init__

   .. py:attribute:: date
      :canonical: gfwapiclient.resources.events.stats.models.response.EventStatsTimeSeries.date
      :type: typing.Optional[datetime.datetime]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.response.EventStatsTimeSeries.date

   .. py:attribute:: value
      :canonical: gfwapiclient.resources.events.stats.models.response.EventStatsTimeSeries.value
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.response.EventStatsTimeSeries.value

.. py:class:: EventStatsItem(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.events.stats.models.response.EventStatsItem

   Bases: :py:obj:`gfwapiclient.http.models.ResultItem`

   .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.response.EventStatsItem

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.response.EventStatsItem.__init__

   .. py:attribute:: num_events
      :canonical: gfwapiclient.resources.events.stats.models.response.EventStatsItem.num_events
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.response.EventStatsItem.num_events

   .. py:attribute:: num_flags
      :canonical: gfwapiclient.resources.events.stats.models.response.EventStatsItem.num_flags
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.response.EventStatsItem.num_flags

   .. py:attribute:: num_vessels
      :canonical: gfwapiclient.resources.events.stats.models.response.EventStatsItem.num_vessels
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.response.EventStatsItem.num_vessels

   .. py:attribute:: flags
      :canonical: gfwapiclient.resources.events.stats.models.response.EventStatsItem.flags
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.response.EventStatsItem.flags

   .. py:attribute:: timeseries
      :canonical: gfwapiclient.resources.events.stats.models.response.EventStatsItem.timeseries
      :type: typing.Optional[typing.List[gfwapiclient.resources.events.stats.models.response.EventStatsTimeSeries]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.response.EventStatsItem.timeseries

.. py:class:: EventStatsResult(data: gfwapiclient.resources.events.stats.models.response.EventStatsItem)
   :canonical: gfwapiclient.resources.events.stats.models.response.EventStatsResult

   Bases: :py:obj:`gfwapiclient.http.models.Result`\ [\ :py:obj:`gfwapiclient.resources.events.stats.models.response.EventStatsItem`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.response.EventStatsResult

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.response.EventStatsResult.__init__

   .. py:attribute:: _result_item_class
      :canonical: gfwapiclient.resources.events.stats.models.response.EventStatsResult._result_item_class
      :type: typing.Type[gfwapiclient.resources.events.stats.models.response.EventStatsItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.response.EventStatsResult._result_item_class

   .. py:attribute:: _data
      :canonical: gfwapiclient.resources.events.stats.models.response.EventStatsResult._data
      :type: gfwapiclient.resources.events.stats.models.response.EventStatsItem
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.response.EventStatsResult._data
