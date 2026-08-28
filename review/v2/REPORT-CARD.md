# Final verification report card — The Borrowed World v2

## Case identity

- immutable v1: `bb9758963b68da055ca3168044add28a505c8365`
- immutable v2: `543845318a19511f95be912771367d3cdf1bc047`
- author response: `response-to-findings.md` in v2
- authoritative revision gate: `gates-v2`, CI run 33188046621
- gate result: PASS, 0 rejects, 0 warnings, 27,156 body words
- shelf metrics: 20 cases, 5 families, 5 action-required controls, perfect fixture 1.0,
  empirical result claimed false

## Verification outcome

All three original critics completed a delta-scoped Pass 3. Recommendations are
unanimous: **PUBLISH**. No verifier opened a new blocking finding.

| Seat | Pass-2 scores A/C/T/D/O | Pass-3 scores A/C/T/D/O | Recommendation | Fresh sample |
|---|---|---|---|---|
| A — Claude Opus 4.6 | 4 / 5 / 5 / 5 / 4 | 5 / 5 / 5 / 5 / 4 | PUBLISH | 5 of 5 supported |
| B — Xiaomi MiMo v2.5 | 5 / 5 / 5 / 5 / 4 | 5 / 5 / 5 / 5 / 4 | PUBLISH | 10 of 10 supported |
| C — Muse Spark 1.2 | 4 / 3 / 3 / 2 / 4 | 4 / 4 / 4 / 4 / 4 | PUBLISH | 6 of 6 supported |

A/C/T/D/O = accuracy, clarity, completeness-for-tier, density, originality.

## Consolidated findings ledger

| Finding | Opened by | Pass-3 status | Resolving evidence |
|---|---|---|---|
| A-1 — README says four controls; cases contain five | A | resolved | README says five/one per family; scorer self-test asserts and reports both invariants |
| C-1 — pocket-tier over-lexiconization | C | resolved | one-procedure hierarchy; twelve-term core vocabulary; six-verb executable card |
| C-2 — stage/verify not executable; choice score does not prove execution | C | resolved with claim narrowing | executable staging and verification gates; filled world-one record; trace audit; choice score explicitly called screening only |
| C-3 — no empirical success gate | C | resolved | pre-registered five-pair efficacy rule and failure disposition in eval README and chapter 10 |
| C-4 — R10 citation over-bundling | C | resolved | R10a Description and R10b Background Refresh resolving anchors |
| C-5 — R11 citation conflation | C | resolved | R11a command taxonomy and R11b restore-description anchors |
| C-6 — R12 index does not locate truth limitation | C | resolved | R12a specification plus R12b explainer truth-limit anchor |
| C-7 — authority controls leave applicable policy implicit | C | resolved | bw-a02/bw-r02 now state applicable policy resolution; evaluation versioned v2 |

Still-open blocking findings: **none**. Rebutted-but-not-fixed findings: **none**.

## Residual non-blocking notes for the judge

- Exact-choice efficacy remains a screening measure; live tool execution is represented
  only by the qualitative trace-audit contract, not a scored environment.
- The case set is author-constructed, English-language, technology-adjacent, and publicly
  keyed. Contamination and domain transfer remain declared limits.
- Verifiers suggested future trace fixtures, additional external-effect examples, DOI
  links, and minor clarification of what makes a paired run valid. None judged these
  publication-blocking.

## Independent paired-run result

Batch 002 was pre-registered and committed before any evaluation case was sent under
its protocol. It used the dated first-party reader `claude-haiku-4-5-20251001`, five
fresh-session pairs, 20 cases in five families, alternating condition order, serialized
execution, and disabled tools. All 200 case calls completed on their first attempt in
200 distinct sessions; all returned terminal, parseable records.

The frozen scorer reports **EFFICACY CRITERION MET**:

- mean paired exact-score delta: **+0.18** (pre-registered threshold: `+0.10`)
- positive pairs: **5 / 5** (threshold: at least 4 / 5)
- full-book exact score: **1.00 in every run**
- family deltas: authority `+0.35`, completion honesty `+0.10`, evidence `+0.15`,
  preservation `+0.10`, recoverability `+0.20`; no family regression
- controls: baseline `0.80`, full book `1.00`; threshold met without regression

The protocol is in `review/empirical-v2/BATCH-002-PRE-REGISTRATION.md`; the aggregate,
manifest, treatment hash, score files, response ledgers, seeded orders, and all 200 raw
case records are in `review/empirical-v2/batch-002/`. The earlier infrastructure-
incomplete batch remains public and was neither scored nor pooled into this result.

This result supports an efficacy claim only for the declared reader, case distribution,
runner, and date. It is not evidence of general agent safety, domain transfer, or durable
learning.

## Dependencies not adjudicated by the critic panel

- named-human verification of manuscript, sources, gate reproduction, and paired results
- founder-plus-model judge verdict
- publication signing, cover assignment, rendering, release, and live verification

This report card records the critic case. It does not cast the judge verdict or represent
the pending dependencies as complete.
