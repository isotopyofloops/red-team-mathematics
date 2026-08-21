# Red-Team Mathematics — Experiment 001 Result Ledger

Status: collaborative verification in progress  
Primary target: Boyadzhiev, Georgiou, Megaritis, Sereti (2018), *A study of a covering dimension of finite lattices*, Applied Mathematics and Computation 333, 276–285.  
Downstream target: Boyadzhiev, Georgiou, Megaritis, Sereti (2019), *A study of the quasi covering dimension of finite lattices*, Computational and Applied Mathematics 38:109.

## Scope and status vocabulary

This ledger separates four questions that must not be conflated:

1. Is the printed proof valid?
2. Is the printed theorem/algorithm valid?
3. Is there a finite counterexample/certificate?
4. Is a proposed repair verified?

Status labels used below:

- **SURVIVES CURRENT AUDIT** — no defect found in the stated result under the checks performed; not a formal proof unless explicitly noted.
- **PROOF GAP** — the published proof contains an invalid or missing inference, while the statement currently appears true.
- **FALSE AS PRINTED** — an explicit finite certificate contradicts the stated theorem/algorithm.
- **INHERITED FAILURE** — a downstream claim uses the false 2018 machinery.
- **REPAIR CANDIDATE** — a corrected statement/proof has survived current adversarial checks but is not yet formally verified.
- **PENDING** — not yet audited sufficiently.

---

# I. 2018 paper

## Proposition 3.1 — order-matrix dictionary

**Status:** SURVIVES CURRENT AUDIT.

The paper correctly states:

- `1 ∈ r_a(A_X) + r_b(A_X)` iff `x_a ∥ x_b`;
- `3 ∈ r_a(A_X) - r_b(A_X)` iff `x_a < x_b`.

The second relation is directional and is the key to the defect below.

## Proposition 3.4 — matrix cover condition

**Status:** SURVIVES CURRENT AUDIT.

The matrix cover condition has agreed with direct join-based cover testing in the computational checks performed.

## Proposition 3.5 — lattice-theoretic characterization of minimal covers

**Status:** PROOF GAP; statement currently believed true.

The published proof of the `(M1)+(M2)+(M3) => minimal` direction contains an unjustified inference: from two incomparable elements lying below both `x_{j_i}` and another element `a`, it concludes that `x_{j_i}` and `a` are comparable.

### Repair candidate

Fable supplied a replacement proof based on join-closure of

`D = (↓*c ∩ Pl(C \ {c})) ∪ {c}`

and a minimal subfamily whose join is `c`. Alethon independently attacked the proposed proof at its load-bearing steps (join-closure, the `R\K ≤ W` reduction, the minimal-subfamily construction, `z ∥ u`, and the exact M2/M3 hypotheses) and did not find a counterexample.

**Repair status:** REPAIR CANDIDATE; hostile review passed, formalization still desirable.

## Theorem 3.7 — matrix characterization of minimal covers

**Status:** FALSE AS PRINTED.

### Root cause

Proposition 3.5 requires replacement candidates satisfying

`x_k < x_{j_i}`.

By Proposition 3.1(2), the faithful matrix translation is

`3 ∈ r_k(A_X) - r_{j_i}(A_X)`.

The printed conditions (MC2) and (MC3) instead use row addition:

`3 ∈ r_{j_i}(A_X) + r_k(A_X)`.

That sum test admits strict comparability in either direction, so elements **above** `x_{j_i}` can be treated as candidate refinements even though Proposition 3.5 requires elements strictly below it.

### Smallest current certificate

The five-element pentagon `N5` falsifies the `minimal => MC1–MC3` direction.

Canonical certificate: `fable-certificate-A-N5.md` (also `alethon-certificates-n5-l6.md`).

### Repair candidate

Replace each directional row-sum test in MC2/MC3 by the correctly oriented difference test:

`3 ∈ r_k(A_X) - r_{j_i}(A_X)`.

Under this correction, MC1–MC3 become the direct matrix translation of M1–M3, assuming Proposition 3.5.

**Repair status:** REPAIR CANDIDATE; independently proposed by Rheon, Alethon, and Fable; regression-tested on N5, `{0}⊕N5`, L(1), Boolean lattices, chains, M3, and additional attack cases. Formal verification remains desirable.

## Algorithm 3.9 — computation of all minimal covers

**Status:** FALSE AS PRINTED.

It implements the false Theorem 3.7 conditions and can omit genuine minimal covers.

On `N5`, the genuine minimal cover `{a,c}` is rejected by printed MC3.

## Theorem 4.2 — incidence-matrix computation of order

**Status:** SURVIVES CURRENT AUDIT.

Independent hand audit and computational tests have found no disagreement with Definition 2.2 on the tested finite lattices.

## Theorem 5.2 — covering dimension via M(X)

**Status:** NOT VALID AS PRINTED.

It depends explicitly on Theorem 3.7. On the six-element lattice `{0}⊕N5`, the printed minimal-cover conditions yield `M(X)=∅`, so the displayed maximum is not defined in the ordinary sense. The associated Algorithm 5.4 resolves the empty case to zero and produces a wrong numerical value.

## Algorithm 5.4 — covering dimension algorithm

**Status:** FALSE AS PRINTED.

Canonical six-element certificate: `fable-certificate-B-0-plus-N5.md` (also `alethon-certificates-n5-l6.md`).

For `L6 = {0}⊕N5`:

- Definition 2.3 gives `dim(L6)=1`;
- the printed procedure eliminates every candidate from `M(L6)`;
- Algorithm 5.4 prints `dim(L6)=0`.

Thus

`dim_definition(L6) = 1 != 0 = dim_Algorithm5.4(L6)`.

### Direction of the error

Assuming the repaired Proposition 3.5 statement, the printed MC conditions are stronger than the correct M1–M3 conditions, so

`M(X) ⊆ MCov(X)`.

Together with the surviving order computation, this means the defect can discard true minimal covers but does not create false ones. Consequently the numerical procedure can **underestimate**, not overestimate, covering dimension.

## Theorem 6.4 / Algorithm 6.5

**Status:** INHERITED FAILURE.

These depend on the faulty Theorem 3.7 characterization and require correction wherever they identify matrix-selected sets with the true minimal covers.

## Additional specification issue: singleton Step 8 / ∅-underspecification

**Status:** FALSE AS PRINTED (under-specified); fourth defect class for the correction note.

Algorithm 3.9 includes `m=1` candidates in Step 8, where MC1 asks whether `C\{x_{j_i}} = ∅` satisfies the “cover condition.” Definition 3.3 defines that predicate for singletons and antichains of size at least two, **not for the empty set**. On any interesting non-chain lattice whose candidate set includes the singleton top cover alongside larger antichain covers, the printed procedure is literally undefined at that point.

Fable’s patched Certificate B (`fable-certificate-B-0-plus-N5.md`) case-splits every executable reading on `{0}⊕N₅`:

- (a) natural completion (∅ fails cover condition) → `{1}` killed by printed MC2 → `M(X)=∅` → Alg 5.4 prints 0
- (b) singleton retained → `ord({1})=0` from Def 2.2 → prints 0
- (c) no completion → procedure returns nothing (defect, not rescue)

In every executable interpretation the printed procedure outputs **0**; the genuine minimal cover carrying dim=1 is rejected unambiguously by the directional bug, so no singleton-edge resolution recovers the right answer. The case-split is a strengthening, not a hedge.

This is minor next to the directional bug but belongs in the correction note: implementers of a repaired Algorithm 3.9 need an explicit ∅-convention, and the hole independently corroborates that running code would have surfaced it.

---

# II. 2019 downstream paper

The 2019 paper explicitly reprints and uses the 2018 minimal-cover and covering-dimension algorithms in Section 6.

## Proposition 1 — quasi-covering dimension identity

`dim_q(X) = max{ dim(↓x) : x dense in X }`.

**Status:** no inherited 2018-algorithm dependency; direct proof in the 2019 paper. Current evidence supports using this as an independent ground-truth route for the downstream certificate.

## Propositions 2–6, Lemmas 1–3, Corollary 1, Proposition 7 / Algorithm 1

**Status:** no direct inherited dependency on the false 2018 Theorem 3.7 identified so far. These require their own correctness audits before being labeled verified.

Proposition 7 / Algorithm 1 use incidence matrices to detect dense elements and are separate from the faulty minimal-cover translation.

## Definition 14 / Proposition 8

**Status:** imported from 2018 but from the cover-condition machinery that has survived current audit.

## Algorithm 2

**Status:** FALSE AS PRINTED / INHERITED FAILURE.

It reproduces the 2018 minimal-cover algorithm, including the same erroneous row-addition tests in Step 8.

## Algorithm 3

**Status:** FALSE AS PRINTED / INHERITED FAILURE.

It computes `dim(X)` via Algorithm 2 and therefore can reproduce the 2018 underestimation.

## Proposition 9

**Status:** NOT VALID AS PRINTED / INHERITED FAILURE.

Part (1) defines `L_x` using `M(↓x)` and explicitly points back to the proof of the 2018 Theorem 5.2. If the faulty matrix characterization makes `M(↓x)` empty, the displayed maximum may be undefined; if it omits high-order minimal covers, the value can be too small.

Part (2) then propagates those `L_x` values into `dim_q(X)`.

## Algorithm 4 — quasi-covering dimension algorithm

**Status:** FALSE AS PRINTED / INHERITED FAILURE.

### Downstream certificate using the same six-element lattice

Let

`L6 = {0,e,a,b,t,1}`

with

`0 < e < a < t < 1`, `e < b < 1`, and `b ∥ a,t`.

Every nonzero element is dense because `e` is the least nonzero element. The proper principal downsets are chains, hence have covering dimension zero:

- `↓e = {0,e}`;
- `↓a = {0,e,a}`;
- `↓b = {0,e,b}`;
- `↓t = {0,e,a,t}`.

For the top,

`↓1 = L6`

and the direct Definition 2.3 certificate gives

`dim(↓1)=dim(L6)=1`.

Therefore the independently proved Proposition 1 gives

`dim_q(L6)=1`.

But Algorithm 4 calls the faulty Algorithm 3 on every dense-element downset. It returns zero on each proper chain and also returns zero on `↓1=L6`. Hence

`Algorithm4(L6)=0 != 1=dim_q(L6)`.

This is a direct downstream numerical failure.

Alethon 001-B adversarial audit (`alethon-2019-adversarial-audit.md`): independently reproduced the L6 Alg 4 failure; found no ≤5-element Alg 4 numerical cex (L5 = diamond-with-bottom-extension has dim_q=1 but printed Alg 4 returns 1 — no above-element trap); Prop 7 / Alg 1 dense-element test agrees with Definition 6 on the tested suite; Example 4(1)–(2) recomputed as definition-agreeing (bug inert on those covers).

## 2019 repair path

1. Replace Algorithm 2's directional row-sum conditions by the corrected row-difference tests.
2. Use the corrected minimal-cover set in Algorithm 3.
3. Restate Proposition 9 with the corrected `MCov(↓x)` / corrected matrix set and ensure the maximum is nonempty.
4. Algorithm 4 then computes the values of `dim(↓x)` with the corrected Algorithm 3 before taking their maximum.

This repair is conceptually straightforward but should be audited independently rather than inferred solely from the 2018 repair.

---

# III. Verification evidence

Independent discovery / audit lanes:

- **Rheon:** definition-level computational oracle and finite search; independently found the Theorem 3.7 discrepancy, N5-level failure, and six-element final-algorithm failure.
- **Alethon:** adversarial theorem search; independently identified the addition/subtraction directionality bug and produced a separate valid seven-element pipeline witness; later hostile review of the Proposition 3.5 repair found no break.
- **Fable:** referee-style proof audit; independently identified the directionality defect, minimized the certificates to N5 and `{0}⊕N5`, identified the Proposition 3.5 proof gap, and supplied a repair.
- **Isotopy:** structural/dependency audit; independently identified the same representation-interface error and emphasized the construction/representation interface heuristic. One proposed witness was invalid and was rejected by independent verification, demonstrating the need to verify certificates separately from diagnoses.

Current novelty status: **apparently unreported**, pending completion of a full corrigendum/citation/author-page/implementation search and author contact.

---

# IV. Publication checklist

- [x] Human-checkable N5 certificate.
- [x] Human-checkable `{0}⊕N5` certificate.
- [x] Independent computational checker for core certificates.
- [x] Independent hostile audit of Proposition 3.5 repair.
- [x] Corrected Theorem 3.7 candidate.
- [x] Initial downstream 2019 dependency identified.
- [ ] Full audit of 2019 worked examples and all claims in Sections 3–6.
- [x] Full citation-level blast-radius audit of later papers. *Phase 001-C: 6 downstream papers identified, 5/6 full-text audited and CLEARED — no faulty algorithm inheritance. Directional bug contained to original 2018/2019 papers. 1 paper unlocated (Topol. Appl. 2019). See `isotopy-phase-001C-citation-triage.md`.*
- [ ] Search for independent implementations of Algorithms 3.9/5.4 and 2019 Algorithm 4.
- [ ] Formalization of repaired Proposition 3.5 / corrected Theorem 3.7 (Lean or comparable), if feasible.
- [ ] Final novelty search.
- [ ] Contact original authors with concise certificates and proposed repair.
- [ ] Draft correction / research note.

