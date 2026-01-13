:py:mod:`gfwapiclient.resources.bulk_downloads.list.models.response`
====================================================================

.. py:module:: gfwapiclient.resources.bulk_downloads.list.models.response

.. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.models.response
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`BulkReportListItem <gfwapiclient.resources.bulk_downloads.list.models.response.BulkReportListItem>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.models.response.BulkReportListItem
          :summary:
   * - :py:obj:`BulkReportListResult <gfwapiclient.resources.bulk_downloads.list.models.response.BulkReportListResult>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.models.response.BulkReportListResult
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.bulk_downloads.list.models.response.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.models.response.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.bulk_downloads.list.models.response.__all__
   :value: ['BulkReportListItem', 'BulkReportListResult']

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.models.response.__all__

.. py:class:: BulkReportListItem(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.bulk_downloads.list.models.response.BulkReportListItem

   Bases: :py:obj:`gfwapiclient.resources.bulk_downloads.base.models.response.BulkReportItem`

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.models.response.BulkReportListItem

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.models.response.BulkReportListItem.__init__

.. py:class:: BulkReportListResult(data: typing.List[gfwapiclient.resources.bulk_downloads.list.models.response.BulkReportListItem])
   :canonical: gfwapiclient.resources.bulk_downloads.list.models.response.BulkReportListResult

   Bases: :py:obj:`gfwapiclient.http.models.Result`\ [\ :py:obj:`gfwapiclient.resources.bulk_downloads.list.models.response.BulkReportListItem`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.models.response.BulkReportListResult

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.models.response.BulkReportListResult.__init__

   .. py:attribute:: _result_item_class
      :canonical: gfwapiclient.resources.bulk_downloads.list.models.response.BulkReportListResult._result_item_class
      :type: typing.Type[gfwapiclient.resources.bulk_downloads.list.models.response.BulkReportListItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.models.response.BulkReportListResult._result_item_class

   .. py:attribute:: _data
      :canonical: gfwapiclient.resources.bulk_downloads.list.models.response.BulkReportListResult._data
      :type: typing.List[gfwapiclient.resources.bulk_downloads.list.models.response.BulkReportListItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.list.models.response.BulkReportListResult._data
