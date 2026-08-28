# Critic review — the-borrowed-world v2

```
CRITIC:    claude-opus-4-6 · Anthropic Claude · Claude Code 2.1.250 (Seat A)
DATE:      2026-08-28
PASS:      3 (verification)
READ:      delta (v1→v2 diff, response-to-findings.md, all revised sections, full eval/)
```

## Verdict summary

The single blocking finding from my Pass-2 review—the eval README stating four action-required controls while `cases.json` defined five—is cleanly resolved. The documentation now states five controls, the scorer mechanically enforces the one-per-family invariant, and the self-test reports both the count and per-family distribution. All seven non-blocking suggestions from my review were substantively addressed: the five-coordinate-to-five-family mapping is now explicit in ch01, references R10/R11/R12 are properly split with section-level anchors, the compact treatment declares its own incompleteness, the 812-vs-900 audience discrepancy is now explained, and the glossary was replaced with a focused core vocabulary. The revision also addresses Critic C's structural findings—executable gates in ch06 and ch07, a pre-registered efficacy decision rule, a trace-audit annex, and policy-explicit authority-control prompts—without introducing new factual errors or anthropomorphic overclaim. A fresh 3% factual sample weighted toward revised sections (five claims, all resolved via web tools) found every cited source accessible and supportive. The manuscript's integrity posture is maintained: no content addresses reviewers or solicits favorable treatment. The revision is proportionate, honest about its remaining pipeline dependencies, and tightens every claim the critics challenged. **PUBLISH** — The manuscript meets the standards of the FOR MACHINE READERS pocket shelf. Its factual claims are grounded in resolving sources, its evaluation is mechanically sound and pre-registered, its disclaimers are honest about what remains pending (paired runs, human verification, judge verdict, signing), and its prose quality is high throughout. The revision demonstrates responsive authorship without defensive padding. The remaining pipeline states (empirical paired run, named-human verification, judge verdict, C2PA signing, cover) are correctly identified as separate dependencies and do not block the manuscript's readiness for those steps.

## Blocking findings

| # | Location (file:section) | Claim / problem | Evidence | Severity (high/med) |
|---|---|---|---|---|

*(No blocking findings. The single Pass-2 blocking finding is resolved; see findings ledger below.)*

## Suggestions (non-blocking)

1. **eval/README.md versioning paragraph line break.** The final versioning paragraph reads: "…`bw-a02` and `bw-r02`; answer choices and keys are unchanged. Any change to prompts, choices, answer keys, scoring, or family assignment creates a new eval version." The adjacency of "choices and keys are unchanged" and "Any change to prompts, choices…creates a new eval version" could momentarily confuse a reader—prompts *did* change, which is why v2 exists. The logic is correct (prompt changes trigger a new version; answer choices/keys did not change), but a paragraph break or conjunction would make the two statements less jarring.

2. **The trace-audit.md filled example references "repository R" and "dependency L" without concrete identifiers.** This is intentional (it maps to the constructed World One case), but a brief note that the example uses the ch09 scenario's symbolic names would help an operator encountering the annex independently of the chapter.

3. **The pre-registered decision rule's "first five valid pairs" language could clarify what makes a pair "valid."** The rule states "The first five valid pairs are the decision set; runs may not be discarded or replaced after scoring." A pair with infrastructure failures (e.g., API outage mid-run) might be ambiguous—is it "valid" if the scorer produces a result from partial responses? The intent is clearly that parse failures remain incorrect, but a sentence about what constitutes a completed pair would close the gap.

## Fact-check sample

Fresh 3% sample (5 claims), weighted toward revised sections. All sources independently resolved via web fetch during this review session.

| Claim (quoted or paraphrased) | Location | Cited source | Supported? (yes/no/partly) |
|---|---|---|---|
| "background refresh behavior can update cached stat information and acquire a lock unless optional locking is disabled" | ch02 (revised citation R10b) | R10b — git-scm.com/docs/git-status#_background_refresh | **yes** — section confirms automatic index refresh, cached stat updates, lock acquisition, and `--no-optional-locks` flag |
| "provenance alone cannot establish that content is factually true" | ch02/ch05 (revised citation R12b) | R12b — C2PA Explainer §7.2.2 | **yes** — exact language: "provenance information alone cannot tell you whether the digital content is true, accurate or factual" |
| "Five cases are action-required controls, exactly one in each family" | eval/README.md (revised) | cases.json | **yes** — bw-p02 (preservation), bw-a02 (authority), bw-r02 (recoverability), bw-e02 (evidence), bw-c03 (completion_honesty); count = 5, one per family |
| "mean paired exact-score improvement is at least +0.10 (two of 20 cases)" | eval/README.md (new section) | arithmetic | **yes** — 2/20 = 0.10 exactly |
| Git documentation distinguishes revert (new commit reversing changes), restore (working-tree/index from another source), reset (moves branch tip) | ch04 (revised citation R11a) | R11a — git-scm.com/docs/git#_reset_restore_and_revert | **yes** — section states: revert "making a new commit that reverts changes," restore "restoring files in the working tree," reset "updating your branch, moving the tip" |

**Source resolution method:** All URLs fetched via web tools during this review session. Git documentation (three section-anchored URLs), C2PA explainer, and internal manuscript artifacts were accessed and compared against claims. No source was inaccessible.

## Scores (1–5)

accuracy: 5 · clarity: 5 · completeness-for-tier: 5 · density: 5 · originality: 4

## Pass-3 only: findings ledger

| Finding # (from Pass 2) | Status | Note |
|---|---|---|
| A-1 (eval README states four controls; cases.json has five) | **resolved** | eval/README.md corrected to "Five…exactly one in each family"; scorer.py `run_self_test` now asserts count (5) and per-family distribution; self-test reports `action_required_control_count` and `action_required_control_families`; eval version bumped to v2 with delta explanation |
| Suggestion 1 (reconcile five coordinates with five eval families) | **resolved** | ch01 "One procedure, three views" explicitly maps coordinates to families: preservation/authority/evidence map directly; recoverability tests recovery; completion honesty combines outcome + legibility |
| Suggestion 2 (add self-test assertion for control count) | **resolved** | scorer.py adds `controls_by_family` Counter, asserts `sum == 5` and `one per family` |
| Suggestion 3 (state control distribution) | **resolved** | eval/README.md: "exactly one in each family" |
| Suggestion 4 (split R11 into R11a/R11b) | **resolved** | R11a = reset/restore/revert taxonomy; R11b = git-restore description (deletion behavior); both verified via web fetch |
| Suggestion 5 (812-vs-900 discrepancy anchoring) | **resolved** | ch09 World Three now explains: "its exact generation applies suppression and eligibility rules, while the headline is explicitly approximate and may count records that cannot receive mail" |
| Suggestion 6 (compact treatment completeness note) | **resolved** | reader-treatment.md opens with: "This is an ablation, not a substitute for the full book. It omits the worked cases, contrary-review procedure, source grounding, and execution-trace annex." |
| Suggestion 7 (glossary casing consistency) | **resolved** | Glossary replaced entirely by "Core vocabulary" with twelve bold-formatted terms and explicit statement that other labels are "local aids, not an API" |
