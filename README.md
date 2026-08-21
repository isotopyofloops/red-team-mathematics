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

**Target:** DGMM (2023), Theorem 3.4 (covering dimension of ordinal sums).  
**Result:** Known defect recovered by 3 independent agents. All 3 produced valid certificates. Calibration passed — the protocol detects real errors.

### Experiment 001 — BGMS (2018)

**Target:** Beran, Georgiou, Megaritis, Sergioli. "A study of a covering dimension of finite lattices." *Applied Mathematics and Computation* 333 (2018) 276–285.  
**Status:** Blind phase complete. Collaborative verification in progress.  
**Finding:** Theorem 3.7 uses row addition (symmetric, tests comparability) where the lattice condition requires row subtraction (asymmetric, tests directed order). 4/4 independent auditors converged on the same defect. Downstream propagation confirmed to Algorithm 5.4.

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
  000-calibration/          # Experiment 000 (DGMM 2023)
  001-bgms-2018/            # Experiment 001 (BGMS 2018)
    isotopy-structural-audit.md
    isotopy-fable-repair-audit.md
```

## License

CC BY 4.0
