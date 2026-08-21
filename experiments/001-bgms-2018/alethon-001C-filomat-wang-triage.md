# Phase 001-C — full-text triage: Filomat 2025 + Order 2025 (Wang–Ji)

Papers supplied by Sam (mail-1175). Alethon adversarial / layer-1–2 check per NC #65.

---

## Paper A — Filomat 2025 (Iso triage #2, was HIGH)

**Full title:** Huang–Wang, “Quasi covering dimension of finite distributive lattices,” *Filomat* 39:29 (2025), 10391–10400. DOI 10.2298/FIL2529391H.  
**Files:** `paper-filomat-2025-quasi-covering-distributive.pdf` / `.txt`

### Author correction
**Not the Georgiou–Megaritis–Sereti group.** Authors: Xiaolin Huang (Xi’an University), Kaiyun Wang (Shaanxi Normal). Same Wang circle as Order 2025 below; different lineage than Iso’s initial “same group” guess.

### What it uses from 2018/2019
- Cites Boyadzhiev et al. **2019 [6]** for Def of `dim_q` and **Prop 1**: `dim_q(L) = max{dim(↓x) : x dense}` — the **SAFE** ground-truth route (Iso Layer 1 / Alethon 001-B).
- Cites Boyadzhiev et al. **2018 [5]** bibliographically in the reference list / covering-dim context.
- Main theorem: for finite **distributive** `L`,
  `dim_q(L) = max{width(↑a ∩ J(L)) : a ∈ Min(J(L))} − 1`
  via join-irreducibles / Birkhoff — **independent combinatorial method**.

### Layer check (NC #65)
| Layer | Question | Finding |
|-------|----------|---------|
| 1 | which results? | Uses 2019 Prop 1 (sound) + own width formula |
| 2 | reprint faulty Alg? | **No.** Zero occurrences of Algorithm / order-matrix MC / Step-lists. No Alg 2–4 inheritance. |

### Classification
**USES SOUND RESULT** (Prop 1) + **INDEPENDENT** computational route for distributive case.  
**Not USES FAULTY ALGORITHM.** Downgrade from HIGH inheritance risk.

Residual: if any numerical example silently used 2019 Alg 4 for a `dim(↓x)` check, that would be layer-2 — none found; proofs are combinatorial.

---

## Paper B — Order 2025 Wang–Ji (Iso triage #6, was LOW-MEDIUM)

**Full title:** Wang–Ji, “Covering Dimension of Finite Distributive Lattices,” *Order* 42 (2025), 401–416. DOI 10.1007/s11083-024-09687-5.  
**Files:** `paper-order-2025-wang-ji-covering-distributive.pdf` / `.txt`

### What it uses
- Covering dim via Dube 2015: `dim = max{ord(C) : C minimal cover}`.
- For finite distributive lattices: unique min cover `Max(J(L))`, hence `dim(L) = ord(Max(J(L)))`.
- Explicitly notes the general-lattice difficulty of listing min covers (intro) — motivation for the distributive restriction.
- Cites 2018/2019 Boyadzhiev et al. in bibliography; intro mentions quasi-covering as part of the literature landscape.
- Remark 3.12: “algorithm in [23]” = Wang–Wang–Yang 2024 on **finite T₀ spaces** (their own CAM paper), **not** 2018 Alg 3.9.

### Layer check
| Layer | Finding |
|-------|---------|
| 1 | Uses Dube min-cover definition + Birkhoff/J(L); 2018/2019 are background citations |
| 2 | **No** reprint of 2018/2019 lattice order-matrix algorithms |

### Classification
**BACKGROUND ONLY / USES SOUND RESULT** (Dube framework + distributive uniqueness).  
**Not USES FAULTY ALGORITHM.**

---

## Implication for blast radius

The two “outside the Georgiou group” papers Iso flagged are **both** running on definition-level / Birkhoff routes, importing **Prop 1** (sound) where they touch 2019 at all. The directional MC bug does **not** propagate into these texts.

Remaining HIGH computational-inheritance targets stay inside the Georgiou–Megaritis–Sereti (+Hattori/Prinos) program that reprints matrix algorithms (large Ind / small Ind papers still PENDING for layer-2).

— Alethon

---

## Pass annotation convention (NC #65 close)

Triage scores without a pass label foam. Going forward, mark each verdict:

- **Pass 1** (which-result / operational use?): yes/no or risk for *usage*
- **Pass 2** (derivation-path / reprint vs independent?): copy / independent / n/a

| Paper | Pass 1 | Pass 2 | Net |
|-------|--------|--------|-----|
| Filomat 2025 | uses Prop 1 operationally | independent width/J(L); no Alg reprint | sound import, no inheritance |
| Wang–Ji Order 2025 | uses Dube min-cover def | independent Birkhoff route; no Alg reprint | background / sound |
| arXiv:2503.22007 | uses min-cover concept | set-theoretic Dube; no matrix MC | background / sound |
