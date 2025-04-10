:py:mod:`gfwapiclient.resources.events.detail.endpoints`
========================================================

.. py:module:: gfwapiclient.resources.events.detail.endpoints

.. autodoc2-docstring:: gfwapiclient.resources.events.detail.endpoints
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`EventDetailEndPoint <gfwapiclient.resources.events.detail.endpoints.EventDetailEndPoint>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.detail.endpoints.EventDetailEndPoint
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.events.detail.endpoints.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.detail.endpoints.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.events.detail.endpoints.__all__
   :value: ['EventDetailEndPoint']

   .. autodoc2-docstring:: gfwapiclient.resources.events.detail.endpoints.__all__

.. py:class:: EventDetailEndPoint(*, event_id: str, request_params: gfwapiclient.resources.events.detail.models.request.EventDetailParams, http_client: gfwapiclient.http.client.HTTPClient)
   :canonical: gfwapiclient.resources.events.detail.endpoints.EventDetailEndPoint

   Bases: :py:obj:`gfwapiclient.http.endpoints.GetEndPoint`\ [\ :py:obj:`gfwapiclient.resources.events.detail.models.request.EventDetailParams`\ , :py:obj:`gfwapiclient.http.models.RequestBody`\ , :py:obj:`gfwapiclient.resources.events.detail.models.response.EventDetailItem`\ , :py:obj:`gfwapiclient.resources.events.detail.models.response.EventDetailResult`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.events.detail.endpoints.EventDetailEndPoint

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.detail.endpoints.EventDetailEndPoint.__init__
