.. _type:

Type
====

.. stereotype:: meta.yml

Definition
----------

A «type» is an ordered :ref:`ultimate sortal <ultimate-sortal>` whose instances are types. Car Model, Species, Contract Type, Hazardous Situation Type, and Meteorological Event Type are types in this sense.

A «type» has ``restrictedTo`` equal to ``{type}`` and a specific order greater than 1. Orderless sortals are not admitted under this stereotype. An orderless class, whose instances cross orders, is represented by another stereotype, such as a :ref:`category` or a :ref:`mixin`, with ``order`` set to ``*`` and ``type`` among its natures. See :ref:`metaproperties`.

A «type» may specialize a :ref:`category` or a :ref:`mixin`. It may be specialized by a :ref:`subkind`, :ref:`role`, :ref:`historicalRole`, or :ref:`phase`. Animal Species, in the endurant examples, is a subkind of Species. Protected Species is a role of Species. Endangered Species is a phase of Species.

When ``isPowertype`` is true, the extension of the higher-order type is its base type together with every specialization of that base type. Hazardous Situation Type then classifies Hazardous Situation itself and Chemical Exposure Situation, Radiation Exposure Situation, and the other specializations. A powertype has order greater than 1, or it is orderless. The base type is reached by an :ref:`instantiation` association.

.. figure:: /specification-figures/generalization-set-powertype.svg
   :alt: Tree species classifying sugar maple, apricot, American elm, and saguaro
   :width: 90%
   :align: center

   Tree Species classifying specializations of Tree. In OntoUML this higher-order type is connected to Tree by «instantiation», and it can be named as the powertype of the generalization set.
