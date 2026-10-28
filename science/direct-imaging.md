# The direct-imaging resolution boundary

This page proves both sides of the direct-imaging result in [the model and main results](model-and-results.md). The comparison allows arbitrary processing of the entire position record, including calibration observations. It does not restrict the classical estimator to a particular fit or moment method.

## 1. Experiment and theorem

Measure each photon's position and divide it by $`\sqrt u`$. A signal observation then has the density

```math
p_{q,B}(y)
=\frac12\phi_{1+B}(y-\sqrt q)
+\frac12\phi_{1+B}(y+\sqrt q),
```

where $`\phi_s`$ denotes the centered Gaussian density of variance $`s`$,
$`q=a^2/u`$, and $`B=v/u`$. A calibration observation has density $`\phi_{1+B}`$. All observations are independent. Within each hypothesis, the signal and calibration streams have the same unknown $`B`$.

Fix $`0<q_{\max}\le1`$, $`b_{\max}<\infty`$, and $`\epsilon\in(0,1/2)`$. The nuisance class is $`0\le B\le b\le b_{\max}`$. Test $`q=0`$ against $`h\le q\le q_{\max}`$. The risk is the maximum of the worst-case type-I and type-II errors, as in the main model.

For $`N`$ signal observations and $`M`$ calibration observations, set

```math
K=\frac{NM}{N+M},\qquad L=\max(\sqrt N,K),
```

with $`K=0`$ when $`M=0`$. The direct-imaging boundary is

```math
\boxed{
R_{\rm DI}(N,M,b)
=N^{-1/2}+\min\{b,L^{-1/2}\}.
}
```

There are constants $`0<c<C<\infty`$ and $`N_0`$, depending only on the fixed quantities above, such that:

- If $`N\ge N_0`$ and $`0<h\le cR_{\rm DI}`$, every direct-imaging test has risk strictly greater than $`\epsilon`$.
- If $`N\ge N_0`$ and $`CR_{\rm DI}\le h\le q_{\max}`$, an explicit test has risk at most $`\epsilon`$.

The upper statement is subject to $`CR_{\rm DI}\le q_{\max}`$, so its alternative is nonempty. The lower construction also lies in the specified local parameter domain once $`N\ge N_0`$.

The unknown-variance Gaussian-mixture singularity and its fixed-noise $`N^{-1/8}`$ separation rate are established classical results. See Chen and Chen (2003), [*Tests for homogeneity in normal mixtures in the presence of a structural parameter*](https://www3.stat.sinica.edu.tw/statistica/j13n2/j13n25/j13n25.html), and Dwivedi et al. (2020), [*Sharp Analysis of Expectation-Maximization for Weakly Identifiable Models*](https://proceedings.mlr.press/v108/dwivedi20a.html). The proof here supplies the finite-error calibration-and-bound comparison needed for the quantum imaging experiment; [related work](../references/related-work.md) records the inheritance.

## 2. Three attainable tests

Let

```math
T=1+B+q,\qquad T_{\max}=1+b_{\max}+q_{\max}.
```

A signal observation can be written as $`Y=\sqrt{1+B}\,G+\sqrt q\,S`$, with $`G`$ standard normal and $`S`$ an independent fair sign. Its moments satisfy

```math
\mathbb EY^2=T,\qquad
\mathbb EY^4=3T^2-2q^2,\qquad
\operatorname{Var}(Y^2)=2T^2-2q^2\le2T_{\max}^2.
```

More generally,

```math
\mathbb EY^{2r}\le(2r-1)!!\,T^r.
```

To see the last inequality, expand the even moment of the sum. Each term is nonnegative, and replacing the fair sign by an independent standard Gaussian changes its even moments from $`1`$ to $`(2j-1)!!\ge1`$. The resulting Gaussian has variance $`T`$.

### 2.1 A fourth-cumulant shape test

For $`N\ge2`$, use the unbiased statistic

```math
\widehat C_4
=\frac1N\sum_{i=1}^NY_i^4
-\frac{3}{N(N-1)}\sum_{i\ne j}Y_i^2Y_j^2.
```

Its expectation is exactly

```math
\mathbb E\widehat C_4
=\mathbb EY^4-3(\mathbb EY^2)^2=-2q^2.
```

It is a degree-two U-statistic with symmetric kernel

```math
H(y,z)=\frac12(y^4+z^4)-3y^2z^2.
```

Write $`m_{2r}=\mathbb EY^{2r}`$. The second moment is

```math
\mathbb EH^2
=\frac12m_8+\frac{19}{2}m_4^2-6m_2m_6
\le138T_{\max}^4.
```

The U-statistic variance identity, including its order-$`N^{-2}`$ term, gives

```math
\operatorname{Var}(\widehat C_4)
\le\frac{4\mathbb EH^2}{N}
\le\frac{V_4}{N},
\qquad V_4=552T_{\max}^4.
```

Decide for two sources if $`\widehat C_4<-h^2`$. Under the null the mean is zero. For every alternative $`q\ge h`$, the distance from the mean to the threshold is at least $`q^2`$. Chebyshev therefore bounds either error by $`V_4/(Nh^4)`$. It suffices that

```math
h\ge A_4N^{-1/4},\qquad A_4=(V_4/\epsilon)^{1/4}.
```

### 2.2 A calibrated second-moment test

For $`M\ge1`$, let

```math
\widehat D_2
=\frac1N\sum_{i=1}^NY_i^2
-\frac1M\sum_{j=1}^M(Y_j^{\rm c})^2.
```

Its expectation is $`q`$, and its variance is at most

```math
2T_{\max}^2\left(\frac1N+\frac1M\right)
=\frac{2T_{\max}^2}{K}.
```

Decide for two sources if $`\widehat D_2>h/2`$. Both errors are at most $`8T_{\max}^2/(Kh^2)`$, uniformly over $`q\ge h`$. Thus

```math
h\ge A_2K^{-1/2},\qquad
A_2=\sqrt{8T_{\max}^2/\epsilon},
```

suffices. This branch is disabled when $`M=0`$.

### 2.3 A known-bound second-moment test

Use $`\widehat S_2=N^{-1}\sum_iY_i^2`$. Under the null its mean is at most $`1+b`$; under the alternative its mean is at least $`1+q`$.

Decide for two sources if $`\widehat S_2>1+h/2`$. When $`h\ge4b`$, the threshold exceeds every null mean by at least $`h/4`$. The type-I error is at most $`32T_{\max}^2/(Nh^2)`$. Under every alternative the distance from the mean to the threshold is at least $`q/2`$, giving type-II error at most $`8T_{\max}^2/(Nq^2)`$. It follows that

```math
h\ge A_{\rm bound}(b+N^{-1/2}),\qquad
A_{\rm bound}
=\max\left\{4,\sqrt{32T_{\max}^2/\epsilon}\right\},
```

suffices. This includes $`b=0`$ and requires no calibration.

### 2.4 Combining the tests

Let $`A=\max(A_4,A_2,A_{\rm bound})`$. Select the best of the three tests using the known $`N,M,b`$. Its threshold is at most

```math
A\min\{N^{-1/4},K^{-1/2},b+N^{-1/2}\},
```

with $`K^{-1/2}=\infty`$ for the disabled branch.

The minimum of the first two terms is $`L^{-1/2}`$. Since $`K\le N`$ and $`N\ge1`$, one has $`L\le N`$ and therefore $`N^{-1/2}\le L^{-1/2}`$. In particular,

```math
\min\{L^{-1/2},b+N^{-1/2}\}
\le N^{-1/2}+\min\{b,L^{-1/2}\}.
```

This proves the upper theorem with $`C=A`$. All thresholds are uniform over the full separated alternative.

## 3. A testing inequality with a strict error margin

For two probability laws $`P_0,P_1`$, write

```math
\chi^2(P_1\Vert P_0)
=\int\frac{(dP_1-dP_0)^2}{dP_0},
\qquad
\operatorname{TV}(P_0,P_1)
=\frac12\int|dP_1-dP_0|.
```

Cauchy–Schwarz gives

```math
\operatorname{TV}(P_0,P_1)\le\frac12\sqrt{\chi^2(P_1\Vert P_0)}.
```

For any test, its larger error is at least its equal-prior average error and hence at least

```math
\frac{1-\operatorname{TV}(P_0,P_1)}2.
```

This also lower-bounds the composite minimax risk whenever the two laws are allowed null and alternative instances.

To keep the lower theorem strictly above $`\epsilon`$, define

```math
\zeta_\epsilon=\log[1+(1-2\epsilon)^2].
```

If $`\log[1+\chi^2(P_1\Vert P_0)]\le\zeta_\epsilon`$, then

```math
\operatorname{TV}(P_0,P_1)\le\frac{1-2\epsilon}{2},
\qquad
\max(\text{two errors})\ge\frac{1+2\epsilon}{4}>\epsilon.
```

All lower constructions below meet this common margin.

For independent observations the collision integral tensorizes:

```math
1+\chi^2(P_1^{\otimes N}\Vert P_0^{\otimes N})
=[1+\chi^2(P_1\Vert P_0)]^N.
```

The same identity applies to the product of the signal and calibration streams.

## 4. The diffraction baseline

Choose $`B=0`$ under both hypotheses; this is allowed for every $`b\ge0`$. Calibration observations then have exactly the same law in both worlds.

For the signal, the null is $`\phi_1`$ and the alternative is the equal mixture shifted by $`\pm\sqrt q`$. Its likelihood ratio under the null is

```math
e^{-q/2}\cosh(\sqrt q\,Y).
```

Direct integration gives

```math
1+\chi^2(p_{q,0}\Vert\phi_1)=\cosh q.
```

Since $`\log\cosh q\le q^2/2`$, the full record satisfies

```math
\log(1+\chi^2_{\rm total})\le\frac{Nq^2}{2}.
```

Choose

```math
q_0=c_0N^{-1/2},\qquad
0<c_0\le\min\{1,\sqrt{2\zeta_\epsilon}\}.
```

Then the strict testing margin above applies. Once $`q_0\le q_{\max}`$, this proves the $`N^{-1/2}`$ lower branch, for every calibration budget and every nuisance bound, including $`b=0`$.

## 5. Exact collision identity for the matched-nuisance pair

Assume $`b>0`$. Set

```math
B_0=b/2,\qquad
w=\frac{N}{N+M},\qquad
B_1=B_0-wq,
```

where $`w=1`$ if $`M=0`$. If $`q\le b/4`$, then both $`B_0`$ and $`B_1`$ lie in $`[0,b]`$.

The null has $`q=0,B=B_0`$. The alternative has separation parameter $`q`$ and variance $`B=B_1`$. In each world, the signal and calibration variances agree. Allowing the nuisance to differ between the two worlds is required by the composite testing problem; it does not give the signal and calibration streams different variances within one experiment.

Let

```math
s_0=1+B_0,\qquad s_1=s_0-wq,\qquad t=q/s_0.
```

When $`|wt|<1`$, the exact one-observation collision integrals are

```math
C_{\rm s}(t,w)
:=1+\chi^2(p_{q,B_1}\Vert\phi_{s_0})
=\frac{e^{\,t/(1+wt)}+e^{-t/(1-wt)}}{2\sqrt{1-w^2t^2}},
```

```math
C_{\rm c}(t,w)
:=1+\chi^2(\phi_{s_1}\Vert\phi_{s_0})
=\frac1{\sqrt{1-w^2t^2}}.
```

For completeness, the same-sign Gaussian overlap is

```math
\int\frac{\phi_{s_1}(y-\sqrt q)^2}{\phi_{s_0}(y)}\,dy
=\frac{e^{\,t/(1+wt)}}{\sqrt{1-w^2t^2}},
```

while the opposite-sign overlap is

```math
\int\frac{\phi_{s_1}(y-\sqrt q)\phi_{s_1}(y+\sqrt q)}
{\phi_{s_0}(y)}\,dy
=\frac{e^{-t/(1-wt)}}{\sqrt{1-w^2t^2}}.
```

Averaging the four terms of the squared mixture gives $`C_{\rm s}`$. Setting the displacement to zero gives $`C_{\rm c}`$.

The signal expression is even in $`t`$. Its second-order expansion is

```math
C_{\rm s}(t,w)
=1+\frac{(1-w)^2}{2}t^2+O(t^4),
```

uniformly for $`0\le w\le1`$ and $`|t|\le1/4`$. This is a uniform remainder, not an assumption about an unspecified asymptotic limit: the displayed function has a continuous fourth derivative on that compact set, with all denominators bounded away from zero. If

```math
C_4=\frac1{24}
\max_{\substack{|t|\le1/4\\0\le w\le1}}
|\partial_t^4C_{\rm s}(t,w)|,
```

Taylor's theorem gives

```math
C_{\rm s}(t,w)-1
\le\frac{(1-w)^2}{2}t^2+C_4t^4.
```

Also,

```math
\log C_{\rm c}
=-\frac12\log(1-w^2t^2)\le w^2t^2
\quad\text{for } |wt|\le1/4.
```

Using $`\log x\le x-1`$ and tensorization,

```math
\begin{aligned}
\log(1+\chi^2_{\rm total})
&=N\log C_{\rm s}+M\log C_{\rm c}\\
&\le [N(1-w)^2+Mw^2]t^2+C_4Nt^4\\
&=Kt^2+C_4Nt^4\\
&\le C_*\,[Kq^2+Nq^4],
\qquad C_*=\max\{1,C_4\}.
\end{aligned}
```

The last step uses $`s_0\ge1`$. The harmonic count $`K`$ follows from the elementary identity

```math
N(1-w)^2+Mw^2=\frac{NM}{N+M}.
```

## 6. The nuisance lower branch and the full converse

Let

```math
\nu=\min\{b,L^{-1/2}\},\qquad q_1=c_1\nu,
```

where $`0<c_1\le1/4`$ is small enough that

```math
C_*(c_1^2+c_1^4)\le\zeta_\epsilon.
```

Then $`q_1\le b/4`$, so the nuisance pair is admissible. Since $`L\ge1`$, one also has $`t\le q_1\le1/4`$. Finally,

```math
K\nu^2\le K/L\le1,\qquad
N\nu^4\le N/L^2\le1.
```

Thus the full collision exponent is at most $`\zeta_\epsilon`$, giving risk strictly above $`\epsilon`$ at $`q=q_1`$. This includes $`M=0`$ exactly: $`w=1`$, $`K=0`$, and the leading quadratic signal term vanishes. At $`b=0`$, this branch is zero and is simply omitted.

The two difficult alternatives $`q_0`$ and $`q_1`$ need not use the same pair of nuisance values. Their existence gives

```math
\max(q_0,q_1)
\ge\frac{\min(c_0,c_1)}2
\left[N^{-1/2}+\min\{b,L^{-1/2}\}\right].
```

Choose $`c=\min(c_0,c_1)/2`$. Whenever $`h\le cR_{\rm DI}`$, at least one constructed difficult alternative belongs to the separated alternative set $`q\ge h`$. Both lie below $`q_{\max}`$ for sufficiently large $`N`$, uniformly in $`b,M`$, because

```math
q_0\le c_0N^{-1/2},\qquad q_1\le c_1N^{-1/4}.
```

This proves the full lower theorem, including its strict error inequality and all resource endpoints.

## 7. Interpretation and verification

Direct imaging retains an order-one position variance even when the pointing jitter vanishes. Its baseline is consequently $`q\asymp N^{-1/2}`$. Unknown jitter can absorb the leading increase in the second moment; the uncalibrated shape information first appears in the fourth cumulant. A finite calibration record and a known variance upper bound provide the other two ways to resolve that ambiguity.

The uniform frontier compares these resources at fixed error. It should not be described only by its fixed-positive-noise $`N^{-1/8}`$ separation endpoint, which omits the shrinking-noise and calibration transitions. [Interpretation](interpretation.md) gives the comparison with the quantum frontier.

[The direct-imaging verification script](../verification/check_direct_imaging.py) checks the exact collision integrals against Gaussian quadrature, the endpoint coefficients at high precision, the harmonic-count identity, and the Gaussian-mixture moment/U-statistic formulas. The analytic argument above supplies the bounds and quantifiers; numerical checks are not substitutes for the minimax proof.

