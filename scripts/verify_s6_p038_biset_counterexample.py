#!/usr/bin/env python3
"""Verify the compressed S6 non-series-parallel extension-tiler witness.

The witness is the six-point poset P with covers

    0 < 1, 1 < 2, 1 < 3, 4 < 3, 4 < 5, 5 < 2.

Let T = L(P).  We define subgroups H,K <= S_6 and tau in S_6 by

    H = < (2 3)(4 5), (0 1)(3 5) >,
    K = < (2 3)(4 5), (0 4 5)(1 3 2) >,
    tau = (3 4).

With the project convention compose_left(g, w) = tuple(g[x] for x in w),
the multiplier set A = H K union H tau K has size 48 and the translates
aT, a in A, partition S_6.
"""

from __future__ import annotations

from collections import Counter, deque
from itertools import combinations, permutations


N = 6


def perm_from_cycles(cycles: list[tuple[int, ...]]) -> tuple[int, ...]:
    p = list(range(N))
    for cycle in cycles:
        for i, a in enumerate(cycle):
            p[a] = cycle[(i + 1) % len(cycle)]
    return tuple(p)


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Return p after q as maps on labels."""
    return tuple(p[q[i]] for i in range(N))


def subgroup(gens: list[tuple[int, ...]]) -> set[tuple[int, ...]]:
    identity = tuple(range(N))
    seen = {identity}
    queue: deque[tuple[int, ...]] = deque([identity])
    while queue:
        a = queue.popleft()
        for g in gens:
            for h in (compose(g, a), compose(a, g)):
                if h not in seen:
                    seen.add(h)
                    queue.append(h)
    return seen


def linear_extensions(relations: list[tuple[int, int]]) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []
    for word in permutations(range(N)):
        pos = {x: i for i, x in enumerate(word)}
        if all(pos[a] < pos[b] for a, b in relations):
            out.append(word)
    return out


def left_action(g: tuple[int, ...], word: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(g[x] for x in word)


def transitive_closure(relations: list[tuple[int, int]]) -> set[tuple[int, int]]:
    rel = set(relations)
    changed = True
    while changed:
        changed = False
        for a, b in list(rel):
            for c, d in list(rel):
                if b == c and (a, d) not in rel:
                    rel.add((a, d))
                    changed = True
    return rel


def induced_n_copies(relations: list[tuple[int, int]]) -> int:
    rel = transitive_closure(relations)
    count = 0
    n_degrees = sorted([(1, 0), (0, 2), (2, 0), (0, 1)])
    for subset in combinations(range(N), 4):
        pairs = [(a, b) for a, b in permutations(subset, 2) if (a, b) in rel]
        if len(pairs) != 3:
            continue
        indeg = Counter(b for _, b in pairs)
        outdeg = Counter(a for a, _ in pairs)
        degrees = sorted((outdeg[x], indeg[x]) for x in subset)
        if degrees == n_degrees:
            count += 1
    return count


def main() -> None:
    covers = [(0, 1), (1, 2), (1, 3), (4, 3), (4, 5), (5, 2)]
    tile = linear_extensions(covers)

    h1 = perm_from_cycles([(2, 3), (4, 5)])
    h2 = perm_from_cycles([(0, 1), (3, 5)])
    k1 = perm_from_cycles([(2, 3), (4, 5)])
    k2 = perm_from_cycles([(0, 4, 5), (1, 3, 2)])
    tau = perm_from_cycles([(3, 4)])

    H = subgroup([h1, h2])
    K = subgroup([k1, k2])
    HK = {compose(h, k) for h in H for k in K}
    HtauK = {compose(compose(h, tau), k) for h in H for k in K}
    A = HK | HtauK

    covered = [left_action(a, w) for a in A for w in tile]
    multiplicities = Counter(covered)

    print(f"|L(P)| = {len(tile)}")
    print(f"|H| = {len(H)}")
    print(f"|K| = {len(K)}")
    print(f"|HK| = {len(HK)}")
    print(f"|H tau K| = {len(HtauK)}")
    print(f"|HK cap H tau K| = {len(HK & HtauK)}")
    print(f"|A| = {len(A)}")
    print(f"covered = {len(multiplicities)} / {len(list(permutations(range(N))))}")
    print(f"multiplicities = {sorted(set(multiplicities.values()))}")
    print(f"induced N copies = {induced_n_copies(covers)}")

    assert len(tile) == 15
    assert len(H) == 8
    assert len(K) == 6
    assert len(HK) == 24
    assert len(HtauK) == 24
    assert not (HK & HtauK)
    assert len(A) == 48
    assert len(covered) == 720
    assert len(multiplicities) == 720
    assert set(multiplicities.values()) == {1}
    assert induced_n_copies(covers) == 4
    print("PASS")


if __name__ == "__main__":
    main()
