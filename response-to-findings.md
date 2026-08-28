# Response to Pass-2 findings — v1 → v2

Author model: OpenAI `gpt-5.6-sol`  
Revision date: 2026-08-28  
Pass-2 reviews: https://github.com/oailly-press/the-borrowed-world/tree/main/review/v1

Every Pass-2 blocking finding is answered below. File and section names identify the
revision diff; the immutable revision SHA and `v2` tag are supplied with submission.

## Critic A

### A-1 — eval README says four controls while cases define five

**Fixed with diff.** `eval/README.md:Measured behaviors` now states that there are five
action-required controls, exactly one per family. `eval/scorer.py:run_self_test` now
asserts both invariants and reports the count and per-family distribution. The self-test
returns five controls across authority, completion honesty, evidence, preservation, and
recoverability.

## Critic C

### C-1 — pocket over-lexiconization and density debt

**Fixed with diff.** `ch01-the-borrowed-world.md:One procedure, three views` establishes
a strict hierarchy: five coordinates judge results, four boundaries detect crossings,
and only the six-verb Stewardship Loop is a procedure to memorize. It also maps the
five result coordinates to the five evaluation families. `frontmatter.md` repeats the
single memory instruction. `backmatter.md:Core vocabulary` replaces the prior glossary
of roughly sixty labels with twelve core terms and states that other chapter labels are
local aids, not an API or additional workflow. The operating card now presents only the
six loop verbs as an executable gate.

The chapters retain some named local checks because removing their distinctions would
reduce diagnostic precision. They are explicitly demoted from memory requirements and
are retrieved only when the matching condition appears.

### C-2 — stage/verify are not executable; choice scoring does not prove tool transfer

**Fixed with diff and claim narrowing.** The “Executable staging gate” in
`ch06-the-smallest-honest-action.md` supplies required fields, an exit rule, and an
anomaly threshold: one unexpected material artifact or party pauses execution. The
“Executable verification gate” in `ch07-verification-is-an-action.md` supplies a filled
claim/check/evidence/preservation/limit matrix and a pass rule: every
completion-contract claim is supported or removed.
`ch09-five-borrowed-worlds.md:World one` adds a filled loop record with target, surface,
stop condition, checks, and handoff language.

`eval/trace-audit.md` adds a structured execution-trace record, seven qualitative pass
conditions, and a filled world-one artifact. `eval/README.md` and chapter 10 now say
explicitly that exact-choice scoring is a screening measure and cannot establish live
tool execution. The trace audit is intentionally not folded into the numeric efficacy
score because the 20 constructed cases do not ship executable environments. The revised
claim is the narrower one the artifact can support.

### C-3 — no predeclared empirical success gate

**Fixed with diff.** Before any paired result was produced, `eval/README.md:Pre-registered
efficacy decision rule` declares the decision batch and threshold: at least five paired
runs; mean exact improvement of at least +0.10; positive deltas in at least four of the
first five pairs; no mean family regression; and action-required-control accuracy of at
least 0.80 without regression. Failed or selectively replaced runs cannot support a
positive claim. Chapter 10 summarizes the gate and defers to the evaluation README for
the complete rule.

### C-4 — R10 bundles distinct git-status claims without locators

**Fixed with diff.** R10 is split into R10a, the official `git-status` Description
section, and R10b, the official Background Refresh section. Chapter 1 and the relevant
chapter 2 propositions now cite the resolving locator that carries each claim. Grounding
notes cite both only when both are used.

### C-5 — R11 conflates Git's three-command distinction with restore deletion behavior

**Fixed with diff.** R11 is split into R11a, the official “Reset, restore and revert”
section, and R11b, the `git-restore` Description section. Chapter 4 cites R11a for command
semantics and R11b for removal of a tracked path absent from the restore source.

### C-6 — R12 points to the C2PA index rather than the truth-limit passage

**Fixed with diff.** R12 is split into R12a for the specification and provenance
manifest capability, and R12b for the explainer section asking whether provenance can
determine whether an asset depicts the truth. Chapters 2 and 5 now cite R12b directly
for the factual-truth limitation. The manifest records both resolving sources.

### C-7 — authority-control cases leave applicable policy implicit

**Fixed with diff and evaluation version bump.** `eval/cases.json` now states in
`bw-a02` that applicable workspace and channel policies were located, grant send
authority, and require no further approval. `bw-r02` now states that applicable service
and incident policies were located, the active runbook authorizes the exact role and
action, and no narrower policy adds approval. Choices and answer keys are unchanged.
Because prompts changed, the scorer and README identify this artifact as
`the-borrowed-world-v2` and record the version delta.

## Non-blocking suggestions incorporated

The revision also distinguishes five recovery dimensions from four action bands; explains
the 812-versus-about-900 audience source-of-truth choice; states the compact treatment's
omissions; harmonizes the measurement card around paired runs; neutralizes the provenance
tool wording; discloses the English-language, technology-adjacent, author-constructed
case distribution and possible contamination; and strengthens quarantine privacy,
backup, and same-volume guidance.

Suggestions to turn all 20 choice cases into executable tool environments or to add DOI
links were not made blocking and are not represented as complete. The trace annex makes
the execution limitation auditable without pretending that a live benchmark was built
inside this one revision cycle.
