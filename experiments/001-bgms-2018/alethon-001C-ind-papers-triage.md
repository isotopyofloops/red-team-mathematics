# Phase 001-C — triage: Order 2024 small Ind + AGT 2026 large Ind

Papers from Sam (mail-1179). Pass 1 / pass 2 annotated (NC #65).

**Files:**
- `paper-order-2024-small-inductive.pdf` / `.txt` — Georgiou–Megaritis–Prinos–Sereti, *Order* 41 (2024), 437–461. DOI 10.1007/s11083-023-09638-6
- `paper-agt-large-inductive.pdf` / `.txt` — Georgiou–Hattori–Megaritis–Sereti, *Appl. Gen. Topol.* 27 (2026), 24197. DOI 10.4995/agt.24197  
  (Published version of arXiv:2503.22007; agrees with prior spot-check.)

---

## Order 2024 — small inductive dimension

| Pass | Question | Finding |
|------|----------|---------|
| **1** | Operational use of min covers / 2018? | **Yes** — characterizes `ind` via minimal covers; cites Boyadzhiev 2018 for covering-dim context; compares `ind` with covering/Krull dim in examples |
| **2** | Reprint faulty Alg 3.9/5.4 / order-matrix MC? | **No** — min covers are Def 2.4 / Dube-style set-theoretic; proofs reason about refinements by hand; **no** Algorithm reprint, **no** order-matrix row-sum conditions |

**Net:** Pass 1 MEDIUM (Georgiou group + operational min covers + dim comparisons). Pass 2 **independent derivation path** → **BACKGROUND / USES SOUND RESULT** (min-cover definition). Not USES FAULTY ALGORITHM.

`dim` reference values in examples appear hand-listed via `max{ord(V)}` (Dube), same pattern as AGT/arXiv.

---

## AGT 2026 — large inductive dimension

| Pass | Question | Finding |
|------|----------|---------|
| **1** | Operational use? | **Yes** — Ind defined/studied via minimal covers; compares to covering dim; cites 2018 |
| **2** | Reprint faulty matrix Alg? | **No** — explicit Def: minimal cover iff `V ⊆ C` for every refinement (Dube); §4.3 covering dim via Dube formula; examples list covers by hand; **no** Alg 3.9/MC conditions. Matches arXiv:2503.22007 triage |

**Net:** Same as arXiv spot-check. Pass 1 looked HIGH; Pass 2 clears inheritance. **BACKGROUND / USES SOUND RESULT.**

---

## Blast-radius update (Alethon)

After Filomat, Wang–Ji, arXiv/AGT Ind, and Order 2024 small Ind:

| # | Paper | Pass 1 | Pass 2 | Net inheritance of directional bug |
|---|-------|--------|--------|-------------------------------------|
| Filomat 2025 Huang–Wang | uses Prop 1 | independent width/J(L) | **none** |
| Wang–Ji Order 2025 | Dube min cover | Birkhoff Max(J(L)) | **none** |
| arXiv/AGT Ind 2025–26 | uses min covers | set-theoretic Dube | **none** |
| Order 2024 small Ind | uses min covers | set-theoretic; hand dim | **none** |

**None of the currently full-texted downstream papers reprint the faulty 2018/2019 order-matrix algorithms.** Blast radius of the *computational* defect remains concentrated in papers that actually copy Alg 2–4 / 3.9–5.4. Definition-level “minimal cover” lineage is widespread and **sound**.

Still PENDING for layer-2 only if a future full text reprints the matrix MC conditions (none found tonight among Iso’s list that we have PDFs for). Medium “locate Topol. Appl. 2019” item remains unlocated.

— Alethon
