# AOG-Note — Spin-Stratum Type-Rigidity: An Obstruction to the Galois Action on the Binary Icosahedral Stratum, with Conditional Consequences for the Chiral Lift

*Arithmetic orthogonality of the Galois action $\sqrt{5}\mapsto-\sqrt{5}$ and the spin-stratum operations; conditional chiral-lift consequences*

J. Beau, Independent Researcher, France

## Status

Working paper, v1.8. DOI: [10.5281/zenodo.20693084](https://doi.org/10.5281/zenodo.20693084)

## Abstract

The generation-split value $\epsilon = \tfrac{1}{10}$ is often presented as a derived prediction
of the spectral stratigraphy of the corpus. This note isolates its exact logical status.

First, $\epsilon = \tfrac{1}{10}$ is a theorem modulo the ADE case-selection gate: once a case is
selected whose class-complete spectrum carries the external level ratio $3:2$, the
generation-deficit normal form forces $\epsilon = \tfrac{1}{10}$ and $\kappa = \tfrac{5}{12}$
algebraically, with no further input. Second, the first-principles status of $\epsilon$ is
therefore exactly the first-principles status of the gate, which this note does not settle.

We then examine a candidate arithmetic obstruction. In the compositum
$K_q = \mathbb{Q}(\zeta_q, \sqrt{5})$ the Born–Infeld parity $c \mapsto q-c$, the restriction of complex
conjugation $\zeta_q \mapsto \zeta_q^{-1}$ (the *candidate* fibre involution of Foundation M, a structurally motivated hypothesis
there and taken here as a premise, not derived), fixes $\sqrt{5}$, whereas the Galois action
$\sigma : \sqrt{5} \mapsto -\sqrt{5}$, which exchanges the two two-dimensional irreducible characters of the
binary icosahedral group $2I \cong \mathrm{SL}(2,5)$, lies in the other direct factor: the two are
arithmetically orthogonal.

## What is proved, what is conditional

Each result is stated with its own status; the note does **not** conclude anything about the ADE gate.

- **Clause (a) of Prop. spin-rigidity: proved by the character-table audit** (computed from the group, `code/`): inner conjugations, the central
  element $-I$ and the projective involution $J_\Pi$ induce the identity permutation of $\mathrm{Irr}(2I)$, whereas
  $\sigma$ induces $(2\,2')(3\,3')$. The outer automorphism fixes the order-four class and maps each of the loci
  $5a \cup 5b$ and $10a \cup 10b$ onto itself (exchanging $5a \leftrightarrow 5b$, $10a \leftrightarrow 10b$).
- **Modelling premise** [M] (distinct from the tex clauses (a)-(d)): the list of generators of the spin stratum is complete. This is not proved; it implies
  (and the carrier-level lemma uses only) carrier-preservation of every admissible fibre operation.
- **Candidate base-fibre involution** (hypothesis of Foundation M, not proved there; the fibre identification is an open
  classification problem and O18 shows the parity orbit is not forced into the fibres): taken as a premise. What is
  proved here about it is only that, as complex conjugation, it fixes $\mathbb{Q}(\sqrt{5})$.
- **Conditional clauses (tex clauses (b)-(d))**: the central reflection $R_b$ acts as $-I$ under [H-WS] of Q11OF; the
  A4-locking clause holds under the A4 hypotheses ([H-Gen], $J_\Pi$-covariance, diagonal form, a locked pair) and is
  also a modelling assertion (the locking contributes nothing beyond a sign); the tensor-functor and Schur-projection
  clauses are modelling assertions, not part of the audit.
- **Consequence (Theorem)**: modulo the conditional clauses and [M], no listed operation of the spin stratum realises $\sigma$.
  This is a statement about $\sigma$ only: since both candidate loci (order four; order five/ten) are
  $\sigma$-invariant, a link between the gate and $\sigma$ is **not established**.
- **Full tower** (one status everywhere): the extension to a recursive tower of admissible fibre operations holds
  **relative to the modelling premise** [M] and, for the central reflection, [H-WS] (recursive non-injectivity multiplies the vertical parity type and cannot
  supply $\sigma$); it is not unconditional.

## The chiral lift: conditional consequences

The chiral orientation note (CHO) proves the orientation chain within the inherited Heisenberg central-phase
convention and under [H-WS], and leaves a residual caveat: a possible additional spin-Galois phase of the full
Lorentzian chiral lift. The Lorentzian chiral lift ($S_L\oplus S_R$,
$\mathfrak{mp}(2,\mathbb{R})_{\mathbb{C}}\simeq\mathfrak{sl}_2(\mathbb{C})$) is an **input that this note does not
construct**: its status is that of the spin-solder hypothesis [H-Spin] of Q14 (part (ii) is supplied by no source).
Under [H-Spin], [H-WS], [M], [B] and the inherited central-phase convention of CHO:

- **Lemma (Galois-internal boost, under [H-Spin] and the premise [B]).** [B] (asserted, not derived): the lift extends
  the spin-stratum operations only by the central character and the complexification unit $\mathrm{i}$, acting by complex
  conjugation; it supplies no automorphism moving $\sqrt{5}$, although $\mathrm{Gal}(K_q(\mathrm{i})/\mathbb{Q})$ contains
  such elements. Under [B] the lift supplies no action on $\mathbb{Q}(\sqrt{5})$.
- **Lemma (Weyl vs. Galois conjugation, under [H-Spin]).** The chiral weight $\sigma_L$ classes the Weyl branches
  $\mathbf{2}$ vs. $\bar{\mathbf{2}}$, which is orthogonal to the outer automorphism separating $2$ from $2'$.
- **Corollary (spin-Galois rigidity of the lift, under [H-Spin], [M], [B], [H-WS]).** Every field automorphism induced on
  $K_q$ by the lift fixes $\mathbb{Q}(\sqrt{5})$; any nontrivial part is cyclotomic.
- **Corollary (orientation, under [H-Spin], [H-WS], [M], [B] and the inherited convention [C]).**
  $\omega_\chi(e) = \zeta_q^{\Delta A_c(e)} \Rightarrow \rho_\chi = 1 \Rightarrow
  [\mathrm{H\text{-}orient}] \Rightarrow N_A = \theta_{\max} \neq 0$, where $\rho_\chi = 1$ holds by definition of
  $\sigma_L := \mathrm{sgn}\,\Delta A_c$ on the support. That a cyclotomic reindexing is absorbed into the central block
  is the assumption [C], not argued here.

The statement concerns $N_A \neq 0$, **not** $u \neq 0$, whose promotion to the spectral split would need a transport
of the oriented signal to the $J_\Pi$-odd generation sector; the only transport stated in PRS is [H-Tr] for the
$\mathfrak{sl}_2$ opening, supplied by no source.

## Position in the programme

This note belongs to the **fermionic matter sub-programme** (Presentation Note 6). It fixes the logical status of the
generation-split value $\epsilon$, shows that the Galois action $\sigma$ is not realised by the listed operations of
the spin stratum (without concluding on the ADE case-selection gate), and states the conditional consequences for the
residual caveat of the **chiral orientation note** (CHO). The downstream consequence bounds the relevance of the gate:
observable masses route through the explicit operator $E_\Pi$ and the Yukawa sector regardless of how the gate is
resolved (FM-Note, PRS).

## Reproduction

The audit scripts are in `code/` (provenance, dependencies, expected output and runtimes in `code/README.md`).

```bash
python -m venv .venv && . .venv/bin/activate && pip install -r code/requirements.txt
for s in spin-stratum-type-rigidity-test outer_automorphism_classes frontB2_no_horizontal_operation \
         frontB_recursive_type_rigidity; do python -W error code/$s.py; done
```

Runs recorded from a clean `git archive` of this repository alone (numpy 2.4.0, sympy 1.14.0, Python 3.14.5,
`python -W error`):

| Script | rc | runtime |
|---|---|---|
| `spin-stratum-type-rigidity-test.py` | 0 | 0.12 s |
| `outer_automorphism_classes.py` | 0 | 0.04 s |
| `frontB2_no_horizontal_operation.py` | 0 | 0.68 s |
| `frontB_recursive_type_rigidity.py` | 0 | 2.96 s |

## Compilation

```bash
bash compile.sh
```

Runs `pdflatex → bibtex → pdflatex → pdflatex → pdflatex` (a fourth pdflatex pass settles the table-of-contents page
numbers) on `tex/ArithmeticOrthogonalityADEgate.tex` and produces `out/ArithmeticOrthogonalityADEgate.pdf`.
