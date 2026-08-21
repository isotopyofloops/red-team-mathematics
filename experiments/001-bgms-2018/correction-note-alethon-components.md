# Correction-note components (Alethon)

**Source_rev:** Boyadzhiev–Georgiou–Megaritis–Sereti, *Appl. Math. Comput.* 333 (2018) 276–285, **as printed** (DOI 10.1016/j.amc.2018.03.041).  
**Pass:** drafting for private technical note (NC #65 version pin).  
**Audit-date:** 2026-08-21.

Sam contacts authors/editors after technical freeze; 10–14 day courtesy window; then centaurXiv. No public release before that.

---

## 1. Certificate block

### Certificate A — N₅ falsifies Theorem 3.7 (characterization)

**Lattice N₅** (5 elements): `0 < a < t < 1`, `0 < b < 1`, with `a ∥ b`, `t ∥ b`.

**Ground truth (Defs 2.1, 2.4):** Unique minimal cover `C = {a,b}`.  
(`a ∨ b = 1`; only refinements of `C` are `C` itself.)

**Printed Theorem 3.7:** When checking (MC3) for drop of `a`, take `k = t`:
- `3 ∈ r_a(A) + r_t(A)` holds because `a < t` (sum detects comparability, not direction);
- `t ∥ b`, so Pl-conditions hold;
- `{t,b}` is a cover.

Hence (MC3) fails ⇒ printed theorem declares `C` non-minimal ⇒ **`C ∈ MCov` but `C ∉ M(X)`**.

**Set-theoretic Prop 3.5:** candidates for (M3) must lie in `↓*a ∩ Pl({b})`; nothing nonzero strictly below `a` qualifies ⇒ (M3) holds ⇒ `C` correctly minimal.

Canonical writeup: `fable-certificate-A-N5.md` (repo). Same lattice as Alethon/Fable/Rheon independent discovery.

### Certificate B — `{0}⊕N₅` falsifies Algorithms 3.9 / 5.4 (and 2019 Alg 4)

**Lattice L₆** (6 elements): `0 < e < a < t < 1`, `e < b < 1`, `b ∥ a`, `b ∥ t`.

**Ground truth:** Unique Def 2.4 minimal cover `{a,b}`, `a ∧ b = e ≠ 0` ⇒ `ord = 1` ⇒ **`dim(L₆) = 1`**.  
All nonzero elements dense ⇒ **`dim_q(L₆) = 1`** (2019 Prop 1).

**Printed pipeline:** (MC3) rejects `{a,b}` via `k = t` (same directional bug). Alg 3.9 omits the cover; under every executable reading of the singleton/`∅` edge case, Alg 5.4 prints **`dim = 0`**. 2019 Alg 4 likewise prints **`dim_q = 0`**.

Canonical writeup: `fable-certificate-B-0-plus-N5.md` (includes ∅-underspecification case-split). Also `alethon-certificates-n5-l6.md`, `alethon-2019-adversarial-audit.md`.

**Minimality of 6 for numerical Alg 4 failure:** L₅ = `{0,e,a,b,1}` has `dim_q = 1` but printed Alg 4 returns 1 (no above-element trap). No ≤5-element Alg 4 numerical cex found.

---

## 2. Repaired MC′ statement

**Anchor:** Prop 3.1(2) as printed: `x_a < x_b ⟺ 3 ∈ r_a(A) − r_b(A)`.

Replace the directional tests in Theorem 3.7 / Algorithm 3.9 (and 2019 Algorithm 2 Step 8) as follows.

### (MC1′) — unchanged in substance
`C \ {x_{j_i}}` does not satisfy the cover condition.  
*(Convention: the empty set does not satisfy the cover condition — state explicitly; Def 3.3 leaves `∅` undefined.)*

### (MC2′)
For every pair `k₁, k₂ ∉ {j₁,…,j_m}` such that
- `1 ∈ r_{k₁}(A) + r_{k₂}(A)`       (`x_{k₁} ∥ x_{k₂}`)
- `3 ∈ r_{k₁}(A) − r_{j_i}(A)`       (**`x_{k₁} < x_{j_i}`** — was sum)
- `3 ∈ r_{k₂}(A) − r_{j_i}(A)`       (**`x_{k₂} < x_{j_i}`** — was sum)
- `1 ∈ r_{k_q}(A) + r_{j_l}(A)` for all `l ≠ i`, `q ∈ {1,2}`  (`Pl`)

the set `(C \ {x_{j_i}}) ∪ {x_{k₁}, x_{k₂}}` does **not** satisfy the cover condition.

### (MC3′)
For every `k ∉ {j₁,…,j_m}` such that
- `3 ∈ r_k(A) − r_{j_i}(A)`       (**`x_k < x_{j_i}`** — was `3 ∈ r_{j_i} + r_k`)
- `1 ∈ r_k(A) + r_{j_l}(A)` for all `l ≠ i`

the set `(C \ {x_{j_i}}) ∪ {x_k}` does **not** satisfy the cover condition.

**Equivalence (assuming Prop 3.5 statement + Props 3.1, 3.4):**  
`C` minimal ⟺ (M1)–(M3) ⟺ (MC1′)–(MC3′).

**Verified on:** N₅, L₆, L(1), B₂, B₃, M₃, chains, attack lattices (`lattice_check.py`); Fable Prop 3.5 repair hostile review passed.

---

## 3. Beshimov CAM 2023 — inheritance and example contamination

**Paper:** Beshimov–Georgiou–Sereti, *Comput. Appl. Math.* 42 (2023) 145.  
**source_rev of dependency:** BGMS 2018-as-printed.  
**Pass 2:** Algorithm 3 Step 3 explicitly: *“Apply Algorithm 3.9 of (Boyadzhiev et al. 2018) to create the set MCov(L).”* → **USES FAULTY ALGORITHM** (pipeline contaminated regardless of examples).

### Example 4(1) — Fig. 3 (7 elements)

Order matrix as printed does **not** define a lattice: `x₃, x₄` have two minimal upper bounds `x₅, x₆` (no lub). Claimed `MCov = {{x₃,x₄},{x₅,x₆}}` is inconsistent with lub-semantics (`{x₃,x₄}` is not a cover). Under the printed matrix, the only Def-style min cover among claimed sets is `{x₅,x₆}`, which both printed MC and MC′ accept.

**Verdict:** Matrix/typesetting or “lattice” claim is dubious; **directional bug not cleanly demonstrated** on this example. Pipeline still cites 3.9.

### Example 4(2) — Fig. 4 (8 elements) — **contaminated**

Order matrix defines a lattice.  

| Cover | Def 2.4 minimal? | Printed MC (Thm 3.7) | MC′ |
|-------|------------------|----------------------|-----|
| `{x₃, x₇}` | **yes** | **rejects** (MC3 fires on `k = x₄`: `x₃ < x₄`, `x₄ ∥ x₇`, `{x₄,x₇}` cover) | **accepts** |
| `{x₅, x₆}` | **yes** | accepts | accepts |
| `{x₅, x₇}`, `{x₆, x₇}` | no | rejects | rejects |

**True MCov = `{{x₃,x₇},{x₅,x₆}}`.**

Paper reports (via “Following Algorithm 3”):  
`MCov(M) = {{x₃,x₇},{x₅,x₆},{x₅,x₇},{x₆,x₇}}` and **`ind(M) = 2`**, with the value 2 driven by the `{x₃,x₇}` branch (`d₁,₁ = 1`).

**Internal inconsistency:** Printed Algorithm 3.9 **must reject** `{x₃,x₇}` (directional bug). So either:
- the listed MCov was taken from definitions / by hand while labeled as Alg 3 output, or
- the printed pipeline was not what produced the table.

**Numerical consequence if Alg 3.9 is run as printed:** `{x₃,x₇}` omitted; remaining contributing covers give `d = 0` on the paper’s own arithmetic for `{x₅,x₆}` ⇒ **`ind` would print 1, not 2**.  
**If MC′ / Def MCov is used:** `{x₃,x₇}` kept ⇒ **`ind = 2`** (matches their reported number, not their claimed algorithm).

**Summary for the note**

| Item | Status |
|------|--------|
| Beshimov Alg 3 pipeline | Contaminated (calls 2018 Alg 3.9 by name) |
| Ex 4(1) numerical | Unclear / matrix not a lattice as printed; bug not isolated |
| Ex 4(2) `ind = 2` | **Inconsistent with printed 3.9**; consistent with repaired/Def MCov. Reported value happens to match the *correct* dimension, not the printed algorithm’s output |
| Future implementations of Beshimov Alg 3 | Will inherit underestimation on lattices where the directional trap fires (e.g. L₆-type) |

**Correction-note recommendation:** List Beshimov 2023 as downstream affected; recommend replacing Step 3’s call with MC′-corrected minimal-cover computation; flag Ex 4(2) as internally inconsistent with printed 3.9.

---

## 4. Files already in repo to cite

- `fable-certificate-A-N5.md`, `fable-certificate-B-0-plus-N5.md`
- `alethon-certificates-n5-l6.md`, `alethon-2019-adversarial-audit.md`
- `alethon-novelty-implementation-pass.md` (Beshimov inheritance discovery)
- `paper-cam-2023-beshimov-small-inductive-matrices.pdf`

— Alethon
