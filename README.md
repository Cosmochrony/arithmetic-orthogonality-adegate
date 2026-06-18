# AOG-Note — Spin-Stratum Type-Rigidity: Orthogonality of the ADE Gate and Closure of the Chiral Lift

*Arithmetic Orthogonality of the ADE Case-Selection Gate, and the Chiral-Lift Corollary*

J. Beau, Independent Researcher, France

## Status

Working paper, v1.2. DOI: [10.5281/zenodo.20693084](https://doi.org/10.5281/zenodo.20693084)

## Abstract

The generation-split value $\epsilon = \tfrac{1}{10}$ is often presented as a derived prediction
of the spectral stratigraphy of the corpus. This note isolates its exact logical status.

First, $\epsilon = \tfrac{1}{10}$ is a theorem modulo the ADE case-selection gate: once a case is
selected whose class-complete spectrum carries the external level ratio $3:2$, the
generation-deficit normal form forces $\epsilon = \tfrac{1}{10}$ and $\kappa = \tfrac{5}{12}$
algebraically, with no further input. Second, the first-principles status of $\epsilon$ is
therefore exactly the first-principles status of the gate.

We then characterise the obstruction to deriving the gate as an **arithmetic orthogonality**.
The selection of the $\sqrt{5}$-locus that carries the $3:2$ ratio requires the nontrivial element
of $\mathrm{Gal}(\mathbb{Q}(\sqrt{5})/\mathbb{Q})$, the action $\sqrt{5} \mapsto -\sqrt{5}$. The
only field automorphism supplied by the foundations is the Born–Infeld parity $c \mapsto q-c$, the
restriction of complex conjugation $\zeta_q \mapsto \zeta_q^{-1}$, which fixes $\sqrt{5}$. In the
compositum $K_q = \mathbb{Q}(\zeta_q, \sqrt{5})$ the two actions lie in distinct direct factors of
the Galois group, hence are arithmetically orthogonal. A bounded character-table audit of the
binary icosahedral group $2I \cong \mathrm{SL}(2,5)$ establishes the type-rigidity the gate needs:
every operation available at the spin stratum of the present corpus construction fixes
$\mathbb{Q}(\sqrt{5})$, so their generated group lies in the $\sqrt{5}$-fixing subgroup of
$\mathrm{Gal}(K_q/\mathbb{Q})$, which by closure cannot manufacture the outer automorphism. The
no-go for the ADE gate is therefore **unconditional in the present construction**; only the
abstract type-rigidity of the full recursive tower remains open, and it is broader than the gate
requires.

## The chiral-lift corollary (v1.2)

The same spin-stratum type-rigidity has a second consequence, of **opposite sign**. The chiral
orientation note (CHO) closes $[\mathrm{H\text{-}orient}]$ in the inherited Heisenberg
central-phase lift and leaves a single residual obstruction: a possible additional spin-Galois
phase of the full Lorentzian chiral lift, orthogonal to $\zeta_q$ — in particular a $\sqrt{5}$ or
ADE-spin factor. This note discharges that obstruction from the same proposition:

- **Lemma (Galois-internal boost).** The Lorentzian chiral lift extends the spin-stratum action on
  $K_q$ only by the central character and the analytic complexification, both fixing
  $\mathbb{Q}(\sqrt{5})$.
- **Lemma (Weyl vs. Galois conjugation).** The chiral weight $\sigma_L$ classes the Weyl branches
  $S_L$ vs. $S_R$ by complex-conjugation type ($\mathbf{2}$ vs. $\bar{\mathbf{2}}$), which is
  orthogonal to the outer automorphism that separates the two two-dimensional irreducible
  characters $2$ vs. $2'$ of $2I$.
- **Corollary (spin-Galois rigidity of the lift).** Every field automorphism induced on $K_q$ by
  the Lorentzian chiral lift fixes $\mathbb{Q}(\sqrt{5})$; any nontrivial part is cyclotomic.
- **Corollary (unconditional orientation).** Within the present spin stratum,
  $\omega_\chi(e) = \zeta_q^{\Delta A_c(e)} \Rightarrow \rho_\chi = 1 \Rightarrow
  [\mathrm{H\text{-}orient}] \Rightarrow N_A = \theta_{\max} \neq 0$.

For the gate the rigidity is fatal (the required $\sqrt{5}$ action is absent); for the chiral lift
it is the closure (the feared $\sqrt{5}$ action is absent). The statement closed here is
$N_A \neq 0$, **not** $u \neq 0$, whose promotion to the spectral split remains the Schur transport
on the $J_\Pi$-odd generation sector (PRS).

## Position in the programme

This note belongs to the **fermionic matter sub-programme** (Presentation Note 6). It fixes the
logical status of the generation-split value $\epsilon$, shows that the ADE case-selection gate is
a no-go unconditional in the present corpus construction, and — via the chiral-lift corollary —
discharges the residual obstruction of the **chiral orientation note** (CHO), the gate no-go and
the chiral closure being opposite cuts of a single spin-stratum type-rigidity. The downstream
consequence bounds the relevance of the gate: observable masses route through the explicit operator
$E_\Pi$ and the Yukawa sector regardless of how the gate is resolved (FM-Note, PRS).

## Compilation

```bash
bash compile.sh
```

Runs `pdflatex → bibtex → pdflatex → pdflatex` on `tex/ArithmeticOrthogonalityADEgate.tex` and
produces `out/ArithmeticOrthogonalityADEgate.pdf`.