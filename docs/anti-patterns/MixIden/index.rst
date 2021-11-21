.. MixIden

MixIden anti-pattern
==================================

Full name
	Mixin With Same Identity

Type
	Classification; Scope

Feature
	Hierarchy; Mixin
	
Description
	A non-sortal class specialized only by sortal types that follow the same identity principle (by inheriting it or supplying it).
	
Justification
	The common characteristic of all different types of mixin classes is the aggregation of individuals that follow different identity principles. The reason to analyze this anti-pattern is that a non-sortal should not be specified as a sortal or it may convey the wrong meaning.
	
Contraints
	1.
		For every Subtype-n, either one of the following holds: (i) Sortal-n = Identity Provider; or (ii) Identity Provider is an ancestor of Sortal-n
			
Examples
	|Examples|

Refactoring Plans
	1.
		**[Mod/New] Change Mixin to Sortal:** change the stereotype of Mixin to either subkind, role or phase and create a generalization from Mixin to Identity Provider.
		
	2.
		**[New] Add Sortal Subtypes:** add new or existing sortal sub-types to Mixin that do not follow the same identity principle of defined by Identity Provider.
	
**References:**

Prince Sales, Tiago. (2014). Ontology Validation for Managers.
	
.. |Examples| image:: examples.png