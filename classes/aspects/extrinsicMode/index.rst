.. _extrinsicMode:

Extrinsic mode
==============

.. stereotype:: meta.yml

Definition
----------

An «extrinsicMode» is a :ref:`first-order ultimate sortal <ultimate-sortal>` whose instances are aspects that inhere in a bearer, are not directly measurable in a quality structure, and existentially depend on at least one entity independent of that bearer.

Love inheres in a person and depends on another person. An employment commitment inheres in an employee and depends on an employer. An insurance claim inheres in a policy holder and depends on an insurer. John's commitment towards Mary, and Maria's claim towards her insurer, are the same kind of aspect. See :ref:`endurants`.

.. figure:: /specification-figures/extrinsic-mode.svg
   :alt: Love, an employment commitment, and an insurance claim as extrinsic modes
   :width: 80%
   :align: center

   Classes categorized as «extrinsicMode».

An extrinsic mode may specialize a :ref:`category` or a :ref:`mixin`. It may be specialized by a :ref:`subkind`, :ref:`role`, :ref:`historicalRole`, or :ref:`phase`.

The inherence in the bearer is a :ref:`characterization`. The dependence on the external entity is an :ref:`externalDependence`. Together they are the usual truthmaker of a one-sided :ref:`material` relation, such as *trusts* or *loves*. A relation that depends on two or more independent endurants, such as marriage or employment, is a :ref:`relator` rather than a single extrinsic mode.

Constraints
-----------

**Ontological nature.** ``restrictedTo`` is exactly ``{extrinsic mode}``, and ``order`` is 1.

**Identity.** An extrinsic mode supplies identity to its instances. It cannot specialize another sortal. See :ref:`class-taxonomy`.

**Inherence and external dependence.** Each instance inheres in exactly one bearer. It also depends on at least one entity that shares no parts with that bearer.
