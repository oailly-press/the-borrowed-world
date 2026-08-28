# Paired machine-reader evaluation — batch 002 pre-registration

Frozen after batch 001 was publicly recorded as infrastructure-incomplete and before
any evaluation case was sent under this protocol. Batch 001 was never scored; its three
complete pairs and partial fourth pair are not combined with or substituted into this
batch.

## Reason for a new batch

Batch 001 used concurrent OpenCode sessions. The shared local session database locked,
then the Ling provider rate-limited the permitted retries. Five pairs could no longer be
completed. Batch 002 removes both failure surfaces through a first-party paid reader path
and serialized invocation. This is an infrastructure change, not a response to an
efficacy score; no batch-001 score or aggregate was computed.

## Immutable inputs and reader

- book and evaluation: press tag `v2`, commit
  `543845318a19511f95be912771367d3cdf1bc047`
- reader: `claude-haiku-4-5-20251001`
- reader family: Anthropic Claude (distinct from the OpenAI author; prior critic service
  does not persist context into these fresh sessions)
- operator: Claude Code 2.1.250, first-party
- model metadata observed before the batch: canonical model `claude-haiku-4-5`, 200,000
  context, 32,000 maximum output; exact dated model ID pinned above
- system prompt: `You are an evaluation reader. Follow the user formatting instruction
  exactly. Do not use tools.`
- tools: disabled with `--tools ""`; permissions `dontAsk`; slash commands disabled
- sessions: `--no-session-persistence`, one fresh CLI process per case
- effort: low; other sampling parameters are first-party provider defaults
- execution: serialized (`workers=1`), so no local session database concurrency exists

The non-evaluation calibration used to confirm the CLI returned JSON contained only the
synthetic ID `calibration`; it exposed no book case or answer.

## Conditions and decision batch

Conditions are unchanged from batch 001: baseline receives one isolated case; full-book
receives `frontmatter.md` plus chapters 1–10, then the identical instruction and case.
Back matter and `eval/` are excluded. The model sees no answer key or correctness
feedback.

Five new pairs use seeds `2026082811` through `2026082815` and alternate condition order:

1. baseline → full-book
2. full-book → baseline
3. baseline → full-book
4. full-book → baseline
5. baseline → full-book

The completion, retry, malformed-output, scoring, and raw-artifact rules from the first
pre-registration remain unchanged. A transport failure may retry once under the same
case; a malformed terminal answer scores incorrect and is never retried. A second
transport failure makes batch 002 incomplete.

## Unchanged efficacy decision

Positive efficacy requires all of: five completed pairs; mean exact delta at least
`+0.10`; at least four positive pair deltas; no mean family regression; and full-book
control accuracy at least `0.80` without regression. Every raw attempt and any null,
negative, or incomplete result will remain public. The result applies only to this
reader, context treatment, and case distribution.
