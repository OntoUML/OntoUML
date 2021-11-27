.. MixRig

MixRig anti-pattern
=======================================

Full name
	Mixin With Same Rigidity
	
Type
	Classification; Scope
	
Feature
	Hierarchy; Mixin
	
Description
	A class stereotyped as «:ref:`mixin`» specialized only by other classes that have the same rigidity property, i.e., are all rigid or all anti-rigid.
	
Justification
	As all non-sortals, mixins aggregated individuals that follow different identity principles. Its distinguishing characteristic, though, is that is semi-rigid, i.e., it behaves as a rigid type for some individuals as an anti-rigid for others. This anti-pattern analyzes mixins that, despite their capabilities, only generalize types with the same rigidity.
	
Contraints
	1.
		All sortals are rigid («:ref:`subkind`», «:ref:`kind`», «:ref:`quantity`», «:ref:`collective`» and «:ref:`category`») or all sortals are anti-rigid («:ref:`role`», «:ref:`phase`» or «:ref:`roleMixin`»)
	
Examples
	|Examples|

Refactoring Plans
	1.
		**[conditional] [Mod] Change mixin to category:** if all subtypes are rigid, and no anti-rigid subtype is expected to specialize «:ref:`mixin`», change the stereotype to «:ref:`category`».
	2.
		**[conditional] [Mod] Change mixin to roleMixin:** if all subtypes are anti-rigid, and no rigid subtype is expected to specialize «:ref:`mixin`», change the stereotype to «:ref:`roleMixin`».
	3.
		**[Mod] Change subtypes stereotypes:** this solution is a recognition that the semi-rigidity of «:ref:`mixin`» is correct and consists in changing the stereotype of one or more subtypes of «:ref:`mixin`» to properly characterize the semi-rigidity.
	4.	
		**[New/Mod] Add subtypes:** set new or existing types as direct children of «:ref:`mixin`» in order to properly characterize the semi-rigidity.

**References:**

Prince Sales, Tiago. (2014). Ontology Validation for Managers.
		
.. |Examples| image:: examples.png