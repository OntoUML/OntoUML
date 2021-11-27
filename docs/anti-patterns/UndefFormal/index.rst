.. UndefFormal

UndefFormal anti-pattern
==================================

Full name
	Undefined Formal Association

Type
	Classification

Feature
	Formal
	
Description
	A «:ref:`formal`» association defined between types that do not own or inherit quality properties, i.e., attributes or associations whose types are data types.
	
Justification
	Although OntoUML imposes no syntactical constraints on formal relations, it does not mean that modelers can use them at will, what is a very common practice.
	
Contraints
	1.
		Let qualities(c) be the function that return all qualities defined for a class c (through attributes or relations) and ancestor(c) be the function that return all direct and indirect super types of a class c, then:
		
		.. math :: \#qualities(Source) = 0 \ \land \ \forall x \in ancestor(Source), \#qualities(x) = 0 \ \land \\
			\#qualities(Target) = 0 \ \land \ \forall x \in ancestor(Target), \#qualities(x) = 0
				
Examples
	|Examples|

Refactoring Plans
	1.
		**[New/Mod/OCL] Set as DCFR:** choose this plan if the formal relation really is a DCFR. The fix consists in specifying the data types to which the relation will be derived from, set the relation as derived, and specify the OCL derivation rule.
	2.
		**[Mod] Change stereotype:** this alternative should be taken if one reaches the conclusion that the relation is better qualified by another stereotype. It consists only in changing the stereotype of the relation.
		
		This solution is strongly discouraged if associations A and B related the same types.

**References:**

Prince Sales, Tiago. (2014). Ontology Validation for Managers.
		
.. |Examples| image:: examples.png