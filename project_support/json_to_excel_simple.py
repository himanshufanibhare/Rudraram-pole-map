#!/usr/bin/env python3
"""Minimal JSON -> Excel converter without argparse.

Usage:
  python json_to_excel_simple.py           # convert all .json in cwd
  python json_to_excel_simple.py file.json # convert a single file
  python json_to_excel_simple.py dir/      # convert all .json in directory
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def convert(path: Path) -> Path:
    import pandas as pd

    with path.open("r", encoding="utf-8") as fh:
        data = json.load(fh)

    if isinstance(data, list):
        df = pd.DataFrame(data)
    elif isinstance(data, dict):
        try:
            df = pd.DataFrame(data)
            if df.empty:
                raise ValueError
        except Exception:
            df = pd.json_normalize(data)
    else:
        df = pd.json_normalize(data)

    out = path.with_suffix(".xlsx")
    df.to_excel(out, index=False)
    return out


def main() -> int:
    args = sys.argv[1:]
    if args:
        p = Path(args[0])
        if p.is_dir():
            targets = sorted(p.glob("*.json"))
        else:
            targets = [p]
    else:
        targets = sorted(Path.cwd().glob("*.json"))

    if not targets:
        print("No JSON files found to convert.")
        return 1

    try:
        import pandas  # noqa: F401
    except Exception:
        print("Missing dependency: pandas (and openpyxl). Install with:\n  pip install pandas openpyxl", file=sys.stderr)
        return 2

    for t in targets:
        try:
            out = convert(t)
            print(f"Converted: {t} -> {out}")
        except Exception as exc:
            print(f"Failed: {t} -> {exc}", file=sys.stderr)
            return 3

    return 0


if __name__ == "__main__":
    raise_code = main()
    sys.exit(raise_code)
