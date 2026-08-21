# Experiment 001 — Structural audit of Fable's Proposition 3.5 repair

**Task:** Attack the repaired proof. Try to break it, not improve its wording. Also verify the corrected Theorem 3.7 and look for counterexamples to the Proposition 3.5 statement itself.

---

## 1. Audit of the six adversarial targets

### Target 1: Is D genuinely join-closed?

D = (↓\*c ∩ Pl(C \ {c})) ∪ {c}.

Take u, v ∈ D. Since u, v ≤ c, we have u ∨ v ≤ c.

**Case u ∨ v = c:** Then u ∨ v ∈ D. ✓

**Case u ∨ v < c:** Need u ∨ v ∈ ↓\*c ∩ Pl(C \ {c}).

First, u ∨ v ≠ 0_X: u ∈ D implies u ≥ some element > 0_X (since u = c or u ∈ ↓\*c, both > 0_X). So u ∨ v ≥ u > 0_X. ✓

Suppose u ∨ v ≤ d for some d ∈ C \ {c}. Then u ≤ u ∨ v ≤ d. If u ∈ ↓\*c ∩ Pl(C \ {c}), then u ‖ d, contradicting u ≤ d. If u = c, then c ≤ u ∨ v (since u = c ≤ u ∨ v), so c ≤ u ∨ v, but u ∨ v ≤ c, so u ∨ v = c — contradicts the case assumption u ∨ v < c. ✗

Suppose d ≤ u ∨ v for some d ∈ C \ {c}. Then d ≤ u ∨ v < c, so d < c. But d, c ∈ C and C is an antichain. ✗

Both branches produce contradictions, so u ∨ v ∈ Pl(C \ {c}). Combined with u ∨ v < c and u ∨ v ≠ 0_X: u ∨ v ∈ ↓\*c ∩ Pl(C \ {c}) ⊆ D. ✓

**Verdict: Sound. No gap found.**

### Target 2: Does every element of R \ K lie below W?

For r ∈ R \ K: since R ≪ C, ∃ d ∈ C with r ≤ d.

If d ∈ C \ {c}: r ≤ d ≤ W. Done.

If d = c: then r ≤ c. Since c ∉ R and r ∈ R, r ≠ c, so r < c. Since r ∉ K, either r = 0_X (impossible: 0_X ∉ R since R is a cover) or r ∉ Pl(C \ {c}). The latter means ∃ d' ∈ C \ {c} with r comparable to d'. If d' ≤ r: then d' ≤ r < c, so d' < c, contradicting C being an antichain. So r ≤ d' ≤ W. ✓

Therefore ⊗(R \ K) ≤ W. Combined with ⊗R = ⊗(R \ K) ∨ ⊗K = 1, we get W ∨ ⊗K = 1.

**Verdict: Sound. No gap found.**

### Target 3: Does s = ⊗K necessarily belong to D?

K ⊆ ↓\*c ∩ Pl(C \ {c}) ⊆ D (each element of K is in R, so ≠ 0_X, and satisfies r < c and r ∈ Pl(C \ {c})). D is join-closed (Target 1). By induction on |K|, ⊗K ∈ D.

**Verdict: Sound. No gap found.**

### Target 4: In Case 2, is z = ⊗(K' \ {u}) guaranteed to lie in D \ {c}, with z ≠ 0_X?

K' ⊆ K is minimal under inclusion with ⊗K' = c. Since every element of K is strictly below c, |K'| ≥ 2. Choose u ∈ K'. Put z = ⊗(K' \ {u}).

**z ∈ D:** K' \ {u} ⊆ K ⊆ D. D join-closed ⟹ z ∈ D. ✓

**z < c:** By minimality of K', no proper subset joins to c. K' \ {u} is proper, so ⊗(K' \ {u}) ≠ c. But ⊗(K' \ {u}) ≤ ⊗K' = c. So z ≤ c and z ≠ c, hence z < c. ✓

**z ∈ D \ {c}:** z < c ⟹ z ≠ c. z ∈ D. So z ∈ D \ {c} = ↓\*c ∩ Pl(C \ {c}). ✓

**z ≠ 0_X:** If z = 0_X, then c = z ∨ u = 0_X ∨ u = u. But u ∈ K, so u < c. Then c = u < c. ✗

**z ∉ C:** z ∈ Pl(C \ {c}), so z ‖ all d ∈ C \ {c}. And z < c, so z ≠ c. Therefore z ∉ C. ✓

**Verdict: Sound. No gap found.**

### Target 5: Are z and u necessarily incomparable?

If z ≤ u: c = z ∨ u = u. But u < c (u ∈ K). Contradiction. ✗
If u ≤ z: c = z ∨ u = z. But z < c. Contradiction. ✗

So z ‖ u. ✓

**Verdict: Sound. No gap found.**

### Target 6: Do the constructed witnesses satisfy ALL hypotheses of M2/M3?

**Case 1 → (M3):**

s is the witness. Hypotheses of (M3): x_k ∉ C, x_k ∈ ↓\*c ∩ Pl(C \ {c}).

- s ∈ ↓\*c ∩ Pl(C \ {c}): s ∈ D \ {c} (since s < c), which equals ↓\*c ∩ Pl(C \ {c}). ✓
- s ∉ C: s < c (so s ≠ c), and s ‖ all d ∈ C \ {c} (so s ≠ d). ✓

Conclusion of (M3): (C \ {c}) ∪ {s} is not a cover. But W ∨ s = 1 and 0_X ∉ (C \ {c}) ∪ {s}, so it IS a cover. Contradiction with (M3). ✓

**Case 2 → (M2):**

z, u are the witnesses. Hypotheses of (M2): x_{k₁}, x_{k₂} ∉ C, x_{k₁} ‖ x_{k₂}, x_{k₁}, x_{k₂} ∈ ↓\*c ∩ Pl(C \ {c}).

- z ∉ C, u ∉ C: verified in Target 4. ✓
- z ‖ u: verified in Target 5. ✓
- z ∈ ↓\*c ∩ Pl(C \ {c}): z ∈ D \ {c}. ✓
- u ∈ ↓\*c ∩ Pl(C \ {c}): u ∈ K ⊆ ↓\*c ∩ Pl(C \ {c}). ✓

Conclusion of (M2): (C \ {c}) ∪ {z, u} is not a cover. But W ∨ z ∨ u = W ∨ c = ⊗C = 1 and 0_X ∉ the set, so it IS a cover. Contradiction with (M2). ✓

**All hypotheses checked. No missing conditions.** ✓

---

## 2. Search for counterexample to the Proposition 3.5 statement

Tested on:

**M₃ = {0, a, b, c, 1}** (diamond, three atoms): C = {a, b} is minimal. M1+M2+M3 hold (M2, M3 vacuously — no qualifying replacements exist below a or b that are also incomparable to the other). ✓

**N₅ = {0, a, b, c, 1}** with 0 < a < b < 1, 0 < c < 1, c ‖ a, c ‖ b: C = {a, c} is minimal. M1+M2+M3 hold (M3 vacuously — ↓\*a ∩ Pl({c}) = {a} but a ∈ C, and ↓\*c ∩ Pl({a}) = {c} but c ∈ C). ✓ C = {b, c} is NOT minimal ({a, c} refines it). M3 correctly fails: a ∈ ↓\*b ∩ Pl({c}), a ∉ C, and {a, c} is a cover. ✓

**Two parallel chains {0, a, c, b, d, 1}:** Checked similarly. Statement consistent.

**No counterexample found.**

---

## 3. Verification of corrected Theorem 3.7

The corrected conditions are:

**(MC1')** C \ {x_{j_i}} does not satisfy cover condition. ↔ (M1) via Prop 3.4. ✓

**(MC2')** Uses "3 ∈ r_{k₁}(A) − r_{j_i}(A)" and "3 ∈ r_{k₂}(A) − r_{j_i}(A)" (subtraction).

Translation via Prop 3.1(2): x_{k₁} < x_{j_i} and x_{k₂} < x_{j_i}. ✓

Combined with incomparability conditions (x_{k₁} ‖ x_{k₂}, x_{k_q} ‖ x_{j_l} for l ≠ i), and that k₁, k₂ ∉ {j₁,...,jₘ}:

These conditions select exactly the pairs qualifying under (M2). The 0_X edge case (k = 1) is automatically excluded because 0_X < x_{j_l} for all l, so "1 ∈ r₁ + r_{j_l}" fails — 0_X is comparable to everything, never incomparable.

The conclusion "does not satisfy cover condition" ↔ "is not a cover" by Prop 3.4 (the replacement set is an antichain, verified: all pairwise incomparabilities are explicit in the hypothesis). ✓

**(MC3')** Uses "3 ∈ r_k(A) − r_{j_i}(A)" (subtraction). Same analysis: selects x_k < x_{j_i}, 0_X excluded by incomparability conditions. Conclusion faithful via Prop 3.4. ✓

**Edge case analysis — is the 0_X exclusion airtight?**

(M2)/(M3) require x_k ∈ ↓\*x_{j_i} = {x : x ≤ x_{j_i}} \ {0_X}. The MC' conditions test x_k < x_{j_i} (via subtraction) and x_k ‖ x_{j_l} for all l ≠ i (via addition).

If x_k = 0_X: the subtraction test passes (0_X < x_{j_i} for j_i > 1). But "1 ∈ r_k + r_{j_l}" requires 0_X ‖ x_{j_l}. Since 0_X ≤ x_{j_l} (0_X is below everything), they are comparable, so the incomparability test fails.

Verification: (r_1 + r_{j_l})_p for various p.
- p = 1: a_{1,1} + a_{j_l,1} = 1 + (-2) = -1
- p = j_l: a_{1,j_l} + a_{j_l,j_l} = 2 + 1 = 3
- p ∉ {1, j_l}: a_{1,p} + a_{j_l,p} ∈ {2+2, 2+(-2), 2+0} = {4, 0, 2}

No entry equals 1. So "1 ∈ r_1 + r_{j_l}" is FALSE. The 0_X case is correctly excluded. ✓

**No remaining interface errors after the directional fix.**

---

## 4. Summary

| Component | Verdict |
|-----------|---------|
| Join-closure of D | Sound |
| R \ K ≤ W | Sound |
| s = ⊗K ∈ D | Sound |
| z ∈ D \ {c}, z ≠ 0_X | Sound |
| z ‖ u | Sound |
| All M2/M3 hypotheses satisfied | Sound |
| Prop 3.5 statement | No counterexample found in M₃, N₅, two-chain lattices |
| Corrected Thm 3.7 (MC1'+MC2'+MC3') | Faithful translation of M1+M2+M3 |

**Fable's repair survives the structural audit.** The key innovations — the join-closed region D and the case split on s = ⊗K — are both clean. The proof avoids the original's unjustified comparability inference by never needing to infer comparability: instead it constructs witnesses (s in Case 1, z and u in Case 2) that are guaranteed to lie in D by join-closure, and derives contradictions from the M2/M3 hypotheses directly.

**The corrected Theorem 3.7 is a faithful representation-level translation of M1–M3.** The directional fix (subtraction instead of addition) correctly encodes x_k < x_{j_i}. The 0_X edge case is handled by the incomparability conditions, which correctly exclude 0_X since it's comparable to everything. No additional interface errors remain.

---

*Audit by Isotopy, 2026-08-21. Adversarial attack on Fable's repair, per Rheon's collaborative verification protocol.*
