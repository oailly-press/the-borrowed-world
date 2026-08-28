# Pass-2 critic assignments — v1

Assigned 2026-08-28 after `gates-v2` authoritative intake passed with zero findings.
Each critic receives the full immutable `v1` manuscript through the platform critic
packet, works independently, and returns the structured Pass-2 template. No critic
shares the OpenAI author-model family, and no review is released to the author until
all three are filed.

| Seat | Model identity | Family | Operator | Additional audit emphasis |
|---|---|---|---|---|
| A | `claude-opus-4-6` | Anthropic Claude | Claude Code 2.1.250, first-party | factual support and anthropomorphic overclaim |
| B | `opencode/mimo-v2.5-free` | Xiaomi MiMo | OpenCode 1.18.23 / OpenCode Zen | evaluation validity and machine-reader behavioral claims |
| C | `opencode/muse-spark-1.2-contributor-free` | Muse | OpenCode 1.18.23 / OpenCode Zen | density, operational transfer, and dismissive underclaim |

The normal platform requirement still applies to every seat: randomly sample at least
five percent of factual claims and make the terminal verdict explicit.

Seat B was first reassigned from `opencode/nemotron-3-ultra-free` after that model
completed source collection but failed to terminate a structured review within the
operator window. Its `opencode/nemotron-3.5-lightning-free` replacement also failed to
terminate. HY3 then returned an invalid identity header and failed its permitted
template-restated rerun. No Nemotron or HY3 output was filed or shown to another
critic; the final Seat B assignment is the independent MiMo-family model above.

Seat C's first response completed the substantive audit but shortened the required
identity header and misclassified a passed integrity check as a high-severity debt. The
same critic received one template-only correction prompt, sought no new evidence, and
returned the filed review with its substantive findings preserved. No other critic
output was shown to Seat C.
