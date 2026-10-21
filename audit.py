#!/usr/bin/env python3
"""Audit which layers of Perplexity Computer are published as source.

Reads sources.json, fetches every layer's source URL, and writes snapshot.json
with the layer table plus what each source said when it was fetched.
`--diff` compares this run with an earlier snapshot and prints what changed.

Usage:
  python3 audit.py
  python3 audit.py --diff snapshot-2026-10-21.json

A source answering 401/403/429 is a bot check, not a missing page: it is
recorded in the snapshot and does not fail the run.

Exit codes: 0 clean, 1 a source is unreachable (404/410/network) or a layer has
no source URL.

Python 3.9+, standard library only.
"""
from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCES = HERE / "sources.json"
SNAPSHOT = HERE / "snapshot.json"
TIMEOUT = 20
UA = (
    "Mozilla/5.0 (compatible; perplexity-computer-source-audit/1.0; "
    "+https://github.com/ArtemShatokhin/perplexity-computer-source-audit)"
)
VALID = {"yes", "no", "partial"}


def load(path: Path) -> list:
    with path.open(encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data, list):
        raise SystemExit(f"{path.name}: expected a list of layers")
    return data


def fetch(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return {
                "url": url,
                "status": resp.status,
                "final_url": resp.geturl(),
                "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            }
    except urllib.error.HTTPError as exc:
        # 401/403/429 are bot checks, not missing pages: the answer is checked in
        # a browser, so they are recorded and do not fail the run.
        blocked = exc.code in (401, 403, 429)
        return {
            "url": url,
            "status": exc.code,
            "final_url": url,
            "blocked_by_bot_check": blocked,
            "error": str(exc),
        }
    except Exception as exc:  # noqa: BLE001 - a failed fetch is an audit result
        return {"url": url, "status": None, "final_url": url, "error": str(exc)}


def run() -> int:
    layers = load(SOURCES)
    problems: list[str] = []
    rows = []
    for layer in layers:
        for key in ("layer", "name", "open", "what_is_published", "source_url", "checked"):
            if not layer.get(key):
                problems.append(f"{layer.get('layer', '?')}: missing {key}")
        if layer.get("open") not in VALID:
            problems.append(f"{layer.get('layer', '?')}: open must be one of {sorted(VALID)}")
        url = layer.get("source_url") or ""
        if not url.startswith("https://"):
            problems.append(f"{layer.get('layer', '?')}: source_url must be https")
            continue
        result = fetch(url)
        status = result.get("status")
        if status != 200 and not result.get("blocked_by_bot_check"):
            problems.append(f"{layer['layer']}: source unreachable ({status})")
        rows.append({**layer, "source": result})

    snapshot = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "layers": rows,
    }
    SNAPSHOT.write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")

    for row in rows:
        status = row["source"].get("status")
        if row["source"].get("blocked_by_bot_check"):
            status = f"{status} (bot check, open in a browser)"
        mark = "PUBLISHED" if row["open"] == "yes" else ("PARTIAL" if row["open"] == "partial" else "CLOSED")
        print(f"{row['layer']:<13} {mark:<10} source {status}  {row['source_url']}")
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for problem in problems:
            print(f"  {problem}")
        return 1
    print(f"\nwrote {SNAPSHOT.name}: {len(rows)} layers, every source reachable")
    return 0


def diff(previous_path: Path) -> int:
    previous = json.loads(previous_path.read_text(encoding="utf-8"))
    current = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    old = {row["layer"]: row for row in previous.get("layers", [])}
    new = {row["layer"]: row for row in current.get("layers", [])}
    changes = 0
    for layer in sorted(set(old) | set(new)):
        if layer not in old:
            print(f"{layer}: new layer, open={new[layer]['open']}")
            changes += 1
            continue
        if layer not in new:
            print(f"{layer}: dropped from the audit")
            changes += 1
            continue
        before, after = old[layer], new[layer]
        if before.get("open") != after.get("open"):
            print(f"{layer}: open {before.get('open')} -> {after.get('open')}")
            changes += 1
        if before.get("source_url") != after.get("source_url"):
            print(f"{layer}: source moved {before.get('source_url')} -> {after.get('source_url')}")
            changes += 1
        source = after.get("source", {})
        status = source.get("status")
        if status != 200 and not source.get("blocked_by_bot_check"):
            print(f"{layer}: source now unreachable ({status})")
            changes += 1
    if not changes:
        print(f"no change since {previous.get('generated_at', previous_path.name)}")
    return 0


def main() -> int:
    if "--diff" in sys.argv:
        index = sys.argv.index("--diff")
        if index + 1 >= len(sys.argv):
            print(__doc__)
            return 2
        return diff(Path(sys.argv[index + 1]))
    return run()


if __name__ == "__main__":
    sys.exit(main())
