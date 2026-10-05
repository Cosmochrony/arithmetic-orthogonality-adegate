# Audit scripts of the AOG note

These scripts support the character-table audit of the binary icosahedral group `2I = SL(2,5)` used in
`tex/ArithmeticOrthogonalityADEgate.tex` (Proposition "spin-stratum type-rigidity", clause (a), and
Lemma "no horizontal admissible operation"). They are self-contained: nothing outside this repository is read.

## Provenance

| Script | Origin | Dates (first / last change at the source) |
|---|---|---|
| `spin-stratum-type-rigidity-test.py` | vendored from `projective-residue-schur/code/` (PRS 3.0, checked at commit `5e9075e`; file unchanged since `dbf6186`) | 2026-06-16 |
| `frontB2_no_horizontal_operation.py` | vendored from the same directory (last change `1d38b5b`) | 2026-06-27 |
| `frontB_recursive_type_rigidity.py` | vendored from the same directory (last change `5a56ab8`) | 2026-06-27 |
| `outer_automorphism_classes.py` | written for AOG 1.8 (2026-10-05), not vendored | 2026-10-05 |

Differences between the vendored copies and the PRS originals: only the text of some printed verdict lines and
docstring sentences, edited in AOG 1.8 so that they no longer assert a conclusion about the ADE gate (the note does not
establish a link between the gate and the Galois action) and no longer call the Galois conjugate icosian set an
"opposite-chirality" set; `R_b` is stated as hypothesis-dependent ([H-WS]). The computations are unchanged.

## Dependencies

`requirements.txt`: `numpy>=2.4.0`, `sympy` (tested with Python 3.14.5, numpy 2.4.0, sympy 1.14.0).
`outer_automorphism_classes.py` uses the standard library only.

## What each script checks, expected output, runtime

Run from the repository root, e.g. `python -W error code/<script>.py` (return code 0 expected, empty stderr).

- `spin-stratum-type-rigidity-test.py` (about 0.1 s). Builds `SL(2,5)` over `F_5` (120 matrices), computes the nine
  conjugacy classes (orders `1,2,3,4,5,5,6,10,10`, sizes `1,1,20,30,12,12,20,12,12`), reconstructs the character table
  from the class algebra (numerical simultaneous diagonalisation), validates row orthogonality, and finds the
  permutation of `Irr` induced by `sqrt5 -> -sqrt5` (swaps `(2,2')` and `(3,3')`, fixes the other irreps). Also checks
  that all characters are real and prints the spinor grading `chi(-I)/chi(1)`. Expected: "row orthogonality holds: True",
  dimensions `[1, 2, 2, 3, 3, 4, 4, 5, 6]`, nontrivial swaps `[(2, 2), (3, 3)]`. It covers inner conjugation, complex
  conjugation and `-I` only; `R_b`, the tensor functors, the Schur projection and the A4 locking are not computed.
- `outer_automorphism_classes.py` (about 0.1 s). Enumerates `SL(2,5)` and computes the class permutation of the outer
  automorphism (conjugation by `diag(2,1)` in `GL(2,5)`) and of the central lift `g -> -g`. Expected: `5a<->5b`,
  `10a<->10b`, all other classes fixed (in particular the order-four class); each of the loci `5a u 5b`, `10a u 10b` is
  mapped onto itself; `g -> -g` exchanges `1<->2`, `3<->6`, `5a<->10a`, `5b<->10b` and fixes the order-four class.
- `frontB2_no_horizontal_operation.py` (about 1 s). Exact (sympy) icosian realisation of `2I` in `SU(2)` over
  `Q(i, sqrt5)`: the entrywise map `sigma: sqrt5 -> -sqrt5` does not permute the 120 icosians (it maps `2I` to a
  different subgroup), `chi_2 o sigma` is orthogonal to `chi_2`; complex conjugation `kappa: i -> -i` preserves `2I` and
  `chi_2 o kappa = chi_2`. Expected: `sigma ... permutes the 120 icosians: False`, `kappa ... True`,
  `<chi_2 o sigma , chi_2> = 0`.
- `frontB_recursive_type_rigidity.py` (about 3 s). Exact class data and `chi_2`, `chi_2'` over `Q(sqrt5)`:
  `<chi_2,chi_2'> = 0`, `chi_2' != chi_2`, `-I` acts as the scalar `-1` in the defining representation. Expected:
  nine classes, "chi_2 character field contains sqrt5: True".

## Reproduction

```bash
python -m venv .venv && . .venv/bin/activate && pip install -r code/requirements.txt
for s in spin-stratum-type-rigidity-test outer_automorphism_classes frontB2_no_horizontal_operation \
         frontB_recursive_type_rigidity; do python -W error code/$s.py; done
```

The runs recorded for the AOG 1.8 candidate (from a clean `git archive` of this repository alone, interpreter with
numpy 2.4.0 and sympy 1.14.0, `python -W error`) are listed in the repository README.
