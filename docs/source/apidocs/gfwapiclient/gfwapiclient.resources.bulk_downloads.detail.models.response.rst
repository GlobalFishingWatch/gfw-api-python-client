:py:mod:`gfwapiclient.resources.bulk_downloads.detail.models.response`
======================================================================

.. py:module:: gfwapiclient.resources.bulk_downloads.detail.models.response

.. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.detail.models.response
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`BulkReportDetailItem <gfwapiclient.resources.bulk_downloads.detail.models.response.BulkReportDetailItem>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.detail.models.response.BulkReportDetailItem
          :summary:
   * - :py:obj:`BulkReportDetailResult <gfwapiclient.resources.bulk_downloads.detail.models.response.BulkReportDetailResult>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.detail.models.response.BulkReportDetailResult
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.bulk_downloads.detail.models.response.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.detail.models.response.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.bulk_downloads.detail.models.response.__all__
   :value: ['BulkReportDetailItem', 'BulkReportDetailResult']

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.detail.models.response.__all__

.. py:class:: BulkReportDetailItem(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.bulk_downloads.detail.models.response.BulkReportDetailItem

   Bases: :py:obj:`gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem`

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.detail.models.response.BulkReportDetailItem

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.detail.models.response.BulkReportDetailItem.__init__

.. py:class:: BulkReportDetailResult(data: gfwapiclient.resources.bulk_downloads.detail.models.response.BulkReportDetailItem)
   :canonical: gfwapiclient.resources.bulk_downloads.detail.models.response.BulkReportDetailResult

   Bases: :py:obj:`gfwapiclient.http.models.Result`\ [\ :py:obj:`gfwapiclient.resources.bulk_downloads.detail.models.response.BulkReportDetailItem`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.detail.models.response.BulkReportDetailResult

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.detail.models.response.BulkReportDetailResult.__init__

   .. py:attribute:: _result_item_class
      :canonical: gfwapiclient.resources.bulk_downloads.detail.models.response.BulkReportDetailResult._result_item_class
      :type: typing.Type[gfwapiclient.resources.bulk_downloads.detail.models.response.BulkReportDetailItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.detail.models.response.BulkReportDetailResult._result_item_class

   .. py:attribute:: _data
      :canonical: gfwapiclient.resources.bulk_downloads.detail.models.response.BulkReportDetailResult._data
      :type: gfwapiclient.resources.bulk_downloads.detail.models.response.BulkReportDetailItem
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.detail.models.response.BulkReportDetailResult._data
