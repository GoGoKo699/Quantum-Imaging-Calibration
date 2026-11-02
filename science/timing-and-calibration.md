# Calibration when the signal also moves

[Repository overview](../README.md) · [Independent-jitter theorem](model-and-results.md) · [Calibration regimes](interpretation.md)

Independent calibration learns a jitter distribution; it does not tell the receiver how a particular signal photon was displaced. This distinction remains consequential when the signal centroid follows a common Brownian path. Closely timed photons can provide a mutual spatial reference for that path, but each retains its own independent jitter.

This page gives the combined experiment, its resolution frontier and the calibration consequences in a self-contained notation. **[Quantum Imaging Timing](https://github.com/GoGoKo699/Quantum-Imaging-Timing) owns the full joint theorem and proof:** [joint model](https://github.com/GoGoKo699/Quantum-Imaging-Timing/blob/3cafbb49807a0928644ad244a5a0df15d86a17fb/science/joint-model.md), [collective converse](https://github.com/GoGoKo699/Quantum-Imaging-Timing/blob/3cafbb49807a0928644ad244a5a0df15d86a17fb/science/joint-converse.md), [weighted pair receiver](https://github.com/GoGoKo699/Quantum-Imaging-Timing/blob/3cafbb49807a0928644ad244a5a0df15d86a17fb/science/joint-receiver.md), and [regimes](https://github.com/GoGoKo699/Quantum-Imaging-Timing/blob/3cafbb49807a0928644ad244a5a0df15d86a17fb/science/jitter-calibration-regimes.md). The [collision kernel](collision-kernel.md) and independent-jitter theorem remain this repository's contributions and imported proof ingredients. The joint result is one shared result, rather than two independent discoveries.

## 1. Two motions and one fully specified calibration source

Keep the known real Gaussian amplitude of [the optical model](model-and-results.md#1-optical-experiment), with intensity variance $`u`$. Use the timing coordinate $`z=x/\sqrt{2u}`$. A pure point-source state centered at $`\alpha`$ then has amplitude $`\pi^{-1/4}\exp[-(z-\alpha)^2/2]`$.

There are $`N`$ labeled signal-photon registers at known times. Their latent centers in this coordinate are

```math
m+B_i+J_i+S_i\sqrt{q_t},\qquad
q_t=\frac{s^2}{8u}.
```

The initial centroid $`m`$ is unknown and unrestricted. The common Brownian path has independent increments with supplied variances $`\nu_i=D(t_i-t_{i-1})/u`$, where physical Brownian increments have variance $`2D(t_i-t_{i-1})`$. Assume $`0\lt\nu_i\le V`$ for a fixed bound $`V`$. The signs $`S_i`$ are independent and fair. The jitters $`J_i\sim\mathcal N(0,w)`$ are independently redrawn, with one fixed unknown variance $`0\le w\le b_t`$. All latent variables are independent except the common Brownian correlations.

Calibration consists of exactly $`M`$ separate photons from an **externally stabilized point at known coordinate zero**, with the same real Gaussian amplitude and the same unknown jitter variance $`w`$. Its jitter realizations are independent of one another and of all signal variables. The calibration photons do not share or monitor the signal Brownian path. Counts and schedules have matched parameter-independent laws. A moving reference, unknown calibration centroid or mismatch of jitter scales would define another experiment.

The normalization changes by a factor of two from the static theorem on this repository:

| Quantity | Static calibration notation | Joint timing notation |
|---|---|---|
| Squared half-separation | $`q=s^2/(4u)`$ | $`q_t=q/2`$ |
| Actual jitter variance | $`B=v/u`$ | $`w=B/2`$ |
| Supplied variance bound | $`b`$ | $`b_t=b/2`$ |
| Brownian increment variance | Absent from the product experiment | $`\nu_i`$, denoted $`v_i`$ in Timing |
| Physical separation | $`s=2\sqrt{uq}`$ | $`s=2\sqrt{2u q_t}`$ |

The static symbols $`q,B,b`$ elsewhere in this repository retain their original meanings. Matching orders survive these fixed factors; exact probability or collision formulas require the displayed substitutions.

## 2. The bounded-schedule frontier

Fix an error tolerance $`\epsilon\in(0,1/2)`$, local range $`0\lt q_t\le q_0=1/4`$, and finite bounds $`V,b_{t,\max}`$. Test $`q_t=0`$ against $`h\le q_t\le q_0`$, uniformly over $`m`$ and $`0\le w\le b_t\le b_{t,\max}`$. Every joint quantum measurement on all $`N+M`$ registers is allowed in the lower bound.

Let $`r_0`$ be the unique positive root

```math
\sum_{i=2}^{N}\frac{r_0^2}{b_t+\nu_i+r_0}=1,
\qquad
S_2=\sum_{i=2}^{N}(b_t+\nu_i)^{-2}.
```

For $`b_t\gt0`$, put

```math
U=\min\left\{b_t,\sqrt{\frac{b_t}{M}},S_2^{-1/4}\right\},
\qquad R_{Q,t}=r_0+U.
```

Omit the calibration term when $`M=0`$. At $`b_t=0`$, set $`U=0`$ explicitly rather than evaluating $`0/0`$.

**Joint theorem.** There are constants $`0\lt c\lt C`$ and $`N_0\ge4`$, depending only on the fixed error and parameter bounds, such that for $`N\ge N_0`$ the minimax error exceeds $`\epsilon`$ if $`0\lt h\le cR_{Q,t}`$, and is at most $`\epsilon`$ if $`CR_{Q,t}\le h\le q_0`$. The upper statement applies only when its interval is nonempty. Constants are uniform in $`N,M,b_t`$ and all individual gaps. These are testing orders, not exact constants, an unbiased-estimation bound or a claim of adaptation to each realized $`w`$.

The root $`r_0`$ is the physical timing/jitter floor at the worst allowed actual variance. The uncertainty term $`U`$ selects among using the supplied variance band, calibration, or shape information. Learning the variance can reduce $`U`$; it cannot reduce the physical noise already present in $`r_0`$.

For position detection with arbitrary processing of all positions and timestamps, every bounded schedule has order

```math
R_{\mathrm{DI},t}=N^{-1/2}+\min\{b_t,L^{-1/2}\},
\qquad L=\max\{\sqrt N,K\},\quad K=\frac{NM}{N+M},
```

with $`K=0`$ at $`M=0`$. Its optical position variance remains nonzero at zero jitter. This explains why its order has no additional gap dependence under a fixed upper gap bound. The shared [model](https://github.com/GoGoKo699/Quantum-Imaging-Timing/blob/3cafbb49807a0928644ad244a5a0df15d86a17fb/science/joint-model.md) states the complete comparison; ordinary relative position differences, calibrated second moments and fourth cumulants attain it.

## 3. Why the two proof mechanisms compose

The [independent-jitter lower bound](quantum-converse.md) survives adding a parameter-independent Brownian translation channel to signal registers. That simple transfer alone is not enough for the full schedule-dependent frontier. The joint converse also extracts independent noise from the correlated Brownian covariance.

Under an auxiliary allowed Gaussian prior for $`m`$, write the Brownian covariance as $`C=L_B\operatorname{diag}(u_1,\ldots,u_N)L_B^{\mathsf T}`$, where $`u_1=V`$, $`u_i=\nu_i`$ and $`u_{N+1}=\infty`$. Its precision form implies

```math
C\succeq\operatorname{diag}(c_i),\qquad
c_i=\left[2\left(\frac1{u_i}+\frac1{u_{i+1}}\right)\right]^{-1}.
```

Thus independent signal noises of variance $`c_i+w`$, followed by an additional parameter-independent correlated Gaussian channel, generate the entire prior-averaged moving experiment. The sums $`\sum_i(b_t+c_i)^{-2}`$ and $`S_2`$ are comparable. In the more informative independent experiment choose $`w_0=b_t/2`$ and $`w_1=w_0-q_t`$. Full variance compensation matches each signal's second moment. Apply the exact collision identity with optical intensity variance $`1/2`$, squared source displacement $`q_t`$ and signal reference variance $`c_i+b_t/2`$. Its total cost is bounded by

```math
C\left(q_t^4 S_2+M\frac{q_t^2}{b_t}\right),\qquad q_t\lesssim b_t.
```

The signal shape and calibration costs yield $`U`$. A separate known-jitter timing converse yields $`r_0`$. This construction imports the [collision identity and its operator-domain justification](collision-kernel.md); it does not infer a theorem by multiplying previously known rates.

For attainment, take disjoint adjacent photon pairs and retain their relative spatial modes. Common absolute centroids cancel. A relative source displacement is zero with probability $`1/2`$ and each $`\pm\sqrt{2q_t}`$ with probability $`1/4`$, while its Gaussian variance is $`w+d_i`$ with $`d_i=\nu_i/2`$. It is not the static theorem's binary mixture. Different selected relative modes are independent because they depend only on disjoint internal Brownian increments, jitters and signs.

For their full HG indices $`Q_i`$, define

```math
A_i=2Q_i-d_i,\qquad
B_i=\frac43Q_i(Q_i-1)-4d_iQ_i+d_i^2.
```

Their means are $`w+q_t`$ and $`(w+q_t)^2-q_t^2/3`$. Weighted means and an unbiased cross-product statistic separate variance and shape, with weights selected from the known gaps and $`b_t`$. The global shape variance bound controls the full separated alternative, including $`q_t`$ much larger than $`b_t`$. See the shared [receiver proof](https://github.com/GoGoKo699/Quantum-Imaging-Timing/blob/3cafbb49807a0928644ad244a5a0df15d86a17fb/science/joint-receiver.md) for the weights, normalization and error bounds.

This receiver is a genuine joint spatial POVM with full HG mode resolution. The oscillator mode index is not an extra photon resource. The construction does not follow merely from access to a SWAP parity bit or an ordinary HOM device. A four-outcome construction is available for the close-doublet corollary below, with its stated local range; four outcomes are not asserted for arbitrary heterogeneous schedules.

## 4. Close doublets: calibration changes uncertainty, not physical jitter

With a linear number of disjoint doublets whose internal Brownian variances are $`O(N^{-1})`$, the quantum order reduces to

```math
R_{Q,t}=N^{-1}+\min\left\{b_t,\sqrt{\frac{b_t}{L}}\right\},
\qquad L=\max\{\sqrt N,K\}.
```

The direct close-doublet proof can also allow arbitrarily large between-doublet motion. Shrinking the internal intervals requires the timing and temporal-mode access specified by Timing's [physical interface](https://github.com/GoGoKo699/Quantum-Imaging-Timing/blob/3cafbb49807a0928644ad244a5a0df15d86a17fb/science/physical-interface.md).

Without calibration, the three quantum regimes are $`N^{-1}`$ when $`b_t\lesssim N^{-1}`$, an uncertainty plateau of order $`b_t`$ when $`N^{-1}\ll b_t\lesssim N^{-1/2}`$, and the shape branch $`\sqrt{b_t}N^{-1/4}`$ at larger bounds. Calibration improves the active uncertainty branch parametrically only when

```math
K\gg\max\{\sqrt N,b_t^{-1}\}.
```

The shape-to-calibration crossover is $`K\asymp\sqrt N`$. Resolving parametrically below the plateau additionally requires $`Kb_t\gg1`$. Equality of orders marks a crossover, not a parametrically smaller resolution.

Comparable budgets $`M\asymp N`$ reach

```math
q_{t,*}\asymp N^{-1}+\sqrt{b_t/N}.
```

Taking $`M\gg N`$ does not improve this order. For a fixed known actual jitter $`w\gt0`$, the remaining floor is $`q_{t,*}\asymp N^{-1}+\sqrt{w/N}`$, hence physical separation of order $`\sqrt u\,(w/N)^{1/4}`$. The ideal $`N^{-1/2}`$ separation law requires physical jitter itself to be $`O(N^{-1})`$. An arbitrarily accurate variance estimate cannot recover the individual realized jitters.

For a general schedule put $`U_0=\min\{b_t,S_2^{-1/4}\}`$. Calibration changes the uncertainty order once

```math
M\gg\frac{b_t}{U_0^2}=\max\{b_t^{-1},b_t\sqrt{S_2}\},
```

provided $`U_0`$ exceeds the floor $`r_0`$. Reaching that floor needs $`M\gtrsim b_t/r_0^2`$. Known Brownian motion can dominate a weak unknown jitter, allowing fewer than $`N`$ stabilized calibration photons to suffice; this does not mean the physical motion has been removed.

## 5. Attribution, independence and limits

The static calibration account supplies its exact collision identity, compensation mechanism, finite calibration budget and four-outcome known-centroid theorem. Timing supplies the correlated-record model, timing-resource account and Brownian precision/fidelity mechanism. The shared theorem adds diagonal covariance extraction and heterogeneous relative-mode moment correction. Its authoritative proof is linked above once; this page retains the definitions, assumptions, consequences and argument needed to understand Calibration independently.

Hermite–Gaussian moment identities, variance confounding, two-sample information and mutual-reference photon measurements are established ingredients. Brownian crossover exponents have earlier adaptive-SPADE precedents. The [related-work account](../references/related-work.md) identifies these sources and the limits of the literature comparison. The common educational anchor remains Tsang's *Resolving starlight*, [arXiv:1906.02064v2](https://arxiv.org/pdf/1906.02064v2); the [bridge](../learning/tsang-bridge.md) separates its foundations from the new joint proof.

The theorem assumes known diffusion and exact schedule, fixed bounded positive gaps for its general statement, independent Gaussian jitter with a supplied variance bound, a known real Gaussian amplitude, equal independent source signs and a fixed axis, and the specified stabilized calibration source. Unknown diffusion, non-Gaussian or correlated jitter, calibration mismatch, a moving path reference and restricted optical hardware are outside it. Analytical uniformity and receiver access are distinct from the [finite numerical checks](../verification/README.md).
