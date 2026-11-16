.. _ontouml:

OntoUML
=======

**OntoUML** is an ontology-driven conceptual modeling language. It is defined as a profile of the OMG Unified Modeling Language (UML) for models expressed with class diagrams. The profile adds stereotypes, stereotype properties, and constraints so that a model can state ontological distinctions that UML leaves implicit: principles of identity, rigidity, existential dependence, part-whole relations, events, situations, and types that classify other types.

Conceptual models describe a domain, support communication among stakeholders, and provide a basis for analysis and system development. Their usefulness depends on how meaning is carried by the language's constructs. A general-purpose language offers a broad notation, and a diagram can be syntactically acceptable while hiding a distinction the domain needs, such as the difference between an object and a relationship, or between a type and its instances. Foundational ontologies supply domain-independent categories against which languages and models can be examined. UFO was developed for that purpose in conceptual modeling, and OntoUML is a language engineered from it.

Ontology-driven conceptual modeling uses an ontological theory to design, evaluate, and interpret conceptual models across domains. The categories of the theory appear as modeling constructs, and constraints derived from the theory limit which combinations are well-formed. The result is a model whose commitments are explicit.

Relationship with UFO
---------------------

:ref:`UFO <ufo>` is the theory. OntoUML is a UML realization of selected distinctions from that theory. The language began as an ontologically well-founded class-diagram fragment for structural conceptual modeling, reflecting UFO-A, the part of UFO concerned with endurants. It has since been extended, through continued research and application, to events, situations, and multi-level classification. OntoUML does not define UFO, and this documentation does not standardize UFO. UFO itself is the subject of ISO/IEC 21838-5. Using OntoUML means employing those distinctions to build a conceptual model of a domain.

In the language, the distinctions appear as stereotypes and constraints. A class stereotyped as a :ref:`kind <kind>` is an identity-providing type of functional complex. A class stereotyped as a :ref:`role <role>` classifies its instances contingently, in a relational context. The stereotypes are interpretations of UML elements, and they decide which models are well-formed.

Relationship with UML class diagrams
------------------------------------

OntoUML reuses UML classes, associations, properties, generalizations, generalization sets, derivations, packages, and comments. Unless an OntoUML stereotype or constraint applies, each element keeps its UML meaning. The profile does not replace the UML metaclasses.

A UML class diagram can show types and structural relationships without a foundational ontology for reading them. In OntoUML, the stereotype assigns the ontological category, and the constraints govern how categories may be related. An OntoUML class diagram describes the types and relations of a domain. It does not prescribe software classes. Implementation, database schemas, and transformations into other languages are later activities. See :ref:`profile` for the elements the profile reuses and for what it leaves out.

Modeling principles
-------------------

Conceptual models and object-oriented design models answer different questions. A conceptual model describes the structure of a domain. A design model describes software structures shaped by a particular implementation platform. The adequacy of a conceptual model is judged against the domain.

That is why OntoUML keeps abstraction mechanisms that a given programming language may support only partially: multiple inheritance, dynamic classification, and orthogonal generalization sets. A person may, at one time, be both an adult and a citizen. Those classifications can overlap, and an individual can move from one to another while remaining the same individual. A later transformation to a relational schema, or to code, has to account for multiple inheritance, overlapping and incomplete classifications, orthogonal hierarchies, and dynamic classification. The conceptual model keeps the domain distinctions. The realization strategy decides how they are represented in the target technology.

OntoUML also works as a pattern language. Its constructs recur in configurations whose structure and constraints express small ontological theories: orthogonal classifications, relators, phase partitions, powertypes, reified aspects, and non-sortal types. Those patterns support reuse and help a model absorb change. Recurrent structures that lead to unintended readings are collected as :ref:`anti-patterns <anti-patterns>`. :ref:`Tonto <tooling>` can insert several of these patterns and can report the anti-patterns as advisory checks.

The foundations of UFO and OntoUML go back to Giancarlo Guizzardi's Ph.D. thesis, `Ontological Foundations for Structural Conceptual Models`_. The language has been used in academic, corporate, and governmental settings, and theories underlying it have influenced other conceptual modeling languages, including ORM 2.0.

.. _Ontological Foundations for Structural Conceptual Models: https://www.researchgate.net/publication/215697579_Ontological_Foundations_for_Structural_Conceptual_Models
