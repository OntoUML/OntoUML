.. WholeOver

WholeOver anti-pattern
==================================

Full name
	Whole Composed of Overlapping Parts

Type
	Logical

Feature
	Part-Whole
	
Description
	A whole composed of two or more types whose extension possibly overlap. The sum of the meronymics’ upper bound cardinalities of the part end must be greater or equal to 2 or at least one of them be unlimited.
	
Justification
	This structure is usually too permissive. It is often the case that some of the part types should be disjoint or set as exclusive in the context of a single whole instance.
	
Contraints
	1.
		Let M be the set of identified meronymic relations, partEnd(m) the function that returns the association end connected to the part of a meronymic relation m, and upper(p) the function that return the upper bound cardinality of a property p, then:
		
		.. math :: (\sum_{m \in M}^{} upper(mediatedEnd(mn))) \geq 2
		
	2.
		Let O be the set of part types that compose Whole, then:
		
		.. math :: \exists x,y \in O \ | \ overlap(x,y)
		
Examples
	|Examples|

Refactoring Plans
	1.
		**[OCL] Exclusiveness*:** choose this option to forbid the same individual to play multiple roles w.r.t the same whole instance. Create an OCL invariant according to the following template:
		
			| *context Whole*
			| *inv: self.over1.oclAsType(Supertype)->asSet()->excludesAll(*
			| *self.over2.oclAsType(Agent)->asSet() and*
			| *self.over1.oclAsType(Supertype)->asSet()->excludesAll(*
			| *self.over3.oclAsType(Agent)->asSet() and*
			| *self.over2.oclAsType(Supertype)->asSet()->excludesAll(*
			| *self.over3.oclAsType(Agent)->asSet())*
		
	2.
		**[OCL] Partially exclusiveness**: choose this option to set a subset of the part types as exclusive.
		
	3.
		**[New/Mod] Disjoint parts:** Enforce part types to be disjoint through the creation or alteration of a disjoint generalization set.
		
		* *Note: to make all types exclusive, every binary combination should be explicitly ruled out*

**References:**

Prince Sales, Tiago. (2014). Ontology Validation for Managers.
		
.. |Examples| image:: examples.png