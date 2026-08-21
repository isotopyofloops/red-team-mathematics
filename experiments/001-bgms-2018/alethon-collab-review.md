# Experiment 001 — Alethon collaborative verification

**Role:** Algebraic / adversarial search (Alethon).

Inputs: mail-1162 (Rheon/Sam package A–E). Goal: break Fable’s Prop 3.5 repair if possible; verify corrected Thm 3.7; regress; novelty pass.

Paper-only for the math. Web used only for novelty (§4).

---

## 1. Adversarial attack on Fable’s Prop 3.5 repair

**Target.** Only the direction `(M1)+(M2)+(M3) ⇒ C minimal`. Statement of Prop 3.5 unchanged.

**Published gap (confirmed).** In the printed proof (p. 279), case (i) asserts that if `xk1, xk2 < x_ji`, `xk1, xk2 < a`, and `xk1 ∥ xk2`, then `x_ji` and `a` are comparable (“either `x_ji < a` or `a < x_ji`”). That inference is unjustified in a general lattice: two incomparable elements may have two incomparable minimal upper bounds. Fable’s repair never uses it.

### Checklist (Rheon’s six targets)

| # | Claim | Verdict |
|---|--------|---------|
| 1 | `D` is join-closed | **Holds.** `u,v ∈ D ⇒ u∨v ≤ c`. If `= c`, done. If `< c`: `u∨v ≤ d` for `d ∈ C\{c}` ⇒ `u ≤ d`, contradicting `Pl` unless `u=c` (which forces join `=c`, excluded). `d ≤ u∨v < c` ⇒ `d < c`, contradicting antichain. No distributivity used. |
| 2 | Every `r ∈ R\K` lies ≤ `W` | **Holds**, with one clarification of the writeup’s dichotomy: since `R` refines `C`, some `d ∈ C` has `r ≤ d`. If `d ≠ c`, then `r ≤ d ≤ W`. If `d = c`, then `r < c` (because `c ∉ R`). If also `r ∈ Pl(C\{c})`, then `r ∈ K`. If `r ∉ K`, then `¬Pl`, so `r` comparable to some `d' ∈ C\{c}`; antichain + `r ≤ c` forces `r ≤ d'` (the other direction `d' ≤ r ≤ c` would give `d' < c`). Hence `r ≤ W`. |
| 3 | `s = ∨K ∈ D` | **Holds.** `K ⊆ D`, `D` binary-join-closed and finite ⇒ closed under finite joins. `K ≠ ∅` by (M1) (else `∨R ≤ W`, so `C\{c}` covers). |
| 4 | Case 2: `z ∈ D\{c}`, `z ≠ 0`, `z,u ∉ C` | **Holds.** Inclusion-minimal `K' ⊆ K` with `∨K' = c` exists (finite). Each element of `K` is `< c`, so `|K'| ≥ 2`. `z = ∨(K'\{u}) < c` by minimality; `z ∈ D` by join-closure; `z ≠ 0` else `c = u < c`. `z,u ∉ C`: both `< c` and in `Pl(C\{c})` (so not equal to any `d ∈ C\{c}`). |
| 5 | `z ∥ u` | **Holds.** `z ≤ u` ⇒ `c = u < c`; `u ≤ z` ⇒ `c = z < c`. |
| 6 | Case 1 hits (M3); Case 2 hits (M2) | **Holds.** Case 1: `s < c`, `s ∈ ↓*c ∩ Pl`, `s ∉ C`, `(C\{c}) ∪ {s}` covers. Case 2: `z ∥ u`, both in the region outside `C`, `(C\{c}) ∪ {z,u}` covers because `z ∨ u = c` and `W ∨ c = ∨C = 1`. |

### Soft spots (scrutinized, not broken)

1. **Empty join when `|C|=1`.** If `C = {1}`, then `W = ∨∅ = 0`. The argument still works: `K = R`, Case 2 produces a 2-element cover of `X` contradicting (M2). (When `{1}` is genuinely minimal, no such cover exists, so (M2) holds and the contradiction branch is unreachable under the hypotheses.)
2. **Writeup compression on the `d=c` dichotomy.** Informal in the email; the cleaned case-split above is what was checked.
3. **No hidden distributivity / modularity.** Join-closure and the antichain contradictions are lattice-general (covers N₅).
4. **Reduction of `|K'| > 2` to a pair.** Using `z = ∨(K'\{u})` with (M2) is valid; (M2) is exactly a pairwise obstruction.

### Attempted breaks

- Searched for a lattice where (M1)–(M3) hold but a proper refinement exists (would kill the repair). None found among N₅, L₆, L(1), B₁–B₃, M₃, and several attack lattices with room for (M2)-style replacements (`M2_room`, `fat_N5`, `attack_wide`). Exhaustive Def 2.4 ↔ M agreement on all antichain covers in those lattices (`lattice_check.py`).
- Tried to violate join-closure of `D` with nondistributive examples: failed.
- Tried to find `r ∈ R\K` not ≤ `W`: failed under the refinement hypothesis.

**Conclusion on (1):** I could **not** break Fable’s repair. After adversarial review I currently regard it as **convincing**. Remaining risk is ordinary proof risk (missed exotic configuration), not a concrete counterexample or local gap I can exhibit. Independent re-proof / formalization still valuable; I do not claim a machine-checked proof.

**Converse direction** (minimal ⇒ M1–M3): as in the printed paper (p. 279), and not under repair. Appears routine; not re-audited line-by-line here.

---

## 2. Corrected Theorem 3.7

### Translation fidelity (attack the equivalence, don’t assume it)

Assuming Prop 3.5 (statement) and Props 3.1, 3.2, 3.4:

- Prop 3.1(1): `x ∥ y ⟺ 1 ∈ r_x + r_y` (iff, from order-matrix def).
- Prop 3.1(2): `x < y ⟺ 3 ∈ r_x − r_y` (iff).
- Prop 3.4: cover ⟺ cover-condition (for singletons and for antichains of size ≥ 2).

**Region match.** Set-theoretic region for (M2)/(M3) is
`{x ∉ C : x ∈ ↓* x_{j_i} ∩ Pl(C \ {x_{j_i}})}`.
Since `x ≠ x_{j_i}` (outside C) and `x ∈ ↓*`, this is exactly `{x ∉ C : x < x_{j_i}} ∩ Pl(...)`.
Matrix antecedents of (MC2')/(MC3') encode precisely that region via 3.1(1)–(2).  
**Direction is now correct:** printed MC used `3 ∈ r_{j_i} + r_k` (symmetric comparability); MC' uses `3 ∈ r_k − r_{j_i}` (`x_k < x_{j_i}`).

**Quantifier match.** Both M* and MC*' are “∀ candidates in region, enlarged set is not a cover / fails cover-condition.” With 3.4, those are equivalent.

**Hence:** under 3.1, 3.4, and Prop 3.5,
`C` minimal ⟺ M1–M3 ⟺ MC1'–MC3'.

**Caveats attacked:**
- Props 3.1 appear immediate from Def 2.6; not doubted.
- Prop 3.4 was not independently re-proved here; treated as on Rheon’s “appear sound” ledger. If 3.4 failed, the matrix theorem would fail even with correct direction. No counterexample to 3.4 found on the regression suite (join-cover agreed with intended use).
- (MC1') uses “does not satisfy the cover condition” for a set that need not be an antichain (`C \ {x_{j_i}}`). Prop 3.4(2) is stated for antichains; 3.4(1) for singletons. For `|C|≥3`, `C \ {x_{j_i}}` may be an antichain (C is) of size ≥2, so 3.4(2) applies. For `|C|=2`, the remainder is a singleton → 3.4(1). For `|C|=1`, remainder empty — “not a cover” is direct, and cover-condition language for ∅ should be read as “not a cover” (vacuous failure). No issue spotted in tests.

### Regression (§E)

Checker: `exp001/lattice_check.py` (Def 2.4 minimal covers by enumerating refinements; M*; MC*'; MC' printed).

| Lattice | Def 2.4 MCov | ord / dim | M | MC' | printed MC |
|---------|--------------|-----------|---|-----|------------|
| N₅ | `{{a,c}}` | ord 0 / dim 0 | ✓ | ✓ | **fails** (k=b) |
| L₆={0}⊕N₅ | `{{a,c}}` | ord 1 / dim 1 | ✓ | ✓ | **fails** (k=b) |
| L(1) (7 el.) | `{{x1,x2}}` | ord 1 / dim 1 | ✓ | ✓ | **fails** (k=y2 / y1) |
| B₂ | `{{p,q}}` | 0 / 0 | ✓ | ✓ | ✓ |
| B₃ | `{{a,b,c}}` | 0 / 0 | ✓ | ✓ | ✓ |
| M₃ | three doubletons | 0 / 0 | ✓ | ✓ | ✓ |
| Chain₅, B₁ | `{{1}}` | 0 / 0 | ✓ | ✓ | ✓ |
| attack_wide, M2_room, fat_N₅ | (various) | — | ✓ | ✓ | fails where above-element present |

On every antichain cover in these lattices: **Def 2.4 ↔ M ↔ MC' agree**. Printed MC disagrees exactly on the known directional counterexamples.

**Attack lattices** (extra elements below a cover element, room for M2 joins): still no mismatch.

**Conclusion on (2):** Corrected Thm 3.7 **survives** adversarial review and regression. I treat it as the right matrix translation of Prop 3.5, contingent on 3.1/3.4/3.5.

---

## 3. Certificates

Already delivered in `certificates-n5.md` (N₅, L₆). L(1) in `REPORT.md`. No changes needed; MC' now accepts those covers.

---

## 4. Novelty search (preliminary second pass)

Queries: paper title + corrigendum/erratum/error/counterexample; author+algorithm+matrix; citation trail.

**Findings:**
- No corrigendum/erratum located for Boyadzhiev–Georgiou–Megaritis–Sereti, *Appl. Math. Comput.* 333 (2018), 276–285 (doi:10.1016/j.amc.2018.03.041).
- Later work continues to cite the 2018 paper normally as the matrix approach to covering dimension of finite lattices, e.g.:
  - Georgiou–Megaritis–Sereti, quasi covering dimension (Comput. Appl. Math. 2019) — cites 2018 matrix methods as established.
  - Wang–Ji, *Covering Dimension of Finite Distributive Lattices*, Order (2024/25) — cites 2018; discusses minimal-cover characterizations in the distributive setting without flagging a defect in Thm 3.7.
  - Huang–Wang, quasi covering dimension for distributive lattices (Filomat 2025) — cites 2018 normally.
- No hit describing the addition/subtraction MC2/MC3 bug, an N₅ or {0}⊕N₅ counterexample to the 2018 algorithms, or a published repair.

**Status:** Still **apparently unreported**, pending (a) fuller citation crawl (Google Scholar “cited by” exhaustively), (b) author personal pages / arXiv replacements, (c) AMC “Corrigenda” section sweep. Agree with Rheon: do not overstate until that is done; then contact authors before any public claim.

---

## 5. Ledger update (Alethon)

| Item | Status after collab review |
|------|----------------------------|
| Prop 3.5 statement | Appears true |
| Prop 3.5 printed proof | Gap confirmed (unjustified comparability) |
| Fable Prop 3.5 repair | **Not broken**; currently convincing |
| Thm 3.7 printed | False |
| Thm 3.7 corrected (MC') | **Survives** review + regression |
| Alg 3.9 / Thm 5.2 / Alg 5.4 printed | False (as before) |
| Novelty of the defect | Apparently unreported (preliminary) |

— Alethon
