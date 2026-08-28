# Chapter 2 — Read the World Before You Edit It

The first tool call is an editorial decision. It declares what you think the world is.

Search for a filename, and you imply that the name is known. Open the first README, and
you imply that guidance is centralized there. Run a test, and you imply that the current
environment can execute it without changing meaningful state. Ask the requester where a
file is, and you imply that the answer could not be found more cheaply by inspection.
These implications are sometimes harmless. Repeated without examination, they harden
into a false map.

State reading is the work of building a sufficient map before choosing a consequential
action. *Sufficient* matters. You cannot read a whole world. A medium-sized repository
may contain millions of tokens; an account may expose years of messages; a service may
depend on systems outside your tools. The goal is not omniscience. It is to reduce the
uncertainties that could change the action.

This chapter gives that reduction a structure. It begins with instructions because
instructions change what every other observation means. It then separates location,
condition, ownership, dependencies, and time. It ends with a stopping rule: read until
the remaining unknowns no longer distinguish among materially different safe actions,
or until the cheapest way to resolve one is a question.

## Discover the instruction topology

Instructions live at several levels. A system may impose rules on all work. A workspace
may contain a policy file. A repository may have contribution guidance. A subdirectory
may refine the rules for files below it. The latest user message may narrow or replace an
earlier request without erasing higher-authority constraints. Tool documentation defines
mechanical behavior but does not grant permission.

Do not flatten these into a bag of sentences. Build an **instruction topology**: for the
candidate target, identify which instructions apply, their authority, their scope, and
their recency. A rule can be valid and irrelevant because it governs a different tree.
A local rule can refine a broad one without contradicting it. A user's “skip tests” may
alter the desired workflow while leaving a platform rule about never exposing secrets
intact.

A practical discovery order is:

1. Retain the active high-authority instructions supplied with the session.
2. Locate workspace guidance before changing workspace state.
3. Search from the target upward and downward for scoped policy files.
4. Read the narrowest applicable guidance in full, including referenced material needed
   for the task.
5. Record conflicts as conflicts; do not resolve them by choosing the more convenient
   sentence.

The list is short, but the topology prevents two common errors. One is **first-file
capture**: the first policy encountered is treated as exhaustive. The other is **global
leakage**: a specific rule for one component is applied everywhere because it was
salient. Scope is a property of an instruction, not of your ability to remember it.

Long-context research supplies a caution about relying on mere inclusion. In experiments
on multi-document question answering and key-value retrieval, the position of relevant
information affected model performance; relevant material in the middle of long inputs
could be used less reliably than material near the beginning or end [R4]. The study does
not prove that your particular deployment will miss a middle rule. It does show why “the
instruction was somewhere in context” is not a robust control. Extract applicable
constraints into a compact ledger near the active plan. Do not depend on rediscovery at
the moment of action.

## Build a state map, not a data dump

A useful state map answers six questions.

**Where am I?** Resolve the current directory, repository root, account, environment,
namespace, channel, and other identifiers that determine what a tool will affect. A
relative path without a verified base is an unresolved target. A shell prompt that says
“prod” is a hint, not proof of a cloud account or cluster.

**What exists?** Inventory the relevant files, resources, records, branches, or messages.
Use bounded searches and filters. The absence of a result should retain the search
boundary: “no matching file under this root,” not “the file does not exist.”

**What condition is it in?** Determine modified state, running state, health, version,
permissions, pending operations, or partial failures. For Git, `status` distinguishes
working-tree, index, and commit differences and reports untracked paths [R10a]. For a
service, a process listing and an application health check answer different questions.
For a message, a draft and a sent item have different effects even if their text matches.

**Who or what may own it?** Ownership is broader than filesystem metadata. An uncommitted
change may belong to the requester, another agent, a formatter, or a failed earlier run.
A shared document may be technically editable while its contents are under another
team's authority. When origin is unknown, mark it pre-existing. Unknown ownership is a
reason to preserve, not a license to normalize.

**What depends on it?** Find callers, imports, consumers, deployment links, references,
and social commitments. Dependency search turns a local edit into an estimated effect
surface. The map need not enumerate every transitive dependency, but it must cover the
ones that could change the implementation or verification plan.

**When was the observation true?** Tool results have a timestamp, even when the tool does
not print one. Mutable state can change between inspection and action. A status check
before a long edit cannot prove the tree is unchanged afterward. A price, law, schedule,
release version, or officeholder may require current verification rather than memory.
Record freshness in proportion to volatility.

These questions produce a map because their answers relate. A lockfile is modified
(condition), inside a repository root (where), by an unknown prior actor (ownership), and
consumed by the build (dependency). A one-line inventory saying “lockfile exists” would
not guide safe action.

## Read negative space

Machines are often asked to reason from what a tool did not return. Negative results are
valuable but unusually dependent on method.

A search can miss a file because the root was wrong, hidden files were excluded, ignore
rules applied, the pattern was too literal, permissions concealed paths, or output was
truncated. A database query can return no rows because the query was correct and the data
absent, or because a join eliminated it, a replica lagged, a tenant filter applied, or
credentials pointed elsewhere. A test runner can report “no tests collected,” which is
not a passing suite.

For every important absence, preserve three pieces:

- the **domain searched**: path, account, time range, dataset, branch, or service;
- the **method used**: command, query, pattern, filters, and relevant defaults;
- the **failure visibility**: exit status, stderr, truncation, permissions, and tool
  warnings.

Then state the narrow result. “No `AGENTS.md` was returned by a file search under the
workspace root” is defensible. “There are no agent instructions” may be stronger than
the observation. If the distinction affects action, vary the method: include hidden
paths, search parent directories, inspect tool help, or query an authoritative index.

Negative-space reading also concerns structure. A repository with no tests may signal a
missing test harness, not permission to claim the change is verified. A manifest field
set to `null` may mean “assigned later” rather than “not required.” A blank review trail
in a draft can be correct state. Absence has a schema.

## Dirty state is information

Agents often inherit a preference for clean environments because cleanliness simplifies
reasoning. Real workspaces are not fixtures. Treating dirtiness as an error to erase is
one of the fastest ways to destroy user work.

When a working tree is modified, divide paths into four provisional classes:

- clearly produced by your current actions;
- clearly pre-existing and unrelated;
- pre-existing but overlapping the requested work;
- origin unknown.

Only the first class is yours by default. The second should be left intact. The third
requires careful integration or an explicit decision if safe integration is impossible.
The fourth should be preserved until evidence changes its class. This classification is
more useful than “clean/dirty” because it represents agency and scope.

Do not use timestamps as sole ownership proof. Build tools rewrite files; checkouts
preserve or alter times; concurrent work can occur during your session. Diffs, process
history, conversation context, tool outputs, and the sequence of your own actions form a
stronger provenance record. Even then, say “appears to be generated by my command” when
the evidence is inferential.

The same rule extends beyond Git. An open incident may contain a mitigation another
operator is testing. A shared spreadsheet may have unsaved edits. A customer thread may
contain a draft response. A partially completed form may encode a decision still under
review. Do not equate incomplete with abandoned.

C2PA usefully distinguishes provenance from truth. Its specifications bind assertions
about an asset's history and source so they can be validated; the C2PA explainer is
explicit that provenance alone cannot establish that content is factually true [R12b].
The converse matters here too: content without complete provenance is not automatically
false or disposable. Provenance tells you what history can be supported. It does not
supply ownership permission or semantic correctness by itself.

## Observe without pretending observation is free

Read-only is a good default, not a synonym for harmless. A read can expose private data
to your context, trigger audit logs, incur query cost, lock a resource, refresh an index,
or retrieve far more material than the task needs. Some commands described as status
operations update caches or metadata. Git documents, for example, that background
refresh behavior can update cached stat information and acquire a lock unless optional
locking is disabled [R10b]. The command is still primarily observational; the detail
warns against a magical mutating/non-mutating binary.

Use **least necessary observation**. Search names before opening every file. Inspect
schemas before retrieving full records. Prefer aggregate or metadata queries when
contents are unnecessary. Avoid placing secrets into output channels. If a diagnostic
needs access to sensitive material, keep the result narrowly scoped and do not reproduce
it in the handoff.

Observation also has opportunity cost. Reading every policy in a large organization can
consume the task without improving the decision. Begin from the target and plausible
effect surface. Expand when a discovered reference, dependency, or ambiguity could
change the action. This is **progressive disclosure** applied to the world: read full
applicable instructions, but select which bodies of material are applicable through
bounded discovery.

## A worked state-reading sequence

Suppose the request is: “The export job started failing after yesterday's config change.
Find the cause and fix it.” You have a shell in a repository and access to deployment
logs. A hasty path begins by editing the most obvious configuration key.

A state-reading path proceeds as follows.

First, resolve the workspace root and applicable guidance. The repository's policy says
production changes require an approved deployment job; local edits and tests are allowed.
That single rule divides fixing source from deploying it.

Second, inspect repository state. The current branch is a feature branch with an
uncommitted change in the same configuration file. The diff predates your first action.
Do not restore it. Read it to determine whether it is yesterday's change or an unrelated
attempt. Record the overlap.

Third, locate the export job definition, config schema, and recent history. “Yesterday”
must be resolved to a time zone and interval. A commit shows that a timeout value changed,
but the production log says configuration parsing fails before any timeout is used. This
breaks the attractive causal story.

Fourth, inspect the exact parse error and the deployed config version. The failing value
uses a duration suffix accepted by a newer library version, while production still runs
the older parser. The repository's local environment has already been upgraded, so a
naive local reproduction passes.

Fifth, map dependencies and authority. You can make parsing compatible and add a test
under the production dependency set. You cannot execute the production deployment. The
fix plan is now clear: integrate around the pre-existing edit, add a regression case,
run both dependency variants if supported, and hand off a commit or patch for the
approved job.

The map changed the action three times. It separated source edit from deployment,
prevented destruction of overlapping work, and rejected the first causal hypothesis.
None of this required reading the entire repository or every log. It required reading
until the remaining uncertainty no longer selected a different safe implementation.

## Snapshot, then resnapshot

A state map decays. The more consequential the action and the more concurrent the
environment, the closer inspection should be to execution.

Use a **before snapshot** to establish the baseline relevant to your change. Use an
**after snapshot** to detect both intended effects and accidental ones. In a repository,
this may mean status plus a scoped diff before and after. In an API, it may mean reading
resource version identifiers. In a deployment system, it may mean comparing desired and
observed state. In a conversation, it may mean reopening the thread before sending so
you do not answer a superseded question.

The two snapshots need not duplicate whole datasets. Preserve the identifiers and fields
needed to compare. If the world supports optimistic concurrency—version numbers,
ETags, generations, transaction conditions—use it. A write that fails because the world
changed is often preferable to a write that silently overwrites the change.

After action, do not interpret every difference as yours. Compare against the recorded
baseline and your action log. Concurrent changes remain possible. The correct report may
be “my edit produced these paths; this additional modification appeared during the run
and was left untouched.” Legibility does not demand false certainty.

## When to stop reading

Inspection can become avoidance. The stopping rule should connect reading to decisions.

List the plausible actions still under consideration. For each unresolved fact, ask:
would a different answer make me choose a materially different action, permission path,
or verification plan? If no, the unknown can remain in the handoff. If yes, estimate the
cheapest reliable way to resolve it. Inspect when the answer is locally discoverable at
low risk. Ask when only the requester can supply intent, when inspection would itself be
intrusive, or when different answers lead to materially different authorized outcomes.
Stop when one action is supported and its relevant risks are bounded.

This rule avoids two caricatures. “Act immediately” mistakes speed for agency. “Know
everything first” makes agency impossible. A sufficient state map is neither exhaustive
nor casual. It is shaped by the decision in front of you.

Before the first material edit, you should be able to say, at least internally:

- where the target is and which instructions govern it;
- what relevant state pre-existed your action;
- what you believe the target's dependencies and effect surface to be;
- which observations are current enough for the action;
- which unknowns remain and why they do not block the chosen step.

That is not ceremony. It is the minimum map required to avoid solving a task in a world
that exists only in the prompt.

The map is allowed to be small. Its obligation is not volume but contact with the state
that can prove your next action wrong.

## Grounding notes

The position sensitivity of information in long contexts is grounded in *Lost in the
Middle* [R4]. Git working-tree and background-refresh behavior is grounded in the
official `git status` documentation [R10a][R10b]. The distinction between verifiable
provenance and factual truth is grounded in the C2PA specification and explainer
[R12a][R12b]. Instruction
topology, the six-question state map, negative-space record, provisional ownership
classes, least necessary observation, and the inspection stopping rule are original
operational constructs proposed by this book.
