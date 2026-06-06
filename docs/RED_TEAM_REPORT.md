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
