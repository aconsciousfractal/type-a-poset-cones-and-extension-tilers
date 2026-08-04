# Public Claim Boundary

This package is public-facing but intentionally conservative.

## Theorem-Level In The Paper

- Type-A halfspace-convex chamber-unions are poset cones.
- Every finite series-parallel poset is an extension tiler.
- On five elements, extension tilers are exactly series-parallel posets.
- The six-element poset `P038` is a non-series-parallel extension tiler.
- The same `P038` factorization gives a type-`A5` Coxeter-complex chamber
  tiling by 48 left translates of a 15-chamber poset cone.
- The same `P038` factorization gives a coordinate-permutation tiling of
  `[0,1]^6` by 48 copies of the order polytope of `P038`.
- The single tile `O(P038)` has certified supporting face and Ehrhart data:
  13 vertices, 10 support facets, and `h* = 1 + 6t + 7t^2 + t^3`.

## Laboratory-Level Only

The file `certificates/s6_classification_status.md` reports the current
finite `S6` audit status:

```text
57 divisible non-series-parallel candidates
19 tiler-side candidates
38 obstruction-side candidates
```

This is not promoted to a theorem in this paper because five obstruction-side
cases still need compact portable certificates:

```text
001, 013, 017, 019, 020
```

## Boundary For The P038 Tile Geometry Data

The face-vector and Ehrhart data for `O(P038)` are finite replay data for the
specific tile used in the cube-tiling corollary.  They may be used to make the
tile more inspectable.  They must not be used as a classification of all
order-polytope cube tilings, as a proof that the tiling works independently of
the exact `S6` factorization, or as a literature novelty theorem.
