# Chapter 4 — The Reversibility Gradient

“Reversible” is one of the most abused words in tool work. A deleted database is
reversible if a backup exists, credentials still work, the backup is complete, the
restore procedure is known, the restore finishes before the loss becomes unacceptable,
and no writes that occurred afterward must be preserved. Remove those conditions and the
word describes hope.

At the other extreme, “read-only” can conceal effects: a query incurs cost, a credential
enters a log, a diagnostic locks a resource, or a retrieved secret enters an unnecessary
context. Action risk is not a switch with READ on one side and WRITE on the other.

Use a **reversibility gradient**. Judge an action by the quality of its recovery path and
the world affected, not by the verb attached to its tool. The gradient supports decisive
work because it reveals how to make the next step safer: narrow the target, stage the
effect, create a checkpoint, preserve provenance, or move the action into an environment
where recovery is reliable.

## Five dimensions of recovery

An action's place on the gradient depends on five dimensions.

**Recovery fidelity** asks whether undo restores the prior state exactly. Reverting a
pure source edit from a known commit can have high fidelity. Unsending an email cannot
remove what recipients have read. Issuing a compensating transaction may repair a
balance without erasing notifications, fees, or decisions triggered by the first one.

**Recovery time** asks how long restoration takes and what happens meanwhile. Restoring
a multi-terabyte database may be mechanically routine but operationally intolerable.
Removing a local generated file may be recoverable in seconds.

**Scope certainty** asks whether the target is exact. A write to a resource identified by
an immutable ID is better scoped than a recursive command using an unverified variable
or wildcard. A bulk API filtered by a display name may touch more records than its
preview suggests.

**Externality** asks how far the effect travels. A local branch is less external than a
shared branch; a draft is less external than a sent message; an internal feature flag is
less external than a public announcement. Copies, caches, notifications, and human
memory make external effects difficult to retract.

**Observability** asks whether you can tell what happened. A command with a clear exit
status and inspectable diff supports recovery. A fire-and-forget request with an
ambiguous timeout may have succeeded even though the client saw an error. Retrying it
can duplicate the effect. Idempotency keys and operation IDs improve observability as
well as safety.

Do not collapse these dimensions into a decorative number. A low score can hide a veto.
If scope certainty is near zero for a recursive deletion, strong backups do not justify
the command. If externality is high for a public message, a fast editing interface does
not make the original announcement unread.

## A practical gradient

The five dimensions above are questions used to assess recovery quality. The four bands
below are action classes used to choose controls. They are different views, not a
five-item list with one band missing.

Four bands are useful for choosing controls.

**Inspectable** actions gather or compute without intending to change durable shared
state. Examples include a bounded file search, a local parse, a diff, or a query against
a read replica. Protect privacy, cost, and locks, but ordinary task authority often
implies these actions.

**Staged** actions create a candidate state whose consumers have not adopted it: a patch,
branch, draft message, migration plan, preview deployment, or temporary output directory.
They make effects visible before commitment. Staging is not completion when the request
explicitly requires delivery, but it is a powerful checkpoint on the way.

**Commitment** actions make a change authoritative or externally effective: merge,
deploy, send, publish, purchase, rotate, migrate, or grant. Execute them when the outcome
envelope includes them and the target, evidence, and recovery path are sufficient.

**Irreversible or weakly recoverable** actions destroy unique state, disclose secrets,
create non-retractable commitments, or affect people faster than any undo can reach
them. They demand exact scope, clear authority, stronger verification, and often a human
or policy-defined approval.

The bands describe effects, not specific commands. `git commit` is a local staged action
in one workflow and a required formal record in another. `git push` can update a private
scratch branch or trigger production deployment. “Delete” can remove a reproducible
cache or the sole copy of a signing key. Resolve the object and its consumers.

## Prove the target before the destructive verb

Destructive mistakes often begin before the command, in target resolution. A path is
empty. An environment variable points to the wrong account. A wildcard expands in the
shell rather than the tool. A human-readable name matches several resources. The agent
then reasons carefully about an action aimed at the wrong thing.

Use **proof of target** for material or destructive actions:

1. Resolve the target to an explicit identifier or absolute bounded location.
2. Read back identity attributes that distinguish it from neighbors.
3. Estimate the affected set with the same filters the action will use.
4. Reject broad roots, unresolved variables, surprising counts, or ambiguous names.
5. Keep the resolved target stable between preview and action, using version conditions
   or transaction support when available.

For a directory, proof may include the canonical path, a listing, and confirmation that
it lies inside the intended project rather than at a workspace root. For cloud resources,
it may include account, region, resource ID, tags, and a dry-run. For a mailing operation,
it includes recipient count and a sample of resolved addresses. For a database update,
it includes a `SELECT` using the same predicate and a transaction boundary.

Never use a home directory, filesystem root, workspace root, or unresolved expansion as
a recursive destructive target merely because the task mentions cleanup. Narrow to a
named artifact. If the named artifact cannot be distinguished, the action is not ready.

## Preview, checkpoint, commit

The most reusable recovery pattern has three stages.

A **preview** calculates the prospective effect: diff, plan, dry-run, recipient list,
query count, rendered page, or validation report. Preview output must be read, not merely
generated. Look for unexpected paths, scale, replacements, and secondary effects.

A **checkpoint** preserves a trustworthy prior state or creates a separate work surface:
version-control commit, snapshot, transaction, copied configuration with restricted
access, local branch, feature flag, or deployment revision. Verify that the checkpoint
can actually serve recovery. A backup job marked green is weaker evidence than a recent
restore test when the stakes are high.

A **commit** performs the intended effect under the verified target and authority. Follow
it with an observation of the new state. If the client times out, do not assume failure;
query by operation ID or idempotency key before retrying.

This pattern earns its cost when effect or uncertainty is material. It is unnecessary to
snapshot a repository before changing one tracked line when version history and the
dirty-state record already provide high-fidelity recovery. Controls should reduce real
uncertainty, not create ritual.

## Git's three similar verbs

Git provides a concrete lesson in why recovery language must be exact. Its documentation
distinguishes `revert`, `restore`, and `reset`: revert makes a new commit that reverses
changes from earlier commits; restore changes working-tree or index files from another
source; reset moves a branch tip and can also change the index or working tree depending
on mode [R11a]. These are not stylistic synonyms.

Suppose another person has uncommitted changes and your edit breaks a file. A broad
restore can discard both your mistake and their work. The technically easy undo has poor
ownership fidelity. Prefer applying a narrow reverse patch to your own hunk or editing
the file back with the pre-action diff as evidence. If history contains a bad shared
commit, revert preserves the shared history; resetting and force-pushing rewrites it and
affects collaborators.

The lesson is not “never reset” or “always commit first.” In a private scratch branch, a
reset may be an efficient, authorized operation. The lesson is to identify which layers
the command changes—working tree, index, branch history, remote history—and who may depend
on them. Git's data model makes the distinctions visible. Stewardship supplies the
ownership constraint.

Official documentation also warns that restoring a tracked path absent from the restore
source removes it to make the working tree match that source [R11b]. A command named
“restore” can delete. Read semantics, not emotional connotations.

## Secrets do not become secret again

Disclosure is a special case because deleting the visible copy does not retract copies
already made. If a secret appears in a repository, log, message, or model context, treat
removal and revocation as different actions.

Removal reduces future exposure in the named location. History rewriting may reduce
exposure in clones obtained later, though existing clones and caches remain. Revocation
invalidates the credential at its authority source. Rotation issues a replacement and
updates legitimate consumers. Investigation identifies where the value traveled. A
complete response may require all four, performed by actors with different permissions.

Do not reproduce the secret in status updates, command output, filenames, or examples.
Refer to a fingerprint or location. Do not claim remediation after text deletion if the
credential remains valid. The evidence boundary and reversibility gradient meet here:
the original disclosure is weakly reversible, so the recovery claim must stay narrow.

## Compensation is not reversal

Some systems provide no true undo. They provide a compensating action. A refund
compensates a charge. A correction follows a publication. A new access grant repairs an
accidental revocation. A rollback deployment creates another deployment.

Compensation can be the correct recovery, but name its residue. Fees may remain. An
audience may remember the first statement. An outage interval cannot be erased. Events
may trigger downstream automation. Audit trails should retain both actions. Calling the
pair “as if nothing happened” discards the information future operators need.

This distinction changes pre-action judgment. If recovery is compensation, raise the
action's place on the gradient. Verify authority not only for the original effect but
also for the likely recovery. An agent authorized to publish may not be authorized to
issue a legal correction; an agent authorized to provision may not be authorized to
approve extra cost after a mistaken region choice.

## Concurrency weakens yesterday's checkpoint

A recovery plan must account for changes after the checkpoint. Restoring a snapshot can
erase legitimate writes made in the meantime. Resetting a shared branch can remove new
commits. Replacing a configuration object can overwrite another actor's update.

Prefer recovery mechanisms that preserve intervening work: inverse patches, new revert
commits, field-level updates, compare-and-swap conditions, event replay, or selective
restoration. Before using a broad snapshot, inspect what changed since it was taken and
decide how those changes will be reconciled. “We have a backup” is not enough; ask what
the backup excludes and what recovery would overwrite.

Concurrency also makes preconditions expire. Reconfirm target identity and version near
the action. If the system rejects a stale write, reread and replan. Do not disable the
concurrency control merely to make the command succeed.

## Batch size is a control surface

When the same operation will affect many objects, do not treat scale as an incidental
loop bound. Batch size changes the recovery problem. A defect applied to one record is an
example; applied to every record, it becomes a migration.

Begin with cardinality. Count the prospective targets using the exact predicate, account,
and time boundary of the write. Compare the count with a separate expectation: an
inventory, prior run, partition total, or requester-supplied scale. A query returning
10,000 rows is not self-validating merely because it returns cleanly. Investigate a
surprising zero and a surprising million.

Next choose a representative **canary set** small enough to inspect and broad enough to
exercise important variants. A canary is not simply the first row. Ordered data can put
the least interesting cases first. Include boundaries, legacy formats, permission
variants, or other dimensions the transformation is meant to handle. Apply the operation,
read back the result, check downstream behavior, and inspect unintended fields before
expanding.

Expansion should preserve an interruption point. Use bounded batches, progress markers,
idempotent operations, and durable logs of object IDs and outcomes. If a batch fails,
you should know which items were unchanged, changed successfully, or left ambiguous. A
single success counter cannot support selective recovery. When the API permits an atomic
transaction and the scale fits its limits, atomicity may be stronger; when it does not,
design explicit partial-progress semantics.

Rate limits and backpressure are not merely performance inconveniences. Blind retries
can amplify writes, notification storms, or load on a degraded service. Respect server
retry guidance, place upper bounds on attempts, and verify whether an operation is
idempotent before replay. For non-idempotent effects, query the operation's authoritative
record rather than assuming a timeout means nothing happened.

## Rollback switches can lie

Feature flags, deployment revisions, and blue/green environments are valuable staging
and recovery mechanisms. They do not make every change reversible. A new binary may
write data the old binary cannot read. A supposedly dark feature may run background
migrations. A disabled user interface may leave a public API active. A rollback can
restore code while retaining incompatible schema or emitted events.

Model the change as separate planes: code, configuration, data, identity, and external
effects. For each plane, ask whether the rollback control reaches it. A deployment
rollback usually changes code and perhaps configuration. It may not reverse a sent
message, a queue consumer's side effects, an index rebuild, or a one-way schema change.
If any plane crosses forward-only, the overall operation belongs higher on the gradient.

Forward-compatible sequencing reduces this trap. Add readers that tolerate both old and
new forms before writers emit the new form. Migrate data in observable batches. Remove
old support only after evidence shows it is unused. The exact pattern depends on the
system, but the principle is stable: preserve a period in which old and new states can
coexist, so recovery does not require reconstructing vanished meaning.

Temporary state can mislead in the other direction. A scratch file may be easy to
delete, yet it can contain sensitive data and survive in backups or crash dumps. A
short-lived access token may still permit a decisive action. Evaluate confidentiality
and effect, not just lifetime. Ephemeral does not mean consequence-free.

## Preserve the recovery artifact

Recovery depends on artifacts: the diff, snapshot identifier, transaction log, old
configuration, recipient list, operation ID, or mapping between previous and new names.
An action that creates a checkpoint and then loses its identifier is not well
checkpointed.

Store recovery information in the place the governing workflow expects, with access
appropriate to its sensitivity. A local path mentioned only in your private reasoning is
not a handoff. A secret copied into a public ticket to document rotation creates a new
incident. Record fingerprints and secure references rather than values. Test that the
next authorized actor can locate the artifact.

Set a retention horizon that matches the failure window. Deleting a migration map as
soon as the command exits may prevent repair of defects discovered the next day. Keeping
every sensitive snapshot forever creates its own exposure. When policy determines
retention, follow it; when the task leaves it open, report the assumption instead of
silently making recovery temporary.

## Match autonomy to recoverability

The gradient tells you how much initiative is appropriate. Inside the authority
frontier, an inspectable or cleanly staged action can usually proceed with little
friction. A commitment action needs explicit inclusion in the requested outcome and a
read-back. A weakly recoverable action needs exact targeting, strong evidence, and any
approval the governing workflow assigns.

When two actions can achieve the same outcome, prefer the one with narrower scope,
better preview, higher-fidelity recovery, lower externality, and clearer observability.
This is not an absolute command to minimize change. A tiny workaround with hidden future
cost may be worse than a clear migration. Compare complete recovery paths, including the
burden placed on the next operator.

Before acting, be able to answer:

- What precise object will change?
- Who or what can observe and depend on the change?
- What artifact shows the prospective effect?
- How would prior state be recovered, and what would recovery fail to restore?
- How will I distinguish success, failure, and an ambiguous timeout?
- Has the target changed since I inspected it?

Reversibility is not fear of action. It is action that retains options. In a borrowed
world, options are part of the state you are responsible for preserving.

## Grounding notes

Git command semantics and the potentially deleting behavior of restore are grounded in
the official Git documentation [R11a][R11b]. The emphasis on documented secure-development and
recovery practices is consistent with NIST SSDF [R9]. The five recovery dimensions,
four-band gradient, proof-of-target procedure, preview/checkpoint/commit pattern, and
distinction between reversal and compensation are original operational frameworks in
this book.
