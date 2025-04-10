:py:mod:`gfwapiclient.resources.vessels.resources`
==================================================

.. py:module:: gfwapiclient.resources.vessels.resources

.. autodoc2-docstring:: gfwapiclient.resources.vessels.resources
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`VesselResource <gfwapiclient.resources.vessels.resources.VesselResource>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.resources.VesselResource
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.vessels.resources.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.resources.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.vessels.resources.__all__
   :value: ['VesselResource']

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.resources.__all__

.. py:class:: VesselResource(*, http_client: gfwapiclient.http.client.HTTPClient)
   :canonical: gfwapiclient.resources.vessels.resources.VesselResource

   Bases: :py:obj:`gfwapiclient.http.resources.BaseResource`

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.resources.VesselResource

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.resources.VesselResource.__init__

   .. py:method:: search_vessels(*, since: typing.Optional[str] = None, limit: typing.Optional[int] = 20, datasets: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.vessels.base.models.request.VesselDataset], typing.List[str]]] = None, query: typing.Optional[str] = None, where: typing.Optional[str] = None, match_fields: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.vessels.base.models.request.VesselMatchField], typing.List[str]]] = None, includes: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.vessels.search.models.request.VesselSearchInclude], typing.List[str]]] = None, **kwargs: typing.Dict[str, typing.Any]) -> gfwapiclient.resources.vessels.search.models.response.VesselSearchResult
      :canonical: gfwapiclient.resources.vessels.resources.VesselResource.search_vessels
      :async:

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.resources.VesselResource.search_vessels

   .. py:method:: get_vessels_by_ids(*, ids: typing.List[str], datasets: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.vessels.base.models.request.VesselDataset], typing.List[str]]] = None, registries_info_data: typing.Optional[gfwapiclient.resources.vessels.base.models.request.VesselRegistryInfoData] = None, includes: typing.Optional[typing.List[gfwapiclient.resources.vessels.base.models.request.VesselInclude]] = None, match_fields: typing.Optional[typing.List[gfwapiclient.resources.vessels.base.models.request.VesselMatchField]] = None, vessel_groups: typing.Optional[typing.List[str]] = None, **kwargs: typing.Dict[str, typing.Any]) -> gfwapiclient.resources.vessels.list.models.response.VesselListResult
      :canonical: gfwapiclient.resources.vessels.resources.VesselResource.get_vessels_by_ids
      :async:

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.resources.VesselResource.get_vessels_by_ids

   .. py:method:: get_vessel_by_id(*, id: str, dataset: typing.Optional[typing.Union[gfwapiclient.resources.vessels.base.models.request.VesselDataset, str]] = None, registries_info_data: typing.Optional[typing.Union[gfwapiclient.resources.vessels.base.models.request.VesselRegistryInfoData, str]] = None, includes: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.vessels.base.models.request.VesselInclude], typing.List[str]]] = None, match_fields: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.vessels.base.models.request.VesselMatchField], typing.List[str]]] = None, **kwargs: typing.Dict[str, typing.Any]) -> gfwapiclient.resources.vessels.detail.models.response.VesselDetailResult
      :canonical: gfwapiclient.resources.vessels.resources.VesselResource.get_vessel_by_id
      :async:

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.resources.VesselResource.get_vessel_by_id

   .. py:method:: _prepare_search_vessels_request_params(*, since: typing.Optional[str] = None, limit: typing.Optional[int] = 20, datasets: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.vessels.base.models.request.VesselDataset], typing.List[str]]] = None, query: typing.Optional[str] = None, where: typing.Optional[str] = None, match_fields: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.vessels.base.models.request.VesselMatchField], typing.List[str]]] = None, includes: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.vessels.search.models.request.VesselSearchInclude], typing.List[str]]] = None) -> gfwapiclient.resources.vessels.search.models.request.VesselSearchParams
      :canonical: gfwapiclient.resources.vessels.resources.VesselResource._prepare_search_vessels_request_params

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.resources.VesselResource._prepare_search_vessels_request_params

   .. py:method:: _prepare_get_vessels_by_ids_request_params(*, ids: typing.List[str], datasets: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.vessels.base.models.request.VesselDataset], typing.List[str]]] = None, registries_info_data: typing.Optional[typing.Union[gfwapiclient.resources.vessels.base.models.request.VesselRegistryInfoData, str]] = None, includes: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.vessels.base.models.request.VesselInclude], typing.List[str]]] = None, match_fields: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.vessels.base.models.request.VesselMatchField], typing.List[str]]] = None, vessel_groups: typing.Optional[typing.List[str]] = None) -> gfwapiclient.resources.vessels.list.models.request.VesselListParams
      :canonical: gfwapiclient.resources.vessels.resources.VesselResource._prepare_get_vessels_by_ids_request_params

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.resources.VesselResource._prepare_get_vessels_by_ids_request_params

   .. py:method:: _prepare_get_vessel_by_id_request_params(*, dataset: typing.Optional[typing.Union[gfwapiclient.resources.vessels.base.models.request.VesselDataset, str]] = None, registries_info_data: typing.Optional[typing.Union[gfwapiclient.resources.vessels.base.models.request.VesselRegistryInfoData, str]] = None, includes: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.vessels.base.models.request.VesselInclude], typing.List[str]]] = None, match_fields: typing.Optional[typing.Union[typing.List[gfwapiclient.resources.vessels.base.models.request.VesselMatchField], typing.List[str]]] = None) -> gfwapiclient.resources.vessels.detail.models.request.VesselDetailParams
      :canonical: gfwapiclient.resources.vessels.resources.VesselResource._prepare_get_vessel_by_id_request_params

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.resources.VesselResource._prepare_get_vessel_by_id_request_params
