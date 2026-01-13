:py:mod:`gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response`
===============================================================================================

.. py:module:: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response

.. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`BulkFixedInfrastructureDataQueryItem <gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem
          :summary:
   * - :py:obj:`BulkFixedInfrastructureDataQueryResult <gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryResult>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryResult
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.__all__
   :value: ['BulkFixedInfrastructureDataQueryItem', 'BulkFixedInfrastructureDataQueryResult']

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.__all__

.. py:class:: BulkFixedInfrastructureDataQueryItem(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem

   Bases: :py:obj:`gfwapiclient.resources.bulk_downloads.query.models.base.response.BulkReportQueryItem`

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem.__init__

   .. py:attribute:: detection_id
      :canonical: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem.detection_id
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem.detection_id

   .. py:attribute:: detection_date
      :canonical: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem.detection_date
      :type: typing.Optional[datetime.datetime]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem.detection_date

   .. py:attribute:: structure_id
      :canonical: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem.structure_id
      :type: typing.Optional[typing.Union[str, int]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem.structure_id

   .. py:attribute:: lat
      :canonical: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem.lat
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem.lat

   .. py:attribute:: lon
      :canonical: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem.lon
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem.lon

   .. py:attribute:: structure_start_date
      :canonical: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem.structure_start_date
      :type: typing.Optional[datetime.datetime]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem.structure_start_date

   .. py:attribute:: structure_end_date
      :canonical: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem.structure_end_date
      :type: typing.Optional[datetime.datetime]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem.structure_end_date

   .. py:attribute:: label
      :canonical: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem.label
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem.label

   .. py:attribute:: label_confidence
      :canonical: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem.label_confidence
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem.label_confidence

   .. py:method:: empty_datetime_str_to_none(value: typing.Any) -> typing.Optional[typing.Any]
      :canonical: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem.empty_datetime_str_to_none
      :classmethod:

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem.empty_datetime_str_to_none

.. py:class:: BulkFixedInfrastructureDataQueryResult(data: typing.List[gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem])
   :canonical: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryResult

   Bases: :py:obj:`gfwapiclient.resources.bulk_downloads.query.models.base.response.BulkReportQueryResult`\ [\ :py:obj:`gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryResult

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryResult.__init__

   .. py:attribute:: _result_item_class
      :canonical: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryResult._result_item_class
      :type: typing.Type[gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryResult._result_item_class

   .. py:attribute:: _data
      :canonical: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryResult._data
      :type: typing.List[gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.query.models.fixed_infrastructure_data.response.BulkFixedInfrastructureDataQueryResult._data
