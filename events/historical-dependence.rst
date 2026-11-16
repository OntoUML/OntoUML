.. _historicalDependence:

Historical dependence
=====================

«historicalDependence» holds between two concrete individuals, a depender and a dependee, such that the depender could not have existed or occurred without the prior existence or occurrence of the dependee.

It can hold between endurants, between events, or between an endurant and an event. *bornIn* holds between a person and a place. *descendsFrom* holds between a descendant and an ancestor. *createdBy* holds between an artifact and its creator. *causedBy* holds between a goal and a kick, or between a birth and a conception.

:ref:`participation`, :ref:`creation`, and :ref:`termination` are specific historical dependences. Causation between events is grounded in chains of :ref:`bringingAbout` and :ref:`triggering`. See :ref:`relations-theory`.

.. figure:: /specification-figures/historical-dependence.svg
   :alt: Examples of historical dependence between people, places, and events
   :width: 100%
   :align: center

   Associations categorized as «historicalDependence».

Allowed ends
------------

Both the dependent end and the dependee end are classes of endurants or of events. ``restrictedTo`` is a non-empty subset of the endurant natures, or exactly ``{event}``.

Constraints
-----------

When the dependent end is restricted exactly to ``{event}``, the dependee end is restricted exactly to ``{event}`` as well. An event's historical dependence on another entity, in this stereotype, is a dependence on an event.
