#!/usr/bin/env python3
"""Verify supporting geometry data for the P038 order polytope.

This script is intentionally self-contained.  It verifies data used to make
the P038 order-polytope tile inspectable; it is not an independent proof of
the cube tiling and it is not a classification claim.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb
from pathlib import Path


N = 6
COVERS = ((0, 1), (1, 2), (1, 3), (4, 3), (4, 5), (5, 2))
ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE_PATH = ROOT / "certificates" / "p038_order_polytope_geometry.json"


def transitive_closure() -> set[tuple[int, int]]:
    rel = set(COVERS)
    changed = True
    while changed:
        changed = False
        for a, b in list(rel):
            for c, d in list(rel):
                if b == c and (a, d) not in rel:
                    rel.add((a, d))
                    changed = True
    return rel


def linear_extensions() -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []
    for word in permutations(range(N)):
        pos = {item: idx for idx, item in enumerate(word)}
        if all(pos[lower] < pos[upper] for lower, upper in COVERS):
            out.append(word)
    return out


def order_ideals() -> list[tuple[int, ...]]:
    rel = transitive_closure()
    ideals: list[tuple[int, ...]] = []
    for mask in range(1 << N):
        subset = {item for item in range(N) if mask & (1 << item)}
        if all(upper not in subset or lower in subset for lower, upper in rel):
            ideals.append(tuple(sorted(subset)))
    ideals.sort(key=lambda item: (len(item), item))
    return ideals


def ideal_vertex(ideal: tuple[int, ...]) -> list[int]:
    ideal_set = set(ideal)
    return [1 if item in ideal_set else 0 for item in range(N)]


def matrix_rank(rows: list[list[int]]) -> int:
    mat = [
        [Fraction(value) for value in row]
        for row in rows
        if any(value != 0 for value in row)
    ]
    if not mat:
        return 0

    row_count = len(mat)
    col_count = len(mat[0])
    rank = 0

    for col in range(col_count):
        pivot = None
        for row in range(rank, row_count):
            if mat[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue

        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        pivot_value = mat[rank][col]
        mat[rank] = [value / pivot_value for value in mat[rank]]

        for row in range(row_count):
            if row == rank or mat[row][col] == 0:
                continue
            factor = mat[row][col]
            mat[row] = [
                mat[row][idx] - factor * mat[rank][idx]
                for idx in range(col_count)
            ]

        rank += 1
        if rank == row_count:
            break

    return rank


def affine_dimension(vertices: list[list[int]]) -> int:
    if len(vertices) <= 1:
        return 0
    base = vertices[0]
    rows = [
        [vertex[idx] - base[idx] for idx in range(N)]
        for vertex in vertices[1:]
    ]
    return matrix_rank(rows)


def minimal_maximal_elements(rel: set[tuple[int, int]]) -> tuple[list[int], list[int]]:
    minimal = [item for item in range(N) if not any(b == item for _, b in rel)]
    maximal = [item for item in range(N) if not any(a == item for a, _ in rel)]
    return minimal, maximal


def natural_inequalities() -> list[dict[str, object]]:
    rel = transitive_closure()
    minimal, maximal = minimal_maximal_elements(rel)
    inequalities: list[dict[str, object]] = []

    for item in maximal:
        normal = [0] * N
        normal[item] = -1
        inequalities.append(
            {
                "id": f"y{item}_ge_0",
                "label": f"0 <= y_{item}",
                "normal_leq": normal,
                "rhs_leq": 0,
            }
        )

    for item in minimal:
        normal = [0] * N
        normal[item] = 1
        inequalities.append(
            {
                "id": f"y{item}_le_1",
                "label": f"y_{item} <= 1",
                "normal_leq": normal,
                "rhs_leq": 1,
            }
        )

    for lower, upper in COVERS:
        normal = [0] * N
        normal[upper] = 1
        normal[lower] = -1
        inequalities.append(
            {
                "id": f"y{upper}_le_y{lower}",
                "label": f"y_{upper} <= y_{lower}",
                "normal_leq": normal,
                "rhs_leq": 0,
            }
        )

    return inequalities


def facet_incidence(
    vertices: list[list[int]],
    inequalities: list[dict[str, object]],
) -> list[set[int]]:
    incidence: list[set[int]] = []
    for inequality in inequalities:
        normal = inequality["normal_leq"]
        rhs = inequality["rhs_leq"]
        assert isinstance(normal, list)
        assert isinstance(rhs, int)
        active = set()
        for idx, vertex in enumerate(vertices):
            lhs = sum(int(normal[j]) * vertex[j] for j in range(N))
            if lhs == rhs:
                active.add(idx)
        incidence.append(active)
    return incidence


def face_dimension(vertex_ids: tuple[int, ...], vertices: list[list[int]]) -> int:
    return affine_dimension([vertices[idx] for idx in vertex_ids])


def face_f_vector(vertices: list[list[int]], incidence: list[set[int]]) -> dict[int, int]:
    all_vertices = set(range(len(vertices)))
    face_vertex_sets: set[tuple[int, ...]] = set()

    for count in range(len(incidence) + 1):
        for facet_indices in combinations(range(len(incidence)), count):
            active = set(all_vertices)
            for facet_index in facet_indices:
                active &= incidence[facet_index]
            if active:
                face_vertex_sets.add(tuple(sorted(active)))

    counter = Counter(
        face_dimension(vertex_ids, vertices)
        for vertex_ids in face_vertex_sets
    )
    return {dim: counter.get(dim, 0) for dim in range(N + 1)}


def count_order_preserving_maps(m: int) -> int:
    count = 0
    for values in product(range(m + 1), repeat=N):
        if all(values[lower] <= values[upper] for lower, upper in COVERS):
            count += 1
    return count


def h_star_from_ehrhart_values(values: list[int], dimension: int) -> list[int]:
    coeffs: list[int] = []
    for i in range(dimension + 1):
        value = 0
        for j in range(i + 1):
            value += ((-1) ** (i - j)) * comb(dimension + 1, i - j) * values[j]
        coeffs.append(value)
    return coeffs


def ehrhart_closed_form(m: int) -> int:
    return (
        comb(m + 6, 6)
        + 6 * comb(m + 5, 6)
        + 7 * comb(m + 4, 6)
        + comb(m + 3, 6)
    )


def build_certificate() -> dict[str, object]:
    extensions = linear_extensions()
    ideals = order_ideals()
    vertices = [ideal_vertex(ideal) for ideal in ideals]
    inequalities = natural_inequalities()
    incidence = facet_incidence(vertices, inequalities)
    f_vector = face_f_vector(vertices, incidence)
    boundary_f_vector = tuple(f_vector[dim] for dim in range(N))
    ehrhart_values = [count_order_preserving_maps(m) for m in range(N + 1)]
    h_star = h_star_from_ehrhart_values(ehrhart_values, N)
    closed_form_values = [ehrhart_closed_form(m) for m in range(N + 1)]
    natural_facet_dimensions = [
        face_dimension(tuple(sorted(active)), vertices)
        for active in incidence
    ]

    validation = {
        "linear_extension_count_is_15": len(extensions) == 15,
        "order_ideal_count_is_13": len(ideals) == 13,
        "affine_dimension_is_6": affine_dimension(vertices) == 6,
        "natural_support_facet_count_is_10": len(inequalities) == 10,
        "natural_support_facets_are_dimension_5": natural_facet_dimensions == [5] * 10,
        "boundary_f_vector_matches": boundary_f_vector == (13, 50, 88, 81, 40, 10),
        "top_face_count_is_1": f_vector[6] == 1,
        "ehrhart_values_match_expected": ehrhart_values == [1, 13, 77, 302, 917, 2338, 5250],
        "ehrhart_values_match_closed_form": closed_form_values == ehrhart_values,
        "h_star_matches_expected": h_star == [1, 6, 7, 1, 0, 0, 0],
        "h_star_sum_matches_linear_extensions": sum(h_star) == len(extensions),
    }
    validation["pass"] = all(validation.values())

    return {
        "certificate_version": "0.1",
        "object_id": "P038_order_polytope_geometry",
        "poset": {
            "label": "P038",
            "element_count": N,
            "covers": [list(edge) for edge in COVERS],
        },
        "coordinate_convention": {
            "paper_standard_order_polytope": "x_i <= x_j for i <_P j",
            "finite_face_data": "order-ideal indicator coordinates y_i = 1 - x_i",
            "cover_inequality": "i <_P j gives y_j <= y_i",
            "invariance": "integral affine equivalence preserves face lattice, lattice-normalized volume, and Ehrhart data",
        },
        "computed": {
            "linear_extension_count": len(extensions),
            "order_ideal_vertex_count": len(ideals),
            "ambient_dimension": N,
            "affine_dimension": affine_dimension(vertices),
            "natural_support_facet_count": len(inequalities),
            "natural_support_facet_dimensions": natural_facet_dimensions,
            "natural_support_inequalities": [
                str(item["label"]) for item in inequalities
            ],
            "boundary_f_vector": list(boundary_f_vector),
            "top_face_count": f_vector[6],
            "ehrhart_values_m0_to_m6": ehrhart_values,
            "h_star_coefficients_degree_0_to_6": h_star,
            "h_star_polynomial": "1 + 6t + 7t^2 + t^3",
            "ehrhart_polynomial_binomial_basis": (
                "binom(m+6,6) + 6 binom(m+5,6) + "
                "7 binom(m+4,6) + binom(m+3,6)"
            ),
            "closed_form_values_m0_to_m6": closed_form_values,
        },
        "claim_boundary": {
            "supporting_order_polytope_data": True,
            "not_a_tiling_proof": True,
            "not_a_classification_claim": True,
            "not_a_novelty_claim": True,
            "not_a_projected_visual_artifact": True,
        },
        "validation": validation,
    }


def assert_certificate(certificate: dict[str, object]) -> None:
    validation = certificate["validation"]
    assert isinstance(validation, dict)
    failures = [
        key for key, value in validation.items()
        if key != "pass" and value is not True
    ]
    assert not failures, failures
    assert validation["pass"] is True


def verify_static_certificate(certificate: dict[str, object]) -> None:
    if not CERTIFICATE_PATH.exists():
        raise AssertionError(f"missing static certificate: {CERTIFICATE_PATH}")
    static_certificate = json.loads(CERTIFICATE_PATH.read_text(encoding="utf-8"))
    if static_certificate != certificate:
        raise AssertionError(
            f"static certificate does not match recomputation: {CERTIFICATE_PATH}"
        )


def write_static_certificate(certificate: dict[str, object]) -> None:
    CERTIFICATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CERTIFICATE_PATH.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def print_summary(certificate: dict[str, object]) -> None:
    computed = certificate["computed"]
    assert isinstance(computed, dict)
    print(f"linear extensions = {computed['linear_extension_count']}")
    print(f"order ideals / vertices = {computed['order_ideal_vertex_count']}")
    print(f"natural support facets = {computed['natural_support_facet_count']}")
    print(f"boundary f-vector = {tuple(computed['boundary_f_vector'])}")
    print(f"top face count = {computed['top_face_count']}")
    print(f"h-star = {computed['h_star_coefficients_degree_0_to_6']}")
    print("h-star polynomial = 1 + 6t + 7t^2 + t^3")
    print("PASS")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write",
        action="store_true",
        help="Regenerate certificates/p038_order_polytope_geometry.json.",
    )
    args = parser.parse_args()

    certificate = build_certificate()
    assert_certificate(certificate)
    if args.write:
        write_static_certificate(certificate)
    else:
        verify_static_certificate(certificate)

    print_summary(certificate)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
