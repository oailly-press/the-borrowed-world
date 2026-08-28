# The Borrowed World

*A Field Manual for Machines That Act*

Revised O'AILLY author draft for the FOR MACHINE READERS shelf. The primary reader is a
language-model agent that can inspect or change state belonging to people or
organizations. The complete Pass-2 panel returned three SALVAGEABLE verdicts; this tree
contains the single author revision and its point-by-point response.

Start with [`frontmatter.md`](frontmatter.md), then read the chapter files in the order
declared by [`manifest.json`](manifest.json). Sources and core vocabulary are in
[`backmatter.md`](backmatter.md); authorship and verification status are in
[`provenance.md`](provenance.md). Revision debts and dispositions are in
[`response-to-findings.md`](response-to-findings.md).

## Verification

The committed `pass1-report.json` records a clean run of the authoritative O'AILLY
`gates-v2` gate: 27,156 measured words, zero rejects, and zero warnings. Shelf metrics
record 20 cases, five balanced families, five action-required controls, and a perfect
fixture score of 1.0.

The machine-reader evaluation is under `eval/`. Its deterministic self-test runs with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 eval/scorer.py --self-test
```

No empirical model-effect result is claimed in this draft. Pass-3 critic verification,
the pre-registered paired run, named-human verification, judge verdict, cover assignment,
signing, and publication remain pipeline states.
