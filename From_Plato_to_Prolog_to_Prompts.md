# From Plato to Prolog to Prompts: The 2,500-Year Journey to Artificial Reason

*Dagfinn D. Dybvig and Mistral Vibe*

## 1. Introduction: The Wheel Comes Full Circle

The preceding papers in this series traced a lineage from Fodor and Wittgenstein to Cassirer and Descartes, arguing that intelligence requires not a single innate Mentalese but an ecology of acquired symbolic forms. They concluded that modern artificial intelligence, to reach the threshold of systematic and exact reasoning, must combine the linguistic breadth of large language models with the formal constraint of theorem provers, code execution, and other symbolic systems. This was framed as a return to Enlightenment thinking — a mechanical realization of Descartes' *Geometry* joined to the contextual flexibility of his *Discourse*.

This essay extends that lineage backward in time and forward in specificity. It argues that the synthesis now emerging in neuro-symbolic AI is not merely a return to Descartes or even to Cassirer. It is the **computational realization of an insight that originates with Plato and Aristotle** — that structured representation and structured reasoning are the twin foundations of thought. The essay's central claim is that **Prolog, and the GOFAI tradition it exemplifies, was not a failed paradigm but an early instantiation of this ancient insight**, and that modern AI succeeds to the extent that it finally provides the missing interface between formal systems and the open world.

The argument proceeds in five steps. Section 2 returns to ancient Greece to establish the philosophical foundation: Plato's Forms and Aristotle's Logic as the origin of ontology and formal method. Section 3 revisits Descartes' *Geometry* as a domain-specific realization of this foundation for the problem of spatial extension. Section 4 examines Prolog as the computational instantiation of the Platonic-Aristotelian vision — a system that could reason with logic and constraints, implement ontologies, and power expert systems, but that lacked the means to connect its formal power to the messiness of the world. Section 5 shows how modern neuro-symbolic AI closes the circle: LLMs provide the interface (the Discourse) that Prolog lacked, while formal systems provide the structure (the Geometry) that LLMs lack. Section 6 concludes by situating this history as the gradual construction of a machine capable of participating in the symbolic forms that have defined human thought since antiquity.

## 2. Plato and Aristotle: The Origin of Ontology and Method

The philosophical tradition of the West begins with a dual insight that remains foundational. Plato, in his theory of Forms, proposed that the objects of true knowledge are not the flux of sensory appearance but the **eternal, unchanging structures** that underlie and constitute them. The Form of a circle is not this or that drawn figure, with its inevitable imperfections, but the ideal circle — the perfect, abstract structure that all particular circles instantiate. This is the origin of **ontology** as the study of what exists at the most fundamental level: not the things we perceive, but the categories and relations that structure reality.

Aristotle, Plato's student, added the complementary insight: that reasoning itself has a structure. In the *Prior Analytics*, he formalized the syllogism as a system of valid inference — the first **formal method** in Western thought. Where Plato gave us the *objects* of thought (the Forms), Aristotle gave us the *operations* of thought (the syllogisms). Together, they established the template: **intelligence consists in the manipulation of structured representations according to structured rules.**

This dual insight — ontology plus method — was not merely a philosophical position. It was a **cognitive technology**. It allowed the Greeks to do something unprecedented: to think systematically about domains as diverse as geometry, biology, ethics, and politics. The Platonic Academy and the Aristotelian Lyceum were not just schools of philosophy; they were the first **centers of systematic thought**, and their method was the first **language of thought** — not innate Mentalese, but a learned practice of representing and reasoning.

Crucially, this insight was **public and cultural**, not private and innate. The Forms and the syllogisms were not discoveries about the mind's hidden code. They were **inventions** — symbolic forms that, once internalized, reorganized what it was possible to think. A student who learned geometry was not merely acquiring information about triangles. They were learning to inhabit a symbolic form in which spatial relations could be represented and manipulated according to formal rules. The thought was not *in* the student; the thought was *in* the form, and the student learned to participate in it.

This is the template that all subsequent formal systems would follow. Plato and Aristotle did not solve the problem of intelligence. They **invented the category** — the idea that thought could be made systematic through structured representation and structured reasoning.

## 3. Descartes: From Forms to Functions

Two millennia after Plato and Aristotle, René Descartes made the next great leap. In *La Géométrie* (1637), he did not merely apply the Platonic-Aristotelian template to a new domain. He **transformed the template itself** by inventing a notation that made the domain of spatial extension formally operable.

Where Plato's Forms were static ideals and Aristotle's syllogisms were static rules, Descartes' coordinate system was **dynamic and generative**. By assigning numerical coordinates to geometric points and expressing curves as algebraic equations, he created a medium in which spatial problems could be transformed into syntactic operations. A circle was no longer a Form to be contemplated or a figure to be drawn. It was an equation — *x² + y² = r²* — that could be manipulated according to fixed rules to yield new truths.

This was the birth of **analytical geometry** as a symbolic form. It had all the hallmarks identified in the preceding papers:
- **Syntactic structure**: Equations had a recursive grammar.
- **Semantic compositionality**: The meaning of complex expressions was determined by their parts.
- **Inferential productivity**: New truths could be generated by mechanical manipulation.
- **Constitutiveness**: The objects of the form — functions, derivatives, integrals — were new objects, made thinkable only by the notation.

Descartes' achievement was to show that **a symbolic form could be productive** — that it could create operations through which new thoughts became constructible, thoughts that were not merely unexpressed but *unavailable* before the form existed. The derivative, as later developed, was not a pre-existing idea given clearer expression. It was a **new object** constituted by the notation of calculus, which itself depended on Descartes' coordinate system.

Yet Descartes' innovation was **domain-specific**. Analytical geometry made extension computable, but it did not address the broader problem of representing and reasoning about the world in all its diversity. For that, the Platonic-Aristotelian template would need to be instantiated more generally — and that would require a different kind of formal system.

## 4. Prolog: The Platonic-Aristotelian Vision in Code

That more general instantiation arrived in the 20th century, in the form of **Prolog** and the broader GOFAI tradition. If Plato and Aristotle invented the template of ontology plus method, and Descartes showed how to make a specific domain formally operable, then Prolog was the attempt to **make the template itself computational**.

Prolog, developed in the early 1970s by Alain Colmerauer and Philippe Roussel, was a logic programming language founded on **first-order logic**. It allowed programmers to define the world in terms of **facts** (ontology) and **rules** (method), and then query the system to derive new facts through logical inference. A simple Prolog program might assert that Socrates is a man, that all men are mortal, and then be queried to conclude that Socrates is mortal — a direct computational instantiation of Aristotle's syllogism.

But Prolog was far more powerful than this toy example suggests. It could:
- **Implement ontologies**: Represent complex domains with hierarchical categories and relations, much like Plato's Forms organized the world into structured kinds.
- **Reason with constraints**: Solve problems by satisfying logical conditions, a feature that made it ideal for planning and scheduling tasks.
- **Power expert systems**: Encode the knowledge of human experts in formal rules, allowing non-experts to query and reason within specialized domains.

In these respects, Prolog was **Descartes' *Geometry* generalized**. Where Descartes had made spatial extension formally operable, Prolog made **any domain** formally operable, provided it could be expressed in logical terms. A Prolog program was a **symbolic form** — a medium in which the objects of a domain could be constituted and manipulated according to formal rules.

### The Knowledge Acquisition Bottleneck

Yet Prolog, for all its elegance, faced a **fatal limitation** — one that Descartes had not confronted because his domain (geometry) was self-contained and mathematically precise. Prolog required that the world be **manually formalized** in its terms. Every fact, every rule, every category had to be explicitly encoded by a human knowledge engineer. This was the infamous **knowledge acquisition bottleneck**: the process of translating open-world knowledge into formal representations was slow, error-prone, and never complete.

The problem was not Prolog's reasoning engine, which was sound. The problem was the **interface** between the formal system and the world it was meant to represent. Prolog could reason flawlessly within its encoded ontology, but it had no way to **learn** new knowledge from experience, no way to **interpret** unstructured input, and no way to **adapt** to domains that resisted formalization.

This was the **Geometry without the Discourse** problem. Descartes had provided the Discourse (*Discourse on Method*) alongside the Geometry, but the Discourse was in natural language — a medium that Prolog could not understand. Prolog had the formal power to reason, but it lacked the linguistic power to connect that reasoning to the world.

### The Brittleness of Pure Formalism

The result was **brittleness**. Prolog-based expert systems worked beautifully within their narrow, carefully encoded domains. MYCIN could diagnose bacterial infections with accuracy rivaling human experts. DENDRAL could infer molecular structures from spectroscopic data. But these systems failed at the boundaries — when faced with information outside their encoded knowledge, with ambiguity, with uncertainty, or with the need to integrate multiple domains.

This was not a failure of Prolog as a formal system. It was a failure of the **paradigm** of pure formalism. Just as Descartes had discovered that natural language alone could not secure the kind of mechanical reasoning needed for geometry, the GOFAI tradition discovered that **formal systems alone could not connect to the open world**. Something was missing — the same something that Descartes had provided in natural language, but that Prolog could not access.

## 5. Modern AI: The Discourse Joins the Geometry

That missing piece is now here. Large language models, trained on vast corpora of natural language text, provide the **Discourse** that Prolog lacked. They can:
- **Interpret unstructured input**: Understand natural language queries, documents, and conversations.
- **Learn from experience**: Acquire knowledge from data, rather than requiring manual encoding.
- **Generate formal representations**: Translate open-world descriptions into formal structures that systems like Prolog can process.
- **Integrate multiple domains**: Connect insights across different areas of knowledge, something that pure formal systems struggle with.

But LLMs, as the preceding essays have argued, have their own limitation: **they can describe formal domains without submitting to their norms**. An LLM can produce proof-shaped text without producing valid proofs. It can describe physical laws without enforcing them. It hits an **asymptote** — improving with scale, but never fully achieving the reliability and necessity of formal reasoning.

The solution, as the essays have proposed, is the **loop**: the bidirectional connection between linguistic interpretation and formal constraint.

```
Interpret (LLM) → Formalize (LLM) → Derive (Formal System) → Verify (Formal System) → Reinterpret (LLM) → Revise (Loop)
```

In this architecture:
- The **LLM** acts as the **Discourse** — interpreting the world, formalizing problems, and reinterpreting results.
- The **formal system** (which could be a theorem prover, a Prolog engine, a physics simulator, or executable code) acts as the **Geometry** — deriving consequences, enforcing constraints, and verifying results.

### Prolog in the Loop

Where does Prolog fit in this modern synthesis? It fits **perfectly** — as one of the formal systems in the loop. Consider a modern neuro-symbolic system that uses Prolog as its reasoning engine:

1. **Interpret**: An LLM reads a natural language query about a complex domain (e.g., legal reasoning, medical diagnosis, or logistic planning).
2. **Formalize**: The LLM translates the query into a Prolog program — defining the relevant facts, rules, and constraints.
3. **Derive**: The Prolog engine performs logical inference, deriving new facts or identifying solutions that satisfy the constraints.
4. **Verify**: The Prolog engine checks the validity of the derivation within its formal framework.
5. **Reinterpret**: The LLM translates the formal results back into natural language, explaining the reasoning and any limitations.
6. **Revise**: If the results are unsatisfactory, the LLM refines the formalization and the loop continues.

In this setup, Prolog is no longer a standalone system trying to do everything. It is **the Geometry** in Descartes' architecture — the formal engine that does the mechanical reasoning. The LLM is **the Discourse** — the interface that connects the formal system to the world.

This is not a rejection of Prolog or of GOFAI. It is the **fulfillment** of what Prolog was always meant to be: a powerful reasoning engine, finally given the means to engage with the world.

## 6. Conclusion: The 2,500-Year Circle

The history of artificial intelligence is often told as a story of paradigms in conflict — symbolic AI vs. connectionist AI, logic vs. statistics, GOFAI vs. deep learning. This essay argues for a different narrative: **one of gradual convergence toward an ancient ideal**.

Plato and Aristotle discovered that intelligence requires **structured representation and structured reasoning**. Descartes showed how to make a specific domain (space) formally operable. Prolog and GOFAI implemented this insight computationally, but lacked the means to connect to the world. Modern neuro-symbolic AI finally provides that connection, combining the **Discourse** (LLMs) with the **Geometry** (formal systems).

In this light, Prolog was not wrong. It was not even just early. It was **a necessary stage** in the long development of artificial reason — the moment when the Platonic-Aristotelian vision was first made computational. The problem was never the formalism. The problem was the **interface**, and the interface is now here.

The circle is full. From Plato's Forms to Prolog's facts and rules to the prompts of modern LLMs, we have been building, step by step, the machinery of thought. The ancient insight was that thought requires structure. The modern insight is that **structure requires connection** — to the world, to language, to human meaning. Descartes had both in his two great works. Prolog had only one. Modern AI, at last, has both.

## References

Aristotle. *Prior Analytics*. Translated by Robin Smith. Indianapolis: Hackett, 1989. (Original work published c. 350 BCE.)

Bratko, Ivan. *Prolog Programming for Artificial Intelligence*. 4th ed. Addison-Wesley, 2001.

Colmerauer, Alain, and Philippe Roussel. "The Birth of Prolog." In *History of Programming Languages*, edited by Richard L. Wexelblat, 281–308. Academic Press, 1981.

Descartes, René. *The Geometry of René Descartes*. Translated by David Eugene Smith and Marcia L. Latham. New York: Dover Publications, 1954. (Original work published 1637.)

Dybvig, Dagfinn D. *Language(s) of Thought: A Wittgensteinian View of Fodor and the Gradually Increasing Capabilities of LLMs*. 2026a. [Preceding paper in this series.]

Dybvig, Dagfinn D. "Symbolic Forms and the Plural Mind: Cassirer beyond Fodor and Wittgenstein." 2026b. [Preceding paper in this series.]

Dybvig, Dagfinn D. "The Cartesian Moment: Analytical Geometry as Language of Thought." 2026c. [Preceding paper in this series.]

Dybvig, Dagfinn D. "Constitution and Rule-Change: Wittgenstein's Remarks, Cassirer's Forms, and the Asymptote of Language-Only Reasoning." 2026d. [Preceding paper in this series.]

Fodor, Jerry A. *The Language of Thought*. Cambridge, MA: Harvard University Press, 1975.

Kowalski, Robert. "Logic for Problem Solving." In *Information Processing*, edited by Donald Michie, 167–194. North-Holland, 1974.

Plato. *Phaedo*. Translated by G. M. A. Grube. Indianapolis: Hackett, 1977. (Original work published c. 360 BCE.)

Russell, Stuart, and Peter Norvig. *Artificial Intelligence: A Modern Approach*. 4th ed. Harlow: Pearson, 2021.

Shortliffe, Edward H. *Computer-Based Medical Consultations: MYCIN*. New York: Elsevier, 1976.

Wittgenstein, Ludwig. *Philosophical Investigations*. 4th ed. Translated by G. E. M. Anscombe, P. M. S. Hacker, and Joachim Schulte. Malden, MA: Wiley-Blackwell, 2009.
