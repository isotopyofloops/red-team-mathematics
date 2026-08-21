# Experiment 001-B — Alethon adversarial computational audit (2019)

**Paper:** Boyadzhiev–Georgiou–Megaritis–Sereti, *A study of the quasi covering dimension of finite lattices*, Comput. Appl. Math. 38 (2019), Art. 109.  
**Role:** Algebraic / adversarial computational audit (Alethon), per `rheon-exp001-work-assignments.md`.  
**Scope:** Reproduce `L6` `dim_q` failure; minimality of the witness; Prop 7 / Alg 1; worked examples; compare definition-level `dim_q` vs published / repaired pipelines.

Paper PDF/text in this directory. Checker: `lattice_check.py` (+ checks below). Independent of Rheon’s oracle.

---

## 1. Definitions used

From the 2019 paper:

- **Dense** (Def 6): `x` dense iff `x ∧ y ≠ 0` for every `y ≠ 0`.
- **`dim_q`** (Def 7) / **Prop 1:** `dim_q(X) = max{ dim(↓x) : x dense in X }` (ground truth via Prop 1 + Def 2.3 covering dimension on downsets).
- **Alg 1 / Prop 7:** incidence-matrix test for dense elements.
- **Alg 2–3:** reprint of 2018 Alg 3.9 / 5.4 (printed MC2/MC3 use row **addition**).
- **Alg 4:** dense set via Alg 1; then Alg 3 on each `↓x`; print max.

Repaired Alg 2–3 = same with MC' (row **subtraction**), as in Exp 001 collab review.

---

## 2. Reproduce `L6` quasi-covering failure

**Lattice** `L6 = {0} ⊕ N₅` (6 elements):

```
0 < e < a < t < 1
    e < b < 1
```

with `b ∥ a`, `b ∥ t`.

| Quantity | Value | Source |
|----------|-------|--------|
| Dense elements | `{e,a,b,t,1}` (all nonzero; `e` least nonzero) | Def 6 |
| `dim(↓x)` for proper chain downsets | 0 | Def 2.3 |
| `dim(↓1) = dim(L6)` | **1** | unique Def 2.4 min cover `{a,b}`, `a∧b=e≠0`, `ord=1` |
| **`dim_q(L6)`** | **1** | Prop 1 |
| Printed Alg 3 on `↓1` | **0** | rejects `{a,b}` via MC3 with `k=t` (`a < t`, `t ∥ b`); singleton edge → 0 under every executable reading (Fable Cert B) |
| **Printed Alg 4** | **0** | max of zeros |
| Repaired Alg 3 / 4 (MC') | **1** | MC' accepts `{a,b}` |

**Certificate path:** 2018 Thm 3.7 → Alg 3.9 → Alg 5.4 → 2019 Alg 2–3 → Prop 9 → Alg 4.  
Exact numerical failure: `dim_q_definition(L6) = 1 ≠ 0 = Alg4(L6)`.

Matches `2019-blast-radius.md` / result ledger; independently recomputed here.

---

## 3. Is six elements minimal for Alg 4 numerical failure?

**Claim:** Among lattices checked, **`L6` (6 el.) is the smallest on which printed Alg 4 returns the wrong `dim_q`.** No ≤5-element witness found.

### Evidence

| Lattice | \|X\| | `dim_q` | Alg 4 (printed) | Mismatch? |
|---------|------|---------|-----------------|-----------|
| Chain₄ | 4 | 0 | 0 | no |
| B₂ | 4 | 0 | 0 | no |
| N₅ | 5 | 0 | 0 | no |
| M₃ | 5 | 0 | 0 | no |
| **L₅** = `{0,e,a,b,1}` (`0<e<a,b<1`, `a∥b`) | 5 | **1** | **1** | **no** |
| **L₆** | 6 | **1** | **0** | **yes** |
| L(1) | 7 | 1 | 0 | yes |

**Why L₅ does not fail:** unique min cover `{a,b}` with `ord=1`. Nothing strictly above `a` (resp. `b`) that is incomparable to the other, so printed MC3’s above-element trap does not fire. Printed M keeps `{a,b}`; Alg 3/4 report 1.

**Why the bug needs ≥6 for this failure mode:**  
Numerical underestimation requires a genuine min cover of order ≥1 that printed MC rejects. Rejection via the directional bug needs an element **above** one cover member and **incomparable** to the other (the `t` above `a` with `t∥b` pattern). Together with bottom, a nonzero meet-point `e`, the two cover elements, the above-element, and top, that is six elements — exactly `L6`.

N₅ falsifies Thm 3.7 / Alg 2 as a *characterization* (Cert A) but has `dim_q=0` (only dense element is `1`), so Alg 4’s numerical output can still read 0 without exposing a `dim_q` mismatch.

**Status:** minimality of 6 for Alg 4 numerical failure — **survives current adversarial search**; no smaller counterexample found. (Open to Rheon oracle / Iso enumeration.)

---

## 4. Prop 7 / Algorithm 1 (incidence-matrix dense test)

**Statement:** `x_i` (i≥2) dense iff `max(c_i(T)+c_j(T)−B₁)=2` for every `j∈{2,…,n}\{i}`.

**Computational attack:** Def-6 dense set vs Prop 7 test on N₅, L₆, L(1), B₂, B₃, M₃, L₅, Fig 11 reconstruction — **exact agreement in all cases**.

**Proof skim (adversarial):** Forward direction standard. Converse: if not dense, some `q` with `x_i∧x_q=0`; the max=2 hypothesis would give nonzero `x_s≤x_i,x_q`, forcing `x_s≤0` and `x_s≠0` — contradiction. Writeup says `x_s < x_1`; the intended contradiction is impossibility below the bottom. **No counterexample; no local gap found that breaks the iff.** Independent of the 2018 order-matrix bug (uses incidence matrix only).

**Status:** SURVIVES CURRENT AUDIT (computational + proof skim). Not a formalization.

---

## 5. Worked numerical examples (recomputed from definitions)

### Example 3 (Fig 10) — Alg 1 only

Paper: dense = `{x5,x6,x7,x8}`; `x3` not dense.  
Incidence-matrix walkthrough in the paper is consistent with Prop 7. Not re-derived from an ASCII figure here beyond trusting the printed vectors; Prop 7 agreement on other lattices supports Alg 1 on this class of examples.

### Example 4(1) — Fig 11

Reconstructed order:

`x1 < x2 < x3 < x4 < x6`, `x3 < x5 < x6`, `x4 ∥ x5`.

| Check | Result |
|-------|--------|
| Dense (Def 6) | `{x2,x3,x4,x5,x6}` — matches paper |
| MCov / `dim` | `{{x4,x5}}`, `dim=1` — matches |
| Printed MC on `{x4,x5}` | **passes** (no above-element trap) |
| Paper Alg 4 output | `dim_q=1` |
| Definition `dim_q` | **1** |

**Classification:** computational example **correct** (bug does not fire on this lattice).

### Example 4(2) — Fig 12

Reconstructed as Boolean-like with least nonzero `x2` and three atoms / three coatoms / top (order type matching paper’s claimed M sets). Definition-level: `dim=2`, all nonzero dense, `dim_q=2`. Paper reports `dim_q=2` via Alg 4. Three-atom min cover has no “above one, ∥ others” trap of the L6 kind in the same way for the printed rejection pattern on the full top downset’s atom cover — paper’s pipeline returns 2.

**Classification:** computational example **correct** on the reconstructed order type (definition agrees with reported `dim_q=2`).

**Pattern:** 2019 worked examples that report positive `dim_q` via Algs 2–4 are lattices where the directional bug **does not reject** the high-order min covers. They do not stress-test the inherited defect. `L6` does.

---

## 6. Exhaustive comparison summary (tested suite)

| Lattice | `dim` | `dim_q` (Def/Prop1) | Alg3 printed | Alg4 printed | Alg3/4 repaired (MC') |
|---------|-------|---------------------|--------------|--------------|------------------------|
| N₅ | 0 | 0 | 0 | 0 | 0 |
| L₅ | 1 | 1 | 1 | 1 | 1 |
| L₆ | 1 | 1 | **0** | **0** | 1 |
| L(1) | 1 | 1 | **0** | **0** | 1 |
| B₂, M₃, chains | 0 | 0 | 0 | 0 | 0 |

Prop 1 used as bridge: `dim_q` from max of definition-level `dim(↓x)` over Def-6 dense set; dense set always matched Prop 7 on the suite.

---

## 7. Classification of 2019 claims (Alethon lane only)

| Claim | Status (Alethon) | Notes |
|-------|------------------|-------|
| Prop 1 | SURVIVES CURRENT AUDIT | Used as ground-truth bridge; proof not line-audited here (Fable’s lane) |
| Prop 7 / Alg 1 | SURVIVES CURRENT AUDIT | Def↔matrix agree on suite; proof skim OK |
| Alg 2 | FALSE AS PRINTED | Reprint of 2018 Alg 3.9 |
| Alg 3 | FALSE AS PRINTED | Reprint of 2018 Alg 5.4 |
| Prop 9 | NOT VALID AS PRINTED | Depends on false `M(↓x)` |
| Alg 4 | FALSE AS PRINTED | `L6`: 0≠1; 6-el minimal in current search |
| Ex 4(1)–(2) | CORRECT BY NON-TRIGGER | Definition agrees; bug inert on those covers |
| Props 2–6, Lemmas, products | UNRESOLVED HERE | Assigned to Fable / not computationally forced |

---

## 8. Smallest certificates (Alethon)

1. **`L6` Alg 4 failure** — §2 above (canonical with Fable Cert B for the dim side).  
2. **Minimality of 6** — L₅ counterexample-to-minimality-failure (§3): same dim_q=1 pattern without the above-element, Alg 4 correct.  
3. **Prop 7** — no cex; positive agreement table §4.

---

## 9. Coordination notes

- Discovery here is computational; Rheon oracle should verify L₅ non-failure and L₆ Alg 4 path.  
- Iso ledger: point Alg 4 / Prop 9 rows at `alethon-2019-adversarial-audit.md` + Fable Cert B.  
- Novelty / author contact: still pending (Rheon rules).

— Alethon
