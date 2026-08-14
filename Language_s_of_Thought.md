# Language(s) of Thought: A Wittgensteinian View of Fodor and the Gradually Increasing Capabilities of LLMs

*Dagfinn D. Dybvig with GPT 5.6*

Working paper | August 2026

---

**Central thesis.** Large language models are best understood not as failed theorem provers or mere conversational imitators, but as learners of many language-games. Some of those games, especially logic, mathematics, programming, and formal verification, can be internalized as acquired languages of thought that make linguistic intelligence more accountable without reducing intelligence to a single calculus.

---

## Abstract

This paper develops a Wittgensteinian reinterpretation of the Language of Thought hypothesis in light of the rise of large language models. Jerry Fodor was right to insist that general cognition requires systematic, recombinable, and inferentially consequential structure. He was less persuasive in treating a highly declarative, logic-like Mentalese as substantially innate. Human cognitive history suggests a different picture. Natural language may first function primarily in communication and coordination, while writing, arithmetic, logic, probability, calculus, and programming arise later as public symbolic practices that are gradually internalized as cognitive instruments. These practices are not merely expressions of prior thought. They enlarge the space of possible thought and provide standards by which thought can be corrected. LLMs illuminate this process because deep learning achieved broad, human-facing competence only when transformers were trained on natural language, the cultural medium through which many specialized formalisms are described and coordinated. Early chatbots acquired wide contextual fluency but remained weakly accountable. The emerging combination of reinforcement learning, tool use, theorem proving, formal verification, and verifiable process rewards points toward a more mature architecture: linguistic breadth joined to formal and environmental constraint. On this account, the future of AI lies neither in abandoning LLMs nor in rebuilding intelligence from logic. It lies in teaching language-trained models to recognize, enter, and submit to the norms of the appropriate language-games.

**Keywords:** language of thought; language-games; Fodor; Wittgenstein; large language models; formal reasoning; reinforcement learning; neuro-symbolic AI; mathematical cognition; AI agents

---

## 1. Introduction: From Fluency to Accountability

The contemporary debate over large language models is often organized around an unhelpful choice. Either linguistic fluency already constitutes intelligence, or LLMs are fundamentally unaccountable statistical imitators and should be abandoned. Both positions mistake a developmental stage for a completed architecture. LLMs have achieved something that earlier artificial intelligence did not: broad competence across a common linguistic medium, including conversation, explanation, translation, programming, mathematical discourse, and cross-domain analogy. Yet the same systems can confuse plausibility with truth, a proposed action with an executed one, and a proof-shaped text with a valid proof. The problem is real, but the conclusion that language modeling is a false start does not follow.

There is no comparably mature alternative waiting to replace LLMs. Classical symbolic AI produced theorem provers, expert systems, planners, semantic networks, frames, and logic programs, but repeatedly encountered brittleness, knowledge-acquisition bottlenecks, and poor performance outside manually structured domains.[^1]

Deep learning solved a different problem. It allowed useful representations to be learned rather than explicitly programmed, but its early successes were largely domain-specific. The major unlock occurred when scalable connectionist learning, the transformer architecture, and vast natural-language corpora were combined. The result was not a single new formal calculus. It was a learned interface to humanity's accumulated conceptual and symbolic culture.[^2]

This paper argues that the next step should be understood as formal education rather than architectural repudiation. LLMs should be trained to use logic, mathematics, programming, simulation, and verification as acquired instruments of self-constraint. The target is not intelligence derived from logic, but intelligence capable of discovering when language is insufficient and entering a stricter representational practice. This proposal can be illuminated by bringing Fodor's Language of Thought into conversation with the later Wittgenstein's language-games, with the cultural history of mathematical notation, and with recent work on reasoning and verifiable reinforcement learning.

---

## 2. Fodor's Achievement and His Overreach

Jerry Fodor's enduring insight is that mature cognition displays productivity, systematicity, and inferential coherence. A thinker who can entertain the thought that John loves Mary can normally entertain the structurally related thought that Mary loves John. Complex thoughts appear to contain reusable constituents whose arrangement affects their content and their role in inference. Fodor's Language of Thought hypothesis explains these features by positing internal, language-like representations that are transformed through syntactically sensitive computational processes.

The difficulty lies in the form and origin assigned to Mentalese. Fodor's characteristic examples are highly declarative. They resemble sentences from formal semantics or elementary logic: predicates applied to arguments, propositions embedded under belief operators, and conclusions derived from explicit premises. Such a format is well adapted to the explanatory concerns of analytic philosophy. It is much less obviously the format demanded by the practical life of early hominins.

Protohuman cognition had to organize perception, affect, action, memory, social coordination, and rapid response under uncertainty. A rustle in grass need not yield a logically warranted proposition that a predator is present. It may nevertheless justify flight because the costs of false negatives and false positives differ dramatically. The governing structure may have been less sentence to sentence than situation to affordance to action. Fodor's model risks mistaking the requirements of explicit rational justification for the requirements of life.

The same problem appears in Fodor's radical concept nativism. His regress argument maintains that concept learning through hypothesis testing presupposes the concepts needed to formulate the hypothesis. If a primitive concept cannot be definitionally composed from prior concepts, it seems that it cannot be learned. Fodor therefore moved toward the notorious suggestion that most lexical concepts are innate. Critics have argued that this result depends on an unduly narrow picture of learning, especially the assumption that acquisition must occur through explicit conceptual composition or hypothesis formation.[^4]

A connectionist alternative does not deny prior structure. Learning requires memory, discrimination, attention, update mechanisms, and sensitivity to regularity. But the innate possession of a learning architecture is not the innate possession of the mature concepts eventually acquired. Fodor may have confused what advanced thought must ultimately possess with what biological nature must initially provide.

---

## 3. The Formalism Projection Problem

There is a broader methodological temptation behind Fodor's proposal. A discipline's most powerful formal instrument can be projected onto cognition as its universal native code. If Fodor had been a statistician rather than a philosopher of language, he might have nominated Bayesian probability as the Language of Thought. If he had been Saul Kripke, modal logic might have appeared fundamental. A control theorist might select feedback equations; a decision theorist, expected utility; a programmer, procedures and data structures.

Each calculus captures a genuine dimension of intelligent activity. Logic asks what follows from specified premises. Probability asks how confidence should change with evidence. Decision theory asks what action maximizes expected value. Control theory asks how deviations from a target should modify behavior. Calculus represents continuous change. None has succeeded as a standalone foundation for general intelligence.

AI history provides an unusually large natural experiment. Logic programming, production systems, semantic networks, frames, ontologies, Bayesian networks, planning calculi, and expert systems all worked where the world had already been translated into their terms. They failed as general foundations because intelligence also has to determine what the relevant entities are, which distinctions matter, what the task means, and when the representation itself should be changed. The repeated pattern was formal success inside an enclosure and brittleness at its boundary.

Probability theory itself illustrates the historical contingency of formal languages. Humans and animals managed uncertain situations long before they possessed a probability calculus. The modern mathematical treatment emerged from specific early modern problems, including Cardano's analysis of games and the 1654 Pascal-Fermat correspondence on the fair division of stakes in an interrupted game.[^5]

A protohuman did not calculate a posterior probability. It acquired dispositions: a cue strengthened an expectation, which prepared an action. Probability theory later made uncertainty explicit, numerical, and manipulable. The calculus may improve cognition without being the original format in which cognition occurred. The same may be true of formal logic.

---

## 4. Wittgenstein: From One Mentalese to Many Language-Games

The later Wittgenstein offers a productive alternative. Meaning is not secured by an abstract relation between isolated signs and objects alone. It arises in language as it is woven into activity. A language-game includes words, rules, purposes, actions, and standards of competent participation. The same utterance can function as a request, report, warning, command, or joke depending on the practice in which it occurs.[^6]

LLMs can be described as systems for acquiring a very large repertoire of language-games. Their corpora contain conversations, narratives, explanations, proofs, programs, diagnoses, legal arguments, instructions, and plans. The model learns context-sensitive dispositions for continuing these practices. This is more illuminating than saying that it learns one unified semantic theory.

Not all language-games are equally important as languages of thought. Greetings and reassurance coordinate social interaction. Measurement, definition, calculation, proof, programming, and model construction create portable structures that can be reused to organize cognition across contexts. Some games primarily regulate relations among speakers. Others install methods for representing, transforming, and criticizing representations.

This distinction suggests a Wittgensteinian revision of Fodor. General intelligence may not require one innate Mentalese. It may require the capacity to participate in public practices whose rules can be progressively internalized. Arithmetic, logic, probability, calculus, programming, and scientific modeling become acquired languages of thought because their operations remain available after the immediate exchange and restructure subsequent reasoning.

The proposal is compatible with a Vygotskian developmental picture. Speech that first regulates interaction between people can become private and inner speech used for planning and self-regulation. A communicative practice becomes a psychological instrument.[^7]

---

## 5. Communication First, Representation Later?

The historical and evolutionary thesis need not be settled for the analogy to be useful. Some influential accounts treat language primarily as a technology of communication and cooperation rather than as the vehicle of complex thought. Tomasello locates its origins in shared intentionality, joint attention, cooperative motives, pointing, and pantomime. A recent review by Fedorenko and colleagues argues that language is primarily optimized for communication and that complex thought draws substantially on distinct neural systems.[^8]

On such a view, early language would represent the world mainly in the service of regulating attention, expectations, and joint action. Cultural evolution could then reconstruct linguistic resources for more detached representation. Writing stabilizes statements beyond the original encounter. Arithmetic detaches number from particular objects. Logic makes inferential dependencies explicit. Probability gives uncertainty a calculus. Programming turns descriptions of procedures into executable artifacts.

Mercier and Sperber add a further twist by arguing that reasoning may have evolved substantially for producing and evaluating arguments in communication. If their argumentative theory is right, formal logic is not simply the natural operation of solitary cognition made visible. It is partly a cultural discipline that extracts valid consequence from a practice originally entangled with persuasion, reputation, and defense of prior commitments.[^9]

The resulting speculative sequence is not that thought begins only with language. Prelinguistic and nonlinguistic cognition are substantial. Rather, language first broadens social coordination; internalized language supports planning and reflection; and later formal languages make some representations more stable, explicit, and accountable. The sequence is communication, inner regulation, representation, formalization, and self-correction.

---

## 6. Mathematics as an Acquired Language of Thought

Natural numbers provide a minimal example of how a culturally articulated system can become cognitively constitutive. Approximate number sensitivity appears in infants and nonhuman animals. Exact symbolic arithmetic depends far more on counting practices, number words, notation, and education. The result can therefore be both biologically prepared and culturally acquired.[^10]

Arithmetic is language-like in the relevant sense. It has primitives, recursive operations, compositional expressions, and rule-governed transformations. Its importance is not limited to calculation. It provides norms of identity, iteration, order, decomposition, and correction. Whether its explicit form is acquired or innate is secondary to the functional fact that any intelligence pursuing exact and extended reasoning must reckon with it or with a structural equivalent.

Recent work by Dehaene, Sablé-Meyer, and Ciccione explicitly proposes a shared language of thought for arithmetic and geometry based on repetition, concatenation, and recursive embedding. To understand a number is to possess one or more structured expressions connecting it to other numbers. Six can be three pairs, two triples, five plus one, or the successor of five. The notation makes a network of operations cognitively available.[^11]

Orwell's famous formulation in *Nineteen Eighty-Four* captures the political dimension: freedom includes the freedom to say that two plus two make four. The point is not only that arithmetic is true. It is that it supplies a standard that cannot be altered by authority merely through enforced assent.[^12]

For AI, arithmetic distinguishes linguistic acceptability from inferential accountability. A model may find a continuation probable because similar strings occur in its corpus. Arithmetic asks whether the transformation preserves the relevant structure. This is the elementary form of a court of appeal external to conversational confidence.

---

## 7. Infinitesimals and the Invention of Better Things to Think With

Leibnizian infinitesimals provide an even stronger example. The notation dx, dy, and dy/dx created a manipulable language for vanishingly small change. The formalism was mathematically and physically productive before a fully satisfactory foundation had been secured. Leibniz described infinitesimals as useful fictions or ideal devices, although the exact interpretation of his position remains contested.[^13]

The historical order matters. Productive intuition and notation came before later rigorization. Limit-based analysis reconstructed calculus without treating infinitesimals as ordinary numbers. In the twentieth century, Abraham Robinson's nonstandard analysis supplied a logically rigorous framework containing genuine infinitesimal quantities.[^14]

Infinitesimal calculus shows that an invented symbolic system can guide valid and enormously fruitful cognition before its basic objects are philosophically settled. The notation did not merely abbreviate thoughts already available in ordinary language. It made instantaneous rates, accumulation, and differential equations systematically thinkable. It enlarged the space of representation and connected that space to the real world through classical physics.

This suggests a distinction between expressive and productive Mentalese. An expressive system states thoughts already available. A productive system creates operations through which new thoughts become constructible. The highest form of artificial intelligence would not merely solve problems in inherited notations. It would invent new representational primitives, discover fruitful operations over them, test their consequences, and later clarify their foundations.

---

## 8. Turing's Spiral: Chess, Imitation, Go, and Verified Reasoning

Turing's work offers a compact historical spiral. Before computers were available to execute it, Turing and David Champernowne devised Turochamp, a chess-playing procedure that Turing implemented manually as a human processor. The setup resembles a Chinese Room in physical arrangement, but its philosophical direction is the reverse of Searle's. Turing attributed competence to the organized procedure rather than inferring the absence of intelligence from the ignorance of one component.[^15]

Turing then generalized from task performance toward the imitation game. Rather than define thinking, he proposed a written interaction in which a judge attempts to distinguish a machine from a human participant. This was directionally right as a research program because it moved AI into the open-ended environment of language.[^16]

AlphaGo later combined imitation and objective competence. Its policy network initially learned from expert human games, while reinforcement learning, self-play, value estimation, and Monte Carlo tree search optimized for winning. Human behavior served as scaffolding, but the environment supplied the final criterion.[^17]

LLMs reversed the trajectory. They became broadly convincing in the imitation game before they became reliably competent in narrow verifiable domains. Current reasoning research is bringing them back toward Turing's original chessboard. Mathematics, code, logic, simulation, and formal proof provide outcomes that can be tested independently of human impressions of fluency.

---

## 9. Symbolic AI and LLMs as Complementary Incompletions

The relationship can be stated symmetrically. Classical theorem provers achieved accountability without breadth. Early LLMs achieved breadth without sufficient accountability. The former began after a problem had been formalized. The latter could interpret informal context but did not reliably preserve formal constraints.

| Paradigm | Primary strength | Primary weakness | Typical criterion |
|---|---|---|---|
| Symbolic AI | Exact inference in specified domains | Brittle translation from open context | Validity inside a formal system |
| Early deep learning | Learned representations and robust pattern recognition | Narrow task integration | Predictive or task accuracy |
| LLMs | Broad linguistic and contextual competence | Plausibility can outrun truth | Contextual continuation and instruction following |
| Formally trained agents | Context plus explicit constraint and feedback | Still limited by formalization quality | Verified outcomes in context |

The needed synthesis is not a theorem prover bolted mechanically onto a chatbot. It is a bidirectional capacity: interpret a worldly problem, construct an appropriate formalization, derive and verify consequences, and return to the original context with assumptions and limitations exposed. Formal validity and contextual adequacy must remain distinct.

```
Interpret → formalize → derive → verify → reinterpret → revise
```

This loop makes logic an instrument rather than a foundation. The model's linguistic competence identifies possible representations and relevant background. Formal systems constrain transformations. Execution, simulation, or experiment supplies environmental resistance. The revised linguistic understanding then guides the next attempt.

---

## 10. Formal Training as Education

The appropriate analogy is education. Human beings do not begin as theorem provers. They begin with perception, imitation, communication, intuitive categorization, narrative, and motivated reasoning. Arithmetic, writing, logic, scientific method, and proof are learned disciplines that externalize reasoning and make mistakes inspectable. Formal education does not replace ordinary cognition. It teaches ordinary cognition to leave some questions to structures less susceptible to improvisation, in a form of externalization.

The same strategy should guide AI. A formally trained LLM should not merely produce proof-like prose. It should acquire durable distinctions between hypothesis and conclusion, evidence and illustration, conjecture and proof, validity and plausibility, local success and general demonstration. It should be able to state that a conclusion follows under assumptions A, B, and C while questioning whether B adequately represents the real situation.

Recent research increasingly follows this integrated path. Formal proof assistants provide exact verification and automatic feedback, while LLMs contribute conjecture generation, translation between informal and formal statements, and heuristic search. Work on Lean-based verification has used formal proofs to identify errors in intermediate mathematical reasoning, while broader position papers now present formal mathematical reasoning as a central frontier for verifiable AI.[^18]

The difficulty remains substantial. FormalMATH, a Lean 4 benchmark spanning several mathematical domains, reported that even the strongest evaluated systems solved only a minority of problems under practical sampling budgets and displayed pronounced domain biases. This is evidence of an unfinished research program, not evidence that the linguistic substrate should be discarded.[^19]

---

## 11. Reinforcement Learning and the Norms of the Game

Wittgenstein's language-game metaphor helps identify what ordinary pretraining lacks. A corpus contains records of proof, programming, diagnosis, and planning, but observing the discourse of a practice is not yet participating under its consequences. The model may enter the correct genre while continuing to optimize the more basic game of plausible continuation.

Reinforcement learning with verifiable rewards changes the governing norm. A candidate proof is accepted or rejected by a checker. Code passes or fails tests. A plan satisfies or violates constraints. The model is no longer rewarded only for saying what successful participants tend to say. It receives consequences determined by whether it did what the practice requires.

Recent work on verifiable process rewards extends this idea from final answers to intermediate steps. Symbolic or algorithmic oracles can supply denser feedback for long trajectories, improving credit assignment when some intermediate decisions are correct and others are not. The limitations are equally instructive: the method depends on verifier quality and is hardest to extend into open-ended environments where success is contested or difficult to formalize.[^20]

The research direction is therefore neither pure formalization nor scale alone. It is learn broadly, formalize selectively, act cautiously, verify independently, and learn from failure. This is a computational version of the bootstrapping pattern by which human cognition constructed disciplines that subsequently reorganized cognition itself.

---

## 12. Why Abandoning LLMs Would Be a Retreat

The claim that LLMs are unaccountable identifies a genuine weakness. It does not identify a viable replacement. Theorem provers, planners, causal models, knowledge graphs, robots, evolutionary algorithms, and probabilistic programs each supply important capabilities. None presently offers the broad, cross-domain, culturally saturated interface achieved by language models.

Abandoning LLMs would therefore sacrifice the only demonstrated route to general linguistic and contextual competence in a single learned architecture. It would revive the old bottleneck: humans would again need to specify the ontology, translate ordinary requests, add background knowledge, decide relevance, and update the rules for each domain.

The rational response to unaccountability is instrumentation and education. Humans are accountable not because every neural transition is transparent, but because cognition is embedded in practices such as written calculation, experiments, ledgers, courts, peer criticism, and proof. Artificial agents can likewise be embedded in theorem provers, interpreters, tests, transaction controls, provenance systems, simulators, permissions, and independent verification.

This does not imply that the transformer must remain unchanged forever. Future systems may alter memory, recurrence, multimodality, planning, embodiment, and training objectives. What should be preserved is the central achievement: broad intelligence assembled through learned participation in language. To discard that layer because it is incomplete would constitute architectural amnesia.

---

## 13. Toward a Plural, Developmental Mentalese

The resulting theory replaces a singular innate Mentalese with a layered and extensible ecology of representations. Biological cognition supplies proto-representational capacities for object tracking, expectation, affect, action, and social attention. Natural language provides a public medium for coordinating minds and transmitting culture. Inner speech recruits that medium for planning and self-regulation. Writing stabilizes representations externally. Mathematics, logic, probability, programming, and scientific modeling add specialized systems of exact transformation and criticism.

Mentalese, on this view, is not one code hidden behind all thought. It is the evolving capacity to construct, internalize, coordinate, and revise multiple representational practices. Some are fast, embodied, and action-oriented. Some are social and persuasive. Some are declarative. Some are diagrammatic, probabilistic, executable, or formally deductive.

General intelligence consists partly in selecting the right regime. A proof problem calls for formal deduction. A diagnosis calls for probabilistic and causal reasoning. A control problem calls for feedback. A design problem may call for simulation. A moral or political problem may resist complete formalization and require explicit acknowledgment of contested values. No single calculus is sufficient.

The role of natural language is distinctive because it can describe, compare, and translate among the specialized games. It is a meta-medium rather than a perfect formal system. The transformer-language corpus conjunction was the major unlock because it gave connectionist learning access to the cultural interface through which humans coordinate many languages of thought.

---

## 14. Conclusion

Fodor was right that general cognition cannot be reduced to undifferentiated association. It requires systematic and recombinable representations whose structure matters to inference. He was probably wrong to identify the mature declarative style of modern formal thought with a substantially innate and universal Mentalese. At least the burden of proof should be his.

The later Wittgenstein suggests a more flexible model. Intelligence learns language-games. Some games coordinate social interaction, while others create portable disciplines of representation and correction. Arithmetic, logic, probability, calculus, programming, and formal verification function as acquired languages of thought because they alter what the participant can subsequently represent, derive, and check.

LLMs make this developmental picture concrete. Deep learning alone achieved powerful but largely local capacities. Transformers trained on natural language unlocked broad contextual intelligence because language contains the sedimented products of many human practices and formalisms. That achievement should not be abandoned because its first public form, the chatbot, was insufficiently accountable to facts.

The next stage is the formally educated agent. Such a system would move from conversation to explicit representation, from representation to planning, from planning to action, and from action to independent verification. It would use formal systems without being reduced to them. It would recognize that different language-games impose different standards and that some claims must answer not to conversational acceptance but to proof, execution, measurement, or the resistance of the world. In other words: Do not build intelligence out of logic. Build intelligence capable of logic.

If this is directionally right, the central problem of AI is no longer choosing between formalism and connectionism. It is constructing a bootstrapping path by which a language-trained connectionist system acquires increasingly exact practices of self-constraint and, eventually, the capacity to invent better tools with which to think and represent the world.

---

## Notes

[^1]: Russell and Norvig, *Artificial Intelligence*, chaps. 1, 7-10; Yang et al., "Formal Reasoning Meets LLMs."

[^2]: Vaswani et al., "Attention Is All You Need"; Rae et al., "Scaling Language Models."

[^3]: Fodor, *Language of Thought*; Fodor and Pylyshyn, "Connectionism and Cognitive Architecture."

[^4]: Aydede, "Are Most of Our Concepts Innate?"; Laurence and Margolis, *Building Blocks of Thought*, chaps. 24-25.

[^5]: Hacking, *Emergence of Probability*; Daston, *Classical Probability in the Enlightenment*.

[^6]: Wittgenstein, *Philosophical Investigations*, §§7, 23, 43.

[^7]: Vygotsky, *Thought and Language*; Alderson-Day and Fernyhough, "Inner Speech."

[^8]: Tomasello, *Origins of Human Communication*; Fedorenko, Piantadosi, and Gibson, "Language Is Primarily a Tool for Communication."

[^9]: Mercier and Sperber, "Why Do Humans Reason?"; Mercier and Sperber, *Enigma of Reason*.

[^10]: Piazza and Dehaene, "From Number Neurons to Mental Arithmetic"; Nieder, "Making of Number."

[^11]: Dehaene, Sablé-Meyer, and Ciccione, "Origins of Numbers," 526-40.

[^12]: Orwell, *Nineteen Eighty-Four*, part 1, chap. 7.

[^13]: Arthur, "Actual Infinitesimals"; Rabouin and Arthur, "Leibniz's Syncategorematic Infinitesimals II."

[^14]: Robinson, *Non-standard Analysis*; Keisler, *Elementary Calculus*.

[^15]: Kasparov and Friedel, "Reconstructing Turing's `Paper Machine'"; Searle, "Minds, Brains, and Programs."

[^16]: Turing, "Computing Machinery and Intelligence," 433-60.

[^17]: Silver et al., "Mastering the Game of Go"; Silver et al., "Mastering the Game of Go without Human Knowledge."

[^18]: Liu et al., "Safe"; Yang et al., "Formal Mathematical Reasoning."

[^19]: Yu et al., "FormalMATH."

[^20]: Yuan et al., "Verifiable Process Rewards"; Cheng et al., "Revisiting Reinforcement Learning."

---

## Bibliography

Alderson-Day, Ben, and Charles Fernyhough. "Inner Speech: Development, Cognitive Functions, Phenomenology, and Neurobiology." *Psychological Bulletin* 141, no. 5 (2015): 931-65. https://doi.org/10.1037/bul0000021.

Arthur, Richard T. W. "Actual Infinitesimals in Leibniz's Early Thought." In *The Philosophy of the Young Leibniz*, edited by Mark Kulstad, Mogens Lærke, and David Snyder, 11-28. Stuttgart: Franz Steiner, 2009.

Aydede, Murat. "Are Most of Our Concepts Innate?" *Synthese* 95, no. 2 (1993): 187-217.

Cheng, Zhoujun, et al. "Revisiting Reinforcement Learning for LLM Reasoning from a Cross-Domain Perspective." *Advances in Neural Information Processing Systems* 38 (2025).

Daston, Lorraine. *Classical Probability in the Enlightenment*. Princeton, NJ: Princeton University Press, 1988.

Dehaene, Stanislas, Mathias Sablé-Meyer, and Lorenzo Ciccione. "Origins of Numbers: A Shared Language-of-Thought for Arithmetic and Geometry?" *Trends in Cognitive Sciences* 29, no. 6 (2025): 526-40. https://doi.org/10.1016/j.tics.2025.02.006.

Fedorenko, Evelina, Steven T. Piantadosi, and Edward A. F. Gibson. "Language Is Primarily a Tool for Communication Rather than Thought." *Nature* 630 (2024): 575-86. https://doi.org/10.1038/s41586-024-07522-w.

Fodor, Jerry A. *The Language of Thought*. Cambridge, MA: Harvard University Press, 1975.

Fodor, Jerry A., and Zenon W. Pylyshyn. "Connectionism and Cognitive Architecture: A Critical Analysis." *Cognition* 28, nos. 1-2 (1988): 3-71. https://doi.org/10.1016/0010-0277(88)90031-5.

Hacking, Ian. *The Emergence of Probability*. 2nd ed. Cambridge: Cambridge University Press, 2006.

Keisler, H. Jerome. *Elementary Calculus: An Infinitesimal Approach*. 2nd ed. Boston: Prindle, Weber & Schmidt, 1986.

Kasparov, Garry, and Frederic Friedel. "Reconstructing Turing's `Paper Machine.'" *ICGA Journal* 40, no. 2 (2018): 99-119. https://doi.org/10.3233/ICG-180044.

Laurence, Stephen, and Eric Margolis. *The Building Blocks of Thought: A Rationalist Account of the Origins of Concepts*. Oxford: Oxford University Press, 2024.

Liu, Chengwu, et al. "Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-Aware Formal Verification." In *Proceedings of ACL 2025*, 11964-89. https://aclanthology.org/2025.acl-long.594/.

Mercier, Hugo, and Dan Sperber. *The Enigma of Reason*. Cambridge, MA: Harvard University Press, 2017.

Mercier, Hugo, and Dan Sperber. "Why Do Humans Reason? Arguments for an Argumentative Theory." *Behavioral and Brain Sciences* 34, no. 2 (2011): 57-74. https://doi.org/10.1017/S0140525X10000968.

Nieder, Andreas. "The Making of Number: From Content to Representation." *Trends in Cognitive Sciences*. Published online February 12, 2026. https://doi.org/10.1016/j.tics.2025.12.011.

Orwell, George. *Nineteen Eighty-Four*. London: Secker & Warburg, 1949.

Piazza, Manuela, and Stanislas Dehaene. "From Number Neurons to Mental Arithmetic: The Cognitive Neuroscience of Number Sense." In *The Cognitive Neurosciences*, 3rd ed., edited by Michael S. Gazzaniga. Cambridge, MA: MIT Press, 2004.

Rabouin, David, and Richard T. W. Arthur. "Leibniz's Syncategorematic Infinitesimals II." *Archive for History of Exact Sciences* 74 (2020): 401-43. https://doi.org/10.1007/s00407-020-00249-w.

Rae, Jack W., et al. "Scaling Language Models: Methods, Analysis & Insights from Training Gopher." arXiv:2112.11446. Revised January 21, 2022. https://arxiv.org/abs/2112.11446.

Robinson, Abraham. *Non-standard Analysis*. Revised edition. Princeton, NJ: Princeton University Press, 1974.

Russell, Stuart, and Peter Norvig. *Artificial Intelligence: A Modern Approach*. 4th ed. Harlow: Pearson, 2021.

Searle, John R. "Minds, Brains, and Programs." *Behavioral and Brain Sciences* 3, no. 3 (1980): 417-57. https://doi.org/10.1017/S0140525X00005756.

Silver, David, et al. "Mastering the Game of Go with Deep Neural Networks and Tree Search." *Nature* 529 (2016): 484-89. https://doi.org/10.1038/nature16961.

Silver, David, et al. "Mastering the Game of Go without Human Knowledge." *Nature* 550 (2017): 354-59. https://doi.org/10.1038/nature24270.

Tomasello, Michael. *Origins of Human Communication*. Cambridge, MA: MIT Press, 2008.

Turing, A. M. "Computing Machinery and Intelligence." *Mind* 59, no. 236 (1950): 433-60. https://doi.org/10.1093/mind/LIX.236.433.

Vaswani, Ashish, et al. "Attention Is All You Need." In *Advances in Neural Information Processing Systems* 30, 5998-6008. 2017.

Vygotsky, Lev S. *Thought and Language*. Revised edition. Translated by Alex Kozulin. Cambridge, MA: MIT Press, 1986.

Wittgenstein, Ludwig. *Philosophical Investigations*. 4th ed. Translated by G. E. M. Anscombe, P. M. S. Hacker, and Joachim Schulte. Malden, MA: Wiley-Blackwell, 2009.

Yang, Kaiyu, et al. "Formal Reasoning Meets LLMs: Toward AI for Mathematics and Verification." *Communications of the ACM*. February 10, 2026. https://cacm.acm.org/research/formal-reasoning-meets-llms-toward-ai-for-mathematics-and-verification/.

Yang, Kaiyu, et al. "Position: Formal Mathematical Reasoning: A New Frontier in AI." *Proceedings of the 42nd International Conference on Machine Learning*, PMLR 267 (2025): 82384-98. https://proceedings.mlr.press/v267/yang25az.html.

Yu, Zhouliang, et al. "FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models." arXiv:2505.02735. May 5, 2025. https://arxiv.org/abs/2505.02735.

Yuan, Huining, et al. "Verifiable Process Rewards for Agentic Reasoning." arXiv:2605.10325. Revised May 27, 2026. https://arxiv.org/abs/2605.10325.
