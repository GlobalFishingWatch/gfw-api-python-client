:py:mod:`gfwapiclient.resources.events.stats.endpoints`
=======================================================

.. py:module:: gfwapiclient.resources.events.stats.endpoints

.. autodoc2-docstring:: gfwapiclient.resources.events.stats.endpoints
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`EventStatsEndPoint <gfwapiclient.resources.events.stats.endpoints.EventStatsEndPoint>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.stats.endpoints.EventStatsEndPoint
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.events.stats.endpoints.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.stats.endpoints.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.events.stats.endpoints.__all__
   :value: ['EventStatsEndPoint']

   .. autodoc2-docstring:: gfwapiclient.resources.events.stats.endpoints.__all__

.. py:class:: EventStatsEndPoint(*, request_body: gfwapiclient.resources.events.stats.models.request.EventStatsBody, http_client: gfwapiclient.http.client.HTTPClient)
   :canonical: gfwapiclient.resources.events.stats.endpoints.EventStatsEndPoint

   Bases: :py:obj:`gfwapiclient.http.endpoints.PostEndPoint`\ [\ :py:obj:`gfwapiclient.http.models.RequestParams`\ , :py:obj:`gfwapiclient.resources.events.stats.models.request.EventStatsBody`\ , :py:obj:`gfwapiclient.resources.events.stats.models.response.EventStatsItem`\ , :py:obj:`gfwapiclient.resources.events.stats.models.response.EventStatsResult`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.events.stats.endpoints.EventStatsEndPoint

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.stats.endpoints.EventStatsEndPoint.__init__
