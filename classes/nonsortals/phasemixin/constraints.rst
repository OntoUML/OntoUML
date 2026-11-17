Constraints
-----------

.. _phasemixin-constraints-c1:
**C1:** A «:ref:`phasemixin`» is always abstract. Notice that abstract classes
are represented with an *italic* label.

.. _phasemixin-constraints-c2:
**C2:** A «:ref:`phasemixin`» aggregates individuals that follow :ref:`different identity principles <identity>`, therefore it may not have a sortal type as ancestor. «:ref:`kind`», «:ref:`quantity`», «:ref:`collective`», «:ref:`subkind`», «:ref:`role`», «:ref:`phase`», «:ref:`relator`», «:ref:`mode`», «:ref:`quality`» are all forbidden. 

.. _phasemixin-constraints-c3:
**C3:** A «:ref:`phasemixin`» is an :ref:`anti-rigid <rigidity>` construct, therefore it cannot have as descendent any :ref:`rigid <rigidity>` or :ref:`semi-rigid <rigidity>` type, as: «:ref:`Kind`», «:ref:`Quantity`», «:ref:`Collective`», «:ref:`Subkind`», «:ref:`Category`», «:ref:`Mixin`», «:ref:`Relator`», «:ref:`Mode`», «:ref:`Quality`».

.. _phasemixin-constraints-c4:
**C4:** A «:ref:`phasemixin`» should be solely dependent on intrinsic properties of its supertype, therefore it cannot have  :ref:`rolemixin <rolemixin>` as its supertype.
