# Claim Ledger

Snapshot date: 2026-06-06.

## Promoted Claims

### Type-A Poset-Cone Dictionary

Reflecting halfspace constraints in type A correspond to precedence
constraints, and the chambers satisfying a poset `P` are exactly the linear
extensions `L(P)`.

Status: paper theorem/background framework.

### Series-Parallel Posets Tile

Every finite series-parallel poset is an extension tiler.

Status: paper theorem.

Boundary: this is one direction only.  The converse is false in `S6`.

### S5 Classification

For posets on five elements, `L(P)` tiles `S5` by left translates if and only
if `P` is series-parallel.

Status: paper theorem with finite audit support.

### S6 Counterexample P038

The six-element poset `P038` is not series-parallel, but `L(P038)` tiles `S6`
by left translates.

Poset covers:

```text
0<1, 1<2, 1<3, 4<3, 4<5, 5<2
```

Multiplier set:

```text
A = H K union H tau K
H = < (2 3)(4 5), (0 1)(3 5) >
K = < (2 3)(4 5), (0 4 5)(1 3 2) >
tau = (3 4)
```

Verifier:

```text
scripts/verify_s6_p038_biset_counterexample.py
```

Status: paper theorem / exact finite construction.

### Order-Polytope Cube Tiling

Any extension-tiler factorization `S_X = disjoint union a L(P)` induces a
tiling of the unit cube `[0,1]^X` by coordinate-permuted copies of the order
polytope `O(P)`, using the standard simplex triangulation of the cube.

For `P038`, this gives a tiling of `[0,1]^6` by 48 coordinate-permuted copies
of `O(P038)`.

Status: paper corollary / deterministic consequence of the exact finite
construction.

## Audit-Level Claims

### S6 19/38 Laboratory Status

Among the `57` divisible non-series-parallel `S6` candidates, the working
audit records `19` tiler-side and `38` obstruction-side candidates.

Status: audit-level laboratory status data.

Reason not promoted here: five obstruction-side cases still lack compact
portable certificates.

Hard cases:

```text
001, 013, 017, 019, 020
```

## Public Boundary

Can say:

```text
The series-parallel converse is false in S6.
P038 is a compact non-series-parallel extension tiler.
P038 also gives a 48-piece order-polytope tiling of the 6-cube.
The current S6 laboratory audit reports a structured 19/38 split.
```

Do not say:

```text
The full S6 19/38 split is a paper theorem.
The five hard obstruction-side cases have compact proof certificates.
Historical Colab/RoundingSat runs are proof certificates.
```
