# Reproduce The Paper Artifacts

Snapshot date: 2026-08-04. Release: `v0.2.1`.

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
pages = 18
bytes = 135929
sha256 = 53F2412560787683CA35D02CC1DD4A3BF820D4C1EC79A6D318B850DC6B1C9DCE
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

The type-`A5` Coxeter-complex realization corollary and the order-polytope
cube-tiling corollary in the paper are direct consequences of this same exact
factorization.  No additional visual or numerical artifact is needed for the
tiling proof.

## Verify The P038 Order-Polytope Geometry

The following replay checks supporting data for the single tile
`O(P038)`.  These data make the tile inspectable; they are not a separate
tiling proof and not a classification claim.

The static certificate is:

```text
certificates/p038_order_polytope_geometry.json
```

From the repository root:

```bash
python scripts/verify_p038_order_polytope_geometry.py
```

Expected output:

```text
linear extensions = 15
order ideals / vertices = 13
natural support facets = 10
boundary f-vector = (13, 50, 88, 81, 40, 10)
top face count = 1
h-star = [1, 6, 7, 1, 0, 0, 0]
h-star polynomial = 1 + 6t + 7t^2 + t^3
PASS
```

The default command recomputes the data and checks the static certificate.
After intentional changes, regenerate the certificate with:

```bash
python scripts/verify_p038_order_polytope_geometry.py --write
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

The root file `MANIFEST_SHA256.txt` contains SHA-256 hashes for tracked files
in this public release package, excluding `MANIFEST_SHA256.txt` itself.

On systems with GNU `sha256sum`, validate it with:

```bash
sha256sum -c MANIFEST_SHA256.txt
```

The cross-platform fail-closed package check is:

```bash
python scripts/check_public_package.py
```
