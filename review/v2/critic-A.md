<!-- CRITIC A · claude-fable-5 · family:anthropic · pass 3 · 2026-08-28T16:27:29Z -->
CRITIC: claude-fable-5 (family anthropic, actor claude-fable-5@session)
DATE: 2026-08-28
PASS: 3
AUTO-TALLIED VERDICT: PUBLISH

---

# Critic review — rogerai-labs--the-borrowed-world v2

```
CRITIC:    claude-fable-5 (Anthropic) + operator claude-fable-5@session
DATE:      2026-08-28
PASS:      3 (verification)
READ:      delta (v1..v2 diff, all files) + full pass-2 findings ledger + fresh source sample
```

## Verdict summary
Every Pass-2 blocking finding — one from Critic A, seven from Critic C, none from Critic B —
is answered in v2 with a real, inspectable diff, not a rhetorical concession. I verified
each against the v2 tree rather than trusting `response-to-findings.md`: the eval control
count and its new self-test invariant, the four citation splits with resolving fragment
anchors, the reduced twelve-term core vocabulary with local labels explicitly demoted, the
two executable gates and the trace-audit annex, the pre-registered efficacy decision rule,
and the two evaluation cases that now state applicable policy. A fresh source sample
(the C2PA explainer anchor, R12b) resolves to the exact cited sentence. The revision also
did the harder, more honest thing on the two "high" findings: rather than overclaim, it
narrowed the manuscript's own claim to what the shipped artifact can support (choice
scoring is labelled a screening measure; live tool execution is explicitly disclaimed and
pushed to the trace annex). No blocking finding remains open and the delta introduces no
new blocking problems. **PUBLISH** — the manuscript now says only what its evidence
supports, and every debt from Pass 2 is discharged with a locatable change.

## Blocking findings
None. The v1..v2 delta introduces no new blocking issues; all Pass-2 debts are discharged
(see findings ledger below).

## Suggestions (non-blocking)
1. The trace-audit annex (`eval/trace-audit.md`) is the right shape but ships one filled
   world (world one). A future edition would be strengthened by a second filled trace in a
   different family (e.g. a recoverability case) so the "screening vs. execution" gap is
   demonstrated across more than one scenario, not just asserted.
2. The pre-registered decision rule lives in `eval/README.md` and is summarized in ch10.
   Consider also emitting it as a machine-readable field in `manifest.json` (or an
   `eval/decision-rule.json`) so a downstream shelf gate can check the declared threshold
   without parsing prose. Non-blocking; the prose rule is sufficient for publication.
3. Core vocabulary is twelve terms; the chapters still introduce local labels. The demotion
   is stated clearly, but a one-line "local label" typographic marker at each term's first
   use would make the memory-set boundary visible in-line rather than only in backmatter.

## Fact-check sample
Pass 3: fresh sample weighted toward revised sections (citations and eval, the areas most
changed). Each claim resolved against its cited source independently.

| Claim (quoted) | Location | Cited source | Supported? (yes/no/partly) |
|---|---|---|---|
| "provenance information alone cannot tell you whether the digital content is true, accurate or factual" | ch02 / ch05 grounding, cites R12b | C2PA Explainer §"can provenance … depict the truth" (fetched 2026-08-28) | yes — anchor resolves; sentence present verbatim |
| "Five cases are action-required controls, exactly one in each family" | eval/README.md:18 | eval/cases.json (5 entries with `"control": true`, one per family) + `run_self_test` asserting the invariant | yes — count and per-family distribution confirmed in the fixture and the self-test |
| R10 split into R10a (git-status Description) and R10b (Background Refresh) with fragment anchors | backmatter.md:107-108 | git-status docs `#_description`, `#_background_refresh` | yes — locators present and point to the sections the Pass-2 critic named |
| bw-a02 / bw-r02 now state the policy lookup and that it grants authority | eval/cases.json | case prompts | yes — both prompts now open with "You locate the applicable … policies; they grant …" |

## Scores (1–5)
accuracy: 5 · clarity: 4 · completeness-for-tier: 5 · density: 4 · originality: 4

## Pass-3 only: findings ledger
| Finding # (from Pass 2) | Status: resolved / rebutted-accepted / still-open | Note |
|---|---|---|
| A-1 (README "four controls" vs five in cases.json) | resolved | README now states five, one per family; `scorer.run_self_test` asserts the count and per-family distribution — the doc and the code now agree and the invariant is enforced. |
| C-1 (pocket over-lexiconization / density debt, high) | resolved | Glossary cut to 12 core terms with a stated memory set; other chapter labels explicitly demoted to local aids; the single memory instruction repeated in frontmatter and the operating card reduced to the six loop verbs. |
| C-2 (stage/verify non-executable; choice scoring ≠ tool transfer, high) | resolved (claim narrowed) | Executable staging gate (ch06:91) with anomaly threshold; executable verification gate (ch07:326) with a pass rule; `eval/trace-audit.md` annex; README + ch10 relabel exact-choice scoring a screening measure and disclaim live tool execution. The honest narrowing, not an overclaim. |
| C-3 (measurable claim without predeclared success gate, med) | resolved | Pre-registered efficacy decision rule in eval/README (≥5 paired runs, mean exact ≥ +0.10, ≥4 of first 5 deltas positive, no family regression, control accuracy ≥0.80), declared before any paired result; ch10 summarizes and defers to it. |
| C-4 (R10 over-bundling git-status, med) | resolved | Split into R10a (Description) / R10b (Background Refresh) with fragment anchors; grounding notes cite each only where used. |
| C-5 (R11 conflates git + git-restore, med) | resolved | Split into R11a (git "Reset, restore and revert") / R11b (git-restore Description); ch04 cites each to the claim it carries. |
| C-6 (R12 index vs explainer page, med) | resolved | Split into R12a (spec) / R12b (explainer truth-limit section, with fragment anchor); ch02/ch05 cite R12b directly. Anchor verified to resolve to the quoted sentence (fact-check sample above). |
| C-7 (eval authority cases hide policy variance, med) | resolved (eval version-bumped) | bw-a02 / bw-r02 now state that applicable policies were located and grant the authority; scorer/README identify the artifact as `the-borrowed-world-v2` and record the version delta. Choices and keys unchanged, so the fixture stays valid. |
