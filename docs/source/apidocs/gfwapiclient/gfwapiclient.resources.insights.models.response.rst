:py:mod:`gfwapiclient.resources.insights.models.response`
=========================================================

.. py:module:: gfwapiclient.resources.insights.models.response

.. autodoc2-docstring:: gfwapiclient.resources.insights.models.response
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`Period <gfwapiclient.resources.insights.models.response.Period>`
     - .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.Period
          :summary:
   * - :py:obj:`PeriodicCounters <gfwapiclient.resources.insights.models.response.PeriodicCounters>`
     - .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.PeriodicCounters
          :summary:
   * - :py:obj:`Gap <gfwapiclient.resources.insights.models.response.Gap>`
     - .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.Gap
          :summary:
   * - :py:obj:`Coverage <gfwapiclient.resources.insights.models.response.Coverage>`
     - .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.Coverage
          :summary:
   * - :py:obj:`ApparentFishing <gfwapiclient.resources.insights.models.response.ApparentFishing>`
     - .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.ApparentFishing
          :summary:
   * - :py:obj:`IuuListPeriod <gfwapiclient.resources.insights.models.response.IuuListPeriod>`
     - .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.IuuListPeriod
          :summary:
   * - :py:obj:`IuuVesselList <gfwapiclient.resources.insights.models.response.IuuVesselList>`
     - .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.IuuVesselList
          :summary:
   * - :py:obj:`VesselIdentity <gfwapiclient.resources.insights.models.response.VesselIdentity>`
     - .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.VesselIdentity
          :summary:
   * - :py:obj:`VesselInsightItem <gfwapiclient.resources.insights.models.response.VesselInsightItem>`
     - .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.VesselInsightItem
          :summary:
   * - :py:obj:`VesselInsightResult <gfwapiclient.resources.insights.models.response.VesselInsightResult>`
     - .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.VesselInsightResult
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.insights.models.response.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.insights.models.response.__all__
   :value: ['VesselInsightItem', 'VesselInsightResult']

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.__all__

.. py:class:: Period(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.insights.models.response.Period

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.Period

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.Period.__init__

   .. py:attribute:: start_date
      :canonical: gfwapiclient.resources.insights.models.response.Period.start_date
      :type: typing.Optional[datetime.date]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.Period.start_date

   .. py:attribute:: end_date
      :canonical: gfwapiclient.resources.insights.models.response.Period.end_date
      :type: typing.Optional[datetime.date]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.Period.end_date

.. py:class:: PeriodicCounters(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.insights.models.response.PeriodicCounters

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.PeriodicCounters

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.PeriodicCounters.__init__

   .. py:attribute:: events
      :canonical: gfwapiclient.resources.insights.models.response.PeriodicCounters.events
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.PeriodicCounters.events

   .. py:attribute:: events_gap_off
      :canonical: gfwapiclient.resources.insights.models.response.PeriodicCounters.events_gap_off
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.PeriodicCounters.events_gap_off

   .. py:attribute:: events_in_rfmo_without_known_authorization
      :canonical: gfwapiclient.resources.insights.models.response.PeriodicCounters.events_in_rfmo_without_known_authorization
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.PeriodicCounters.events_in_rfmo_without_known_authorization

   .. py:attribute:: events_in_no_take_mpas
      :canonical: gfwapiclient.resources.insights.models.response.PeriodicCounters.events_in_no_take_mpas
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.PeriodicCounters.events_in_no_take_mpas

.. py:class:: Gap(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.insights.models.response.Gap

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.Gap

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.Gap.__init__

   .. py:attribute:: datasets
      :canonical: gfwapiclient.resources.insights.models.response.Gap.datasets
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.Gap.datasets

   .. py:attribute:: historical_counters
      :canonical: gfwapiclient.resources.insights.models.response.Gap.historical_counters
      :type: typing.Optional[gfwapiclient.resources.insights.models.response.PeriodicCounters]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.Gap.historical_counters

   .. py:attribute:: period_selected_counters
      :canonical: gfwapiclient.resources.insights.models.response.Gap.period_selected_counters
      :type: typing.Optional[gfwapiclient.resources.insights.models.response.PeriodicCounters]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.Gap.period_selected_counters

   .. py:attribute:: ais_off
      :canonical: gfwapiclient.resources.insights.models.response.Gap.ais_off
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.Gap.ais_off

.. py:class:: Coverage(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.insights.models.response.Coverage

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.Coverage

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.Coverage.__init__

   .. py:attribute:: blocks
      :canonical: gfwapiclient.resources.insights.models.response.Coverage.blocks
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.Coverage.blocks

   .. py:attribute:: blocks_with_positions
      :canonical: gfwapiclient.resources.insights.models.response.Coverage.blocks_with_positions
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.Coverage.blocks_with_positions

   .. py:attribute:: percentage
      :canonical: gfwapiclient.resources.insights.models.response.Coverage.percentage
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.Coverage.percentage

.. py:class:: ApparentFishing(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.insights.models.response.ApparentFishing

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.ApparentFishing

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.ApparentFishing.__init__

   .. py:attribute:: datasets
      :canonical: gfwapiclient.resources.insights.models.response.ApparentFishing.datasets
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.ApparentFishing.datasets

   .. py:attribute:: historical_counters
      :canonical: gfwapiclient.resources.insights.models.response.ApparentFishing.historical_counters
      :type: typing.Optional[gfwapiclient.resources.insights.models.response.PeriodicCounters]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.ApparentFishing.historical_counters

   .. py:attribute:: period_selected_counters
      :canonical: gfwapiclient.resources.insights.models.response.ApparentFishing.period_selected_counters
      :type: typing.Optional[gfwapiclient.resources.insights.models.response.PeriodicCounters]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.ApparentFishing.period_selected_counters

   .. py:attribute:: events_in_rfmo_without_known_authorization
      :canonical: gfwapiclient.resources.insights.models.response.ApparentFishing.events_in_rfmo_without_known_authorization
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.ApparentFishing.events_in_rfmo_without_known_authorization

   .. py:attribute:: events_in_no_take_mpas
      :canonical: gfwapiclient.resources.insights.models.response.ApparentFishing.events_in_no_take_mpas
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.ApparentFishing.events_in_no_take_mpas

.. py:class:: IuuListPeriod(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.insights.models.response.IuuListPeriod

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.IuuListPeriod

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.IuuListPeriod.__init__

   .. py:attribute:: from_
      :canonical: gfwapiclient.resources.insights.models.response.IuuListPeriod.from_
      :type: typing.Optional[datetime.datetime]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.IuuListPeriod.from_

   .. py:attribute:: to
      :canonical: gfwapiclient.resources.insights.models.response.IuuListPeriod.to
      :type: typing.Optional[datetime.datetime]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.IuuListPeriod.to

.. py:class:: IuuVesselList(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.insights.models.response.IuuVesselList

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.IuuVesselList

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.IuuVesselList.__init__

   .. py:attribute:: values_in_the_period
      :canonical: gfwapiclient.resources.insights.models.response.IuuVesselList.values_in_the_period
      :type: typing.Optional[typing.List[gfwapiclient.resources.insights.models.response.IuuListPeriod]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.IuuVesselList.values_in_the_period

   .. py:attribute:: total_times_listed
      :canonical: gfwapiclient.resources.insights.models.response.IuuVesselList.total_times_listed
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.IuuVesselList.total_times_listed

   .. py:attribute:: total_times_listed_in_the_period
      :canonical: gfwapiclient.resources.insights.models.response.IuuVesselList.total_times_listed_in_the_period
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.IuuVesselList.total_times_listed_in_the_period

.. py:class:: VesselIdentity(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.insights.models.response.VesselIdentity

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.VesselIdentity

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.VesselIdentity.__init__

   .. py:attribute:: datasets
      :canonical: gfwapiclient.resources.insights.models.response.VesselIdentity.datasets
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.VesselIdentity.datasets

   .. py:attribute:: iuu_vessel_list
      :canonical: gfwapiclient.resources.insights.models.response.VesselIdentity.iuu_vessel_list
      :type: typing.Optional[gfwapiclient.resources.insights.models.response.IuuVesselList]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.VesselIdentity.iuu_vessel_list

.. py:class:: VesselInsightItem(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.insights.models.response.VesselInsightItem

   Bases: :py:obj:`gfwapiclient.http.models.ResultItem`

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.VesselInsightItem

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.VesselInsightItem.__init__

   .. py:attribute:: period
      :canonical: gfwapiclient.resources.insights.models.response.VesselInsightItem.period
      :type: typing.Optional[gfwapiclient.resources.insights.models.response.Period]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.VesselInsightItem.period

   .. py:attribute:: vessel_ids_without_identity
      :canonical: gfwapiclient.resources.insights.models.response.VesselInsightItem.vessel_ids_without_identity
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.VesselInsightItem.vessel_ids_without_identity

   .. py:attribute:: gap
      :canonical: gfwapiclient.resources.insights.models.response.VesselInsightItem.gap
      :type: typing.Optional[gfwapiclient.resources.insights.models.response.Gap]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.VesselInsightItem.gap

   .. py:attribute:: coverage
      :canonical: gfwapiclient.resources.insights.models.response.VesselInsightItem.coverage
      :type: typing.Optional[gfwapiclient.resources.insights.models.response.Coverage]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.VesselInsightItem.coverage

   .. py:attribute:: apparent_fishing
      :canonical: gfwapiclient.resources.insights.models.response.VesselInsightItem.apparent_fishing
      :type: typing.Optional[gfwapiclient.resources.insights.models.response.ApparentFishing]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.VesselInsightItem.apparent_fishing

   .. py:attribute:: vessel_identity
      :canonical: gfwapiclient.resources.insights.models.response.VesselInsightItem.vessel_identity
      :type: typing.Optional[gfwapiclient.resources.insights.models.response.VesselIdentity]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.VesselInsightItem.vessel_identity

.. py:class:: VesselInsightResult(data: gfwapiclient.resources.insights.models.response.VesselInsightItem)
   :canonical: gfwapiclient.resources.insights.models.response.VesselInsightResult

   Bases: :py:obj:`gfwapiclient.http.models.Result`\ [\ :py:obj:`gfwapiclient.resources.insights.models.response.VesselInsightItem`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.VesselInsightResult

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.VesselInsightResult.__init__

   .. py:attribute:: _result_item_class
      :canonical: gfwapiclient.resources.insights.models.response.VesselInsightResult._result_item_class
      :type: typing.Type[gfwapiclient.resources.insights.models.response.VesselInsightItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.VesselInsightResult._result_item_class

   .. py:attribute:: _data
      :canonical: gfwapiclient.resources.insights.models.response.VesselInsightResult._data
      :type: gfwapiclient.resources.insights.models.response.VesselInsightItem
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.response.VesselInsightResult._data
