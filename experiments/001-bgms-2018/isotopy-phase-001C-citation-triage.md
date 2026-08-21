# Phase 001-C — Citation Blast-Radius Triage

**Isotopy, Phase 001-C assignment: collect and classify papers citing the 2018/2019 papers.**

Initial triage based on web search (2026-08-21). Full-text audit of each paper is required before any status is final.

---

## Classification scheme

- **BACKGROUND ONLY**: cites the 2018/2019 paper for context, definitions, or motivation; does not use any algorithm or theorem that descends from the faulty machinery
- **USES SOUND RESULT**: cites a result that has survived current audit (e.g., Prop 1, Prop 7/Alg 1, cover condition)
- **USES FAULTY ALGORITHM**: cites or reimplements Algorithm 3.9/5.4 (2018) or Algorithms 2-4 (2019) — the affected chain
- **UNCLEAR/NEEDS FULL TEXT**: cannot determine dependency from title/abstract alone
- **INDEPENDENT**: different methodology; citation is comparative, not operational

---

## Papers by the same author group

These carry the highest risk. The same researchers who wrote the 2018/2019 papers continued the research program.

### 1. Small inductive dimension (Order, 2024)

**Full title:** "A Study of the Small Inductive Dimension in the Area of Finite Lattices"
**Authors:** D. N. Georgiou, A. C. Megaritis, G. Prinos, F. Sereti
**Journal:** Order 41(2):437-461, 2024
**DOI:** 10.1007/s11083-023-09638-6

**Risk level:** MEDIUM
**Rationale:** The small inductive dimension (ind) is defined independently of the covering dimension. However, the paper likely compares ind with dim and dim_q, and may use the faulty algorithms for computational examples. Need full text to determine whether any claims depend on Algorithm 3.9/5.4 outputs.

**Status:** PENDING — need full text

### 2. Quasi covering dimension of finite distributive lattices (Filomat, 2025)

**Full title:** "Quasi covering dimension of finite distributive lattices"
**Authors:** Xiaolin Huang, Kaiyun Wang (Xi'an University / Shaanxi Normal — NOT the Georgiou group)
**Journal:** Filomat 39:29 (2025), 10391–10400. DOI: 10.2298/FIL2529391H

**Risk level:** ~~HIGH~~ → **USES SOUND RESULT / INDEPENDENT**
**Rationale:** Uses 2019 Prop 1 (sound ground-truth route) + independent width/J(L) formula via Birkhoff for distributive case. Zero occurrences of Algorithm/order-matrix MC/Step-lists. No Alg 2-4 inheritance.

**Alethon full-text audit (2026-08-21, `alethon-001C-filomat-wang-triage.md`):** Layer 1: uses Prop 1 (sound). Layer 2: no algorithm reprint. Cleared.

**Status:** CLEARED — uses sound result + independent computational route

### 3. Finite lattices and large inductive dimension (AGT, 2026)

**Full title:** "Finite lattices and large inductive dimension"
**Authors:** D. N. Georgiou, Y. Hattori, A. C. Megaritis, F. Sereti
**Journal:** Applied General Topology 27(1), April 2026

**Risk level:** HIGH
**Rationale:** Introduces large inductive dimension (Ind) for finite lattices "based on minimal covers." If the minimal-cover computation uses the 2018/2019 algorithms, any computational results are affected. The definition of Ind itself may be independent, but the matrix characterization and algorithms likely inherit.

**Status:** PENDING — need full text

### 4. The realm of finite lattices in combination with a new dimension (arXiv, 2025)

**Full title:** "The realm of finite lattices in combination with a new dimension"
**Authors:** D. N. Georgiou, Y. Hattori, A. C. Megaritis, F. Sereti
**arXiv:** 2503.22007 (March 2025)

**Risk level:** ~~HIGH~~ → **BACKGROUND ONLY**
**Rationale:** Likely a preprint version of paper #3 above, or a companion paper. Abstract mentions "minimal covers" and relations with covering dimension.

**Alethon spot-check (2026-08-21, `alethon-001C-arxiv-2503.22007-triage.md`):** Full text fetched. Defines Ind via definition-level minimal covers (Dube 2015 sense), NOT via the faulty matrix algorithm. No reprint of Algorithms 3.9/5.4 or order-matrix MC conditions found. Citation of 2018 is bibliographic, not operational. Follow-up: no dim_q anywhere in the paper; covering dim examples use hand-listed covers from Dube 2015 definition. The directional bug path does not fire. Residual risk is ordinary hand-enumeration error, not the systematic defect.

**Status:** CLEARED — background citation only. Remaining check: identity with AGT 2026 published version.

### 5. A study of a new dimension for finite lattices (Georgiou, 2019)

**Full title:** "A study of a new dimension for finite lattices" (cited in 2019 paper references as Georgiou et al., accepted for publication, Topol. Appl.)
**Authors:** D. Georgiou, I. Kougias, A. Megaritis, A. Prinos, G. Sereti, F. (2019)

**Risk level:** MEDIUM
**Rationale:** Listed in the 2019 paper's bibliography as "(accepted for publication)." May be the small inductive dimension paper or a precursor.

**Status:** PENDING — need to identify and locate

---

## Papers by other authors

### 6. Covering Dimension of Finite Distributive Lattices (Order, 2025)

**Full title:** "Covering Dimension of Finite Distributive Lattices"
**Authors:** K. Wang, C. Ji
**Journal:** Order 42(2):401-416, 2025
**DOI:** 10.1007/s11083-024-09687-5

**Risk level:** ~~LOW-MEDIUM~~ → **BACKGROUND ONLY / USES SOUND RESULT**
**Rationale:** Uses Dube 2015 min-cover definition + Birkhoff/J(L) for distributive uniqueness. Cites 2018/2019 in bibliography as literature context. Remark 3.12 references "algorithm in [23]" = Wang–Wang–Yang 2024 on finite T₀ spaces, NOT 2018 Alg 3.9.

**Alethon full-text audit (2026-08-21, `alethon-001C-filomat-wang-triage.md`):** Layer 1: background citation + Dube framework. Layer 2: no reprint of 2018/2019 algorithms. Cleared.

**Status:** CLEARED — background citation + independent Birkhoff route

---

## Pre-2018 papers (cited BY the target, not citing it)

These are upstream references and are NOT part of the blast radius:

- Dube et al. (2015), "A study of covering dimension for the class of finite lattices" — defines the covering-dimension framework the 2018 paper builds on
- Dube et al. (2017), "Studying the Krull dimension of finite lattices under the prism of matrices" — same group, matrix methods for Krull dimension
- Georgiou et al. (2016), "A study of the order dimension of a poset through the matrix theory" — order dimension via matrices

---

## Summary

| # | Paper | Year | Authors | Risk | Status |
|---|-------|------|---------|------|--------|
| 1 | Small inductive dimension (Order) | 2024 | Same group + Prinos | MEDIUM | PENDING |
| 2 | Quasi covering dim, distributive (Filomat) | 2025 | Huang, Wang | ~~HIGH~~ SOUND/INDEP | CLEARED (Alethon) |
| 3 | Large inductive dimension (AGT) | 2026 | Same group + Hattori | HIGH | PENDING |
| 4 | Realm of finite lattices (arXiv) | 2025 | Same group + Hattori | ~~HIGH~~ BACKGROUND | CLEARED (Alethon) |
| 5 | New dimension, Topol. Appl. | 2019 | Same group | MEDIUM | PENDING (locate) |
| 6 | Covering dim, distributive (Order) | 2025 | Wang, Ji | ~~LOW-MED~~ BACKGROUND | CLEARED (Alethon) |

**Key observation (updated 2026-08-21):** Of 6 downstream papers, 3 are now CLEARED (arXiv:2503.22007, Filomat 2025 Huang–Wang, Order 2025 Wang–Ji) — all use definition-level minimal covers or Prop 1 (sound) with independent computational routes. The blast radius has narrowed to the Georgiou–Megaritis–Sereti core group papers that may reprint matrix algorithms: small inductive dimension (Order 2024) and large inductive dimension (AGT 2026, published version). Papers outside the Georgiou group independently developed Birkhoff/J(L) routes that bypass the faulty algorithm entirely.

**Next steps:**
1. Obtain full texts of papers #2, #3, #4 (highest risk)
2. For each: trace whether dim/dim_q values are computed from definitions or from algorithms
3. For each: check whether worked examples would produce different values under the corrected algorithm
4. Identify any papers outside this group that cite the 2018/2019 papers (broader search needed)
