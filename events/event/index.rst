.. _event:

Event
=====

.. stereotype:: meta.yml

Definition
----------

An «event» is a :ref:`first-order ultimate sortal <ultimate-sortal>` whose instances are events. They unfold in time by accumulating temporal parts, they are manifestations of aspects, and they exist once they have occurred.

Events are immutable. They cannot change, because they belong to the past. An apparent change is a variation across temporal parts. The philosophical literature also calls events perdurants or occurrents.

Soccer Match, Act of Composition, Presidential Election, Birth, and Death are events.

.. figure:: /specification-figures/event.svg
   :alt: Soccer match and birth as event types
   :width: 80%
   :align: center

   Classes categorized as «event».

An event may specialize a :ref:`category` or a :ref:`mixin`. It may be specialized by a :ref:`subkind`. Anti-rigid sortals cannot specialize a class whose instances are events, so roles and phases are not subtypes of an event. A contingent classification grounded in having participated in an event is a :ref:`historicalRole` of the participant, not a subtype of the event.

``restrictedTo`` is exactly ``{event}`` and ``order`` is 1.

Participants are connected by :ref:`participation`, :ref:`creation`, :ref:`termination`, or :ref:`change`. Parts of events use :ref:`structural`, :ref:`temporal`, or :ref:`participational`. The situations that trigger an event, and the situations an event brings about, are specified in :ref:`situations`.
