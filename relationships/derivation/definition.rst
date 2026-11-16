Definition
----------

Derivation is the UML derivation dependency, reused by OntoUML. It records that a derived element follows from a truthmaker. It does not, by itself, state the domain rule. The model supplies that rule.

Two patterns are specified:

- A :ref:`material` association is derived from a :ref:`relator` and its :ref:`mediation` associations, or from an :ref:`extrinsicMode` with its :ref:`characterization` and :ref:`externalDependence`.
- A :ref:`comparative` association is derived from the qualities whose values are compared.

Deriving a material relation collapses the cardinality constraints of the paths through the relator. See the examples on the material page. Several material relations can be derived from a single relator.
