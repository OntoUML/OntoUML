Definition
----------

A «:ref:`kind`» is a :ref:`first-order ultimate sortal <ultimate-sortal>` whose instances are mereologically simple substantials or functional complexes. A functional complex is an integral whole whose parts play differentiated functional roles. A car is a kind because its engine generates power, its wheels enable movement, its brakes support controlled deceleration, and its steering system controls direction. Person, Car, and Organization are typical kinds.

The stereotype name is short for *functional-complex kind*. Functional complexes are the most common kind of substantial in OntoUML models, so the language uses the short name. The same abbreviation drops the suffix "kind" from :ref:`collective`, :ref:`quantity`, :ref:`relator`, :ref:`intrinsicMode`, :ref:`extrinsicMode`, and :ref:`quality`. Those stereotypes classify types. A :ref:`category` named Functional Complex, by contrast, is a first-order type whose instances are the complexes themselves.

.. figure:: /specification-figures/kind.svg
   :alt: Person, Car, and Organization stereotyped as kind
   :width: 80%
   :align: center

   Classes categorized as «kind».

A kind may specialize a :ref:`category` or a :ref:`mixin`. It may be specialized by a :ref:`subkind`, :ref:`role`, :ref:`historicalRole`, or :ref:`phase`. Parts of a functional complex are related to it by :ref:`componenthood <componentOf>`.

``restrictedTo`` is exactly ``{functional complex}`` and ``order`` is 1.
