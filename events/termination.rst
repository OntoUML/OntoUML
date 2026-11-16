.. _termination:

Termination
===========

«termination» is a :ref:`participation` whose instances connect an event to an endurant that ceases to exist because of the event.

Under the historical semantics of this part of the profile, a terminated endurant is not removed from the universe of discourse. It ceases to exist in the present, and the event marks its passage into a phase that captures the post-termination state. A legislation repeal terminates a piece of legislation, which thereafter instantiates Repealed Piece of Legislation.

A divorce terminates a marriage. A death terminates a person.

.. figure:: /specification-figures/termination.svg
   :alt: A death terminating a person
   :width: 75%
   :align: center

   Associations categorized as «termination».

Allowed ends
------------

- **Event end.** A class restricted exactly to ``{event}``.
- **Terminated end.** A class of endurants. ``restrictedTo`` is a non-empty subset of the endurant natures.

The instant at which the endurant ceases to exist can be recorded with :ref:`end`. On an endurant that may still exist, that attribute is optional.
