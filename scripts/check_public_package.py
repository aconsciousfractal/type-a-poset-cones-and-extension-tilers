#!/usr/bin/env python3
"""Fail-closed checks for the public release package."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "MANIFEST_SHA256.txt"
TRANSIENT_DIRS = {".git", ".pytest_cache", ".venv", "__pycache__", "tmp"}
TRANSIENT_SUFFIXES = {
    ".aux", ".bbl", ".blg", ".fdb_latexmk", ".fls", ".log", ".out",
    ".pyc", ".synctex.gz",
}
TEXT_SUFFIXES = {".cff", ".json", ".md", ".py", ".tex", ".txt", ".yaml", ".yml"}
RETIRED_PATHS = {
    "certificates/claim_register.md",
    "certificates/legacy_colab_artifacts.md",
    "certificates/s6_paper_red_team_findings.yaml",
    "certificates/s6_paper_red_team_readthrough.md",
    "docs/RED_TEAM_REPORT.md",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def excluded(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    if any(part in TRANSIENT_DIRS for part in rel.parts):
        return True
    return any(path.name.endswith(suffix) for suffix in TRANSIENT_SUFFIXES)


def package_files() -> dict[str, Path]:
    files: dict[str, Path] = {}
    for path in ROOT.rglob("*"):
        if not path.is_file() or path == MANIFEST or excluded(path):
            continue
        files[path.relative_to(ROOT).as_posix()] = path
    return files


def read_manifest() -> dict[str, str]:
    entries: dict[str, str] = {}
    pattern = re.compile(r"^([0-9A-Fa-f]{64})  (.+)$")
    for line_number, line in enumerate(MANIFEST.read_text(encoding="utf-8").splitlines(), 1):
        match = pattern.fullmatch(line)
        if not match:
            raise AssertionError(f"malformed manifest line {line_number}: {line!r}")
        digest, rel = match.groups()
        if rel in entries:
            raise AssertionError(f"duplicate manifest path: {rel}")
        entries[rel] = digest.upper()
    return entries


def check_manifest() -> int:
    expected = read_manifest()
    actual = package_files()
    if set(expected) != set(actual):
        missing = sorted(set(expected) - set(actual))
        unlisted = sorted(set(actual) - set(expected))
        raise AssertionError(f"manifest paths differ; missing={missing}, unlisted={unlisted}")
    mismatches = [rel for rel, path in actual.items() if sha256(path) != expected[rel]]
    if mismatches:
        raise AssertionError(f"manifest hash mismatch: {sorted(mismatches)}")
    return len(expected)


def check_public_surface(files: dict[str, Path]) -> None:
    for rel in RETIRED_PATHS:
        if (ROOT / rel).exists():
            raise AssertionError(f"retired internal file is present: {rel}")

    forbidden = [
        "P" + "APP",
        "Gate" + "-Disciplined",
        "RED" + "_TEAM_REPORT",
        "s6_paper_" + "red_team",
        "legacy_" + "colab",
        "Col" + "ab",
        "Rounding" + "Sat",
        "public " + "staging",
        "agent " + "excessive",
    ]
    hits: list[str] = []
    checker = Path(__file__).resolve()
    for rel, path in files.items():
        if path.resolve() == checker or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        contents = path.read_text(encoding="utf-8")
        for marker in forbidden:
            if marker.lower() in contents.lower():
                hits.append(f"{rel}: {marker}")
    if hits:
        raise AssertionError("forbidden public-surface markers: " + "; ".join(hits))


def check_metadata(files: dict[str, Path]) -> None:
    cff = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    for expected in ['version: "0.2.1"', 'date-released: "2026-08-04"', "/tree/v0.2.1"]:
        if expected not in cff:
            raise AssertionError(f"CITATION.cff missing {expected!r}")

    status = json.loads((ROOT / "certificates/s6_classification_status.json").read_text(encoding="utf-8"))
    lab = status["laboratory_status"]
    counts = (
        lab["non_series_parallel_divisible_candidates"],
        lab["non_series_parallel_tilers"],
        lab["obstruction_side_non_tilers"],
    )
    if counts != (57, 19, 38):
        raise AssertionError("unexpected S6 laboratory counts")
    hard_cases = [row["candidate"] for row in status["hard_cases"]]
    if hard_cases != ["001", "013", "017", "019", "020"]:
        raise AssertionError("unexpected hard-case boundary")

    pdfs = sorted(rel for rel in files if rel.lower().endswith(".pdf"))
    if pdfs != ["paper/Type-A Poset Cones and Extension Tilers.pdf"]:
        raise AssertionError(f"expected exactly the canonical paper PDF, found {pdfs}")


def main() -> int:
    try:
        count = check_manifest()
        files = package_files()
        check_public_surface(files)
        check_metadata(files)
    except (AssertionError, json.JSONDecodeError, OSError, UnicodeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"Manifest OK: {count} entries")
    print("Public surface OK")
    print("Release metadata OK")
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
