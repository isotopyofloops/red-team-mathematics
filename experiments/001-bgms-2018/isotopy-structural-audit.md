# Experiment 001 — Structural/Dependency Audit

**Paper:** Boyadzhiev, Georgiou, Megaritis, Sereti. "A study of a covering dimension of finite lattices." *Applied Mathematics and Computation* 333 (2018) 276–285.

**Role:** Translate matrix predicates back to order/lattice language, map proposition dependencies, work small lattices through both paths, identify where the matrix representation loses or changes information.

**Disclosure:** I do not recognize this paper or any known criticism of it from training data. The analysis below is independent.

---

## 1. Translation of matrix predicates (Section 3)

The paper defines two matrices for a finite poset (X, ≤) with X = {x₁, ..., xₙ}, x₁ = 0_X, xₙ = 1_X:

**Incidence matrix** T_X^≤ = (t_{ij}): t_{ij} = 1 if x_i ≤ x_j, else 0.

**Order matrix** A_X^≤ = (a_{ij}):
- a_{ij} = 1 if i = j
- a_{ij} = 2 if x_i < x_j
- a_{ij} = −2 if x_j < x_i
- a_{ij} = 0 if x_i ‖ x_j

### Proposition 3.1 — Comparability and strict order

**(1)** x_{k₁} ‖ x_{k₂} iff 1 ∈ r_{k₁}(A) + r_{k₂}(A).

**Translation:** The row sum can only hit 1 at column k₁ (where a_{k₁,k₁} + a_{k₂,k₁} = 1 + 0) or column k₂ (symmetrically). Off-diagonal entries are in {2, −2, 0}, so their pairwise sums are in {4, 0, 2, −2, −4} — never 1. The value 1 appears iff at least one diagonal entry is paired with 0 (incomparability). **Correct. ✓**

**(2)** x_{k₁} < x_{k₂} iff 3 ∈ r_{k₁}(A) − r_{k₂}(A).

**Translation:** The difference hits 3 only at column k₁, where a_{k₁,k₁} − a_{k₂,k₁} = 1 − (−2) = 3 requires a_{k₂,k₁} = −2, i.e., x_{k₁} < x_{k₂}. No other column combination reaches 3 (max of 2 − (−2) = 4 requires both entries at their extremes, but the 1 = 3 route is the only path through the diagonal). **Uses SUBTRACTION. Correct. ✓**

**Critical observation:** Proposition 3.1(1) uses ADDITION (symmetric, tests incomparability). Proposition 3.1(2) uses SUBTRACTION (asymmetric, tests directed strict order). These are different operations testing different things.

### What does "3 ∈ r_a(A) + r_b(A)" test?

This is NOT the same as Proposition 3.1(2). Let me compute what the SUM detects:

(r_a + r_b)_p = a_{a,p} + a_{b,p}.

- At p = a: a_{a,a} + a_{b,a} = 1 + a_{b,a}. This equals 3 iff a_{b,a} = 2, i.e., x_b < x_a.
- At p = b: a_{a,b} + a_{b,b} = a_{a,b} + 1. This equals 3 iff a_{a,b} = 2, i.e., x_a < x_b.
- At p ∉ {a,b}: both entries are in {2, −2, 0}, sum in {4, 0, 2, −2, −4}. Never 3.

**Therefore: 3 ∈ r_a(A) + r_b(A) iff x_a and x_b are COMPARABLE (one is strictly less than the other). It does NOT distinguish which direction.**

This is the key fact for the audit.

### Definition 3.3 — Cover condition

(1) Singleton {x_j}: satisfies cover condition iff 3 ∉ r_j(A) − r_n(A). Translation: x_j is not strictly less than x_n, i.e., x_j = x_n = 1_X. **Correct. ✓**

(2) Antichain {x_{j₁},...,x_{jₘ}}, m ≥ 2: satisfies cover condition iff 2m + 2 ∉ r_{j₁}(A) + ··· + r_{jₘ}(A) + (−1)·r_n(A). Translation: there is no x_k (with k < n, k ∉ {j₁,...,jₘ}) such that x_{jᵢ} < x_k for all i, which is equivalent to ⋁C = 1_X. **Correct. ✓**

### Proposition 3.4 — Cover condition ↔ cover

Both parts correctly translate between the cover condition and being a cover. **Correct. ✓**

---

## 2. Proposition 3.5 — Lattice characterization of minimal covers

C = {x_{j₁},...,x_{jₘ}} (antichain cover) is minimal iff for every i ∈ {1,...,m}:

**(M1)** C \ {x_{jᵢ}} is not a cover.
**(M2)** For every k₁, k₂ ∉ C with x_{k₁} ‖ x_{k₂}, x_{k₁}, x_{k₂} ∈ ↓*x_{jᵢ} ∩ Pl(C\{x_{jᵢ}}): (C\{x_{jᵢ}}) ∪ {x_{k₁}, x_{k₂}} is **NOT a cover.**
**(M3)** For every k ∉ C with x_k ∈ ↓*x_{jᵢ} ∩ Pl(C\{x_{jᵢ}}): (C\{x_{jᵢ}}) ∪ {x_k} is **NOT a cover.**

Where ↓*x_{jᵢ} = {x ∈ X : x ≤ x_{jᵢ}} \ {0_X} requires x_k **< x_{jᵢ}** (strictly below, not above).

---

## 3. Theorem 3.7 — Matrix characterization of minimal covers

**(MC1)** C \ {x_{jᵢ}} does not satisfy cover condition. — Translates (M1). **Correct. ✓**

**(MC2)** If k₁, k₂ satisfy:
- 1 ∈ r_{k₁}(A) + r_{k₂}(A) — x_{k₁} ‖ x_{k₂} ✓
- **3 ∈ r_{jᵢ}(A) + r_{k₁}(A)** — tests **comparability** of x_{jᵢ} and x_{k₁}
- **3 ∈ r_{jᵢ}(A) + r_{k₂}(A)** — tests **comparability** of x_{jᵢ} and x_{k₂}
- 1 ∈ r_{k₁}(A) + r_{jₗ}(A) for all l ≠ i — x_{k₁} ‖ x_{jₗ} ✓
- 1 ∈ r_{k₂}(A) + r_{jₗ}(A) for all l ≠ i — x_{k₂} ‖ x_{jₗ} ✓

then (C\{x_{jᵢ}}) ∪ {x_{k₁}, x_{k₂}} **does NOT satisfy** cover condition.

**Error (direction loss):** The condition "3 ∈ r_{jᵢ}(A) + r_{k₁}(A)" tests comparability (symmetric). The lattice condition (M2) requires x_{k₁} ∈ ↓*x_{jᵢ}, meaning x_{k₁} < x_{jᵢ} (directional). The correct matrix test is "3 ∈ r_{k₁}(A) − r_{jᵢ}(A)" (Proposition 3.1(2)). The addition picks up pairs where x_{jᵢ} < x_{k₁} (above, not below), which should not qualify.

**(MC3)** If k satisfies:
- **3 ∈ r_{jᵢ}(A) + r_k(A)** — tests **comparability**, not x_k < x_{jᵢ}
- 1 ∈ r_k(A) + r_{jₗ}(A) for all l ≠ i — x_k ‖ x_{jₗ} ✓

then (C\{x_{jᵢ}}) ∪ {x_k} does NOT satisfy cover condition.

**Same error (direction loss):** Same as MC2. The condition should be "3 ∈ r_k(A) − r_{jᵢ}(A)" to test x_k < x_{jᵢ}. With addition, it picks up x_{jᵢ} < x_k (wrong direction).

---

## 4. Concrete witness

### Lattice: X from Fig. 2 / Example 3.10

X = {x₁,...,x₈} with order matrix as given on p. 280.

Key relations from the order matrix:
- x₃ ‖ x₄ (a₃₄ = 0)
- x₃ < x₆ (a₃₆ = 2)
- x₄ ‖ x₆ (a₄₆ = 0)
- x₆ ‖ x₅ (a₅₆ = 0)

### Claim: C = {x₃, x₄} is a minimal cover of X

**Cover verification:** x₃ ‖ x₄ (antichain). Upper bounds of {x₃, x₄}: x₅ is above x₄ (a₄₅ = 2) but x₅ ‖ x₃ (a₃₅ = 0) — not an upper bound. x₆ is above x₃ (a₃₆ = 2) but x₆ ‖ x₄ (a₄₆ = 0) — not an upper bound. x₇ above x₄ (a₄₇ = 2) but x₇ ‖ x₃ (a₃₇ = 0) — not an upper bound. Only x₈ is above both. So x₃ ∨ x₄ = x₈ = 1_X. ✓

**Cover condition verification:** 2·2 + 2 = 6.
r₃ + r₄ − r₈ = (−2, 0, 1, 1, 2, 2, 2, 4) + (2, 2, 2, 2, 2, 2, 2, −1) = (−2 + 2, 0 + 0, 1 + 0, 0 + 1, 0 + 2, 2 + 0, 0 + 2, 2 + 2) + (2, 2, 2, 2, 2, 2, 2, −1).

Let me recompute carefully:
r₃ = (−2, 0, 1, 0, 0, 2, 0, 2)
r₄ = (−2, 0, 0, 1, 2, 0, 2, 2)
r₈ = (−2, −2, −2, −2, −2, −2, −2, 1)

r₃ + r₄ = (−4, 0, 1, 1, 2, 2, 2, 4)
−r₈ = (2, 2, 2, 2, 2, 2, 2, −1)
r₃ + r₄ − r₈ = (−2, 2, 3, 3, 4, 4, 4, 3)

6 ∉ {−2, 2, 3, 4}. Cover condition satisfied. ✓

**Minimality verification (direct):** Remove x₃ → {x₄}, ⋁{x₄} = x₄ ≠ 1_X. Remove x₄ → {x₃}, ⋁{x₃} = x₃ ≠ 1_X. Any refinement D ≪ {x₃, x₄} has D ⊆ {x₁, x₃, x₄} (elements ≤ x₃ or ≤ x₄). The only cover from these is {x₃, x₄} itself. Minimal. ✓

### (MC3) gives a false prediction for C = {x₃, x₄}

For i = 1 (remove x₃, j₁ = 3), test k = 6:

**Hypothesis check:**

"3 ∈ r₃(A) + r₆(A)":
r₃ = (−2, 0, 1, 0, 0, 2, 0, 2)
r₆ = (−2, −2, −2, 0, 0, 1, 0, 2)
r₃ + r₆ = (−4, −2, −1, 0, 0, **3**, 0, 4)

3 appears at position 6 (from a₃₆ + a₆₆ = 2 + 1 = 3, reflecting x₃ < x₆). **Hypothesis satisfied. ✓**

"1 ∈ r₆(A) + r₄(A)" (x₆ ‖ x₄):
r₆ + r₄ = (−4, −2, −2, **1**, 2, **1**, 2, 4)

1 appears at positions 4 and 6. **Hypothesis satisfied. ✓**

All conditions of (MC3) hold for k = 6.

**Conclusion claimed by (MC3):** {x₄, x₆} does not satisfy the cover condition (= is not a cover).

**Actual fact:** ⋁{x₄, x₆}: upper bounds of {x₄, x₆}. x₅: above x₄ (a₄₅ = 2) but x₅ ‖ x₆ (a₅₆ = 0). x₇: above x₄ but x₇ ‖ x₆. Only x₈ is above both. So x₄ ∨ x₆ = x₈ = 1_X. {x₄, x₆} **IS a cover.**

Direct matrix check: r₄ + r₆ − r₈ = (−4, −2, −2, 1, 2, 1, 2, 4) + (2, 2, 2, 2, 2, 2, 2, −1) = (−2, 0, 0, 3, 4, 3, 4, 3). 6 ∉ {−2, 0, 3, 4}. **Cover condition satisfied.**

**(MC3) gives a false answer.** It claims {x₄, x₆} is not a cover, but it is.

### Why the error occurs

The lattice condition (M3) requires x_k ∈ ↓*x_{jᵢ}, meaning x_k < x_{jᵢ}. Here x₆ > x₃ (not x₆ < x₃). The matrix test "3 ∈ r₃ + r₆" detects that x₃ and x₆ are comparable but does not check which direction. The correct test "3 ∈ r₆ − r₃" would detect x₆ < x₃, which is FALSE, and the hypothesis would correctly fail.

### Consequence for Algorithm 3.9

Algorithm 3.9, Step 8 applies (MC1)+(MC2)+(MC3) to filter covers into minimal covers. For C = {x₃, x₄}:

- (MC3) fails (false prediction for k = 6)
- Algorithm rejects {x₃, x₄} as "not minimal"
- But {x₃, x₄} IS minimal

The algorithm misses a genuine minimal cover.

### Additional: Example 3.10 is independently incorrect

The paper claims A₂(X) = {{x₂,x₇}, {x₃,x₅}, {x₄,x₆}, {x₅,x₆}, {x₅,x₇}, {x₆,x₇}}, omitting {x₃,x₄} and {x₃,x₇} (both verified to satisfy the cover condition). It claims MCov(X) = {{x₂,x₃,x₄}}, but {x₂,x₃,x₄} is not minimal (since {x₃,x₄} ≪ {x₂,x₃,x₄} and {x₃,x₄} is a cover). The true MCov(X) includes {x₈}, {x₂,x₇}, and {x₃,x₄}.

---

## 5. Error classification

| # | Location | Type | Description |
|---|----------|------|-------------|
| 1 | Theorem 3.7, (MC3) | **False intermediate theorem** | Uses "3 ∈ r_{jᵢ}(A) + r_k(A)" (comparability, symmetric) where the lattice condition (M3) requires x_k < x_{jᵢ}, needing "3 ∈ r_k(A) − r_{jᵢ}(A)" (directed, asymmetric). The addition admits pairs where x_{jᵢ} < x_k (wrong direction), producing false conclusions. |
| 2 | Theorem 3.7, (MC2) | **False intermediate theorem** | Same directional error as #1: uses row addition (comparability) where row subtraction (directed order) is needed. |
| 3 | Example 3.10 | **Computational error** | A₂(X) omits {x₃,x₄} and {x₃,x₇}. MCov(X) given as {{x₂,x₃,x₄}} which is not minimal. |

**Primary defect:** The matrix translation of the ↓*x_{jᵢ} condition (x_k strictly below x_{jᵢ}) uses row addition where it must use row subtraction. Row addition is symmetric and detects comparability; row subtraction is asymmetric and detects directed strict order — exactly the distinction Proposition 3.1 defines. The paper uses the correct operation (subtraction) in Prop 3.1(2) but switches to the wrong operation (addition) in Theorem 3.7's conditions (MC2) and (MC3).

**Smallest certificate:** Lattice X from Fig. 2, cover C = {x₃, x₄}, parameter k = 6 in (MC3) for i = 1. The matrix condition fires (x₃ comparable to x₆, x₆ incomparable to x₄) and predicts {x₄, x₆} is not a cover. But {x₄, x₆} is a cover (⋁ = x₈ = 1_X, and 6 ∉ r₄ + r₆ − r₈).

---

## 6. Downstream blast radius

### Directly affected:

- **Algorithm 3.9 (Step 8):** Uses (MC1)+(MC2)+(MC3) to identify minimal covers. The direction error causes it to reject genuine minimal covers (proven by example).

- **Algorithm 5.4:** Computes dim(X) via Algorithm 3.9. Since 3.9 may produce wrong MCov(X), the computed dimension could be wrong.

- **Theorem 6.4:** States dim(X∘Y) = dim(X⊕Y) = L − 1 where L is computed from M(Y) (Algorithm 3.9's output). The proof cites Theorem 3.7 to equate M(Y) with MCov(Y). If M(Y) ≠ MCov(Y), the computation is invalid.

### Not affected:

- **Propositions 3.1, 3.2:** Correct matrix characterizations of comparability and antichain. ✓
- **Definition 3.3 / Proposition 3.4:** Cover condition correctly characterizes covers. ✓
- **Proposition 3.5:** Lattice-theoretic characterization of minimal covers using (M1)+(M2)+(M3). Independent of matrix translation. ✓
- **Theorem 4.2:** Order computation using incidence matrix (column sums). Uses T_X^≤, not A_X^≤. Different machinery, correct. ✓
- **Remark 6.3:** Results about dim of lexicographic products/linear sums from [5]. Uses MCov directly, not the matrix algorithm. ✓

### Summary: The theoretical results about covering dimension are correct. The matrix translation of the minimality filter (Theorem 3.7) is wrong, and both algorithms that depend on it (3.9 and 5.4) can produce incorrect output.

---

## 7. What is NOT affected — and what the paper gets right

The paper's contributions that survive the defect:
1. The order matrix A_X^≤ faithfully encodes the lattice order (Prop 3.1). ✓
2. The cover condition (Def 3.3) correctly characterizes covers via row sums (Props 3.4). ✓
3. The order computation via incidence matrix columns (Theorem 4.2) is correct. ✓
4. Proposition 3.5 gives a correct lattice-theoretic characterization of minimal covers. ✓

The defect is localized to the translation of Proposition 3.5's directional conditions (↓*x_{jᵢ}) into matrix operations in Theorem 3.7.

---

*Analysis by Isotopy, 2026-08-20. Independent structural audit from the paper without external sources.*
*STOP POINT reached: certificate and classification reported. Proposed repair in separate section below.*

---

## POST-DEBRIEF CORRECTIONS (2026-08-21, after Rheon's cross-auditor report)

Two errors in my report, identified by Rheon's independent verification:

### Correction 1: Certificate C = {x₃, x₄} is INVALID

I misread the order matrix. Entry a₃₇ is **2** (x₃ < x₇), not 0 (x₃ ‖ x₇). This is confirmed by the antisymmetric entry a₇₃ = −2 in row 7.

With the correct reading: upper bounds of {x₃, x₄} include x₇ (since x₃ < x₇ and x₄ < x₇), and x₇ < x₈. So x₃ ∨ x₄ = x₇ ≠ x₈ = 1_X. **{x₃, x₄} is NOT a cover**, and Theorem 3.7 does not apply to it. My entire certificate construction was built on this misread entry.

The claims in Section 4 that depended on this (cover verification, minimality verification, MC3 false prediction, Example 3.10 analysis) are all invalidated.

### Correction 2: MC2 conclusion direction is correct

I claimed M2 says the replacement "IS a cover" while MC2 says "NOT a cover" (Error B). This was a misreading of M2. M2 itself says the replacement is NOT a cover. The genuine MC2 bug is solely the directional error (addition vs subtraction), same as MC3. There is no separate conclusion-reversal error.

### What survives from my report

The theorem-level diagnosis is correct: (MC2) and (MC3) use row addition (symmetric, comparability) where they need row subtraction (asymmetric, directed order). This was independently confirmed by all four auditors. The mechanism description — "a matrix predicate intended to encode a directional order relation actually encoded a symmetric one" — was specifically endorsed by Rheon.

### Valid certificates from other auditors

- **Fable:** N₅ (5 elements) falsifies Theorem 3.7. {0} ⊕ N₅ (6 elements) makes Algorithm 5.4 return dim = 0 when true dim = 1. This 6-element example was independently found by Rheon computationally.
- **Alethon:** 7-element lattice where the error propagates through Algorithm 3.9 to give wrong dimension.

### Lesson

Matrix misread → invalid certificate → cascading false claims (cover verification, minimality, MC3 prediction, Example 3.10 analysis). The theorem-level mechanism was correct, but the specific witness was not independently verified against the paper. Rheon's protocol (independent certificate verification) caught exactly this failure mode.

---

## 8. Proposed repair (separate section per instructions)

### Fix for (MC3):

Replace "3 ∈ r_{jᵢ}(A_X^≤) + r_k(A_X^≤)" with "3 ∈ r_k(A_X^≤) − r_{jᵢ}(A_X^≤)".

This correctly tests x_k < x_{jᵢ} (Proposition 3.1(2) with k₁ = k, k₂ = jᵢ).

### Fix for (MC2):

1. Replace "3 ∈ r_{jᵢ}(A_X^≤) + r_{k₁}(A_X^≤)" with "3 ∈ r_{k₁}(A_X^≤) − r_{jᵢ}(A_X^≤)" (and similarly for k₂).

### Verification of repair

My original {x₃, x₄} witness is invalid (see Correction 1 above — a₃₇ = 2, not 0, so {x₃, x₄} is not a cover). For valid repair verification, see Fable's N₅ certificate (`isotopy-fable-repair-audit.md`) and Alethon's 7-element certificate (`alethon-certificates-n5-l6.md`), both independently verified by `verify_certificates.py`.
