:py:mod:`gfwapiclient.resources.vessels.list.models.request`
============================================================

.. py:module:: gfwapiclient.resources.vessels.list.models.request

.. autodoc2-docstring:: gfwapiclient.resources.vessels.list.models.request
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`VesselListParams <gfwapiclient.resources.vessels.list.models.request.VesselListParams>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.models.request.VesselListParams
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.vessels.list.models.request.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.models.request.__all__
          :summary:
   * - :py:obj:`VESSEL_LIST_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE <gfwapiclient.resources.vessels.list.models.request.VESSEL_LIST_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.models.request.VESSEL_LIST_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.vessels.list.models.request.__all__
   :value: ['VesselListParams']

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.models.request.__all__

.. py:data:: VESSEL_LIST_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE
   :canonical: gfwapiclient.resources.vessels.list.models.request.VESSEL_LIST_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE
   :type: typing.Final[str]
   :value: 'Get vesselS by IDs request parameters validation failed.'

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.models.request.VESSEL_LIST_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE

.. py:class:: VesselListParams(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.vessels.list.models.request.VesselListParams

   Bases: :py:obj:`gfwapiclient.resources.vessels.base.models.request.VesselBaseDetailParams`

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.models.request.VesselListParams

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.models.request.VesselListParams.__init__

   .. py:attribute:: indexed_fields
      :canonical: gfwapiclient.resources.vessels.list.models.request.VesselListParams.indexed_fields
      :type: typing.ClassVar[typing.Optional[typing.List[str]]]
      :value: ['datasets', 'includes', 'match-fields', 'ids', 'vessel-groups']

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.models.request.VesselListParams.indexed_fields

   .. py:attribute:: datasets
      :canonical: gfwapiclient.resources.vessels.list.models.request.VesselListParams.datasets
      :type: typing.List[gfwapiclient.resources.vessels.base.models.request.VesselDataset]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.models.request.VesselListParams.datasets

   .. py:attribute:: ids
      :canonical: gfwapiclient.resources.vessels.list.models.request.VesselListParams.ids
      :type: typing.List[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.models.request.VesselListParams.ids

   .. py:attribute:: vessel_groups
      :canonical: gfwapiclient.resources.vessels.list.models.request.VesselListParams.vessel_groups
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.list.models.request.VesselListParams.vessel_groups
