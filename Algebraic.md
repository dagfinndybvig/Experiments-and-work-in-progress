# The Algebraic Mind and Its Acquired Languages: Gary Marcus in the Ecology of Symbolic Forms

*Dagfinn D. Dybvig with GPT-6 Astra*

Working paper | September 2026

---

**Central thesis.** The capacity to operate over variables and structured representations may help explain how minds acquire languages of thought without implying that those languages are themselves innate. Gary Marcus supplies a challenge concerning cognitive machinery; the preceding essays supply an account of cultural development and normative practice. Bringing them together requires distinguishing what makes symbolic learning possible, what that learning creates, and what makes its results accountable.

---

## 1. Introduction: What Makes a Symbolic Form Learnable?

The preceding essays argued that intelligence requires more than linguistic fluency. Logic, mathematics, programming, and scientific modeling are acquired languages of thought: practices that make representations more systematic, operations more productive, and conclusions more accountable. Wittgenstein supplied the language of practice and rule; Cassirer supplied the idea of symbolic forms; Descartes supplied a historical example of a representational innovation that transformed what could be calculated and understood. The neuro-symbolic demonstrations translated part of this argument into an architecture joining linguistic interpretation to formal inference.

But the developmental account leaves a question behind. What must a learner already be able to do in order to acquire these practices? Saying that algebra is learned does not yet explain how a learner recognizes that the same operation applies to different things. Saying that a symbolic form is culturally invented does not explain how an individual maintains its relations while changing its contents. The history of notation and the architecture of learning are connected questions, not interchangeable ones.

Gary Marcus's *The Algebraic Mind: Integrating Connectionism and Cognitive Science* (2001) makes this difficulty central. Its title names not a mind that has completed a mathematics course, but a mind capable of operations over variables and structured representations. Marcus asks what computational organization would support that capacity, and whether influential connectionist models adequately explain it. His project is not simply to oppose neural networks to symbols. It is to investigate how a neural system could implement the machinery that symbolic explanations require.

Marcus therefore enters this series as both an ally and a challenge. He supports its insistence on structure, but resists any suggestion that explaining the acquisition of sophisticated formalisms removes the need to explain the machinery of acquisition. The proposed synthesis is a layered one: algebraic resources may support the learning of many symbolic languages, while those languages introduce operations, meanings, and standards not specified by the resources alone. Whether particular resources must be innate remains a further question.

## 2. What Marcus Means by "Algebraic"

Consider a procedure that takes an item and returns two copies of it. Learning that `red` produces `red red` and that `blue` produces `blue blue` does not, by itself, determine what will happen with a previously unseen item. A system might retain particular associations, exploit similarities among inputs, or acquire a procedure describable as `duplicate(X) = (X, X)`. The algebraic description matters because the operation is specified independently of the particular value occupying `X`.

A variable is not merely an unfamiliar name. It is a place in a structure that can receive different values while the operation remains stable. Binding connects that place to a particular value for the purposes of a computation. A procedure that preserves the same binding across two positions can reproduce an item without first learning a separate duplication association for each possible item. This independence is always relative to a supported domain: the procedure still needs an input representation, an output mechanism, and sufficient resources.

Structured representations introduce a related requirement. "John loves Mary" and "Mary loves John" contain the same words, but not the same relation between participants. A representation must preserve who occupies which role. Embedding creates a further demand: "Anna believes that John loves Mary" must keep the believer distinct from the participants in the embedded proposition. A collection of associated names is not enough to specify these differences.

Marcus's book develops the case for variables, structured representations, and the representation of individuals as elements of cognitive architecture. The crucial contrast is not between numbers and words, or digital computers and biological brains. It is between organizations that preserve these computational distinctions and organizations that fail to do so. A distributed representation need not be unstructured; a neural implementation need not eliminate operations over variables. The explanatory task is to show how the relevant organization is achieved.

This is why the book's subtitle matters. *Integrating Connectionism and Cognitive Science* proposes a problem of reconciliation. "Neural" describes aspects of implementation; "algebraic" describes aspects of computational organization. These descriptions need not compete. Conversely, calling a system neural does not establish that it possesses the structural capacities in question. One must identify the mechanism, or provide sufficiently discriminating behavioral evidence for its operation.

The connection to the series is immediate but limited. Algebraic machinery could support several acquired languages of thought without itself being any one of them. It would supply reusable resources, not a complete geometry, grammar, or ontology.

## 3. From Familiar Patterns to Systematic Generalization

The empirical importance of this distinction appears when a system encounters unfamiliar cases. Successful prediction on held-out examples is evidence of generalization, but different forms of generalization make different demands. New examples may resemble training examples closely. A harder task changes the occupants of a relation, rearranges familiar components into untrained combinations, or extends a structure beyond the depths previously encountered.

In "Rethinking Eliminative Connectionism," Marcus (1998) argues that the class of eliminative connectionist models he examines cannot extend universals to arbitrary instances outside their training space. The scope of the claim matters. It concerns particular architectures, representations, and generalization demands, not a theorem that every possible neural network must fail on every unfamiliar input. Its enduring methodological contribution is the demand to ask what kind of novelty a model can handle, rather than treating all successful generalization as equivalent.

Marcus and colleagues' experiments on seven-month-old infants provide a complementary example (Marcus et al. 1999). After exposure to artificial syllable sequences, infants differentiated familiar from unfamiliar sequence structures when tested with novel syllables. Patterns such as ABA and ABB illustrate the relevant distinction: what transfers is a relation of repetition across positions, rather than the identity of a particular syllable. The authors interpret the results as evidence for abstract algebraic rule learning.

The experiment is important without settling every architectural question. Generalizing a repetition pattern does not uniquely identify a mechanism for variable binding, establish a complete symbolic language in the infant, or demonstrate that the relevant mechanism is genetically specified. The authors' controls challenge particular alternatives, including explanations based only on transitional probabilities. They do not eliminate every possible learning account. Behavioral evidence constrains architecture without reading architecture directly out of behavior.

Three issues should therefore remain separate. Can a system represent a relation? Can its learning procedure acquire that relation under the available conditions? Can it apply the relation reliably to the relevant new cases? A model may have adequate representational capacity but learn an unreliable shortcut. Another may transfer effectively within a bounded domain without possessing an unrestricted procedure. Finite success does not establish unlimited systematicity; finite failure does not establish permanent impossibility.

Subsequent research makes this restraint necessary. Lake and Baroni (2023) show that a neural network trained through meta-learning for compositionality can achieve human-like systematic generalization in their experimental setting. That result does not establish universal reliability or settle the architecture of ordinary LLMs. It does challenge a simple opposition between neural learning and systematic behavior. Marcus's question survives as a demand for mechanisms and discriminating experiments, not as a license to dismiss every later network in advance.

## 4. Marcus and Fodor: Innate Machinery, Acquired Languages

The first essay in this series distinguished what mature cognition must possess from what biological nature must initially provide. That distinction remains useful, but Marcus forces us to apply it in both directions. Sophisticated competence does not prove that a sophisticated formalism was innate. Equally, the cultural acquisition of a formalism does not prove that all the machinery supporting it was acquired through the same process.

Fodor's Language of Thought hypothesis connects productivity and systematicity to internally structured representations. His stronger claims about concept nativism raise an additional question about the origins of representational content. Marcus's argument should not be collapsed into that entire package. A claim that cognition needs operations over variables is distinct from a claim that humans are born knowing particular mathematical rules, grammatical principles, or lexical concepts.

We should distinguish at least three levels. There are enabling resources, such as memory, attention, role-sensitive representation, and mechanisms for preserving identity across a computation. There are learned structures, such as a particular grammar, arithmetic procedure, or programming language. There are public standards through which those structures are taught, corrected, and extended. Establishing an innate contribution at the first level would not establish that the contents of the second or the norms of the third were genetically specified.

Marcus's discussion of the origins of symbol-manipulation machinery presses the case for an innate architectural contribution. The cultural account developed here can accommodate that possibility, but should not pretend to have demonstrated it. A proposed innate mechanism must be supported by developmental and computational evidence. Conversely, an account that claims to learn the mechanism must explain the resources, biases, experience, and training procedure that make the learning possible. "Learned" does not mean unstructured, just as "innate" does not mean a fully formed adult competence.

This qualifies the series' earlier contrast between one innate Mentalese and many acquired languages of thought. Multiplicity at the level of culturally developed representations does not logically exclude common machinery beneath them. Several programming languages can run on a shared computational architecture while exposing different abstractions. The analogy does not establish that the brain is a conventional computer; it shows why plurality of languages alone cannot decide the architecture of their implementation.

The reconciliation proposed here is consequently conditional. If learners possess or develop stable resources for binding, composition, and rule application, those resources could support entry into many symbolic practices. The practices would still be historically acquired and transformative. Marcus asks how learning can get started and generalize; Wittgenstein and Cassirer help ask what is learned and how its acquisition reorganizes thought.

## 5. Two Senses of Algebra: Marcus Meets Descartes and Cassirer

The title *The Algebraic Mind* invites a connection with the historical algebra explored in *The Cartesian Moment*. But the connection becomes informative only if we resist an equivocation. Marcus's algebraic machinery is a proposed feature of cognitive organization. Algebra as a mathematical practice is a historically developed system of expressions, transformations, problems, and standards. Possessing resources that support the latter is not the same as already possessing the latter.

Take the equation `y = mx + b`. A learner must distinguish the roles of the symbols, preserve an assignment while calculating, and understand which quantities vary in a given problem. These tasks draw on capacities that fit an algebraic description. But the equation's use in representing a line also depends on learned mathematical meanings and conventions. The capacity to bind a value to a variable does not itself supply coordinate geometry.

Descartes' achievement, understood within the longer history of algebra and geometry, exemplifies the construction of a powerful bridge between representational practices. It was not the first appearance of structured thought or the invention of the human capacity to handle relations. It reorganized existing resources into a method through which geometric problems could be approached algebraically. That reorganization opened paths to further developments without containing the whole of later calculus in advance.

This makes the series' constitutive thesis more precise. A new notation does not create cognitive powers from nothing. It stabilizes distinctions, makes operations repeatable, reduces burdens on memory, and organizes paths of inference that would otherwise be difficult to sustain. The important claim need not be that no earlier person could have any relevant intuition. It is that a public representational system can make a domain systematically tractable in ways that scattered intuitions do not.

Cassirer's emphasis on relations and functions strengthens this account. In *Substance and Function*, scientific concepts are not adequately understood as collections of common properties abstracted from individual things. Their significance depends on relational organization. Marcus's variables offer a possible computational resource for preserving relations as their occupants change. Cassirer addresses a different level: how relational systems organize scientific knowledge. This is a philosophical connection proposed here, not a claim that the two authors offer the same theory.

Nor would common algebraic resources erase the plurality of symbolic forms. The ability to preserve roles in a structure does not decide whether a structure is a proof, a story, a legal argument, or a scientific model. Those practices have different aims and standards. Shared machinery may help explain how one learner participates in several forms; it does not make their meanings or criteria interchangeable. Marcus can supply a candidate enabling condition without becoming a reduction of Cassirer.

## 6. Wittgenstein: Executing a Rule Is Not the Whole of a Practice

A machine can preserve a variable binding and still formalize the wrong problem. A person can execute an arithmetic procedure and still misunderstand when it applies. These possibilities separate the mechanism of a transformation from the practice that gives the transformation its role.

The Wittgensteinian contribution is not that computation becomes mysterious whenever norms appear. Within a specified formal system, a program can determine whether particular steps satisfy explicit rules. The further questions concern how the rules are taught, what the expressions mean in an application, which assumptions are accepted, and what counts as correcting a mistake rather than changing the subject. Competence includes application and judgment as well as execution.

Marcus and Wittgenstein can therefore be brought into conversation without making either answer the other's question. An architectural account asks how a learner represents a rule, binds its arguments, and carries an operation across cases. A practice-oriented account asks what makes those cases instances of the same activity and what licenses the operation there. A full explanation may require both, but their compatibility is an argument to develop, not a quotation to attribute to either author.

This distinction also qualifies the earlier essays' contrast between learning patterns and following rules. Statistical learning can produce a mechanism that performs rule-governed operations. The statistical character of training does not establish that the resulting computation is merely a collection of superficial associations. Nor does exposure to text imply exposure only to ordinary conversation: textual corpora can include programs, equations, and formal proofs. What matters is what organization is learned and how reliably it is exercised.

The series' proposed asymptote of language-only reasoning should accordingly remain a hypothesis, not a philosophical impossibility result. Neither Cassirer's account of symbolic forms nor Wittgenstein's account of mathematical practice, by itself, proves that a transformer cannot acquire an effective internal procedure. Residual errors and benefits from tools justify investigating limitations; they do not identify an immutable boundary. Claims about such a boundary require explicit task definitions and empirical evidence.

The case for external formal systems remains strong on more modest grounds. An inspectable derivation and an independently implemented checker can provide accountability that an unsupported answer lacks. Their value need not depend on proving that the proposing model could never reason correctly. They separate proposing from checking and expose assumptions for scrutiny. A proof checker establishes compliance with its formal rules; it does not establish that the formalized proposition faithfully captures the user's intention or the world.

## 7. From the Algebraic Mind to the Neuro-Symbolic Loop

The repository's LLM-SWI-Prolog demonstration gives these distinctions a concrete setting. Consider a simplified version of its family-relation scenario:

> John is a parent of Mary. Mary is a parent of Bob. Bob is a parent of Charlie. Who are Charlie's ancestors?

Suppose the formalization uses the following definition of ancestry:

```prolog
parent(john, mary).
parent(mary, bob).
parent(bob, charlie).

ancestor(X, Y) :- parent(X, Y).
ancestor(X, Z) :- parent(X, Y), ancestor(Y, Z).
```

The query is `ancestor(X, charlie)`. For this finite, acyclic knowledge base, the answers are Bob, Mary, and John, irrespective of presentation order.

The first rule covers direct parenthood. The second preserves a shared individual across two relations: the person bound to `Y` must be both a child of `X` and an ancestor of `Z`. Prolog's unification and fresh variables for separate rule invocations allow the same rule to be reused as the derivation proceeds. This is an explicit instance of the role-sensitive, variable-based organization Marcus asks cognitive models to explain.

Replacing every name consistently with an unfamiliar atom leaves the relational structure intact. Adding another parent link allows another application of the same rule. These are concrete forms of systematicity, not resemblance between familiar names. They remain subject to computational conditions: cyclic data, search order, and resource limits can affect execution. The repository's SWI-Prolog wrapper imposes an inference limit; the example is not a promise of unbounded practical computation.

The natural-language component has a different responsibility. It must interpret the question, extract the direction of parenthood, choose the intended definition of ancestry, and produce the right query. Returning Prolog's answers to language must preserve those commitments rather than inventing additional relationships. The architecture is thus the familiar loop:

```text
Interpret -> Formalize -> Derive -> Verify -> Reinterpret -> Revise
```

These labels describe responsibilities, not an assurance that the current demonstration implements an independent verifier or automatic revision for every failure. A Prolog query executes a derivation; it does not independently audit the translation that supplied its premises. The code is a demonstration of a division of labor, not a completed system for general epistemic accountability.

If "parent" was intended to mean a legal guardian rather than the relation encoded by the program, a formally correct result could answer the wrong question. If facts are missing, failure to derive an ancestor is not evidence that no such ancestor exists in reality. Formal inference constrains consequences relative to a representation. It does not certify that the representation is complete, appropriate, or true.

There is also a difference between locating algebraic operations inside a neural model and supplying them through a tool. The external-engine design gives the combined system explicit capabilities without demonstrating that the LLM has acquired the same machinery internally. Conversely, a neural implementation of systematic operations would not make external checking pointless. Marcus's integration problem admits several engineering arrangements, which should be compared rather than conflated.

A useful evaluation would vary names, reverse argument roles, withhold combinations, increase chain depth, and paraphrase the question. It would assess formalization, derivation, and final explanation separately. This is a proposed extension of the demonstration, not an experiment reported here. Its aim would be to establish where systematicity resides and where it fails, rather than assigning success or failure indiscriminately to "the AI."

## 8. Conclusion: An Algebraic Capacity, a Plural Education

Marcus changes the series by making its developmental thesis answer an architectural question. Public symbolic practices can transform cognition only if learners can acquire, preserve, and reuse their organization. Variable binding, structured representation, and operations that survive changes of content are candidate resources for explaining that capacity. Their origin cannot be settled merely by observing that mature mathematics is culturally transmitted.

The series, in turn, places an algebraic architecture within a larger account. Enabling machinery does not specify which symbolic languages will be invented, which objects and relations they will make tractable, or which norms will govern their use. Coordinate geometry is not simply variable binding written down. A scientific practice includes measurement, interpretation, criticism, and revision as well as formal transformation. A common computational resource need not imply a single complete language of thought.

The resulting position has three levels: resources for structured computation; acquired representational practices that organize problems and possibilities; and standards of correction that make their application accountable. These levels interact. Learning changes computational dispositions, public notation supports operations that unaided memory cannot sustain, and failures of application can motivate new formalisms. The layers are distinctions of explanation, not isolated compartments.

For artificial intelligence, the conclusion is neither that scaling must suffice nor that neural learning must fail. It is that the acquisition and deployment of structure must be demonstrated under demands that distinguish genuine transfer from narrow familiarity. We should investigate learned internal procedures, explicit external engines, and combinations of the two, while keeping correctness of inference separate from adequacy of formalization.

The mind described here is algebraic in its capacity to preserve structure and plural in the languages through which that capacity develops. Its education is not the accumulation of examples alone, but neither can its architecture replace education. Marcus helps ask how a learner can carry a rule beyond the cases it has seen. The preceding essays help ask how such rules become instruments of thought, and how thought learns when those instruments should be used.

## References

Cassirer, Ernst. *Substance and Function, and Einstein's Theory of Relativity*. Translated by William Curtis Swabey and Marie Collins Swabey. Chicago: Open Court, 1923. (*Substance and Function* originally published in 1910.)

Cassirer, Ernst. *The Philosophy of Symbolic Forms*. 3 vols. Translated by Ralph Manheim. New Haven: Yale University Press, 1953-1957. (Original volumes published 1923-1929.)

Descartes, Rene. *The Geometry of Rene Descartes*. Translated by David Eugene Smith and Marcia L. Latham. New York: Dover, 1954. (Original work published 1637.)

Dybvig, Dagfinn D., with GPT 5.6. [*Language(s) of Thought: A Wittgensteinian View of Fodor and the Gradually Increasing Capabilities of LLMs*](Language_s_of_Thought.md). Working paper, 2026.

Dybvig, Dagfinn D., and Kimi 2.6. [*Symbolic Forms and the Plural Mind: Cassirer beyond Fodor and Wittgenstein*](Symbolic_Forms_and_the_Plural_Mind.md). Working paper, 2026.

Dybvig, Dagfinn D., and Kimi 2.6. [*The Cartesian Moment: Analytical Geometry as Language of Thought*](The%20Cartesian%20Moment.md). Working paper, 2026.

Dybvig, Dagfinn D., and Mistral Vibe. [*Constitution and Rule-Change: Wittgenstein's Remarks, Cassirer's Forms, and the Asymptote of Language-Only Reasoning*](Constitution_and_Rule-Change.md). Working paper, 2026.

Dybvig, Dagfinn D., and Mistral Vibe. [*From Plato to Prolog to Prompts: The 2,500-Year Journey to Artificial Reason*](From_Plato_to_Prolog_to_Prompts.md). Working paper, 2026.

Fodor, Jerry A. *The Language of Thought*. New York: Thomas Y. Crowell, 1975.

Lake, Brenden M., and Marco Baroni. "Human-like Systematic Generalization through a Meta-learning Neural Network." *Nature* 623 (2023): 115-121. https://doi.org/10.1038/s41586-023-06668-3.

Marcus, Gary F. "Rethinking Eliminative Connectionism." *Cognitive Psychology* 37, no. 3 (1998): 243-282. https://doi.org/10.1006/cogp.1998.0694. [Abstract record](https://eric.ed.gov/?id=EJ578664).

Marcus, Gary F. *The Algebraic Mind: Integrating Connectionism and Cognitive Science*. Cambridge, MA: MIT Press, 2001. [Publisher page](https://mitpress.mit.edu/9780262632683/the-algebraic-mind/).

Marcus, Gary F., Sudha Vijayan, S. Bandi Rao, and Peter M. Vishton. "Rule Learning by Seven-Month-Old Infants." *Science* 283, no. 5398 (1999): 77-80. https://doi.org/10.1126/science.283.5398.77. [Abstract](https://pubmed.ncbi.nlm.nih.gov/9872745/).

Wittgenstein, Ludwig. *Philosophical Investigations*. 4th ed. Edited by P. M. S. Hacker and Joachim Schulte. Translated by G. E. M. Anscombe, P. M. S. Hacker, and Joachim Schulte. Wiley-Blackwell, 2009.

Wittgenstein, Ludwig. *Remarks on the Foundations of Mathematics*. Revised ed. Edited by G. H. von Wright, R. Rhees, and G. E. M. Anscombe. Translated by G. E. M. Anscombe. MIT Press, 1978.
