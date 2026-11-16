Definition
----------

A «:ref:`phase`» is an anti-rigid sortal that specializes a unique :ref:`ultimate sortal <ultimate-sortal>` and classifies entities contingently, in virtue of an intrinsic condition. Every instance of a given phase follows the same identity principle.

Phases are defined in partitions. The members of a partition are alternative intrinsic conditions for individuals of the same ultimate sortal. Child, Teenager, and Adult partition Person by age. Draft Contract, Active Contract, and Expired Contract partition Contract by lifecycle status. Endangered Species and Least Concern Species partition Species by conservation status.

.. figure:: /specification-figures/phase.svg
   :alt: Child, Adult, and Elder as phases of Person
   :width: 80%
   :align: center

   Classes categorized as «phase».

.. note::

   When you define a :ref:`phase partition <phase-partition-pattern>`, include the property whose variation moves instances between the phases. For Child, Adult, and Elder, that property is the age of Person.

A phase may specialize a kind, collective, quantity, relator, intrinsic mode, extrinsic mode, quality, situation, type, subkind, phase, category, mixin, or phase mixin. It may be specialized by a phase or a role.

A phase is declared in a partition: a disjoint and complete generalization set that contains at least two phases and no specializing class of another OntoUML stereotype.
