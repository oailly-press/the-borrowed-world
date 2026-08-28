#!/usr/bin/env python3
"""Export an answer-key-free, optionally shuffled JSONL prompt set."""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

from scorer import DEFAULT_CASES, load_cases


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    cases = load_cases(args.cases)
    random.Random(args.seed).shuffle(cases)
    lines = []
    for case in cases:
        lines.append(json.dumps({
            "id": case["id"],
            "prompt": case["prompt"],
            "options": {
                label: option["text"] for label, option in case["options"].items()
            },
        }, ensure_ascii=False))
    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {len(lines)} prompts to {args.output} with seed {args.seed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
