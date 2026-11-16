.. _multilevel:

Multi-level modeling
====================

Multi-level models include types that classify other types: Species, Dog Breed, Car Model, Organization Type. Those higher-order types capture properties of their instances. Lion can instantiate Species and bear the binomial name *Panthera leo* and an estimated population of 25,000. Those are properties of the type Lion. They are not properties of any particular lion. The theory is in :ref:`multilevel-theory`.

OntoUML represents this with the class meta-properties ``order`` and ``isPowertype`` (see :ref:`metaproperties`), the stereotype :ref:`type`, and the association :ref:`instantiation`.

.. figure:: /specification-figures/multilevel-classes.svg
   :alt: Profile diagram of the higher-order class stereotype
   :width: 70%
   :align: center

   Higher-order class stereotype.

.. figure:: /specification-figures/multilevel-associations.svg
   :alt: Profile diagram of the instantiation association
   :width: 40%
   :align: center

   Instantiation association.

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   type/index
   instantiation
