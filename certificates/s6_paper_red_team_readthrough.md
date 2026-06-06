# S6 Paper Red-Team Readthrough

Date: 2026-06-06

## Classification

Internal manuscript red-team pass for the Type-A extension-tiler paper after
the S6 counterexample and S6 laboratory-status integration.

This pass is not a new mathematical proof phase.  It checks claim hygiene,
finite-audit boundaries, LaTeX build health, trigger phrases, and code/paper
alignment under the local PAPP red-team rules used during preparation.

## Scope

Manuscript:

```text
paper/Type-A Poset Cones and Extension Tilers.tex
paper/sections/*.tex
```

Primary supplementary artifacts:

```text
scripts/verify_s6_p038_biset_counterexample.py
certificates/s6_classification_status.md
certificates/s6_classification_status.json
certificates/legacy_colab_artifacts.md
```

## PAPP Red-Team Checks

| ID | Check | Result |
| --- | --- | --- |
| RT-1 | source mismatch | No blocker found in the edited paper scope. |
| RT-2 | notation drift | No blocker found; left action convention is stated in the S6 theorem proof. |
| RT-3 | normalization error | No blocker found; P038 verifier uses the same left action convention. |
| RT-4 | theorem import abuse | No new theorem import introduced. |
| RT-5 | finite replay overclaim | Mitigated: full S6 classification is labelled laboratory status, not theorem. |
| RT-6 | numeric precision overclaim | Not applicable; computations are finite/exact. |
| RT-7 | missing exception | Mitigated: the five hard S6 cases are explicitly listed. |
| RT-8 | artifact not reproducible | P038 verifier is reproducible; five hard-case Colab logs are marked non-certificates. |
| RT-9 | code/paper mismatch | P038 verifier output matches the theorem statement. |
| RT-10 | public claim mismatch | Mitigated: abstract says the audit has five obstruction-side cases lacking short certificates. |
| RT-11 | agent excessive agency | Mitigated: external-agent/Colab outputs are not promoted as proof. |
| RT-12 | prompt/source injection | Not applicable to the paper text. |
| RT-13 | copyright/license breach | No long external quotations or external copyrighted payloads added. |
| RT-14 | false cross-field bridge | No bridge theorem is claimed from external literature. |
| RT-15 | stale external data/citation drift | No new external date-sensitive citation added in this pass. |

## Edits Made In Response

The paper now includes a dedicated section:

```text
Audit-Level S6 Laboratory Status
```

This section records the current audit state:

```text
57 non-series-parallel divisible candidates
19 non-series-parallel tilers
38 obstruction-side non-tilers
0 unresolved survivors in the audit
```

The section explicitly prevents overclaim by saying this is audit-level
laboratory status data, not a theorem of the paper.  It also lists the five
remaining certificate-compression cases:

```text
001, 013, 017, 019, 020
```

The computational appendix now points to:

```text
certificates/s6_classification_status.md
certificates/legacy_colab_artifacts.md
```

## Commands Run

```text
python scripts/verify_s6_p038_biset_counterexample.py
pdflatex -interaction=nonstopmode -halt-on-error "Type-A Poset Cones and Extension Tilers.tex"
python -m json.tool certificates/s6_classification_status.json
Select-String paper/**/*.tex "paper/Type-A Poset Cones and Extension Tilers.tex" for task markers and stale overclaim phrases
Select-String paper/*.log for LaTeX warnings, undefined references, citations, overfull/underfull boxes, rerun warnings
```

## Verification Result

P038 verifier:

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

LaTeX:

```text
paper PDF pages = 15
paper PDF bytes = 404972
undefined_reference_count = 0
citation_warning_count = 0
meaningful_latex_warning_count = 0
overfull_underfull_count = 0
```

MiKTeX emitted a local update notice.  This is an environment notice, not a
manuscript warning.

Trigger phrase sweep:

```text
task-marker/internal stale marker hits = 0
stale S6 overclaim phrase hits = 0
```

## Decision

No paper-blocking red-team issue remains for the current claim boundary.

A second external red-team pass was accepted on the same date.  The paper was
updated so that the abstract no longer advertises a missing S5 replay script,
the S6 laboratory terms are defined explicitly, the S6 rows are tied to the
curated JSON snapshot rather than legacy Colab artifacts, the companion
tetrahedron manuscript is cited, and a data/code availability paragraph records
the exact local artifact boundary.

Safe current paper-level claims:

```text
S5: extension tilers are exactly series-parallel posets.
S6: the series-parallel converse is false.
S6: P038 is a verified non-series-parallel extension tiler.
S6 lab: current finite audit reports 19 non-SP tilers and 38 obstruction-side
        candidates among the 57 non-SP divisible candidates.
```

Not promoted to theorem in this paper:

```text
The full S6 19/38 classification as a paper-grade theorem.
The five hard obstruction cases as compact mathematical lemmas.
The Colab/RoundingSat timeout logs as certificates.
```

## Recommended Next Action

Either:

```text
1. polish the current paper with this conservative S6 laboratory section; or
2. start a separate certificate-compression phase for 001,013,017,019,020.
```

The second route should start from residual packing/near-tiling structure, not
from another raw Colab OPB run.
