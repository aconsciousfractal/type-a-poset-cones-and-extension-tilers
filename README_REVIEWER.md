# Reviewer Guide

This package is intended to make the current paper snapshot inspectable with
minimal setup.

## Five-Minute Verification

From the repository root:

```bash
python scripts/verify_s6_p038_biset_counterexample.py
python scripts/verify_p038_order_polytope_geometry.py
python scripts/replay_s5_extension_tiler_audit.py
python -m json.tool certificates/s6_classification_status.json
```

Expected high-level outcomes:

- `verify_s6_p038_biset_counterexample.py` ends with `PASS`.
- `verify_p038_order_polytope_geometry.py` ends with `PASS` and validates
  `certificates/p038_order_polytope_geometry.json`.
- `replay_s5_extension_tiler_audit.py` ends with `PASS`.
- `s6_classification_status.json` parses as valid JSON.

## What Is Theorem-Level Here

The paper promotes:

- the type-A poset-cone dictionary;
- the positive theorem for series-parallel posets;
- the full `S5` classification;
- the explicit non-series-parallel `S6` extension tiler `P038`;
- the type-`A5` Coxeter-complex realization induced by the same `P038`
  factorization;
- the order-polytope tiling of `[0,1]^6` induced by the same `P038`
  factorization.
The finite face-vector and Ehrhart data for `O(P038)` support the last item
but are not promoted as a separate classification or novelty theorem.

## What Is Audit-Level Only

The broader `S6` laboratory table reports:

```text
57 divisible non-series-parallel candidates
19 tiler-side candidates
38 obstruction-side candidates
```

This `19/38` split is not stated as a completed theorem in the paper.  Five
obstruction-side rows still need compact portable certificates:

```text
001, 013, 017, 019, 020
```

## Files To Inspect First

```text
paper/Type-A Poset Cones and Extension Tilers.tex
paper/sections/06-s6-counterexample.tex
paper/sections/07-order-polytope-cube-tilings.tex
paper/sections/07-s6-laboratory.tex
docs/CLAIM_LEDGER.md
docs/PUBLIC_CLAIM_BOUNDARY.md
scripts/verify_s6_p038_biset_counterexample.py
scripts/verify_p038_order_polytope_geometry.py
```
