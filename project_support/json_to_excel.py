#!/usr/bin/env python3
"""Convert JSON files to Excel (.xlsx) and save them in the same directory.

Usage:
  python json_to_excel.py                # convert all .json in current dir
  python json_to_excel.py file.json     # convert a single file
  python json_to_excel.py dir/ -r       # convert all .json in dir recursively
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def convert_file(path: Path) -> Path:
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


def gather_targets(args) -> list[Path]:
    targets: list[Path] = []
    if args.paths:
        for p in args.paths:
            pth = Path(p)
            if pth.is_dir():
                if args.recursive:
                    targets.extend(sorted(pth.rglob("*.json")))
                else:
                    targets.extend(sorted(pth.glob("*.json")))
            else:
                targets.append(pth)
    else:
        targets = sorted(Path.cwd().glob("*.json"))
    return targets


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert JSON files to Excel files in-place")
    parser.add_argument("paths", nargs="*", help="JSON file(s) or directory(ies) to convert")
    parser.add_argument("-r", "--recursive", action="store_true", help="Recurse into directories")
    args = parser.parse_args()

    try:
        import pandas  # type: ignore
    except Exception:
        print("Missing dependency: pandas (and openpyxl). Install with:\n  pip install pandas openpyxl", file=sys.stderr)
        return 2

    targets = gather_targets(args)
    if not targets:
        print("No JSON files found to convert.")
        return 1

    exit_code = 0
    for t in targets:
        try:
            out = convert_file(t)
            print(f"Converted: {t} -> {out}")
        except Exception as exc:
            print(f"Failed: {t} -> {exc}", file=sys.stderr)
            exit_code = 3

    return exit_code


if __name__ == "__main__":
    raise_code = main()
    sys.exit(raise_code)
