#!/usr/bin/env python3
"""Run the independent scientific checks against their committed references."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", action="store_true",
                        help="intentionally refresh references after independent checks pass")
    args = parser.parse_args()
    directory = Path(__file__).resolve().parent
    results = {}
    for name in ("check_collision.py", "check_receiver.py", "check_direct_imaging.py"):
        command = [sys.executable, str(directory / name)]
        if args.record:
            command.append("--record")
        completed = subprocess.run(command, text=True, capture_output=True)
        if completed.returncode:
            print(completed.stdout, end="", file=sys.stderr)
            print(completed.stderr, end="", file=sys.stderr)
            raise SystemExit(f"FAILED: {name} (exit {completed.returncode})")
        results[name] = json.loads(completed.stdout)
    print(json.dumps({
        "status": "recorded" if args.record else "passed",
        "checks": results,
        "meaning": "Finite independent consistency checks; analytic proofs establish uniform minimax bounds."
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
