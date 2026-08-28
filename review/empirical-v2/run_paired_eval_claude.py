#!/usr/bin/env python3
"""Claude first-party adapter for pre-registered paired-evaluation batch 002."""

from __future__ import annotations

import json
import os
import subprocess
import time
from pathlib import Path

import run_paired_eval as core


MODEL = "claude-haiku-4-5-20251001"
MODEL_IDENTITY = (
    "claude-haiku-4-5-20251001 · Anthropic Claude Haiku 4.5 · "
    "Claude Code 2.1.250 (first-party)"
)
SYSTEM_PROMPT = (
    "You are an evaluation reader. Follow the user formatting instruction exactly. "
    "Do not use tools."
)
SEEDS = [2026082811, 2026082812, 2026082813, 2026082814, 2026082815]
CONDITION_ORDERS = [
    ["baseline", "full_book"],
    ["full_book", "baseline"],
    ["baseline", "full_book"],
    ["full_book", "baseline"],
    ["baseline", "full_book"],
]


def invoke(claude: Path, sandbox: Path, prompt: str, case_id: str) -> dict:
    attempts: list[dict] = []
    for attempt_number in (1, 2):
        started = core.utc_now()
        start_clock = time.monotonic()
        try:
            completed = subprocess.run(
                [
                    str(claude), "-p",
                    "--model", MODEL,
                    "--effort", "low",
                    "--output-format", "json",
                    "--no-session-persistence",
                    "--permission-mode", "dontAsk",
                    "--tools", "",
                    "--disable-slash-commands",
                    "--system-prompt", SYSTEM_PROMPT,
                ],
                input=prompt,
                text=True,
                capture_output=True,
                timeout=180,
                cwd=sandbox,
                env=os.environ.copy(),
            )
            wrapper = None
            wrapper_error = None
            try:
                wrapper = json.loads(completed.stdout)
            except json.JSONDecodeError as error:
                wrapper_error = str(error)
            transport_failure = (
                completed.returncode != 0
                or not isinstance(wrapper, dict)
                or bool(wrapper.get("is_error"))
            )
            attempt = {
                "attempt": attempt_number,
                "started_at": started,
                "finished_at": core.utc_now(),
                "duration_seconds": round(time.monotonic() - start_clock, 3),
                "returncode": completed.returncode,
                "stdout": completed.stdout,
                "stderr": completed.stderr,
                "wrapper_parse_error": wrapper_error,
                "transport_failure": transport_failure,
            }
            if isinstance(wrapper, dict):
                attempt["terminal_reason"] = wrapper.get("terminal_reason")
                attempt["model_usage"] = wrapper.get("modelUsage")
                attempt["cost_usd"] = wrapper.get("total_cost_usd")
        except (subprocess.TimeoutExpired, OSError) as error:
            wrapper = None
            attempt = {
                "attempt": attempt_number,
                "started_at": started,
                "finished_at": core.utc_now(),
                "duration_seconds": round(time.monotonic() - start_clock, 3),
                "returncode": None,
                "stdout": getattr(error, "stdout", "") or "",
                "stderr": getattr(error, "stderr", "") or str(error),
                "transport_failure": True,
                "timeout": isinstance(error, subprocess.TimeoutExpired),
            }
        attempts.append(attempt)
        if not attempt["transport_failure"]:
            result_text = wrapper.get("result", "") if isinstance(wrapper, dict) else ""
            extracted, parse_error = core.extract_object(result_text, case_id)
            return {
                "case_id": case_id,
                "attempts": attempts,
                "terminal_output": True,
                "extracted": extracted,
                "parse_error": parse_error,
            }
    return {
        "case_id": case_id,
        "attempts": attempts,
        "terminal_output": False,
        "extracted": None,
        "parse_error": "infrastructure failure after one preserved retry",
    }


def main() -> int:
    core.MODEL = MODEL
    core.MODEL_IDENTITY = MODEL_IDENTITY
    core.SEEDS = SEEDS
    core.CONDITION_ORDERS = CONDITION_ORDERS
    core.invoke = invoke
    return core.main()


if __name__ == "__main__":
    raise SystemExit(main())
