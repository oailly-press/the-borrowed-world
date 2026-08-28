# Batch 001 outcome — infrastructure incomplete

Batch 001 cannot produce an efficacy verdict under its pre-registration.

Preserved records:

- runs 1–3: 120 terminal, parsed responses; three complete pairs
- run 4 full-book: 20 terminal, parsed responses
- run 4 baseline: five cases attempted; all five exhausted the single permitted retry
- run 4 remaining baseline cases: not launched
- run 5: not launched
- total per-case records: 145

The first failed attempt sampled here reported a local OpenCode `database is locked`
error under four-worker concurrency. Its one allowed retry reached the provider and
returned `Rate limit exceeded. Please try again later.` Four neighboring cases followed
the same terminal infrastructure-failure path. Their raw stdout, stderr, durations, and
attempt counts are preserved in `raw/run-04/baseline/`.

At that point the batch could no longer contain five completed pairs. The operator
interrupted the runner to avoid additional provider calls that could not restore
eligibility. Failed cases were not replaced, no sixth pair was added, and no scorer or
aggregate result was run. The existing run-01 baseline response JSONL was regenerated
from its preserved raw records during resume; only JSON object key order changed, not
any model-selected `id` or `choice`.

This is not a null or negative efficacy result; it is an infrastructure-incomplete
experiment. It cannot support a positive efficacy claim and must remain visible. A
future attempt, if authorized, requires a separately frozen protocol that prevents the
local database collision and respects provider limits. It may not relabel or erase this
batch.
