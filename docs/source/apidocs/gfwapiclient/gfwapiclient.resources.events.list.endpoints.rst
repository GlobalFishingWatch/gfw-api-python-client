:py:mod:`gfwapiclient.resources.events.list.endpoints`
======================================================

.. py:module:: gfwapiclient.resources.events.list.endpoints

.. autodoc2-docstring:: gfwapiclient.resources.events.list.endpoints
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`EventListEndPoint <gfwapiclient.resources.events.list.endpoints.EventListEndPoint>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.list.endpoints.EventListEndPoint
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.events.list.endpoints.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.list.endpoints.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.events.list.endpoints.__all__
   :value: ['EventListEndPoint']

   .. autodoc2-docstring:: gfwapiclient.resources.events.list.endpoints.__all__

.. py:class:: EventListEndPoint(*, request_params: gfwapiclient.resources.events.list.models.request.EventListParams, request_body: gfwapiclient.resources.events.list.models.request.EventListBody, http_client: gfwapiclient.http.client.HTTPClient)
   :canonical: gfwapiclient.resources.events.list.endpoints.EventListEndPoint

   Bases: :py:obj:`gfwapiclient.http.endpoints.PostEndPoint`\ [\ :py:obj:`gfwapiclient.resources.events.list.models.request.EventListParams`\ , :py:obj:`gfwapiclient.resources.events.list.models.request.EventListBody`\ , :py:obj:`gfwapiclient.resources.events.list.models.response.EventListItem`\ , :py:obj:`gfwapiclient.resources.events.list.models.response.EventListResult`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.events.list.endpoints.EventListEndPoint

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.list.endpoints.EventListEndPoint.__init__

   .. py:method:: _transform_response_data(*, body: typing.Union[typing.List[typing.Dict[str, typing.Any]], typing.Dict[str, typing.Any]]) -> typing.Union[typing.List[typing.Dict[str, typing.Any]], typing.Dict[str, typing.Any]]
      :canonical: gfwapiclient.resources.events.list.endpoints.EventListEndPoint._transform_response_data

      .. autodoc2-docstring:: gfwapiclient.resources.events.list.endpoints.EventListEndPoint._transform_response_data
