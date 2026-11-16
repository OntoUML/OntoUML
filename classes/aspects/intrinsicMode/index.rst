.. _intrinsicMode:

Intrinsic mode
==============

.. stereotype:: meta.yml

Definition
----------

An «intrinsicMode» is a :ref:`first-order ultimate sortal <ultimate-sortal>` whose instances are aspects that inhere in a bearer, are not directly measurable in a quality structure, and do not existentially depend on any entity independent of that bearer.

Courage inheres in a person. Fragility inheres in a glass. A magnetic attraction disposition inheres in a magnet. Other examples are a capacity to program, a headache, and a belief that it will rain. See :ref:`endurants` for the distinction between intrinsic aspects, qualities, extrinsic modes, and relators.

.. figure:: /specification-figures/intrinsic-mode.svg
   :alt: Courage, fragility, and a magnetic disposition as intrinsic modes
   :width: 80%
   :align: center

   Classes categorized as «intrinsicMode».

An intrinsic mode may specialize a :ref:`category` or a :ref:`mixin`. It may be specialized by a :ref:`subkind`, :ref:`role`, :ref:`historicalRole`, or :ref:`phase`.

The connection to the bearer is a :ref:`characterization`. Because the aspect depends only on that bearer, it has no :ref:`externalDependence`.

Constraints
-----------

**Ontological nature.** ``restrictedTo`` is exactly ``{intrinsic mode}``, and ``order`` is 1.

**Identity.** An intrinsic mode supplies identity to its instances. It cannot specialize another sortal. Rigid sortals, including intrinsic modes, cannot specialize anti-rigid types. See :ref:`class-taxonomy`.

**Inherence.** Each instance inheres in exactly one bearer and cannot migrate to another. The characterized end of the characterization has multiplicity one.
