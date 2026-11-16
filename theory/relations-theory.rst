.. _relations-theory:

Relations
=========

Relations hold between two or more entities, their **relata**. The question that classifies them is truthmaking: what in the world makes a relational statement true? The entity responsible for the truth of "John is married to Mary" or "John is taller than Mary" is its **truthmaker**.

The profile's association stereotypes are specified in :ref:`relations`. This page is the theory those stereotypes realize.

Material and comparative relations
----------------------------------

**Material relations** hold in virtue of a relator that mediates the relata or, when only one relatum bears the connecting aspect, in virtue of an extrinsic mode. "John is married to Mary" is made true by their marriage. "Ana is employed by the University of Twente" is made true by her employment. "John loves Mary" is made true by John's love. The relata instantiate the relation when a suitable relator or extrinsic mode connecting them exists. OntoUML uses :ref:`material`, derived from a :ref:`relator` and its :ref:`mediations <mediation>`, or from an :ref:`extrinsicMode` connected by :ref:`characterization` and :ref:`externalDependence`.

**Comparative relations** hold in virtue of intrinsic qualities of the relata, with no mediating entity. "John is taller than Mary" is made true by John's height and Mary's height. The relata are not connected by a further individual: each can enter indefinitely many comparisons in virtue of how it intrinsically is. OntoUML uses :ref:`comparative`.

Dependence
----------

An entity **existentially depends** on another when it cannot exist unless the other exists. Inherence of an aspect in its bearer is existential dependence, and so is the dependence of a relator on the endurants it mediates, of an extrinsic mode on the entity it is directed at, and of an event on its participants.

**Specific dependence** holds towards one particular individual: Maria's body temperature depends on Maria, and John's love for Mary depends on Mary. **Generic dependence** holds towards some instance of a type, whichever it is: a car depends on having an engine, and the engine can be replaced while the car remains the same car. A legal person generically depends on some legal system.

An entity **historically depends** on another when its existence requires the other to exist or to have existed at some earlier time. Historical dependence does not require the depended-on entity to exist whenever the dependent one does. A widow historically depends on a marriage that no longer exists. A person historically depends on their birth. A glass of wine historically depends on the grapes it was made from. Historical dependence also holds between events along chains of triggering and bringing about: a goal scored from a penalty kick historically depends on that kick, and the kick on the foul that led to it.

Inherence, external dependence, and mediation are existential-dependence relations and hold directly between their relata. Relations derived from historical dependence have events as truthmakers: "Marie Curie was born in Warsaw" is made true by the event of her birth. OntoUML represents the general case with :ref:`historicalDependence`, and special cases with :ref:`participation`, :ref:`creation`, :ref:`termination`, and :ref:`change`.

Part-whole relations
--------------------

Parthood is a family of relations. They share irreflexivity, asymmetry, and weak supplementation. A proper part of a whole, a part distinct from the whole, cannot have that whole as one of its parts. A whole that has a proper part always has at least one other part disjoint from the first. That principle is **weak supplementation**.

Beyond that core, the relations differ. Some are transitive, so a part of a part is a part of the whole, and some are not. Parts can be essential to their wholes or exchangeable over time, as the engine of a car is. Events stand in part-whole relations as well, and because events are immutable their parts are essential to them.

Which relation applies depends on the categories of the relata. OntoUML separates :ref:`componenthood <componentOf>`, :ref:`membership <memberOf>`, :ref:`subCollection <subCollectionOf>`, and :ref:`subQuantity <subQuantityOf>` for endurants, and :ref:`structural`, :ref:`temporal`, and :ref:`participational` for events.

:ref:`Constitution <constitution>` is a different relation. It connects a concrete individual to another of the same broad category and of a different ultimate sortal, from which the constituted individual derives its basic properties. A lump of clay constitutes a statue, and a group of musicians constitutes a band. Constitution does not satisfy weak supplementation, so it is not parthood: a statue constituted by a single lump of clay has no further part disjoint from that lump. It is also distinct from identity. The lump survives reshaping, and the statue does not. The statue survives the loss of a minor piece and is then constituted by a different lump.
