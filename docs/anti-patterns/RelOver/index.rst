.. RelOver

RelOver anti-pattern
==================================

Full name
	Relator Mediating Overlapping Types

Type
	Logical

Feature
	Relator
	
Description
	A relator connected, through mediations, to two or more types whose extension possibly overlap. The sum of the mediations’ upper bound cardinalities of the mediated end must be greater than 2.
	
Justification
	Although OntoUML imposes no syntactical constraints on formal relations, it does not mean that modelers can use them at will, what is a very common practice.
	
Contraints
	1.
		Let M be the set of identified mediations, mediatedEnd(m) the function that returns the association end opposed to relator of a mediation m, and upper(p) the function that return the upper bound cardinality of a property p, then:
		
		.. math:: \sum_{}^{upper} (mediatedEnd(mn)) > 2
		
	2.
		Let O be the set of types mediated by Relator, then:
		
		.. math:: \exists x,y \in O \ | \ overlap(x,y)
		
Examples
	|Examples|

Refactoring Plans
	1.
		**[OCL] Exclusiveness** \*: choose this option to forbid the same individual to play multiple roles w.r.t the same relator instance. Create an OCL invariant according to the following template:
		
		| *context Relator*
		| *inv: self.over1.oclAsType(Supertype)->asSet()->excludesAll(*
		| *self.over2.oclAsType(Agent)->asSet() and*
		| *self.over1.oclAsType(Supertype)->asSet()->excludesAll(*
		| *self.over3.oclAsType(Agent)->asSet() and*
		| *self.over2.oclAsType(Supertype)->asSet()->excludesAll(*
		| *self.over3.oclAsType(Agent)->asSet())*
		
	2.
		**[OCL] Partially exclusiveness**: choose this option to forbid a subset of mediated types as exclusive.
		
	3.
		**[Mod/New] Disjoint mediated**: Enforce types to be disjoint through the creation or alteration of a disjoint generalization set.
		
		\* *Note: to make all types exclusive, every binary combination should be explicitly ruled out*

**References:**

Prince Sales, Tiago. (2014). Ontology Validation for Managers.
		
.. |Examples| image:: examples.png
