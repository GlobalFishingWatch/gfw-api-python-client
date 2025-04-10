:py:mod:`gfwapiclient.resources.fourwings.report.endpoints`
===========================================================

.. py:module:: gfwapiclient.resources.fourwings.report.endpoints

.. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.endpoints
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`FourWingsReportEndPoint <gfwapiclient.resources.fourwings.report.endpoints.FourWingsReportEndPoint>`
     - .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.endpoints.FourWingsReportEndPoint
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.fourwings.report.endpoints.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.endpoints.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.fourwings.report.endpoints.__all__
   :value: ['FourWingsReportEndPoint']

   .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.endpoints.__all__

.. py:class:: FourWingsReportEndPoint(*, request_params: gfwapiclient.resources.fourwings.report.models.request.FourWingsReportParams, request_body: gfwapiclient.resources.fourwings.report.models.request.FourWingsReportBody, http_client: gfwapiclient.http.client.HTTPClient)
   :canonical: gfwapiclient.resources.fourwings.report.endpoints.FourWingsReportEndPoint

   Bases: :py:obj:`gfwapiclient.http.endpoints.PostEndPoint`\ [\ :py:obj:`gfwapiclient.resources.fourwings.report.models.request.FourWingsReportParams`\ , :py:obj:`gfwapiclient.resources.fourwings.report.models.request.FourWingsReportBody`\ , :py:obj:`gfwapiclient.resources.fourwings.report.models.response.FourWingsReportItem`\ , :py:obj:`gfwapiclient.resources.fourwings.report.models.response.FourWingsReportResult`\ ]

   .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.endpoints.FourWingsReportEndPoint

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.endpoints.FourWingsReportEndPoint.__init__

   .. py:method:: _transform_response_data(*, body: typing.Union[typing.List[typing.Dict[str, typing.Any]], typing.Dict[str, typing.Any]]) -> typing.Union[typing.List[typing.Dict[str, typing.Any]], typing.Dict[str, typing.Any]]
      :canonical: gfwapiclient.resources.fourwings.report.endpoints.FourWingsReportEndPoint._transform_response_data

      .. autodoc2-docstring:: gfwapiclient.resources.fourwings.report.endpoints.FourWingsReportEndPoint._transform_response_data
