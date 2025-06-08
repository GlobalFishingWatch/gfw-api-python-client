:py:mod:`gfwapiclient.resources.datasets.resources`
===================================================

.. py:module:: gfwapiclient.resources.datasets.resources

.. autodoc2-docstring:: gfwapiclient.resources.datasets.resources
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`DatasetResource <gfwapiclient.resources.datasets.resources.DatasetResource>`
     - .. autodoc2-docstring:: gfwapiclient.resources.datasets.resources.DatasetResource
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.datasets.resources.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.datasets.resources.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.datasets.resources.__all__
   :value: ['DatasetResource']

   .. autodoc2-docstring:: gfwapiclient.resources.datasets.resources.__all__

.. py:class:: DatasetResource(*, http_client: gfwapiclient.http.client.HTTPClient)
   :canonical: gfwapiclient.resources.datasets.resources.DatasetResource

   Bases: :py:obj:`gfwapiclient.http.resources.BaseResource`

   .. autodoc2-docstring:: gfwapiclient.resources.datasets.resources.DatasetResource

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.datasets.resources.DatasetResource.__init__

   .. py:method:: get_sar_fixed_infrastructure(*, z: typing.Optional[int] = None, x: typing.Optional[int] = None, y: typing.Optional[int] = None, geometry: typing.Optional[typing.Union[geojson_pydantic.geometries.Geometry, typing.Dict[str, typing.Any]]] = None, **kwargs: typing.Dict[str, typing.Any]) -> gfwapiclient.resources.datasets.models.response.SARFixedInfrastructureResult
      :canonical: gfwapiclient.resources.datasets.resources.DatasetResource.get_sar_fixed_infrastructure
      :async:

      .. autodoc2-docstring:: gfwapiclient.resources.datasets.resources.DatasetResource.get_sar_fixed_infrastructure

   .. py:method:: _prepare_get_sar_fixed_infrastructure_request_params(*, z: typing.Optional[int] = None, x: typing.Optional[int] = None, y: typing.Optional[int] = None, geometry: typing.Optional[typing.Union[geojson_pydantic.geometries.Geometry, typing.Dict[str, typing.Any]]] = None) -> gfwapiclient.resources.datasets.models.request.SARFixedInfrastructureParams
      :canonical: gfwapiclient.resources.datasets.resources.DatasetResource._prepare_get_sar_fixed_infrastructure_request_params

      .. autodoc2-docstring:: gfwapiclient.resources.datasets.resources.DatasetResource._prepare_get_sar_fixed_infrastructure_request_params
