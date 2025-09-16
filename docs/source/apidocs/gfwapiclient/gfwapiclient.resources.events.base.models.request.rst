:py:mod:`gfwapiclient.resources.events.base.models.request`
===========================================================

.. py:module:: gfwapiclient.resources.events.base.models.request

.. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`EventType <gfwapiclient.resources.events.base.models.request.EventType>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventType
          :summary:
   * - :py:obj:`EventConfidence <gfwapiclient.resources.events.base.models.request.EventConfidence>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventConfidence
          :summary:
   * - :py:obj:`EventEncounterType <gfwapiclient.resources.events.base.models.request.EventEncounterType>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventEncounterType
          :summary:
   * - :py:obj:`EventVesselType <gfwapiclient.resources.events.base.models.request.EventVesselType>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventVesselType
          :summary:
   * - :py:obj:`EventDataset <gfwapiclient.resources.events.base.models.request.EventDataset>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventDataset
          :summary:
   * - :py:obj:`EventGeometry <gfwapiclient.resources.events.base.models.request.EventGeometry>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventGeometry
          :summary:
   * - :py:obj:`EventRegion <gfwapiclient.resources.events.base.models.request.EventRegion>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventRegion
          :summary:
   * - :py:obj:`EventBaseBody <gfwapiclient.resources.events.base.models.request.EventBaseBody>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventBaseBody
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.events.base.models.request.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.events.base.models.request.__all__
   :value: ['EventBaseBody', 'EventConfidence', 'EventDataset', 'EventEncounterType', 'EventGeometry', 'EventRe...

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.__all__

.. py:class:: EventType()
   :canonical: gfwapiclient.resources.events.base.models.request.EventType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventType

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventType.__init__

   .. py:attribute:: ENCOUNTER
      :canonical: gfwapiclient.resources.events.base.models.request.EventType.ENCOUNTER
      :value: 'ENCOUNTER'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventType.ENCOUNTER

   .. py:attribute:: FISHING
      :canonical: gfwapiclient.resources.events.base.models.request.EventType.FISHING
      :value: 'FISHING'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventType.FISHING

   .. py:attribute:: GAP
      :canonical: gfwapiclient.resources.events.base.models.request.EventType.GAP
      :value: 'GAP'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventType.GAP

   .. py:attribute:: GAP_START
      :canonical: gfwapiclient.resources.events.base.models.request.EventType.GAP_START
      :value: 'GAP_START'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventType.GAP_START

   .. py:attribute:: LOITERING
      :canonical: gfwapiclient.resources.events.base.models.request.EventType.LOITERING
      :value: 'LOITERING'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventType.LOITERING

   .. py:attribute:: PORT
      :canonical: gfwapiclient.resources.events.base.models.request.EventType.PORT
      :value: 'PORT'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventType.PORT

   .. py:attribute:: PORT_VISIT
      :canonical: gfwapiclient.resources.events.base.models.request.EventType.PORT_VISIT
      :value: 'PORT_VISIT'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventType.PORT_VISIT

.. py:class:: EventConfidence()
   :canonical: gfwapiclient.resources.events.base.models.request.EventConfidence

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventConfidence

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventConfidence.__init__

   .. py:attribute:: LOW
      :canonical: gfwapiclient.resources.events.base.models.request.EventConfidence.LOW
      :value: '2'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventConfidence.LOW

   .. py:attribute:: MEDIUM
      :canonical: gfwapiclient.resources.events.base.models.request.EventConfidence.MEDIUM
      :value: '3'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventConfidence.MEDIUM

   .. py:attribute:: HIGH
      :canonical: gfwapiclient.resources.events.base.models.request.EventConfidence.HIGH
      :value: '4'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventConfidence.HIGH

.. py:class:: EventEncounterType()
   :canonical: gfwapiclient.resources.events.base.models.request.EventEncounterType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventEncounterType

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventEncounterType.__init__

   .. py:attribute:: CARRIER_FISHING
      :canonical: gfwapiclient.resources.events.base.models.request.EventEncounterType.CARRIER_FISHING
      :value: 'CARRIER-FISHING'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventEncounterType.CARRIER_FISHING

   .. py:attribute:: FISHING_CARRIER
      :canonical: gfwapiclient.resources.events.base.models.request.EventEncounterType.FISHING_CARRIER
      :value: 'FISHING-CARRIER'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventEncounterType.FISHING_CARRIER

   .. py:attribute:: FISHING_SUPPORT
      :canonical: gfwapiclient.resources.events.base.models.request.EventEncounterType.FISHING_SUPPORT
      :value: 'FISHING-SUPPORT'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventEncounterType.FISHING_SUPPORT

   .. py:attribute:: SUPPORT_FISHING
      :canonical: gfwapiclient.resources.events.base.models.request.EventEncounterType.SUPPORT_FISHING
      :value: 'SUPPORT-FISHING'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventEncounterType.SUPPORT_FISHING

   .. py:attribute:: FISHING_BUNKER
      :canonical: gfwapiclient.resources.events.base.models.request.EventEncounterType.FISHING_BUNKER
      :value: 'FISHING-BUNKER'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventEncounterType.FISHING_BUNKER

   .. py:attribute:: BUNKER_FISHING
      :canonical: gfwapiclient.resources.events.base.models.request.EventEncounterType.BUNKER_FISHING
      :value: 'BUNKER-FISHING'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventEncounterType.BUNKER_FISHING

   .. py:attribute:: FISHING_FISHING
      :canonical: gfwapiclient.resources.events.base.models.request.EventEncounterType.FISHING_FISHING
      :value: 'FISHING-FISHING'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventEncounterType.FISHING_FISHING

   .. py:attribute:: FISHING_TANKER
      :canonical: gfwapiclient.resources.events.base.models.request.EventEncounterType.FISHING_TANKER
      :value: 'FISHING-TANKER'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventEncounterType.FISHING_TANKER

   .. py:attribute:: TANKER_FISHING
      :canonical: gfwapiclient.resources.events.base.models.request.EventEncounterType.TANKER_FISHING
      :value: 'TANKER-FISHING'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventEncounterType.TANKER_FISHING

   .. py:attribute:: CARRIER_BUNKER
      :canonical: gfwapiclient.resources.events.base.models.request.EventEncounterType.CARRIER_BUNKER
      :value: 'CARRIER-BUNKER'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventEncounterType.CARRIER_BUNKER

   .. py:attribute:: BUNKER_CARRIER
      :canonical: gfwapiclient.resources.events.base.models.request.EventEncounterType.BUNKER_CARRIER
      :value: 'BUNKER-CARRIER'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventEncounterType.BUNKER_CARRIER

   .. py:attribute:: SUPPORT_BUNKER
      :canonical: gfwapiclient.resources.events.base.models.request.EventEncounterType.SUPPORT_BUNKER
      :value: 'SUPPORT-BUNKER'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventEncounterType.SUPPORT_BUNKER

   .. py:attribute:: BUNKER_SUPPORT
      :canonical: gfwapiclient.resources.events.base.models.request.EventEncounterType.BUNKER_SUPPORT
      :value: 'BUNKER-SUPPORT'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventEncounterType.BUNKER_SUPPORT

.. py:class:: EventVesselType()
   :canonical: gfwapiclient.resources.events.base.models.request.EventVesselType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventVesselType

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventVesselType.__init__

   .. py:attribute:: BUNKER
      :canonical: gfwapiclient.resources.events.base.models.request.EventVesselType.BUNKER
      :value: 'BUNKER'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventVesselType.BUNKER

   .. py:attribute:: CARGO
      :canonical: gfwapiclient.resources.events.base.models.request.EventVesselType.CARGO
      :value: 'CARGO'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventVesselType.CARGO

   .. py:attribute:: DISCREPANCY
      :canonical: gfwapiclient.resources.events.base.models.request.EventVesselType.DISCREPANCY
      :value: 'DISCREPANCY'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventVesselType.DISCREPANCY

   .. py:attribute:: CARRIER
      :canonical: gfwapiclient.resources.events.base.models.request.EventVesselType.CARRIER
      :value: 'CARRIER'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventVesselType.CARRIER

   .. py:attribute:: FISHING
      :canonical: gfwapiclient.resources.events.base.models.request.EventVesselType.FISHING
      :value: 'FISHING'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventVesselType.FISHING

   .. py:attribute:: GEAR
      :canonical: gfwapiclient.resources.events.base.models.request.EventVesselType.GEAR
      :value: 'GEAR'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventVesselType.GEAR

   .. py:attribute:: OTHER
      :canonical: gfwapiclient.resources.events.base.models.request.EventVesselType.OTHER
      :value: 'OTHER'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventVesselType.OTHER

   .. py:attribute:: PASSENGER
      :canonical: gfwapiclient.resources.events.base.models.request.EventVesselType.PASSENGER
      :value: 'PASSENGER'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventVesselType.PASSENGER

   .. py:attribute:: SEISMIC_VESSEL
      :canonical: gfwapiclient.resources.events.base.models.request.EventVesselType.SEISMIC_VESSEL
      :value: 'SEISMIC_VESSEL'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventVesselType.SEISMIC_VESSEL

   .. py:attribute:: SUPPORT
      :canonical: gfwapiclient.resources.events.base.models.request.EventVesselType.SUPPORT
      :value: 'SUPPORT'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventVesselType.SUPPORT

.. py:class:: EventDataset()
   :canonical: gfwapiclient.resources.events.base.models.request.EventDataset

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventDataset

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventDataset.__init__

   .. py:attribute:: ENCOUNTERS_EVENTS_LATEST
      :canonical: gfwapiclient.resources.events.base.models.request.EventDataset.ENCOUNTERS_EVENTS_LATEST
      :value: 'public-global-encounters-events:latest'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventDataset.ENCOUNTERS_EVENTS_LATEST

   .. py:attribute:: FISHING_EVENTS_LATEST
      :canonical: gfwapiclient.resources.events.base.models.request.EventDataset.FISHING_EVENTS_LATEST
      :value: 'public-global-fishing-events:latest'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventDataset.FISHING_EVENTS_LATEST

   .. py:attribute:: GAPS_EVENTS_LATEST
      :canonical: gfwapiclient.resources.events.base.models.request.EventDataset.GAPS_EVENTS_LATEST
      :value: 'public-global-gaps-events:latest'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventDataset.GAPS_EVENTS_LATEST

   .. py:attribute:: LOITERING_EVENTS_LATEST
      :canonical: gfwapiclient.resources.events.base.models.request.EventDataset.LOITERING_EVENTS_LATEST
      :value: 'public-global-loitering-events:latest'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventDataset.LOITERING_EVENTS_LATEST

   .. py:attribute:: PORT_VISITS_EVENTS_LATEST
      :canonical: gfwapiclient.resources.events.base.models.request.EventDataset.PORT_VISITS_EVENTS_LATEST
      :value: 'public-global-port-visits-events:latest'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventDataset.PORT_VISITS_EVENTS_LATEST

.. py:class:: EventGeometry(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.events.base.models.request.EventGeometry

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventGeometry

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventGeometry.__init__

   .. py:attribute:: type
      :canonical: gfwapiclient.resources.events.base.models.request.EventGeometry.type
      :type: str
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventGeometry.type

   .. py:attribute:: coordinates
      :canonical: gfwapiclient.resources.events.base.models.request.EventGeometry.coordinates
      :type: typing.Any
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventGeometry.coordinates

.. py:class:: EventRegion(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.events.base.models.request.EventRegion

   Bases: :py:obj:`gfwapiclient.base.models.BaseModel`

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventRegion

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventRegion.__init__

   .. py:attribute:: dataset
      :canonical: gfwapiclient.resources.events.base.models.request.EventRegion.dataset
      :type: str
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventRegion.dataset

   .. py:attribute:: id
      :canonical: gfwapiclient.resources.events.base.models.request.EventRegion.id
      :type: str
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventRegion.id

.. py:class:: EventBaseBody(/, **data: typing.Any)
   :canonical: gfwapiclient.resources.events.base.models.request.EventBaseBody

   Bases: :py:obj:`gfwapiclient.http.models.request.RequestBody`

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventBaseBody

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventBaseBody.__init__

   .. py:attribute:: datasets
      :canonical: gfwapiclient.resources.events.base.models.request.EventBaseBody.datasets
      :type: typing.List[gfwapiclient.resources.events.base.models.request.EventDataset]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventBaseBody.datasets

   .. py:attribute:: vessels
      :canonical: gfwapiclient.resources.events.base.models.request.EventBaseBody.vessels
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventBaseBody.vessels

   .. py:attribute:: types
      :canonical: gfwapiclient.resources.events.base.models.request.EventBaseBody.types
      :type: typing.Optional[typing.List[gfwapiclient.resources.events.base.models.request.EventType]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventBaseBody.types

   .. py:attribute:: start_date
      :canonical: gfwapiclient.resources.events.base.models.request.EventBaseBody.start_date
      :type: typing.Optional[datetime.date]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventBaseBody.start_date

   .. py:attribute:: end_date
      :canonical: gfwapiclient.resources.events.base.models.request.EventBaseBody.end_date
      :type: typing.Optional[datetime.date]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventBaseBody.end_date

   .. py:attribute:: confidences
      :canonical: gfwapiclient.resources.events.base.models.request.EventBaseBody.confidences
      :type: typing.Optional[typing.List[gfwapiclient.resources.events.base.models.request.EventConfidence]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventBaseBody.confidences

   .. py:attribute:: encounter_types
      :canonical: gfwapiclient.resources.events.base.models.request.EventBaseBody.encounter_types
      :type: typing.Optional[typing.List[gfwapiclient.resources.events.base.models.request.EventEncounterType]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventBaseBody.encounter_types

   .. py:attribute:: duration
      :canonical: gfwapiclient.resources.events.base.models.request.EventBaseBody.duration
      :type: typing.Optional[int]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventBaseBody.duration

   .. py:attribute:: vessel_groups
      :canonical: gfwapiclient.resources.events.base.models.request.EventBaseBody.vessel_groups
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventBaseBody.vessel_groups

   .. py:attribute:: flags
      :canonical: gfwapiclient.resources.events.base.models.request.EventBaseBody.flags
      :type: typing.Optional[typing.List[str]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventBaseBody.flags

   .. py:attribute:: geometry
      :canonical: gfwapiclient.resources.events.base.models.request.EventBaseBody.geometry
      :type: typing.Optional[gfwapiclient.resources.events.base.models.request.EventGeometry]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventBaseBody.geometry

   .. py:attribute:: region
      :canonical: gfwapiclient.resources.events.base.models.request.EventBaseBody.region
      :type: typing.Optional[gfwapiclient.resources.events.base.models.request.EventRegion]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventBaseBody.region

   .. py:attribute:: vessel_types
      :canonical: gfwapiclient.resources.events.base.models.request.EventBaseBody.vessel_types
      :type: typing.Optional[typing.List[gfwapiclient.resources.events.base.models.request.EventVesselType]]
      :value: 'Field(...)'

      .. autodoc2-docstring:: gfwapiclient.resources.events.base.models.request.EventBaseBody.vessel_types
