Definition
----------

«:ref:`membership <memberOf>`» is a :ref:`parthood` relation between a member and a collective. The member plays a uniform role with respect to the whole, indistinguishable from that of every other member. Membership is anti-transitive.

A tree is a member of a forest. A card is a member of a deck of cards. A lion is a member of a pack. A visitor is a member of a group of visitors.

.. figure:: /specification-figures/membership.svg
   :alt: Trees as members of a forest
   :width: 75%
   :align: center

   Associations categorized as «membership».

The member end is a class of substantials: ``restrictedTo`` is a non-empty subset of ``{functional complex, collective, quantity}``. The collection end is restricted exactly to ``{collective}``.

A member of a collective is also a member of any collective of which that collective is a :ref:`subCollection <subCollectionOf>`. Membership itself does not chain: members of a club that is a member of an association are not thereby members of the association.

The discussion below uses the earlier name «memberOf».

«:ref:`memberOf`» is a parthood relation between a substantial (as a part) and a «:ref:`collective`» (as a whole).

Examples include:

A. a tree is part of forest;
B. a card is part of a deck of cards;
C. a fork is part of cutlery set;
D. a club member is part of a club.

«:ref:`memberOf`» relation obeys *weak supplementation principle* (at least 2 parts are required, may be of different types). The memberOf relation is **intransitive.**

For example, Kazi, Bobek, Nemo and others are members of the *TJ Sokol Zizkov* Youth Tourist Club. The TJ Sokol Zizkov Youth Tourist Club is the member of the Association of the Youth Tourist Clubs. But Kazi, Bobek, Nemo and others are not members of the Association of the Youth Tourist Clubs, since not persons but only clubs may be members of the association. Although transitivity does not hold across two «:ref:`memberOf`» relations, a «:ref:`memberOf`» relation followed by «:ref:`subCollectionOf`» is transitive.
