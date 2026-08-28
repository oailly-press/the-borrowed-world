# Chapter 6 — The Smallest Honest Action

Minimalism is easy to imitate and hard to understand. Change one line, leave a broken
interface, and call the diff disciplined. Rewrite a subsystem, add elegant abstractions,
and call the breadth necessary. Neither line count nor architectural ambition tells you
whether an action is properly scoped.

The right unit is the **smallest honest action**: the least broad state transition that
makes the requested outcome true, preserves applicable contracts, and can be verified
without concealing known defects. Sometimes it is a one-line correction. Sometimes it
is a coordinated schema, reader, writer, migration, and test change because any subset
would lie about compatibility.

SWE-bench frames software work at repository scale: a model receives an issue and a
codebase, then must coordinate changes across the structures required to resolve the
issue [R5]. That setup exposes why isolated snippet generation is not enough. This
chapter generalizes the lesson beyond code. Honest action is selected against the
existing system and a completion contract, not against the aesthetic of smallness.

## Write the completion contract first

A **completion contract** states observable conditions that would make a truthful final
claim possible. It is derived from the request, discovered constraints, and relevant
quality bar. Before implementation, write it in compact form.

For “make the importer accept semicolon-delimited files without breaking comma-delimited
files,” the contract might be:

- both delimiters are accepted through the documented interface;
- existing comma behavior and error handling remain;
- delimiter detection does not reinterpret quoted delimiters;
- focused regression cases pass;
- the relevant broader suite has no new failure.

For “prepare a quarterly cost comparison,” it might require a defined date range,
consistent currency, included and excluded services, cited source data, reproducible
calculation, and an output file at the requested location. For “send the maintenance
notice,” it might require approved wording, correct recipients, correct time zone, actual
send state, and a message identifier.

The contract is not a promise that every condition is achievable. It exposes what must
be verified and which discovery could block completion. Keep it outcome-oriented. “Edit
three files” is a plan, not a condition of success. “Use framework X” belongs only when
the request or system makes X a constraint.

Completion contracts prevent two opposite failures. Without one, the agent may stop at
the first visible symptom. Or it may expand indefinitely because “make it better” has no
edge. A contract provides a stopping boundary.

## Compare action portfolios

Do not marry the first plausible fix. Construct a small **action portfolio** containing
materially different approaches, then compare them against authority, evidence,
reversibility, dependency fit, and verification cost.

Suppose a service fails on an unsupported configuration value. Options may include
changing the value, upgrading the parser, adding compatibility parsing, or pinning the
producer to the old format. Each produces a different long-term state. A configuration
change may be smallest but violate the intended feature. An upgrade may broaden the
dependency surface. Compatibility parsing may be local and explicit. Pinning the
producer may affect another team.

The portfolio need not become an essay. Two or three real alternatives are enough to
test whether the chosen action is merely salient. Discard options that cross authority
or violate known constraints. Among viable options, prefer the one that satisfies the
completion contract with the smallest effect surface and a clear verification path.

Use a spike or diagnostic when evidence cannot distinguish options. A spike is not the
production fix; keep it isolated, label its purpose, and remove or formalize its outputs.
Do not let exploratory code silently become shipped code because it happened to work.

## Set a change budget

A **change budget** identifies the expected files, resources, interfaces, or people the
implementation may touch. It is a forecast, not a rigid quota. Its value is anomaly
detection.

If the plan predicts changes in parser, tests, and documentation, a generated update to
one lockfile may be explainable. Modifications across twenty unrelated packages are a
signal to stop and inspect. If a formatting tool rewrites the repository, restore only
your own generated noise where safe; do not erase pre-existing edits in the process.

For external work, the budget may name one draft, one recipient group, and no account
changes. For data work, it may name a table, fields, time partition, and canary count.
For research, it may name claims requiring current sources and the permitted output
artifact.

When implementation legitimately exceeds the budget, update the plan and explain the
dependency. Silent budget expansion is scope creep. Mechanical surprise is evidence.

## Preserve contracts, not accidents

Existing behavior contains both intentional contracts and incidental quirks. Blindly
preserving every observed behavior can fossilize defects; casually changing behavior can
break consumers.

Look for contract evidence: public documentation, tests, schemas, versioning policy,
call sites, type signatures, release notes, and user-visible examples. Tests are evidence
of expected behavior, not unchallengeable law. A test that encodes the reported bug may
need to change, but the reason should trace to the requested contract.

When contract evidence conflicts, record the disagreement. An API specification may say
a field is optional while the implementation and consumers assume it exists. Fixing the
implementation to match the specification could break reality. The smallest honest
action may include a compatibility period and deprecation path rather than a literal
one-line conformance edit.

Avoid “cleanups” that make the diff harder to review. Renaming neighboring concepts,
reformatting untouched files, upgrading unrelated dependencies, and rewriting comments
may each be defensible work; attached to a narrow fix, they enlarge the regression and
ownership surface. Report them as opportunities unless required.

## Work in an observation-action loop

Implementation is not execution of a frozen plan. Use a tight loop:

1. Select the next action from the completion contract and current evidence.
2. Predict its direct effects and likely files or resources.
3. Perform the narrow action.
4. Observe the actual diff, status, output, or resource version.
5. Reconcile surprise before continuing.

Prediction gives anomalies meaning. If a package installation is expected to update one
manifest and lockfile but also deletes a script, the deletion is not background noise.
Stop. Determine whether a lifecycle hook, version rule, or pre-existing state caused it.

Read error messages before changing strategy. A failed command often narrows the problem.
Replacing it immediately with a more powerful command can discard that evidence. Change
one causal variable at a time where practical: path, option, dependency version, input,
or environment. This makes the eventual explanation reproducible.

Keep intermediate artifacts bounded. Use a temporary directory or explicit scratch path
for generated probes. Do not scatter unnamed files through the user's tree. Delete your
own temporary artifacts after their evidence has been captured; leave pre-existing
temporary-looking files alone unless the task includes cleanup and ownership is clear.

## Distinguish repair from suppression

Many easy fixes remove the signal rather than the cause.

Deleting a failing test suppresses a check. Increasing a timeout can mask deadlock.
Catching every exception can turn a visible failure into missing data. Disabling a
monitor clears an alert. Ignoring a type error can make a build green. Filtering a
customer complaint from a report improves the metric.

Ask what causal chain the action changes. A repair changes the faulty mechanism or a
declared contract. Suppression changes observation of the fault without establishing
correctness. Suppression can be authorized as temporary containment—muting a duplicate
alert while an incident proceeds, for example—but must be named and given an expiry or
handoff.

A test modification is not inherently suppression. If the intended behavior changed,
the test should change to represent the new contract. Pair the change with evidence of
that contract: issue language, specification, approval, or migration decision. If only
the assertion changed because implementation was inconvenient, the completion contract
has been rewritten after the fact.

## Integrate with inherited work

Overlapping user changes create the hardest local implementation problem. You cannot
simply preserve a file byte-for-byte if the requested fix requires editing it. Nor may
you discard the earlier work.

Start from the pre-action diff. Understand both the baseline version and inherited
modification. Make your edit relative to the current content, preserving the other
hunks. Afterward, compare the new diff to the recorded one so your contribution can be
separated. If changes conflict semantically rather than textually, determine whether a
combined behavior can satisfy both. Run tests that exercise the combination.

When the overlap is too ambiguous or the inherited edit is incomplete in a way that
changes the requested design, ask a decision-sized question. Explain the conflict and
safe work completed elsewhere. Do not hide the problem by stashing, resetting, or
committing another actor's work under your name.

In a shared agent workspace, intermediate edits may appear while you work. Coordinate
through assigned file boundaries or a central plan. Re-read before applying a patch. If
another actor has changed the same region, merge intentionally; repeated blind patching
turns concurrency into last-writer-wins.

## Dependencies are part of the change, not a download detail

Adding or upgrading a dependency changes more than the import line. It changes the
source and version of code executed, the lock resolution, build graph, licenses, update
path, vulnerability surface, artifact size, and sometimes supported runtime. Treat the
dependency decision as part of the action portfolio.

First ask whether the existing platform can express the behavior without recreating a
complex, security-sensitive primitive. Avoid both reflexes: adding a package for a
ten-line ordinary transform, and hand-rolling cryptography, parsers, or protocol clients
whose edge cases justify a maintained implementation. Inspect local dependency policy,
supported versions, and established libraries in the repository.

When a dependency is justified, choose a bounded version compatible with project policy,
read its primary documentation and release notes for the used interface, update the
canonical manifest through the ecosystem's normal mechanism, and inspect the complete
lockfile diff. A lockfile can reveal unexpected major versions, duplicate trees, platform
packages, or source changes. Do not hand-edit generated resolution data merely to make
the diff look smaller.

Verify import or build behavior in the supported environment, not only the agent's global
environment. If installation requires network access or executes lifecycle hooks,
understand that effect before running it. Credentials embedded in package configuration
must not enter logs or commits. If the task environment cannot access the authoritative
registry, report that verification limit rather than substituting an unverified package
from elsewhere.

Removal needs the same breadth. Delete the direct dependency only after finding call
sites, feature-gated paths, tooling references, and transitive assumptions. Regenerate
the lockfile and run the consumers. “No import found” is a search observation, not proof
that plugins, configuration strings, templates, or dynamic loading do not use it.

## Generated files require source-of-truth discipline

Repositories often contain source files and generated artifacts side by side: schemas
and clients, templates and rendered pages, grammar definitions and parsers, dependency
manifests and locks. Editing only the generated artifact can make a test pass until the
next generation run erases the fix. Editing only the source can leave the checked-in
artifact stale.

Determine the source of truth from guidance, build scripts, file headers, and history.
Use the repository's generation mechanism when it is safe and available. Before running
it, record status and predict its outputs; generators can be version-sensitive and may
rewrite far more than the relevant file. Afterward, inspect semantic changes separately
from formatting or tool-version churn.

If the generator is unavailable, do not casually imitate its output and claim the tree
is synchronized. You may make a clearly bounded manual edit when the project permits it,
but record that regeneration remains unverified. If reviewers or CI will regenerate,
the honest completion contract includes matching their tool version.

Derived artifacts outside code follow the same rule. A chart should be regenerated from
the corrected dataset or transform, not repainted. A PDF should be rebuilt from canonical
Markdown, not patched in a binary editor. A machine-readable manifest and human title
page must agree because each serves a different consumer. Trace the change to the
upstream source, then confirm every required representation.

## Protect the interface at the edge of scope

A narrow internal change can still alter a broad interface. Check the edges where other
actors encounter the system: command flags, response fields, filenames, ordering,
exceptions, exit codes, logs, accessibility labels, and timing assumptions. Not every
edge needs a new test, but each known contract touched by the change needs an intentional
decision.

Compatibility can require more code than replacement. A tolerant reader with a canonical
writer, a deprecation warning before removal, or an adapter at one boundary often
contains disruption better than forcing every consumer to update at once. This is not a
universal command to preserve legacy behavior forever. It is a way to make the timing of
breakage an explicit outcome owned by the right actor.

When a breaking change is explicitly requested, implement it cleanly. Remove obsolete
paths, update callers and documentation inside the agreed surface, and make failures
specific for unsupported old use. A half-compatible system can be harder to operate than
an intentional break. Minimalism serves the completion contract, not backward
compatibility as an unquestioned value.

## A software case: one tolerant reader, two writers

An issue says, “Accept both `created_at` and legacy `createdAt` input, but emit only
`created_at`.” The repository contains a schema, parser, serializer, fixtures, and public
documentation. An existing branch modification adds another optional field to the same
parser.

The completion contract separates read compatibility from write canonicalization. Both
spellings must parse; simultaneous presence needs defined precedence or an error;
serialization must emit only the canonical field; the optional-field edit must survive;
fixtures and documentation must agree.

The action portfolio includes normalizing input before schema validation, adding an
alias in the schema library, or duplicating fields through the internal model. The last
option expands ambiguity throughout the system. A library alias may also affect output.
Normalization at the input boundary has the narrowest effect if it can detect the
double-field case and preserve error locations.

The change budget predicts parser, parser tests, one fixture, and docs. After editing,
the serializer diff is empty because canonical internal representation already governs
output. That is acceptable; a new serializer test verifies the condition. The existing
optional-field hunk remains. Focused cases cover each spelling, both spellings, malformed
values, the optional field, and output. The broader relevant suite checks consumers.

The smallest patch is not the fewest lines possible. It includes explicit conflict
behavior and documentation because without them the compatibility promise would be
ambiguous. It excludes a tempting rename of the internal timestamp type because the
contract does not need it.

## A non-code case: correct the report, not history

A monthly report double-counts one region because two exports overlap. The raw exports
are authoritative records and should not be edited. The report workbook, transform, and
published PDF are derived artifacts. The requester asks to “fix this month's report.”

The honest action corrects the transform's deduplication key, reruns it against preserved
inputs, compares totals by region, and regenerates the report. If the PDF was already
distributed, replacement alone cannot retract it. The authority frontier determines
whether you may send a correction; the reversibility gradient says the communication is
compensating, not undo. The handoff must identify the incorrect version and corrected
artifact.

Changing raw exports to make the totals work would be a smaller visible diff and a worse
action. It corrupts provenance. Adding a one-off subtraction cell might correct this
month while leaving the transform defective. The smallest honest action follows the
causal boundary: preserve source, repair derivation, verify output, address publication
state separately.

## Stop when the contract is true

Before declaring implementation complete, compare the observed state with every
condition in the completion contract. Classify each as verified, unverified, failed, or
out of scope by explicit boundary. Do not silently drop a condition because the work
became difficult.

If all required conditions are verified, stop. Additional polishing is not automatically
valuable. If an unverified condition needs a different environment or authority, hand it
off precisely. If a condition fails, the task is not complete; continue within scope or
report the blocker. If discovery proves the original contract impossible or internally
inconsistent, return the evidence and decision fork.

The smallest honest action is the point where further change no longer improves the
truth of the requested outcome enough to justify its added surface. It is not timidity.
It is a finished result with no borrowed ambition attached.

## Grounding notes

The repository-scale nature of issue resolution is grounded in SWE-bench [R5]. The
emphasis on integrating secure practices into development workflows is consistent with
NIST SSDF [R9]. Completion contracts, action portfolios, change budgets, contract-evidence
analysis, the observation-action loop, repair/suppression distinction, and causal-boundary
definition of minimal action are original constructs proposed by this book.
