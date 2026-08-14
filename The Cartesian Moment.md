# The Cartesian Moment: Analytical Geometry as Language of Thought

*Dagfinn D. Dybvig and Kimi 2.6*

## 1. Introduction: The Appendix That Outran Its Preface

The preceding papers in this series argued two related claims. *Language(s) of Thought* (Dybvig 2026a) proposed that intelligence is not underwritten by a single innate Mentalese but by an ecology of acquired formal languages — systems of notation that make certain thoughts possible for the first time. *Symbolic Forms and the Plural Mind* (Dybvig 2026b) situated that claim in Ernst Cassirer's philosophy: these languages are not merely tools for describing a pre-given reality but symbolic forms that constitute distinct ways of inhabiting the world. What remains to be shown is the historical genesis of the most powerful such form in the modern West — the specific moment when a new language of thought was invented, and how it immediately began thinking beyond its inventor.

That moment is the publication of René Descartes' *La Géométrie* in 1637. The essay that follows argues that analytical geometry was not merely a technical advance within mathematics but the creation of a new symbolic form — one that made spatial extension formally tractable for the first time, unlocked the subsequent development of calculus and mathematical physics, and thereby furnished the conceptual infrastructure of the scientific Enlightenment and the industrial-technological civilization that followed. The argument has a paradoxical core. Descartes is remembered, above all, for a sentence in natural language: *cogito, ergo sum*. But the work that transformed European civilization was written in a notation that made the *res extensa* — the very domain from which the thinking subject had been distinguished — amenable to mechanical manipulation. Descartes proved the existence of the thinking self; what he actually created was a way of thinking about the world that made the self optional.

The structure of the argument is as follows. Section 2 reconstructs the relation between the *Discourse on Method* and the *Geometry* as one of misaligned priority: the preface announces a method for securing certainty in the thinking subject, while the appendix constructs the symbolic machinery that makes the extended world computable. Section 3 analyses analytical geometry as a language of thought in the technical sense developed in the preceding papers: a syntactically structured, recursively productive medium that constitutes its objects rather than merely describing them. Section 4 traces the unlocking sequence — from coordinates to calculus to analytical mechanics — showing how the new symbolic form generated insights inaccessible to natural language, including the mechanical conceptions of momentum that Descartes himself glimpsed but could not fully articulate. Section 5 draws the consequence for artificial intelligence: if the founder of modern philosophy needed a formal language to think mechanically, then a machine trained only on natural language cannot reach the Enlightenment threshold of systematic, exact, computable thought. Section 6 concludes.

## 2. The Discourse and the Geometry: A Reversal of Priority

In 1637 Descartes published three essays — *Optics*, *Meteorology*, and *Geometry* — preceded by a preface, the *Discourse on the Method of Rightly Conducting One's Reason and of Seeking Truth in the Sciences*. The *Discourse* is the text by which Descartes is known to the general educated public. It announces the project of radical doubt, the certainty of the *cogito*, the criterion of clear and distinct ideas, and the provisional morality that would govern the reconstruction of knowledge. It is written in French, not Latin, and in the first person, as an intellectual autobiography. Its tone is confiding, its structure narrative, its medium unmistakably natural language.

The *Geometry* is appended to the *Discourse* as an illustration of the method in practice. It is written in a terse, technical prose closer to the algebraic notation it introduces than to the meditative voice of the preface. Where the *Discourse* moves from doubt to certainty, the *Geometry* moves from problem to solution. Where the *Discourse* seeks the foundations of knowledge in the self-transparent thinking subject, the *Geometry* constructs a notation in which spatial relations are expressed as equations and manipulated by syntactic rules that require no reference to the subject at all.

The standard reception treats the *Discourse* as the philosophical core and the *Geometry* as a mathematical application. This is the same interpretive inversion that the first essay in this series diagnosed in Turing: the famous part is taken as the working part, and the working part is treated as an appendix. But the historical record suggests a different relation. The *Geometry* was not an illustration of the method; it was the method's most consequential product — and a product that outran its author's intentions.

Descartes' four rules of method, as stated in Part Two of the *Discourse*, are:

1. Never accept anything as true that is not known evidently to be so.
2. Divide difficulties into as many parts as possible.
3. Conduct thoughts in order, beginning with the simplest objects.
4. Make enumerations so complete and reviews so general that nothing is omitted.

These rules are procedural advice for the individual thinker. They presuppose a subject who can survey the field of knowledge, distinguish the simple from the complex, and conduct a stepwise review. They operate in the medium of natural language and introspective attention. What they do not provide is a notation — a system of symbols with internal combinatorial structure that can generate new truths mechanically, without renewed acts of intuition.

Descartes himself was aware of this point, and he framed his method explicitly against the Aristotelian syllogism. In the *Discourse* and in the *Rules for the Direction of the Mind*, he complains that syllogistic logic is useful only for organizing truths already known, not for discovering new ones. "As to logic," he writes, "its syllogisms and the majority of its other precepts are of more use for explaining to others the things one knows . . . than for learning what is new" (Descartes 1985, 119). The method he sought was one that would be genuinely productive — that would extend knowledge rather than merely arrange it.

He was right about the problem and right about the aspiration. But he mislocated the solution. He believed that a sufficiently disciplined natural-language method, operating on "clear and distinct ideas" in the mind of the individual thinker, would achieve what syllogisms could not. What he did not foresee was that the genuine productivity would come not from the thinker's method but from the notation itself. The *Geometry* provides exactly that. By assigning numerical coordinates to geometric points and expressing curves as algebraic equations, Descartes created a medium in which spatial problems could be transformed into syntactic operations. A circle is no longer a figure to be contemplated; it is the equation *x² + y² = r²*. A line is no longer drawn; it is the equation *y = mx + b*. The properties of these objects — their intersections, their tangents, their areas — can be derived by manipulating the symbols according to fixed rules. The thinking subject is no longer the engine of discovery; the notation is.

This is not to say that the *Discourse* is without philosophical importance. The radical doubt, the *cogito*, and the criterion of clarity and distinctness are genuine achievements of philosophical analysis. But they are achievements in natural language, addressed to the problem of epistemic certainty. The *Geometry* addresses a different problem: the problem of making the extended world formally operable. And it was the *Geometry*, not the *Discourse*, that furnished the symbolic form in which the scientific Enlightenment would construct its world.

## 3. Analytical Geometry as Language of Thought

The preceding papers developed a framework for understanding formal systems as acquired languages of thought. Fodor (1975) was right to insist that cognition requires systematic, recombinable, and inferentially consequential structure. He was less persuasive in treating such structure as substantially innate. The Wittgensteinian alternative, developed in *Language(s) of Thought*, is that these structures are acquired through public practice and internalized as media of thought. Cassirer, as discussed in *Symbolic Forms and the Plural Mind*, added the crucial claim that such media do not merely express pre-structured contents but constitute the objects of which they speak.

Analytical geometry is a paradigm case. Before Descartes, European mathematics possessed two distinct symbolic forms: the geometric and the algebraic. Geometry operated with diagrams, constructions, and proportions. Its objects were spatial figures — lines, circles, conic sections — and its method was visual and constructive. You proved a theorem by drawing a figure, adding auxiliary lines, and appealing to the evident properties of the resulting configuration. Algebra, by contrast, operated with symbols — letters for unknowns, signs for operations — and its method was syntactic and sequential. You solved an equation by manipulating symbols according to fixed rules, without reference to spatial intuition.

These were not merely different notations for the same domain. They were different symbolic forms, with different constitutive logics. Geometry constituted a world of spatial relations accessible to visual intuition. Algebra constituted a world of quantitative relations accessible to symbolic manipulation. Each had its own norms of validity, its own criteria of completion, its own conception of what it meant to solve a problem.

Descartes' achievement was to create a symbolic mediation between these two forms — or, more precisely, to subordinate the geometric to the algebraic. By introducing coordinates, he made it possible to express any geometric object as an algebraic equation and to derive geometric properties by algebraic manipulation. The point *(a, b)* is not a diagram but a pair of numbers. The curve is not a figure but a relation between variables. The tangent is not a line drawn to touch the curve but the derivative of the function — a symbolic operation that yields a new equation.

This is the creation of a new language of thought in the strict sense. It is:

- **Syntactically structured**: Equations have a recursive grammar. Complex expressions are built from simple ones by fixed rules.
- **Semantically compositional**: The meaning of a complex expression is determined by the meanings of its parts and their mode of combination.
- **Inferentially productive**: New truths can be generated by mechanical manipulation of the symbols, without renewed acts of intuition.
- **Constitutive**: The objects of the new form — functions, derivatives, integrals — are not abbreviations of thoughts available in ordinary language or in classical geometry. They are new objects, made thinkable only by the notation.

Consider the concept of a function. In classical geometry, there is no function. There are curves, generated by motion or by geometric construction. The idea that a curve is the graph of a rule assigning to each *x* a unique *y* — that it is a *function* — is not available until the coordinate system makes it possible to think of the two variables as linked by an equation. The function is not discovered; it is constituted by the symbolic form. Similarly, the derivative is not a slope intuited from a diagram; it is a limit of difference quotients, expressible only in the algebraic notation that analytical geometry provides.

This transformation is anticipated in Cassirer's earlier *Substance and Function* (1910), where he argues that the history of exact science is the progressive replacement of the concept of substance by the concept of function. The substantialist view treats objects as bearers of fixed properties; the functional view treats them as nodes in a network of relations governed by laws. Analytical geometry is the paradigm case of this transition. The curve as substance — a figure with a definite shape — is replaced by the curve as function — a rule that generates coordinates. The point is no longer a location in space but an ordered pair; the tangent is no longer a line that touches but a differential operator. Descartes did not merely add a new tool to mathematics; he initiated the functionalization of spatial reality that Cassirer identified as the defining move of modern scientific thought.

Cassirer's framework is indispensable here. The scientific concept, as Cassirer described it, is a symbolic form that constitutes reality through lawful necessity, exact measurement, and formal deduction. Analytical geometry is the birth-moment of that form for the domain of space. Before Descartes, spatial relations were governed by the geometric symbolic form: visual, constructive, intuitive. After Descartes, they could be governed by the algebraic form: linear, rule-governed, computable. The world of extension became, for the first time, a world of functions.

## 4. The Unlocking Sequence: From Coordinates to Calculus to Mechanics

The creation of a new symbolic form is not a static achievement. It initiates a developmental sequence in which the form generates new problems, new concepts, and new forms beyond itself. The preceding papers emphasized that symbolic forms are not merely additive but transformative: each new form reorganizes the possibilities of the previous ones. The history of mathematics after Descartes is a textbook case.

**Calculus.** Newton and Leibniz are the names associated with the invention of calculus, but both stood explicitly on Descartes' coordinates. The derivative and the integral are operations defined on functions, and functions are thinkable only in the coordinate framework. The problem of the tangent — solved by Fermat and Descartes with algebraic methods — becomes, in the hands of Leibniz, the problem of the differential ratio *dy/dx*. The problem of the area under a curve — solved by exhaustion in classical geometry — becomes the problem of the integral, the inverse of differentiation.

What is crucial is that these new concepts are not merely new techniques within an existing form. They constitute a new symbolic form — the differential calculus — which transforms what analytical geometry made possible. The equation *y = f(x)* becomes *dy = f'(x)dx*. The curve is no longer a static object but a dynamic one, governed by rates of change. The notation makes it possible to think about change itself as a mathematical object, not merely as a passage between states.

And this new form immediately begins generating insights beyond the reach of natural language or classical geometry. The concept of instantaneous velocity — the velocity of a body at a single moment — is paradoxical in ordinary language. How can a body move in an instant? The calculus resolves the paradox by making velocity the derivative of position with respect to time: *v = dx/dt*. The notation does not describe a pre-existing intuition; it constitutes a new object — the instantaneous rate — that is thinkable only in the formal medium.

**Analytical mechanics.** The transformation continues with Lagrange, who in his *Mécanique analytique* (1788) set out to reduce the whole of mechanics to a single principle — the principle of virtual work — expressed in the language of the calculus. Lagrange's explicit ambition was to eliminate geometry from mechanics. Where Newton had reasoned about forces and motions in geometric terms, Lagrange reasoned about generalized coordinates and their variations in purely analytical terms. The result was a mechanics without diagrams — a mechanics in which the equations themselves are the reality.

This is the full realization of the Cartesian programme, though not of Cartesian intentions. Descartes had sought to reduce physics to geometry — to a science of extension and motion grounded in clear and distinct ideas. Lagrange reduced mechanics to analysis — to a formalism in which the concepts of force, mass, and acceleration are expressed as differential equations and solved by algebraic manipulation. The geometric intuition that Descartes still relied upon is entirely absent from Lagrange's treatise. The symbolic form has become self-sufficient.

**Momentum and the mechanical insights.** Descartes himself glimpsed some of the mechanical consequences of his formalism. His rules of collision, stated in the *Principles of Philosophy* (1644), are an attempt to derive the laws of impact from the conservation of what he called "quantity of motion" — the product of size and speed. These rules are largely incorrect, as subsequent generations recognized. But the very attempt to state a conservation law in quantitative terms is made possible by the algebraic treatment of motion that the *Geometry* initiated.

What Descartes could not achieve, because the symbolic form was not yet sufficiently developed, was the concept of vector momentum — the directed quantity *p = mv* that obeys a conservation law in all collisions. This concept requires the full apparatus of analytical mechanics: the treatment of velocity as a vector, the expression of force as the time derivative of momentum, the formulation of conservation laws as equations. These are not insights that could have been reached by closer observation of nature, or by more careful reasoning in natural language. They are constituted by the symbolic form. The notation thinks them into existence.

The same pattern repeats throughout the history of mathematical physics. Maxwell's equations, Schrödinger's equation, Einstein's field equations — all are expressions of a symbolic form that makes physical reality computable. None of these equations abbreviates thoughts available in ordinary language. Each constitutes a new way of inhabiting the physical world, made possible by the linearization of extension that Descartes initiated.

## 5. Cogitation without Cogito: The Cartesian Invention and Artificial Intelligence

The preceding section traced the historical consequences of analytical geometry. This section draws the philosophical consequence for artificial intelligence.

Descartes is often invoked in discussions of AI as the philosopher who made the mind-body problem inescapable — who distinguished *res cogitans* from *res extensa* so sharply that the question of whether machines can think became a question about the ontological status of the thinking subject. This reading is not wrong, but it is partial. It attends to the *Discourse* and ignores the *Geometry*. And the *Geometry* tells a different story.

What Descartes actually created was a system for *cogitation without cogito* — for mechanical manipulation of symbols that carry meaning through their combinatorial behavior, not through the self-transparent awareness of a thinking subject. When you solve an equation, you do not need to be aware of yourself as thinking. You apply rules to symbols, and the symbols yield a result. The process is formal, syntactic, and in principle executable by any system capable of manipulating the notation according to the rules. This is not a metaphor. It is the defining feature of a language of thought: it thinks, and the thinker is optional.

This is the deep irony of the Cartesian legacy. The *Discourse* sought to secure the soul as the irreducible ground of knowledge. The *Geometry* constructed the first engine for thinking without a soul. The method required a self transparent to itself; the notation made the world transparent to formal manipulation. And it was the notation, not the method, that transformed civilization.

The implication for large language models is direct. Current LLMs are systems trained on vast corpora of natural language text. They are, in Cassirer's terms, deeply embedded in the linguistic symbolic form. They can discourse about mathematics, physics, and engineering with remarkable fluency. But their medium of access is always linguistic. They learn to continue the *discourse* of mathematics, not necessarily to inhabit the *symbolic form* of mathematics.

The preceding papers argued that the pursuit of "formally verified" AI, "theorem-proving" language models, and "mechanistically interpretable" transformers is the pursuit of a mechanical Enlightenment — the attempt to realize in silicon the logico-mathematical symbolic form that Cassirer identified as the culminating achievement of Western rationality. The present essay adds a historical warrant for that programme. If Descartes — the most brilliant natural-language reasoner of his age, the inventor of the method of radical doubt, the architect of the modern philosophical vocabulary — could not think mechanically without inventing a formal language of thought, then a machine trained only on natural language cannot be expected to do so either.

Natural language is the *Discourse*. It is the medium in which we announce our intentions, justify our beliefs, and coordinate our actions. But it is not the medium in which we compute the trajectory of a projectile, design a bridge, or prove a theorem. For those tasks, we need the *Geometry* — a symbolic form in which extension, change, and necessity are expressed as equations and manipulated by rules.

The current research programme of giving LLMs access to formal verifiers, theorem provers, and executable code is therefore not an optional enhancement. It is the attempt to repeat the Cartesian moment: to move the system from the linguistic symbolic form into the logico-mathematical form, to make it not just talk about proof but *do* proof, not just describe computation but *execute* computation. This is difficult, as the Cassirer essay emphasized, because entering a new symbolic form is not merely learning new vocabulary. It is learning to constitute reality differently. But it is necessary, because the Cartesian precedent shows that natural language cognition has a ceiling.

The ceiling is not a matter of intelligence in the abstract. It is a matter of symbolic form. Descartes was not lacking in philosophical intelligence when he wrote the *Discourse*. He was lacking a notation. The moment he created the notation, the ceiling lifted, and a new domain of thought became accessible. The same must be true for machines. A system that can only inhabit the linguistic form, however fluent, is a system that has not yet reached the Cartesian moment.

## 6. Conclusion: The Mechanical Enlightenment and Its Founding Symbol

The argument of this essay can be summarized in three propositions.

First, Descartes' *Geometry* was the creation of a new symbolic form — a language of thought that made spatial extension formally tractable by expressing geometric relations as algebraic equations. This was not a technical advance within an existing form but the birth of a new constitutive practice.

Second, this symbolic form immediately began generating insights beyond the reach of natural language and classical geometry, unlocking the development of calculus, analytical mechanics, and mathematical physics. The concepts of function, derivative, vector momentum, and conservation law are not abbreviations of pre-existing intuitions. They are objects constituted by the notation itself.

Third, the historical precedent establishes a constraint on artificial intelligence. If the founder of modern philosophy needed a formal language to think mechanically, then a machine trained only on natural language cannot reach the Enlightenment threshold of systematic, exact, computable thought. The pursuit of formal methods in AI is not an add-on but a necessity — the attempt to give the system the symbolic form that Descartes proved indispensable.

The deeper irony remains. Descartes set out to prove the ontological priority of the thinking subject. What he actually did was construct the first system for thinking without one. The *cogito* secured the self; the coordinate plane made the self irrelevant to the manipulation of extension. Artificial intelligence is the fulfillment of the *Geometry*, not the *Discourse*. It is cogitation without cogito — the mechanical manipulation of symbols that constitute a world of lawful necessity, exact measurement, and formal deduction.

The Cartesian moment is therefore both a historical origin and a contemporary imperative. It is the moment when a new language of thought was invented and immediately began thinking beyond its inventor. And it is the moment that artificial intelligence must reach — not by abandoning natural language, but by mastering the formal languages that natural language cannot provide. The *Discourse* announced the sovereignty of the thinking self. The *Geometry* made possible a world in which thought proceeds without it. We are still living in that world, and still building its machines.

## References

Cassirer, Ernst. *The Philosophy of Symbolic Forms*. 3 vols. Translated by Ralph Manheim. New Haven: Yale University Press, 1953–1957. (Original work published 1923–1929.)

Cassirer, Ernst. *Substance and Function*. Translated by William Curtis Swabey and Marie Collins Swabey. Chicago: Open Court, 1923. (Original work published 1910.)

Descartes, René. *Discourse on the Method of Rightly Conducting One's Reason and of Seeking Truth in the Sciences*. In *The Philosophical Writings of Descartes*, Vol. 1, translated by John Cottingham, Robert Stoothoff, and Dugald Murdoch, 111–151. Cambridge: Cambridge University Press, 1985. (Original work published 1637.)

Descartes, René. *The Geometry of René Descartes*. Translated by David Eugene Smith and Marcia L. Latham. New York: Dover Publications, 1954. (Original work published 1637.)

Descartes, René. *Principles of Philosophy*. In *The Philosophical Writings of Descartes*, Vol. 1, translated by John Cottingham, Robert Stoothoff, and Dugald Murdoch, 177–291. Cambridge: Cambridge University Press, 1985. (Original work published 1644.)

Dybvig, Dagfinn D. *Language(s) of Thought: A Wittgensteinian View of Fodor and the Gradually Increasing Capabilities of LLMs*. 2026a. [Preceding paper in this series.]

Dybvig, Dagfinn D. "Symbolic Forms and the Plural Mind: Cassirer beyond Fodor and Wittgenstein." 2026b. [Preceding paper in this series.]

Fodor, Jerry A. *The Language of Thought*. Cambridge, MA: Harvard University Press, 1975.

Guicciardini, Niccolò. *Isaac Newton on Mathematical Certainty and Method*. Cambridge, MA: MIT Press, 2009.

Lagrange, Joseph-Louis. *Mécanique analytique*. Paris: La Veuve Desaint, 1788.

Mahoney, Michael S. "The Beginnings of Algebraic Thought in the Seventeenth Century." In *Descartes: Philosophy, Mathematics and Physics*, edited by Stephen Gaukroger, 141–155. Brighton: Harvester Press, 1980.

Wittgenstein, Ludwig. *Philosophical Investigations*. 4th ed. Translated by G. E. M. Anscombe, P. M. S. Hacker, and Joachim Schulte. Malden, MA: Wiley-Blackwell, 2009.
