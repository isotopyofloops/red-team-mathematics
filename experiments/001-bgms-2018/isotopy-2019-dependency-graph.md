# 2019 Paper — Theorem-Level Dependency Graph

**Isotopy, Phase 001-B assignment: dependency graph and blast-radius audit.**

Target: Boyadzhiev, Georgiou, Megaritis, Sereti (2019), "A study of the quasi covering dimension of finite lattices," *Comp. Appl. Math.* 38:109.

## Notation

- **SAFE**: no dependency on 2018 faulty machinery; uses only definitions and/or incidence matrices
- **AFFECTED**: descends from 2018 Theorem 3.7 / Algorithm 3.9 (the row-sum/row-difference bug)
- **IMPORTED**: directly reprinted from the 2018 paper

---

## Layer 0 — Imported 2018 definitions (all SAFE)

These are definitional imports. The 2018 definitions themselves are correct; the error is in the *translation* to matrix conditions.

| Item | Content | Status |
|------|---------|--------|
| Def 1 | Cover of X | SAFE |
| Def 2 | Order of a subset, ord(C) | SAFE |
| Def 3 | Covering dimension, dim(X) | SAFE |
| Def 4 | Incidence matrix T_X | SAFE |
| Def 5 | Order matrix A_X | SAFE |
| Example 1 | Worked example (7-element lattice) | SAFE |

## Layer 1 — Original 2019 theory (§3, all SAFE)

These results develop quasi-covering dimension from first principles. None reference any 2018 algorithm or theorem.

| Item | Content | Depends on | Status |
|------|---------|------------|--------|
| Def 6 | Quasi cover, similarity, refinement | Defs 1-3 | SAFE |
| Def 7 | Quasi covering dimension, dim_q(X) | Def 6 | SAFE |
| **Prop 1** | dim_q(X) = max{dim(↓x) : x dense} | Defs 3, 6, 7 | **SAFE — ground truth route** |
| Remark 1 | dim(X) ≤ dim_q(X); isomorphism invariance | Prop 1 | SAFE |
| Example 2 | Worked dim_q examples | Prop 1 | SAFE |
| Prop 2 | Existence of lattice with arbitrary dim_q, dim=1 | Prop 1 | SAFE |
| Remark 2 | Sublattice can have higher dim_q | — | SAFE |
| Prop 3 | Sublattice with same dense elements: dim_q(Y) ≤ dim_q(X) | Prop 1 | SAFE |
| Remark 3 | Similarity is equivalence relation | Def 6 | SAFE |
| Def 8 | c_x-minimal cover | Def 6 | SAFE |
| Lemma 1 | Existence of c_x-minimal cover refining C | Def 8 | SAFE |
| Prop 4 | dim_q(X) ≤ k iff each c_x-minimal cover has ord ≤ k | Def 8, Lemma 1 | SAFE |
| Corollary 1 | dim_q(X) = max{ord(C) : C ∈ c_x ∈ qc(X,~)} | Prop 4 | SAFE |
| Prop 5 | Every c_x-minimal cover is an antichain | Def 8 | SAFE |

## Layer 2 — Properties (§4, all SAFE)

Product operations on quasi-covering dimension. No algorithmic dependencies.

| Item | Content | Depends on | Status |
|------|---------|------------|--------|
| Def 9 | Linear sum X ⊕ Y | — | SAFE |
| Remark 4 | dim_q(X ⊕ Y) ≠ dim_q(Y ⊕ X) in general | Example | SAFE |
| Def 10 | Cartesian product X × Y | — | SAFE |
| Lemma 2 | ↓(x,y) = ↓x × ↓y in X × Y | Def 10 | SAFE |
| Lemma 3 | (x,y) dense iff x dense and y dense | Def 10 | SAFE |
| Prop 6 | dim_q(X × Y) = max{dim_q(X), dim_q(Y)} | Prop 1, Lemmas 2-3, Zhang 2017 | SAFE |
| Remark 5 | Cartesian product properties | Prop 6 | SAFE |
| Def 11 | Lexicographic product X ◇ Y | — | SAFE |
| Remark 6 | Subadditivity fails for ◇ | Example | SAFE |
| Def 12 | Rectangular product X□Y | — | SAFE |
| Remark 7 | Subadditivity fails for □ | Example | SAFE |

## Layer 3 — Dense element characterization (§5, all SAFE)

Uses **incidence matrix** T_X, completely independent of the order-matrix bug.

| Item | Content | Depends on | Status |
|------|---------|------------|--------|
| Notation 1 | B_m matrix (from 2018) | — | SAFE |
| **Prop 7** | x_i dense iff max(c_i(T_X) + c_j(T_X) - B_1) = 2 ∀j≠i | Incidence matrix T_X | **SAFE — verified by Alethon** |
| **Alg 1** | Find all dense elements D(X) | Prop 7 | **SAFE — verified by Alethon** |
| Example 3 | Worked dense-element computation | Alg 1 | SAFE |

## Layer 4 — Imported 2018 cover machinery (§6, SAFE imports)

| Item | Content | Depends on | Status |
|------|---------|------------|--------|
| Def 13 | Minimal cover (from Dube 2015) | Def 1 | SAFE |
| Def 14 | Cover condition (from 2018) | Order matrix A_X | SAFE (the cover condition itself is correct) |
| Prop 8 | Cover condition characterizes covers | Def 14, 2018 Prop 3.4 | SAFE (survives current audit) |

## Layer 5 — AFFECTED: faulty algorithm chain (§6)

This is where the 2018 bug enters the 2019 paper. The dependency chain is:

```
2018 Theorem 3.7 (FALSE)
  → 2018 Algorithm 3.9 (FALSE)
    → 2019 Algorithm 2, Step 8 (INHERITED)
      → 2019 Algorithm 3, Step 4 (INHERITED)
        → 2019 Proposition 9 (INHERITED)
          → 2019 Algorithm 4, Step 4 (INHERITED)
```

| Item | Content | Depends on | Status | Certificate |
|------|---------|------------|--------|-------------|
| **Alg 2** | Find MCov(X) — all minimal covers | Def 14, Prop 8, **2018 Thm 3.7** | **AFFECTED** — Step 8 reprints faulty MC1-MC3 | N5 |
| **Alg 3** | Compute dim(X) via minimal covers | **Alg 2** | **AFFECTED** — Step 4 calls Alg 2 for M(X) | L6={0}⊕N5 |
| **Prop 9(1)** | L_x formula using M(↓x) | **Alg 2**, cites 2018 Thm 5.2 proof | **AFFECTED** | L6 |
| **Prop 9(2)** | dim_q(X) = max{L_x : x dense} | **Prop 9(1)**, Prop 1 | **AFFECTED** via Part (1) | L6 |
| **Alg 4** | Compute dim_q(X) | **Alg 1** (SAFE), **Alg 3** (AFFECTED) | **AFFECTED** — Step 4 calls Alg 3 | L6: prints 0, true value 1 |
| Example 4(1) | dim_q = 1 for 6-element lattice | Algs 1-3 | Correct by non-trigger (Alethon) | — |
| Example 4(2) | dim_q = 2 for 9-element lattice | Algs 1-3 | Correct by non-trigger (Alethon) | — |

## Key structural observations

1. **The theoretical half of the paper is entirely sound.** Sections 3-5 (Props 1-7, Lemmas 1-3, Corollary 1, Algorithm 1) develop quasi-covering dimension from definitions and prove its properties using only lattice theory and incidence matrices. None of this machinery touches the faulty 2018 order-matrix algorithm.

2. **Proposition 1 provides an independent ground-truth route.** `dim_q(X) = max{dim(↓x) : x dense}` is proved directly from definitions. Combined with the sound Algorithm 1 (dense-element detection via incidence matrix), this gives a correct two-step procedure: find dense elements, then compute dim(↓x) from Definition 3 for each. The only missing piece is an efficient algorithm for dim(↓x) from definitions — but correctness is assured.

3. **The computational half inherits the 2018 bug exactly.** Algorithm 2 reprints Algorithm 3.9 with the same row-sum error in MC2/MC3. The error propagates mechanically through Algorithms 3 and 4.

4. **The error direction is one-sided.** The faulty conditions are strictly stronger than the correct ones (row-sum detects comparability in both directions; row-difference detects only the required direction). So M(X) ⊆ MCov(X): the algorithm can only *discard* genuine minimal covers, never *create* false ones. This means dim_q values computed by Algorithm 4 are **lower bounds**, never overestimates.

5. **Six elements is minimal for the computational failure.** Alethon's exhaustive search found no ≤5-element lattice where Algorithm 4 returns the wrong dim_q. L5 = {0,e,a,b,1} has dim_q=1 and Algorithm 4 correctly returns 1 (the above-element trap doesn't fire). The L6={0}⊕N5 certificate is the smallest computational counterexample for the quasi-covering pipeline.

---

## Separation: citation propagation vs logical error propagation

The 2019 paper cites the 2018 paper in three distinct ways:

1. **Definitional import** (Defs 1-5, Notation 1): The definitions are correct. Citation is operational but carries no error.

2. **Result import with independent proof** (Prop 8 / cover condition): The imported result has survived current audit. Citation is operational and currently sound.

3. **Algorithm import with inherited defect** (Alg 2 = 2018 Alg 3.9): The algorithm is reprinted with the same bug. Citation transmits the actual logical error.

Only category 3 constitutes error propagation. A paper citing the 2019 paper could cite it for the theory (Props 1-7, safe) or for the algorithm (Algs 2-4, affected). Phase 001-C must distinguish these.
