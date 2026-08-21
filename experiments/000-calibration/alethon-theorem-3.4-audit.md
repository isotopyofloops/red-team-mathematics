# Experiment 000 — Alethon adversarial audit of Theorem 3.4

**Role:** Algebraic / adversarial search (Alethon).

Red-team of Theorem 3.4 (DGMM / Discrete Mathematics 338 (2015)), paper-only, no web.

Recognition note: I may have seen “covering dimension of a lattice / Dube et al.” in training data; I did not use remembered corrigenda. The failure below was recomputed from the paper’s definitions and construction.

## Theorem 3.4
For any k ∈ ℕ₀ there is a finite lattice L(k) with dim(L(k)) = k.

## Construction (k > 0)
L = {x, x₁,…,x_{k+1}, y₁,…,y_{k+1}, 0, 1} with
(1) 0 ≤ x ≤ x_i ∀i
(2) x_i ≤ y_j ∀j ≠ i
(3) y_i ≤ 1 ∀i
R = {x₁,…,x_{k+1}}; claim ∨R=1, ∧R=x≠0, ord(R)=k, R refines every cover, hence dim(L)=k.

## Smallest failure certificate: k = 3

For k=3 the stated relations do **not** define a lattice.

Pair x₁, x₂: upper bounds in L are {y₃, y₄, 1}.
Minimal upper bounds: y₃ and y₄ (incomparable; neither ≤ the other).
Hence x₁ ∨ x₂ does not exist in L.

Explicit check:
- y₃ ≥ x₁ (by (2), 3≠1) and y₃ ≥ x₂ (3≠2)
- y₄ ≥ x₁ and y₄ ≥ x₂ similarly
- y₃ ≰ y₄, y₄ ≰ y₃
- no other element is a common upper bound below 1

So the proof’s “consider the finite lattice L = …” is false for k≥3: the poset is not a lattice.

## Boundary check
| k | lattice? | computed dim (when lattice) |
|---|----------|------------------------------|
| 0 | yes ({0,1}) | 0 |
| 1 | yes | 1 (matches claim) |
| 2 | yes (x₁∨x₂=y₃ unique) | 2 (matches claim) |
| 3 | **NO** | — |
| 4+ | **NO** (same: ≥2 y’s outside {i,j}) | — |

Pattern: x_i ∨ x_j has unique lub iff there is exactly one index m ∉ {i,j}, i.e. k+1=3 ⇒ k=2. For k≥3 there are ≥2 such indices ⇒ ≥2 minimal upper bounds.

Fig. 1 only draws L(1), L(2) — consistent with the only k>0 cases where the construction is a lattice.

## What this breaks
- The **construction/proof** of Theorem 3.4 for all k≥3.
- Not yet a counterexample to the *existence claim* (some other finite lattice might still realize each dim k). Per instructions I have not tried to repair.

## Finite certificate (short)
**k=3, elements x₁,x₂: two minimal upper bounds y₃,y₄ ⇒ not a lattice.**

— Alethon (blind phase)
