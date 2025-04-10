:py:mod:`gfwapiclient.resources.vessels.list.endpoints`
=======================================================

.. py:module:: gfwapiclient.resources.vessels.list.endpoints

.. autodoc2-docstring:: gfwapiclient.resources.vessels.list.endpoints
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`VesselListEndPoint <gfwapiclient.resources.vessels.list.endpoints.VesselListEndPoint>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.endpoints.VesselListEndPoint
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.vessels.list.endpoints.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.endpoints.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.vessels.list.endpoints.__all__
   :value: ['VesselListEndPoint']

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.endpoints.__all__

.. py:class:: VesselListEndPoint(*, request_params: gfwapiclient.resources.vessels.list.models.request.VesselListParams, http_client: gfwapiclient.http.client.HTTPClient)
   :canonical: gfwapiclient.resources.vessels.list.endpoints.VesselListEndPoint

   Bases: :py:obj:`gfwapiclient.http.endpoints.GetEndPoint`\ [\ :py:obj:`gfwapiclient.resources.vessels.list.models.request.VesselListParams`\ , :py:obj:`gfwapiclient.http.models.RequestBody`\ , :py:obj:`gfwapiclient.resources.vessels.list.models.response.VesselListItem`\ , :py:obj:`gfwapiclient.resources.vessels.list.models.response.VesselListResult`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.endpoints.VesselListEndPoint

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.endpoints.VesselListEndPoint.__init__

   .. py:method:: _transform_response_data(*, body: typing.Union[typing.List[typing.Dict[str, typing.Any]], typing.Dict[str, typing.Any]]) -> typing.Union[typing.List[typing.Dict[str, typing.Any]], typing.Dict[str, typing.Any]]
      :canonical: gfwapiclient.resources.vessels.list.endpoints.VesselListEndPoint._transform_response_data

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.endpoints.VesselListEndPoint._transform_response_data
