.. _instantiation:

Instantiation
=============

«instantiation» connects instances of a base type to an instance of a higher-order type. Each link is the instantiation of the former in the latter.

An individual tree is connected to exactly one instance of Tree Species, such as Apricot or American Elm. General Sherman, a giant sequoia in Sequoia National Park, instantiates Giant Sequoia. An individual hazardous situation is connected to at least one instance of Hazardous Situation Type, such as Chemical Exposure Situation or Radiation Exposure Situation, and that set of instances includes Hazardous Situation itself when the higher-order type is a powertype.

.. figure:: /specification-figures/instantiation-example.svg
   :alt: Instantiation of trees in tree species and of hazardous situations in hazardous situation types
   :width: 100%
   :align: center

   Two uses of «instantiation».

Allowed ends
------------

- **Base-type end.** An OntoUML class.
- **Higher-order end.** A class whose instances are types. ``restrictedTo`` is exactly ``{type}``, and ``order`` is at least 2.

When the higher-order class is a Cardelli powertype (``isPowertype`` is true), the multiplicity on that end is ``1..*``.

Generalization sets
-------------------

UML generalization sets have an optional powertype: the classifier instantiated by the specific classifiers in the set. OntoUML restricts that classifier.

- It is an OntoUML class with ``restrictedTo`` exactly ``{type}``.
- ``isPowertype`` is false. A Cardelli powertype already classifies its base type and every specialization, so it is not used as the powertype of one generalization set.
- It is connected to the general classifier of the set by «instantiation», with the general classifier at the base-type end and the powertype at the higher-order end.

Tree Species, in the figure above, is that classifier for the specializations of Tree. The multiplicity on the higher-order end interacts with the ``{complete}`` and ``{disjoint}`` constraints of the generalization set:

.. list-table:: Multiplicity on the higher-order end, and what the generalization set tells you
   :header-rows: 1
   :widths: 16 21 21 21 21

   * - Multiplicity
     - overlapping, incomplete
     - overlapping, complete
     - disjoint, incomplete
     - disjoint, complete
   * - ``0..*``
     - silent
     - invalid
     - non-enumerated
     - invalid
   * - ``0..1``
     - invalid
     - invalid
     - silent
     - invalid
   * - ``1..*``
     - non-enumerated
     - silent
     - non-enumerated
     - non-enumerated
   * - ``1..1``
     - invalid
     - invalid
     - non-enumerated
     - enumerated

- **invalid** combinations are forbidden.
- **enumerated** means every instance of the higher-order type is included in the generalization set.
- **non-enumerated** means some instance of the higher-order type is absent from the generalization set.
- **silent** means the combination does not decide whether every instance is included.

A higher-order type **categorizes** its base type when every instance of the higher-order type is a proper specialization of the base type. It **partitions** the base type when every instance of the base type instantiates exactly one instance of the categorizer. It is the **powertype** of the base type, in the sense of :ref:`multilevel-theory`, when ``isPowertype`` is true and its instances are exactly the specializations of the base type, the base type included.
