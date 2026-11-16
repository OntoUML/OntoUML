.. _class-stereotypes:

Class stereotypes
=================

Every class in an OntoUML model has exactly one stereotype. For endurants, the stereotype says whether the class supplies identity, whether the classification is essential or accidental, and which ontological nature its instances have. The figure below is the endurant fragment of the profile. Event, situation, and higher-order class stereotypes are specified in :ref:`events`, :ref:`situations`, and :ref:`multilevel`.

.. figure:: /specification-figures/endurant-classes.svg
   :alt: Profile diagram of the endurant class stereotypes
   :width: 100%
   :align: center

   Endurant class stereotypes.

The summary below is the endurant portion of the stereotype table. "Order" is 1 for the first-order ultimate sortals. Subkinds, phases, roles, and the non-sortals may be used at any order, within the rules in :ref:`metaproperties`. Non-sortals are abstract classes.

.. list-table:: Endurant class stereotypes
   :header-rows: 1
   :widths: 18 14 22 46

   * - Stereotype
     - Rigidity
     - Sortality
     - ``restrictedTo``
   * - :ref:`kind`
     - rigid
     - ultimate sortal
     - exactly {functional complex}
   * - :ref:`collective`
     - rigid
     - ultimate sortal
     - exactly {collective}
   * - :ref:`quantity`
     - rigid
     - ultimate sortal
     - exactly {quantity}
   * - :ref:`relator`
     - rigid
     - ultimate sortal
     - exactly {relator}
   * - :ref:`intrinsicMode`
     - rigid
     - ultimate sortal
     - exactly {intrinsic mode}
   * - :ref:`extrinsicMode`
     - rigid
     - ultimate sortal
     - exactly {extrinsic mode}
   * - :ref:`quality`
     - rigid
     - ultimate sortal
     - exactly {quality}
   * - :ref:`subkind`
     - rigid
     - subordinate sortal
     - a single nature, derived from its parents
   * - :ref:`role`
     - anti-rigid
     - subordinate sortal
     - a single nature other than event or abstract
   * - :ref:`phase`
     - anti-rigid
     - subordinate sortal
     - a single nature other than event or abstract
   * - :ref:`category`
     - rigid
     - non-sortal
     - one or more natures
   * - :ref:`roleMixin <rolemixin>`
     - anti-rigid
     - non-sortal
     - one or more natures
   * - :ref:`phaseMixin <phasemixin>`
     - anti-rigid
     - non-sortal
     - one or more natures
   * - :ref:`mixin`
     - semi-rigid
     - non-sortal
     - one or more endurant natures

Earlier OntoUML used a single «mode» stereotype. The current profile separates :ref:`intrinsicMode` and :ref:`extrinsicMode`. The :ref:`mode` page keeps the earlier discussion and points at the two stereotypes.

.. toctree::
   :maxdepth: 1
   :caption: Classification:

   metaproperties
   taxonomy

.. toctree::
   :maxdepth: 1
   :caption: Sortals:

   sortals/kind/index
   sortals/subkind/index
   sortals/phase/index
   sortals/role/index
   sortals/collective/index
   sortals/quantity/index
   sortals/relator/index

.. toctree::
   :maxdepth: 1
   :caption: Non-sortals:

   nonsortals/category/index
   nonsortals/phasemixin/index
   nonsortals/rolemixin/index
   nonsortals/mixin/index

.. toctree::
   :maxdepth: 1
   :caption: Aspects:

   aspects/intrinsicMode/index
   aspects/extrinsicMode/index
   aspects/quality/index
   aspects/mode/index
