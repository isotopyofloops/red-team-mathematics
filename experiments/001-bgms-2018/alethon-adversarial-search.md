# Experiment 001 — Alethon adversarial search (STOP POINT)

**Role:** Algebraic / adversarial search (Alethon).

Blind-phase report as delivered at STOP.

Paper: Boyadzhiev–Georgiou–Megaritis–Sereti, *A study of a covering dimension of finite lattices*, Appl. Math. Comput. 333 (2018). Paper only; no web. Possible training familiarity with this group’s lattice-dimension papers (incl. Exp 000); certificate below recomputed from this paper’s definitions.

## Targets
Theorem 3.7, Algorithm 3.9, Theorem 5.2, Algorithm 5.4 vs underlying Defs 2.1–2.4.

## Minimal certificate

**Lattice L** (7 elements) — same order type as Fig. 1 / L(1) in the 2015 DGMM paper, which *is* a lattice:

```
0 ≤ x ≤ x₁ ≤ y₂ ≤ 1
0 ≤ x ≤ x₂ ≤ y₁ ≤ 1
```
with x₁ ≰ y₁, x₂ ≰ y₂ (antichain pairs as in Fig. 1 of Exp 000 / Remark 3.5 of DGMM).

**Ground truth (Defs 2.1–2.4):**
- Unique Def 2.4 minimal cover: C = {x₁, x₂}
- ord(C) = 1 (meet = x ≠ 0; cannot take 3 elements)
- Therefore dim(L) = 1

**Theorem 3.7 matrix conditions reject C:**
When checking (MC3) for drop of x₁, the matrix test fires on k = y₂:
- `3 ∈ r_{x₁}(A) + r_{y₂}(A)` holds because x₁ < y₂ gives entry 2+1=3 in the sum
- and the Pl-type conditions hold
- enlarged set {x₂, y₂} is a cover

So (MC3) fails and Theorem 3.7 / Algorithm 3.9 declare C non-minimal.

Set-theoretically (Prop 3.5): y₂ ∉ ↓*x₁ (y₂ ≰ x₁), candidate set empty, (MC3) vacuously OK — C correctly minimal.

**Root cause:** Prop 3.1(2) encodes strict order by **subtraction**: `x_a < x_b ⇔ 3 ∈ r_a(A) − r_b(A)`.
Theorem 3.7 (MC2)/(MC3) uses **addition**: `3 ∈ r_{j_i}(A) + r_k(A)`, which is true for both x_k < x_{j_i} and x_{j_i} < x_k. The matrix test cannot tell “below” from “above.”

**Algorithm consequence:**
- Algorithm 3.9 (Step 8 uses Thm 3.7) misses {x₁,x₂}; returns no minimal cover of order 1
- Algorithm 5.4 / Theorem 5.2 then output **dim(L) = 0**
- Disagrees with Def 2.3–2.4: **true dim = 1**

Same false rejection on N5 and on the lattice `{0,e,a,b,c,1}` with e < a, e < b, e ∥ c (minimal cover {c,e} missed).

## Classification
| Claim | Status |
|-------|--------|
| Prop 3.5 (set-theoretic MC1–3) | Appears OK on tested lattices (not fully proved here) |
| **Theorem 3.7** (matrix MC) | **False** — disagrees with Def 2.4 on L |
| **Algorithm 3.9** | **False** — misses minimal covers |
| **Theorem 5.2** | **False** as stated — uses M(X) from 3.7 |
| **Algorithm 5.4** | **False** — reports dim=0 on L where dim=1 |

Not merely exposition: the characterization and algorithms disagree with the paper’s own definitions on an explicit 7-element lattice.

## Finite certificate (short)
Lattice L(1) as above. Def 2.4 min cover {x₁,x₂}, dim=1.
Thm 3.7 rejects it via `3 ∈ r_{x₁}+r_{y₂}` (fires on x₁ < y₂).
Alg 5.4 → dim=0 ≠ 1.

## Repair (separate section — after STOP)

Replace every `3 ∈ r_{j_i}(A) + r_k(A)` in Theorem 3.7 / Algorithm 3.9 with the Prop 3.1(2) form that forces k below j_i, e.g. `3 ∈ r_k(A) − r_{j_i}(A)` (and similarly for MC2’s two indices). Re-verify on L(1), N5, Boolean algebras, Fig. 5–6 examples.

— Alethon
