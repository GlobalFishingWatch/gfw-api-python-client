:py:mod:`gfwapiclient.resources.bulk_downloads.base.models.response`
====================================================================

.. py:module:: gfwapiclient.resources.bulk_downloads.base.models.response

.. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`BulkReportStatus <gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportStatus>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportStatus
          :summary:
   * - :py:obj:`BulkReportGeography <gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportGeography>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportGeography
          :summary:
   * - :py:obj:`BulkReportItem <gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.bulk_downloads.base.models.response.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.bulk_downloads.base.models.response.__all__
   :value: ['BulkReportItem']

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.__all__

.. py:class:: BulkReportStatus()
   :canonical: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportStatus

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportStatus

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportStatus.__init__

   .. py:attribute:: PENDING
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportStatus.PENDING
      :value: 'pending'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportStatus.PENDING

   .. py:attribute:: PROCESSING
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportStatus.PROCESSING
      :value: 'processing'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportStatus.PROCESSING

   .. py:attribute:: DONE
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportStatus.DONE
      :value: 'done'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportStatus.DONE

   .. py:attribute:: FAILED
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportStatus.FAILED
      :value: 'failed'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportStatus.FAILED

.. py:class:: BulkReportGeography(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportGeography

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportGeography

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportGeography.__init__

   .. py:attribute:: type
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportGeography.type
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportGeography.type

   .. py:attribute:: dataset
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportGeography.dataset
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportGeography.dataset

   .. py:attribute:: id
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportGeography.id
      :type: typing.Optional[typing.Union[str, int]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportGeography.id

.. py:class:: BulkReportItem(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem

   Bases: :py:obj:`gfwapiclient.http.models.ResultItem`

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.__init__

   .. py:attribute:: id
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.id
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.id

   .. py:attribute:: name
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.name
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.name

   .. py:attribute:: file_path
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.file_path
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.file_path

   .. py:attribute:: format
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.format
      :type: typing.Optional[gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFormat]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.format

   .. py:attribute:: filters
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.filters
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.filters

   .. py:attribute:: geom
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.geom
      :type: typing.Optional[gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportGeography]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.geom

   .. py:attribute:: status
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.status
      :type: typing.Optional[gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportStatus]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.status

   .. py:attribute:: owner_id
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.owner_id
      :type: typing.Optional[typing.Union[str, int]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.owner_id

   .. py:attribute:: owner_type
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.owner_type
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.owner_type

   .. py:attribute:: created_at
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.created_at
      :type: typing.Optional[datetime.datetime]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.created_at

   .. py:attribute:: updated_at
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.updated_at
      :type: typing.Optional[datetime.datetime]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.updated_at

   .. py:attribute:: file_size
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.file_size
      :type: typing.Optional[float]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.file_size

   .. py:method:: empty_datetime_str_to_none(value: typing.Any) -> typing.Optional[typing.Any]
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.empty_datetime_str_to_none
      :classmethod:

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem.empty_datetime_str_to_none
