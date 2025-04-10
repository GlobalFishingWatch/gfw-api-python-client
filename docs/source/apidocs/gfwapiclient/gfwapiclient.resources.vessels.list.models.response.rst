:py:mod:`gfwapiclient.resources.vessels.list.models.response`
=============================================================

.. py:module:: gfwapiclient.resources.vessels.list.models.response

.. autodoc2-docstring:: gfwapiclient.resources.vessels.list.models.response
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`VesselListItem <gfwapiclient.resources.vessels.list.models.response.VesselListItem>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.models.response.VesselListItem
          :summary:
   * - :py:obj:`VesselListResult <gfwapiclient.resources.vessels.list.models.response.VesselListResult>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.models.response.VesselListResult
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.vessels.list.models.response.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.models.response.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.vessels.list.models.response.__all__
   :value: ['VesselListItem', 'VesselListResult']

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.models.response.__all__

.. py:class:: VesselListItem(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.vessels.list.models.response.VesselListItem

   Bases: :py:obj:`gfwapiclient.resources.vessels.base.models.response.VesselItem`

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.models.response.VesselListItem

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.models.response.VesselListItem.__init__

.. py:class:: VesselListResult(data: typing.List[gfwapiclient.resources.vessels.list.models.response.VesselListItem])
   :canonical: gfwapiclient.resources.vessels.list.models.response.VesselListResult

   Bases: :py:obj:`gfwapiclient.http.models.Result`\ [\ :py:obj:`gfwapiclient.resources.vessels.list.models.response.VesselListItem`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.models.response.VesselListResult

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.models.response.VesselListResult.__init__

   .. py:attribute:: _result_item_class
      :canonical: gfwapiclient.resources.vessels.list.models.response.VesselListResult._result_item_class
      :type: typing.Type[gfwapiclient.resources.vessels.list.models.response.VesselListItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.models.response.VesselListResult._result_item_class

   .. py:attribute:: _data
      :canonical: gfwapiclient.resources.vessels.list.models.response.VesselListResult._data
      :type: typing.List[gfwapiclient.resources.vessels.list.models.response.VesselListItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.models.response.VesselListResult._data
