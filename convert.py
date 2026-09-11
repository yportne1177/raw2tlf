#!/usr/bin/env python3
import argparse, yaml, pandas as pd
from pathlib import Path

def load_mapping(path):
    with open(path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)

def apply_mapping(df, mapping):
    out = pd.DataFrame()
    cols = mapping.get("columns", {})
    for out_col, spec in cols.items():
        if isinstance(spec, str):
            out[out_col] = df.get(spec)
        elif isinstance(spec, dict) and spec.get("type") == "const":
            out[out_col] = spec.get("value")
        elif isinstance(spec, dict) and spec.get("type") == "expr":
            out[out_col] = df.eval(spec.get("value"))
        else:
            out[out_col] = None
    filters = mapping.get("filters", [])
    for f in filters:
        col, op, val = f["column"], f["op"], f["value"]
        if op == "==": out = out[df[col] == val]
        if op == "!=": out = out[df[col] != val]
        if op == ">": out = out[df[col] > val]
        if op == "<": out = out[df[col] < val]
    return out

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mapping", required=True)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    mapping = load_mapping(args.mapping)
    df = pd.read_csv(args.input)
    out = apply_mapping(df, mapping)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.output, index=False)
    print(f"Wrote {args.output} ({len(out)} rows)")

if __name__ == "__main__":
    main()
