:py:mod:`gfwapiclient.resources.vessels.detail.models.response`
===============================================================

.. py:module:: gfwapiclient.resources.vessels.detail.models.response

.. autodoc2-docstring:: gfwapiclient.resources.vessels.detail.models.response
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`VesselDetailItem <gfwapiclient.resources.vessels.detail.models.response.VesselDetailItem>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.detail.models.response.VesselDetailItem
          :summary:
   * - :py:obj:`VesselDetailResult <gfwapiclient.resources.vessels.detail.models.response.VesselDetailResult>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.detail.models.response.VesselDetailResult
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.vessels.detail.models.response.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.detail.models.response.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.vessels.detail.models.response.__all__
   :value: ['VesselDetailItem', 'VesselDetailResult']

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.detail.models.response.__all__

.. py:class:: VesselDetailItem(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.vessels.detail.models.response.VesselDetailItem

   Bases: :py:obj:`gfwapiclient.resources.vessels.base.models.response.VesselItem`

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.detail.models.response.VesselDetailItem

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.detail.models.response.VesselDetailItem.__init__

.. py:class:: VesselDetailResult(data: gfwapiclient.resources.vessels.detail.models.response.VesselDetailItem)
   :canonical: gfwapiclient.resources.vessels.detail.models.response.VesselDetailResult

   Bases: :py:obj:`gfwapiclient.http.models.Result`\ [\ :py:obj:`gfwapiclient.resources.vessels.detail.models.response.VesselDetailItem`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.detail.models.response.VesselDetailResult

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.detail.models.response.VesselDetailResult.__init__

   .. py:attribute:: _result_item_class
      :canonical: gfwapiclient.resources.vessels.detail.models.response.VesselDetailResult._result_item_class
      :type: typing.Type[gfwapiclient.resources.vessels.detail.models.response.VesselDetailItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.detail.models.response.VesselDetailResult._result_item_class

   .. py:attribute:: _data
      :canonical: gfwapiclient.resources.vessels.detail.models.response.VesselDetailResult._data
      :type: gfwapiclient.resources.vessels.detail.models.response.VesselDetailItem
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.detail.models.response.VesselDetailResult._data
