Constraints
-----------

**C1:** A «Mixin» is always abstract. Note that abstract classes are
represented with *italic* labels.

.. container:: figure

   |Mixin application 2|

**C2:** A «Mixin» is a semi-rigid construct and because of that, it
cannot have as ancestor either a rigid or an anti-rigid type. Therefore,
only mixins can be ancestor of other mixins.

.. container:: figure

   |Mixin forbidden 1|


.. |Mixin application 2| image:: _images/ontouml_mixin-application-2.png
.. |Mixin forbidden 1| image:: _images/ontouml_mixin-forbidden-1.png
