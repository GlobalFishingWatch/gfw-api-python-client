:py:mod:`gfwapiclient.resources.vessels.search.endpoints`
=========================================================

.. py:module:: gfwapiclient.resources.vessels.search.endpoints

.. autodoc2-docstring:: gfwapiclient.resources.vessels.search.endpoints
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`VesselSearchEndPoint <gfwapiclient.resources.vessels.search.endpoints.VesselSearchEndPoint>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.endpoints.VesselSearchEndPoint
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.vessels.search.endpoints.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.endpoints.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.vessels.search.endpoints.__all__
   :value: ['VesselSearchEndPoint']

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.endpoints.__all__

.. py:class:: VesselSearchEndPoint(*, request_params: gfwapiclient.resources.vessels.search.models.request.VesselSearchParams, http_client: gfwapiclient.http.client.HTTPClient)
   :canonical: gfwapiclient.resources.vessels.search.endpoints.VesselSearchEndPoint

   Bases: :py:obj:`gfwapiclient.http.endpoints.GetEndPoint`\ [\ :py:obj:`gfwapiclient.resources.vessels.search.models.request.VesselSearchParams`\ , :py:obj:`gfwapiclient.http.models.RequestBody`\ , :py:obj:`gfwapiclient.resources.vessels.search.models.response.VesselSearchItem`\ , :py:obj:`gfwapiclient.resources.vessels.search.models.response.VesselSearchResult`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.endpoints.VesselSearchEndPoint

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.endpoints.VesselSearchEndPoint.__init__

   .. py:method:: _transform_response_data(*, body: typing.Union[typing.List[typing.Dict[str, typing.Any]], typing.Dict[str, typing.Any]]) -> typing.Union[typing.List[typing.Dict[str, typing.Any]], typing.Dict[str, typing.Any]]
      :canonical: gfwapiclient.resources.vessels.search.endpoints.VesselSearchEndPoint._transform_response_data

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.endpoints.VesselSearchEndPoint._transform_response_data
