.. _profile:

Profile architecture
====================

OntoUML is a UML profile for conceptual models drawn as class diagrams. It reuses UML metaclasses and extends selected elements with stereotypes, meta-properties, and well-formedness constraints. A stereotype refines how a UML element is interpreted. It does not change the underlying metaclass. A profiled model keeps its UML structure and makes its OntoUML commitments explicit.

The profile is organized in four areas:

- **Endurant modeling.** Class meta-properties, class stereotypes, and associations for endurants, their aspects, and their structural relations. See :ref:`class-stereotypes` and :ref:`relations`.
- **Event modeling.** Event types, historical roles, event relations, and temporal bounds. See :ref:`events`.
- **Situation modeling.** Situations and their relations to events and to the entities that are present in them. See :ref:`situations`.
- **Multi-level modeling.** Types that classify other types, including order and powertype semantics. See :ref:`multilevel`.

A user model may use UML packages to organize its vocabulary. Package membership does not, by itself, mean specialization, dependence, or parthood.

Reused UML elements
-------------------

Unless an OntoUML stereotype or constraint applies, each element below keeps its UML meaning.

**Class.**
   A type in the conceptual model. OntoUML stereotypes interpret it as a kind, a role, an event, a situation, a higher-order type, or another category from the profile. The meta-properties ``restrictedTo``, ``order``, and ``isPowertype`` add further information. See :ref:`metaproperties`. A class is not an individual of the domain. It classifies individuals or, in a multi-level model, other types.

**Generalization.**
   Specialization between a specific class and a more general class. Instances of the specific class are instances of the general class, subject to the stereotype constraints. Multiple generalization is allowed when those constraints are satisfied.

**Generalization set.**
   A group of generalizations that share a general classifier, with disjointness and completeness. OntoUML uses these properties for phase partitions and for the interaction between generalization sets and higher-order types.

**Association.**
   A relationship type among the types at its ends. OntoUML stereotypes interpret it as mediation, characterization, participation, parthood, triggering, instantiation, or another relation from the profile. The constraints fix the admissible end types and, where it matters, direction and multiplicity.

**Property.**
   An attribute of a class, or an end of an association. OntoUML property stereotypes include :ref:`addOnly` for a value that may be added and then kept, and :ref:`begin` and :ref:`end` for temporal bounds.

**Derivation.**
   A dependency that records that one element is derived from another. In OntoUML it documents that a :ref:`material` or :ref:`comparative` association follows from a truthmaker, such as a relator and its mediations, or qualities and a comparison of their values. The domain-specific derivation rule belongs to the model.

**Package.**
   A namespace for organizing model elements. A package boundary does not establish a domain relation.

**Comment.**
   Explanatory text attached to one or more elements. A comment can record assumptions or a relation whose full meaning is not in the diagram. It does not, by itself, add a machine-checkable constraint or change an element's ontological interpretation.

Outside the profile
-------------------

OntoUML specifies semantics and constraints for the class-modeling elements above. It does not define OntoUML semantics for operations, operation behavior, or the behavioral and interaction diagrams of UML. Event and situation constructs describe domain types and relations. They do not prescribe executable behavior, algorithms, workflows, or a runtime model.

The profile does not define a method for discovering or validating a domain model, and it does not standardize UFO. It also does not prescribe how a conceptual model is implemented as a software design, a database schema, or another ontology language, and it does not require a particular tool architecture. Tools such as :ref:`Tonto <tooling>` can check these constraints and offer transformations. Those tools are separate from the profile.
