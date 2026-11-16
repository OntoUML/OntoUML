.. _endurants:

Endurants
=========

An **individual endurant** is a concrete individual that is wholly present at every instant in which it exists. Endurants bear essential and accidental properties, so they can change qualitatively and remain the same individual. Frida Kahlo remains the same person when her weight or her address changes. The marriage of John and Mary remains the same marriage when its property regime changes. Which changes are possible is fixed by the kind the endurant instantiates.

Endurants divide into substantials and aspects, according to existential dependence.

Substantials
------------

A **substantial** does not depend on any other entity in order to exist. Examples include Mick Jagger, the Moon, the University of Twente, a deck of cards, and a puddle of water.

Substantials that have proper parts are wholes. The unity condition that binds the parts yields three categories, and OntoUML gives each its own ultimate sortal.

A **functional complex** is a substantial whose parts play differentiated functional roles. A human body, an organization, a computer, and a car are functional complexes: a car's engine generates power, its wheels enable movement, and its brakes support controlled deceleration. OntoUML represents the type of such wholes with :ref:`kind`. Parthood between functional complexes is :ref:`componenthood <componentOf>`.

A **collective** is a substantial whose parts play the same role with respect to the whole. A forest is unified by the co-location of its trees: every tree in the relevant region is one more member, on a par with the others. A deck of cards, a pile of bricks, and a group of visitors are collectives. OntoUML uses :ref:`collective`, :ref:`membership <memberOf>`, and :ref:`subCollection <subCollectionOf>`.

The same natural-language term can fall in either category, depending on the unity condition you mean. A band is a collective when its parts are uniformly band members. It is a functional complex when singer, guitarist, and drummer are distinct functions. A group of musicians can also :ref:`constitute <constitution>` a band: the group and the band then follow different identity principles.

A **quantity** is a maximally topologically self-connected portion of matter. A lump of clay, a pile of sand, and a portion of water are quantities. Quantities are homogeneous: their parts are portions of the same kind of matter. Splitting a lump of clay yields two smaller lumps of clay. Because a quantity is maximal, it cannot have another quantity of the same kind of matter as a part. The alcohol in a portion of wine is a quantity of a different kind, and a portion of water separated from a puddle is a new quantity. OntoUML uses :ref:`quantity` and :ref:`subQuantity <subQuantityOf>`.

Aspects
-------

An **aspect** is an endurant that existentially depends on another entity, its **bearer**, in which it **inheres**. The Moon's mass, Mick Jagger's ability to sing, John's love for Mary, and the marriage of John and Mary are aspects: none of them could exist without the entities they are about. An aspect inheres in exactly one bearer and cannot migrate, so Maria's body temperature cannot become Ana's.

In the philosophical literature, aspects are also called moments, tropes, abstract particulars, individual accidents, or particularized properties. Earlier UFO publications use "moment".

Substantials and aspects can both bear aspects. The intensity of a headache, the hue of a color, and the duration of an employment are aspects of aspects. Every chain of inherence is grounded in a bearer that is not itself an aspect.

An **intrinsic aspect** depends only on its bearer.

- A :ref:`quality` can be projected into a value space, called a **quality structure**, which is an abstract individual. Color, height, weight, temperature, and electrical charge are qualities. The color of a particular rose inheres in that rose and can change from red to brown while remaining the same quality. In OntoUML, quality structures are datatypes or enumerations.
- An :ref:`intrinsic mode <intrinsicMode>` cannot be projected directly into a quality structure. Fragility of a glass, the magnetic attraction of a magnet, a capacity to program, courage, a headache, and a belief are intrinsic modes.

An **extrinsic aspect** inheres in a bearer and also depends on at least one entity that is independent of that bearer, an entity that shares no parts with it.

- An :ref:`extrinsic mode <extrinsicMode>` inheres in a single bearer and is externally dependent on another entity. John's love for Mary, a commitment to meet for lunch, and an insurance claim are extrinsic modes. They are what make true a relational statement in which one entity bears a property directed at another, such as "John loves Mary". The dependence is an :ref:`externalDependence` association.
- A :ref:`relator` depends on two or more endurants, which it **mediates**. It is often an aggregate of extrinsic modes borne by those endurants. The marriage of John and Mary is composed of John's conjugal commitments and claims towards Mary and of Mary's towards John. Enrollments, employments, and presidential mandates are relators. They are what make true statements such as "John is married to Mary" or "Ana is employed by the University of Twente". The connection to each relatum is a :ref:`mediation`.

Both substantials and aspects are endurants, and so are types. See :ref:`types-as-endurants`.
