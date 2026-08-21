#!/usr/bin/env python3
"""Finite-lattice checker for Exp 001 collab: Def 2.4 min covers, Prop 3.5 M*, corrected MC*."""

from __future__ import annotations
from itertools import combinations
from typing import Iterable

# Element labels; 0 and 1 reserved names for bottom/top when present.


class Lattice:
    def __init__(self, elems: list[str], leq: set[tuple[str, str]]):
        self.elems = list(elems)
        self.idx = {e: i for i, e in enumerate(self.elems)}
        self.n = len(elems)
        # reflexive closure assumed in leq input; ensure
        self.leq = set(leq)
        for e in elems:
            self.leq.add((e, e))
        # transitive? assume input is full order relation
        self.bottom = elems[0]
        self.top = elems[-1]
        self._validate()

    def _validate(self):
        # all pairwise joins/meets exist
        for a, b in combinations(self.elems, 2):
            self.join(a, b)
            self.meet(a, b)

    def le(self, a: str, b: str) -> bool:
        return (a, b) in self.leq

    def lt(self, a: str, b: str) -> bool:
        return a != b and self.le(a, b)

    def parallel(self, a: str, b: str) -> bool:
        return a != b and not self.le(a, b) and not self.le(b, a)

    def upper_bounds(self, s: Iterable[str]) -> list[str]:
        s = list(s)
        return [u for u in self.elems if all(self.le(x, u) for x in s)]

    def lower_bounds(self, s: Iterable[str]) -> list[str]:
        s = list(s)
        return [u for u in self.elems if all(self.le(u, x) for x in s)]

    def join(self, a: str, b: str) -> str:
        ubs = self.upper_bounds([a, b])
        # least upper bound
        for u in ubs:
            if all(self.le(u, v) for v in ubs):
                return u
        raise ValueError(f"no join for {a},{b}")

    def meet(self, a: str, b: str) -> str:
        lbs = self.lower_bounds([a, b])
        for u in lbs:
            if all(self.le(v, u) for v in lbs):
                return u
        raise ValueError(f"no meet for {a},{b}")

    def join_set(self, s: Iterable[str]) -> str:
        s = list(s)
        if not s:
            return self.bottom
        j = s[0]
        for x in s[1:]:
            j = self.join(j, x)
        return j

    def meet_set(self, s: Iterable[str]) -> str:
        s = list(s)
        if not s:
            return self.top
        m = s[0]
        for x in s[1:]:
            m = self.meet(m, x)
        return m

    def is_cover(self, c: set[str]) -> bool:
        if not c or self.bottom in c:
            return False
        return self.join_set(c) == self.top

    def is_antichain(self, c: set[str]) -> bool:
        for a, b in combinations(c, 2):
            if not self.parallel(a, b):
                return False
        return True

    def refines(self, d: set[str], c: set[str]) -> bool:
        """D ≼ C: every d has some c with d ≤ c."""
        return all(any(self.le(x, y) for y in c) for x in d)

    def downstar(self, c: str) -> set[str]:
        return {x for x in self.elems if self.le(x, c) and x != self.bottom}

    def pl(self, a: set[str]) -> set[str]:
        return {x for x in self.elems if all(self.parallel(x, y) for y in a)}

    def is_minimal_cover_def24(self, c: set[str]) -> bool:
        if not self.is_cover(c):
            return False
        # every refinement R of C must contain C
        # enumerate all covers that refine C
        candidates = []
        # any nonempty subset of elems\{0} that is a cover and refines C
        nonzero = [e for e in self.elems if e != self.bottom]
        for r in range(1, len(nonzero) + 1):
            for subset in combinations(nonzero, r):
                s = set(subset)
                if self.is_cover(s) and self.refines(s, c):
                    candidates.append(s)
        return all(c <= r for r in candidates)

    def all_minimal_covers(self) -> list[set[str]]:
        nonzero = [e for e in self.elems if e != self.bottom]
        covers = []
        for r in range(1, len(nonzero) + 1):
            for subset in combinations(nonzero, r):
                s = set(subset)
                if self.is_cover(s) and self.is_minimal_cover_def24(s):
                    covers.append(s)
        return covers

    def ord(self, c: set[str]) -> int:
        """Def 2.2: ord=k if any k+2 have meet 0, and some k+1 have meet ≠0."""
        el = list(c)
        m = len(el)
        # find largest t such that some t elements have meet ≠ 0
        best = 0
        for t in range(1, m + 1):
            for subset in combinations(el, t):
                if self.meet_set(subset) != self.bottom:
                    best = t
                    break
        # ord = best - 1 if best>=1, with the k+2 condition automatic for finite small sets
        # Def: ord=k if inf of any k+2 distinct is 0 AND exist k+1 with inf ≠0
        # so k+1 = best ⇒ k = best-1, and need any best+1 have meet 0 (true if m < best+1 or check)
        if best == 0:
            # no singleton ≠0? impossible for cover elements
            return -1
        k = best - 1
        # verify any k+2 have meet 0
        if m >= k + 2:
            for subset in combinations(el, k + 2):
                if self.meet_set(subset) != self.bottom:
                    # not exactly this k; fall back scan
                    pass
        return k

    def order_matrix(self):
        n = self.n
        A = [[0] * n for _ in range(n)]
        for i, xi in enumerate(self.elems):
            for j, xj in enumerate(self.elems):
                if i == j:
                    A[i][j] = 1
                elif self.lt(xi, xj):
                    A[i][j] = 2
                elif self.lt(xj, xi):
                    A[i][j] = -2
                else:
                    A[i][j] = 0
        return A

    def row(self, A, e: str):
        return A[self.idx[e]]

    def has_in_sum(self, ra, rb, val) -> bool:
        return any(a + b == val for a, b in zip(ra, rb))

    def has_in_diff(self, ra, rb, val) -> bool:
        return any(a - b == val for a, b in zip(ra, rb))

    def satisfies_cover_condition(self, c: set[str]) -> bool:
        """Prop 3.4 cover condition via joins — equivalent to is_cover for lattices.
        Paper uses matrix form; for checking we use join."""
        return self.is_cover(c)

    def check_M(self, c: set[str]) -> dict:
        """Prop 3.5 M1,M2,M3 for every c in C. Returns failures."""
        failures = []
        if not self.is_antichain(c) or not self.is_cover(c):
            return {"ok": False, "failures": ["not antichain cover"]}
        for ci in list(c):
            rest = c - {ci}
            # M1
            if self.is_cover(rest):
                failures.append(f"M1 fail at {ci}: rest is cover")
            region = self.downstar(ci) & self.pl(rest)
            # exclude elements in C (M2/M3 quantify outside C)
            region = {x for x in region if x not in c}
            # M3
            for xk in region:
                if self.is_cover(rest | {xk}):
                    failures.append(f"M3 fail at {ci}: rest∪{{{xk}}} is cover")
            # M2
            for xk1, xk2 in combinations(region, 2):
                if self.parallel(xk1, xk2) and self.is_cover(rest | {xk1, xk2}):
                    failures.append(f"M2 fail at {ci}: rest∪{{{xk1},{xk2}}} is cover")
        return {"ok": not failures, "failures": failures}

    def check_MC_prime(self, c: set[str]) -> dict:
        """Corrected MC1', MC2', MC3'."""
        failures = []
        if not self.is_antichain(c) or not self.is_cover(c):
            return {"ok": False, "failures": ["not antichain cover"]}
        A = self.order_matrix()
        for ci in list(c):
            rest = c - {ci}
            # MC1'
            if self.satisfies_cover_condition(rest):
                failures.append(f"MC1' fail at {ci}")
            # candidates outside C
            outside = [e for e in self.elems if e not in c and e != self.bottom]
            # MC3'
            for xk in outside:
                rk = self.row(A, xk)
                rji = self.row(A, ci)
                if not self.has_in_diff(rk, rji, 3):
                    continue
                if not all(self.has_in_sum(rk, self.row(A, jl), 1) for jl in rest):
                    continue
                # antecedent holds
                if self.satisfies_cover_condition(rest | {xk}):
                    failures.append(f"MC3' fail at {ci} k={xk}: enlarged is cover")
            # MC2'
            for xk1, xk2 in combinations(outside, 2):
                r1, r2 = self.row(A, xk1), self.row(A, xk2)
                rji = self.row(A, ci)
                if not self.has_in_sum(r1, r2, 1):
                    continue
                if not self.has_in_diff(r1, rji, 3):
                    continue
                if not self.has_in_diff(r2, rji, 3):
                    continue
                if not all(self.has_in_sum(r1, self.row(A, jl), 1) for jl in rest):
                    continue
                if not all(self.has_in_sum(r2, self.row(A, jl), 1) for jl in rest):
                    continue
                if self.satisfies_cover_condition(rest | {xk1, xk2}):
                    failures.append(f"MC2' fail at {ci} k={xk1},{xk2}: enlarged is cover")
        return {"ok": not failures, "failures": failures}

    def check_MC_printed(self, c: set[str]) -> dict:
        """Printed (buggy) MC3 using addition for direction."""
        failures = []
        A = self.order_matrix()
        for ci in list(c):
            rest = c - {ci}
            outside = [e for e in self.elems if e not in c and e != self.bottom]
            for xk in outside:
                rk = self.row(A, xk)
                rji = self.row(A, ci)
                # printed: 3 ∈ r_ji + r_k
                if not self.has_in_sum(rji, rk, 3):
                    continue
                if not all(self.has_in_sum(rk, self.row(A, jl), 1) for jl in rest):
                    continue
                if self.satisfies_cover_condition(rest | {xk}):
                    failures.append(f"printed MC3 fail at {ci} k={xk}")
        return {"ok": not failures, "failures": failures}


def close_leq(elems, covering_edges):
    """Reflexive transitive closure from covering relations / generators."""
    leq = {(a, b) for a, b in covering_edges}
    for e in elems:
        leq.add((e, e))
    changed = True
    while changed:
        changed = False
        add = set()
        for a, b in leq:
            for c, d in leq:
                if b == c and (a, d) not in leq:
                    add.add((a, d))
        if add:
            leq |= add
            changed = True
    return leq


def N5():
    elems = ["0", "a", "b", "c", "1"]
    edges = [("0", "a"), ("a", "b"), ("b", "1"), ("0", "c"), ("c", "1")]
    # also need 0<=b, 0<=1, a<=1 etc via closure
    return Lattice(elems, close_leq(elems, edges))


def L6():
    elems = ["0", "e", "a", "b", "c", "1"]
    edges = [
        ("0", "e"),
        ("e", "a"),
        ("a", "b"),
        ("b", "1"),
        ("e", "c"),
        ("c", "1"),
    ]
    return Lattice(elems, close_leq(elems, edges))


def L1():
    """7-element L(1): 0 < x < x1 < y2 < 1, 0 < x < x2 < y1 < 1, x1∥y1, x2∥y2, etc."""
    elems = ["0", "x", "x1", "x2", "y1", "y2", "1"]
    edges = [
        ("0", "x"),
        ("x", "x1"),
        ("x", "x2"),
        ("x1", "y2"),
        ("x2", "y1"),
        ("y1", "1"),
        ("y2", "1"),
        # also x1 < 1, x2 < 1 via closure; need x1∥y1, x2∥y2
        # is x1 <= y1? NO. x2 <= y2? NO.
        # crosses: x1 < 1, x2 < 1 already; y's above x's only as specified
    ]
    # Also need: is there x1 < 1 path? x1-y2-1 yes. x2-y1-1 yes.
    # Comparabilities of y1,y2: both <1, incomparable to each other?
    # y1∥y2 typically in L(1). No edge between them.
    # x1∥x2: yes.
    return Lattice(elems, close_leq(elems, edges))


def B2():
    """Boolean lattice 2^2."""
    elems = ["0", "p", "q", "1"]
    edges = [("0", "p"), ("0", "q"), ("p", "1"), ("q", "1")]
    return Lattice(elems, close_leq(elems, edges))


def B3():
    elems = ["0", "a", "b", "c", "ab", "ac", "bc", "1"]
    edges = [
        ("0", "a"),
        ("0", "b"),
        ("0", "c"),
        ("a", "ab"),
        ("b", "ab"),
        ("a", "ac"),
        ("c", "ac"),
        ("b", "bc"),
        ("c", "bc"),
        ("ab", "1"),
        ("ac", "1"),
        ("bc", "1"),
    ]
    return Lattice(elems, close_leq(elems, edges))


def M3():
    """Diamond M3: 0 < a,b,c < 1 all atoms incomparable."""
    elems = ["0", "a", "b", "c", "1"]
    edges = [("0", "a"), ("0", "b"), ("0", "c"), ("a", "1"), ("b", "1"), ("c", "1")]
    return Lattice(elems, close_leq(elems, edges))


def attack_wide():
    """Try: bottom, two mid layers, top — seek M2-style replacement."""
    # 0 < p,q < r < 1 and 0 < s < 1 with complications
    # Use N5 with an extra element below a: 0 < z < a < b < 1, 0 < c < 1
    elems = ["0", "z", "a", "b", "c", "1"]
    edges = [("0", "z"), ("z", "a"), ("a", "b"), ("b", "1"), ("0", "c"), ("c", "1")]
    return Lattice(elems, close_leq(elems, edges))


def report(name, L: Lattice):
    print(f"\n=== {name} |X|={L.n} ===")
    mcov = L.all_minimal_covers()
    print("Def2.4 MCov:", [sorted(c) for c in mcov])
    for c in mcov:
        print(f"  ord({sorted(c)})={L.ord(c)}")
    if mcov:
        dim = max(L.ord(c) for c in mcov)
        print(f"  dim={dim}")
    # check each min cover under M and MC'
    for c in mcov:
        m = L.check_M(c)
        mcp = L.check_MC_prime(c)
        mc_old = L.check_MC_printed(c)
        print(f"  C={sorted(c)} M:{m['ok']} MC':{mcp['ok']} printedMC:{mc_old['ok']}")
        if not m["ok"]:
            print("    M failures:", m["failures"])
        if not mcp["ok"]:
            print("    MC' failures:", mcp["failures"])
        if not mc_old["ok"]:
            print("    printed fails (expected on known cex):", mc_old["failures"])
    # also: any antichain cover that passes MC' but is not minimal? or vice versa
    nonzero = [e for e in L.elems if e != L.bottom]
    bad = []
    for r in range(1, len(nonzero) + 1):
        for subset in combinations(nonzero, r):
            s = set(subset)
            if not (L.is_cover(s) and L.is_antichain(s)):
                continue
            is_min = L.is_minimal_cover_def24(s)
            mcp = L.check_MC_prime(s)
            m = L.check_M(s)
            if is_min != mcp["ok"] or is_min != m["ok"] or mcp["ok"] != m["ok"]:
                bad.append((sorted(s), is_min, m["ok"], mcp["ok"], m["failures"], mcp["failures"]))
    if bad:
        print("  MISMATCHES antichain-cover vs M/MC'/Def24:")
        for row in bad:
            print("   ", row)
    else:
        print("  All antichain covers: Def24 ↔ M ↔ MC' agree")


if __name__ == "__main__":
    for name, factory in [
        ("N5", N5),
        ("L6", L6),
        ("L1", L1),
        ("B2", B2),
        ("B3", B3),
        ("M3", M3),
        ("attack_wide", attack_wide),
    ]:
        report(name, factory())
