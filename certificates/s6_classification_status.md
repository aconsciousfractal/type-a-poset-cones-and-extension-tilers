# S6 Classification Status

Date: 2026-08-04

This note separates paper-grade facts from computational laboratory status for
the six-element extension-tiler problem.

## Paper-Grade Result Available Now

The old converse

```text
extension tiler => series-parallel
```

is false in `S_6`.

The verified counterexample is the six-element poset `P038` with covers:

```text
0 < 1
1 < 2
1 < 3
4 < 3
4 < 5
5 < 2
```

It has:

```text
|L(P038)| = 15
induced N copies = 4
```

Thus it is not series-parallel.

The multiplier set has the compact form:

```text
A = H K union H tau K
H = < (2 3)(4 5), (0 1)(3 5) >
K = < (2 3)(4 5), (0 4 5)(1 3 2) >
tau = (3 4)
```

with:

```text
|H| = 8
|K| = 6
|HK| = 24
|H tau K| = 24
HK cap H tau K = empty
|A| = 48
```

The translates `a L(P038)`, for `a in A`, partition `S_6`.

Interpreting the elements of `S_6` as chambers of the type-`A5` Coxeter
complex, the same exact factorization gives a 48-piece Coxeter-complex chamber
tiling by translates of the 15-chamber poset cone `C(P038)=L(P038)`.

This is a Coxeter-complex chamber statement.  It is not a full type-`A5` tiler
classification, not an outer-automorphism explanation, and not a metric
rigidity or full face-lattice theorem.

By the standard simplex triangulation of the unit cube, the same
factorization also gives a coordinate-permutation tiling of `[0,1]^6` by 48
copies of the order polytope `O(P038)`.

Verifier:

```text
scripts/verify_s6_p038_biset_counterexample.py
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

## S6 Laboratory Status

The working S6 laboratory classification reached:

```text
57 non-series-parallel divisible candidates
19 non-series-parallel tilers
38 obstruction-side non-tilers
0 unresolved/survivors
```

This is laboratory/computational status, not a paper-grade theorem in the
current repository snapshot.  The remaining gap is certificate compression for
the five hard obstruction-side cases, not the theorem-level P038 counterexample
or the S5 replay.

## Obstruction Grammar Already Identified

Most obstruction-side cases were assigned to interpretable families:

```text
terminal block
endpoint pair
endpoint-local 3-3-2
positional gcd
single-position balance
ordered-pair balance
mod-3 peak/threshold in low partition modules
```

These families are plausible paper-grade material once the clean scripts and
certificate tables are regenerated.

## Remaining Hard Cases

The five cases still lacking compact paper-grade certificates are:

```text
001
013
017
019
020
```

They are defect-one residual packing obstructions.

| candidate | `|L(P)|` | required tiles | target residual clique | known max residual clique | residual vertices | nonedge constraints |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `001` | 48 | 15 | 14 | 13 | 488 | 42850 |
| `013` | 24 | 30 | 29 | 28 | 313 | 6554 |
| `017` | 24 | 30 | 29 | 28 | 314 | 6498 |
| `019` | 24 | 30 | 29 | 28 | 314 | 6498 |
| `020` | 24 | 30 | 29 | 28 | 313 | 6554 |

These rows are retained only as bounded computational status.  They are not
used as proof of a theorem in this paper, and no portable certificate is
claimed for them.  The full `19/38` split remains a laboratory-status
statement until the five hard packing obstructions have compact independently
checkable certificates.
