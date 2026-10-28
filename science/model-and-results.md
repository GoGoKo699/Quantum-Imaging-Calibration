# Imaging with an unknown jitter variance

Two nearby incoherent point sources and one randomly wandering point source can produce nearly the same image. Spatial mode measurements retain information that direct imaging discards, but they do not remove this ambiguity for free. This project determines the number of signal and calibration photons needed to resolve it when each photon experiences an independent Gaussian displacement whose variance is unknown.

The result is a uniform fixed-error resolution law. Its lower bound permits every joint quantum receiver; its upper bound uses one fixed four-outcome spatial measurement. A matching direct-imaging law exposes an intermediate regime in which uncertainty in the noise removes the scaling advantage of quantum detection. The [interpretation](interpretation.md) explains that regime and the calibration budget needed to leave it.

## Reading route

| Question | Authoritative account |
|---|---|
| What is observed, what is unknown, and what is claimed? | This page |
| Why can no quantum receiver beat the stated order? | [Quantum converse](quantum-converse.md) |
| How is the infinite-dimensional collision calculation justified? | [Collision kernel](collision-kernel.md) |
| Which finite apparatus and tests attain the quantum order? | [Four-outcome receiver](finite-receiver.md) |
| What can be achieved from photon positions alone? | [Direct imaging](direct-imaging.md) |
| What do the plateau and calibration crossovers mean? | [Physical interpretation](interpretation.md) |
| Which ingredients are inherited and what has been compared? | [Related work](../references/related-work.md) |
| Which finite calculations can be reproduced? | [Verification](../verification/README.md) |

## 1. Optical experiment

The known point-spread amplitude is real and transform limited:

```math
\psi_x(y)=(2\pi u)^{-1/4}
\exp\!\left[-\frac{(y-x)^2}{4u}\right],\qquad u>0.
```

The intensity of a point source has variance $`u`$. Specifying its intensity alone would leave an unknown amplitude phase and would not define the quantum model used below. The source centroid and separation axis are known. Two equally bright, mutually incoherent point sources are located at $`-a`$ and $`+a`$, where $`a\ge0`$. Their physical separation is $`s=2a`$.

Each detected photon experiences a fresh unobserved translation $`Z\sim\mathcal N(0,v)`$. The variance $`v`$ is fixed throughout the experiment but unknown. The known dimensionless bound is

```math
0\le B:=v/u\le b,\qquad 0\le b\le b_{\max}.
```

Here $`b_{\max}`$ is fixed; the supplied bound $`b`$ may depend on the photon budgets. No positive lower bound on the actual jitter is required. At $`b=0`$ the model is exactly noiseless.

Let $`g_v`$ denote the centered Gaussian probability measure of variance $`v`$, with $`g_0`$ interpreted as a point mass. The one-photon signal and calibration states are

```math
\begin{aligned}
\rho_{a,v}
&=\int\frac{g_v(x-a)+g_v(x+a)}{2}
\,|\psi_x\rangle\langle\psi_x|\,dx,\\
\tau_v&=\rho_{0,v}.
\end{aligned}
```

Equivalently, the signal displacement is $`X=Z+Sa`$, where the sign $`S\in\{-1,+1\}`$ is fair and independent of $`Z`$. The integral notation at $`v=0`$ means integration against the corresponding point masses.

There are exactly $`N`$ detected signal photons and $`M`$ detected photons from a known point calibration source. The latter have the same jitter variance and independent jitter realizations. With $`q=a^2/u`$, the joint input state is

```math
\Omega_{q,v}
=\rho_{\sqrt{uq},v}^{\otimes N}\otimes\tau_v^{\otimes M}.
```

The counts are conditioned upon, or their laws are parameter independent and matched between hypotheses. Thus a photon-count side channel is not implicitly supplying extra separation information. The calibration photons reveal a distributional parameter; they do not reveal any signal photon's realized displacement. A shared moving screen, a monitored trajectory, or repeated observations with a common displacement would define a different statistical experiment.

## 2. Allowed receivers and statistical task

Write the dimensionless squared half-separation as

```math
q=\frac{a^2}{u}=\frac{s^2}{4u}.
```

Fix an error tolerance $`\epsilon\in(0,1/2)`$ and a finite local range $`0<q_{\max}\le1`$. For a proposed resolution $`h\in(0,q_{\max}]`$, test

```math
H_0:q=0,\ 0\le v\le ub,
\qquad
H_1:h\le q\le q_{\max},\ 0\le v\le ub.
```

The unknown variance is one common value for the signal and calibration streams within each physical world. A composite-hypothesis lower bound may compare a null world with variance $`v_0`$ and an alternative world with a different allowed variance $`v_1`$. Restricting every lower-bound comparison to $`v_0=v_1`$ would exclude admissible hard pairs and could miss the cost of the unknown variance.

A quantum decision is an effect $`0\le T\le I`$ on all $`N+M`$ photons, with outcome $`T`$ interpreted as two sources. Its risk is the larger of its worst false-positive and false-negative probabilities:

```math
\begin{aligned}
\mathcal R_Q(h;N,M,b)
=\inf_{0\le T\le I}\max\Big\{&
\sup_{0\le v\le ub}\mathrm{Tr}(T\Omega_{0,v}),\\
&\sup_{\substack{h\le q\le q_{\max}\\0\le v\le ub}}
\mathrm{Tr}[(I-T)\Omega_{q,v}]
\Big\}.
\end{aligned}
```

The infimum includes collective measurements, quantum memory, independent ancillas, adaptive processing and classical randomization. The receiver may depend on $`N,M,b,u,h,\epsilon,q_{\max}`$, but not on the true $`a`$ or $`v`$. The source is passive: there is no active probe preparation or measurement of the jitter environment.

For $`\mathcal R_{\mathrm{DI}}`$, each photon is measured in position and the infimum is over all randomized classical decisions using the entire resulting record. It is not restricted to a particular estimator. The signal positions have distribution

```math
\tfrac12\mathcal N(-a,u+v)+\tfrac12\mathcal N(a,u+v),
```

and the calibration positions have distribution $`\mathcal N(0,u+v)`$.

## 3. Uniform resolution theorem

Define the effective calibration count and the competing information scale by

```math
K=\frac{NM}{N+M},\qquad K=0\ \text{when }M=0,
\qquad L=\max\{\sqrt N,K\}.
```

The harmonic count arises because a calibrated difference must learn from both samples. Its occurrence is an inherited two-sample statistical mechanism, rather than a separate novelty claim; see [attribution](../references/related-work.md).

**Theorem.** Fix $`\epsilon\in(0,1/2)`$, $`0\le b_{\max}<\infty`$ and $`q_{\max}\in(0,1]`$. There are constants $`0<c<C<\infty`$ and $`N_0\ge2`$, depending only on these fixed quantities, with the following properties for every integer $`N\ge N_0`$, every integer $`M\ge0`$, every $`b\in[0,b_{\max}]`$ and every $`u>0`$. Let

```math
\boxed{
R_Q(N,M,b)=\frac1N+
\min\left\{b,\sqrt{\frac bL}\right\}}
```

and

```math
\boxed{
R_{\mathrm{DI}}(N,M,b)=\frac1{\sqrt N}+
\min\left\{b,\frac1{\sqrt L}\right\}.}
```

For either measurement class $`A\in\{Q,\mathrm{DI}\}`$:

1. If $`0<h\le cR_A`$, then $`\mathcal R_A(h;N,M,b)>\epsilon`$.
2. If $`CR_A\le h\le q_{\max}`$, then $`\mathcal R_A(h;N,M,b)\le\epsilon`$.

The upper statement is asserted only when its interval is nonempty. The choice of $`N_0`$ makes the small hard alternatives in the lower proof lie within $`q_{\max}`$ uniformly in $`M,b`$. These are matching orders with uniform multiplicative constants, not exact leading minimax constants. In physical separation, the corresponding orders are $`s_Q\asymp\sqrt{uR_Q}`$ and $`s_{\mathrm{DI}}\asymp\sqrt{uR_{\mathrm{DI}}}`$; the conversion itself is exactly $`s=2\sqrt{uq}`$.

### Endpoint and resource checks

| Regime | Quantum squared-separation order | Direct-imaging squared-separation order |
|---|---|---|
| Exactly noiseless, $`b=0`$ | $`N^{-1}`$ | $`N^{-1/2}`$ |
| No calibration, $`M=0`$ | $`N^{-1}+\min\{b,\sqrt b\,N^{-1/4}\}`$ | $`N^{-1/2}+\min\{b,N^{-1/4}\}`$ |
| Calibration comparable to signal, $`M\asymp N`$ | $`N^{-1}+\sqrt{b/N}`$ | $`N^{-1/2}`$ |
| Arbitrarily many calibration photons | Same order as $`M\asymp N`$ | Same order as $`M\asymp N`$ |

The simplified calibrated quantum expression uses the fact that when $`b\ll N^{-1}`$, its square-root term is already below the noiseless floor. For $`M\gg N`$, $`K\le N`$ prevents calibration from replacing missing signal photons.

## 4. Why the theorem holds

There are two mechanisms in the quantum lower bound. The first is the noiseless $`1/N`$ floor, which survives any parameter-independent jitter channel. The second is a pair of allowed worlds in which reducing the alternative's jitter partly compensates for its source separation.

For this pair, the [exact collision identity](collision-kernel.md) controls the trace distance of the complete $`N+M`$-photon states. Choosing the compensation weight to balance the two samples gives the exponent

```math
K\frac{q^2}{b}+N\frac{q^4}{b^2}.
```

This expression is used only for $`b>0`$ and for a chosen interior null variance proportional to $`ub`$. The allowed nuisance interval also requires $`q\lesssim b`$. Together these restrictions give $`\min\{b,\sqrt{b/L}\}`$. The proof works at fixed nonzero error and therefore does not infer a testing law solely from a singular Fisher information matrix.

The [attaining apparatus](finite-receiver.md) resolves Hermite–Gaussian modes $`0,1,2`$ of the known point-spread amplitude and groups all higher modes into one fourth outcome. Its basis is independent of the unknown variance. Three classical tests can be formed from the same type of record:

| Information used | Sufficient quantum threshold in $`q`$, up to constants |
|---|---|
| The known upper bound on the jitter variance | $`b+N^{-1}`$ |
| A difference of calibration and signal zero-mode frequencies | $`N^{-1}+\sqrt{b/K}`$, when $`M>0`$ |
| An exact quadratic invariant of modes $`0,1,2`$ | $`N^{-1/2}+\sqrt b\,N^{-1/4}`$ |

Select the test with the smallest certified threshold using the known budgets and noise bound. This choice uses no estimate of the true variance. The minimum is comparable to $`R_Q`$ uniformly, including $`b=0`$ and $`M=0`$.

The direct-imaging proof follows the same nuisance comparison with the optical intensity variance as a nonzero baseline. A fourth cumulant, calibrated second moment and bounded-noise second-moment test attain its three branches. Full proofs are given in [Direct imaging](direct-imaging.md).

## 5. Attribution and scope

Gaussian-mixture weak identifiability and the uncalibrated $`N^{-1/8}`$ physical-separation exponent are established statistical phenomena. Quantum moment estimation, Hermite–Gaussian mode probabilities, noisy-imaging penalties, collision-divergence methods and minimax testing are also established tools. The contribution developed here is their explicit uniform resolution frontier for the stated experiment, with an exact all-receiver converse, an attaining four-outcome measurement, and the resulting calibration-dependent plateau. [Related work](../references/related-work.md) distinguishes those ingredients and records the limits of the source comparison.

The theorem assumes a known real Gaussian point-spread amplitude, a known centroid and axis, equal incoherent source brightness, Gaussian jitter redrawn independently per photon, and identical signal/calibration jitter variances. It does not establish the same law for arbitrary unknown point-spread functions, unknown centroid, correlated motion, non-Gaussian jitter, imperfect calibration transfer or imperfect mode detection. These changes alter either the input experiment or the attaining measurement and require their own analysis.

Proceed to the [quantum converse](quantum-converse.md) for the fundamental limit or the [finite receiver](finite-receiver.md) for the attaining construction.
