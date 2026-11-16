.. _creation:

Creation
========

«creation» is a :ref:`participation` whose instances connect an event to an endurant that begins to exist because of the event.

A song is created in a music composition. A person is created by a birth. A book is created by a writing event.

.. figure:: /specification-figures/creation.svg
   :alt: A birth creating a person
   :width: 75%
   :align: center

   Associations categorized as «creation».

Allowed ends
------------

- **Event end.** A class restricted exactly to ``{event}``.
- **Created end.** A class of endurants. ``restrictedTo`` is a non-empty subset of the endurant natures.

The instant at which the created endurant begins to exist can be recorded with :ref:`begin`.
