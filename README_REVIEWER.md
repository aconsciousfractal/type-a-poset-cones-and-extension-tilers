# Reviewer Guide

This package is intended to make the current paper snapshot inspectable with
minimal setup.

## Five-Minute Verification

From the repository root:

```bash
python scripts/verify_s6_p038_biset_counterexample.py
python scripts/replay_s5_extension_tiler_audit.py
python -m json.tool certificates/s6_classification_status.json
```

Expected high-level outcomes:

- `verify_s6_p038_biset_counterexample.py` ends with `PASS`.
- `replay_s5_extension_tiler_audit.py` ends with `PASS`.
- `s6_classification_status.json` parses as valid JSON.

## What Is Theorem-Level Here

The paper promotes:

- the type-A poset-cone dictionary;
- the positive theorem for series-parallel posets;
- the full `S5` classification;
- the explicit non-series-parallel `S6` extension tiler `P038`.

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

Historical Colab/RoundingSat artifacts are not proof certificates.  They are
only retained as audit trail notes in `certificates/legacy_colab_artifacts.md`.

## Files To Inspect First

```text
paper/Type-A Poset Cones and Extension Tilers.tex
paper/sections/06-s6-counterexample.tex
paper/sections/07-s6-laboratory.tex
docs/CLAIM_LEDGER.md
docs/PUBLIC_CLAIM_BOUNDARY.md
scripts/verify_s6_p038_biset_counterexample.py
```
