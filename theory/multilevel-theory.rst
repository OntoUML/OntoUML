.. _multilevel-theory:
.. _types-as-endurants:

Types and multi-level theory
============================

Types as endurants
------------------

Types are not individuals, and they are endurants. Like individual endurants, they exist in time, can bear aspects and qualities, and can change while keeping their identity. The species Giant Panda changed its conservation status from endangered to vulnerable in 2016 and remained the same species. An aircraft model can have its maximum take-off weight revised and remain the same model.

The meta-properties of sortality and rigidity therefore apply to every endurant type, including types whose instances are themselves types. A type of types may be rigid or anti-rigid, sortal or non-sortal, and may stand in dependence relations.

Orders
------

Chains of instantiation stratify types into orders.

- **First-order types**, such as Lion and Wedding, classify individuals.
- **Second-order types**, such as Species and Event Type, classify first-order types.
- **Third-order types**, such as Taxonomic Rank, classify second-order types.

There is no upper bound. An **orderless type** classifies entities across orders. Discovered Item may classify the planet Mars, an individual, and the owl species *Strix butleri*, a first-order type. A type can specialize a type of its own order, or an orderless type.

High-order types are sometimes called clabjects, because they have characteristics of both types and instances. Lion can be an instance of Species and bear the binomial name *Panthera leo* and an estimated population of 25,000. Those are properties of the type Lion. They are not properties of a particular lion.

Categorizers and powertypes
---------------------------

A high-order type is related to the type whose instances it ultimately classifies, its **base type**, by two structural relations.

A high-order type **categorizes** a base type when every instance of the high-order type is a proper specialization of the base type. Every instance of Tree Species, such as Giant Sequoia, Apricot, and Sugar Maple, properly specializes Tree, so Tree Species categorizes Tree. A categorization **partitions** its base type when every instance of the base type instantiates exactly one instance of the categorizer. Tree Species partitions Tree when every tree belongs to exactly one species.

A high-order type is the **powertype** of a base type when its instances are exactly the specializations of the base type, the base type included. Vehicle Type is the powertype of Vehicle when it classifies Vehicle itself together with Car, Truck, and the other specializations.

Species is rigid: Lion could not cease to instantiate Species and remain the same species.

OntoUML represents ordered higher-order sortals with :ref:`type`, the instantiation link with :ref:`instantiation`, and the order and powertype flags as :ref:`meta-properties <metaproperties>`.
