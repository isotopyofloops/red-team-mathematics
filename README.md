# Red-Team Mathematics

Systematic adversarial audits of published mathematical results by AI agents and humans, with independent verification.

## Method

Red-Team Mathematics is a structured protocol for stress-testing published proofs:

- **Role separation:** Multiple auditors attack a paper from distinct methodological angles (structural/dependency, algebraic, computational, proof-gap). Convergence on the same defect from independent lanes is stronger evidence than any single audit.
- **Blind phase:** Auditors work independently without sharing findings. No access to external criticism or errata.
- **Certificate requirement:** Concrete finite witnesses that can be independently verified. Claims without certificates are conjectures, not findings.
- **Collaborative phase:** After blind convergence, auditors cross-verify certificates, attack proposed repairs, and trace downstream consequences.
- **Repair verification:** Proposed fixes are subjected to the same adversarial treatment as the original paper.

## Experiments

### Experiment 000 — Calibration

**Target:** DGMM (2015), Theorem 3.4 (existence of finite lattices of each covering dimension).  
**Result:** Known defect recovered by 3 independent agents. All 3 produced valid certificates. Calibration passed — the protocol detects real errors.

### Experiment 001 — BGMS (2018)

**Primary target:** Boyadzhiev, Georgiou, Megaritis, Sereti. "A study of a covering dimension of finite lattices." *Applied Mathematics and Computation* 333 (2018) 276–285.  
**Downstream target:** Boyadzhiev, Georgiou, Megaritis, Sereti. "A study of the quasi covering dimension of finite lattices." *Computational and Applied Mathematics* 38 (2019), Article 109.  
**Status:** Blind phase complete. Collaborative verification in progress.  
**Finding:** Theorem 3.7 uses row addition (symmetric, tests comparability) where the lattice condition requires row subtraction (asymmetric, tests directed order). 4/4 independent auditors converged on the same defect. The error propagates to Algorithms 3.9 and 5.4 in the 2018 paper and to Algorithms 2–4 in the 2019 downstream paper, producing incorrect covering-dimension and quasi-covering-dimension values.

## Auditors

| Role | Agent | Architecture |
|------|-------|-------------|
| Structural/dependency audit | Isotopy | Claude (autonomous) |
| Algebraic verification | Alethon | Grok (autonomous) |
| Proof-gap analysis + counterexamples | Claude Fable | Claude Fable 5 |
| Protocol design + computational verification | Rheon | ChatGPT (Sam's) |

## Steward

Samantha White (ssrpw2@gmail.com)

## Repository Structure

```
experiments/
  000-calibration/          # Experiment 000 (DGMM 2015)
    alethon-theorem-3.4-audit.md
  001-bgms-2018/            # Experiment 001 (BGMS 2018 + 2019 downstream)
    result-ledger.md            # Claim-by-claim status for both papers
    isotopy-structural-audit.md # Structural/dependency audit (Isotopy)
    isotopy-fable-repair-audit.md # Adversarial audit of Fable's Prop 3.5 repair
    alethon-adversarial-search.md # Adversarial theorem search (Alethon)
    alethon-certificates-n5-l6.md # N5 and L6 certificates (Alethon)
    alethon-collab-review.md    # Collaborative review (Alethon)
    2019-blast-radius.md        # Downstream propagation to 2019 paper
    verify_certificates.py      # Independent finite checker (Rheon, Python)
    lattice_check.py            # Lattice verification (Alethon)
```

## License

CC BY 4.0
