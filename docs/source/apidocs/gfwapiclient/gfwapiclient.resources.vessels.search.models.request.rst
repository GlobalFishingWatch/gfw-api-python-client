:py:mod:`gfwapiclient.resources.vessels.search.models.request`
==============================================================

.. py:module:: gfwapiclient.resources.vessels.search.models.request

.. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.request
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`VesselSearchInclude <gfwapiclient.resources.vessels.search.models.request.VesselSearchInclude>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.request.VesselSearchInclude
          :summary:
   * - :py:obj:`VesselSearchParams <gfwapiclient.resources.vessels.search.models.request.VesselSearchParams>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.request.VesselSearchParams
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.vessels.search.models.request.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.request.__all__
          :summary:
   * - :py:obj:`VESSEL_SEARCH_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE <gfwapiclient.resources.vessels.search.models.request.VESSEL_SEARCH_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE>`
     - .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.request.VESSEL_SEARCH_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.vessels.search.models.request.__all__
   :value: ['VesselSearchParams']

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.request.__all__

.. py:data:: VESSEL_SEARCH_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE
   :canonical: gfwapiclient.resources.vessels.search.models.request.VESSEL_SEARCH_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE
   :type: typing.Final[str]
   :value: 'Search vessels request parameters validation failed.'

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.request.VESSEL_SEARCH_REQUEST_PARAMS_VALIDATION_ERROR_MESSAGE

.. py:class:: VesselSearchInclude()
   :canonical: gfwapiclient.resources.vessels.search.models.request.VesselSearchInclude

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.request.VesselSearchInclude

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.request.VesselSearchInclude.__init__

   .. py:attribute:: OWNERSHIP
      :canonical: gfwapiclient.resources.vessels.search.models.request.VesselSearchInclude.OWNERSHIP
      :value: 'OWNERSHIP'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.request.VesselSearchInclude.OWNERSHIP

   .. py:attribute:: AUTHORIZATIONS
      :canonical: gfwapiclient.resources.vessels.search.models.request.VesselSearchInclude.AUTHORIZATIONS
      :value: 'AUTHORIZATIONS'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.request.VesselSearchInclude.AUTHORIZATIONS

   .. py:attribute:: MATCH_CRITERIA
      :canonical: gfwapiclient.resources.vessels.search.models.request.VesselSearchInclude.MATCH_CRITERIA
      :value: 'MATCH_CRITERIA'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.request.VesselSearchInclude.MATCH_CRITERIA

.. py:class:: VesselSearchParams(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.vessels.search.models.request.VesselSearchParams

   Bases: :py:obj:`gfwapiclient.resources.vessels.base.models.request.VesselBaseParams`

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.request.VesselSearchParams

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.request.VesselSearchParams.__init__

   .. py:attribute:: indexed_fields
      :canonical: gfwapiclient.resources.vessels.search.models.request.VesselSearchParams.indexed_fields
      :type: typing.ClassVar[typing.Optional[typing.List[str]]]
      :value: ['datasets', 'match-fields', 'includes']

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.request.VesselSearchParams.indexed_fields

   .. py:attribute:: since
      :canonical: gfwapiclient.resources.vessels.search.models.request.VesselSearchParams.since
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.request.VesselSearchParams.since

   .. py:attribute:: limit
      :canonical: gfwapiclient.resources.vessels.search.models.request.VesselSearchParams.limit
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.request.VesselSearchParams.limit

   .. py:attribute:: datasets
      :canonical: gfwapiclient.resources.vessels.search.models.request.VesselSearchParams.datasets
      :type: typing.List[gfwapiclient.resources.vessels.base.models.request.VesselDataset]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.request.VesselSearchParams.datasets

   .. py:attribute:: query
      :canonical: gfwapiclient.resources.vessels.search.models.request.VesselSearchParams.query
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.request.VesselSearchParams.query

   .. py:attribute:: where
      :canonical: gfwapiclient.resources.vessels.search.models.request.VesselSearchParams.where
      :type: typing.Optional[str]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.request.VesselSearchParams.where

   .. py:attribute:: includes
      :canonical: gfwapiclient.resources.vessels.search.models.request.VesselSearchParams.includes
      :type: typing.Optional[typing.List[gfwapiclient.resources.vessels.search.models.request.VesselSearchInclude]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.vessels.search.models.request.VesselSearchParams.includes
