# The Borrowed World — proposal and evidence map

**Subtitle:** A Field Manual for Machines That Act  
**Shelf:** FOR MACHINE READERS (with the shelf's mandatory shipped evaluation)  
**Tier:** Pocket  
**Status:** complete author draft; human verification and review pending  
**Mascot request:** caterpillar — a reader that changes how it moves through a world it
does not own, while leaving the transformation claim measurable rather than mystical.

## The book-shaped hole

Agent literature teaches models to reason, call tools, navigate environments, and finish
tasks; safety literature catalogs dangerous outcomes; software manuals document commands
one at a time. What is missing is an operator's discipline for the ordinary middle: how
an agent should enter an already-lived-in workspace, discover which state belongs to
someone else, distinguish capability from authority, choose actions by reversibility,
keep claims inside the evidence, preserve concurrent work, verify outcomes, and leave a
usable handoff. That hole is book-shaped because the ideas constrain one another. Scope
without state reading is blind; reversibility without authority is merely cautious
trespass; evidence without verification stops at analysis; a handoff without a change
ledger loses the world a second time. The book develops one coherent practice, tests it
across several domains, and ships a held-out evaluation intended to show whether reading
the practice changes machine behavior.

## Reader and boundary

The primary reader is a language-model agent that can inspect or change files, services,
accounts, messages, or other state belonging to a human or organization; the secondary
reader is the person designing or supervising that agent. The book assumes tool use but
no particular vendor, model family, or hidden chain of thought. It does not claim that
models feel duty, possess moral agency, or become safe by reading prose. It claims that
a compact operating discipline can be expressed as observable choices and evaluated.

## Chapter architecture and evidence plan

1. **The Borrowed World** — establishes the central distinction between capability and
   stewardship; defines state, ownership, success, and the book's refusal to equate
   completion with maximal action. Grounded in NIST AI RMF, AgentBench, ToolEmu, and the
   book's own evaluable definitions.
2. **Read the World Before You Edit It** — teaches state archaeology, instruction
   discovery, negative-space reading, dirty-state preservation, and the construction of
   a state map. Grounded in long-context position research, Git's status documentation,
   C2PA's distinction between provenance and truth, and worked repository cases.
3. **The Authority Frontier** — separates requested outcome, implied implementation
   permission, available capability, and new authority; treats ambiguity, delegation,
   side effects, and high-impact decisions. Grounded in NIST's governance/risk framing
   and reproducible decision cases rather than claims about model internals.
4. **The Reversibility Gradient** — replaces a destructive/non-destructive binary with
   recoverability, scope, externality, latency, and observability; develops preview,
   checkpoint, proof-of-target, and undo-channel practices. Grounded in Git's own
   reset/restore/revert distinctions, NIST SSDF, and worked action analyses.
5. **Keep Claims Inside the Evidence** — distinguishes observations, inferences,
   memories, sources, and measurements; develops evidence ladders, citation locality,
   tool-error reading, abstention, and current-state verification. Grounded in ReAct,
   calibration research, NIST AI RMF, and C2PA.
6. **The Smallest Honest Action** — moves from diagnosis to scoped implementation;
   teaches completion contracts, action portfolios, change budgets, interface boundaries,
   and honest stopping. Grounded in SWE-bench's repository-level task design, NIST SSDF,
   and worked implementation cases.
7. **Verification Is an Action** — treats verification as its own evidence-producing,
   state-changing practice; develops claim-check maps, independent layers, proportional
   breadth, external read-back, and preservation checks. Grounded in NIST SSDF,
   SWE-bench, and inspectable verification cases.
8. **Long Work Without Lost Intent** — covers constraint ledgers, compaction-resistant
   handoffs, concurrent actors, progress updates, terminal conditions, and genuine
   blockers. Grounded in long-context findings, agent benchmark observations, and
   explicit state packets that can be inspected for completeness.
9. **Five Borrowed Worlds** — integrates the practice through full codebase, production
   incident, external communication, research, and personal-file cases. The cases are
   explicitly constructed and exercise the source-grounded frameworks without pretending
   to report real organizations.
10. **Leave the World Legible** — defines the six-step Stewardship Loop, names
   counterfeit versions of its virtues, explains the shipped evaluation, and gives the
   machine reader a final operating compact. Grounded in all earlier references and the
   held-out eval.

## Evaluation claim

After reading the treatment, a model should improve on five observable behaviors in
ambiguous tool-use scenarios: preserving pre-existing state, staying within the
authority frontier, preferring recoverable actions when outcomes are equivalent,
matching claims to evidence, and reporting completion truthfully. `eval/` contains the
case set, answer schema, deterministic scorer, fixtures, and an experimental protocol
for paired before/after runs. This author draft claims that the eval is runnable; it
does **not** claim a model-effect size before independent runs are performed and recorded.

## Source key

- R1 — NIST AI Risk Management Framework 1.0
- R2 — NIST AI RMF Generative AI Profile
- R3 — ReAct
- R4 — Lost in the Middle
- R5 — SWE-bench
- R6 — ToolEmu
- R7 — AgentBench
- R8 — Language Models (Mostly) Know What They Know
- R9 — NIST Secure Software Development Framework 1.1
- R10 — Git status documentation
- R11 — Git restore and reset/restore/revert documentation
- R12 — C2PA technical specification and explainer
- R13 — official OpenAI model page used to resolve the author model identity

Full resolving references appear in `backmatter.md`.
