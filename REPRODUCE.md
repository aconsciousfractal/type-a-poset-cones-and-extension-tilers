# Reproduce The Paper Artifacts

Snapshot date: 2026-06-06.

## Environment

- Python 3.10 or newer.
- A LaTeX installation with `pdflatex` and `bibtex`.
- No third-party Python packages are required for the included verification
  scripts.

```bash
pip install -r requirements.txt
```

The requirements file is intentionally empty except for comments.

## Build The Paper

From `paper/`:

```bash
pdflatex -interaction=nonstopmode -halt-on-error "Type-A Poset Cones and Extension Tilers.tex"
bibtex "Type-A Poset Cones and Extension Tilers"
pdflatex -interaction=nonstopmode -halt-on-error "Type-A Poset Cones and Extension Tilers.tex"
pdflatex -interaction=nonstopmode -halt-on-error "Type-A Poset Cones and Extension Tilers.tex"
```

Current canonical PDF:

```text
paper/Type-A Poset Cones and Extension Tilers.pdf
pages = 15
bytes = 404972
sha256 = 5FC09ECC3EAC9DD4CB3FC75B463FD15185C18D00E95A0371918E5F97AB913632
```

The paper source is `paper/Type-A Poset Cones and Extension Tilers.tex`.

## Verify The S6 Counterexample

From the repository root:

```bash
python scripts/verify_s6_p038_biset_counterexample.py
```

Expected output:

```text
|L(P)| = 15
|H| = 8
|K| = 6
|HK| = 24
|H tau K| = 24
|HK cap H tau K| = 0
|A| = 48
covered = 720 / 720
multiplicities = [1]
induced N copies = 4
PASS
```

## Replay The S5 Audit

From the repository root:

```bash
python scripts/replay_s5_extension_tiler_audit.py
```

Expected tail:

```text
For the |L(P)| = 8 type:
  distinct left translates = 120
  candidates disjoint from base translate = 96
  maximum packing containing base translate = 14
  tiling would require = 15

PASS
```

## Validate Static S6 Status Data

```bash
python -m json.tool certificates/s6_classification_status.json
```

The Markdown companion is:

```text
certificates/s6_classification_status.md
```

## Manifest

The root file `MANIFEST_SHA256.txt` contains SHA-256 hashes for every file in
this public staging package.
