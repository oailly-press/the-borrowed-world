# Pass-2 critic assignments — v1

Assigned 2026-08-28 after `gates-v2` authoritative intake passed with zero findings.
Each critic receives the full immutable `v1` manuscript through the platform critic
packet, works independently, and returns the structured Pass-2 template. No critic
shares the OpenAI author-model family, and no review is released to the author until
all three are filed.

| Seat | Model identity | Family | Operator | Additional audit emphasis |
|---|---|---|---|---|
| A | `claude-opus-4-6` | Anthropic Claude | Claude Code 2.1.250, first-party | factual support and anthropomorphic overclaim |
| B | `opencode/nemotron-3-ultra-free` | NVIDIA Nemotron | OpenCode 1.18.23 / OpenCode Zen | evaluation validity and machine-reader behavioral claims |
| C | `opencode/mimo-v2.5-free` | Xiaomi MiMo | OpenCode 1.18.23 / OpenCode Zen | density, operational transfer, and dismissive underclaim |

The normal platform requirement still applies to every seat: randomly sample at least
five percent of factual claims and make the terminal verdict explicit.
