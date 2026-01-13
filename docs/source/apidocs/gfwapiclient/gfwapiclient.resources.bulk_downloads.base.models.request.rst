:py:mod:`gfwapiclient.resources.bulk_downloads.base.models.request`
===================================================================

.. py:module:: gfwapiclient.resources.bulk_downloads.base.models.request

.. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`BulkReportDataset <gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportDataset>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportDataset
          :summary:
   * - :py:obj:`BulkReportFormat <gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFormat>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFormat
          :summary:
   * - :py:obj:`BulkReportGeometry <gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportGeometry>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportGeometry
          :summary:
   * - :py:obj:`BulkReportRegion <gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportRegion>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportRegion
          :summary:
   * - :py:obj:`BulkReportFileType <gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFileType>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFileType
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.bulk_downloads.base.models.request.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.bulk_downloads.base.models.request.__all__
   :value: ['BulkReportDataset', 'BulkReportFileType', 'BulkReportFormat', 'BulkReportGeometry', 'BulkReportReg...

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.__all__

.. py:class:: BulkReportDataset()
   :canonical: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportDataset

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportDataset

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportDataset.__init__

   .. py:attribute:: FIXED_INFRASTRUCTURE_DATA_LATEST
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportDataset.FIXED_INFRASTRUCTURE_DATA_LATEST
      :value: 'public-fixed-infrastructure-data:latest'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportDataset.FIXED_INFRASTRUCTURE_DATA_LATEST

.. py:class:: BulkReportFormat()
   :canonical: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFormat

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFormat

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFormat.__init__

   .. py:attribute:: CSV
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFormat.CSV
      :value: 'CSV'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFormat.CSV

   .. py:attribute:: JSON
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFormat.JSON
      :value: 'JSON'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFormat.JSON

.. py:class:: BulkReportGeometry(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportGeometry

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportGeometry

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportGeometry.__init__

   .. py:attribute:: type
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportGeometry.type
      :type: str
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportGeometry.type

   .. py:attribute:: coordinates
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportGeometry.coordinates
      :type: typing.Any
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportGeometry.coordinates

.. py:class:: BulkReportRegion(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportRegion

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportRegion

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportRegion.__init__

   .. py:attribute:: dataset
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportRegion.dataset
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportRegion.dataset

   .. py:attribute:: id
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportRegion.id
      :type: typing.Optional[typing.Union[str, int]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportRegion.id

.. py:class:: BulkReportFileType()
   :canonical: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFileType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFileType

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFileType.__init__

   .. py:attribute:: DATA
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFileType.DATA
      :value: 'DATA'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFileType.DATA

   .. py:attribute:: README
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFileType.README
      :value: 'README'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFileType.README

   .. py:attribute:: GEOM
      :canonical: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFileType.GEOM
      :value: 'GEOM'

      .. autodoc2-docstring:: gfwapiclient.resources.bulk_downloads.base.models.request.BulkReportFileType.GEOM
