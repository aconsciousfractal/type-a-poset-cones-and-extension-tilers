# Claim Register

Date: 2026-06-18

This register records the current claim boundary for the Type-A
extension-tiler paper after the S6 counterexample.
For public-facing review, `docs/CLAIM_LEDGER.md` is the primary claim ledger;
this register records the corresponding certificate-level statuses and
verification paths.

## Claim Levels

The levels follow the PAPP convention:

- `CL3`: certified finite result / exact finite replay.
- `CL5`: internal theorem in the paper.
- `CLO`: proof obligation still open.
- `CLB`: blocked from theorem promotion.

## Promoted Claims

### CL5 - Poset-Cone Dictionary In Type A

Statement:

```text
Type-A chamber halfspace constraints correspond to posets, and the chambers
satisfying a poset P are the linear extensions L(P).
```

Status:

```text
paper theorem/background framework
```

Boundary:

```text
Do not merge this with divisibility, tiling, or series-parallelity into one
global equivalence.
```

### CL5 - Series-Parallel Posets Are Extension Tilers

Statement:

```text
Every finite series-parallel poset is an extension tiler.
```

Status:

```text
paper theorem
```

Boundary:

```text
This is one direction only.  The converse is false in S6.
```

### CL5/CL3 - S5 Classification

Statement:

```text
For posets on five elements, L(P) tiles S5 by left translates if and only if
P is series-parallel.
```

Evidence:

```text
finite classification plus explicit obstruction certificates
```

Status:

```text
paper theorem with finite audit support
```

### CL5/CL3 - S6 Counterexample P038

Statement:

```text
The six-element poset P038 is not series-parallel, but L(P038) tiles S6 by
left translates.
```

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

Expected verifier result:

```text
PASS
```

Status:

```text
paper theorem / exact finite construction
```

Consequence:

```text
The converse "extension tiler => series-parallel" is false.
```

### CL5/CL3 - Order-Polytope Cube Tiling

Statement:

```text
If S_X is tiled by left translates a L(P), then [0,1]^X is tiled by the
coordinate-permuted order polytopes a O(P) along the standard cube
triangulation.
```

P038 consequence:

```text
[0,1]^6 is tiled by 48 coordinate-permuted copies of O(P038).
```

Status:

```text
paper corollary / deterministic consequence of the P038 exact factorization
```

Boundary:

```text
This is not a claim about arbitrary Euclidean congruent copies and does not
use the projected PAPP/flux visual artifacts.
```

### CL3 - P038 Order-Polytope Geometry Data

Statement:

```text
The order polytope O(P038), in order-ideal indicator coordinates, has
13 vertices, 10 irredundant natural support facets, boundary f-vector
(13,50,88,81,40,10), and h*-polynomial 1 + 6t + 7t^2 + t^3.
```

Verifier:

```text
scripts/verify_p038_order_polytope_geometry.py
```

Static certificate:

```text
certificates/p038_order_polytope_geometry.json
```

Expected verifier result:

```text
PASS
```

Status:

```text
supporting finite replay data for the order-polytope cube-tiling corollary
```

Boundary:

```text
This is tile geometry data.  It is not a new tiling proof, not a
classification of order-polytope cube tilings, and not a novelty claim.
```

## Laboratory Claims Not Promoted To Theorem

### CL3-Lab - S6 19/38 Audit

Statement:

```text
Among the 57 non-series-parallel divisible S6 candidates, the working audit
finds 19 tilers and 38 obstruction-side non-tilers.
```

Status:

```text
audit-level laboratory status data
```

Reason not theorem-level in this paper:

```text
Five obstruction-side cases still lack portable compact certificates.
```

Hard cases:

```text
001, 013, 017, 019, 020
```

Boundary:

```text
May be reported as laboratory status.  Must not be stated as a completed
paper theorem until the five hard cases have proof-grade certificates or an
independent proof-logged checker.
```

### CLO - Five Defect-One Packing Obstructions

Statement:

```text
The candidates 001,013,017,019,020 are obstruction-side non-tilers according
to the finite audit, but need compact certificate compression.
```

Current evidence:

```text
residual packing graphs;
defect-one maximum near-packings;
ordered-triple integer-hole diagnostics;
raw OPB instances exported.
```

Blocked route:

```text
Blind Colab/RoundingSat OPB runs timed out or returned UNKNOWN and are not
certificates.
```

Recommended route:

```text
residual packing compression;
orbit quotient;
coloring / clique-cover upper bound;
near-tiling residual profile obstruction;
proof-logged SAT/PB only after compression.
```

## Public Boundary

Can say:

```text
The series-parallel converse is false in S6.
P038 is a compact non-series-parallel extension tiler.
P038 gives a 48-piece order-polytope tiling of the 6-cube.
The current S6 laboratory audit reports a structured 19/38 split among
non-series-parallel divisible candidates.
```

Can say internally:

```text
The S6 finite classification appears complete in the lab.
The five remaining hard cases are obstruction-side by finite packing/IP
evidence.
```

Must not say:

```text
The full S6 19/38 classification is a paper-grade theorem.
The five hard cases are closed by the Colab/RoundingSat logs.
Extension tilers are exactly series-parallel posets.
```
