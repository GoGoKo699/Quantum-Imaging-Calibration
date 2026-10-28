# Checking the quantum collision calculation

[Collision derivation](../science/collision-kernel.md) · [Quantum converse](../science/quantum-converse.md)

`check_collision.py` verifies the exact weighted collision identity using an independently constructed squeezed-oscillator representation. The script uses Python 3.11 or newer with the pinned NumPy dependency. It uses no random sampling, network access, or SciPy.

## Run

From the repository root:

```sh
python verification/check_collision.py
```

The default command enforces the analytic-comparison tolerances and compares the computed results with the committed [expected data](expected/check_collision.json). It does not modify files. A failed comparison exits with an error.

After reviewing a deliberate change to the calculation, the reference can be regenerated explicitly:

```sh
python verification/check_collision.py --record
```

The recording command still requires all comparisons with the closed formulas to pass. Recording new values does not establish their scientific correctness; the spectral construction, quadrature, conventions and analytic derivation must remain consistent.

## What is computed independently

The script does not evaluate the closed kernel inside its oscillator-state calculation. It constructs the coefficients
$`\langle n_w|\psi_x\rangle/\lambda_n(\tau_v)^{1/4}`$ using their three-term recurrence. It then integrates their outer products with Gauss-Hermite quadrature to obtain the weighted operator
$`\tau_v^{-1/4}\rho\tau_v^{-1/4}`$ in a finite basis.

Collision divergences are calculated as the squared Hilbert-Schmidt norm of the weighted state difference. This avoids subtracting one from a nearly unit trace and permits a useful check even when the variance-matched divergence is below $`10^{-15}`$. The closed formula is evaluated separately with 70-digit decimal arithmetic.

The thermal ratio is evaluated as

```math
r=\frac{v/u}{(\sqrt{1+v/u}+1)^2},
```

which is algebraically identical to the formula in the proof but avoids cancellation at very small jitter.

## Check inventory

| Calculation | Cases | Purpose |
|---|---:|---|
| Kernel from weighted coefficient inner products | 18 | Normalization, squeezing convention and cross-term sign |
| Signal collision from integrated weighted matrices | 20 | Non-Gaussian mixture identity and variance compensation |
| Calibration collision from integrated weighted matrices | 20 | Gaussian reference change and exact-zero cases |
| Explicit tensor products of weighted matrices | 2 | Product formula, including no calibration |
| Direct quadrature of pure amplitude overlaps | 3 | Zero-noise endpoint and squared-fidelity convention |

The main parameter grid is
$`(u,v)=(1,10^{-6}),(1,10^{-2}),(1,10^{-1}),(1,1),(1,10),(3,0.2)`$,
with $`a^2=0.2v`$ and compensation weights $`\omega=0,0.3,1`$.
Additional cases include identical states and an alternative with exactly zero jitter, while keeping the collision reference faithful. The separate pure-state checks never evaluate an inverse of a pure reference state.

The kernel uses 200 oscillator levels. Most collision cases use 80 levels and 80 quadrature nodes. The case $`v/u=10`$ uses 160 levels and 240 nodes to control its slower convergence. Explicit tensor checks use 12 levels at $`v/u=0.01`$, where the thermal tail is very small. These finite settings are part of the reproducible calculation, not a uniform tail estimate over all model parameters.

## Expected output and tolerances

The committed calculation reports `PASS` with the following residuals, up to floating-point differences:

| Quantity | Recorded value |
|---|---:|
| Maximum kernel relative error | $`1.29\times10^{-15}`$ |
| Maximum collision absolute error | $`9.03\times10^{-17}`$ |
| Maximum nonzero collision relative error | $`2.27\times10^{-14}`$ |

Kernel and pure-overlap comparisons allow relative error $`2\times10^{-12}`$. Nonzero collision comparisons allow relative error $`2\times10^{-9}`$ plus absolute error $`10^{-25}`$. Exact-zero collision cases have a separate absolute tolerance $`10^{-18}`$: the high-variance calibration quadrature has a small absolute residual, about $`7.4\times10^{-20}`$, even though its mathematical divergence is exactly zero. This zero-case tolerance does not relax the nonzero small-divergence comparisons.

The expected data contain each case's numerical and closed-form values, rather than only a pass/fail flag. The default command also checks that the inventory agrees with the committed reference.

## Limits of the checks

These calculations can expose an incorrect prefactor, thermal parameter, compensation sign, fidelity convention, or tensorization formula. They do not prove the inverse-operator domain, convergence at arbitrary parameters, uniform constants, or minimax optimality. Those claims follow from the analytic [kernel](../science/collision-kernel.md) and [converse](../science/quantum-converse.md) proofs. The calculation is a deterministic consistency check, not a simulation of an implemented receiver or an experimental performance forecast.
