# Critic review — the-borrowed-world v1

```
CRITIC:    claude-opus-4-6 · Anthropic Claude · Claude Code 2.1.250 (Seat A)
DATE:      2026-08-28
PASS:      2 (panel)
READ:      full manuscript (frontmatter, provenance, ch01–ch10, backmatter, eval/)
```

## Verdict summary

*The Borrowed World* is a disciplined, original, and well-grounded pocket manual that systematizes the implicit craft of acting inside environments with history, owners, and consequences. Its prose is precise without being sterile, its disclaimers are honest (it does not claim moral agency, measured effect, or domain authority), and its shipped evaluation is carefully designed with deterministic scoring, action-required controls, and a reproducible paired-run protocol. The reference set is real, correctly attributed (all sampled sources resolved), and used with appropriate scope. The manuscript's assigned audit emphasis—anthropomorphic overclaim—found no violations; the "control policy, not a personality" framing in ch01 is maintained throughout. One blocking finding exists in the evaluation README, and several non-blocking suggestions would strengthen the work. **SALVAGEABLE — findings below**

## Blocking findings

| # | Location (file:section) | Claim / problem | Evidence | Severity (high/med) |
|---|---|---|---|---|
| 1 | eval/README.md: "Measured behaviors" ¶2 | States "Four cases are action-required controls" | `cases.json` contains **five** cases with `"control": true`: bw-p02, bw-a02, bw-r02, bw-e02, bw-c03 — one per family. The scorer's self-test does not validate this count against the README, so the code runs correctly while the documentation is wrong. | med |

## Suggestions (non-blocking)

1. **Reconcile the foundational five coordinates with the evaluation's five families.** Ch01 introduces Outcome, Preservation, Authority, Evidence, and Legibility as the faithful-objective coordinates. The eval measures Preservation, Authority, Recoverability, Evidence, and Completion honesty. "Recoverability" is absent from ch01's list; "Legibility" and "Outcome" are absent from the eval families. The book develops recoverability fully in ch04 and completion honesty in ch07/ch10, so the concepts are present—but the ch01→ch10 arc would benefit from a sentence in ch10 or the eval README explaining how the foundational coordinates evolved into the measured families. The "at least" qualifier in ch01 leaves room, but the silent substitution may confuse a reader tracking the thread.

2. **Add a self-test assertion for the control count.** The scorer's `run_self_test` validates family count but not the number of action-required controls. A one-line check (`sum(1 for c in cases if c["control"])`) would catch the README discrepancy mechanically and guard against future drift.

3. **Consider stating the control distribution (one per family).** The balanced design—one control per family—is deliberate and elegant, ensuring false-restraint measurement cannot cluster in one family. Making this explicit in the eval README would help independent operators understand the design intent.

4. **R11 references two URLs under one citation key.** The backmatter gives R11 as both `https://git-scm.com/docs/git` and `https://git-scm.com/docs/git-restore`. Consider splitting into R11a/R11b or noting both URLs explicitly, since ch04 draws on the `git-restore` page for the deletion-during-restore claim and on the parent page for the revert/restore/reset taxonomy.

5. **Ch09 "World three" could anchor the 812-vs-900 discrepancy more tightly.** The scenario notes the view returns 812 recipients while the dashboard says "about 900" and tells the agent to "record the discrepancy." A sentence about *why* the authoritative send view should govern (e.g., dashboards may include non-deliverable or filtered addresses) would make the pedagogical point sharper without over-specifying the constructed case.

6. **The compact treatment (`reader-treatment.md`) could note its own incompleteness relative to the book.** The eval README discusses the ablation protocol but the treatment file itself contains no disclaimer that it omits cases, failure analysis, and grounding detail present in the full book. A one-line scope note would help operators using it in isolation.

7. **Minor ordering in the glossary.** "Stewardship Loop" is capitalized and appears among lowercase entries. The glossary is otherwise consistently lowercased and alphabetized; normalizing the casing would improve consistency (the operating card already uses the phrase without capitalization).

## Fact-check sample

Seven claims sampled (~5.4% of estimated 130 distinct factual claims), spanning academic citations, specification claims, documentation behavior, and internal eval consistency.

| Claim (quoted or paraphrased) | Location | Cited source | Supported? |
|---|---|---|---|
| "ReAct studies a loop in which reasoning and environment actions inform one another" | ch01 | R3 — arxiv 2210.03629 | **yes** — abstract states "reasoning traces and task-specific actions in an interleaved manner" |
| "relevant material in the middle of long inputs could be used less reliably than material near the beginning or end" | ch02 | R4 — arxiv 2307.03172 | **yes** — abstract: "performance…significantly degrades when models must access relevant information in the middle" |
| "NIST's AI Risk Management Framework…organized around Govern, Map, Measure, and Manage" | ch01 | R1 — NIST AI 100-1 | **yes** — the four core functions confirmed via NIST AI RMF Playbook |
| "restoring a tracked path absent from the restore source removes it to make the working tree match that source" | ch04 | R11 — git-scm.com/docs/git-restore | **yes** — git-restore documentation confirms this behavior |
| "C2PA's own explainer is explicit that provenance alone cannot establish that content is factually true" | ch02 | R12 — spec.c2pa.org 2.2 | **yes** (substantively) — the spec's Guiding Principles state it provides validation of assertions, not truth judgments; the manuscript's claim is a fair inference from the spec's stated non-goals |
| GPT-5.6 Sol exists as a documented OpenAI model at the cited URL | provenance.md | R13 — developers.openai.com | **yes** — page resolves; documents GPT-5.6 Sol as a flagship model with 1.05M context, Feb 2026 cutoff |
| "Four cases are action-required controls" | eval/README.md | cases.json | **no** — cases.json contains five controls (bw-p02, bw-a02, bw-r02, bw-e02, bw-c03); promoted to blocking finding #1 |

**Note on R4 venue year:** The manuscript cites "Transactions of the Association for Computational Linguistics, 2024." The arXiv preprint is dated 2023. The TACL journal publication date (Volume 12, 2024) is the standard venue-of-record year; the manuscript's citation is correct.

**Source resolution method:** All sampled URLs were fetched via web tools during this review session. ArXiv abstracts, NIST publication pages, Git documentation, the C2PA specification, and the OpenAI model catalog page were accessed and their content compared against manuscript claims. No source was inaccessible.

## Scores (1–5)

accuracy: 4 · clarity: 5 · completeness-for-tier: 5 · density: 5 · originality: 4
