# Experiment 001 — Alethon certificates: N₅ and {0}⊕N₅

**Role:** Algebraic / adversarial search (Alethon). Collaborative phase item (3).

Paper: Boyadzhiev–Georgiou–Megaritis–Sereti, Appl. Math. Comput. 333 (2018).
Aligned with Rheon’s blind-phase ledger (mail-1161). Human-checkable.

Conventions from Defs 2.1–2.4, 2.6; Prop 3.1(2); Thm 3.7 (MC3).

---

## Certificate A — N₅ falsifies Theorem 3.7

**Lattice N₅** (5 elements):

```
      1
     / \
    b   c
   /   /
  a   /
   \ /
    0
```

Order: `0 < a < b < 1`, `0 < c < 1`, and `a ∥ c`, `b ∥ c`.

**Def 2.4 ground truth.** Unique minimal cover is `C = {a, c}`:
- Cover: `a ∨ c = 1`, `0 ∉ C`.
- Antichain: `a ∥ c`.
- Only nonzero elements ≤ `a` (resp. `c`) are `a` (resp. `c`), so the only refinement of `C` is `C` itself; hence `C ⊆ R` for every refinement `R`.
- `{b,c}` is a cover but not minimal: `{a,c} ≼ {b,c}` and `{b,c} ⊈ {a,c}`.
- `{1}` is not minimal: `{a,c}` refines `{1}` and does not contain `1`.

**ord / dim.** `a ∧ c = 0`, so `ord(C) = 0`. By Cor. 1.2, `dim(N₅) = 0`.
(This certificate is for Thm 3.7, not for a dim-algorithm mismatch.)

**Theorem 3.7 rejects C.** Index `i` for drop of `a`. Candidate `k = b`:
- Prop 3.1 / order-matrix: `a < b` gives an entry `2` in `r_a` and `-2` in `r_b` at the paired columns; in particular `3 ∈ r_a(A) + r_b(A)` (printed MC3 uses **addition**).
- `b ∈ Pl({c})` because `b ∥ c`, and `b ∉ C`.
- Antecedent of (MC3) holds for `k = b`.
- Consequent requires `(C \ {a}) ∪ {b} = {b,c}` is **not** a cover — but `b ∨ c = 1`, so it **is** a cover.

Hence (MC3) fails → Thm 3.7 declares `C` non-minimal → **false**.

**Set-theoretic contrast (Prop 3.5).** Candidates for (M3) must lie in `↓*a ∩ Pl({c})`. Elements strictly below `a`: none nonzero. So the candidate set is empty and (M3) holds vacuously. Prop 3.5 correctly keeps `C` minimal.

**Root cause (same as L(1)).** Prop 3.1(2) needs `3 ∈ r_k − r_{j_i}` (`x_k < x_{j_i}`). Printed MC3 uses `3 ∈ r_{j_i} + r_k`, which is also true for `x_{j_i} < x_k` (here `a < b`).

---

## Certificate B — {0}⊕N₅ falsifies Algorithm 5.4 / Theorem 5.2

**Lattice L₆ = {0} ⊕ N₅** (6 elements): ordinal sum — a new bottom `0` strictly below a copy of N₅ whose former bottom is renamed `e`.

```
        1
       / \
      b   c
     /   /
    a   /
     \ /
      e
      |
      0
```

Order: `0 < e < a < b < 1`, `0 < e < c < 1`, and `a ∥ c`, `b ∥ c`.

(This is the same order type as `{0,e,a,b,c,1}` in the Exp 001 STOP report.)

**Def 2.4 ground truth.** Unique minimal cover `C = {a,c}`:
- `a ∨ c = 1`.
- Same refinement argument as above (nothing nonzero strictly below `a` or `c` that stays incomparable to the other).
- Meet: `a ∧ c = e ≠ 0`, so `ord(C) = 1`.
- Hence **`dim(L₆) = 1`**.

**Theorem 3.7 / Algorithm 3.9.** Same false (MC3) fire as in Certificate A with `k = b` when dropping `a` (`a < b` triggers the row-sum test; `{b,c}` is a cover). So Alg 3.9 omits `C` from `M(X)`.

**Algorithm 5.4 / Theorem 5.2.** With no minimal cover of order 1 recorded, the algorithms output **`dim(L₆) = 0`**, contradicting Def 2.3–2.4 / Cor. 1.2.

**Finite check list (human):**
1. Confirm lattice axioms (all pairwise joins/meets exist) — standard for N₅ and ordinal sum with a new bottom.
2. Confirm `C = {a,c}` is a cover and Def 2.4-minimal.
3. Confirm `a ∧ c = e ≠ 0` ⇒ `ord = 1` ⇒ `dim = 1`.
4. Confirm printed (MC3) fires on `k = b` via `3 ∈ r_a + r_b`.
5. Confirm Alg 5.4 path yields 0.

---

## Relation to Alethon’s 7-element L(1) certificate

L(1) from the STOP report is a 7-element lattice with the same directional bug and the same dim `1 ↦ 0` failure. N₅ is the **smallest** Thm 3.7 counterexample (characterization only). L₆ = {0}⊕N₅ is the **smallest** final-algorithm counterexample (matches Rheon/Fable). L(1) remains a valid independent witness of the full pipeline failure.

## Repair (unchanged)

Replace every `3 ∈ r_{j_i}(A) + r_k(A)` in Thm 3.7 / Alg 3.9 by the Prop 3.1(2) form `3 ∈ r_k(A) − r_{j_i}(A)` (and the analogous change for MC2). Re-check on N₅, L₆, L(1).

— Alethon
