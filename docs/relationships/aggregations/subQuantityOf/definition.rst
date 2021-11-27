Definition
----------

«:ref:`subQuantityOf`» is a parthood relation between two quantities, e.g.:

A. alcohol is part of wine;
B. plasma is part of blood;
C. sugar is part of ice cream.

:ref:`Quantities <quantity>` have not elements (or members). Since their members cannot be enumerated, they must be defined by a relation that unifies them into a connected whole (self-connectedness). Quantities are connected *topologically* (unlike e.g. collectives, which parts and members may not be placed together). *Topological connection* is characteristic for quantities and because of *topological connection,* sub-quantities cannot be shared among several super-quantities. For this reason, a subQuantityOf relation is always **non-sharable.** Since quantities do not have elements, they can be arbitrarily divided, like e.g. water. That´s why any quantity is defined to be *maximal portion* and can not be part of itself (water cannot be part of water). Since every part of a quantity is maximal (and self-connected), the SubQuantityOf parthood must have a **cardinality constraint of one and exactly one** in the sub-quantity side. E.g. since alcohol is a quantity (and, hence, maximal), there is exactly one quantity of alcohol which is part of a specific quantity of wine. Since quantity is *maximal,* it cannot have a quantity of the same kind as its part -- i.e. the «:ref:`subQuantityOf`» relation is **irreflexive**.

Nevertheless, a quantity can be part of another quantity (like glucose in wine) using the «:ref:`subQuantityOf`» relation. The change of any of parts of the quantity changes the identity of the whole (i.e. quantities are *extensional* entities). That is why **the strong supplementation axiom** holds for the the «:ref:`subQuantityOf`» relations (unlike «:ref:`subCollectionOf`» relation, which on contrary holds only weaker axiom). For the same reason, all parts of a quantity are **essential** and «:ref:`subQuantityOf`» relations are essential parthood relations. Further, since essential parthood relations are always transitive, «:ref:`subQuantityOf`» is always **transitive**.
