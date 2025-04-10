:py:mod:`gfwapiclient.resources.vessels.detail.models.request`
==============================================================

.. py:module:: gfwapiclient.resources.vessels.detail.models.request

.. autodoc2-docstring:: gfwapiclient.resources.vessels.detail.models.request
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`VesselDetailParams <gfwapiclient.resources.vessels.detail.models.request.VesselDetailParams>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.detail.models.request.VesselDetailParams
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.vessels.detail.models.request.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.detail.models.request.__all__
          :summary:
   * - :py:obj:`VESSEL_DETAIL_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE <gfwapiclient.resources.vessels.detail.models.request.VESSEL_DETAIL_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.detail.models.request.VESSEL_DETAIL_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.vessels.detail.models.request.__all__
   :value: ['VesselDetailParams']

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.detail.models.request.__all__

.. py:data:: VESSEL_DETAIL_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE
   :canonical: gfwapiclient.resources.vessels.detail.models.request.VESSEL_DETAIL_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE
   :type: typing.Final[str]
   :value: 'Get vessel by ID request parameters validation failed.'

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.detail.models.request.VESSEL_DETAIL_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE

.. py:class:: VesselDetailParams(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.vessels.detail.models.request.VesselDetailParams

   Bases: :py:obj:`gfwapiclient.resources.vessels.base.models.request.VesselBaseDetailParams`

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.detail.models.request.VesselDetailParams

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.detail.models.request.VesselDetailParams.__init__

   .. py:attribute:: indexed_fields
      :canonical: gfwapiclient.resources.vessels.detail.models.request.VesselDetailParams.indexed_fields
      :type: typing.ClassVar[typing.Optional[typing.List[str]]]
      :value: ['includes', 'match-fields']

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.detail.models.request.VesselDetailParams.indexed_fields

   .. py:attribute:: dataset
      :canonical: gfwapiclient.resources.vessels.detail.models.request.VesselDetailParams.dataset
      :type: gfwapiclient.resources.vessels.base.models.request.VesselDataset
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.detail.models.request.VesselDetailParams.dataset
