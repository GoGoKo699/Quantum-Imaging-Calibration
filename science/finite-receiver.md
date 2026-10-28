# A fixed four-outcome receiver attains the quantum boundary

This page proves the upper bound in [the model and main results](model-and-results.md). The measurement resolves the first three Hermite–Gaussian modes of the known pure point-spread function and groups every other mode into one outcome. The same measurement works for all allowed jitter variances; only the classical decision rule depends on the known resource counts and variance bound.

## 1. Scope and claim

Use the real Gaussian amplitude

```math
\psi_x(y)=(2\pi u)^{-1/4}\exp[-(y-x)^2/(4u)],\qquad u>0.
```

A signal photon has latent displacement $`X=Z+Sa`$, where $`Z\sim\mathcal N(0,v)`$ and $`S=\pm1`$ is an independent fair sign. A calibration photon has displacement $`Z`$. Displacements are independently redrawn for every photon, while the unknown variance is common to both streams. Write

```math
q=\frac{a^2}{u},\qquad B=\frac vu,\qquad
0\le B\le b\le b_{\max},\qquad 0\le q\le q_{\max}\le1.
```

The constants $`b_{\max}<\infty`$, $`q_{\max}>0`$, and error tolerance $`\epsilon\in(0,1/2)`$ are fixed. There are $`N\ge2`$ signal photons and $`M\ge0`$ calibration photons. The null is $`q=0`$; the separated alternative is $`h\le q\le q_{\max}`$, with the same allowed nuisance class in each hypothesis.

Define

```math
K=\frac{NM}{N+M},\qquad L=\max(\sqrt N,K),
```

where $`K=0`$ when $`M=0`$. There is a constant $`C`$, depending only on $`\epsilon,b_{\max},q_{\max}`$, such that the receiver below has both worst-case type-I and worst-case type-II error at most $`\epsilon`$ whenever

```math
h\ge C\left[N^{-1}+\min\left\{b,\sqrt{\frac bL}\right\}\right],
\qquad h\le q_{\max}.
```

The result is a fixed-error, finite-sample statement. It does not require local unbiasedness, asymptotic normality, or a preliminary estimate of $`v`$. [The quantum converse](quantum-converse.md) proves the matching limitation for arbitrary collective measurements.

## 2. Exact outcome probabilities

Let $`Q`$ denote the HG mode index in the basis matched to $`\psi_0`$. The Gaussian overlap identity gives

```math
\Pr(Q=j\mid X=x)
=e^{-x^2/(4u)}\frac{[x^2/(4u)]^j}{j!},
\qquad j=0,1,\ldots.
```

Thus $`Q\mid X=x`$ is Poisson with mean $`x^2/(4u)`$. This standard HG identity, and its use for factorial-moment estimation, are given in Tsang, *Physical Review Research* **1**, 033006 (2019), [arXiv:1906.04578v2](https://arxiv.org/pdf/1906.04578v2), Eqs. (7.17)–(7.19); see also [related work](../references/related-work.md).

Only the four categories $`Y=0,1,2,\mathrm{rest}`$ are retained. All photons count toward $`N`$ or $`M`$, including the remainder outcome. There is no postselection.

For signal photons, direct Gaussian integration gives the generating function

```math
G(z)=\mathbb E z^Q
=\left[1+\frac B2(1-z)\right]^{-1/2}
\exp\left[-\frac{q(1-z)}{4+2B(1-z)}\right].
```

Let $`D=2+B`$. Expanding at zero yields

```math
p_0=(1+B/2)^{-1/2}e^{-q/(4+2B)},
```

```math
\frac{p_1}{p_0}=\frac{B}{2D}+\frac q{D^2},
\qquad
\frac{p_2}{p_0}
=\frac{3B^2}{8D^2}+\frac{3Bq}{2D^3}
+\frac{q^2}{2D^4}.
```

The remainder probability is $`1-p_0-p_1-p_2`$. Calibration probabilities are obtained by setting $`q=0`$. These expressions include $`B=0`$ by continuity and directly agree there with a Poisson law of mean $`q/4`$.

The relevant cancellation is exact:

```math
\theta:=p_0p_2-\frac32p_1^2
=-\frac{p_0^2q^2}{D^4}.
```

The $`B^2`$ and $`Bq`$ terms cancel, leaving a signal that is zero for every allowed null variance and negative for every nonzero separation.

For useful uniform constants, set

```math
p_{\min}=(1+b_{\max}/2)^{-1/2}e^{-q_{\max}/4},
\qquad
\kappa=\frac{p_{\min}^2}{(2+b_{\max})^4},
\qquad
\beta=\frac{p_{\min}}{2(2+b_{\max})}.
```

Throughout the parameter domain,

```math
p_0\ge p_{\min}>0,\qquad
\kappa q^2\le-\theta\le\frac{q^2}{16}.
```

The displayed lower bound on $`p_0`$ uses $`4+2B\ge4`$ and therefore remains valid without estimating $`B`$.

## 3. A shape test with a uniform variance bound

For independent category outcomes $`Y_1,\ldots,Y_N`$, define the symmetric kernel

```math
H(Y_i,Y_j)
=\frac12\!\left[\mathbf1_0(Y_i)\mathbf1_2(Y_j)
+\mathbf1_2(Y_i)\mathbf1_0(Y_j)\right]
-\frac32\mathbf1_1(Y_i)\mathbf1_1(Y_j).
```

Its expectation is $`\theta`$. The corresponding degree-two U-statistic is

```math
\widehat\theta
=\binom N2^{-1}\sum_{i<j}H(Y_i,Y_j)
=\frac{n_0n_2-\frac32n_1(n_1-1)}{N(N-1)}.
```

Here $`n_j`$ is the number of photons in category $`j`$. In particular, the term $`n_1(n_1-1)`$ removes the finite-sample bias that would be introduced by squaring an empirical probability.

Let $`H_1(Y)=\mathbb E[H(Y,Y')\mid Y]`$. Its explicit form and the two relevant moments are

```math
H_1(Y)=\frac12p_2\mathbf1_0(Y)+\frac12p_0\mathbf1_2(Y)
-\frac32p_1\mathbf1_1(Y),
```

```math
\mathbb E H_1^2
=\frac14p_0p_2^2+\frac14p_0^2p_2+\frac94p_1^3,
\qquad
\mathbb E H^2=\frac12p_0p_2+\frac94p_1^2.
```

The exact variance identity is

```math
\mathrm{Var}(\widehat\theta)
=\frac{4(N-2)}{N(N-1)}\mathrm{Var}(H_1)
+\frac{2}{N(N-1)}\mathrm{Var}(H).
```

It includes the degenerate part and remains valid at $`N=2`$.

Put $`t=B+q`$. The probability formulas imply

```math
p_1\le\frac t4,\qquad p_2\le\frac{3t^2}{32}.
```

Consequently $`\mathbb E H^2\le3t^2/16`$. Conditional Jensen gives $`\mathrm{Var}(H_1)\le\mathbb E H^2`$, and the variance identity yields the particularly simple bound

```math
\boxed{\mathrm{Var}(\widehat\theta)
\le \frac{3(B+q)^2}{4N}.}
```

No Gaussian approximation to the count distribution is involved.

Decide for two sources when

```math
\widehat\theta<-\frac{\kappa h^2}{2}.
```

Under the null, Chebyshev's inequality gives

```math
\Pr_0(\text{two sources})
\le\frac{3b^2}{\kappa^2Nh^4}.
```

Under every allowed alternative $`q\ge h`$, the distance between the mean and the threshold is at least $`\kappa q^2/2`$. Hence

```math
\Pr_{q,B}(\text{one source})
\le\frac{3(b+q)^2}{\kappa^2Nq^4}
\le\frac6{\kappa^2}
\left(\frac{b^2}{Nh^4}+\frac1{Nh^2}\right).
```

Both errors are at most $`\epsilon`$ if

```math
h\ge A_{\rm shape}
\left[N^{-1/2}+\sqrt b\,N^{-1/4}\right],
```

for example with

```math
A_{\rm shape}=\max\left\{1,\sqrt{\frac{12}{\kappa^2\epsilon}}\right\}.
```

This controls the full separated alternative, rather than only the point $`q=h`$.

## 4. A calibration test using only the zero-mode event

Assume $`M\ge1`$. Let $`\widehat r_{\rm s}`$ and $`\widehat r_{\rm c}`$ be the signal and calibration frequencies of $`Y\ne0`$. Their difference has null mean zero. Under the alternative its mean is

```math
\Delta(B,q)
=p_0(B,0)-p_0(B,q)
=(1+B/2)^{-1/2}\left[1-e^{-q/(4+2B)}\right].
```

Using $`1-e^{-x}\ge xe^{-x}`$ for $`x\ge0`$ gives

```math
\beta q\le\Delta(B,q)\le\frac q4.
```

The excitation probability obeys

```math
r(B,q)=1-p_0(B,q)
\le\frac{B+q}{4}.
```

One proof uses $`\Pr(Q\ge1)\le\mathbb E Q=(B+q)/4`$; alternatively it follows directly from the expression for $`p_0`$. Thus

```math
\mathrm{Var}(\widehat r_{\rm s}-\widehat r_{\rm c})
\le\frac{b+q}{4N}+\frac b{4M}
=\frac14\left(\frac bK+\frac qN\right).
```

Decide for two sources when $`\widehat r_{\rm s}-\widehat r_{\rm c}>\beta h/2`$. The type-I error is at most $`b/(\beta^2Kh^2)`$. The type-II error, uniformly for $`q\ge h`$, is at most

```math
\frac1{\beta^2}\left(\frac b{Kh^2}+\frac1{Nh}\right).
```

Therefore

```math
h\ge A_{\rm cal}\left[N^{-1}+\sqrt{\frac bK}\right],
\qquad
A_{\rm cal}=\max\left\{1,\frac{2}{\beta^2\epsilon}\right\},
```

suffices. The calibration branch is disabled when $`M=0`$; no expression involving $`0/0`$ is used.

## 5. A test using the known variance upper bound

No calibration is required for this branch. Under the null,

```math
r(B,0)\le b/4.
```

Under the alternative,

```math
r(B,q)\ge\Delta(B,q)\ge\beta q.
```

Use the signal excitation frequency alone and decide for two sources if $`\widehat r_{\rm s}>\beta h/2`$.

If $`h\ge b/\beta`$, the threshold exceeds every null mean by at least $`\beta h/4`$. Chebyshev therefore bounds the type-I error by

```math
\frac{4b}{\beta^2Nh^2}.
```

For the alternative the error is at most

```math
\frac1{\beta^2}\left(\frac b{Nh^2}+\frac1{Nh}\right).
```

Both are at most $`\epsilon`$ whenever

```math
h\ge A_{\rm bound}(b+N^{-1}),
\qquad
A_{\rm bound}=
\max\left\{1,\beta^{-1},\frac{4}{\beta^2\epsilon}\right\}.
```

This branch uses the actual information supplied about the nuisance: an upper bound on its variance. It does not assume that the variance equals the bound or is bounded away from zero.

At $`b=0`$, an even simpler exact test decides for two sources whenever at least one signal photon leaves HG0. Its type-I error is zero and its type-II error is

```math
p_0(0,q)^N=e^{-Nq/4}.
```

Thus $`h\ge4\log(1/\epsilon)/N`$ suffices, irrespective of $`M`$.

## 6. Combining the branches

Let $`A`$ be the maximum of the three constants above. The same optical data admit thresholds of order

```math
S=N^{-1/2}+\sqrt b\,N^{-1/4},\qquad
C_{\rm cal}=N^{-1}+\sqrt{b/K},\qquad
P=N^{-1}+b,
```

where $`C_{\rm cal}=\infty`$ if $`M=0`$. Select the smallest branch using only $`N,M,b`$.

If $`K\ge\sqrt N`$, the better of calibration and the known-bound test attains

```math
N^{-1}+\min\{b,\sqrt{b/K}\}.
```

If $`K\le\sqrt N`$ and $`b\le N^{-1/2}`$, the known-bound test attains $`N^{-1}+b`$. If $`K\le\sqrt N`$ and $`b\ge N^{-1/2}`$, then

```math
S\le2\sqrt b\,N^{-1/4}.
```

Together these cases prove

```math
\min\{S,C_{\rm cal},P\}
\le2\left[N^{-1}+\min\{b,\sqrt{b/L}\}\right].
```

Taking $`C=2A`$ proves the claim. Its error guarantee is meaningful whenever the required threshold lies inside $`(0,q_{\max}]`$. The proof itself works for every $`N\ge2`$; the main theorem uses sufficiently large $`N`$ so the stated local threshold is nonempty.

## 7. Verification and attribution

[The receiver verification script](../verification/check_receiver.py) checks the exact probabilities against Gaussian quadrature and independently enumerates the multinomial count distribution at small sample sizes. It verifies the U-statistic's expectation, its full variance identity, and the stated elementary variance bound, including zero jitter and the null. These calculations check algebra and normalization; the inequalities above establish the uniform testing guarantee.

HG mode sorting, Gaussian HG probabilities, moment sensitivity, and the possibility of attaining moment orders with finitely many selected modes are established methods. The receiver here provides an explicit attainable construction for the composite jitter-and-calibration boundary. The contribution and its closest comparisons are separated in [related work](../references/related-work.md).

