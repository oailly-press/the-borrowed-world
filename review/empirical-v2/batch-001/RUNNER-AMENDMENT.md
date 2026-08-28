# Runner amendment after infrastructure stop

The first batch invocation stopped on 2026-08-28 after all 20 run-01 baseline cases
returned terminal, parsed output. When the runner began the first full-book condition,
Python raised operating-system error `Errno 7: Argument list too long` before launching
any model process because the treatment was passed as a command-line argument.

No full-book case was sent. No response was scored, replaced, or inspected to select a
different treatment, model, seed, or criterion. The 20 baseline raw records remain the
run-01 baseline and are resumed without regeneration.

Transport-only amendment:

- send the byte-identical prompt through process stdin instead of the argument vector;
- reuse any existing per-case raw record on resume;
- preserve `OSError` as an infrastructure attempt instead of crashing the batch; and
- preserve the original batch manifest timestamp on resume.

The neutral instruction, treatment bytes and hash, cases, condition order, model,
permissions, extraction rule, scorer, and pre-registered efficacy criteria are unchanged.
