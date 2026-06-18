# Claim Ledger

Snapshot date: 2026-06-15.

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

### Type-A5 Coxeter-Complex Realization

The `P038` exact factorization
`S6 = disjoint union a L(P038)` also realizes the type-`A5` Coxeter complex
as 48 left translates of a 15-chamber poset cone.

Status: paper corollary / deterministic consequence of the exact finite
construction.

Boundary: this is a Coxeter-complex chamber statement.  It is not a full
classification of type-`A5` tilers, not an outer-automorphism explanation, and
not a metric rigidity or full face-lattice theorem.

### Order-Polytope Cube Tiling

Any extension-tiler factorization `S_X = disjoint union a L(P)` induces a
tiling of the unit cube `[0,1]^X` by coordinate-permuted copies of the order
polytope `O(P)`, using the standard simplex triangulation of the cube.

For `P038`, this gives a tiling of `[0,1]^6` by 48 coordinate-permuted copies
of `O(P038)`.

Status: paper corollary / deterministic consequence of the exact finite
construction.

### Certified P038 Order-Polytope Geometry

In order-ideal indicator coordinates, the order polytope `O(P038)` has 13
vertices, 10 irredundant natural support facets, boundary `f`-vector
`(13,50,88,81,40,10)`, and `h*`-polynomial
`1 + 6t + 7t^2 + t^3`.

Verifier:

```text
scripts/verify_p038_order_polytope_geometry.py
```

Static certificate: `certificates/p038_order_polytope_geometry.json`.

Status: supporting finite replay data for the order-polytope cube-tiling
corollary.

Boundary: this is not a separate tiling proof, not a classification claim, and
not a novelty claim.

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
P038 gives a 48-piece type-A5 Coxeter-complex chamber tiling.
P038 also gives a 48-piece order-polytope tiling of the 6-cube.
The P038 order-polytope tile has certified supporting face and Ehrhart data.
The current S6 laboratory audit reports a structured 19/38 split.
```

Do not say:

```text
The full S6 19/38 split is a paper theorem.
The five hard obstruction-side cases have compact proof certificates.
Historical Colab/RoundingSat runs are proof certificates.
The P038 Coxeter-complex corollary classifies all type-A5 tilers.
The P038 Coxeter-complex corollary proves an outer-automorphism explanation.
The P038 order-polytope geometry data classify order-polytope cube tilings.
The P038 order-polytope geometry data establish a literature novelty theorem.
```
