# Experiment 001-B — 2019 Downstream Blast-Radius Audit

Target: D. Boyadzhiev, D. Georgiou, A. Megaritis, F. Sereti, **“A study of the quasi covering dimension of finite lattices,”** *Computational and Applied Mathematics* 38 (2019), Article 109, DOI 10.1007/s40314-019-0885-6.

This document tracks only the propagation of the 2018 minimal-cover matrix defect into the 2019 quasi-covering-dimension paper. “Not implicated” does **not** mean “fully verified.”

## 1. Dependency structure

The 2019 paper first develops quasi-covering dimension independently and proves

`dim_q(X) = max{dim(↓x) : x is dense in X}`

(Proposition 1).

Section 6 then explicitly imports the 2018 covering-dimension computation:

`2018 Theorem 3.7 (false as printed)`

→ `2018 Algorithm 3.9`

→ reprinted as `2019 Algorithm 2`

→ used by `2019 Algorithm 3` to compute `dim(↓x)`

→ used by `2019 Proposition 9`

→ called inside `2019 Algorithm 4`

→ claimed computation of `dim_q(X)`.

The inherited defect is therefore operational, not merely bibliographic.

## 2. Exact inherited defect

The correct lattice-theoretic condition requires a candidate `x_k` satisfying

`x_k < x_{j_i}`.

The 2018 order-matrix dictionary encodes this by

`3 ∈ r_k(A) - r_{j_i}(A)`.

But the 2019 reprint of Algorithm 2 retains the erroneous symmetric row-sum test

`3 ∈ r_{j_i}(A) + r_k(A)`

in Step 8 (and the analogous pair of tests in MC2).

Thus an element above the removed cover member can be admitted as a supposed replacement witness. Genuine minimal covers can be discarded.

## 3. Six-element downstream certificate

Let

`L6 = {0,e,a,b,t,1}`

with order

`0 < e < a < t < 1`,

`e < b < 1`,

and `b ∥ a,t`.

This is `{0} ⊕ N5`.

### 3.1 Ground truth for covering dimension

From Definition 2.3 of the 2018 paper (equivalently the covering-dimension definition repeated in 2019):

`dim(L6)=1`.

A complete independent certificate is in `certificate-B-0-plus-N5.md`.

### 3.2 Dense elements

`e` is the least nonzero element of `L6`. Therefore for any nonzero `x,y`,

`x ∧ y ≥ e > 0`.

So every nonzero element is dense:

`D(L6) = {e,a,b,t,1}`.

The proper principal downsets are chains:

- `↓e = {0,e}`;
- `↓a = {0,e,a}`;
- `↓b = {0,e,b}`;
- `↓t = {0,e,a,t}`.

Hence each has covering dimension `0`.

The top downset is

`↓1 = L6`,

so

`dim(↓1)=1`.

### 3.3 True quasi-covering dimension

By the 2019 paper's Proposition 1,

`dim_q(L6) = max{dim(↓x) : x dense}`

`= max{0,0,0,0,1}`

`= 1`.

This route does not use the faulty 2018 minimal-cover algorithm.

### 3.4 Published Algorithm 4 output

Algorithm 4 applies Algorithm 3 to each dense-element downset.

- On each proper chain, Algorithm 3 returns `0` (correctly).
- On `↓1 = L6`, Algorithm 3 inherits the faulty minimal-cover computation and returns `0` instead of `1`.

Therefore Algorithm 4 takes

`max{0,0,0,0,0}=0`.

Thus

`dim_q(L6)=1`

but

`Algorithm 4(L6)=0`.

This is a concrete downstream numerical failure in the 2019 paper.

## 4. Claim-by-claim inherited-error triage

| 2019 item | Dependency on faulty 2018 minimal-cover translation | Current status |
|---|---|---|
| Definition 6–7 | none | not implicated |
| Proposition 1 | direct proof from definitions | not implicated; useful as ground truth |
| Remark 1 | via Proposition 1 / definitions | not implicated by 2018 bug |
| Proposition 2 | uses Proposition 1 plus a covering-dimension claim for a constructed downset | not directly implicated; audit separately |
| Proposition 3 | Proposition 1 | not implicated by 2018 bug |
| Lemma 1 | direct finite refinement argument | not implicated by 2018 bug |
| Proposition 4 / Corollary 1 / Proposition 5 | quasi-minimal-cover theory | not implicated by 2018 bug |
| Lemmas 2–3 / Proposition 6 | Proposition 1 + product results | not implicated by 2018 bug |
| Remarks 4–7 | numerical examples / structural claims | audit separately |
| Proposition 7 / Algorithm 1 | incidence-matrix dense-element test | separate machinery; not implicated by 2018 bug |
| Definition 14 / Proposition 8 | imported 2018 cover-condition machinery | current audit says sound |
| Algorithm 2 | direct reprint of faulty 2018 minimal-cover algorithm | **false as printed** |
| Algorithm 3 | depends on Algorithm 2 | **false as printed** |
| Proposition 9(1) | uses `M(↓x)` and cites 2018 Theorem 5.2 proof | **not valid as printed** |
| Proposition 9(2) | depends on part (1) | **not valid as printed** |
| Algorithm 4 | calls Algorithm 3 for each dense downset | **false as printed**; L6 certificate |
| Example 4(1),(2) | computed using Algorithms 1–3 | values may be right by accident; recompute independently |

## 5. Repair plan

### Algorithm 2

Replace directional row sums in Step 8 by correctly oriented difference tests:

`3 ∈ r_k(A) - r_{j_i}(A)`.

Likewise for both replacement elements in MC2.

### Algorithm 3

Use the corrected Algorithm 2 / corrected minimal-cover set. The order-computation machinery can remain if Theorem 4.2 is retained.

### Proposition 9

Define the matrix-selected family using the corrected characterization, or state the formula directly over `MCov(↓x)` and then substitute the corrected matrix characterization.

A clean repaired statement is:

For every dense `x`,

`dim(↓x) = max{ord(C) : C ∈ MCov(↓x)}`,

with `ord(C)` computed by the surviving incidence-matrix formula. Then

`dim_q(X) = max{dim(↓x) : x dense}`

by Proposition 1.

### Algorithm 4

Keep the dense-element enumeration, but call the corrected covering-dimension routine on every `↓x`.

## 6. Next audit questions

1. Recompute Examples 4(1) and 4(2) directly from definitions and compare to the printed values.
2. Audit whether any earlier numerical examples (Remarks 4–7 / Proposition 2 construction) rely on values obtained only through the faulty 2018 procedure.
3. Search later citing papers for explicit use of Proposition 9 or Algorithms 2–4.
4. Search for software/code that implemented the 2018/2019 algorithms; inspect whether implementers silently corrected the row operation.
5. If the repair remains stable, add a formal proof or mechanized verification of the corrected minimal-cover characterization.

