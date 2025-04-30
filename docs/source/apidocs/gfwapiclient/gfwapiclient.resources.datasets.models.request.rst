:py:mod:`gfwapiclient.resources.datasets.models.request`
========================================================

.. py:module:: gfwapiclient.resources.datasets.models.request

.. autodoc2-docstring:: gfwapiclient.resources.datasets.models.request
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`SARFixedInfrastructureParams <gfwapiclient.resources.datasets.models.request.SARFixedInfrastructureParams>`
     - .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.request.SARFixedInfrastructureParams
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`SAR_FIXED_INFRASTRUCTURE_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE <gfwapiclient.resources.datasets.models.request.SAR_FIXED_INFRASTRUCTURE_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE>`
     - .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.request.SAR_FIXED_INFRASTRUCTURE_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE
          :summary:

API
~~~

.. py:data:: SAR_FIXED_INFRASTRUCTURE_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE
   :canonical: gfwapiclient.resources.datasets.models.request.SAR_FIXED_INFRASTRUCTURE_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE
   :type: typing.Final[str]
   :value: 'Get SAR fixed infrastructure request parameters validation failed.'

   .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.request.SAR_FIXED_INFRASTRUCTURE_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE

.. py:class:: SARFixedInfrastructureParams(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.datasets.models.request.SARFixedInfrastructureParams

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.request.SARFixedInfrastructureParams

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.request.SARFixedInfrastructureParams.__init__

   .. py:attribute:: z
      :canonical: gfwapiclient.resources.datasets.models.request.SARFixedInfrastructureParams.z
      :type: int
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.request.SARFixedInfrastructureParams.z

   .. py:attribute:: x
      :canonical: gfwapiclient.resources.datasets.models.request.SARFixedInfrastructureParams.x
      :type: int
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.request.SARFixedInfrastructureParams.x

   .. py:attribute:: y
      :canonical: gfwapiclient.resources.datasets.models.request.SARFixedInfrastructureParams.y
      :type: int
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.request.SARFixedInfrastructureParams.y

   .. py:attribute:: geometry
      :canonical: gfwapiclient.resources.datasets.models.request.SARFixedInfrastructureParams.geometry
      :type: typing.Optional[geojson_pydantic.geometries.Geometry]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.request.SARFixedInfrastructureParams.geometry

   .. py:method:: from_tile_or_geometry(*, z: typing.Optional[int] = None, x: typing.Optional[int] = None, y: typing.Optional[int] = None, geometry: typing.Optional[geojson_pydantic.geometries.Geometry] = None) -> typing.Self
      :canonical: gfwapiclient.resources.datasets.models.request.SARFixedInfrastructureParams.from_tile_or_geometry
      :classmethod:

      .. autodoc2-docstring:: gfwapiclient.resources.datasets.models.request.SARFixedInfrastructureParams.from_tile_or_geometry
