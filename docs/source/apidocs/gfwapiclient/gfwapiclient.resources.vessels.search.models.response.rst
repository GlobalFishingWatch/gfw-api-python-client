:py:mod:`gfwapiclient.resources.vessels.search.models.response`
===============================================================

.. py:module:: gfwapiclient.resources.vessels.search.models.response

.. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.response
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`VesselSearchItem <gfwapiclient.resources.vessels.search.models.response.VesselSearchItem>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.response.VesselSearchItem
          :summary:
   * - :py:obj:`VesselSearchResult <gfwapiclient.resources.vessels.search.models.response.VesselSearchResult>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.response.VesselSearchResult
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.vessels.search.models.response.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.response.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.vessels.search.models.response.__all__
   :value: ['VesselSearchItem', 'VesselSearchResult']

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.response.__all__

.. py:class:: VesselSearchItem(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.vessels.search.models.response.VesselSearchItem

   Bases: :py:obj:`gfwapiclient.resources.vessels.base.models.response.VesselItem`

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.response.VesselSearchItem

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.response.VesselSearchItem.__init__

.. py:class:: VesselSearchResult(data: typing.List[gfwapiclient.resources.vessels.search.models.response.VesselSearchItem])
   :canonical: gfwapiclient.resources.vessels.search.models.response.VesselSearchResult

   Bases: :py:obj:`gfwapiclient.http.models.Result`\ [\ :py:obj:`gfwapiclient.resources.vessels.search.models.response.VesselSearchItem`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.response.VesselSearchResult

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.response.VesselSearchResult.__init__

   .. py:attribute:: _result_item_class
      :canonical: gfwapiclient.resources.vessels.search.models.response.VesselSearchResult._result_item_class
      :type: typing.Type[gfwapiclient.resources.vessels.search.models.response.VesselSearchItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.response.VesselSearchResult._result_item_class

   .. py:attribute:: _data
      :canonical: gfwapiclient.resources.vessels.search.models.response.VesselSearchResult._data
      :type: typing.List[gfwapiclient.resources.vessels.search.models.response.VesselSearchItem]
      :value: None

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.response.VesselSearchResult._data
