Constraints
-----------

.. _phasemixin-contraints-c1:
**C1:** A «:ref:`phasemixin`» is always abstract. Notice that abstract classes
are represented with an *italic* label.

.. _phasemixin-contraints-c2:
**C2:** A «:ref:`phasemixin`» aggregate individuals that follow :ref:`different identity principles <identity>`, therefore it may not have a sortal type as ancestor. «:ref:`kind`», «:ref:`collective`», «:ref:`quantity`», «:ref:`relator`», «:ref:`quality`», «:ref:`intrinsicMode`», «:ref:`extrinsicMode`», «:ref:`event`», «:ref:`situation`», «:ref:`type`», «:ref:`subkind`», «:ref:`role`», «:ref:`historicalRole`», and «:ref:`phase`» are all forbidden. 

.. _phasemixin-contraints-c3:
**C3:** A «:ref:`phasemixin`» is an :ref:`anti-rigid <rigidity>` construct, therefore it cannot have as descendant any :ref:`rigid <rigidity>` or :ref:`semi-rigid <rigidity>` type, such as «:ref:`kind`», «:ref:`collective`», «:ref:`quantity`», «:ref:`relator`», «:ref:`quality`», «:ref:`intrinsicMode`», «:ref:`extrinsicMode`», «:ref:`subkind`», «:ref:`category`», or «:ref:`mixin`».

.. _phasemixin-contraints-c4:
**C4:** A «:ref:`phasemixin`» should be solely dependant on intrinsic properties of its supertype, therefore it cannot have  :ref:`rolemixin <rolemixin>` as its supertype.
