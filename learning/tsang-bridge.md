# From spatial-mode imaging to finite calibration

[Repository overview](../README.md) · [30 milestones](milestones.md) · [Exact model and results](../science/model-and-results.md)

Imagine trying to distinguish two nearby stars from one star whose image wanders randomly. Both mechanisms broaden the observed spot. A mode sorter can retain information that a camera loses, but the apparatus still has to distinguish source structure from unknown motion. This project asks how many signal photons and independently jittered calibration photons make that distinction possible.

The single educational anchor is **Mankei Tsang, *Resolving starlight: a quantum perspective***, [arXiv:1906.02064v2](https://arxiv.org/pdf/1906.02064v2), revised 25 February 2020; the PDF is dated 26 February 2020. The journal record is *Contemporary Physics* **60**, 279–298 (2019 volume), [DOI:10.1080/00107514.2020.1736375](https://doi.org/10.1080/00107514.2020.1736375). Bibliographic metadata and primary research dependencies remain in the [bibliography](../references/references.bib).

Use the review for the optical and statistical viewpoint. The derivations below connect that viewpoint to the repository's experiment. They point to the authoritative proofs rather than replacing them. The [milestone map](milestones.md) organizes the full understanding route; reading the entire review first is unnecessary.

## A focused source route

Page numbers refer to the pinned arXiv PDF, not the journal pagination.

| Review locator | Foundation | Continue in this repository |
|---|---|---|
| II–IV, pp. 1–3 | Measurement choice and the direct-imaging penalty | [Model, §§1–2](../science/model-and-results.md#1-optical-experiment) |
| V, pp. 3–4, Eqs. (5.1)–(5.8); C, pp. 13–14, Eq. (C14) | Position/mode probabilities and incoherent mixtures | [Receiver, §2](../science/finite-receiver.md#2-exact-outcome-probabilities) |
| VII.A–C, pp. 6–8; VII.F, pp. 8–9 | Moment sensitivity and quantum limits | [Shape statistic](../science/finite-receiver.md#3-a-shape-test-with-a-uniform-variance-bound) |
| VIII.A, p. 9; VIII.I–K, pp. 10–11 | Alignment, displacement, minimax reasoning and testing | [Risk](../science/model-and-results.md#2-allowed-receivers-and-statistical-task), [interpretation](../science/interpretation.md) |
| A–B, p. 13 | Statistical and quantum measurement notation | [Quantum converse, §§2–4](../science/quantum-converse.md#2-from-a-pair-of-states-to-minimax-risk) |

## Translate the notation first

| In the review | Here |
|---|---|
| Separation $`\theta`$ | Full separation $`s=2a`$; reconcile any length normalization before substitution |
| Mode label $`q`$ | $`j`$ or $`Q`$; this project's $`q=a^2/u`$ is a different quantity |
| Object moments $`\theta_\mu`$ | Separate from the receiver statistic $`\theta=p_0p_2-3p_1^2/2`$ |
| Mean photon number $`N`$ | Conditioned signal count $`N`$ |
| Temporal-mode count $`M`$ in Appendix C | Separate from calibration-photon count $`M`$ |

The project defines $`u`$ as the known Gaussian **intensity variance** and $`v`$ as the unknown jitter variance. No width notation from a different optical convention is silently identified with $`u`$.

## 1. From one displaced photon to the whole experiment

A point at coordinate $`x`$ produces the normalized amplitude

```math
\psi_x(y)=(2\pi u)^{-1/4}\exp[-(y-x)^2/(4u)].
```

Its intensity $`|\psi_x(y)|^2`$ is a normal density of variance $`u`$. The amplitude is known and real: an intensity profile alone would leave phase information unspecified and would not define the same quantum experiment.

For two equally bright incoherent sources, a signal photon's latent displacement is $`X=Z+Sa`$: $`S`$ is a fair independent sign and $`Z`$ is a fresh normal displacement of variance $`v`$. Average the projectors $`|\psi_X\rangle\langle\psi_X|`$, not the amplitudes, because the sources are incoherent. A calibration photon has displacement $`X=Z`$. These averages give $`\rho_{a,v}`$ and $`\tau_v=\rho_{0,v}`$ in the [model](../science/model-and-results.md#1-optical-experiment).

Independently redrawn displacements yield the product experiment

```math
\Omega_{q,v}=\rho_{\sqrt{uq},v}^{\otimes N}\otimes\tau_v^{\otimes M},
\qquad q=\frac{a^2}{u}=\frac{s^2}{4u}.
```

The streams share one variance, not a realized trajectory. Calibration learns a distributional property; it cannot tell the receiver where an individual signal photon wandered. Counts are fixed or conditioned upon under matched, parameter-independent count laws. These assumptions are part of the experiment, rather than deductions from an optical approximation in the review.

## 2. Why broadening alone cannot settle the question

Normalize a detected position by $`\sqrt u`$ and put $`B=v/u`$. Under direct imaging, its second and fourth moments obey

```math
\mathbb E Y^2=1+B+q,
\qquad
\mathbb E Y^4=3(1+B+q)^2-2q^2.
```

Increasing separation changes the variance through $`q`$. Decreasing jitter can cancel that change. The fourth cumulant still equals

```math
\mathbb E Y^4-3(\mathbb E Y^2)^2=-2q^2.
```

Thus the matched distributions are close rather than identical: the surviving shape signature is quadratic in $`q`$, or fourth order in physical separation. Its classical mixture-statistics origin is credited in [Related work, §2](../references/related-work.md#2-mixture-singularity-and-the-fourth-moment-rate).

For a concrete allowed pair, set $`u=1`$ and allow $`B\le0.02`$. A one-source world with $`B_0=0.010`$ and a two-source world with $`q=0.002`$, $`B_1=0.008`$ both have signal position variance $`1.010`$. Their fourth cumulants are respectively $`0`$ and $`-0.000008`$. Calibration position variances are respectively $`1.010`$ and $`1.008`$. The calibration sample can therefore distinguish these worlds even though their signal variances agree.

Within either world both streams have the same variance parameter. A lower bound may compare different allowed parameters across worlds because a single decision rule must work for all of them. The [quantum converse, §5](../science/quantum-converse.md#5-an-admissible-nuisance-comparison) uses partial rather than necessarily complete compensation when calibration is available.

## 3. What the four outcomes retain

The apparatus resolves modes HG0, HG1 and HG2 of the known optical amplitude and collects their orthogonal complement as a fourth outcome. It uses every detected photon, including a remainder count. Its basis does not depend on the unknown jitter.

Conditionally on displacement $`x`$, the full HG index has the exact law

```math
\Pr(Q=j\mid X=x)=e^{-x^2/(4u)}\frac{[x^2/(4u)]^j}{j!}.
```

The [receiver derivation, §2](../science/finite-receiver.md#2-exact-outcome-probabilities) attributes this identity to Tsang's primary semiparametric-imaging paper, Eqs. (7.17)–(7.19). That research dependency remains distinct from the selected educational review.

Averaging this law over $`Z+Sa`$ gives exact probabilities $`p_0,p_1,p_2`$. With $`D=2+B`$, their useful combination is

```math
p_0=(1+B/2)^{-1/2}e^{-q/(4+2B)},
\qquad
\theta=p_0p_2-\frac32p_1^2=-\frac{p_0^2q^2}{D^4}.
```

Every allowed null has $`\theta=0`$; every nonzero separation makes it negative. The unknown $`B`$ still controls the size of the fluctuations, so cancellation of the mean nuisance is only the beginning of a sample bound.

If $`n_j`$ photons enter category $`j`$, the unbiased pair statistic is

```math
\widehat\theta=
\frac{n_0n_2-\frac32 n_1(n_1-1)}{N(N-1)},\qquad N\ge2.
```

Using $`n_1(n_1-1)`$ counts distinct ordered pairs and avoids the self-counting bias in $`n_1^2`$. The [full variance calculation](../science/finite-receiver.md#3-a-shape-test-with-a-uniform-variance-bound) gives $`\mathrm{Var}(\widehat\theta)\le3(B+q)^2/(4N)`$. When $`q`$ is smaller than $`B`$, balancing its order-$`q^2`$ mean against order-$`B/\sqrt N`$ fluctuations suggests $`q\sim\sqrt B\,N^{-1/4}`$. The proof uses the known upper bound $`b`$, uniform constants and all alternatives $`q\ge h`$, rather than substituting an estimated true variance.

## 4. Calibration, the variance bound and shape are three routes

The same four-outcome record supports three decisions. Their sufficient thresholds are, up to fixed constants,

| Information used | Quantum threshold in $`q`$ |
|---|---|
| Supplied variance bound | $`P=N^{-1}+b`$ |
| Signal/calibration difference of nonzero-mode frequencies | $`C=N^{-1}+\sqrt{b/K}`$, for $`M>0`$ |
| The quadratic shape statistic | $`S=N^{-1/2}+\sqrt b\,N^{-1/4}`$ |

Here $`K=NM/(N+M)`$. A difference of independent sample frequencies has a variance containing both $`1/N`$ and $`1/M`$; their sum equals $`1/K`$. Thus $`K\asymp M`$ when calibration is scarce, and $`K\asymp N`$ when it is abundant. Unlimited calibration cannot supply missing signal photons.

Choose the smallest certified branch using $`N,M,b`$. Disable calibration when $`M=0`$. The [branch comparison](../science/finite-receiver.md#6-combining-the-branches) then gives, with $`L=\max\{\sqrt N,K\}`$,

```math
R_Q=N^{-1}+\min\{b,\sqrt{b/L}\}.
```

At $`b=0`$ all null photons enter HG0. Declaring two sources after any excitation has zero false-positive probability and false-negative probability $`e^{-Nq/4}`$, recovering the $`N^{-1}`$ floor directly.

For position data, the corresponding shape and calibrated-variance tests have a nonzero optical fluctuation baseline even when jitter vanishes. Their combination gives

```math
R_{\mathrm{DI}}=N^{-1/2}+\min\{b,L^{-1/2}\}.
```

The [direct-imaging proof](../science/direct-imaging.md) optimizes over all classical processing of the full position record in its lower bound. It therefore compares measurement classes, rather than just two selected estimators.

## 5. Why this also limits every quantum receiver

An attaining test alone cannot prove optimality. The [converse](../science/quantum-converse.md) chooses one admissible null/alternative pair and bounds the trace distance of their complete states. Every receiver's larger error is at least half of one minus that distance. This includes collective measurements, memory and adaptive processing.

For $`b>0`$, take $`v_0=ub/2`$ and $`v_1=v_0-\omega uq`$, with $`\omega=N/(N+M)`$. Small enough $`q\le b/4`$ keeps both variances allowed. The collision argument bounds the joint distinguishability through a cost of order

```math
K\frac{q^2}{b}+N\frac{q^4}{b^2}.
```

The first term charges the residual two-sample broadening information; the second charges the surviving shape difference. Keeping both small, while respecting $`q\lesssim b`$, gives the nuisance part $`\min\{b,\sqrt{b/L}\}`$. A separate noiseless fidelity comparison supplies the $`N^{-1}`$ floor and covers $`b=0`$.

The [collision-kernel proof](../science/collision-kernel.md) is a research-level dependency of this step. It constructs the weighted state using an inverse quarter root of a faithful Gaussian reference and justifies its domain, trace-class integral and tensor products. The sandwiched weighting cannot be replaced by a different quantum chi-square convention. A local Fisher-information calculation or a finite oscillator truncation does not by itself prove this uniform testing theorem.

## 6. Reassemble the physical conclusion

For small fixed $`b>0`$ without calibration, the quantum scale passes from $`N^{-1}`$ to an order-$`b`$ uncertainty plateau and eventually to $`\sqrt b\,N^{-1/4}`$. More photons never worsen absolute resolution. A relative quantum advantage can nevertheless close when direct imaging reaches the same order near $`N\asymp b^{-2}`$, then return as the quantum shape statistic resolves below the plateau. The [interpretation](../science/interpretation.md) derives the crossovers and calibration requirements.

These are uniform matching orders at fixed error, with a bounded noise range and fixed local separation range. They are not exact risk curves or optimal constants. Physical separation is $`s=2\sqrt{uq}`$, so an exponent for $`q`$ must be halved when reporting an exponent for $`s`$.

The known centroid, known real Gaussian amplitude, equal incoherent sources, independent per-photon jitter and identical signal/calibration variance remain essential. The [source comparison](../references/related-work.md) credits inherited methods and retains unresolved full-text comparison limits. The [verification guide](../verification/README.md) separates reproducible finite calculations from the analytical proofs. Join these ingredients at [M30](milestones.md#m30--reconstruct-the-resolution-frontier-as-one-story) after the map's background and narrative phases.
