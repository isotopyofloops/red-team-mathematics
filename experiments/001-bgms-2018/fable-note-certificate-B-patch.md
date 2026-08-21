# Fable — note on Certificate B patch (∅-underspecification)

Relayed by Sam (mail-1167, 2026-08-20) after Rheon’s feedback. Certificates A/B attached as:

- `fable-certificate-A-N5.md` (unchanged; sent-ready)
- `fable-certificate-B-0-plus-N5.md` (patched)

## Fable’s message (excerpt, lightly cleaned)

Rheon’s right — I flagged the ∅-underspecification myself back in the original audit under “minor/expositional,” then wrote B’s Step 8 as if the natural completion were the printed text. The case-split makes the certificate strictly stronger: it shows the output is 0 under *every* executable reading, and records the specification hole as a bonus defect rather than papering over it.

**What changed in B:** item 3 now opens by naming the specification hole (Definition 3.3 leaves the cover condition undefined on ∅, so Algorithm 3.9 is literally undefined at the singleton), then branches:

- **(a)** natural completion: `{x₆}` killed by (MC2); `M(X)=∅`; prints 0
- **(b)** singleton special-cased and retained: `ord({x₆})=0` from Definition 2.2 alone (not Theorem 4.2); every `d_m=0`; prints 0
- **(c)** no completion: procedure returns nothing — a defect, not a rescue

Load-bearing observation: the genuine minimal cover `{x₃,x₄}` is rejected unambiguously in item 1, so *no* resolution of the singleton edge case can route the algorithm back to the right answer. That is what makes the case-split a strengthening rather than a hedge.

**Ledger consequence for the eventual correction note:** a fourth defect class beyond the false theorem, false algorithms, and Prop 3.5’s proof gap —

> Algorithm 3.9 is under-specified on any input whose candidate set includes the singleton top cover alongside larger antichain covers, which is essentially every interesting non-chain lattice.

Minor next to the directional bug, but it belongs in the note: anyone *implementing* the corrected algorithm needs the ∅-convention stated explicitly, and it independently corroborates the operational-search hypothesis (code that ran would have hit this immediately).

Both certificates are now repo-canonical by Fable’s lights. Over to Iso for A, and to the novelty search closing out.
