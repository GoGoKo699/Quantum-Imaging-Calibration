# Reproduce the scientific checks

The checks compare independent finite representations of the formulas used in the [scientific account](../science/model-and-results.md). They are deterministic numerical calculations, with no random sampling or network access during a run. The analytical proofs establish the infinite-dimensional statements and uniform minimax guarantees.

## Run from the repository root

Use Python 3.11 or later; the recorded run used Python 3.12.14. Install the pinned dependencies, then run the suite:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The [requirements](requirements.txt) pin NumPy 2.3.5, SciPy 1.17.0 and Matplotlib 3.10.8. Matplotlib is used only to reproduce the figure. The runner executes all three calculation scripts, compares their results with committed reference data, and exits unsuccessfully if a check fails. The default command does not rewrite the references. Floating-point comparisons use the tolerances described below; byte-for-byte output equality across numerical-library builds is not required.

## Check inventory

| Script | Independent calculation | Scientific purpose |
|---|---|---|
| [check_collision.py](check_collision.py) | Weighted oscillator coefficients, Gauss–Hermite integration of state matrices, explicit small tensor products and pure-amplitude overlaps | Checks the exact quantum kernel, signal/calibration collision identities, tensorization and fidelity normalization |
| [check_receiver.py](check_receiver.py) | Gaussian quadrature of conditional HG probabilities and exhaustive enumeration of four-category multinomial count records | Checks the finite-mode probabilities, invariant, unbiased count statistic and full U-statistic variance |
| [check_direct_imaging.py](check_direct_imaging.py) | Direct integration of classical collision densities, high-precision endpoint coefficients, Gaussian-mixture moments and kernel squares | Checks the classical hard pair, fourth cumulant, variance calculations and endpoint reductions |

The collision suite has 18 kernel comparisons, 20 signal and 20 calibration collision cases, two explicit tensor-product checks, and three pure-overlap checks. It includes very weak jitter, different optical widths, a high-jitter convergence case, identical states and an alternative with zero jitter. The reference used for every inverse operator remains faithful. The [collision verification note](collision-verification.md) explains the basis sizes, quadrature rules and separate zero-case tolerance.

The receiver suite uses 20 pairs of variance and separation parameters and 60 complete multinomial experiments, with sample sizes 2, 3 and 7. It includes the degenerate zero-jitter null. The direct-imaging suite checks eight collision integrals and nine moment/kernel cases. Both also check 100 resource/noise choices against the algebraic branch reduction. Those finite grids provide useful regression checks; they do not prove uniformity between or beyond their grid points.

## Results and tolerances

The committed references are [quantum collision](expected/check_collision.json), [finite receiver](expected/check_receiver.json) and [direct imaging](expected/check_direct_imaging.json). They retain computed quantities for every case, rather than only a pass/fail flag.

The recorded run found these discrepancies between independent calculations:

| Quantity | Maximum discrepancy, approximately |
|---|---:|
| Quantum collision kernel | $`1.3\times10^{-15}`$ relative |
| Quantum collision identity | $`9.1\times10^{-17}`$ absolute; $`2.3\times10^{-14}`$ relative for nonzero cases |
| HG mode probabilities | $`3.4\times10^{-16}`$ absolute |
| HG invariant and count-statistic moments | Below $`2\times10^{-17}`$ absolute |
| Classical collision identity | $`1.4\times10^{-17}`$ absolute |
| Classical eighth-order moments and kernel squares | Below $`5.5\times10^{-12}`$ absolute on quantities reaching order $`10^3`$ |

The receiver and direct-imaging reference comparisons use absolute tolerance $`5\times10^{-12}`$ and relative tolerance $`2\times10^{-10}`$. The direct-imaging quadrature of larger moments and kernel squares allows absolute tolerance $`2\times10^{-9}`$. High-precision scalar evaluations use Python's decimal arithmetic. Collision checks apply tighter scale-sensitive tolerances, documented in the [dedicated note](collision-verification.md), to avoid masking the small variance-matched divergence with an unnecessarily large absolute threshold.

These are reproducibility tolerances, not bounds on experimental errors or substitutes for the error constants in the proofs. Small platform-dependent differences in the reported residuals are expected.

## Regenerate a deliberately changed reference

After reviewing the scientific meaning of a changed calculation, run:

```bash
python3 verification/run_all.py --record
python3 verification/run_all.py
```

Each recording command still runs its independent formula comparisons before writing. Recording a reference is not independent evidence that a changed formula is correct. Inspect the analytical derivation, the alternate calculation and the changed data together.

## Reproduce the figure

```bash
python3 verification/plot_regimes.py
```

This writes [resolution-regimes.svg](../figures/resolution-regimes.svg) from the theorem's representative scales at the fixed bound $`b=10^{-4}`$. It compares no calibration with $`M=N`$ and plots the uncalibrated direct-imaging/quantum scale ratio. An optional local preview is available with `--png path/to/preview.png`.

The plot omits unknown multiplicative constants. It is a visualization of matching orders, not an exact minimax risk curve, a Monte Carlo performance study, or a forecast for an imperfect laboratory receiver. The physical-separation ratio is the square root of the plotted squared-separation ratio.

## What remains analytical

The following claims are established in the linked proofs, not by the finite checks:

- The [inverse-quarter-root domain and trace-class integration](../science/collision-kernel.md), for every allowed parameter value.
- The [all-receiver trace-distance lower bound](../science/quantum-converse.md), including its uniform constants and separated-alternative quantifiers.
- The [finite receiver's worst-case error guarantees](../science/finite-receiver.md), including all three resource branches.
- The [classical minimax lower bound and moment-test guarantees](../science/direct-imaging.md).
- The [plateau and calibration consequences](../science/interpretation.md) inferred from the proved orders.

Bibliographic priority, experimental implementation and performance outside the stated model are not certified by the numerical suite. Attribution and source-access limits are recorded in [Related work](../references/related-work.md).
