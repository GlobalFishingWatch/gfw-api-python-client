:py:mod:`gfwapiclient.resources.bulk_downloads.file.models.response`
====================================================================

.. py:module:: gfwapiclient.resources.bulk_downloads.file.models.response

.. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.file.models.response
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`BulkReportFileItem <gfwapiclient.resources.bulk_downloads.file.models.response.BulkReportFileItem>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.file.models.response.BulkReportFileItem
          :summary:
   * - :py:obj:`BulkReportFileResult <gfwapiclient.resources.bulk_downloads.file.models.response.BulkReportFileResult>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.file.models.response.BulkReportFileResult
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.bulk_downloads.file.models.response.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.file.models.response.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.bulk_downloads.file.models.response.__all__
   :value: ['BulkReportFileItem', 'BulkReportFileResult']

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.file.models.response.__all__

.. py:class:: BulkReportFileItem(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.bulk_downloads.file.models.response.BulkReportFileItem

   Bases: :py:obj:`gfwapiclient.http.models.ResultItem`

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.file.models.response.BulkReportFileItem

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.file.models.response.BulkReportFileItem.__init__

   .. py:attribute:: url
      :canonical: gfwapiclient.resources.bulk_downloads.file.models.response.BulkReportFileItem.url
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.file.models.response.BulkReportFileItem.url

.. py:class:: BulkReportFileResult(data: gfwapiclient.resources.bulk_downloads.file.models.response.BulkReportFileItem)
   :canonical: gfwapiclient.resources.bulk_downloads.file.models.response.BulkReportFileResult

   Bases: :py:obj:`gfwapiclient.http.models.Result`\ [\ :py:obj:`gfwapiclient.resources.bulk_downloads.file.models.response.BulkReportFileItem`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.file.models.response.BulkReportFileResult

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.file.models.response.BulkReportFileResult.__init__

   .. py:attribute:: _result_item_class
      :canonical: gfwapiclient.resources.bulk_downloads.file.models.response.BulkReportFileResult._result_item_class
      :type: typing.Type[gfwapiclient.resources.bulk_downloads.file.models.response.BulkReportFileItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.file.models.response.BulkReportFileResult._result_item_class

   .. py:attribute:: _data
      :canonical: gfwapiclient.resources.bulk_downloads.file.models.response.BulkReportFileResult._data
      :type: gfwapiclient.resources.bulk_downloads.file.models.response.BulkReportFileItem
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.file.models.response.BulkReportFileResult._data
