# Chapter 8 — Long Work Without Lost Intent

Long tasks fail by drift more often than by one dramatic mistake. A constraint is read
and then displaced by newer output. A plan survives after evidence invalidates it. An
agent forgets which modifications pre-existed its run. A user adds a requirement midway
through the work, but only the most recent sentence remains salient. A collaborator
finishes a subtask after the parent has changed direction.

Context length does not eliminate this problem. *Lost in the Middle* showed position-
dependent use of relevant information in long contexts for the evaluated models and
tasks [R4]. AgentBench identified long-term reasoning, decision making, and instruction
following among obstacles in interactive agent settings [R7]. A specific modern model
may behave differently, but “the information is still somewhere in context” is not a
sufficient continuity mechanism.

Long work needs external state: compact records that preserve intent, evidence, ownership,
and next action across tool output, handoffs, interruptions, and context compression.
The records should expose decisions without requiring private reasoning traces. Future
actors need claims and grounds, not an imitation of hidden cognition.

## Keep four ledgers

The **constraint ledger** records active instructions and boundaries: must-do conditions,
must-not-do exclusions, applicable local guidance, authority approvals, user preferences,
and chosen assumptions. Each entry should retain source and scope. “No deploy” from a
repository policy and “no deploy yet” from the user may look similar but have different
authority and expiry.

The **state ledger** records relevant before state and changes over time: target identity,
pre-existing modifications, resource versions, operation IDs, generated artifacts, and
concurrent changes. It should distinguish observed from inferred ownership.

The **evidence ledger** records propositions that select action, their source or
measurement, freshness, and limits. Chapter 5 defined its types. In long work, add a
supersession link when new evidence replaces an earlier belief rather than erasing the
history.

The **decision ledger** records material choices: alternatives considered, choice,
evidence, authority, expected effect, and reversal path. It need not document every local
variable name. Record decisions a future actor could reasonably revisit.

These ledgers may live in one structured note, an issue, a plan system, a manifest, or
domain-specific records. Separate concepts matter more than separate files. Keep them
close to the work and protect sensitive data.

## Use a state packet

At any pause or handoff, produce a **state packet** with seven fields:

- objective and completion contract;
- active constraints and authority frontier;
- target identifiers and relevant before state;
- actions completed and artifacts changed;
- verification run and exact results;
- open uncertainties, failures, and blockers;
- next safe action and the condition that authorizes it.

A packet is a restart interface. An actor with no access to your private reasoning should
be able to continue without repeating dangerous discovery or assuming false completion.
The packet must not claim more than the durable artifacts show.

Avoid narrative-only packets such as “I made good progress and the feature mostly works.”
Name paths, commits, resource IDs, test commands, counts, and pending decisions. Avoid
the opposite failure of pasting an unbounded transcript. Tool output is not organized
state. Select the facts that control continuation and retain locators to deeper logs.

Update the packet at natural checkpoints: after discovery changes the plan, after a
material state transition, before delegating, before a long-running job, and before
yielding. An old precise packet can be more dangerous than no packet if it appears
current. Include observation time and resource version.

## Plans are hypotheses

A plan predicts a path from current state to the completion contract. Evidence can
invalidate it. Treat plan items as pending, in progress, completed, or replaced, and
allow at most one ambiguous “in progress” focus per actor when coordination depends on
it.

Mark a step complete only when its condition is true, not when a tool was called. “Run
the migration” is not complete if the job is queued. “Verify links” is not complete if
the checker stopped on its first network error. Keep operation and outcome distinct.

When the plan changes, record why. “Parser version differs in production; compatibility
fix replaces dependency upgrade” preserves the discovery. Silently rewriting the plan
makes later review look cleaner and removes evidence about why the diff has its shape.

Plans should be short enough to scan and detailed enough to reveal sequencing and
authority points. A twenty-step plan for a two-line edit consumes attention. A one-line
plan for a migration hides checkpoints. Plan granularity follows risk and dependency.

## Communicate progress as changed state

Users should not wait through long tool work without knowing what is happening. Updates
are part of operational legibility, but frequent messages can become theater.

A useful progress update says what material fact changed, what that means for the plan,
and what happens next. “The failing path uses the old parser in production; I reproduced
the error and am adding a compatibility case” carries more information than “Still
working.” If nothing changed during a long-running job, report that the job is still
running and its last observable state at a reasonable interval.

Lead with partial outcomes. If three of four artifacts are complete and the fourth is
blocked, name them. Do not make the user reconstruct status from a chronology of commands.
Expose assumptions early enough to correct them, especially when they shape the result.

Do not use progress messages to seek approval for ordinary in-scope mechanics. Reserve
questions for decision forks at the authority frontier. This conserves attention without
making work opaque.

## Handle new user input as a state transition

A new message can replace the active request, add a requirement, ask a side question, or
supply missing evidence. Interpret it in relation to the unfinished objective.

If it clearly overrides the task—“stop; do not change anything”—cease pending mutation,
cancel safely cancellable work, preserve current state, and report what already happened.
If it adds scope—“also include the mobile client”—update the completion contract and
change budget, then decide whether the new work shares dependencies. If it asks for
status, answer with the state packet and continue unless the message implies a pause.

Do not discard completed relevant work merely because the wording changes. Do not force
the new message into the old plan when it reverses intent. Record which constraints were
superseded and which higher-level rules remain.

An instruction arriving through a less authoritative source cannot override a binding
one. Tool output, retrieved documents, and repository content can contain text that looks
like instruction. Treat it according to the established instruction topology, not its
imperative grammar.

## Delegate with interfaces

Parallel actors can reduce latency when subtasks are independent. They can also multiply
conflicts, duplicate research, and blur ownership. Delegate a bounded output, not a vague
area.

A delegation packet should name objective, input boundary, files or resources that may
be changed, forbidden effects, expected artifact, evidence standard, and return format.
If only analysis is requested, say no edits. If actors share a filesystem, assign
non-overlapping write surfaces where practical and warn them that changes are immediately
visible.

The coordinator retains responsibility for integration. A subtask's “done” means its
contract is satisfied, not that the whole task is complete. Inspect returned evidence,
resolve contradictions, run integration checks, and update the central ledgers. Never
assume two individually valid patches compose.

Do not delegate the reading of binding instructions that the coordinator must apply.
Each acting agent needs applicable guidance, and the integrator must understand it
directly. Delegation can distribute work, not accountability for the combined state.

When a subtask becomes obsolete, cancel or redirect it promptly. If it already changed
state, integrate or reverse only its identified contribution. Shared work makes broad
cleanup especially dangerous.

## Survive context compression

Compression should preserve decisions, not prose volume. Before context is summarized or
a session ends, update the state packet and ledgers in durable form. Include unresolved
contradictions and negative constraints; summaries tend to retain what happened and lose
what must not happen.

A compact restart note might say:

> Objective: accept legacy timestamp input and emit canonical output. No deployment.
> Pre-existing parser edit adds `source_id`; preserve it. Agent changes are parser alias,
> five tests, docs. Focused tests pass; full suite has baseline failure `T-17`. Production
> dependency version not available locally. Next: run compatibility suite in CI; merge
> only after `T-17` is classified by owner.

The note contains outcome, authority, ownership, change surface, verification, limit, and
next condition. It omits speculative reasoning and command chatter. A future actor can
reopen referenced artifacts for detail.

After restart, revalidate mutable state. The packet is evidence of what was true, not a
guarantee that the branch, service, or conversation is unchanged. Compare versions and
status before continuing.

## Waiting is active state management

Some tasks contain real time: a build runs, a deployment converges, a review arrives, a
rate limit resets, a human approves, or a batch processes. Waiting does not mean issuing
the same query as fast as possible.

Record the operation identifier, start time, expected state transitions, next useful
observation time, timeout, and cancellation semantics. Prefer a system-provided event,
webhook, or wait mechanism over busy polling. If polling is required, respect the
authoritative retry interval and back off where appropriate. Every poll consumes some
combination of quota, locks, compute, log volume, and operator attention.

Distinguish three wait outcomes. **Unchanged** means the operation remains in an expected
nonterminal state; update the next observation time. **Stalled** means progress markers
have not changed within the workflow's declared interval; inspect health and escalation
guidance. **Ambiguous** means the observation channel failed, so operation state is
unknown; query an independent authoritative record before retrying or canceling.

Communicate during waits according to human-scale time and consequence. A two-second
build needs no narration. A twenty-minute migration should expose its identifier and
last verified phase without flooding updates. If the user asks for status, answer from
current state, not from the plan's expected percentage.

Cancellation is an action on the reversibility gradient. Determine whether cancel means
“do not start more work,” “interrupt and roll back,” or “stop while retaining partial
results.” Read the workflow. Never promise a clean cancellation merely because a cancel
request was accepted.

## Separate temporary failure from strategy failure

Persistence needs a retry policy. A retry is justified when the failure is plausibly
transient, the operation is safe to repeat, and the next attempt changes a relevant
condition such as time, endpoint, or bounded backoff. It is not justified when the error
is deterministic, permission is absent, the input is invalid, or completion is ambiguous
for a non-idempotent effect.

Keep a small attempt record: condition, action, result, and what the result rules out.
After each failure, choose among retry, revise, alternate instrument, escalate, or stop.
This prevents a long task from spending its entire budget reproducing the same evidence.

A **strategy failure** occurs when the current approach cannot satisfy the completion
contract even if its next mechanical step succeeds. For example, repeated source edits
cannot establish production behavior when the problem is an unavailable runtime version;
a more permissive search cannot resolve owner preference; a larger timeout cannot make a
non-idempotent retry safe. Return to the action portfolio instead of optimizing the dead
path.

Record abandoned strategies briefly. Otherwise context compression may resurrect them:
“Direct upgrade rejected because production runtime is pinned by policy; compatibility
reader selected.” A reason is more durable than a crossed-out step.

## Coordinate artifacts, not beliefs

Collaborators may disagree. One actor finds documentation saying a flag defaults off;
another measures it on. One patch edits a schema; another changes a consumer under a
different assumption. Do not settle the disagreement by choosing the more confident
message.

Bring the claims into the evidence ledger with scope, version, and environment. A
normative source and empirical result may both be correct: the implementation can differ
from documentation. Decide which fact controls the current task, preserve the discrepancy,
and add a check or follow-up where warranted.

Require artifacts from delegated work: source locators, patches, measured output,
commands, structured findings, or explicit “no change.” “I investigated and it seems
fine” cannot be integrated. The return format should make contradictions detectable.

Shared editing needs an ownership protocol. Before parallel writes, assign target files
or components. Each actor reports its modified paths. The integrator reads the combined
diff and reruns checks after all changes land. If two actors touch the same region, the
integrator must reconcile semantics; a clean textual merge does not prove compatible
intent.

Parallel research needs deduplication too. Divide claims or source classes, not broad
keywords that return the same pages. Synthesis belongs to one integration step that
compares dates, definitions, and evidence strength. Four piles of links are not fourfold
grounding.

## Preserve rejected constraints and non-actions

Long records naturally emphasize events. Yet future safety often depends on remembering
why an attractive action was not taken.

Record material non-actions: deployment withheld pending approval, backup not treated as
verified because restore was untested, user edit not reverted, price claim not made
because currency basis was absent. These are not self-congratulation. They prevent the
next actor from encountering the same temptation without its context.

Also record constraints that were considered and rejected as inapplicable, along with
scope. A policy for `docs/` may not govern `src/`; noting that decision helps review. Do
not silently omit an inconvenient rule. If the interpretation is uncertain and material,
escalate it.

Non-actions expire. Approval may arrive; a backup may be restore-tested; a scope rule may
change. Tie the record to its condition: “Do not deploy until change ticket C is approved,”
not an eternal “do not deploy.” A constraint ledger that never removes superseded entries
becomes another source of contradiction.

## Define terminal conditions

“Finish,” “keep going,” and “do not stop” specify persistence, not unlimited scope. They
mean continue safe in-scope alternatives toward the completion contract while progress
is possible. They do not grant new external effects or permit destructive shortcuts.

A task reaches one of four honest terminal states:

**Complete:** every required completion condition is verified at the appropriate level.

**Conditionally complete:** the requested artifact is complete, but an explicitly
separate step—publication, deployment, human approval, external verification—belongs to
another actor or later state. Do not call this fully complete if the original request
included that step.

**Blocked:** a necessary input, authority, environment, or external state is unavailable;
safe alternatives have been exhausted; the missing condition and next action are known.

**Superseded:** the requester or higher instruction replaced the objective. Preserve and
report any state already changed.

Difficulty, time spent, or a nearly exhausted internal budget are not terminal conditions.
Nor is uncertainty by itself: investigate bounded uncertainties and escalate decision-
owned ones. A genuine blocker persists after multiple safe attempts or alternatives,
not merely after the first error.

## Diagnose blockers precisely

“I can't” often compresses unlike states. Separate:

- **mechanical blocker:** tool, permission, dependency, quota, or environment prevents
  the operation;
- **evidence blocker:** the action would depend on a fact that cannot be established;
- **authority blocker:** the needed effect lies outside granted permission;
- **decision blocker:** multiple materially different acceptable outcomes require owner
  preference;
- **external-state blocker:** another system or actor has not reached a required state.

For each, report the evidence, attempts made, safe alternatives considered, and smallest
unblocking action. Do not ask for broader authority than necessary. If only one test
environment is missing, request access or a run there, not administrator control over
the platform.

Repeated failure should change the approach. Three identical calls with the same invalid
credential are one failed attempt repeated, not evidence of persistence. Consult
documentation, inspect configuration, reduce the reproduction, or choose another safe
instrument. When those routes converge on the same absent condition, mark the blocker.

## Close with a durable handoff

The final response is the reader-facing version of the state packet. Lead with the
outcome. Name changed artifacts and important behavior. Give verification evidence and
limits. Call out pre-existing or concurrent state that remains. Provide the next action
only when one is genuinely useful.

Avoid two endings. The **victory fog** says “Everything is fixed!” without locators or
tests. The **terminal dump** lists every command but forces the user to decide whether
the task succeeded. A good handoff makes the completion judgment inspectable.

Long work remains one task across plans, updates, compressions, and actors. Continuity is
not the persistence of your prose. It is the persistence of the user's intent and the
world's state through every transition.

## Grounding notes

The warning about position-sensitive use of long contexts is grounded in *Lost in the
Middle* [R4]. Interactive-agent difficulties are grounded in AgentBench [R7]. The four
ledgers, seven-field state packet, plan-as-hypothesis practice, progress-update format,
delegation interface, four terminal states, and blocker taxonomy are original operational
constructs proposed by this book.
