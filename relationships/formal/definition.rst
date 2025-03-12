Definition
----------

The name «:ref:`formal`» is short for :ref:`Domain Comparative Formal Relation <relations>`. This construct is used to represent relations that can be reduced to the comparison of the quality values that characterize the related individuals, like heavier-than, younger-than or cheaper-than. Here are some examples in OntoUML:

.. container:: figure

   |Formal examples|

To specify how the relation can be reduced, use an OCL derivation rule:

::

   context Person::lighter : Set(Person)
   derive : Person.allInstances()->select(x | self.weight > x.weight)

*Tip*: Due to its ontological, the «:ref:`formal`» relations have no constraints in OntoUML. Nonetheless, make sure the relation you are modeling is indeed a comparative one. Think about how to reduce the relation to a comparison between values and represent the necessary properties.

.. |Formal examples| image:: _images/ontouml_formal-examples.png
