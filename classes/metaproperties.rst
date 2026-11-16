.. _metaproperties:

Class meta-properties
=====================

``OntoUMLClass`` is the supertype of the stereotypes in this profile. It defines three meta-properties. Most stereotypes restrict the values a modeler may assign.

.. _restrictedTo:

``restrictedTo``
----------------

``restrictedTo`` states which ontological natures the instances of the class may have: functional complexes, relators, modes, and so on. It matters most for non-sortals, whose instances can belong to different categories.

The natures are:

- ``functional complex``
- ``collective``
- ``quantity``
- ``relator``
- ``intrinsic mode``
- ``extrinsic mode``
- ``quality``
- ``event``
- ``situation``
- ``type``
- ``abstract``

Three named subsets are used throughout the association constraints:

- The **substantial natures** are ``{functional complex, collective, quantity}``.
- The **endurant natures** are the substantial natures plus ``{relator, intrinsic mode, extrinsic mode, quality, type}``.
- The **concrete individual natures** are the endurant natures plus ``{event, situation}``.

A sortal is restricted to a single nature. An ultimate sortal is restricted to exactly one nature, fixed by its stereotype. A class that does not include ``type`` among its natures has ``order`` 1 and ``isPowertype`` false.

``order``
---------

``order`` is the classification level of the class.

- ``1`` is a first-order class. Its instances are individuals. Person classifies Bob and Eva. Meeting classifies the meeting that occurred yesterday.
- ``2`` is a second-order class. Its instances are first-order types. Organization Type classifies Non-profit Organization and Governmental Organization.
- Higher integers continue the chain.
- ``*`` is an **orderless** class. Its instances are not confined to one level. Discovered Item classifies the planet Pluto and the owl species *Strix butleri*.

A class restricted only to types has order greater than 1, or is orderless. A class whose natures mix ``type`` with any other nature is orderless, and it is not a powertype. A class of order 1 does not include ``type``. A class of order greater than 1 is restricted to types. A class specializes a class of the same order, or an orderless class.

See :ref:`multilevel-theory` and :ref:`multilevel`.

``isPowertype``
---------------

``isPowertype`` records whether the class is a powertype in Cardelli's sense: its extension is its base type together with every direct and indirect specialization of that base type. Hazardous Situation Type, for example, classifies Hazardous Situation itself and Chemical Exposure Situation, Radiation Exposure Situation, and Vehicle Operation Under the Influence Situation.

A first-order class has ``isPowertype`` false. A class that mixes ``type`` with another nature also has ``isPowertype`` false. A powertype has order greater than 1, or is orderless. How the base type is represented, and how generalization sets interact with this flag, is specified in :ref:`instantiation`.
