# S6 Classification Status

Date: 2026-06-14

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

The exported OPB instances ask for one more residual disjoint translate than
the known maximum.  An UNSAT proof for each OPB instance would certify the
packing obstruction.

## Colab/RoundingSat Attempt

The raw OPB route was tested on Colab.  The input-path issues were fixed, and
RoundingSat read the OPB files correctly, but the saved runs did not produce
UNSAT certificates.

Observed saved results:

```text
013: RoundingSat ran and timed out / UNKNOWN
017: RoundingSat ran and timed out / UNKNOWN
020: RoundingSat ran and timed out / UNKNOWN in earlier session
```

Therefore the next step should not be another blind raw OPB run.  The raw OPB
instances are useful exports, but they are not the shortest route to a
paper-grade proof.

## Recommended Next Route For The Five Hard Cases

1. Rebuild clean source scripts for:

```text
packing graph construction
maximum residual clique verification
near-tiling residual extraction
orbit quotient / stabilizer quotient
```

2. Try to compress each defect-one obstruction by:

```text
dual/isomorphism pairing among 013/017/019/020
orbit quotient of the residual packing graph
coloring or clique-cover upper-bound certificates
residual profile obstruction: leftover has tile size but is never a translate
```

3. Use proof-logging PB/SAT only after compression, or with a solver better
suited to maximum clique certificates.

## Paper Recommendation

The current paper should include:

```text
S5 classification theorem
P038 S6 counterexample theorem
P038 order-polytope cube-tiling corollary
corollary: the extension-tiler converse is false
open problem: classify extension tilers, especially the S6 non-SP families
```

The full statement

```text
S6 has exactly 19 non-SP tilers and 38 non-SP non-tilers
```

should remain a laboratory/computational-status statement until the five hard
packing obstructions have portable certificates.
