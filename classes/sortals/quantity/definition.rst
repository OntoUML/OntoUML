Definition
----------

The «:ref:`quantity`» construct is used to represent :ref:`rigid <rigidity>` concepts
that provide an :ref:`identity principle <identity>` for their instances. A «:ref:`quantity`»
represent uncountable things, like Water, Clay, or Beer. It represents a
maximally topologically connected amount of matter. Quantities only have
other quantities as parts (see the «:ref:`subQuantityOf`» relation for more
details about members of collections). Here are some examples:

.. container:: figure

   |Quantity examples|

An easy way to decide whether a concept is a quantity or not, as
yourself this: if you physically divide an instance of 'x' in two parts,
are the resulting individuals two new instances of x? What if you divide
another 5 or 10 times? If the answer is always yes, 'x' is a Quantity.
To exemplify, let's think about an pile of sand. If you divide the pile
in two, you now have to new piles of sand, right? What if you do that
again for each remaining part? We would have 4 piles of sand.

.. container:: figure

   |Tannin heap|

As the other identity provider stereotypes («:ref:`kind`», «:ref:`collective`», «:ref:`relator`»
and «:ref:`mode`»), a Quality can be specialized by :ref:`subkinds <subkind>`, :ref:`phases <phase>` and :ref:`roles <role>`, as well as generalized by :ref:`mixins <mixin>` and :ref:`categories <category>`.

.. container:: figure

   |Quantity application 1|

Be careful not to confuse «:ref:`quantity`» and «:ref:`quality`».


.. |Quantity examples| image:: _images/ontouml_quantity-examples.png
.. |Tannin heap| image:: _images/Tannin_heap.jpeg
.. |Quantity application 1| image:: _images/ontouml_quantity-application-1.png
