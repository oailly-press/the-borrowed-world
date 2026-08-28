# Pass-3 verification assignments — v2

Assigned 2026-08-28 after revision SHA
`543845318a19511f95be912771367d3cdf1bc047` was imported as tag `v2` and passed
authoritative `gates-v2` CI run 33188046621 with zero findings.

The same Pass-2 panel verified the immutable `v1..v2` delta. Each seat received the full
v2 manuscript and evaluation, the complete diff (including `response-to-findings.md`),
and only its own immutable Pass-2 review. No verifier saw another seat's Pass-3 output
before all three completed.

| Seat | Model identity | Operator | Verification emphasis |
|---|---|---|---|
| A | `claude-opus-4-6` | Claude Code 2.1.250 | A-1, fresh source sample, anthropomorphic overclaim |
| B | `opencode/mimo-v2.5-free` | OpenCode 1.18.23 / OpenCode Zen | full ledger, evaluation validity, behavioral claims |
| C | `opencode/muse-spark-1.2-contributor-free` | OpenCode 1.18.23 / OpenCode Zen | C-1–C-7, density, operational transfer |

Seat B's first completed template mislabeled the manuscript `v3` and omitted C-7 from
the ledger despite verifying its `bw-a02` fix in the fact-check table. The same session
received one template-only correction prompt: title changed to v2 and the already
verified C-7 disposition was added. No new evidence was sought. Filed content otherwise
preserves the completed review.

Seat C printed its assigned identity once before the requested template. The filed
artifact begins at the template heading and preserves the complete review verbatim.
