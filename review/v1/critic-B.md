# Critic review — the-borrowed-world v1

```
CRITIC:    opencode/mimo-v2.5-free · Xiaomi MiMo · OpenCode 1.18.23 / OpenCode Zen (Seat B)
DATE:      2026-08-28
PASS:      2 (panel)
READ:      full manuscript
```

## Verdict summary

This is a structurally complete, internally consistent, and methodologically honest author draft. The ten chapters build a coherent operational framework with clearly delineated original constructs versus cited foundations. The shipped evaluation artifact is reproducible and self-testing. No integrity violations were found; no content addresses the reviewer or attempts to influence outcomes. The fact-check sample verified 10 of 10 claims against resolved sources, with all claims supported. The manuscript has no blocking findings that would prevent publication consideration pending completion of the stated publication dependencies (human verification, C2PA signing, empirical model-effect runs). **SALVAGEABLE — findings below**

## Blocking findings

None identified. The manuscript's explicit disclosure of what remains incomplete (provenance.md, publication status) is accurate and not deceptive. The evaluation claims are properly bounded to the shipped artifact and do not assert measured model improvement without empirical runs.

## Suggestions (non-blocking)

1. The five-coordinate objective (Ch. 1) and six-step Stewardship Loop (Ch. 10) are presented as complementary but never explicitly mapped to each other. A brief cross-reference would help readers see the relationship between diagnosis (five coordinates) and execution (six verbs).

2. Chapter 9's five cases are strong but all operate in English-language, technology-adjacent domains. A note acknowledging cultural and linguistic limitations of the case set would strengthen the bounded-claim posture the book otherwise maintains well.

3. The glossary entries for "commitment" and "commitment action" are close enough to risk confusion. "Commitment" in common usage overlaps with version-control commits; consider a brief disambiguation note or renaming one.

4. The compact reader treatment (`reader-treatment.md`) omits the "contrary review" six-attack procedure described in Chapter 10. If the compact is meant to be a self-sufficient operational extraction, this omission should be flagged in `eval/README.md` so operators understand what the ablation does and does not test.

5. The "measurement card" section in Chapter 5 and the evaluation `README.md` measurement card use overlapping but slightly different field names. Harmonizing terminology (e.g., "repetitions" vs. "runs") would reduce reader friction without changing substance.

6. The provenance page states the OpenAI Docs skill "caused the provenance to use `gpt-5.6-sol` rather than a guessed generic GPT-5 label." This is a reasonable production note but could read as editorializing about tool quality. Consider neutral phrasing.

7. The five-band reversibility gradient (Ch. 4) names four bands. The text says "Four bands are useful" but earlier introduces five dimensions. The five-to-four mapping could be made explicit to avoid the impression of a counting error.

8. The evaluation cases are all authored by the same model family (GPT-5.6-sol per provenance). The `eval/README.md` acknowledges this limitation but a one-sentence callout in the main manuscript (Ch. 10) would help readers who skip the eval docs.

## Fact-check sample

10 factual claims sampled (approximately 5% of the substantive factual claims across the manuscript):

| Claim (quoted) | Location | Cited source | Supported? |
|---|---|---|---|
| "SWE-bench asks a model to change a real repository so that an issue is resolved [R5]" | ch01:§1 | SWE-bench (arXiv:2310.06770) | Yes — abstract confirms "Given a codebase along with a description of an issue to be resolved, a language model is tasked with editing the codebase to address the issue" |
| "ReAct studies a loop in which reasoning and environment actions inform one another [R3]" | ch01:§1 | ReAct (arXiv:2210.03629) | Yes — abstract confirms "generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two" |
| "relevant material in the middle of long inputs could be used less reliably than material near the beginning or end [R4]" | ch02:§2 | Lost in the Middle (arXiv:2307.03172) | Yes — abstract confirms "performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle" |
| "ToolEmu was created because testing agents against high-stakes tools in real environments is expensive and risky [R6]" | ch01:§1 | ToolEmu (arXiv:2309.15817) | Yes — abstract confirms "testing agents against high-stakes tools in real environments is expensive and risky" |
| "Kadavath and colleagues found encouraging calibration for some formats and tasks, while cross-task generalization for knowing-what-is-known remained imperfect [R8]" | ch05:§4 | Kadavath et al. (arXiv:2207.05221) | Yes — abstract confirms "Performance at self-evaluation further improves" and "they struggle with calibration of P(IK) on new tasks" |
| "Git's `status` command exists to show differences among the current commit, the index, and the working tree [R10]" | ch01:§4 | git-status docs (git-scm.com) | Yes — documentation confirms "Displays paths that have differences between the index file and the current HEAD commit, paths that have differences between the working tree and the index file" |
| "restoring a tracked path absent from the restore source removes it to make the working tree match that source [R11]" | ch04:§3 | git-restore docs (git-scm.com) | Yes — documentation states "If a path is tracked but does not exist in the restore source, it will be removed to match the source" |
| "C2PA can bind assertions about an asset's source and history in a tamper-evident manifest [R12]" | ch05:§5 | C2PA spec 2.2 | Yes — C2PA standard addresses "technical standards for certifying the source and history (or provenance) of media content" |
| "NIST's AI Risk Management Framework likewise treats risk management as a continuous practice organized around Govern, Map, Measure, and Manage [R1]" | ch01:§1 | NIST AI RMF 1.0 (NIST AI 100-1) | Yes — AI RMF 1.0 organizes around GOVERN, MAP, MEASURE, and MANAGE core functions |
| "GPT-5.6 Sol" is a real model identifier on the OpenAI platform [R13] | provenance.md | OpenAI model catalog | Yes — model ID `gpt-5.6-sol` confirmed at developers.openai.com/api/docs/models/gpt-5.6-sol |

## Scores (1–5)

accuracy: 5 · clarity: 5 · completeness-for-tier: 5 · density: 5 · originality: 4
