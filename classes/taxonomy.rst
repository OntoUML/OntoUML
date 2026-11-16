.. _ultimate-sortal:
.. _class-taxonomy:

Sortals, rigidity, and specialization
=====================================

Every class in an OntoUML model carries exactly one stereotype from this profile. The stereotype places the class in the taxonomy below. Cross-cutting meta-properties are defined in :ref:`metaproperties`.

Sortals and non-sortals
-----------------------

A **sortal** is a class whose instances carry a single identity principle. Person, Child, and Student are sortals. A sortal is restricted to a single ontological nature.

An **ultimate sortal** supplies that principle. Person, House, Car, Marriage, Weight, and Headache are ultimate sortals. An ultimate sortal is restricted to one ontological nature, and it cannot specialize another sortal. The figures below are rejected: Person specializing Organization, and Intention specializing Agreement and Status.

.. figure:: /specification-figures/ultimate-sortal-violation.svg
   :alt: Two models in which an ultimate sortal specializes another sortal
   :width: 85%
   :align: center

   Ultimate sortals specializing other sortals.

A **subordinate sortal** inherits its identity principle from exactly one ultimate sortal. The subordinate sortal stereotypes are :ref:`subkind`, :ref:`phase`, :ref:`role`, and :ref:`historicalRole`.

A **non-sortal** classifies entities whose identity principles come from different sortals. Physical Object, Agent, Customer, and Musical Artist are non-sortals. A non-sortal class is abstract. It cannot specialize a sortal. Somewhere in the model, a sortal specializes it, or a sortal and the non-sortal share a non-sortal supertype. The non-sortal stereotypes are :ref:`category`, :ref:`mixin`, :ref:`rolemixin`, :ref:`phasemixin`, and :ref:`historicalRoleMixin`.

Rigidity
--------

A **rigid sortal** classifies its instances in every possible circumstance in which they exist. Person, Car, Station Wagon, Tree, Oak, and Rental Contract are rigid sortals. A rigid sortal cannot specialize an anti-rigid sortal or an anti-rigid non-sortal. Person specializing Child, and Marriage specializing Legal Marriage, are rejected.

.. figure:: /specification-figures/rigid-sortal-violation.svg
   :alt: Two models in which a rigid sortal specializes an anti-rigid type
   :width: 85%
   :align: center

   Rigid sortals specializing anti-rigid types.

The rigid sortal stereotypes are the ultimate sortals :ref:`kind`, :ref:`collective`, :ref:`quantity`, :ref:`relator`, :ref:`intrinsicMode`, :ref:`extrinsicMode`, :ref:`quality`, :ref:`event`, :ref:`situation`, and :ref:`type`, together with the subordinate stereotype :ref:`subkind`. :ref:`category` is the rigid non-sortal.

An **anti-rigid sortal** classifies its instances contingently. Child, Employee, Healthy Dog, and Endangered Species are anti-rigid sortals. An anti-rigid sortal cannot specialize a class whose instances may be events or abstract individuals. Its ``restrictedTo`` value is derived from its parents. The anti-rigid sortal stereotypes are :ref:`role`, :ref:`phase`, and :ref:`historicalRole`.

An **anti-rigid non-sortal** classifies its instances contingently and does not carry a uniform identity principle. Living Animal, Infant Animal, and Customer are examples. It cannot specialize a class whose extension may include abstract individuals. The stereotypes are :ref:`rolemixin`, :ref:`phasemixin`, and :ref:`historicalRoleMixin`.

A **semi-rigid** non-sortal is essential for some of its instances and accidental for others. The stereotype is :ref:`mixin`. A mixin cannot specialize an anti-rigid type, and its ``restrictedTo`` value includes endurant natures.

First-order ultimate sortals
----------------------------

A **first-order ultimate sortal** is an ultimate sortal whose instances are individuals. Its ``order`` is 1. Kind, collective, quantity, relator, intrinsic mode, extrinsic mode, quality, event, and situation are first-order ultimate sortals. :ref:`type` is an ultimate sortal whose instances are types, so its order is greater than 1.

Specialization of natures
-------------------------

A class can be restricted only to ontological natures that its parents also allow. A subclass's ``restrictedTo`` set is a subset of each parent's set.

The same rule, read from the stereotypes, is what the "allowed supertypes" and "allowed subtypes" lines on each stereotype page record.
