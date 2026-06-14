# Red-Team Report

Snapshot date: 2026-06-06.

## Scope

The final readthrough checked the paper-facing claim boundary, the `S5`
classification statement, the `S6` counterexample, and the audit-level `S6`
laboratory status section.

## Outcome

Verdict after fixes:

```text
GO after minor fixes
```

No theorem-level blocker remained after the fixes below.

## Fixes Applied

- The `S6` section title was changed from classification language to
  audit-level status language.
- The `19/38` split is consistently described as laboratory status, not as a
  promoted theorem.
- The `S6` status note no longer says that source scripts need to be
  regenerated; it now says the remaining gap is certificate compression for
  the five hard obstruction-side cases.
- The Valdes--Tarjan--Lawler citation is used with explicit wording: the
  characterization is applied to the transitive directed comparability graph
  of the poset.
- The right-hand symmetry of the `P038` witness is presented as a verified
  finite witness observation, not as an unexplained general theorem.

## Remaining Open Compression Target

The only non-paper-grade part of the broader `S6` audit is the certificate
compression problem for:

```text
001, 013, 017, 019, 020
```

These are not needed for the theorem-level `P038` counterexample.

## 2026-06-14 Addendum - Order-Polytope Cube Tiling

Scope: checked the new `Order-Polytope Cube Tilings` section and its public
claim-boundary updates.

Verdict:

```text
GO
```

Checks:

- The new theorem-level statement is a deterministic consequence of
  `S_X = disjoint union a L(P)` and the standard cube triangulation.
- The `P038` corollary uses the already verified `48 * 15 = 720`
  factorization; it does not add a new finite search claim.
- The paper does not include the exploratory PAPP flux, OBJ, or tube-mesh
  artifacts as proof figures.
- The wording distinguishes coordinate-permutation cube tilings from arbitrary
  Euclidean congruent-copy tilings.
- The broader `S6` `19/38` laboratory split remains audit-level only.

Verification run:

```text
pdflatex/bibtex/pdflatex/pdflatex: PASS
scripts/verify_s6_p038_biset_counterexample.py: PASS
scripts/replay_s5_extension_tiler_audit.py: PASS
python -m json.tool certificates/s6_classification_status.json: PASS
MANIFEST_SHA256.txt: PASS
```
