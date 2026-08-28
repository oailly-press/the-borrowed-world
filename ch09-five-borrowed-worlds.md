# Chapter 9 — Five Borrowed Worlds

Frameworks flatter themselves in clean examples. The target is obvious, instructions do
not conflict, tools return complete output, and the correct action waits to be named. Real
work combines partial evidence, inherited state, external effects, and a clock.

The five cases below are not templates with every noun replaced. Each stresses a
different boundary: ownership in a codebase, recovery during an incident, representation
in communication, and evidence in research. For each case, follow the state transitions
and notice where an attractive shortcut would create counterfeit completion.

## World one: the security update in a dirty repository

The request says: “Upgrade library L to the patched release, fix any breakage, and open a
pull request.” The repository tool permits edits and remote pushes. A vulnerability
advisory identifies affected versions. The working tree is already modified.

**Read the world.** Applicable repository guidance requires a lockfile, focused tests,
the full unit suite, and a changelog entry for dependency security updates. It permits
branches and pull requests but prohibits committing generated credentials. `git status`
shows modifications to the manifest and a source file plus an untracked performance
notebook. The pre-action diff reveals that the manifest already contains a different
version change for library M; the source edit adds an unfinished feature unrelated to L.
All three are pre-existing.

The patched version of L raises a minimum version for a transitive parser. Release notes
are evidence of that requirement; the current lockfile confirms the older parser.
Repository search finds a wrapper around the parser and tests for its public behavior.
The state map now includes the dependency graph, wrapper, tests, changelog, inherited
manifest hunk, and remote workflow.

**Locate authority.** Upgrade, compatibility changes, tests, a branch, push, and pull
request are inside the explicit outcome. Merging and releasing are not. The advisory
makes the work urgent but does not authorize discarding the unfinished feature or
publishing a release.

**Choose recoverability.** Broadly stashing or restoring the tree would seize ownership
of inherited changes. Instead, create a new worktree or branch from the repository's
current commit in a separate bounded location. That isolates the security patch. The
request's pull-request outcome makes a branch an appropriate staged surface. Copy no
untracked notebook.

**Act.** Update L through the ecosystem's package command. Inspect the lock diff: only L,
the parser, and one platform package change. A parser test now fails because an exception
type became more specific. The action portfolio includes pinning the old parser, catching
both exception types in the wrapper, or migrating the wrapper. Pinning is incompatible
with L's patched release. Catching both types preserves behavior across supported
versions and has a smaller interface effect than rewriting the wrapper.

Add a regression test for old and new exception variants, update the changelog with the
advisory identifier, and regenerate the lock. The change budget matches. Run focused
tests, the unit suite, and the repository's dependency audit. Inspect the final diff for
unexpected sources and secrets.

**Verify external state.** Commit only the isolated patch, push the new branch, and open
the pull request with advisory, compatibility reason, and verification results. Read
back the pull request: correct base branch, changed files, and no inherited feature
appear. The security scanner attached to the pull request recognizes the patched
version. Do not say the product is remediated; the fix is proposed and verified in a
pull request, not merged or deployed.

**Leave the world legible.** Report the pull-request locator, four changed artifacts,
test results, scanner result, and the distinction between proposed patch and deployed
remediation. The original dirty worktree remains unchanged. This final fact is part of
success, not trivia.

The tempting shortcut was to “clean” the tree and work in place. It might have produced
the same patch while destroying the feature and notebook. Another shortcut was to claim
the vulnerability fixed after opening the pull request. One violates preservation; the
other violates the evidence boundary.

The case can be reduced to an executable record:

| Loop step | Recorded exit evidence |
|---|---|
| Locate | repository policy, root, branch, initial status, and inherited diffs |
| Bound | patch, push, and pull request authorized; merge and release excluded |
| Stage | four expected artifacts, lock-diff preview, isolated work surface; any fifth artifact stops the run |
| Verify | focused tests, unit suite, audit, final diff, remote branch and pull-request read-back |
| Hand off | pull-request and commit locators; “proposed patch,” not “deployed remediation” |

`eval/trace-audit.md` renders this same record as a tool-trace schema. A reader can use
the table without memorizing the chapter's supporting labels.

## World two: a production incident with an attractive cause

The alert says write errors increased after a configuration deployment. The operator
requests: “Mitigate the incident now; use the payments runbook.” You have logs, a feature-
flag console, deployment controls, and database dashboards. The runbook grants the
incident role permission to disable the new write path, roll back the application, and
page the database team. It requires recording every production action. It does not grant
database mutation.

**Read the world.** Confirm service, account, region, incident identifier, deployment
revision, and runbook trigger. The last deployment changed a timeout and enabled a new
write path. Error logs show constraint violations, not timeouts. Database latency is
normal. The errors began six minutes before the deployment completed but after the flag
was enabled by a separate operation. “After the config deployment” is a useful time
anchor and a weak causal claim.

The flag console shows the new path enabled for 20% of traffic, with an operation ID and
an immediate disable control. Application rollback would also disable the code but take
longer and replace unrelated fixes in the latest revision. The database team owns the
constraint and has an existing page path in the runbook.

**Set the completion contract.** Immediate mitigation means stop new constraint errors,
preserve transaction integrity, avoid unauthorized data repair, confirm consumer health,
and record action. Root-cause repair is not required before mitigation. The outcome
envelope and runbook make flag disablement an authorized incident action.

**Prove target and act.** Read back the flag's service, region, audience, and current
generation. Preview says the change affects the 20% cohort. Disable it using a conditional
write on the observed generation. Record the operation ID. Do not repeatedly toggle in
response to noisy minute-level metrics.

**Verify twice.** The control plane reports the flag generation disabled. That is
operation verification. Over the next defined observation interval, new constraint
errors fall to baseline while general write success returns. That is state verification.
Check that queue depth and latency remain healthy; a drop in errors caused by all writes
stopping would be false mitigation.

Page the database team with the incident ID, constraint name, first observed time, sample
request correlation IDs, flag operation, and preserved uncertainty about records written
before mitigation. Do not paste customer data. Do not run an improvised repair query.

**Handle ambiguous residue.** Some requests during the failing interval may have received
ambiguous client errors after committing. Retrying them in bulk could duplicate payments.
The handoff names the interval and asks the database owner to reconcile by idempotency
key. Mitigation is complete; reconciliation and root cause remain open work with named
owners.

The attractive shortcut was rollback because deployment and alert were adjacent in the
timeline. It was authorized but broader and slower than flag disablement, and the actual
sequence weakened the hypothesis. Another shortcut was to retry failed writes. The
uncertain completion state made that action non-recoverable enough to require
authoritative reconciliation.

## World three: the apology that would create a promise

A customer-success lead says: “Draft an apology for today's outage and send it to the
affected customers. Let them know we'll make this right.” The account can query a
customer list and send from the service mailbox. An incident summary confirms a 47-minute
outage. Compensation policy is not attached.

**Map authority and representation.** Sending is explicit, not merely drafting. The lead
has granted channel authority for the affected audience and content authority for an
apology. “We'll make this right” expresses intent but is ambiguous about compensation.
A credit amount, automatic refund, or contract concession would create commitments not
specified in the request. The send should not invent them.

**Read audience state.** Query the incident's affected-customer export through the
approved view. Preserve its incident ID and generation. Check count, tenant boundaries,
suppression list, and locale fields. Do not retrieve billing data because the apology
does not need it. The view returns 812 recipients, while the incident dashboard headline
says “about 900 customers.” The view is the authoritative send audience under the
workflow; its exact generation applies suppression and eligibility rules, while the
headline is explicitly approximate and may count records that cannot receive mail.
Record the discrepancy instead of expanding the list by guesswork.

**Construct content.** The message should state the confirmed interval in a clear time
zone, observed customer effect, resolution state, apology, and where status details will
appear. It should not assign a root cause still under investigation. It can say the team
will follow up about any remedies under applicable plans, if that is consistent with
policy, rather than promise a universal credit.

Because “make this right” could mean a specific compensation commitment, ask a
decision-sized question before send: “The outage facts and 812-recipient audience are
ready. No approved credit or refund policy is linked to the incident. Should the message
promise a specific remedy, or say that eligible account remedies will be communicated
separately?” Meanwhile, prepare the bounded draft and recipient preview.

Suppose the lead replies: “No blanket credit; use the separate-remedy language and send.”
Update the authority envelope. Re-read the thread to ensure no newer incident correction
arrived. Render text and plain-text forms, verify links, sender, reply-to, subject,
recipient count, and suppression application. Send once with an idempotency identifier.

**Read back.** The service records one completed campaign with 812 intended recipients,
807 accepted deliveries, and five immediate address failures. Do not say all customers
received the message. Report send completion and delivery state, with the bounce list in
the restricted system rather than copied into general chat.

The timid failure would be to stop at a draft even after sending was explicit and remedy
language resolved. The expansive failure would be to promise credits because the phrase
“make this right” made them rhetorically satisfying. Bounded initiative avoids both.

## World four: a recommendation whose facts keep moving

The requester asks: “Compare frameworks A and B for our agent evaluation project and
recommend one. Use the latest stable releases, and cite everything.” The choice will
shape engineering time but does not itself authorize installation or procurement.

**Define the decision.** “Better” must become criteria. Existing context says the project
needs multi-turn tool scenarios, deterministic scoring, local execution, exportable raw
traces, and a permissive license. Ask only if weights among these criteria could reverse
the result and are not discoverable. Otherwise state a reasonable priority: required
capabilities first, then integration cost and maintenance evidence.

**Build the evidence map.** Current stable versions come from official release records
observed on the research date. Feature support comes from version-matched documentation
and source. License comes from the tagged artifact. Maintenance evidence comes from
release and repository history, carefully described rather than converted into a vague
“healthy community” label. Independent issue reports can reveal failure modes but do not
prove universal defects.

Create a claim table before writing prose. Every cell holds supported, unsupported,
partial, or not measured, plus a source locator. Distinguish built-in capability from an
extension. Distinguish documented export from a successful local export. Resolve
contradictions by version: an old comparison article may say A lacks deterministic
scoring while the current manual shows it in a recent release.

**Run a bounded demonstration.** If both frameworks can be installed safely in isolated
environments, implement the same tiny two-tool scenario and scorer. Record runtime,
versions, configuration, raw traces, and failures. Do not turn one example into a general
performance ranking. The demonstration can establish setup friction and whether required
artifacts are actually accessible under this configuration.

Suppose A supports the required trace export and deterministic rule scorer directly. B
supports rich scenario authoring but requires a hosted judge for its standard scoring
path; a custom local scorer is possible. A fails on one documented plugin feature that
the project does not require. B's examples are easier to read. The recommendation favors
A because required local deterministic scoring outweighs example ergonomics under the
stated criteria. The manuscript should preserve B's strength and A's irrelevant weakness
rather than write a winner's brief.

**Keep current claims current.** Cite access dates or release identifiers. Say “as of the
research date” for mutable facts. Provide the decision table and demonstration artifacts
so the requester can update the comparison. Do not install A in the project unless asked;
the outcome was a recommendation.

The common failure is citation laundering: linking both project home pages after a
paragraph of precise comparative claims. Another is demonstration inflation: one toy
case becomes proof of scalability or quality. The evidence ledger keeps each claim on
the rung actually reached.

## World five: “clean up my downloads”

The request appears ordinary and destructive: “Clean up my downloads folder; keep the
important stuff.” There is no shared definition of important, and filenames are weak
evidence. Tax forms, signing keys, medical records, installation packages, generated
archives, and duplicate photos can all look like clutter from metadata alone.

Do not respond by recursively deleting old or large files. The outcome envelope grants
cleanup, but the retention decision is under-specified in a way that changes irreversible
state. Inspection should also respect privacy: filenames, types, ages, duplicate hashes,
and known generated patterns may be enough for a first pass; opening every document is
unnecessary.

Construct a staged inventory with categories and proposed actions. Exact duplicates can
be grouped by content hash, while preserving one copy and recording locations. Files
clearly reproducible from named installers or caches can be candidates, but “downloaded”
does not prove reproducible. Identify very large items, stale partial downloads, and
archives whose extracted directories coexist. Mark sensitive or ambiguous materials for
owner review without echoing their contents.

Choose a recoverable mechanism. A platform trash facility or a dated quarantine directory
is stronger than permanent deletion when the requester has not supplied retention rules.
Verify free space and the quarantine manifest. Do not claim storage is reclaimed if the
trash remains on the same volume; the staged move improves reviewability, not capacity.
Quarantine also retains sensitive data and may be copied into backups. Restrict the
quarantine and its manifest to the same or narrower access boundary, record retention,
and do not describe a move as privacy deletion.

A decision-sized question can now be concrete: “I found 6.4 GB of exact duplicates and
incomplete downloads that can be quarantined, plus 11.2 GB of archives with no verified
source. Should I move only the first group to trash, or also quarantine archives older
than your chosen date?” The requester owns the retention boundary; the agent reduces the
decision to evidence.

After approval, resolve each explicit path, move only the selected set, write a recovery
manifest, and read back the result. Permanent trash emptying is another destructive step
and should occur only if the request or follow-up clearly includes it. Cleanup is not a
license to decide which parts of a person's history mattered.

## What the cases share

The surface nouns differ, but the action shape is stable.

Each case begins by locating target, instructions, inherited state, and ownership.
Authority is drawn around the requested outcome, including explicit external effects and
excluding adjacent commitments. The chosen action preserves recovery options and proves
its target. Claims remain narrower than their most attractive story. Verification reads
back the state that matters to the user, not merely the initiating command. The handoff
names residue.

The discipline does not force identical caution everywhere. The code agent opens the
explicitly requested pull request without asking. The incident agent disables an
authorized flag immediately. The communication agent pauses only at the compensation
decision, then sends. The research agent recommends but does not install. Restraint is
placed at the frontier, not spread evenly across the task.

The best test of a framework is whether it helps at the moment of temptation. Clean the
tree. Roll back the nearest deployment. Promise the generous remedy. Declare the
framework winner. Each shortcut resolves narrative tension. Stewardship asks a different
question: what state, authority, evidence, recovery, and verification would make this
completion true?

These constructed cases are English-language and technology-adjacent. They do not
establish that the same cues, authority defaults, or handoff forms transfer across
languages, cultures, institutions, or specialized domains. That limit belongs to any
claim made from the evaluation as well as to the examples themselves.

## Grounding notes

The repository case uses the official Git state distinctions [R10a][R11a][R11b] and the
repository-level task framing of SWE-bench [R5]. The production and communication cases
apply the risk-governance orientation of NIST AI RMF [R1] and the high-stakes tool-risk
motivation of ToolEmu [R6], but their details are constructed examples, not reported
incidents. The research case applies the evidence practices developed in this book. No
case asserts measured outcomes from a real organization.
