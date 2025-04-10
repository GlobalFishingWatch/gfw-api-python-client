:py:mod:`gfwapiclient.resources.events.stats.models.request`
============================================================

.. py:module:: gfwapiclient.resources.events.stats.models.request

.. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.request
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`EventStatsTimeSeriesInterval <gfwapiclient.resources.events.stats.models.request.EventStatsTimeSeriesInterval>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.request.EventStatsTimeSeriesInterval
          :summary:
   * - :py:obj:`EventStatsInclude <gfwapiclient.resources.events.stats.models.request.EventStatsInclude>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.request.EventStatsInclude
          :summary:
   * - :py:obj:`EventStatsBody <gfwapiclient.resources.events.stats.models.request.EventStatsBody>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.request.EventStatsBody
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.events.stats.models.request.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.request.__all__
          :summary:
   * - :py:obj:`EVENT_STATS_REQUEST_BODY_VALIDATION_ERROR_MESSAGE <gfwapiclient.resources.events.stats.models.request.EVENT_STATS_REQUEST_BODY_VALIDATION_ERROR_MESSAGE>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.request.EVENT_STATS_REQUEST_BODY_VALIDATION_ERROR_MESSAGE
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.events.stats.models.request.__all__
   :value: ['EventStatsBody']

   .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.request.__all__

.. py:data:: EVENT_STATS_REQUEST_BODY_VALIDATION_ERROR_MESSAGE
   :canonical: gfwapiclient.resources.events.stats.models.request.EVENT_STATS_REQUEST_BODY_VALIDATION_ERROR_MESSAGE
   :type: typing.Final[str]
   :value: 'Get events statistics request body validation failed.'

   .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.request.EVENT_STATS_REQUEST_BODY_VALIDATION_ERROR_MESSAGE

.. py:class:: EventStatsTimeSeriesInterval()
   :canonical: gfwapiclient.resources.events.stats.models.request.EventStatsTimeSeriesInterval

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`

   .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.request.EventStatsTimeSeriesInterval

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.request.EventStatsTimeSeriesInterval.__init__

   .. py:attribute:: HOUR
      :canonical: gfwapiclient.resources.events.stats.models.request.EventStatsTimeSeriesInterval.HOUR
      :value: 'HOUR'

      .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.request.EventStatsTimeSeriesInterval.HOUR

   .. py:attribute:: DAY
      :canonical: gfwapiclient.resources.events.stats.models.request.EventStatsTimeSeriesInterval.DAY
      :value: 'DAY'

      .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.request.EventStatsTimeSeriesInterval.DAY

   .. py:attribute:: MONTH
      :canonical: gfwapiclient.resources.events.stats.models.request.EventStatsTimeSeriesInterval.MONTH
      :value: 'MONTH'

      .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.request.EventStatsTimeSeriesInterval.MONTH

   .. py:attribute:: YEAR
      :canonical: gfwapiclient.resources.events.stats.models.request.EventStatsTimeSeriesInterval.YEAR
      :value: 'YEAR'

      .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.request.EventStatsTimeSeriesInterval.YEAR

.. py:class:: EventStatsInclude()
   :canonical: gfwapiclient.resources.events.stats.models.request.EventStatsInclude

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`

   .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.request.EventStatsInclude

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.request.EventStatsInclude.__init__

   .. py:attribute:: TOTAL_COUNT
      :canonical: gfwapiclient.resources.events.stats.models.request.EventStatsInclude.TOTAL_COUNT
      :value: 'TOTAL_COUNT'

      .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.request.EventStatsInclude.TOTAL_COUNT

   .. py:attribute:: TIME_SERIES
      :canonical: gfwapiclient.resources.events.stats.models.request.EventStatsInclude.TIME_SERIES
      :value: 'TIME_SERIES'

      .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.request.EventStatsInclude.TIME_SERIES

.. py:class:: EventStatsBody(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.events.stats.models.request.EventStatsBody

   Bases: :py:obj:`gfwapiclient.resources.events.base.models.request.EventBaseBody`

   .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.request.EventStatsBody

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.request.EventStatsBody.__init__

   .. py:attribute:: timeseries_interval
      :canonical: gfwapiclient.resources.events.stats.models.request.EventStatsBody.timeseries_interval
      :type: typing.Optional[gfwapiclient.resources.events.stats.models.request.EventStatsTimeSeriesInterval]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.request.EventStatsBody.timeseries_interval

   .. py:attribute:: includes
      :canonical: gfwapiclient.resources.events.stats.models.request.EventStatsBody.includes
      :type: typing.Optional[typing.List[gfwapiclient.resources.events.stats.models.request.EventStatsInclude]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.stats.models.request.EventStatsBody.includes
