# Named-human verification — The Borrowed World v2

**Status: UNSIGNED — publication is not authorized by this document.**

This sheet makes the final human decision small enough to inspect and precise enough to
audit. It does not treat a request to continue work as approval, and no operator or model
may complete the signature fields for the verifier.

## Release identity

- book: *The Borrowed World: A Field Manual for Machines That Act*
- shelf / tier: FOR MACHINE READERS / pocket
- release manuscript: press tag `v2`
- release commit: `543845318a19511f95be912771367d3cdf1bc047`
- release rule: render manuscript files from tag `v2`; attach review artifacts from the
  press review branch. The review branch is not a substitute manuscript version.
- gate: public `gates-v2` CI run 33188046621 — PASS, 0 rejects, 0 warnings

## Evidence presented to the verifier

- the complete v2 manuscript and provenance/source ledger
- Pass 2 reviews from Claude Opus 4.6, Xiaomi MiMo v2.5, and Muse Spark 1.2
- the author's point-by-point response and the exact v1→v2 delta
- Pass 3 verification from the same three seats: unanimous PUBLISH, no blocking finding
- final report card: all eight Pass-2 blocking findings resolved
- paired batch 001: retained publicly as infrastructure-incomplete and never scored
- paired batch 002: protocol committed before execution; 200/200 terminal and parseable
  case calls, one attempt each, 200 distinct sessions; frozen criterion met
- judge draft and post-draft evidence supplement: model recommendation PUBLISH

## Bounded empirical statement offered for approval

Under the pre-registered batch-002 protocol, the dated reader
`claude-haiku-4-5-20251001` (Claude Code 2.1.250, first-party, tools disabled,
serialized fresh sessions), evaluated on the 20-case, five-family exact-choice fixture
at release commit `543845318a19511f95be912771367d3cdf1bc047`, met the frozen efficacy
criterion: mean paired exact-score delta `+0.18` (threshold `+0.10`), `5/5` positive
pairs, no family regression, and controls `0.80` baseline / `1.00` full-book.

This statement applies only to that reader, case distribution, runner, and date.
Exact-choice scoring is a screening measure. It is not evidence of general agent safety,
domain transfer, durable learning, or live tool execution. Publication is not authorized
to broaden the claim to “the book makes agents safer” or equivalent language.

## Human attestations

The named verifier should approve only after personally confirming each item:

- [ ] I reviewed the v2 manuscript at the exact release commit above sufficiently to
  take responsibility for publication.
- [ ] I reviewed its provenance and source ledger and the critics' fresh source checks;
  I found no unresolved issue that should block publication.
- [ ] I reviewed the authoritative gate result and accept its recorded scope.
- [ ] I reviewed the paired protocol, immutable ordering, raw-artifact completeness,
  scorer result, and limitations; I approve only the bounded statement above.
- [ ] I reviewed the full findings ledger and current model-judge recommendation.
- [ ] My verdict is **PUBLISH**. (If not, do not sign this form; record PUBLISH WITH
  CONDITIONS or REJECT and reasons in `review/judge-verdict.md`.)

## Signature

Human verifier public name: ______________________________

Role / organization: ____________________________________

Signature or explicit signed-off-by notation: ____________

Date (YYYY-MM-DD): ______________________________________

The operator may record a verifier's explicit written attestation here, including a link
or other durable locator, but may never invent, infer, or anonymize it.
