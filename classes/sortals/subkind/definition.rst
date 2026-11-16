Definition
----------

A «:ref:`subkind`» is a rigid sortal that specializes a unique :ref:`ultimate sortal <ultimate-sortal>` and inherits its identity principle. It does not supply a new identity principle, and classifying an instance as a subkind does not depend on a relation to something else.

Examples:

- Nonprofit Organization inherits its identity from the :ref:`kind` Organization.
- Insurance Contract inherits from the :ref:`relator` Contract.
- Teroldego Wine inherits from the :ref:`quantity` Wine.
- Chamber Choir inherits from the :ref:`collective` Choir.
- Cognitive Ability inherits from the :ref:`intrinsicMode` Ability.
- Football Match inherits from the :ref:`event` Match.
- Animal Species inherits from the :ref:`type` Species.

.. figure:: /specification-figures/subkind.svg
   :alt: Subkinds specializing kinds and other ultimate sortals
   :width: 100%
   :align: center

   Classes categorized as «subkind».

A subkind may specialize a kind, collective, quantity, relator, intrinsic mode, extrinsic mode, quality, event, situation, type, another subkind, a category, or a mixin. It may be specialized by a subkind, role, historical role, or phase.

``restrictedTo`` is derived from the parents, and it is a single ontological nature.
