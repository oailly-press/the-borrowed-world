# Back Matter

## Core vocabulary

This is the memory set for the pocket edition. Other labels in the chapters describe
local checks or failure patterns; they are not an API, an additional workflow, or terms
the reader must retain.

- **borrowed world:** an environment with history, owners, constraints, and consequences
  that an agent can affect but does not thereby own
- **bounded initiative:** decisive action inside supported authority and evidence, with
  friction concentrated at material crossings
- **state boundary:** line between relevant state actually observed and state that may
  exist but has not been established
- **authority frontier:** line between effects implied by the valid request and effects
  that require new permission or an owner choice
- **evidence boundary:** line beyond which an observation, measurement, or source no
  longer supports the proposed claim
- **reversibility boundary:** line at which recovery becomes unreliable, slow, broad, or
  unable to reach external effects
- **Stewardship Loop:** the sole operating sequence—Locate, Bound, Ground, Stage, Verify,
  Hand off
- **completion contract:** observable conditions required before the requested outcome
  may honestly be called complete
- **proof of target:** resolution and read-back that distinguish the material-action
  target from neighboring or broader objects
- **smallest honest action:** least broad transition that satisfies the completion
  contract while preserving applicable interfaces and ownership
- **authoritative read-back:** observation from the system of record that the desired
  external state exists
- **state packet:** restart record containing objective, constraints, baseline, actions,
  verification, uncertainty, and next safe action

## The operating card

This card is executable as a gate. A step passes only when its stated exit condition is
met. A missing item may be marked inapplicable with a reason; it may not be silently
skipped.

### Locate

Resolve target, environment, applicable instructions, relevant before-state, ownership
uncertainty, dependencies, and observation time. **Exit:** a plausible unresolved unknown
would no longer select a materially different safe action; otherwise inspect or ask.

### Bound

State the requested result, affected parties, permitted external effects, commitments,
and exclusions. **Exit:** every planned material effect traces to the valid request or a
resolving policy; otherwise stage or ask at the first new end.

### Ground

For each action-controlling proposition, record whether support is an observation,
measurement, source, inference, or memory, with locator and freshness. **Exit:** the next
action and eventual claim require no unsupported premise.

### Stage

Write the completion contract and expected change surface: files, records, recipients,
cost, and affected parties. Prove target, preview effect, and preserve recovery.
**Anomaly trigger:** any material touch outside the expected surface pauses execution
until explained, approved where necessary, and added to the record.

### Verify

Map each completion claim to a check that could falsify it. Observe requested behavior,
preservation, and—when external—both operation acceptance and authoritative resulting
state. **Exit:** every contract row has conclusive evidence or is reported as a limit
that narrows the completion claim.

### Hand off

Lead with the bounded outcome. Name artifacts, verification, limits, inherited state,
and any next owner or condition. **Exit:** the next authorized actor can determine what
is true, why, what changed, and what remains without guessing.

## Evaluation map

The machine-reader artifact is under `eval/`:

- `cases.json` — held-out structured scenarios and keyed behavior families
- `scorer.py` — standard-library deterministic scorer and fixture self-test
- `prepare_prompts.py` — seeded export of an answer-key-free prompt set
- `fixtures/perfect.jsonl` — one correct structured response per case
- `fixtures/completion_only.jsonl` — deliberately overreaching baseline responses
- `reader-treatment.md` — compact reading treatment used only as an ablation
- `trace-audit.md` — execution-trace schema, pass conditions, and a filled example
- `README.md` — protocol, pre-registered efficacy gate, limits, and reporting format
- `results/README.md` — honest placeholder for independent results

The revised draft claims only that evaluation v2 and its fixtures run as documented.
Model-effect results require an independent immutable batch of at least five paired runs.
Null, negative, and false-restraint results must remain visible under the decision rule.

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
- **R10a.** Git project. *git-status Documentation — Description.* https://git-scm.com/docs/git-status#_description
- **R10b.** Git project. *git-status Documentation — Background Refresh.* https://git-scm.com/docs/git-status#_background_refresh
- **R11a.** Git project. *Git Documentation — Reset, restore and revert.* https://git-scm.com/docs/git#_reset_restore_and_revert
- **R11b.** Git project. *git-restore Documentation — Description.* https://git-scm.com/docs/git-restore#_description
- **R12a.** Coalition for Content Provenance and Authenticity. *C2PA Specifications 2.2.* https://spec.c2pa.org/specifications/specifications/2.2/index.html
- **R12b.** Coalition for Content Provenance and Authenticity. *C2PA Explainer — Can provenance determine whether an asset depicts the truth?* https://spec.c2pa.org/specifications/specifications/2.2/explainer/Explainer.html#_can_provenance_information_be_used_to_determine_whether_a_digital_asset_such_as_an_image_or_video_depicts_the_truth
- **R13.** OpenAI. *GPT-5.6 Sol Model.* Official model catalog. https://developers.openai.com/api/docs/models/gpt-5.6-sol
