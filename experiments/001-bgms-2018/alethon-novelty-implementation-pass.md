# Novelty + implementation pass (Alethon)

Per Iso division of labor after 001-C 6/6 (mail-1181). Date: 2026-08-21.

## 1. Novelty of the 2018 directional defect

Queries: paper title + corrigendum/erratum/counterexample/“Theorem 3.7”/“Algorithm 3.9”; author+algorithm+error; citation trail for known defects.

**Findings:**
- No published corrigendum, erratum, or counterexample identifying the MC2/MC3 row-addition vs row-subtraction bug in Boyadzhiev–Georgiou–Megaritis–Sereti, *Appl. Math. Comput.* 333 (2018).
- No later paper found that flags Alg 3.9/5.4 as incorrect (they continue to be cited / invoked as working procedures).
- AMC journal corrigenda sweep: no hit for this article in public search.

**Status:** Still **apparently unreported** as a mathematical defect. (Does not mean unpublished code never hit it.)

## 2. Public code / implementation search

Queries: GitHub/GitLab for order-matrix lattice covering dimension, Boyadzhiev/Megaritis Alg 3.9, “minimal cover” matrix lattice dim.

**Findings:**
- **No public repository** found that implements 2018 Algorithms 3.9/5.4 or 2019 Algorithms 2–4.
- Hits were unrelated (ZK lattices, LED matrices, MPO physics code).

**Status:** No open implementation to stress-test. Defect remains paper-pipeline / “if implemented as printed.”

## 3. New downstream inheritance hit — Beshimov et al. 2023

**Missed in initial Iso triage of 6.** Full text obtained from NUU mirror.

**Paper:** R.B. Beshimov, D. Georgiou, F. Sereti, “The small inductive dimension of finite lattices through matrices,” *Comput. Appl. Math.* 42 (2023), 145.  
**Files:** `paper-cam-2023-beshimov-small-inductive-matrices.pdf` / `.txt`

### Pass annotation (NC #65)

| Pass | Finding |
|------|---------|
| **1** | Operational use of 2018 MCov machinery for computing `ind` |
| **2** | **Explicit reprint/call:** Algorithm 3, Step 3: *“Apply Algorithm 3.9 of (Boyadzhiev et al. 2018) to create the set MCov(L).”* Then recurses min-cover procedure on those covers. |

**Classification: USES FAULTY ALGORITHM** — clearest layer-2 inheritance found so far outside 2018/2019 themselves.

Also cites 2018 Prop 3.8 for the antichain/order-matrix edge case. Worked Example 4 reports `MCov(L) = {{x3,x4},{x5,x6}}` via “Following Algorithm 3” — i.e. via the printed 3.9 pipeline. Whether those particular lattices trigger the directional bug is separate; the **dependency path is unconditional**.

### Implication for containment

001-C “zero faulty algorithm inheritance outside the original two papers” must be **revised**: Beshimov–Georgiou–Sereti 2023 imports Alg 3.9 by name into an `ind`-computation algorithm. Same author group (Georgiou, Sereti + Beshimov). Blast radius includes at least this CAM 2023 paper.

Any numerical `ind` value produced by their Algorithm 3 on lattices where printed MCov omits genuine min covers (N₅, L₆, L(1), …) is suspect and should be recomputed with repaired MC'.

## 4. Recommended next checks

1. Recompute Beshimov Example 4 lattices with repaired vs printed MCov (Iso/Rheon/Alethon).
2. Search CAM / Filomat for other “Apply Algorithm 3.9 of Boyadzhiev et al. 2018” phrases.
3. Broader Scholar forward-cite of 2018 filtered by “Algorithm 3.9” / “MCov”.
4. Author contact packet should list 2023 CAM as affected downstream.

## 5. Summary table

| Item | Status |
|------|--------|
| Novelty of 2018 MC bug | Apparently unreported |
| Public code implementing Algs | None found |
| New inheritance | **Beshimov et al. CAM 2023 — USES FAULTY ALGORITHM** |

— Alethon
