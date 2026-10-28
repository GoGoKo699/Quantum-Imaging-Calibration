# Quantum converse for finite-calibration resolution

[Model and results](model-and-results.md) · [Collision kernel](collision-kernel.md) · [Finite receiver](finite-receiver.md) · [Interpretation](interpretation.md)

This page proves the lower bound for every quantum receiver. Two different obstructions are needed: the ideal pure-state detection limit, and a nuisance-variance comparison that trades a small source separation against a smaller jitter variance. Together they remain uniform when the only noise information is an upper bound and that bound approaches zero.

## 1. Experiment and fixed-error risk

The known real Gaussian amplitude PSF has intensity variance $`u>0`$. Let

```math
q=\frac{a^2}{u},\qquad 0\le v\le ub,\qquad 0\le b\le b_{\max}.
```

The physical source separation is $`s=2a=2\sqrt{uq}`$. There are $`N\ge1`$ signal photons and $`M\ge0`$ point-calibration photons, with independently redrawn Gaussian translations and a common unknown variance $`v`$. The state is

```math
\Omega_{q,v}
=\rho_{\sqrt{uq},v}^{\otimes N}\otimes\tau_v^{\otimes M}.
```

The one-photon states are defined in the [model](model-and-results.md) and [collision calculation](collision-kernel.md). A factor with exponent zero is omitted. Counts are fixed, or conditioned upon under a parameter-independent matched count law.

Fix $`\epsilon\in(0,1/2)`$ and $`q_{\max}\in(0,1]`$. A test effect $`T`$ means deciding that two sources are present. Its minimax risk at squared-separation threshold $`h\in(0,q_{\max}]`$ is

```math
\mathcal R_Q(h)=\inf_{0\le T\le I}\max\left\{
\sup_{0\le v\le ub}\mathrm{Tr}(\Omega_{0,v}T),
\sup_{\substack{0\le v\le ub\\h\le q\le q_{\max}}}
\mathrm{Tr}[\Omega_{q,v}(I-T)]
\right\}.
```

The measurement can be collective. Independent ancillas, storage, adaptive processing and a final measurement are included in this optimization. The source and its jitter realizations are not controllable inputs to the receiver.

The nuisance variance is the same for the signal and calibration photons **within each hypothesis**. A minimax lower bound can select different variances under the null and alternative, because the same test must control its errors at every allowed parameter point.

Set

```math
K=\frac{NM}{N+M},\qquad L=\max(\sqrt N,K),
```

with $`K=0`$ at $`M=0`$, and define

```math
R_Q=\frac1N+\min\!\left\{b,\sqrt{\frac bL}\right\}.
```

**Theorem.** There are $`c_\epsilon>0`$ and
$`N_0=N_0(\epsilon,b_{\max},q_{\max})`$ such that, for every
$`N\ge N_0`$, every integer $`M\ge0`$ and every $`b\in[0,b_{\max}]`$,

```math
0<h\le c_\epsilon R_Q
\quad\Longrightarrow\quad
\mathcal R_Q(h)>\epsilon.
```

The constants are independent of $`N,M,b,u`$. The [finite receiver](finite-receiver.md) supplies the matching upper bound at sufficiently large multiples of $`R_Q`$, whenever those thresholds fit below $`q_{\max}`$. The theorem concerns fixed nonzero error; it does not specify an optimal error exponent or a leading minimax constant.

## 2. From a pair of states to minimax risk

For any selected null state $`\sigma_0`$ and alternative state $`\sigma_1`$, let

```math
D(\sigma_0,\sigma_1)=\frac12\|\sigma_0-\sigma_1\|_1.
```

Every binary test satisfies

```math
\frac12\left[\mathrm{Tr}(\sigma_0T)
+\mathrm{Tr}[\sigma_1(I-T)]\right]
\ge\frac{1-D(\sigma_0,\sigma_1)}2.
```

Indeed, the left side is
$`\tfrac12[1-\mathrm{Tr}T(\sigma_1-\sigma_0)]`$, and trace-distance duality bounds the last trace by $`D`$. The maximum of the two errors is at least their average. A single admissible pair with small trace distance therefore proves a lower bound on the stated composite risk.

All processing by the receiver is a quantum channel followed by a measurement; trace distance cannot increase under such processing. The converse is consequently independent of the choice of spatial measurement or quantum implementation.

## 3. Pure-state obstruction

Use the squared-fidelity convention
$`F(\sigma,\rho)=\|\sqrt\sigma\sqrt\rho\|_1^2`$. For the noiseless one-photon null and equal two-source alternative,

```math
F(|\psi_0\rangle\langle\psi_0|,\rho_{a,0})
=\langle\psi_0|\rho_{a,0}|\psi_0\rangle
=e^{-a^2/(4u)}=e^{-q/4}.
```

For $`N`$ independent photons this becomes $`e^{-Nq/4}`$. The fidelity–trace-distance inequality of [Fuchs and van de Graaf](https://arxiv.org/abs/quant-ph/9712042) gives

```math
D(\Omega_{0,0},\Omega_{q,0})
\le\sqrt{1-e^{-Nq/4}}.
```

The calibration factor is identical in the two hypotheses and does not affect the distance. The same upper bound holds if the same fixed variance $`v`$ is added to both signal states, by contractivity under the Gaussian translation channel. In particular, $`v=0`$ is always an admissible pair in the present nuisance family.

Thus $`Nq`$ must be at least a constant at any prescribed error below one half. This argument remains valid at $`b=0`$ and does not use an expansion around a full-rank state.

## 4. Collision tools, with infinite-dimensional justification

For the Gaussian reference states below, the [kernel proof](collision-kernel.md) constructs the weighted operator

```math
T_\rho=\tau^{-1/4}\rho\tau^{-1/4}
```

as a positive trace-class integral. In particular,
$`\rho=\tau^{1/4}T_\rho\tau^{1/4}`$ and
$`\mathrm{Tr}(T_\rho\tau^{1/2})=1`$. Consequently,

```math
\chi^2_{1/2}(\rho\Vert\tau)
=\|T_\rho-\tau^{1/2}\|_2^2
=\mathrm{Tr}(T_\rho^2)-1.
```

### Trace-distance bound

Let $`B=T_\rho-\tau^{1/2}`$. For a Hermitian contraction $`H`$,

```math
|\mathrm{Tr}[(\rho-\tau)H]|
=|\mathrm{Tr}[B\tau^{1/4}H\tau^{1/4}]|
\le\|B\|_2\,\|\tau^{1/4}H\tau^{1/4}\|_2.
```

The products are legitimate by Schatten Hölder inequalities: $`B`$ is Hilbert-Schmidt and $`\tau^{1/4}`$ is in Schatten class four. In a spectral basis of $`\tau`$,

```math
\|\tau^{1/4}H\tau^{1/4}\|_2^2
=\sum_{i,j}\sqrt{\lambda_i\lambda_j}|H_{ij}|^2
\le\mathrm{Tr}(\tau H^2)\le1.
```

The middle inequality uses $`\sqrt{\lambda_i\lambda_j}\le(\lambda_i+\lambda_j)/2`$. Taking the dual supremum gives

```math
\boxed{D(\rho,\tau)\le\frac12\sqrt{\chi^2_{1/2}(\rho\Vert\tau)}.}
```

### Product identity

Weighted operators factor under finite tensor products. Therefore,

```math
1+\chi^2_{1/2}(\rho^{\otimes N}\otimes\sigma^{\otimes M}
\Vert\tau^{\otimes(N+M)})
=\bigl[1+\chi^2_{1/2}(\rho\Vert\tau)\bigr]^N
\bigl[1+\chi^2_{1/2}(\sigma\Vert\tau)\bigr]^M.
```

This is an identity for the sandwiched collision weighting, not for an interchangeable choice of quantum chi-square divergence. At $`M=0`$ the second factor equals one. The positive trace-class construction in the companion proof justifies the tensor products and trace factorization without a bounded-inverse assumption.

## 5. An admissible nuisance comparison

Assume $`b>0`$. Select

```math
v_0=\frac{ub}{2},\qquad
\omega=\frac{N}{N+M},\qquad
v_1=v_0-\omega uq.
```

If $`q\le b/4`$, then $`ub/4\le v_1\le v_0\le ub`$. Thus the null point
$`(0,v_0)`$ and alternative point $`(q,v_1)`$ are both allowed. In the null, every photon has state $`\tau_{v_0}`$. In the alternative, signal photons have state $`\rho_{\sqrt{uq},v_1}`$ and calibration photons have state $`\tau_{v_1}`$.

Set

```math
z=\frac{uq}{\sqrt{v_0(u+v_0)}}
=\frac{q}{\sqrt{(b/2)(1+b/2)}}.
```

For $`|z|\le1/2`$, the exact collision identities imply

```math
\chi^2_{\rm sig}\le\frac12(1-\omega)^2z^2+200z^4,
\qquad
\chi^2_{\rm cal}\le\omega^2z^2.
```

Use $`\log(1+x)\le x`$ and the product identity. Since

```math
N(1-\omega)^2+M\omega^2=\frac{NM}{N+M}=K,
```

the joint collision cost obeys

```math
\log\!\left[1+\chi^2_{1/2}(\Omega_{q,v_1}\Vert\Omega_{0,v_0})\right]
\le Kz^2+200Nz^4
\le\frac{2Kq^2}{b}+\frac{800Nq^4}{b^2}.
```

This finite-error inequality holds for arbitrary collective receivers. No singular Fisher-information inversion is involved. At $`M=0`$, $`\omega=1`$ and $`K=0`$: the leading variance difference is absorbed completely, leaving the fourth-order shape cost.

## 6. Uniform phase lower bound

Write

```math
r_1=\frac1N,\qquad
r_2=\min\!\left\{b,\sqrt{\frac bL}\right\},\qquad
R_Q=r_1+r_2.
```

We construct a hard pair at exactly $`q=cR_Q`$. This automatically belongs to every separated alternative whose threshold satisfies $`h\le cR_Q`$.

### Case A: the pure scale dominates

If $`r_1\ge r_2`$, then $`q\le2c/N`$. The pure-state comparison gives

```math
D\le\sqrt{1-e^{-Nq/4}}\le\sqrt{c/2}.
```

This case includes $`b=0`$.

### Case B: the nuisance scale dominates

If $`r_2\ge r_1`$, then $`b>0`$ and $`q\le2cr_2\le2cb`$. Choose $`c\le1/8`$. The variances in Section 5 are then admissible, and

```math
z\le\frac{2cb}{\sqrt{(b/2)(1+b/2)}}\le4c\le\frac12.
```

If $`Lb\ge1`$, then $`r_2=\sqrt{b/L}`$, so

```math
\frac{Kq^2}{b}\le4c^2\frac KL\le4c^2,
\qquad
\frac{Nq^4}{b^2}\le16c^4\frac N{L^2}\le16c^4.
```

If $`Lb\le1`$, then $`r_2=b`$, so

```math
\frac{Kq^2}{b}\le4c^2Kb\le4c^2,
\qquad
\frac{Nq^4}{b^2}\le16c^4Nb^2\le16c^4.
```

Both cases use only $`K\le L`$ and $`N\le L^2`$. Thus

```math
D(\Omega_{q,v_1},\Omega_{0,v_0})
\le\frac12\sqrt{\exp(8c^2+12800c^4)-1}.
```

The right side can be made uniformly small by one fixed choice of $`c`$.

### Choice of constants and separated alternatives

For example, let $`\delta=1-2\epsilon\in(0,1)`$ and choose the conservative constant

```math
c_\epsilon=\frac{\delta^2}{100}.
```

Both case bounds are then less than $`\delta/8`$. Every test has maximum error at least

```math
\frac{1-\delta/8}{2}>\epsilon
```

at the constructed pair. This proves the theorem for all
$`h\le c_\epsilon R_Q`$.

The upper alternative cutoff causes no hidden nonuniformity. Since $`L\ge\sqrt N`$,

```math
R_Q\le\frac1N+\sqrt{b_{\max}}\,N^{-1/4}.
```

Choose $`N_0`$ so that $`c_\epsilon`$ times this upper bound is at most $`q_{\max}`$. The hard point then lies inside the allowed alternative uniformly over $`M`$ and $`b`$. The construction does not require the hard point to equal the user-specified threshold; its inclusion in the separated alternative is sufficient.

## 7. Endpoints and scope

| Case | How the converse applies |
|---|---|
| $`M=0`$ | $`K=0`$, $`\omega=1`$; no calibration tensor factor is present. |
| $`b=0`$ | Use the pure-state comparison only; $`R_Q=N^{-1}`$. No inverse of a pure state is evaluated. |
| $`b\to0`$ | The positive reference variance is selected separately for each $`b>0`$; all constants remain uniform. |
| Very large $`M`$ | $`K\le N`$ and the proof is unchanged; calibration photons are counted explicitly. |
| $`h< c_\epsilon R_Q`$ | The same hard point at $`q=c_\epsilon R_Q`$ remains in the alternative. |

The nuisance lower bound is an experiment comparison, not a claim that its selected pair is uniquely least favorable. The receiver may know the upper bound $`b`$ and all other specified model parameters. It does not receive the realized jitter or a reference system correlated with that realization. Shared jitter across photons, an unknown centroid, non-Gaussian jitter, a mismatch between the two streams, or active probing define different experiments.

## References and proof dependencies

- C. A. Fuchs and J. van de Graaf, “Cryptographic distinguishability measures for quantum-mechanical states,” *IEEE Transactions on Information Theory* **45**, 1216–1227 (1999). [arXiv:quant-ph/9712042](https://arxiv.org/abs/quant-ph/9712042).
- M. Müller-Lennert et al., “On quantum Rényi entropies: a new generalization and some properties,” *Journal of Mathematical Physics* **54**, 122203 (2013). [arXiv:1306.3142](https://arxiv.org/abs/1306.3142).
- The [collision-kernel derivation](collision-kernel.md) supplies the exact weighted Gaussian-mixture identity and its operator-domain justification.
- The [finite receiver](finite-receiver.md) supplies the matching uniform upper bound with four spatial outcomes.

The theorem is established by the analytic arguments. The [verification note](../verification/collision-verification.md) describes numerical checks of the collision formula and its constants, without treating finite truncation as a proof of the infinite-dimensional statement.
