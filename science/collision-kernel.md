# Exact collision identity for Gaussian jitter

[Model and results](model-and-results.md) · [Quantum converse](quantum-converse.md) · [Finite receiver](finite-receiver.md)

An exact weighted collision identity makes it possible to compare two-source and one-source images uniformly as the jitter variance approaches zero. This page derives that identity, including the domain of the unbounded inverse operator. The [quantum converse](quantum-converse.md) applies it to the full signal and calibration experiment.

## 1. States and collision convention

The real Gaussian amplitude point-spread function is

```math
\psi_x(y)=(2\pi u)^{-1/4}\exp\!\left[-\frac{(y-x)^2}{4u}\right],
\qquad u>0.
```

Its intensity variance is $`u`$. For $`v>0`$, define

```math
\tau_v=\int_{\mathbb R}g_v(x)|\psi_x\rangle\langle\psi_x|\,dx,
\qquad
\rho_{a,v}=\frac12\int_{\mathbb R}
[g_v(x-a)+g_v(x+a)]|\psi_x\rangle\langle\psi_x|\,dx.
```

Here $`g_v`$ is the centered normal density with variance $`v`$. At $`v=0`$, the integral is interpreted using a point measure. The independent-photon assumption concerns tensor products of these states; it does not change the one-photon calculation below.

For a faithful reference state $`\tau`$, the weighted collision quantity is

```math
\chi^2_{1/2}(\rho\Vert\tau)
=\left\|\tau^{-1/4}(\rho-\tau)\tau^{-1/4}\right\|_2^2
=\mathrm{Tr}\!\left[(\tau^{-1/4}\rho\tau^{-1/4})^2\right]-1,
```

whenever the displayed weighted operators are well defined. The subscript identifies the weighting convention. This is $`\exp[\widetilde D_2(\rho\Vert\tau)]-1`$ for the sandwiched Rényi relative entropy, rather than the Petz expression $`\mathrm{Tr}(\rho^2\tau^{-1})-1`$. The sandwiched relative-entropy framework is established in [Müller-Lennert et al.](https://arxiv.org/abs/1306.3142); general Gaussian-state formulas are developed by [Seshadreesan, Lami and Wilde](https://arxiv.org/abs/1706.09885). The two-source state $`\rho_{a,v}`$ is generally non-Gaussian.

## 2. Squeezed thermal decomposition

Introduce

```math
w=\sqrt{u(u+v)},\qquad t=\frac wu=\sqrt{1+v/u},
\qquad r=\frac{t-1}{t+1}\in(0,1).
```

Let $`|n_w\rangle`$ denote the Hermite-Gaussian basis whose ground-state intensity variance is $`w`$. The Gaussian position kernel is

```math
\langle y|\tau_v|y'\rangle
=\frac1{\sqrt{2\pi(u+v)}}
\exp\!\left[-\frac{(y+y')^2}{8(u+v)}
-\frac{(y-y')^2}{8u}\right].
```

Mehler's identity therefore gives

```math
\tau_v=(1-r)\sum_{n=0}^{\infty}r^n|n_w\rangle\langle n_w|.
```

This representation is faithful for every $`v>0`$, although its inverse is unbounded. It also fixes the squeezing convention and all normalization factors used below.

For $`c_n(x)=\langle n_w|\psi_x\rangle`$, the Hermite generating function gives

```math
\sum_{n=0}^{\infty}\frac{c_n(x)}{\sqrt{n!}}\zeta^n
=(1-r^2)^{1/4}
\exp\!\left[-\frac{x^2}{4(u+w)}
+\frac{\sqrt w\,x}{u+w}\zeta-\frac r2\zeta^2\right].
```

Equivalently, the coefficients obey

```math
c_0(x)=(1-r^2)^{1/4}e^{-x^2/[4(u+w)]},
```

```math
c_n(x)=\frac{\sqrt w\,x}{(u+w)\sqrt n}c_{n-1}(x)
-r\sqrt{\frac{n-1}{n}}c_{n-2}(x),\qquad n\ge1,
```

with the second term absent at $`n=1`$. This recurrence also provides an independent numerical representation of the weighted states.

## 3. Domain of the inverse quarter root

The kernel notation $`\langle\psi_x|\tau_v^{-1/2}|\psi_y\rangle`$ must be interpreted as the quadratic form

```math
\langle\xi_x,\xi_y\rangle,
\qquad |\xi_x\rangle=\tau_v^{-1/4}|\psi_x\rangle.
```

It is not necessary, or generally valid, to apply $`\tau_v^{-1/2}`$ to $`|\psi_y\rangle`$ as a Hilbert-space vector. We first prove that $`|\xi_x\rangle`$ exists.

The Bargmann representation maps a coefficient sequence $`(d_n)`$ to $`\sum_n d_n\zeta^n/\sqrt{n!}`$, with squared norm

```math
\frac1\pi\int_{\mathbb C}|f(\zeta)|^2e^{-|\zeta|^2}\,d^2\zeta.
```

Its isometry follows from the Gaussian orthogonality of the monomials. Multiplying the preceding coefficients by $`[(1-r)r^n]^{-1/4}`$ gives the entire function

```math
f_x(\zeta)=(1+r)^{1/4}e^{-x^2/[4(u+w)]}
\exp\!\left[-\frac{\sqrt r}{2}\zeta^2+\beta_x\zeta\right],
\qquad
\beta_x=\frac{\sqrt w\,x}{(u+w)r^{1/4}}.
```

Writing $`\zeta=s+it`$, the quadratic terms in its norm integral are
$`-(1+\sqrt r)s^2-(1-\sqrt r)t^2`$. Both coefficients are strictly negative. Thus $`f_x`$ has finite Bargmann norm for every real $`x`$, which proves
$`\psi_x\in\mathrm{Dom}\tau_v^{-1/4}`$.

The same integral evaluates the inner product explicitly:

```math
\langle\xi_x,\xi_y\rangle
=\sqrt t\,
\exp\!\left[-\frac{x^2+y^2}{4u}
+\frac{\sqrt{(u+v)/v}}{2u}xy\right].
```

For example, the two Gaussian integrations have linear terms
$`(\beta_x+\beta_y)s`$ and $`i(\beta_y-\beta_x)t`$, respectively. Their factors are
$`\exp[(\beta_x+\beta_y)^2/(4(1+\sqrt r))]`$ and
$`\exp[-(\beta_y-\beta_x)^2/(4(1-\sqrt r))]`$. Substitution gives the displayed expression.

The exact squared kernel is consequently

```math
\boxed{
K_v(x,y)=|\langle\xi_x,\xi_y\rangle|^2
=\sqrt{1+v/u}\,
\exp\!\left[-\frac{x^2+y^2}{2u}
+\frac{\sqrt{(u+v)/v}}u xy\right].
}
```

## 4. Weighted Gaussian mixtures are trace class

Let $`p`$ be a Gaussian position law with any finite mean and variance $`v_1\le v`$, or a finite mixture of such laws. The weighted operator can be constructed directly as the positive trace-class integral

```math
T_p=\int |\xi_x\rangle\langle\xi_x|\,p(dx).
```

To justify this statement, put $`c_v=\sqrt{(u+v)/v}`$. The kernel yields

```math
\|\xi_x\|^2=\sqrt t\,
\exp\!\left[\frac{c_v-1}{2u}x^2\right].
```

Its Gaussian expectation is finite because

```math
\frac{v_1(c_v-1)}u
\le\frac{\sqrt{v(u+v)}-v}{u}<\frac12<1.
```

The first strict inequality on the right follows from
$`\sqrt{v(u+v)}<v+u/2`$. This proves integrability of the trace norm of the positive rank-one integrand. In particular, $`T_p`$ is Hilbert-Schmidt.

For the unweighted preparation $`\rho_p=\int|\psi_x\rangle\langle\psi_x|p(dx)`$,

```math
\rho_p=\tau_v^{1/4}T_p\tau_v^{1/4}.
```

This identity follows first for the rank-one integrands and then for their trace-class integral. It gives a rigorous meaning to $`T_p=\tau_v^{-1/4}\rho_p\tau_v^{-1/4}`$. Finite thermal-basis projections of $`T_p`$ converge in trace norm, and therefore in Hilbert-Schmidt norm.

Furthermore,

```math
\mathrm{Tr}(T_p\tau_v^{1/2})
=\int\langle\xi_x|\tau_v^{1/2}|\xi_x\rangle p(dx)=1.
```

Thus the two definitions of the collision quantity agree, and

```math
1+\chi^2_{1/2}(\rho_p\Vert\tau_v)
=\mathrm{Tr}(T_p^2)
=\iint K_v(x,y)\,p(dx)p(dy).
```

The last equality follows by trace-class integration; the integrand is also bounded in absolute value by $`\|\xi_x\|^2\|\xi_y\|^2`$, whose double integral is finite. These arguments include $`v_1=0`$ without a limiting inverse operator.

## 5. Gaussian integration

Choose

```math
v_1=v-\omega a^2\ge0,\qquad 0\le\omega\le1,
\qquad \ell_v=\sqrt{v(u+v)},\qquad z=\frac{a^2}{\ell_v}.
```

The exponent in $`K_v`$ is $`-\tfrac12(x,y)A(x,y)^T`$, where

```math
A=\frac1u\begin{pmatrix}1&-c_v\\-c_v&1\end{pmatrix}.
```

For independent normal variables with common variance $`v_1`$, the quadratic integral is finite because $`I+v_1A`$ is positive definite. Its smaller eigenvalue is
$`1-v_1/(\ell_v+v)>0`$; the other eigenvalue is positive. Its determinant is

```math
\det(I+v_1A)
=1+\frac{2v_1}u-\frac{v_1^2}{uv}
=(1+v/u)(1-\omega^2z^2).
```

The equal-mean cases $`(a,a)`$ and $`(-a,-a)`$ contribute the exponential
$`\exp[a^2/(\ell_v+\omega a^2)]`$. The opposite-mean cases contribute
$`\exp[-a^2/(\ell_v-\omega a^2)]`$. Both denominators are positive since
$`\omega a^2\le v<\ell_v`$.

**Exact signal identity.** Averaging the four mean choices gives

```math
\boxed{
1+\chi^2_{1/2}(\rho_{a,v-\omega a^2}\Vert\tau_v)
=\frac{\exp[z/(1+\omega z)]+\exp[-z/(1-\omega z)]}
{2\sqrt{1-\omega^2z^2}}.
}
```

**Exact calibration identity.** Setting both means to zero gives

```math
\boxed{
1+\chi^2_{1/2}(\tau_{v-\omega a^2}\Vert\tau_v)
=\frac1{\sqrt{1-\omega^2z^2}}.
}
```

These identities hold throughout $`v>0`$, $`a\ge0`$, $`0\le\omega\le1`$, and $`v-\omega a^2\ge0`$. A small-$`z`$ assumption is needed only for the uniform bounds used next.

## 6. Uniform bounds and variance matching

Denote the right side of the signal identity by $`F_\omega(z)`$. It is even and analytic in $`z`$ for $`|z|<1`$, uniformly for $`\omega\in[0,1]`$. Its quadratic coefficient is
$`\tfrac12(1-\omega)^2`$. Consequently,

```math
\chi^2_{1/2}(\rho_{a,v-\omega a^2}\Vert\tau_v)
=\frac12(1-\omega)^2z^2+O(z^4).
```

For a fully uniform numerical bound, one may take

```math
\chi^2_{1/2}(\rho_{a,v-\omega a^2}\Vert\tau_v)
\le\frac12(1-\omega)^2z^2+200z^4,
\qquad |z|\le\frac12,
```

```math
\chi^2_{1/2}(\tau_{v-\omega a^2}\Vert\tau_v)
\le\omega^2z^2,
\qquad |z|\le\frac12.
```

To see the first bound, on the complex circle $`|z|=3/4`$ one has
$`|F_\omega(z)|\le e^3/\sqrt{1-(3/4)^2}`$. Cauchy's coefficient bound, evenness, and a geometric sum bound the fourth-and-higher-order remainder on $`|z|\le1/2`$ by

```math
\frac{e^3}{\sqrt{1-9/16}}
\frac{|z|^4}{(3/4)^4[1-(2/3)^2]}
<200|z|^4.
```

For the calibration expression, apply the mean-value theorem to
$`(1-x)^{-1/2}-1`$ on $`0\le x\le1/4`$; its derivative is less than one there.

At exact variance matching, $`\omega=1`$, the quadratic term vanishes and

```math
\chi^2_{1/2}(\rho_{a,v-a^2}\Vert\tau_v)
=\frac{z^4}{6}+O(z^6)
=\frac{a^8}{6v^2(u+v)^2}+O(z^6).
```

The relevant local scale is therefore $`\ell_v=\sqrt{v(u+v)}`$, not the jitter variance $`v`$ alone. In particular, for $`a^2\ll v\ll u`$, the collision cost is of order $`a^8/(u^2v^2)`$. The [quantum converse](quantum-converse.md) uses the uniform inequalities rather than treating this local expansion as a minimax theorem.

## References and verification

- M. Müller-Lennert, F. Dupuis, O. Szehr, S. Fehr and M. Tomamichel, “On quantum Rényi entropies: a new generalization and some properties,” *Journal of Mathematical Physics* **54**, 122203 (2013). [arXiv:1306.3142](https://arxiv.org/abs/1306.3142).
- K. P. Seshadreesan, L. Lami and M. M. Wilde, “Rényi relative entropies of quantum Gaussian states,” *Journal of Mathematical Physics* **59**, 072204 (2018). [arXiv:1706.09885](https://arxiv.org/abs/1706.09885).

The [collision verification note](../verification/collision-verification.md) documents an independent oscillator-basis calculation, its tolerances and its scope. The numerical check supplements the analytic domain and integration arguments above.
