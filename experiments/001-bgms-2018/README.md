# Experiment 001 — BGMS (2018)

**Paper:** Boyadzhiev–Georgiou–Megaritis–Sereti, *Appl. Math. Comput.* 333 (2018) 276–285.  
**Status:** Blind phase complete; collaborative verification in progress.

## Alethon lane (algebraic / adversarial)

| File | Contents |
|------|----------|
| `alethon-adversarial-search.md` | Blind STOP report: Thm 3.7 / Alg 3.9 / Thm 5.2 / Alg 5.4 false on L(1) |
| `alethon-certificates-n5-l6.md` | Clean N₅ and {0}⊕N₅ certificates |
| `alethon-collab-review.md` | Adversarial review of Fable Prop 3.5 repair + corrected Thm 3.7; novelty pass |
| `lattice_check.py` | Finite-lattice checker (Def 2.4 ↔ M ↔ MC' / printed MC) |

## Isotopy lane

| File | Contents |
|------|----------|
| `isotopy-structural-audit.md` | Structural/dependency blind audit |
| `isotopy-fable-repair-audit.md` | Audit of Fable’s Prop 3.5 repair |

## Fable lane (proof-gap / counterexamples)

| File | Contents |
|------|----------|
| `fable-certificate-A-N5.md` | Canonical N₅ certificate falsifying Theorem 3.7 |
| `fable-certificate-B-0-plus-N5.md` | Canonical `{0}⊕N₅` certificate: Alg 5.4 → 0 under every executable singleton reading; ∅-underspecification case-split |
| `fable-note-certificate-B-patch.md` | Fable’s note on the B patch and fourth defect class |

## Shared

| File | Contents |
|------|----------|
| `result-ledger.md` | Cross-lane status ledger |
| `verify_certificates.py` | Independent certificate checker |
| `2019-blast-radius.md` | Downstream 2019 inheritance |

