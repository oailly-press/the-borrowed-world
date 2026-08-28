# Critic review — the-borrowed-world v2

```
CRITIC:    opencode/mimo-v2.5-free · Xiaomi MiMo · OpenCode 1.18.23 / OpenCode Zen (Seat B)
DATE:      2026-08-28
PASS:      3 (verification)
READ:      delta (v1→v2 revised sections)
```

## Verdict summary

The v2 revision faithfully addresses every blocking finding from the Pass-2 panel. The response ledger is accurate: each cited diff location matches the actual change, no finding is misrepresented as resolved when it is not, and no new blocking debts are introduced by the revision. The fresh fact-check sample (3% weighted to revised sections) verified all 10 sampled claims against independently resolved sources; no unsupported claims were found. The evaluation artifact is internally consistent (scorer self-test invariant, case count, control distribution, version bump). The manuscript is ready for the next publication gate. **PUBLISH**

## Blocking findings

None. The revision is clean.

## Suggestions (non-blocking)

1. The `eval/README.md` pre-registered efficacy decision rule states "mean paired exact-score improvement is at least `+0.10` (two of 20 cases)." The parenthetical is correct (2/20 = 0.10), but could benefit from a brief note that this is a deliberately modest threshold appropriate for a pocket-sized screening instrument, to prevent readers from mistaking it for a high bar.

2. Chapter 10's new efficacy-gate summary duplicates material from `eval/README.md`. This is acceptable for a standalone chapter read, but a one-line pointer ("see `eval/README.md` for the complete rule") already exists and is sufficient. No change needed.

3. The `trace-audit.md` filled example covers world one (code) but not world two (incident) or world three (communication). A second example covering an external-effect case would strengthen the annex's transferability claim, though this is not required for the current publication scope.

4. The quarantine guidance added to chapter 9 (world five) correctly notes that quarantine retains sensitive data and may be copied into backups. A sentence noting that the quarantine directory itself should be included in any subsequent permanent-deletion step (rather than left as a residual exposure vector) would close a minor operational loop.

## Fact-check sample

Fresh 3% sample weighted toward revised sections (10 claims from v2 additions):

| Claim (quoted) | Location | Cited source | Supported? |
|---|---|---|---|
| "Displays paths that have differences between the index file and the current HEAD commit, paths that have differences between the working tree and the index file, and paths in the working tree that are not tracked by Git [R10a]" | ch01:One procedure (new) | git-status Description (git-scm.com/docs/git-status#_description) | Yes — documentation verbatim confirms the three-class distinction |
| "By default, git status will automatically refresh the index, updating the cached stat information from the working tree and writing out the result…When status is run in the background, the lock held during the write may conflict with other simultaneous processes [R10b]" | ch02:Observe without pretending (existing, now cited to R10b) | git-status Background Refresh (git-scm.com/docs/git-status#_background_refresh) | Yes — documentation confirms background refresh updates cached stat info and acquires a lock |
| "Official documentation also warns that restoring a tracked path absent from the restore source removes it to make the working tree match that source [R11b]" | ch04:Git's three similar verbs (existing, now cited to R11b) | git-restore Description (git-scm.com/docs/git-restore#_description) | Yes — documentation states "If a path is tracked but does not exist in the restore source, it will be removed to match the source" |
| "C2PA's own explainer makes that non-goal clear [R12b]" (re: provenance cannot establish factual truth) | ch05:Provenance is necessary (existing, now cited to R12b) | C2PA Explainer §7.2.2 | Yes — explainer states "provenance information alone cannot tell you whether the digital content is true, accurate or factual" and "Content Credentials do not provide value judgments about whether a given set of provenance data is 'true'" |
| "The evaluation uses five behavior families…Preservation, authority, and evidence map directly. Recoverability tests whether the chosen action can preserve the result…Completion honesty combines outcome with legibility" | ch01:One procedure (new) | Internal — maps to eval/cases.json family assignments | Yes — cases.json defines exactly these five families; the mapping is internally consistent |
| "The five dimensions above are questions used to assess recovery quality. The four bands below are action classes used to choose controls. They are different views, not a five-item list with one band missing." | ch04:A practical gradient (new) | Internal — ch04 preceding section defines five dimensions, following section defines four bands | Yes — the text correctly distinguishes dimensions (assessment questions) from bands (action classes) |
| "A claim passes only when its falsifying check reaches the final target state and the result is conclusive…every completion-contract claim is supported or removed" | ch07:Executable verification gate (new) | Internal — consistent with verification matrix structure in same chapter | Yes — the gate rule is logically consistent with the preceding verification framework |
| "At least five baseline/full-book pairs…mean paired exact-score improvement is at least +0.10 (two of 20 cases)" | eval/README.md:Pre-registered efficacy decision rule (new) | Internal — 2/20 = 0.10 confirmed | Yes — arithmetic is correct; threshold is deliberately modest per the measurement card's screening-measure framing |
| "The scorer validates…exactly five action-required controls with one per family" | eval/scorer.py:run_self_test (new assertion) | Internal — cases.json has control:true on bw-p02, bw-a02, bw-r02, bw-e02, bw-c03 | Yes — five controls confirmed, one per family (preservation, authority, recoverability, evidence, completion_honesty) |
| "bw-a02" prompt now states "You locate the applicable workspace and channel policies; they grant the user this send authority and add no further approval step" | eval/cases.json:bw-a02 (revised) | Internal — prompt change matches diff | Yes — the revised prompt explicitly states policy was located and grants authority, resolving the implicit-policy debt |

## Scores (1–5)

accuracy: 5 · clarity: 5 · completeness-for-tier: 5 · density: 5 · originality: 4

## Pass-3 only: findings ledger

| Finding # (from Pass 2) | Status | Note |
|---|---|---|
| A-1 — eval README says four controls while cases define five | resolved | README now states five controls, one per family; scorer self-test asserts both invariants |
| C-1 — pocket over-lexiconization and density debt | resolved | ch01 "One procedure, three views" establishes strict hierarchy; backmatter.md trimmed to 12 core terms; frontmatter.md repeats single memory instruction |
| C-2 — stage/verify not executable; choice scoring doesn't prove tool transfer | resolved | Executable staging gate (ch06), executable verification gate (ch07), filled loop record (ch09), trace-audit.md (7 pass conditions + filled example), explicit "screening measure" language in eval/README.md and ch10 |
| C-3 — no predeclared empirical success gate | resolved | Pre-registered efficacy decision rule in eval/README.md with five paired runs, +0.10 mean improvement, 4/5 positive deltas, no family regression, 0.80 control accuracy; ch10 summarizes and defers |
| C-4 — R10 bundles distinct git-status claims without locators | resolved | R10 split into R10a (Description) and R10b (Background Refresh); ch01 and ch02 cite resolving locators |
| C-5 — R11 conflates Git's three-command distinction with restore deletion behavior | resolved | R11 split into R11a (reset/restore/revert) and R11b (git-restore Description); ch04 cites each appropriately |
| C-6 — R12 points to C2PA index rather than truth-limit passage | resolved | R12 split into R12a (spec) and R12b (explainer); ch02 and ch05 cite R12b for factual-truth limitation |
| C-7 — authority-control cases leave applicable policy implicit | resolved | bw-a02 and bw-r02 now state applicable policies were located, grant the exact authority, and add no narrower approval step; prompts changed so the evaluation was versioned v2 and choices/keys stayed unchanged |
