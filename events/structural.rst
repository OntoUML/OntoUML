.. _structural:

Structural parthood
===================

«structural» is a :ref:`parthood` relation between events. The part belongs to the very definition of the whole. It is a structure-dependent part.

A goal is a structural part of a soccer match. A soccer match is a structural part of a soccer championship. A test execution is a structural part of a testing process.

.. figure:: /specification-figures/structural.svg
   :alt: A goal as a structural part of a soccer match
   :width: 75%
   :align: center

   Associations categorized as «structural».

Both ends are classes restricted exactly to ``{event}``. A temporal segment of an event, carved out by an external time frame, uses :ref:`temporal` instead. The part that depends on a single participant uses :ref:`participational`.
