# Related work and attribution

This account compares the experiment in [Model and results](../science/model-and-results.md) with literature available on 28 October 2026. The central distinction is between established ingredients—mixture singularity, quantum moment sensitivity, nuisance projection, and mode-selective detection—and their combination in a uniform finite-calibration resolution law. Bibliographic records are collected in [references.bib](references.bib).

## 1. The statement being compared

The optical amplitude is a known real Gaussian with intensity variance $`u`$. The source is either a point at a known centroid or two equally bright incoherent points at $`\pm a`$. Each detected photon experiences a fresh, unobserved Gaussian translation with a fixed but unknown variance $`v`$. The receiver knows only $`0\le v\le ub`$. It receives $`N`$ signal photons and $`M`$ independent point-source calibration photons with the same unknown variance. Calibration photons do not reveal the signal photons' realized translations.

For $`q=a^2/u`$, $`K=NM/(N+M)`$ and $`L=\max\{\sqrt N,K\}`$, the project proves the fixed-error minimax orders

```math
q_Q\asymp N^{-1}+\min\{b,\sqrt{b/L}\},
\qquad
q_{\mathrm{DI}}\asymp N^{-1/2}+\min\{b,L^{-1/2}\}.
```

The constants are uniform over the stated bounded ranges, including $`b=0`$ and $`M=0`$. The quantum lower bound permits every joint measurement on the signal and calibration states. The upper bound uses the fixed outcomes HG0, HG1, HG2, and their orthogonal complement. These are matching orders, not exact leading constants or a claim that four outcomes are necessary.

At fixed small $`b`$ without calibration, the quantum resolution in $`q`$ follows $`N^{-1}`$, then stays of order $`b`$ for $`b^{-1}\ll N\ll b^{-2}`$, then follows $`\sqrt b\,N^{-1/4}`$. Its parametric advantage over direct imaging closes near $`N\asymp b^{-2}`$ and reappears at larger photon budgets. Resolution does not worsen with additional photons. The plateau is temporary and calibration-dependent; it is not an absolute nonidentifiability claim.

The distinguishing mathematical statement is this joint dependence on the noise bound, the two photon budgets, and the measurement class. The following comparisons identify what is already present in earlier work.

## 2. Mixture singularity and the fourth-moment rate

For direct imaging, the observation law is the symmetric mixture of Gaussians with means $`\pm a`$ and variance $`u+v`$. Reducing the alternative's variance can cancel the leading $`a^2`$ change. The remaining shape difference appears through a fourth cumulant of order $`a^4`$, producing a divergence of order $`a^8`$ at fixed positive noise. This mechanism and the resulting $`N^{-1/8}`$ location or physical-separation exponent are established phenomena in Gaussian-mixture statistics.

Chen and Chen's *Tests for homogeneity in normal mixtures in the presence of a structural parameter* (2003) explicitly reports $`n^{-1/4}`$ behavior for a structural scale parameter and $`n^{-1/8}`$ behavior for the mixing distribution. The [journal abstract](https://www3.stat.sinica.edu.tw/statistica/j13n2/j13n25/j13n25.html) supports this attribution; a theorem-by-theorem comparison with its full text is not used here. `ChenChen2003`

Dwivedi et al.'s *Sharp Analysis of Expectation-Maximization for Weakly Identifiable Models* (AISTATS 2020) studies the corresponding location-scale mixture singularity and proves slow statistical and algorithmic rates for EM. Section 1.2, Eq. (2), identifies the derivative relation coupling mean and variance; the stated univariate location and scale rates are $`n^{-1/8}`$ and $`n^{-1/4}`$. These results concern mixture estimation rather than a quantum receiver or an independent optical calibration budget. They establish that neither the cancellation mechanism nor its fixed-noise exponent is new here. [Primary paper](https://proceedings.mlr.press/v108/dwivedi20a/dwivedi20a.pdf). `DwivediEtAl2020`

The [direct-imaging proof](../science/direct-imaging.md) supplies the finite-error, bounded-nuisance and finite-calibration comparison needed for this optical experiment. It should be read as a model-specific use of that established singularity.

## 3. Quantum imaging, moments and minimax analysis

### 3.1 Noiseless resolution and worst-case guarantees

Tsang, Nair and Lu established the quantum advantage of spatial-mode measurements for two incoherent point sources in *Quantum Theory of Superresolution for Two Incoherent Optical Point Sources* (2016). The known-response, noiseless endpoint is therefore an antecedent, not an independent contribution of the present result. [Primary record](https://arxiv.org/abs/1511.00552). `TsangNairLu2016`

Tsang's *Conservative classical and quantum resolution limits for incoherent imaging* (2018; preprint version 3 dated 26 March 2017) already replaces unbiased pointwise Cramér–Rao reasoning with worst-case mean-square error. Equations (2)–(4) bound the quantum and direct-imaging risks and prove a finite-photon SPADE maximum-likelihood guarantee. Appendix B develops the Bayesian/minimax bound and Appendix D proves the attaining bound. The experiment has a known Gaussian response and no unknown jitter variance or finite calibration sample. It nevertheless establishes that minimax imaging analysis, finite-photon guarantees and optimization over quantum measurements are inherited methods. [Primary paper](https://arxiv.org/pdf/1605.03799v3). `Tsang2018Minimax`

### 3.2 Fourth moments and finite mode measurements

Tsang's *Quantum limit to subdiffraction incoherent optical imaging* (2019) derives the moment-information hierarchy: Eq. (4.14) gives an upper information order $`N\Delta^{-2\lfloor\mu/2\rfloor}`$ for moment order $`\mu`$ and object width $`\Delta`$. In particular, fourth-moment uncertainty of order $`\Delta^4/N`$ in mean-square error is already anticipated. Interpreting $`\Delta^2`$ as a weak displacement variance explains the improved quantum sensitivity to the fourth-order signature. [Primary paper](https://arxiv.org/pdf/1806.02781v4). `Tsang2019Moments`

The sequel *Quantum limit to subdiffraction incoherent optical imaging. II. A parametric-submodel approach* (2021) supplies an infinite-dimensional proof. Theorem 1, Eq. (5.11), and Proposition 1, Eq. (6.16), establish moment lower bounds and attainment with one or two selected modes. Theorem 1 assumes a bounded momentum operator and a compact-support object distribution in a specified Szegő class; the attaining proposition has weaker optical assumptions, including a Gaussian spatial-frequency distribution. Those hypotheses do not literally give the present Gaussian-jitter testing theorem. The conclusion that few-mode measurements attain moment orders is, however, explicit prior work. [Primary paper, pp. 6–7](https://arxiv.org/pdf/2010.03518v4). `Tsang2021Submodel`

Tsang's *Semiparametric estimation for incoherent optical imaging* (2019) derives efficient moment estimators for known-response direct imaging and SPADE. For a Gaussian amplitude, Eqs. (7.17)–(7.19) give the exact HG Poisson probabilities and factorial-moment estimators. These identities are the starting point of the receiver calculation here. The nuisance distribution in that paper is the object itself; it does not supply the present finite-calibration testing law for an unknown optical displacement variance. [Primary paper, Sec. VII, p. 6](https://arxiv.org/pdf/1906.04578v2). `Tsang2019Semiparametric`

Consequently, the fixed-positive-noise separation exponent, the weak-noise fourth-moment sensitivity and the broad principle of few-mode attainment are inherited. The [receiver construction](../science/finite-receiver.md) uses an exact quadratic identity among three Gaussian HG probabilities to attain the uniform composite testing frontier. Its significance is tied to that frontier; the construction does not assert the first nuisance-eliminating statistic or the first finite-mode receiver.

### 3.3 Random-displacement models

Tsang's *Quantum noise spectroscopy as an incoherent imaging problem* (2023) explicitly develops the connection between incoherent imaging and a quantum probe subject to random displacement. Appendix C, Eq. (80), gives an information upper bound that, under the present Gaussian normalization, becomes $`1/[2v(v+2u)]`$. Thus the displacement interpretation and the enhanced local sensitivity at weak noise are antecedents. The present result addresses a finite-error composite test in which a binary source displacement and an unknown Gaussian variance compete, with a separate finite calibration stream. [Primary paper](https://arxiv.org/pdf/2209.06104v3). `Tsang2023Noise`

### 3.4 State-distance and Gaussian-operator methods

The quantum converse uses established information-theoretic tools. Its collision quantity is $`\exp[\widetilde D_2(\rho\Vert\tau)]-1`$ in the sandwiched Rényi convention developed by Müller-Lennert et al. (2013); general Gaussian-state Rényi formulas are developed by Seshadreesan, Lami and Wilde (2018). The fidelity-to-trace-distance inequalities are due to Fuchs and van de Graaf (1999). The [collision-kernel proof](../science/collision-kernel.md) supplies the specific infinite-dimensional integral and binary-mixture identity used here, with operator domains treated explicitly. The signal mixture is generally non-Gaussian, so its identity is not cited as a Gaussian-state formula. [Rényi framework](https://arxiv.org/abs/1306.3142), [Gaussian states](https://arxiv.org/abs/1706.09885), [fidelity inequalities](https://arxiv.org/abs/quant-ph/9712042). `MullerLennertEtAl2013`, `SeshadreesanLamiWilde2018`, `FuchsVanDeGraaf1999`

## 4. Nuisance parameters and calibration

Suzuki, Yang and Hayashi's review *Quantum state estimation with nuisance parameters* (2020) develops the classical and quantum nuisance framework. Section 2.1, Eq. (13), gives the Schur-complement information; Section 2.3 describes parameter orthogonalization; Sections 4–5 treat quantum nuisance models and one parameter of interest. This provides the established local geometry behind variance confounding. [Primary review](https://arxiv.org/pdf/1911.02790v3). `SuzukiYangHayashi2020`

The harmonic count is an ordinary two-sample consequence. Independent estimates with errors proportional to $`1/N`$ and $`1/M`$ give a difference variance proportional to $`1/N+1/M=1/K`$. Equivalently, nuisance elimination in a local information matrix gives the same Schur complement. The appearance of $`K`$ alone is therefore not a novelty claim. What requires the present calculation is how this calibration scale competes with the higher-order shape information and the shrinking noise interval, uniformly at a singular boundary.

Grace, Dutton, Ashok and Guha's *Approaching quantum-limited imaging resolution without prior knowledge of the object location* (2020) develops a two-stage strategy: direct imaging estimates the centroid and subsequent mode sorting estimates separation. Section II.B treats an offset with a specified distribution; Eq. (13) averages a joint record over an offset drawn once per trial. The systematic-error scale is supplied to the estimator. This is a static alignment nuisance and a photon-allocation problem, rather than fresh per-photon noise with unknown variance learned from an independent point-source sample. [Primary paper, pp. 2–5](https://arxiv.org/pdf/1908.01996v1). `GraceEtAl2020`

Grace and Guha's *Identifying Objects at the Quantum Limit for Superresolution Imaging* (2022) establishes quantum limits and linear-optical detection strategies for discriminating incoherent objects. Its accessible primary abstract supports credit for quantum object classification and object-independent structured receivers. Detailed comparisons below do not rely on inaccessible supplementary calculations from that paper. [Primary record](https://arxiv.org/abs/2107.00673), [journal](https://doi.org/10.1103/PhysRevLett.129.180502). `GraceGuha2022`

## 5. Noise, imperfections and finite-photon failures

Oh, Zhou, Wong and Jiang's *Quantum Limits of Superresolution in a Noisy Environment* (2021) proves that excitation noise can force the separation quantum Fisher information to vanish at zero separation; Proposition 1 gives the full-rank-noise obstruction. It also treats false detections. This establishes that a fundamental quantum imaging advantage can be degraded by noise. Its local-information statement does not quantify the extra ambiguity of an unknown jitter variance or the independent calibration cost considered here. [Primary paper](https://arxiv.org/pdf/2008.11339v3). `OhEtAl2021`

Schlichtholz et al.'s *Practical tests for sub-Rayleigh source discriminations with imperfect demultiplexers* (2024) is especially relevant to finite-error testing. Its Eq. (5) gives a Chernoff crossover from quadratic to quartic separation dependence under crosstalk. Equations (9)–(12) show the failure of the ideal single-click test and construct a test with controlled error for separations above a chosen threshold. The noise enters a specified imperfect mode measurement; its null click probability is supplied to the test. The paper does not optimize over all receivers after the unknown random-displacement channel. The present formulation inherits the need for finite-error tests and nonuniform noise limits. [Primary preprint, pp. 2–4](https://arxiv.org/pdf/2303.02654v1). `SchlichtholzEtAl2024`

Schlichtholz's *Superresolving optical ruler based on spatial mode demultiplexing for systems evolving under Brownian motion* (2025; preprint 2024) analyzes adaptive HG sorting between realignments. The diffusion coefficient and measurement-cycle duration determine the averaged response. Section IV, Eq. (7), and its discussion give the transition between $`N^{-1/2}`$ and $`N^{-1/4}`$ physical-separation scalings; Sections V–VI discuss alignment timing. It studies a specified receiver and a Brownian trajectory, not the independent unknown-variance experiment used here. Correlated Brownian motion cannot be identified with fresh independent jitter merely because their one-photon marginals can both be broadened. [Primary preprint](https://arxiv.org/html/2407.13723v1). `Schlichtholz2025Brownian`

Kariya's *Singular Asymptotics of SPADE in Quantum Source Discrimination* (2026, version 3 dated 14 August) analyzes a weak unequal-brightness companion, singular Bayesian asymptotics, and a fixed sorter offset. Section IV.2 and Appendix C exhibit a reflection-induced blind branch at $`s=2\theta`$ for HG counting about that offset. This is prior evidence that singularity and finite photon budgets can undermine a nominal SPADE advantage. Its receiver-specific fixed-offset model differs from the present all-receiver minimax law for fresh jitter and independent calibration. [Primary paper](https://arxiv.org/html/2605.14432v3). `Kariya2026`

## 6. Blind responses and nuisance-eliminating measurements

Lian, Zhu and Cao's *Quantum Limits of Blind Superresolution Imaging* (20 October 2026, version 1) treats an unknown static, shift-invariant **pure** complex-amplitude response. Its local separation-information identity and proposed receivers apply to that shared pure-response model. Appendix G, Eq. (G1), also states the contrasting mixed-response boundary: unrestricted unknown mixed responses can exactly confound distinct separations because binary translation channels commute. It explicitly distinguishes a screen shared across photons from independent copies. These distinctions are already in that paper. The present model restricts mixing to a Gaussian variance family and derives a quantitative, eventually identifiable finite-calibration frontier; it does not overturn the pure-response result or claim to discover the pure/mixed distinction. [Primary record](https://arxiv.org/abs/2610.28089), [inspected PDF mirror, Appendix G, pp. 14–15](https://borowiecki.dev/pdf/2610.28089). `LianZhuCao2026`

Qian's *Parameter-Decoupled Quantum Superresolution without Multiparameter Estimation* (18 September 2026, version 1) announces a projection-channel log-probability invariant that removes unknown brightness imbalance, mutual coherence and relative phase. The accessible primary abstract is enough to establish that nuisance-eliminating measurement invariants and reduction to a separation-only statistic are prior ideas. It does not establish a theorem-level comparison with unknown Gaussian jitter or finite independent calibration. Full text was not retrieved, so no assertion is made that such a result is absent from it. [Primary record](https://arxiv.org/abs/2609.21796). `Qian2026`

## 7. Access limitations and the scope of the comparison

The strongest unresolved full-text comparison is Michael Robert Grace Jr.'s 2022 University of Arizona dissertation, *Quantum Limits and Optimal Receivers for Passive Sub-Diffraction Imaging*. Lvovsky et al.'s 2026 review, Sec. 3.4.1, cites that thesis for quantum-optimal SPADE under fast, zero-mean stochastic misalignment. This makes it a relevant source even though the retrieved review does not specify an unknown-variance calibration frontier. [Thesis record](https://repository.arizona.edu/handle/10150/667290); [review, Sec. 3.4.1](https://arxiv.org/html/2605.10767v1#S3.SS4.SSS1). `Grace2022Thesis`, `LvovskyEtAl2026`

As of 28 October 2026, the thesis's canonical endpoint returned HTTP 403 in this environment. Handle, legacy-repository and metadata-endpoint attempts did not yield its full text. Qian's arXiv abstract was retrievable through the index, but direct PDF/HTML access did not provide the paper. These are access limitations, not evidence that either source lacks a particular theorem. The published 2020 static-offset paper cannot substitute for a full reading of the 2022 thesis's stochastic-noise analysis.

The retrieved sources support the following bounded positioning:

| Ingredient or conclusion | Attribution |
|---|---|
| Gaussian variance can absorb the leading source-separation signature; fixed-noise fourth-order rates | Established mixture-statistics mechanism |
| Quantum moment sensitivity and HG factorial-moment estimators | Established imaging theory |
| Few-mode attainment, quantum minimax methods, and finite-error threshold tests | Established methods and earlier optical constructions |
| Harmonic signal/calibration count | Established two-sample nuisance-information mechanism |
| Noise-induced loss of ideal sensitivity; singular finite-photon failures | Established in several different noise and receiver models |
| Pure-response versus unrestricted mixed-response identifiability | Explicit in the inspected blind-imaging preprint |
| Uniform upper-bound-only jitter/calibration frontier, all-joint-receiver converse, temporary plateau and its calibration dependence | Combined statement established in this project's stated experiment; no earlier proof of the complete statement was identified in the retrieved sources |

This comparison does not support a categorical first-ever claim. It supports a precise model and theorem comparison, with the inaccessible dissertation and preprint remaining visible limitations.
