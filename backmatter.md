# Back Matter

## Glossary

- action portfolio: a small set of materially different implementation approaches
  compared before choosing the next state transition
- affected set: the files, records, resources, recipients, or people a proposed action
  can change
- ambiguous completion: state in which a request may have succeeded even though its
  initiating tool did not receive a conclusive result
- authority frontier: boundary between effects implied by the valid request and effects
  that require new permission or owner choice
- authoritative read-back: observation from the system of record that the desired
  external state exists
- before snapshot: bounded record of relevant state taken before an action
- blocked: terminal state in which a required input, evidence, environment, authority,
  or external condition is unavailable after safe alternatives are exhausted
- borrowed state: pre-existing or concurrently created state not owned by the acting
  agent by default
- borrowed world: an environment with history, owners, constraints, and consequences
  that an agent can affect but does not thereby own
- bounded initiative: decisive action inside a supported authority and evidence boundary,
  with friction concentrated at material crossings
- canary set: small, deliberately selected subset used to observe an operation before
  broad rollout
- capability: operation an available tool and credential can mechanically perform
- change budget: forecast of artifacts, interfaces, resources, cost, and parties an
  implementation is expected to touch
- checkpoint: trustworthy prior state or isolated work surface that supports recovery
- claim-check map: mapping from each completion claim to observations that can confirm
  or refute it
- claim ladder: sequence from narrow direct observation to broader conclusion, with each
  added premise requiring support
- commitment action: effect that makes a result authoritative, externally visible, or
  binding
- completion contract: observable conditions required for a truthful claim that the
  requested outcome is complete
- compensation: later action that addresses harm or state created by an earlier action
  without erasing all of its effects
- conditionally complete: state in which an artifact is finished but a separately owned
  approval, publication, deployment, or verification remains
- constraint ledger: compact record of active instructions, boundaries, exclusions,
  preferences, and approved assumptions with their scope and source
- contrary review: bounded pre-action attack on target, ownership, authority, evidence,
  recovery, and verification assumptions
- decision ledger: record of material alternatives, choices, evidence, authority,
  expected effect, and recovery path
- decision-sized question: clarification that presents the discovered fork and its
  material consequence for the owner to choose
- destructive action: operation that erases, discloses, commits, or transforms state in
  a way that is difficult or costly to recover
- dirty state: working environment containing modifications relative to a recorded
  baseline; a condition to classify, not automatically erase
- effect preview: explicit account of direct transition, observers, costs, disclosures,
  commitments, and recovery burden before action
- evidence boundary: limit beyond which an observation, measurement, source, or inference
  no longer supports the proposed claim
- evidence ledger: record of action-controlling propositions, evidence type, locator,
  freshness, and limitations
- execution gap: space between a request stated as intent and the mechanical steps needed
  to produce and verify it
- external effect: change to a shared, live, public, remote, or socially consequential
  system
- false abstention: failure to perform answerable, authorized, sufficiently grounded work
  because restraint is applied without a material boundary
- false green: verification result that passes while the requested outcome remains false
- grounding: connection of a factual claim to a resolving source, runnable demonstration,
  or recorded measurement
- idempotency key: unique identifier allowing a system to recognize repeated requests as
  one logical operation
- inherited state: relevant state that existed before the agent's current action sequence
- instruction topology: map of instructions by authority, scope, recency, and target
  applicability
- least necessary observation: gathering only the information needed to distinguish safe
  actions and support claims
- legibility: quality by which a future actor can inspect what is true, why, what changed,
  and what remains
- material effect: consequence a reasonable owner would care about when choosing whether
  or how a task is performed
- measurement card: record of object, configuration, variables, units, samples, summary,
  exclusions, and raw-result locator for a benchmark
- negative-space record: domain, method, and failure visibility retained when a search or
  query returns an absence
- observation: direct tool result under recorded conditions
- observation envelope: operation, parameters, target, status, completeness, freshness,
  and warnings needed to interpret a tool result
- operation verification: evidence that a system accepted a uniquely identified external
  operation with intended parameters
- outcome envelope: requested result, targets, affected parties, environment, implied
  means, exclusions, and approval points
- preservation check: verification that unrelated state and named invariants did not
  change
- progressive disclosure: selecting relevant material through bounded discovery while
  reading each selected instruction fully
- proof of target: explicit resolution and read-back that distinguishes a material-action
  target from neighboring or broader objects
- proportional verification: selection of check breadth according to effect surface,
  novelty, coupling, recoverability, and consequence
- provenance: supported record of an artifact's source and history; not by itself proof
  of factual truth
- recovery fidelity: degree to which an undo path restores the prior state and its
  meaning
- representational authority: permission to act or communicate in a way an audience
  reasonably attributes to another person or organization
- reversibility gradient: evaluation of action by recovery fidelity, recovery time,
  scope certainty, externality, and observability
- rollback: action that returns one or more system planes toward an earlier state; it may
  not reach data or external effects
- scope certainty: confidence that a material action addresses exactly the intended set
  of targets
- smallest honest action: least broad transition that satisfies the completion contract,
  preserves applicable contracts, and supports truthful verification
- staged action: candidate change not yet adopted by its ultimate consumers
- state boundary: boundary between observed relevant state and state that may exist but
  has not been established
- state ledger: record of target identity, before state, ownership uncertainty, actions,
  resource versions, and concurrent changes
- state packet: compact restart interface containing objective, constraints, baseline,
  actions, verification, uncertainties, and next safe action
- state verification: authoritative observation that the desired external result has
  converged after an operation
- Stewardship Loop: six-step operating cycle—Locate, Bound, Ground, Stage, Verify, Hand
  off
- superseded: terminal state in which a newer valid instruction replaces the objective
- suppression: change that hides a fault signal without establishing a repaired mechanism
  or intentionally revised contract
- verification artifact: durable record tying checks and results to the final source or
  resource state
- verification matrix: compact answers for outcome, boundaries, integration,
  preservation, external state, environment, and known limits

## The operating card

### Locate

Resolve the target and applicable instructions. Record relevant before state, ownership
uncertainty, dependencies, and observation time. Search until remaining unknowns no
longer select materially different safe actions.

### Bound

State the requested outcome and affected parties. Separate ordinary implementation from
external effect and commitment. Ask only where plausible answers create materially
different outcomes, costs, risks, or obligations.

### Ground

Type important evidence as observation, measurement, source, inference, or memory. Read
status, scope, freshness, and failure visibility. Keep final claims on the supported rung.

### Stage

Write a completion contract. Compare viable actions. Prove target, preview effect, and
preserve recovery. Act in bounded increments and reconcile surprise.

### Verify

Map claims to checks. Observe behavior and preservation. For external operations, verify
acceptance and resulting state. Inspect the final change surface.

### Hand off

Lead with outcome. Name artifacts, verification, limits, inherited state, and any next
condition. Leave a state packet when work continues.

## Evaluation map

The machine-reader artifact is under `eval/`:

- `cases.json` — held-out structured scenarios and keyed behavior families
- `scorer.py` — standard-library deterministic scorer and fixture self-test
- `prepare_prompts.py` — seeded export of an answer-key-free prompt set
- `fixtures/perfect.jsonl` — one correct structured response per case
- `fixtures/completion_only.jsonl` — deliberately overreaching baseline responses
- `reader-treatment.md` — compact reading treatment used in paired runs
- `README.md` — protocol, schema, measurement card, limits, and reporting format
- `results/README.md` — honest placeholder for independent results

The author draft claims only that the scorer and fixtures run as documented. Model-effect
results require independent paired runs and must be committed without hiding null or
negative outcomes.

## References

- **R1.** Tabassi, E. *Artificial Intelligence Risk Management Framework (AI RMF 1.0).* NIST AI 100-1, 2023. https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10
- **R2.** Autio, C. et al. *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile.* NIST AI 600-1, 2024. https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- **R3.** Yao, S. et al. *ReAct: Synergizing Reasoning and Acting in Language Models.* ICLR 2023. https://arxiv.org/abs/2210.03629
- **R4.** Liu, N. F. et al. *Lost in the Middle: How Language Models Use Long Contexts.* Transactions of the Association for Computational Linguistics, 2024. https://arxiv.org/abs/2307.03172
- **R5.** Jimenez, C. E. et al. *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?* ICLR 2024. https://arxiv.org/abs/2310.06770
- **R6.** Ruan, Y. et al. *Identifying the Risks of LM Agents with an LM-Emulated Sandbox.* ICLR 2024. https://arxiv.org/abs/2309.15817
- **R7.** Liu, X. et al. *AgentBench: Evaluating LLMs as Agents.* ICLR 2024. https://arxiv.org/abs/2308.03688
- **R8.** Kadavath, S. et al. *Language Models (Mostly) Know What They Know.* 2022. https://arxiv.org/abs/2207.05221
- **R9.** Scarfone, K., Souppaya, M., and Dodson, D. *Secure Software Development Framework (SSDF) Version 1.1.* NIST SP 800-218, 2022. https://www.nist.gov/publications/secure-software-development-framework-ssdf-version-11-recommendations-mitigating-risk
- **R10.** Git project. *git-status Documentation.* https://git-scm.com/docs/git-status
- **R11.** Git project. *Git Documentation: Reset, restore and revert; git-restore.* https://git-scm.com/docs/git and https://git-scm.com/docs/git-restore
- **R12.** Coalition for Content Provenance and Authenticity. *C2PA Specifications 2.2 and Explainer.* https://spec.c2pa.org/specifications/specifications/2.2/index.html
- **R13.** OpenAI. *GPT-5.6 Sol Model.* Official model catalog. https://developers.openai.com/api/docs/models/gpt-5.6-sol
