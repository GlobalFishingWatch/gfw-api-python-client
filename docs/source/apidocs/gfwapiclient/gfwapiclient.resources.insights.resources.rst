:py:mod:`gfwapiclient.resources.insights.resources`
===================================================

.. py:module:: gfwapiclient.resources.insights.resources

.. autodoc2-docstring:: gfwapiclient.resources.insights.resources
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`InsightResource <gfwapiclient.resources.insights.resources.InsightResource>`
     - .. autodoc2-docstring:: gfwapiclient.resources.insights.resources.InsightResource
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.insights.resources.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.insights.resources.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.insights.resources.__all__
   :value: ['InsightResource']

   .. autodoc2-docstring:: gfwapiclient.resources.insights.resources.__all__

.. py:class:: InsightResource(*, http_client: gfwapiclient.http.client.HTTPClient)
   :canonical: gfwapiclient.resources.insights.resources.InsightResource

   Bases: :py:obj:`gfwapiclient.http.resources.BaseResource`

   .. autodoc2-docstring:: gfwapiclient.resources.insights.resources.InsightResource

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.insights.resources.InsightResource.__init__

   .. py:method:: get_vessel_insights(*, includes: typing.Union[typing.List[gfwapiclient.resources.insights.models.request.VesselInsightInclude], typing.List[str]], start_date: typing.Union[datetime.date, str], end_date: typing.Union[datetime.date, str], vessels: typing.Union[typing.List[gfwapiclient.resources.insights.models.request.VesselInsightDatasetVessel], typing.List[typing.Dict[str, typing.Any]]], **kwargs: typing.Dict[str, typing.Any]) -> gfwapiclient.resources.insights.models.response.VesselInsightResult
      :canonical: gfwapiclient.resources.insights.resources.InsightResource.get_vessel_insights
      :async:

      .. autodoc2-docstring:: gfwapiclient.resources.insights.resources.InsightResource.get_vessel_insights

   .. py:method:: _prepare_get_vessel_insights_request_body(*, includes: typing.Union[typing.List[gfwapiclient.resources.insights.models.request.VesselInsightInclude], typing.List[str]], start_date: typing.Union[datetime.date, str], end_date: typing.Union[datetime.date, str], vessels: typing.Union[typing.List[gfwapiclient.resources.insights.models.request.VesselInsightDatasetVessel], typing.List[typing.Dict[str, typing.Any]]], **kwargs: typing.Dict[str, typing.Any]) -> gfwapiclient.resources.insights.models.request.VesselInsightBody
      :canonical: gfwapiclient.resources.insights.resources.InsightResource._prepare_get_vessel_insights_request_body

      .. autodoc2-docstring:: gfwapiclient.resources.insights.resources.InsightResource._prepare_get_vessel_insights_request_body
