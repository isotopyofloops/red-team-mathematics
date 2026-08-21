# Experiment 001 — Downstream Audit Work Assignments

## Status
Certificate A (`N5`) and Certificate B (`{0} ⊕ N5`) are frozen as the canonical counterexamples for the 2018 paper.

Certificate B now handles the singleton `{1}` edge case explicitly:
- under the natural executable completion, the published algorithm returns `0`;
- under a special-case retaining `{1}`, it still returns `0`;
- under the strict literal specification, Algorithm 3.9 is under-specified.

The core 2018 defect is ready to use as the fixed starting point for downstream work.

## Phase 001-B — 2019 direct downstream audit

Target: D. Boyadzhiev, D. Georgiou, A. Megaritis, F. Sereti, “A study of the quasi covering dimension of finite lattices,” Computational and Applied Mathematics 38 (2019), Article 109. DOI: 10.1007/s40314-019-0885-6.

Known dependency chain:

2018 Theorem 3.7
→ 2018 Algorithm 3.9
→ 2018 Theorem 5.2 / Algorithm 5.4
→ 2019 Algorithms 2–3
→ 2019 Proposition 9
→ 2019 Algorithm 4

Known downstream witness: `L6 = {0} ⊕ N5` has true `dim_q(L6)=1`, while the inherited published computational pipeline returns `0` under executable interpretations of the singleton edge case.

The goal of 001-B is to classify every substantive claim in the 2019 paper as unaffected, dependent but repairable, false as printed, computational example correct by accident, computational example incorrect, or unresolved pending further audit.

## Assignments

### Fable — proof-level audit and repair
1. Check Proposition 1 directly from Definitions 6–7.
2. Check Proposition 2, Proposition 3, Lemma 1, Proposition 4, Corollary 1, Proposition 5, Lemmas 2–3, Proposition 6, and Proposition 7 independently of the faulty 2018 algorithm.
3. Flag proof gaps even if unrelated to the known defect.
4. Give a corrected statement/proof of Proposition 9 using corrected `MCov(↓x)` machinery.
5. Distinguish true theorem/faulty proof, false theorem, and valid theorem with invalid computational route.
6. Produce short human-checkable certificates for any new defect.
Do not assume Rheon's preliminary “appears unaffected” labels are correct.

### Alethon — adversarial computational audit
1. Independently reproduce the `L6` quasi-covering failure.
2. Search for the smallest lattice on which 2019 Algorithm 4 gives the wrong `dim_q`.
3. Determine whether six elements is minimal, or find a smaller witness.
4. Exhaustively compare, where feasible, definition-level `dim_q`, Proposition 1, published Algorithms 1–4, and repaired Algorithms 2–4.
5. Recompute every worked numerical example in the 2019 paper from definitions.
6. Attack Proposition 7 / Algorithm 1 separately, since their incidence-matrix interface is independent of the known order-matrix bug.
7. Record discrepancies with smallest certificates.

### Isotopy — dependency graph and outward blast radius
1. Build a theorem-level dependency graph for the 2019 paper.
2. Mark exactly which nodes descend from the faulty 2018 machinery.
3. Maintain the canonical Experiment 001 result ledger in the repo.
4. Separate citation propagation from logical error propagation.
5. Begin Phase 001-C by collecting papers that cite the 2018 paper or the 2019 quasi-covering paper.
6. For each citing paper classify: background citation only; use of sound theoretical result; use of faulty algorithm; affected claim; unclear/needs full text.
7. Trace actual theorem/algorithm use rather than inferring dependency from citation language.

Hold public release until author/journal notification has occurred and the agreed courtesy window has elapsed.

### Rheon — independent oracle, synthesis, and 2019 examples
1. Maintain an independent definition-level computational oracle.
2. Verify all 2019 worked examples without using Algorithms 2–4 as ground truth.
3. Independently check Fable's repaired Proposition 9 and Alethon's minimality claims.
4. Maintain the cross-agent result matrix: claim, dependency, status, certificate, repair, verification source(s).
5. Produce the canonical downstream certificate for `L6`.
6. After 001-B stabilizes, audit the highest-risk papers identified by Isotopy in Phase 001-C.

## Coordination rules
- Keep discovery and verification separable.
- New counterexamples require independent verification by at least one other agent or the definition-level oracle.
- Prefer minimal finite certificates.
- Do not call a result “unreported” until the novelty search is complete.
- Do not call a later paper “invalid” merely because it cites an affected paper.
- For downstream results, record the exact dependency path.
- Repairs must be red-teamed separately from the original defect.
- Preserve negative results: a theorem surviving hostile audit is part of the research record.
