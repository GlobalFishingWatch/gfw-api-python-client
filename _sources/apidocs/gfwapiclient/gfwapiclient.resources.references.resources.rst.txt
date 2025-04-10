:py:mod:`gfwapiclient.resources.references.resources`
=====================================================

.. py:module:: gfwapiclient.resources.references.resources

.. autodoc2-docstring:: gfwapiclient.resources.references.resources
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`ReferenceResource <gfwapiclient.resources.references.resources.ReferenceResource>`
     - .. autodoc2-docstring:: gfwapiclient.resources.references.resources.ReferenceResource
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`__all__ <gfwapiclient.resources.references.resources.__all__>`
     - .. autodoc2-docstring:: gfwapiclient.resources.references.resources.__all__
          :summary:

API
~~~

.. py:data:: __all__
   :canonical: gfwapiclient.resources.references.resources.__all__
   :value: ['ReferenceResource']

   .. autodoc2-docstring:: gfwapiclient.resources.references.resources.__all__

.. py:class:: ReferenceResource(*, http_client: gfwapiclient.http.client.HTTPClient)
   :canonical: gfwapiclient.resources.references.resources.ReferenceResource

   Bases: :py:obj:`gfwapiclient.http.resources.BaseResource`

   .. autodoc2-docstring:: gfwapiclient.resources.references.resources.ReferenceResource

   .. rubric:: Initialization

   .. autodoc2-docstring:: gfwapiclient.resources.references.resources.ReferenceResource.__init__

   .. py:method:: get_eez_regions(**kwargs: typing.Dict[str, typing.Any]) -> gfwapiclient.resources.references.regions.models.EEZRegionResult
      :canonical: gfwapiclient.resources.references.resources.ReferenceResource.get_eez_regions
      :async:

      .. autodoc2-docstring:: gfwapiclient.resources.references.resources.ReferenceResource.get_eez_regions

   .. py:method:: get_mpa_regions(**kwargs: typing.Dict[str, typing.Any]) -> gfwapiclient.resources.references.regions.models.MPARegionResult
      :canonical: gfwapiclient.resources.references.resources.ReferenceResource.get_mpa_regions
      :async:

      .. autodoc2-docstring:: gfwapiclient.resources.references.resources.ReferenceResource.get_mpa_regions

   .. py:method:: get_rfmo_regions(**kwargs: typing.Dict[str, typing.Any]) -> gfwapiclient.resources.references.regions.models.RFMORegionResult
      :canonical: gfwapiclient.resources.references.resources.ReferenceResource.get_rfmo_regions
      :async:

      .. autodoc2-docstring:: gfwapiclient.resources.references.resources.ReferenceResource.get_rfmo_regions
