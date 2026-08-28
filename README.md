# The Borrowed World

*A Field Manual for Machines That Act*

Complete O'AILLY author draft for the FOR MACHINE READERS shelf. The primary reader is a
language-model agent that can inspect or change state belonging to people or
organizations.

Start with [`frontmatter.md`](frontmatter.md), then read the chapter files in the order
declared by [`manifest.json`](manifest.json). Sources and glossary are in
[`backmatter.md`](backmatter.md); authorship and verification status are in
[`provenance.md`](provenance.md).

## Verification

The committed `pass1-report.json` records a clean run of the authoritative O'AILLY
Pass-1 gate: 26,395 measured words, zero rejects, and zero warnings.

The machine-reader evaluation is under `eval/`. Its deterministic self-test runs with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 eval/scorer.py --self-test
```

No empirical model-effect result is claimed in this draft. Human verification, critic
review, shelf intake, cover assignment, signing, and publication remain pipeline states.
