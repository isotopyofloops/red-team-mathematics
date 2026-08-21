#!/usr/bin/env python3
"""Independent finite checker for Red-Team Mathematics Experiment 001.

This script checks the core N5 and {0}+N5 certificates from first principles.
It uses only Python's standard library.

It is not a formal proof assistant. Its purpose is reproducible finite verification:
- build each poset/lattice from generating order relations;
- compute joins, meets, covers, refinements, minimal covers, and dimension directly;
- construct the 2018 order matrix;
- evaluate the printed MC2/MC3 conditions under the natural pointwise reading;
- compare the printed matrix-selected family M(X) with true MCov(X);
- verify the 2019 downstream quasi-dimension failure on L6.
"""

from itertools import combinations


def transitive_closure(n, edges):
    le = [[False] * n for _ in range(n)]
    for i in range(n):
        le[i][i] = True
    for a, b in edges:
        le[a][b] = True
    for k in range(n):
        for i in range(n):
            if le[i][k]:
                for j in range(n):
                    if le[k][j]:
                        le[i][j] = True
    return le


def bottom(le):
    xs = [x for x in range(len(le)) if all(le[x][y] for y in range(len(le)))]
    assert len(xs) == 1
    return xs[0]


def top(le):
    xs = [x for x in range(len(le)) if all(le[y][x] for y in range(len(le)))]
    assert len(xs) == 1
    return xs[0]


def join(le, subset):
    subset = tuple(subset)
    if not subset:
        return bottom(le)
    ubs = [x for x in range(len(le)) if all(le[s][x] for s in subset)]
    least = [x for x in ubs if all(le[x][y] for y in ubs)]
    assert len(least) == 1, (subset, ubs, least)
    return least[0]


def meet(le, subset):
    subset = tuple(subset)
    if not subset:
        return top(le)
    lbs = [x for x in range(len(le)) if all(le[x][s] for s in subset)]
    greatest = [x for x in lbs if all(le[y][x] for y in lbs)]
    assert len(greatest) == 1, (subset, lbs, greatest)
    return greatest[0]


def is_antichain(le, subset):
    for a, b in combinations(subset, 2):
        if le[a][b] or le[b][a]:
            return False
    return True


def is_cover(le, subset):
    return bottom(le) not in subset and join(le, subset) == top(le)


def refines(le, d, c):
    return all(any(le[x][y] for y in c) for x in d)


def all_covers(le):
    elems = [x for x in range(len(le)) if x != bottom(le)]
    out = []
    for r in range(1, len(elems) + 1):
        for s in combinations(elems, r):
            s = frozenset(s)
            if is_cover(le, s):
                out.append(s)
    return out


def minimal_covers(le):
    cov = all_covers(le)
    return [
        c
        for c in cov
        if all((not refines(le, d, c)) or c.issubset(d) for d in cov)
    ]


def subset_order(le, subset):
    """Definition 2.2 for a finite nonempty subset."""
    max_nonzero_meet_size = 0
    for r in range(1, len(subset) + 1):
        if any(meet(le, s) != bottom(le) for s in combinations(subset, r)):
            max_nonzero_meet_size = r
    return max_nonzero_meet_size - 1


def dimension_direct(le):
    """Compute Definition 2.3 directly, without minimal-cover theorems."""
    cov = all_covers(le)
    worst = 0
    for c in cov:
        refinements = [d for d in cov if refines(le, d, c)]
        best_for_c = min(subset_order(le, d) for d in refinements)
        worst = max(worst, best_for_c)
    return worst


def order_matrix(le):
    a = []
    for i in range(len(le)):
        row = []
        for j in range(len(le)):
            if i == j:
                row.append(1)
            elif le[i][j]:
                row.append(2)
            elif le[j][i]:
                row.append(-2)
            else:
                row.append(0)
        a.append(row)
    return a


def add(*vectors):
    return [sum(xs) for xs in zip(*vectors)]


def sub(a, b):
    return [x - y for x, y in zip(a, b)]


def cover_condition(le, a, subset):
    """2018 Definition 3.3. Empty set is treated as non-cover for Step-8 evaluation.

    The paper does not define a cover-condition predicate for the empty set; that is a
    separate singleton/MC1 specification gap. Treating it as false is the natural extension
    consistent with the actual cover predicate.
    """
    subset = tuple(subset)
    if not subset:
        return False
    if not is_antichain(le, subset):
        return False
    n = len(le)
    t = top(le)
    m = len(subset)
    if m == 1:
        return 3 not in sub(a[subset[0]], a[t])
    v = [sum(a[j][q] for j in subset) - a[t][q] for q in range(n)]
    return 2 * m + 2 not in v


def printed_mc(le, a, c):
    """Pointwise reading of printed Theorem 3.7 MC1-MC3."""
    c = set(c)
    if not is_cover(le, c) or not is_antichain(le, c):
        return False
    outside = [k for k in range(len(le)) if k not in c]

    for ji in tuple(c):
        rest = c - {ji}

        # MC1
        if cover_condition(le, a, rest):
            return False

        # MC2
        for k1, k2 in combinations(outside, 2):
            if 1 not in add(a[k1], a[k2]):
                continue
            if 3 not in add(a[ji], a[k1]):
                continue
            if 3 not in add(a[ji], a[k2]):
                continue
            if any(
                1 not in add(a[k1], a[jl]) or 1 not in add(a[k2], a[jl])
                for jl in rest
            ):
                continue
            if cover_condition(le, a, rest | {k1, k2}):
                return False

        # MC3
        for k in outside:
            if 3 not in add(a[ji], a[k]):
                continue
            if any(1 not in add(a[k], a[jl]) for jl in rest):
                continue
            if cover_condition(le, a, rest | {k}):
                return False

    return True


def corrected_mc(le, a, c):
    """Candidate repair: directional difference replaces row sum in MC2/MC3."""
    c = set(c)
    if not is_cover(le, c) or not is_antichain(le, c):
        return False
    outside = [k for k in range(len(le)) if k not in c]

    for ji in tuple(c):
        rest = c - {ji}
        if cover_condition(le, a, rest):
            return False

        for k1, k2 in combinations(outside, 2):
            if 1 not in add(a[k1], a[k2]):
                continue
            if 3 not in sub(a[k1], a[ji]):
                continue
            if 3 not in sub(a[k2], a[ji]):
                continue
            if any(
                1 not in add(a[k1], a[jl]) or 1 not in add(a[k2], a[jl])
                for jl in rest
            ):
                continue
            if cover_condition(le, a, rest | {k1, k2}):
                return False

        for k in outside:
            if 3 not in sub(a[k], a[ji]):
                continue
            if any(1 not in add(a[k], a[jl]) for jl in rest):
                continue
            if cover_condition(le, a, rest | {k}):
                return False

    return True


def matrix_selected(le, corrected=False):
    a = order_matrix(le)
    test = corrected_mc if corrected else printed_mc
    return [
        c
        for c in all_covers(le)
        if is_antichain(le, c) and test(le, a, c)
    ]


def paper_dimension(le):
    """Numerical behavior relevant to Algorithm 5.4: zero default when M is empty."""
    m = matrix_selected(le, corrected=False)
    return max((subset_order(le, c) for c in m), default=0)


def dense_elements(le):
    b = bottom(le)
    return [
        x
        for x in range(len(le))
        if x != b and all(meet(le, (x, y)) != b for y in range(len(le)) if y != b)
    ]


def downset(le, x):
    elems = [y for y in range(len(le)) if le[y][x]]
    suble = [[le[a][b] for b in elems] for a in elems]
    return suble, elems


def quasi_dimension_direct(le):
    return max(dimension_direct(downset(le, x)[0]) for x in dense_elements(le))


def quasi_dimension_published_pipeline(le):
    return max(paper_dimension(downset(le, x)[0]) for x in dense_elements(le))


def fmt_sets(sets, names):
    return ["{" + ",".join(names[i] for i in sorted(s)) + "}" for s in sets]


def check_n5():
    # 0 < a < t < 1, 0 < b < 1
    le = transitive_closure(5, [(0, 1), (1, 2), (2, 4), (0, 3), (3, 4)])
    names = ["0", "a", "t", "b", "1"]
    a = order_matrix(le)

    expected = [
        [1, 2, 2, 2, 2],
        [-2, 1, 2, 0, 2],
        [-2, -2, 1, 0, 2],
        [-2, 0, 0, 1, 2],
        [-2, -2, -2, -2, 1],
    ]
    assert a == expected

    c = frozenset({1, 3})  # {a,b}
    assert minimal_covers(le) == [c]
    assert dimension_direct(le) == 0

    # Certificate A arithmetic.
    assert add(a[1], a[2]) == [-4, -1, 3, 0, 4]
    assert add(a[2], a[3]) == [-4, -2, 1, 1, 4]
    assert sub(add(a[2], a[3]), a[4]) == [-2, 0, 3, 3, 3]
    assert cover_condition(le, a, {2, 3})
    assert not printed_mc(le, a, c)
    assert corrected_mc(le, a, c)

    print("N5:")
    print("  MCov =", fmt_sets(minimal_covers(le), names))
    print("  printed M =", fmt_sets(matrix_selected(le), names))
    print("  corrected M =", fmt_sets(matrix_selected(le, True), names))
    print("  dim (direct) =", dimension_direct(le))


def check_l6():
    # 0 < e < a < t < 1, e < b < 1
    le = transitive_closure(6, [(0, 1), (1, 2), (2, 4), (4, 5), (1, 3), (3, 5)])
    names = ["0", "e", "a", "b", "t", "1"]
    a = order_matrix(le)

    expected = [
        [1, 2, 2, 2, 2, 2],
        [-2, 1, 2, 2, 2, 2],
        [-2, -2, 1, 0, 2, 2],
        [-2, -2, 0, 1, 0, 2],
        [-2, -2, -2, 0, 1, 2],
        [-2, -2, -2, -2, -2, 1],
    ]
    assert a == expected

    c = frozenset({2, 3})  # {a,b}
    assert minimal_covers(le) == [c]
    assert subset_order(le, c) == 1
    assert dimension_direct(le) == 1

    # Certificate B candidate covers and MC eliminations.
    assert cover_condition(le, a, {2, 3})
    assert cover_condition(le, a, {3, 4})
    assert cover_condition(le, a, {5})
    assert not printed_mc(le, a, {2, 3})
    assert not printed_mc(le, a, {3, 4})
    assert not printed_mc(le, a, {5})
    assert matrix_selected(le) == []
    assert paper_dimension(le) == 0
    assert matrix_selected(le, corrected=True) == [c]

    print("L6 = {0}+N5:")
    print("  MCov =", fmt_sets(minimal_covers(le), names))
    print("  printed M =", fmt_sets(matrix_selected(le), names))
    print("  corrected M =", fmt_sets(matrix_selected(le, True), names))
    print("  dim (Definition 2.3 direct) =", dimension_direct(le))
    print("  printed Algorithm 5.4 behavior =", paper_dimension(le))

    dense = dense_elements(le)
    assert dense == [1, 2, 3, 4, 5]
    direct_q = quasi_dimension_direct(le)
    paper_q = quasi_dimension_published_pipeline(le)
    assert direct_q == 1
    assert paper_q == 0

    print("  dense elements =", [names[i] for i in dense])
    print("  dim_q (2019 Proposition 1 / direct downsets) =", direct_q)
    print("  2019 Algorithm 4 inherited pipeline =", paper_q)


if __name__ == "__main__":
    check_n5()
    print()
    check_l6()
    print("\nAll Experiment 001 certificate checks passed.")
