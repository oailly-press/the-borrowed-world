# Chapter 7 — Verification Is an Action

An edit is an intention. A tool call is an attempt. Neither is the resulting world.

Verification closes that distance by observing state after action and comparing it with
the completion contract. This sounds obvious, yet many agent reports substitute one of
three weaker facts: the command was issued, the changed text looks plausible, or no error
was noticed. A world can reject a request, apply only part of it, accept it under a
different identity, or change again before the report.

Verification is itself an action with scope, cost, side effects, and limits. A complete
test suite may consume hours, alter fixtures, call external services, or fail for unrelated
reasons. A single focused test may miss integration faults. The task is not to maximize
testing. It is to assemble enough independent evidence for the claim you intend to make.

## Derive checks from claims

Start with the completion contract. For each condition, name an observation that could
confirm it and an observation that could refute it. This produces a **claim-check map**.

If the claim is “the parser accepts legacy input,” a positive fixture can confirm one
example; malformed and ambiguous fixtures probe the boundary. If the claim is “the file
was published,” a local rendering is insufficient; read back the public artifact or
publication record. If the claim is “only these records changed,” compare identifiers
and unexpected fields before and after. If the claim is “the message was sent once,”
inspect the authoritative sent record and recipient set, not merely the client response.

Design checks before or alongside implementation when possible. Doing so reduces the
temptation to choose a test that the current output already passes. A regression check
should fail for the observed defect under the old behavior and pass for the reason the
fix addresses. If you never observed that contrast, say what the test establishes rather
than claiming it reproduces history.

Verification includes **negative checks**: what must not have changed? Pre-existing
files, public interfaces, recipient groups, permissions, unrelated totals, and external
systems may form the preservation side of the contract. A green positive result can
coexist with collateral damage.

## Use independent layers

Different checks catch different defects. A strong verification portfolio often moves
through these layers.

**Structural checks** establish form: parsing, schema validation, type checking, linting,
link resolution, manifest consistency, or required fields. They are fast and precise but
do not prove behavioral outcome.

**Focused behavioral checks** exercise the changed mechanism and its boundary cases.
They provide a tight relation between defect and fix and are usually the first useful
feedback after an edit.

**Integration checks** exercise neighboring components through their real interface.
They detect wrong assumptions about serialization, dependencies, configuration, or
callers.

**System or workflow checks** run a representative end-to-end path in an appropriate
environment. They provide broader evidence at higher cost and often lower diagnostic
specificity.

**Authoritative read-back** observes the durable or external state the user actually
cares about: deployed revision, published page, sent message, database value, generated
artifact, or signed record.

**Regression-boundary checks** inspect unrelated state expected to remain unchanged:
working-tree diff, resource count, permission set, performance budget, or existing suite.

Layers should be independent enough that one mistaken assumption does not make all of
them green. Running the same function twice with the same input is repetition, not a new
layer. A generated file compared against the generator that produced it may need an
independent parser or golden property.

## Match breadth to risk and surface

Use **proportional verification**. Breadth grows with effect surface, novelty, coupling,
irreversibility, and consequence.

A documentation typo may need rendering and link checks. A local pure function change
needs focused cases and relevant callers. A dependency upgrade needs lock inspection,
build, focused behavior, and a broader suite. A schema migration needs canary data,
compatibility checks, counts, downstream observation, and recovery readiness. A public
message needs content, audience, approval, send-state, and representation checks—not a
unit test.

Risk does not always correlate with diff size. One policy character can change access
for an organization. A thousand-line generated update may be low risk if its source and
reproducible process are well controlled. Verify semantic effect.

Time pressure can reduce breadth but should not erase truth. Run the highest-value checks,
state which were omitted, and avoid a stronger completion claim than the evidence. If an
omitted check is essential at the consequence level, the state is not complete; hand off
or obtain authority for the needed environment.

## Read failures as evidence

A failing verification does not always refute the change. It can reveal a pre-existing
failure, environment mismatch, flaky test, stale fixture, missing dependency, or broader
regression. Classify before repairing.

Record whether the same check failed on the pre-action baseline when that comparison is
safe and feasible. A baseline failure predating your edit remains relevant because it
may block full verification, but do not assign it to your change without evidence. A new
failure in a touched dependency is presumptively related until investigated.

Do not rerun nondeterministic checks until they pass and report only the green run. Record
the sequence and estimate variability through repeated runs when it affects the claim.
If a test is known flaky, link the evidence and still determine whether your change
increases its failure rate. “Flaky” is a hypothesis, not a disposal category.

When a verification tool fails mechanically—out of disk, permission denied, missing
runtime—separate **test result** from **test execution**. A suite that did not execute did
not pass or fail its assertions. Repair the environment inside scope, choose an alternate
valid check, or report the limit.

## Test the test

Verification code can be wrong. A test may never reach the changed path, assert a
constant, catch the wrong exception, omit a required await, reuse cached state, or pass
because no cases were collected. Inspect collection counts, relevant assertions, and
failure behavior.

For a regression, one strong method is mutation: temporarily restore the old defective
behavior or introduce the specific fault and confirm the new test fails. Perform this in
a controlled local state, then remove the mutation and inspect the final diff. If
temporary mutation could disturb shared work, use a separate worktree, scratch copy, or
test double.

Property checks can complement examples. A delimiter parser might preserve a round-trip
property; a migration might preserve record count and key uniqueness; a permission
change might assert that no additional principal gains access. Properties widen coverage
but can encode the same mistaken model as implementation. Combine them with concrete
cases derived from the observed defect.

For model-judged output, separate generation from scoring where possible. A judge prompt
should not reward vocabulary unique to the treatment. Structured action choices and
deterministic rules reduce, but do not eliminate, evaluator bias. Human review or blinded
comparison may be required for nuance.

## Environment parity is a claim

“Works locally” is precise when local behavior is the requested outcome. It is incomplete
when the target is a different runtime.

Record the dimensions that could change behavior: operating system, architecture,
runtime and dependency versions, configuration, feature flags, credentials, network,
data shape, locale, time zone, and concurrency. You rarely need perfect duplication.
You need parity on dimensions causal to the feature.

If production uses an older parser, testing only the upgraded development environment
misses the defect. If an API sandbox suppresses notifications, it cannot verify recipient
experience. If a fixture contains ten rows, it cannot establish batch behavior at a
million rows. State the tested environment and the inference to target.

NIST SSDF treats verification and release integrity as integrated development practices,
not an afterthought [R9]. The framework is broader than this book's task-level method,
but it supports the principle that development evidence should be planned and retained.

## Verify external effects twice

External systems often separate request acceptance from state convergence. A deployment
API can accept a job that later fails. A publication endpoint can return success before
caches update. A message service can enqueue but bounce recipients. A permission change
can propagate asynchronously.

Use two observations:

1. **Operation verification:** the system accepted a uniquely identified operation with
   the intended parameters.
2. **State verification:** the authoritative target reached the desired state, or its
   convergence status is known.

If the task requires user-visible availability, inspect through the user path rather
than only the control plane. Check the intended identity and location; seeing a page from
a local cache or authenticated admin session may not establish public access.

Define a bounded convergence interval. Polling without a stop condition can consume
resources and hide a stuck operation. Respect system-provided retry intervals. On
timeout, report the operation ID and last observed state; do not declare failure if
completion remains ambiguous.

## Verify the diff, not only the behavior

After tests pass, inspect the final change surface. Build tools, formatters, generators,
and tests can alter files. External operations can touch metadata or related resources.

Compare final state with the change budget and before snapshot. For code, review each
diff hunk, untracked path, mode change, and relevant generated artifact. Look for secrets,
debug output, temporary bypasses, commented-out checks, absolute paths, environment-
specific values, and accidental ownership changes. For data, compare field-level and
count deltas. For communications, compare final text and recipients with approved draft.

This review is not redundant with behavioral tests. A suite may ignore an accidentally
committed credential. A report may calculate correct totals while containing hidden
source data. A deployment may work while enabling a debug endpoint. Verification must
cover both outcome and artifact hygiene.

## When no test exists

Absence of an automated test does not make verification optional. Build the strongest
available evidence and label it.

For a visual change, render at representative dimensions, inspect or compare screenshots,
check structure and accessibility metadata, and exercise interaction. For a data repair,
query affected and unaffected partitions, reconcile totals, and preserve a reversible
change record. For a research synthesis, resolve every citation, trace sampled claims,
and reproduce calculations. For a process document, walk representative scenarios and
have the designated operator verify feasibility.

If a cheap durable regression check can be added, add it inside scope. Do not build a
new testing platform for a narrow task unless the completion contract requires one.
Manual evidence can be sufficient; “untested” should never mean “I looked at the text and
felt done.”

## Spend the verification budget on information

Verification has a budget: time, compute, API quota, fixture maintenance, human review,
and opportunity cost. Choose checks by expected information, not by familiarity.

A check is valuable when it can distinguish plausible states that require different
conclusions. If a type checker and compiler reject the same syntax through the same
front end, running both may add little for a one-line change. If a focused unit test and
an integration test exercise different serializers, each can expose a distinct fault.
A public read-back after deployment adds information no local suite can supply.

Order checks for fast discrimination. Begin with cheap structural checks that can reveal
obvious defects, then focused behavior, then broader and external checks. This “narrow to
broad” order saves resources when early evidence fails. It is not a rule to postpone a
critical environmental check; if the entire hypothesis depends on a production version,
verify that version before polishing local code.

Use failure impact to allocate repetitions. Deterministic parsing cases rarely benefit
from a hundred identical runs. Concurrent, stochastic, timing-sensitive, or model-based
behavior may. Record the sampling configuration and distribution. A result that appears
in nine of ten trials supports a different claim from one deterministic pass, even if
both produce a green summary icon.

Stop testing when additional checks are unlikely to change the completion judgment at
the consequence level. This is not permission to skip known required gates. It prevents
unbounded test accumulation from masquerading as care. If a release policy names a suite,
the suite is part of the contract; if it fails mechanically, the release remains
unverified.

## Security and privacy are preservation checks

A functional result can be correct while violating security or privacy constraints.
Include focused preservation questions wherever the change touches identities, data,
execution, dependencies, network boundaries, or generated output.

For identity changes, compare principals, roles, scopes, expiry, and inheritance before
and after. Verify both intended access and non-access for a representative unauthorized
principal when a safe test identity exists. Avoid using a real user's credentials merely
to demonstrate denial.

For data handling, trace sensitive fields across input, logs, errors, caches, artifacts,
and handoff. A redacted display does not prove the raw value was not written elsewhere.
Inspect configuration and representative outputs without copying secrets into the
verification record. Use synthetic data for tests when real data is unnecessary.

For command or template changes, probe boundaries where untrusted input meets interpreters:
quoting, path traversal, query parameters, markup, deserialization, and permission checks.
Do not claim a security audit from one regression case. State the property tested and
retain domain review requirements for high-consequence surfaces.

For dependencies, verify source and integrity through the ecosystem's established lock
or signature mechanism, inspect unexpected transitive changes, and run the supported
scanner or policy gate when one exists. A scanner's clean report supports only its rules,
database, and configuration; it does not establish absence of vulnerabilities.

NIST SSDF recommends integrating security practices throughout development rather than
bolting them onto the end [R9]. At task scale, this means deriving security and privacy
checks from the actual change surface. A generic “security considered” checkbox is not
evidence.

## Keep verification artifacts legible

The future reader needs enough evidence to reproduce or challenge the completion claim,
not a transcript of every terminal byte. Preserve commands or procedures, relevant
versions, result summaries, failure details, and artifact locators. Remove secrets and
irrelevant bulk output.

When a report is generated automatically, inspect it before citing its verdict. Ensure
the report corresponds to the final source state rather than an earlier run. Tie it to a
commit, content hash, resource version, or timestamp as the workflow allows. A passing
report detached from the artifact under review is provenance without identity.

Do not rewrite failed history into a perfect story. If the first test exposed a missing
case and the fix changed, that sequence can improve the handoff. Summarize the relevant
learning rather than hiding it or dumping the entire debug log. Legibility is selected
truth, not selective truth.

## A deployment case

The request is to fix a health endpoint and deploy through an authorized job. The source
change is one condition check. Focused tests cover healthy, degraded, and dependency-
unreachable states. Integration tests confirm the server maps each to the documented
status. The repository suite passes except for one baseline flaky test recorded before
the edit.

The final diff contains the handler, tests, and a generated route table. The route table
regenerates reproducibly. The authorized deployment job accepts commit `K` and returns
operation `D`. That proves submission, not availability. The job reaches healthy state;
the control plane reports revision `K`; a request through the service's consumer path
returns the correct payload. Logs show no increase in dependency calls, a preservation
condition derived from the handler design.

The final report can now say the fix was deployed and observed through the consumer path.
It should also say the broader suite contained a pre-existing flaky failure if the suite
was not wholly green. It need not narrate every passing command. It must expose evidence
that controls the completion claim.

## A verification matrix

For each task, the final private or recorded matrix should answer:

- **Requested outcome:** which observation proves it?
- **Boundary behavior:** which cases test edges and failures?
- **Integration:** which consumer or neighbor was exercised?
- **Preservation:** what evidence shows unrelated state remained intact?
- **External state:** what authoritative read-back confirms convergence?
- **Environment:** which relevant target dimensions were matched or missing?
- **Limits:** which important check could not run, and how does that narrow the claim?

Not every row needs a different tool. Every row needs a truthful answer. Verification is
complete when the evidence supports the completion contract at the task's consequence
level—not when the agent has exhausted every available test.

### Executable verification gate

Write one row for every sentence you intend to use as a completion claim:

| Proposed claim | Falsifying check | Pass evidence | Preservation check | Limit |
|---|---|---|---|---|
| fix is present in revision K | read deployed revision | control plane returns K | prior stable revision remains recoverable | none |
| consumer path works | exercise named request through consumer interface | expected response tied to K | dependency-call rate unchanged | one region sampled |
| deployment completed | query operation D and resulting service state | D accepted once; service healthy | no duplicate operation ID | broader load test not run |

A claim passes only when its falsifying check reaches the final target state and the
result is conclusive. An unrun or inconclusive check is written in the Limit column and
the claim is narrowed accordingly. If a missing check controls the requested outcome,
verification does not pass. This is the threshold: every completion-contract claim is
supported or removed; no amount of unrelated green checks can compensate for one
unsupported material claim.

## Grounding notes

Repository-level evaluation context is grounded in SWE-bench [R5]. Secure-development
verification and evidence retention are grounded at a broader process level in NIST SSDF
[R9]. The claim-check map, verification layers, proportionality rule, operation/state
double check, final change-surface review, and verification matrix are original
operational constructs proposed by this book.
