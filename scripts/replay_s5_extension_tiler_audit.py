"""Replay the finite S5 extension-tiler audit.

This script is intentionally self-contained.  It enumerates all strict posets
on five labelled points, quotients them up to relabelling, identifies the
non-series-parallel divisible types, and replays the two finite certificates
recorded in the paper snapshot:

* the mod-5 rank obstruction for the two five-extension types;
* the maximum-packing obstruction for the eight-extension type.

The script uses the same left action convention as the S6 verifier:

    compose_left(g, word) = tuple(g[x] for x in word).
"""

from __future__ import annotations

import itertools
from functools import lru_cache
from typing import Iterable


N = 5
POINTS = tuple(range(N))
PERMS = tuple(itertools.permutations(POINTS))
ORDERED_PAIRS = tuple((i, j) for i in POINTS for j in POINTS if i != j)
PAIR_TO_BIT = {pair: 1 << idx for idx, pair in enumerate(ORDERED_PAIRS)}


def has_bit(mask: int, i: int, j: int) -> bool:
    return bool(mask & PAIR_TO_BIT[(i, j)])


def relation_pairs(mask: int) -> tuple[tuple[int, int], ...]:
    return tuple(pair for pair in ORDERED_PAIRS if mask & PAIR_TO_BIT[pair])


def is_strict_poset(mask: int) -> bool:
    for i, j in itertools.combinations(POINTS, 2):
        if has_bit(mask, i, j) and has_bit(mask, j, i):
            return False
    for i, j, k in itertools.product(POINTS, repeat=3):
        if i != j and j != k and i != k:
            if has_bit(mask, i, j) and has_bit(mask, j, k) and not has_bit(mask, i, k):
                return False
    return True


def relabel_mask(mask: int, perm: tuple[int, ...]) -> int:
    out = 0
    for i, j in relation_pairs(mask):
        out |= PAIR_TO_BIT[(perm[i], perm[j])]
    return out


def canonical_mask(mask: int) -> int:
    return min(relabel_mask(mask, perm) for perm in PERMS)


@lru_cache(maxsize=None)
def linear_extensions(mask: int) -> tuple[tuple[int, ...], ...]:
    out = []
    for word in PERMS:
        pos = {x: idx for idx, x in enumerate(word)}
        if all(pos[i] < pos[j] for i, j in relation_pairs(mask)):
            out.append(word)
    return tuple(out)


def induced_mask(mask: int, subset: tuple[int, ...]) -> int:
    index = {old: new for new, old in enumerate(subset)}
    out = 0
    for i, j in relation_pairs(mask):
        if i in index and j in index:
            out |= PAIR_TO_BIT[(index[i], index[j])]
    return out


def n_poset_masks() -> set[int]:
    # The forbidden N has a < b, c < b, c < d on four points.
    base = 0
    for pair in [(0, 1), (2, 1), (2, 3)]:
        base |= PAIR_TO_BIT[pair]
    return {relabel_mask(base, perm) for perm in itertools.permutations(range(4))}


N4_MASKS = n_poset_masks()


def is_series_parallel(mask: int) -> bool:
    for subset in itertools.combinations(POINTS, 4):
        if induced_mask(mask, subset) in N4_MASKS:
            return False
    return True


def left_translate(g: tuple[int, ...], word: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(g[x] for x in word)


def distinct_left_translates(tile: Iterable[tuple[int, ...]]) -> list[frozenset[tuple[int, ...]]]:
    base = tuple(tile)
    seen: dict[frozenset[tuple[int, ...]], None] = {}
    for g in PERMS:
        seen[frozenset(left_translate(g, word) for word in base)] = None
    return list(seen.keys())


def rank_mod_p(rows: list[list[int]], p: int) -> int:
    if not rows:
        return 0
    mat = [[x % p for x in row] for row in rows]
    n_rows = len(mat)
    n_cols = len(mat[0])
    rank = 0
    for col in range(n_cols):
        pivot = None
        for r in range(rank, n_rows):
            if mat[r][col] % p:
                pivot = r
                break
        if pivot is None:
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        inv = pow(mat[rank][col], -1, p)
        mat[rank] = [(v * inv) % p for v in mat[rank]]
        for r in range(n_rows):
            if r != rank and mat[r][col] % p:
                factor = mat[r][col] % p
                mat[r] = [(a - factor * b) % p for a, b in zip(mat[r], mat[rank])]
        rank += 1
        if rank == n_rows:
            break
    return rank


def incidence_matrix(translates: list[frozenset[tuple[int, ...]]]) -> list[list[int]]:
    row_index = {word: idx for idx, word in enumerate(PERMS)}
    rows = [[0 for _ in translates] for _ in PERMS]
    for col, tile in enumerate(translates):
        for word in tile:
            rows[row_index[word]][col] = 1
    return rows


def max_clique_size(adj: list[int], candidates: int) -> int:
    best = 0

    def color_sort(vertices: int) -> tuple[list[int], list[int]]:
        order: list[int] = []
        colors: list[int] = []
        remaining = vertices
        color = 0
        while remaining:
            color += 1
            available = remaining
            while available:
                v_bit = available & -available
                v = v_bit.bit_length() - 1
                order.append(v)
                colors.append(color)
                remaining &= ~v_bit
                available &= ~v_bit
                available &= ~adj[v]
        return order, colors

    def expand(size: int, vertices: int) -> None:
        nonlocal best
        if not vertices:
            best = max(best, size)
            return
        order, colors = color_sort(vertices)
        for idx in range(len(order) - 1, -1, -1):
            if size + colors[idx] <= best:
                return
            v = order[idx]
            v_bit = 1 << v
            if not (vertices & v_bit):
                continue
            expand(size + 1, vertices & adj[v])
            vertices &= ~v_bit
            if size + colors[idx] <= best:
                return

    expand(0, candidates)
    return best


def packing_certificate(tile: tuple[tuple[int, ...], ...]) -> tuple[int, int, int]:
    translates = distinct_left_translates(tile)
    base = frozenset(tile)
    base_index = translates.index(base)
    disjoint = [idx for idx, other in enumerate(translates) if idx != base_index and base.isdisjoint(other)]
    local_index = {old: new for new, old in enumerate(disjoint)}
    adj = [0 for _ in disjoint]
    for a_pos, a_old in enumerate(disjoint):
        a_tile = translates[a_old]
        mask = 0
        for b_old in disjoint:
            b_pos = local_index[b_old]
            if a_old != b_old and a_tile.isdisjoint(translates[b_old]):
                mask |= 1 << b_pos
        adj[a_pos] = mask
    candidates_mask = (1 << len(disjoint)) - 1
    residual_max = max_clique_size(adj, candidates_mask)
    return len(translates), len(disjoint), 1 + residual_max


def profile_mask(d_letters: str, u_letters: str) -> int:
    labels = {"a": 0, "b": 1, "c": 2, "d": 3, "x": 4}
    out = 0
    for pair in [(0, 1), (2, 1), (2, 3)]:
        out |= PAIR_TO_BIT[pair]
    for name in d_letters:
        out |= PAIR_TO_BIT[(labels[name], labels["x"])]
    for name in u_letters:
        out |= PAIR_TO_BIT[(labels["x"], labels[name])]
    return out


def main() -> None:
    labeled = [mask for mask in range(1 << len(ORDERED_PAIRS)) if is_strict_poset(mask)]
    canonical_to_masks: dict[int, list[int]] = {}
    for mask in labeled:
        canonical_to_masks.setdefault(canonical_mask(mask), []).append(mask)

    series_labeled = [mask for mask in labeled if is_series_parallel(mask)]
    divisible_labeled = [mask for mask in labeled if 120 % len(linear_extensions(mask)) == 0]
    non_sp_div_labeled = [mask for mask in divisible_labeled if not is_series_parallel(mask)]

    unlabeled = sorted(canonical_to_masks)
    series_unlabeled = [mask for mask in unlabeled if is_series_parallel(mask)]
    divisible_unlabeled = [mask for mask in unlabeled if 120 % len(linear_extensions(mask)) == 0]
    non_sp_div_unlabeled = [mask for mask in divisible_unlabeled if not is_series_parallel(mask)]

    print("S5 extension-tiler audit replay")
    print()
    print("Aggregate counts")
    print("----------------")
    print(f"labeled posets: {len(labeled)}")
    print(f"unlabeled posets: {len(unlabeled)}")
    print(f"series-parallel labeled posets: {len(series_labeled)}")
    print(f"series-parallel unlabeled posets: {len(series_unlabeled)}")
    print(f"divisible labeled posets: {len(divisible_labeled)}")
    print(f"divisible unlabeled posets: {len(divisible_unlabeled)}")
    print(f"non-series-parallel divisible labeled posets: {len(non_sp_div_labeled)}")
    print(f"non-series-parallel divisible unlabeled posets: {len(non_sp_div_unlabeled)}")
    print()
    print("Non-series-parallel divisible unlabeled types")
    print("--------------------------------------------")
    by_size: dict[int, list[int]] = {}
    for mask in non_sp_div_unlabeled:
        by_size.setdefault(len(linear_extensions(mask)), []).append(mask)
    print(f"There are exactly {len(non_sp_div_unlabeled)}.")
    print(f"Two types have |L(P)| = {len(linear_extensions(canonical_mask(profile_mask('', 'abcd'))))}.")
    print(f"One type has |L(P)| = {len(linear_extensions(canonical_mask(profile_mask('', 'abd'))))}.")
    print()

    five_types = [
        canonical_mask(profile_mask("abcd", "")),
        canonical_mask(profile_mask("", "abcd")),
    ]
    print("Former rank certificates retained for audit context")
    print("---------------------------------------------------")
    for mask in five_types:
        translates = distinct_left_translates(linear_extensions(mask))
        rows = incidence_matrix(translates)
        augmented = [row + [1] for row in rows]
        print("For one former |L(P)| = 5 type:")
        print(f"  rank_F5(M) = {rank_mod_p(rows, 5)}")
        print(f"  rank_F5(M | 1) = {rank_mod_p(augmented, 5)}")
    print()

    eight_mask = canonical_mask(profile_mask("", "abd"))
    distinct, disjoint_from_base, max_pack = packing_certificate(linear_extensions(eight_mask))
    print("Former packing certificate retained for audit context")
    print("-----------------------------------------------------")
    print("For the |L(P)| = 8 type:")
    print(f"  distinct left translates = {distinct}")
    print(f"  candidates disjoint from base translate = {disjoint_from_base}")
    print(f"  maximum packing containing base translate = {max_pack}")
    print(f"  tiling would require = {120 // len(linear_extensions(eight_mask))}")
    print()
    print("PASS")


if __name__ == "__main__":
    main()
