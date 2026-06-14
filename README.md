# Type-A Poset Cones and Extension Tilers

Public staging package for the paper:

```text
Type-A Poset Cones and Extension Tilers
Oleksiy Babanskyy, 2026
```

The paper studies chamber-unions in the type-A Coxeter complex via the
dictionary between braid-arrangement halfspaces and finite posets.  A poset
`P` gives a tile `L(P)` inside the symmetric group.  The main results in this
snapshot are:

- every finite series-parallel poset is an extension tiler;
- for `S5`, the extension tilers are exactly the series-parallel posets;
- in `S6`, the converse fails: candidate `P038` is a non-series-parallel
  extension tiler with a compact double-coset witness;
- the `P038` witness also gives a coordinate-permutation tiling of `[0,1]^6`
  by 48 copies of its order polytope, via the standard cube triangulation;
- the broader `S6` audit records a structured `19/38` laboratory split among
  the `57` divisible non-series-parallel candidates, but this split is not
  promoted to a theorem in this paper.

## Repository Layout

```text
.
|-- paper/             LaTeX source, bibliography, sections, and PDFs
|-- scripts/           Self-contained finite verification scripts
|-- certificates/      Static audit records and claim-boundary data
|-- docs/              Reviewer-facing claim ledger and red-team notes
|-- README.md
|-- README_REVIEWER.md
|-- REPRODUCE.md
|-- CITATION.cff
|-- LICENSE
|-- requirements.txt
`-- MANIFEST_SHA256.txt
```

## Quick Start

No Python package dependencies are required for the included verification
scripts.

```bash
python scripts/verify_s6_p038_biset_counterexample.py
python scripts/replay_s5_extension_tiler_audit.py
python -m json.tool certificates/s6_classification_status.json
```

To rebuild the paper, use a standard LaTeX installation with `pdflatex` and
`bibtex`:

```bash
cd paper
pdflatex -interaction=nonstopmode -halt-on-error "Type-A Poset Cones and Extension Tilers.tex"
bibtex "Type-A Poset Cones and Extension Tilers"
pdflatex -interaction=nonstopmode -halt-on-error "Type-A Poset Cones and Extension Tilers.tex"
pdflatex -interaction=nonstopmode -halt-on-error "Type-A Poset Cones and Extension Tilers.tex"
```

## Claim Boundary

The theorem-level objects are the `S5` classification, the explicit `S6`
counterexample `P038`, and the order-polytope cube-tiling corollary that
follows from the same factorization.  The broader `S6` table is retained as
audit-level laboratory status because five obstruction-side cases still lack
compact portable certificates:

```text
001, 013, 017, 019, 020
```

See `docs/PUBLIC_CLAIM_BOUNDARY.md` and `docs/CLAIM_LEDGER.md`.

## Citation

See `CITATION.cff`.

## License

Code is released under the MIT license.  Paper text and PDF artifacts under
`paper/` are released under CC-BY-4.0; see `LICENSE`.
