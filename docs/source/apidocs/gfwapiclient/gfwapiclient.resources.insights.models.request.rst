:py:mod:`gfwapiclient.resources.insights.models.request`
========================================================

.. py:module:: gfwapiclient.resources.insights.models.request

.. autodoc2-docstring:: gfwapiclient.resources.insights.models.request
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`VesselInsightInclude <gfwapiclient.resources.insights.models.request.VesselInsightInclude>`
     - .. autodoc2-docstring:: gfwapiclient.resources.insights.models.request.VesselInsightInclude
          :summary:
   * - :py:obj:`VesselInsightDatasetVessel <gfwapiclient.resources.insights.models.request.VesselInsightDatasetVessel>`
     - .. autodoc2-docstring:: gfwapiclient.resources.insights.models.request.VesselInsightDatasetVessel
          :summary:
   * - :py:obj:`VesselInsightBody <gfwapiclient.resources.insights.models.request.VesselInsightBody>`
     - .. autodoc2-docstring:: gfwapiclient.resources.insights.models.request.VesselInsightBody
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.insights.models.request.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.insights.models.request.__all__
          :summary:
   * - :py:obj:`VESSEL_INSIGHT_REQUEST_BODY_VALIDATION_ERROR_MESSAGE <gfwapiclient.resources.insights.models.request.VESSEL_INSIGHT_REQUEST_BODY_VALIDATION_ERROR_MESSAGE>`
     - .. autodoc2-docstring:: gfwapiclient.resources.insights.models.request.VESSEL_INSIGHT_REQUEST_BODY_VALIDATION_ERROR_MESSAGE
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.insights.models.request.__all__
   :value: ['VesselInsightBody', 'VesselInsightDatasetVessel', 'VesselInsightInclude']

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.request.__all__

.. py:data:: VESSEL_INSIGHT_REQUEST_BODY_VALIDATION_ERROR_MESSAGE
   :canonical: gfwapiclient.resources.insights.models.request.VESSEL_INSIGHT_REQUEST_BODY_VALIDATION_ERROR_MESSAGE
   :type: typing.Final[str]
   :value: 'Vessel insights request body validation failed.'

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.request.VESSEL_INSIGHT_REQUEST_BODY_VALIDATION_ERROR_MESSAGE

.. py:class:: VesselInsightInclude()
   :canonical: gfwapiclient.resources.insights.models.request.VesselInsightInclude

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.request.VesselInsightInclude

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.request.VesselInsightInclude.__init__

   .. py:attribute:: FISHING
      :canonical: gfwapiclient.resources.insights.models.request.VesselInsightInclude.FISHING
      :value: 'FISHING'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.request.VesselInsightInclude.FISHING

   .. py:attribute:: GAP
      :canonical: gfwapiclient.resources.insights.models.request.VesselInsightInclude.GAP
      :value: 'GAP'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.request.VesselInsightInclude.GAP

   .. py:attribute:: COVERAGE
      :canonical: gfwapiclient.resources.insights.models.request.VesselInsightInclude.COVERAGE
      :value: 'COVERAGE'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.request.VesselInsightInclude.COVERAGE

   .. py:attribute:: VESSEL_IDENTITY_IUU_VESSEL_LIST
      :canonical: gfwapiclient.resources.insights.models.request.VesselInsightInclude.VESSEL_IDENTITY_IUU_VESSEL_LIST
      :value: 'VESSEL-IDENTITY-IUU-VESSEL-LIST'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.request.VesselInsightInclude.VESSEL_IDENTITY_IUU_VESSEL_LIST

.. py:class:: VesselInsightDatasetVessel(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.insights.models.request.VesselInsightDatasetVessel

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.request.VesselInsightDatasetVessel

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.request.VesselInsightDatasetVessel.__init__

   .. py:attribute:: dataset_id
      :canonical: gfwapiclient.resources.insights.models.request.VesselInsightDatasetVessel.dataset_id
      :type: str
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.request.VesselInsightDatasetVessel.dataset_id

   .. py:attribute:: vessel_id
      :canonical: gfwapiclient.resources.insights.models.request.VesselInsightDatasetVessel.vessel_id
      :type: str
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.request.VesselInsightDatasetVessel.vessel_id

.. py:class:: VesselInsightBody(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.insights.models.request.VesselInsightBody

   Bases: :py:obj:`gfwapiclient.http.models.RequestBody`

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.request.VesselInsightBody

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.insights.models.request.VesselInsightBody.__init__

   .. py:attribute:: includes
      :canonical: gfwapiclient.resources.insights.models.request.VesselInsightBody.includes
      :type: typing.List[gfwapiclient.resources.insights.models.request.VesselInsightInclude]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.request.VesselInsightBody.includes

   .. py:attribute:: start_date
      :canonical: gfwapiclient.resources.insights.models.request.VesselInsightBody.start_date
      :type: datetime.date
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.request.VesselInsightBody.start_date

   .. py:attribute:: end_date
      :canonical: gfwapiclient.resources.insights.models.request.VesselInsightBody.end_date
      :type: datetime.date
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.request.VesselInsightBody.end_date

   .. py:attribute:: vessels
      :canonical: gfwapiclient.resources.insights.models.request.VesselInsightBody.vessels
      :type: typing.List[gfwapiclient.resources.insights.models.request.VesselInsightDatasetVessel]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.insights.models.request.VesselInsightBody.vessels
