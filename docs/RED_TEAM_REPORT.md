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

## 2026-06-14 External Red-Team Follow-Up

Scope: checked an external readthrough of the order-polytope corollary,
abstract, data availability statement, and audit-level `S6` wording.

Verdict:

```text
GO after wording fixes
```

Fixes applied:

- The abstract now says the cube tiling holds up to shared faces of the
  standard triangulation.
- The five hard obstruction-side rows are described as negative audit rows
  still lacking compact independent certificates, not as theorem-level
  exclusions with compact paper certificates.
- The `S6` status table separates `audit-unclassified survivors = 0` from
  the five negative rows still lacking compact independent certificates.
- The defect-one residual packing statement is explicitly attributed to the
  audit computation and audit data.
- The order-polytope coordinate action now defines `T_a` before using
  `a O(P)`.
- The corollary introduces `P038` as the supplementary enumeration label.
- Internal visualization language was removed from the proof-facing text.
- The data/code statement now includes the public repository URL and points
  standalone readers to the manifest hashes.

Verification run after follow-up fixes:

```text
pdflatex/pdflatex: PASS
scripts/verify_s6_p038_biset_counterexample.py: PASS
scripts/replay_s5_extension_tiler_audit.py: PASS
python -m json.tool certificates/s6_classification_status.json: PASS
MANIFEST_SHA256.txt: PASS
LaTeX log red-team scan: PASS
fragile-wording scan: PASS
```
