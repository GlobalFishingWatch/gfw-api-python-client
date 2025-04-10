:py:mod:`gfwapiclient.resources.fourwings.report.models.response`
=================================================================

.. py:module:: gfwapiclient.resources.fourwings.report.models.response

.. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`FourWingsReportItem <gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem>`
     - .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem
          :summary:
   * - :py:obj:`FourWingsReportResult <gfwapiclient.resources.fourwings.report.models.response.FourWingsReportResult>`
     - .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportResult
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.fourwings.report.models.response.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.fourwings.report.models.response.__all__
   :value: ['FourWingsReportItem', 'FourWingsReportResult']

   .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.__all__

.. py:class:: FourWingsReportItem(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem

   Bases: :py:obj:`gfwapiclient.http.models.ResultItem`

   .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.__init__

   .. py:attribute:: date
      :canonical: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.date
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.date

   .. py:attribute:: detections
      :canonical: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.detections
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.detections

   .. py:attribute:: flag
      :canonical: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.flag
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.flag

   .. py:attribute:: gear_type
      :canonical: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.gear_type
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.gear_type

   .. py:attribute:: hours
      :canonical: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.hours
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.hours

   .. py:attribute:: vessel_ids
      :canonical: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.vessel_ids
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.vessel_ids

   .. py:attribute:: vessel_id
      :canonical: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.vessel_id
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.vessel_id

   .. py:attribute:: vessel_type
      :canonical: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.vessel_type
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.vessel_type

   .. py:attribute:: entry_timestamp
      :canonical: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.entry_timestamp
      :type: typing.Optional[datetime.datetime]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.entry_timestamp

   .. py:attribute:: exit_timestamp
      :canonical: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.exit_timestamp
      :type: typing.Optional[datetime.datetime]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.exit_timestamp

   .. py:attribute:: first_transmission_date
      :canonical: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.first_transmission_date
      :type: typing.Optional[datetime.datetime]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.first_transmission_date

   .. py:attribute:: last_transmission_date
      :canonical: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.last_transmission_date
      :type: typing.Optional[datetime.datetime]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.last_transmission_date

   .. py:attribute:: imo
      :canonical: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.imo
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.imo

   .. py:attribute:: mmsi
      :canonical: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.mmsi
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.mmsi

   .. py:attribute:: call_sign
      :canonical: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.call_sign
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.call_sign

   .. py:attribute:: dataset
      :canonical: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.dataset
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.dataset

   .. py:attribute:: report_dataset
      :canonical: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.report_dataset
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.report_dataset

   .. py:attribute:: ship_name
      :canonical: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.ship_name
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.ship_name

   .. py:attribute:: lat
      :canonical: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.lat
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.lat

   .. py:attribute:: lon
      :canonical: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.lon
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.lon

   .. py:method:: empty_datetime_str_to_none(value: typing.Any) -> typing.Optional[typing.Any]
      :canonical: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.empty_datetime_str_to_none
      :classmethod:

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem.empty_datetime_str_to_none

.. py:class:: FourWingsReportResult(data: typing.List[gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem])
   :canonical: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportResult

   Bases: :py:obj:`gfwapiclient.http.models.Result`\ [\ :py:obj:`gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportResult

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportResult.__init__

   .. py:attribute:: _result_item_class
      :canonical: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportResult._result_item_class
      :type: typing.Type[gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportResult._result_item_class

   .. py:attribute:: _data
      :canonical: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportResult._data
      :type: typing.List[gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.models.response.FourWingsReportResult._data
