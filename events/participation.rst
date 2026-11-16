.. _participation:

Participation
=============

«participation» is an :ref:`existential dependence <dependency>` whose instances connect an event to an object. The event is a manifestation of an aspect inhering in the object, or it is composed of such manifestations.

Brutus participates in Caesar's assassination. A person participates in an act of composition while playing the role of composer. A soccer player, or a referee, participates in a soccer match.

.. figure:: /specification-figures/participation.svg
   :alt: A player and a referee participating in a soccer match
   :width: 80%
   :align: center

   Associations categorized as «participation».

Allowed ends
------------

- **Event end.** A class restricted exactly to ``{event}``.
- **Participant end.** A class of endurants. ``restrictedTo`` is a non-empty subset of the endurant natures.

The part of the event that depends exclusively on one participant is that participant's participational part. See :ref:`participational`. A :ref:`historicalRole` is connected to its event type by a participation whose event end has minimum cardinality one.
