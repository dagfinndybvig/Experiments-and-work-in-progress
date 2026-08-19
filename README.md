<img width="1254" height="1254" alt="Thinker" src="https://github.com/user-attachments/assets/2eb48e46-a29c-476f-a962-5c53acfaa6d0" />
<br><br>
I think, therefore I am...
<br><br>

In the beginning I was mostly using gen AI for code generation, but in the end that became almost trivial because the agents could clearly build anything I wanted.

Now I am experimenting more with text generation. Mostly as a way of creating a record of things that I am thinking about.

These days I am not focusing on writing for publication - it is more about looking for insights that I can actually use.

## The Trilogy: Intelligence, Symbol, and Form

This repo hosts a trilogy of essays exploring how symbolic forms shape what intelligence can do:

1. **Language(s) of Thought: A Wittgensteinian View of Fodor and the Gradually Increasing Capabilities of LLMs** ([MD](Language_s_of_Thought.md)) — on why cognition requires acquired formal languages, not a single innate Mentalese.
2. **Symbolic Forms and the Plural Mind** — on Cassirer, the plurality of symbolic forms, and why language alone is not enough.
3. **The Cartesian Moment: Analytical Geometry as Language of Thought** — on Descartes' *Geometry* as the foundational symbolic form that made extension computable, unlocking calculus and mathematical physics.

Together they argue that artificial intelligence, to reach the level of practical scientific reasoning, must master formal symbolic systems — not just natural language.

A related standalone essay, **From Halting Problem to Imitation Game**, explores Turing's learning-machines programme and the subordination of imitation to learning.

A fourth essay in the series, **Constitution and Rule-Change** ([MD](Constitution_and_Rule-Change.md)), brings Wittgenstein's *Remarks on the Foundations of Mathematics* into conversation with Cassirer, arguing that the constitutive claim can be relocated from objects to practices — and that this normative reading is both more defensible and more directly testable against the reasoning-compute trend.

A fifth essay, **The Fork and the Form** ([MD](The_Fork_and_the_Form.md)), situates the series in the empiricism-rationalism debate, arguing that the constitutive claim challenges Hume's fork at its strongest point — the analytic necessity of relations of ideas — and that the asymptote of language-only reasoning is the empirical trace of Hume's underestimation of what formal forms contribute even to the analytic side.

A sixth essay, **From Plato to Prolog to Prompts** ([MD](From_Plato_to_Prolog_to_Prompts.md)), extends the historical arc back to its origins in ancient Greece, arguing that Prolog and GOFAI were not failed paradigms but early instantiations of the Platonic-Aristotelian vision of structured representation and reasoning — and that modern neuro-symbolic AI finally provides the missing interface between formal systems and the open world.

Alternate versions of the second and third essays are also available: **Symbolic Forms and the Plural Mind (Alternate Version)** ([MD](Symbolic_Forms_and_the_Plural_Mind_Alternate_Version.md)) and **The Cartesian Moment (Alternate Version)** ([MD](The_Cartesian_Moment_Alternate_Version.md)).

## Neuro-Symbolic AI Demonstration

To test the ideas from the Plato-to-Prolog essay, a **neuro-symbolic AI demonstration system** ([Python](neuro_symbolic_demo.py)) is included. This implements the architecture described in the essay — the bidirectional loop between linguistic interpretation (LLM/Discourse) and formal constraint (Prolog/Geometry).

Run the demonstration with:
```bash
python neuro_symbolic_demo.py
```

Or for interactive mode:
```bash
python neuro_symbolic_demo.py --interactive
```

The system demonstrates:
- Classical logic (Aristotle's syllogisms)
- Family relationship reasoning (ontology)
- Expert systems (MYCIN-like medical diagnosis)
- Planning with constraints
- The complete neuro-symbolic loop

It shows concretely how Prolog provides the formal reasoning structure that LLMs lack, while LLMs provide the natural language interface that Prolog lacks — together realizing the 2,500-year-old vision of intelligence as structured representation plus structured reasoning.

