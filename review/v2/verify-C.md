# Critic review — the-borrowed-world [v2]

```
CRITIC:    opencode/muse-spark-1.2-contributor-free · Muse · OpenCode 1.18.23 / OpenCode Zen (Seat C)
DATE:      2026-08-28
PASS:      3 (verification)
READ:      delta (frontmatter.md, ch01-the-borrowed-world.md, ch02-read-before-edit.md, ch04-the-reversibility-gradient.md, ch05-inside-the-evidence.md, ch06-the-smallest-honest-action.md, ch07-verification-is-an-action.md, ch09-five-borrowed-worlds.md, ch10-leave-the-world-legible.md, backmatter.md, provenance.md, manifest.json, pass1-report.json, eval/README.md, eval/cases.json, eval/scorer.py, eval/trace-audit.md, eval/reader-treatment.md, response-to-findings.md)
```

## Verdict summary
Pass-3 delta verification of v1→v2 finds all seven C-1–C-7 blocking debts addressed with diff and claim narrowing: hierarchy demotes local labels to aids and core vocabulary collapses to 12 terms, executable staging/verification gates with stop-trigger/thresholds are added and trace-audit annex separates screening choice-score from tool transfer, pre-registered efficacy gate is declared before any paired runs, citation locators are split to R10a/R10b/R11a/R11b/R12a/R12b with section-anchored URLs, and authority cases bw-a02/bw-r02 explicitly locate applicable policy/runbook authority. Fresh 3% factual sample weighted to revised sections resolves and supports its sources (webfetch verified). No reviewer-addressed content detected. Residual density/choice-only limits are now disclosed rather than debt. **PUBLISH** — v2 meets pocket tier and FOR MACHINE READERS shelf intake requirements as revised author draft 2.0; empirical efficacy remains unverified by design and must be reported per the new pre-registered gate without rescoring as general safety.

## Blocking findings

| # | Location (file:section) | Claim / problem | Evidence | Severity (high/med) |
|---|---|---|---|---|
| — | — | No new blocking debt introduced in v2 delta. All Pass-2 blocking debts resolved or claim-narrowed as ledgered. Minor residual density (retained local checks) now explicitly marked non-memorization aids and does not constitute a tier-blocking debt. | delta diff + response-to-findings.md | — |

## Suggestions (non-blocking)
1. Keep opposite of C-1 by adding a single-page quick-reference card consolidating the 12 core terms + Stewardship Loop gates; optional to reduce locate-bound-ground recall friction in retrieval mode.
2. Future eval version should add 2–3 live-tool trace fixtures (status before/after, operation ID read-back, recipient preview) to complement screening choice score without holding pocket draft to full benchmark build.
3. Add DOI fragment to arXiv references (R3–R8) for persistence; already functional via cited URLs.
4. After five paired runs, version contamination header (`no-train`) for eval v2 and refresh cadence are correctly disclosed — retain as-is.

## Fact-check sample
Pass 3: fresh 3% weighted to revised sections (6 claims). All sampled cited sources independently resolved via webfetch 2026-08-28; no claim its citation does not support.

| Claim (quoted) | Location | Cited source | Supported? (yes/no/partly) |
|---|---|---|---|
| "Git's `status` command exists to show differences among the current commit, the index, and the working tree, including untracked paths" | ch01:A first case — ch02:What condition (revised cites R10a) | R10a Git git-status Documentation — Description `https://git-scm.com/docs/git-status#_description` | yes — webfetch DESCRIPTION: "Displays paths that have differences between the index file and the current HEAD commit, paths that have differences between the working tree and the index file, and paths in the working tree that are not tracked by Git" |
| "background refresh behavior can update cached stat information and acquire a lock unless optional locking is disabled" | ch02:Observe without pretending (revised cite R10b) | R10b Git git-status Documentation — Background Refresh `https://git-scm.com/docs/git-status#_background_refresh` | yes — webfetch: "By default, git status will automatically refresh the index, updating the cached stat information... lock held during the write may conflict... Scripts running status in the background should consider using git --no-optional-locks status" |
| "Its documentation distinguishes `revert`, `restore`, and `reset`: revert makes a new commit that reverses changes ... restore changes working-tree or index ... reset moves a branch tip..." | ch04:Git's three similar verbs (revised cite R11a) | R11a Git Documentation — Reset, restore and revert `https://git-scm.com/docs/git#_reset_restore_and_revert` | yes — R11a and linked git-restore/git-reset pages define distinct roles; webfetch of git-restore confirms restore scope; partly synthetic synthesis but not contradicted and now correctly split — locus correct |
| "restoring a tracked path absent from the restore source removes it to make the working tree match that source" | ch04:Git's three similar verbs (revised cite R11b) | R11b Git git-restore Documentation — Description `https://git-scm.com/docs/git-restore#_description` | yes — webfetch DESCRIPTION: "If a path is tracked but does not exist in the restore source, it will be removed to match the source." verbatim |
| "C2PA explainer is explicit that provenance alone cannot establish that content is factually true" | ch02:Dirty state / ch05:Provenance is necessary (revised cite R12b) | R12b C2PA Explainer — Can provenance determine whether an asset depicts the truth? `https://spec.c2pa.org/specifications/specifications/2.2/explainer/Explainer.html#_can_provenance_information_be_used_to_determine_whether_a_digital_asset_such_as_an_image_or_video_depicts_the_truth` | yes — webfetch FAQ 7.2.2: "Provenance information alone cannot tell you whether the digital content is true, accurate or factual." and sec 2 Goals and Non-goals: "Content Credentials do not provide value judgments about whether a given set of provenance data is 'true'"; revised locator correct (previous index-only locator fixed) |
| "In experiments on multi-document question answering and key-value retrieval, the position of relevant information affected model performance; relevant material in the middle... could be used less reliably" | ch02:Discover the instruction topology (grounding note R4, retained) | R4 Liu et al. Lost in the Middle `https://arxiv.org/abs/2307.03172` | yes — Abstract verified Pass-2 and re-resolved: performance highest at beginning/end, degrades in middle; supports position-sensitivity caution |

## Scores (1–5)
accuracy: 4 · clarity: 4 · completeness-for-tier: 4 · density: 4 · originality: 4

## Pass-3 only: findings ledger
| Finding # (from Pass 2) | Status: resolved / rebutted-accepted / still-open | Note |
|---|---|---|
| C-1 (density debt — pocket over-lexiconization) | resolved | ch01:One procedure, three views hierarchy + frontmatter single-memory instruction + backmatter Core vocabulary collapsed from ~60 to 12 terms; operating card reduced to 6-verb gate with exit conditions; response-to-findings C-1 documents diff. Residual local labels explicitly demoted to aids, not API. |
| C-2 (stage/verify non-executable; choice≠tool transfer) | resolved (with claim narrowing) | ch06 Executable staging gate (5 lines, anomaly trigger: one unexpected material artifact pauses) + ch07 Executable verification gate (claim/check/evidence/preservation/limit matrix, pass rule) + ch09 world-one loop record + eval/trace-audit.md with 7 pass conditions and filled example. eval/README.md and ch10 now explicitly state exact-choice = screening measure, not execution proof. Static audit only — no code execution. |
| C-3 (no predeclared success gate) | resolved | eval/README.md:Pre-registered efficacy decision rule added: ≥5 paired runs, mean +0.10 exact, ≥4/5 deltas positive, no family regression, controls ≥0.80 no regression, immutable batch, efficacy criterion not met on failure. ch10 summary defers to README. |
| C-4 (R10 over-bundling) | resolved | Split to R10a Description + R10b Background Refresh; ch01 cites R10a, ch02 cites R10a/R10b, backmatter lists both with #_description / #_background_refresh anchors; webfetch above confirms. |
| C-5 (R11 conflates git + git-restore) | resolved | Split to R11a `git#_reset_restore_and_revert` + R11b `git-restore#_description`; ch04 cites respectively; webfetch confirms both locators contain quoted sentences. |
| C-6 (R12 index not explainer) | resolved | Split to R12a spec index + R12b Explainer `#_can_provenance_information_be_used...`; ch02/ch05 now cite R12b directly; webfetch confirms truth-limit sentence at FAQ 7.2.2. |
| C-7 (bw-a02/bw-r02 authority assumption) | resolved | eval/cases.json prompts expanded to state applicable policy/runbook located and grants authority with no narrower approval; scorer and README bumped to the-borrowed-world-v2, self-test asserts 5 controls one-per-family; choices/keys unchanged, version delta documented. |
