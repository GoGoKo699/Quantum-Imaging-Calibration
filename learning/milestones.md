# Thirty milestones for quantum imaging calibration

[Repository overview](../README.md) · [Tsang-to-project bridge](tsang-bridge.md) · [Scientific model](../science/model-and-results.md)

This map connects the optical experiment to its uniform resolution frontier. It has **12 background/preliminaries milestones (M01–M12)** and **18 narrative/innovation milestones (M13–M30)**. The background phase builds from one optical amplitude to the full statistical experiment; the narrative phase builds from the confounding mechanism to matching limits, an attaining receiver, and their physical meaning. The allocation reflects the project's combination of optics, quantum discrimination and nuisance statistics.

The single educational anchor is Mankei Tsang, [*Resolving starlight: a quantum perspective*, arXiv:1906.02064v2](https://arxiv.org/pdf/1906.02064v2). Section references below refer to that version. The anchor provides the imaging foundations; the linked project pages supply the unknown-jitter, finite-calibration proofs. Primary research references in those pages retain their separate role as proof dependencies and attribution.

The targets are shared understanding goals for any reader. They describe the project as a connected whole, without attempting to cover every calculation. The [model and results](../science/model-and-results.md) remain the authoritative statements; the [verification guide](../verification/README.md) separates reproducible finite checks from analytical proofs.

| Phase | Milestones | Integration point |
|---|---|---|
| Background/preliminaries | M01–M12 | Specify the experiment, information and fixed-error task together |
| Narrative/innovation | M13–M30 | Explain the matching frontiers, receiver, calibration regimes and scope together |

## Background/preliminaries

### M01 — From an optical amplitude to a photon position

- **Central question:** What does the point-spread function specify about one detected photon?
- **Understanding target:** Distinguish the amplitude from its squared magnitude, identify the known intensity variance $`u`$, and explain why intensity alone does not specify the quantum state.
- **Dependencies and story role:** None; this fixes the local optical object used throughout the map.
- **Conceptual connection:** A translated Gaussian amplitude defines both a position distribution and a state whose spatial-mode overlaps can be measured.
- **Sources:** Tsang V and Appendix B; [optical experiment](../science/model-and-results.md#1-optical-experiment).

### M02 — Two incoherent sources form a mixture

- **Central question:** How does a photon from two equally bright incoherent sources differ from a coherent superposition?
- **Understanding target:** Interpret the equal mixture of translated one-source states at $`-a`$ and $`+a`$, and relate half-separation $`a`$ to physical separation $`s=2a`$.
- **Dependencies and story role:** M01; joins individual source states into the two-source object.
- **Conceptual connection:** Random source identity changes probabilities through an incoherent mixture; the project does not supply a controllable phase between the sources.
- **Sources:** Tsang V and Appendix C, Eq. (C14); [optical experiment](../science/model-and-results.md#1-optical-experiment).

### M03 — Photon counts are charged observations

- **Central question:** What information is supplied by collecting more photons?
- **Understanding target:** Explain independent repetitions, the roles of signal count $`N`$ and calibration count $`M`$, and the distinction between conditioned counts and a parameter-dependent count side channel.
- **Dependencies and story role:** M02; turns the one-photon object into the experiment's resource model.
- **Conceptual connection:** More observations reduce statistical uncertainty, but collecting calibration photons is an additional charged resource. The review's mean Poisson count is translated here into fixed or conditioned detected counts.
- **Sources:** Tsang I, V and Appendix C; [joint input state and count assumptions](../science/model-and-results.md#1-optical-experiment).

### M04 — A measurement chooses the available record

- **Central question:** Why can position detection and mode detection reveal different information about the same light?
- **Understanding target:** Distinguish a quantum state from a measurement outcome distribution, and compare photon positions with spatial-mode labels.
- **Dependencies and story role:** M01–M03; identifies the measurement choice before discussing its performance.
- **Conceptual connection:** Direct imaging is one allowed quantum measurement. Subsequent classical processing can use its full record, but cannot replace a different optical measurement.
- **Sources:** Tsang II, IV–V and Appendix B; [allowed receivers and statistical task](../science/model-and-results.md#2-allowed-receivers-and-statistical-task).

### M05 — Why low Hermite–Gaussian modes respond to small shifts

- **Central question:** What makes a mode sorter sensitive to a small displacement?
- **Understanding target:** Explain the special role of the mode matched to the unshifted Gaussian and why a translated photon can leave that mode even when the image remains visually unresolved.
- **Dependencies and story role:** M01 and M04; supplies the physical basis of the eventual receiver.
- **Conceptual connection:** Gaussian mode overlaps turn the latent displacement into count probabilities. Here $`Q`$ or $`j`$ denotes the mode index; the project's $`q`$ denotes squared separation.
- **Sources:** Tsang IV–V; [conditional HG probabilities](../science/finite-receiver.md#2-exact-outcome-probabilities).

### M06 — Width and shape carry different information

- **Central question:** Why can two distributions agree in width while differing in shape?
- **Understanding target:** Distinguish a second moment from a fourth cumulant and explain how a shape statistic can reveal information hidden from width alone.
- **Dependencies and story role:** M02 and M04; introduces the statistical distinction behind nuisance compensation.
- **Conceptual connection:** Spatial-mode statistics and position moments interrogate features of the same displacement distribution, with different fluctuations.
- **Sources:** Tsang VII.A–B; [broadening and fourth-order shape](../science/interpretation.md#a-separation-can-imitate-additional-blur), [direct-imaging moments](../science/direct-imaging.md#2-three-attainable-tests).

### M07 — Unknown jitter is a distributional nuisance

- **Central question:** What is unknown when every photon undergoes fresh Gaussian jitter?
- **Understanding target:** Distinguish the fixed unknown variance $`v`$ from each independently redrawn translation, and distinguish the supplied bound $`b`$ from the actual normalized variance $`B=v/u`$.
- **Dependencies and story role:** M02–M03 and M06; places the extra broadening inside the optical model.
- **Conceptual connection:** Calibration learns a shared distributional parameter. It does not reveal the signal photons' realized translations; a common displacement or an unknown centroid is a different experiment.
- **Sources:** Tsang VIII.A and VIII.I as related physical context; [optical experiment](../science/model-and-results.md#1-optical-experiment), [scope](../science/quantum-converse.md#7-endpoints-and-scope).

### M08 — A calibrated difference needs both samples

- **Central question:** Why do unlimited calibration photons not replace signal photons?
- **Understanding target:** Explain how independent sample uncertainties add and why $`K=NM/(N+M)`$ is controlled by the smaller budget, with $`K=0`$ at $`M=0`$.
- **Dependencies and story role:** M03 and M07; assembles the two resource streams.
- **Conceptual connection:** The variance of a signal–calibration difference contains both $`1/N`$ and $`1/M`$. The harmonic count expresses their joint bottleneck.
- **Sources:** Tsang V for photon statistics; [effective calibration count](../science/model-and-results.md#3-uniform-resolution-theorem), [calibrated position moments](../science/direct-imaging.md#22-a-calibrated-second-moment-test).

### M09 — Resolution is a fixed-error decision

- **Central question:** What does it mean to resolve one source from two without assuming an unbiased estimator?
- **Understanding target:** State false-positive and false-negative errors, the separated alternative $`h\le q\le q_{\max}`$, and worst-case control over every allowed variance.
- **Dependencies and story role:** M03–M04 and M07; specifies the operational objective.
- **Conceptual connection:** The project asks for uniformly reliable decisions at fixed nonzero error, rather than inferring a boundary from a local estimation formula at a singular point.
- **Sources:** Tsang VIII.J–K and Appendix A; [risk and hypotheses](../science/model-and-results.md#2-allowed-receivers-and-statistical-task).

### M10 — One difficult pair can constrain every receiver

- **Central question:** How can two particular parameter choices limit a composite testing problem?
- **Understanding target:** Explain why any uniformly successful test must distinguish every admissible null–alternative pair, and why small trace distance limits that distinction after arbitrary processing.
- **Dependencies and story role:** M04, M07 and M09; introduces the lower-bound logic.
- **Conceptual connection:** The nuisance must match between signal and calibration within a world, but may differ between the two worlds selected for a converse.
- **Sources:** Tsang II and VIII.K for the detection setting; [pair-to-risk inequality](../science/quantum-converse.md#2-from-a-pair-of-states-to-minimax-risk).

### M11 — A statistic needs a signal and a fluctuation bound

- **Central question:** When does a difference in expected outcomes yield a reliable test?
- **Understanding target:** Relate a statistic's mean gap, variance and decision threshold; distinguish an exact cancellation in expectation from finite-photon error control.
- **Dependencies and story role:** M03, M06 and M09; introduces the upper-bound logic.
- **Conceptual connection:** The attaining tests use explicit moments and concentration bounds. Their guarantees do not require a normal approximation to the count record.
- **Sources:** Tsang V and Appendix A for statistical context; [uniform shape-test variance and errors](../science/finite-receiver.md#3-a-shape-test-with-a-uniform-variance-bound).

### M12 — Assemble the complete experiment

- **Central question:** Which information, resources and success criterion define the theorem?
- **Understanding target:** Specify the known real Gaussian amplitude, centroid and axis; equal incoherent sources; fresh Gaussian jitter; independent matched calibration; counts; receiver classes; and fixed-error risk in one account.
- **Dependencies and story role:** M01–M11; integrates the background phase before the proof narrative begins.
- **Conceptual connection:** The dimensionless parameter $`q=s^2/(4u)`$, the bound $`0\le B\le b`$, and both photon budgets must remain attached to every resolution claim.
- **Sources:** Tsang II–V and VIII.K as the anchor route; [complete model and task](../science/model-and-results.md#1-optical-experiment), [uniform theorem](../science/model-and-results.md#3-uniform-resolution-theorem).

## Narrative/innovation

### M13 — Separation can be hidden inside a variance change

- **Central question:** How can one wandering source resemble two less-wandering sources?
- **Understanding target:** Explain the compensation of the $`a^2`$ contribution to latent variance and why the nuisance interval only permits this comparison when separation is small enough relative to $`b`$.
- **Dependencies and story role:** M06–M07, M10 and M12; isolates the mechanism driving the extra resolution cost.
- **Conceptual connection:** Matching width leaves a fourth-order shape difference. The hard pair is admissible because it changes the common variance of both streams within the alternative world.
- **Sources:** Tsang VII for moment context; [admissible nuisance comparison](../science/quantum-converse.md#5-an-admissible-nuisance-comparison), [physical explanation](../science/interpretation.md#a-separation-can-imitate-additional-blur).

### M14 — The noiseless quantum floor survives calibration

- **Central question:** Why is there always a $`q\asymp N^{-1}`$ obstruction?
- **Understanding target:** Connect the one-photon overlap to the product-state fidelity $`e^{-Nq/4}`$, and explain why an identical calibration factor cannot distinguish the selected pair.
- **Dependencies and story role:** M02–M03, M10 and M12; establishes the first quantum lower branch independently of a positive jitter reference.
- **Conceptual connection:** Contractive processing preserves this obstruction. At $`b=0`$ it supplies the converse without applying an inverse to a pure state.
- **Sources:** Tsang IV–V and VIII.K for the ideal imaging setting; [pure-state obstruction](../science/quantum-converse.md#3-pure-state-obstruction).

### M15 — A faithful reference still needs a domain argument

- **Central question:** Why is a formal Gaussian inverse insufficient in an infinite-dimensional proof?
- **Understanding target:** Distinguish faithfulness from a bounded inverse, and explain the role of the weighted vectors $`\tau_v^{-1/4}|\psi_x\rangle`$ and their trace-class mixture for $`v>0`$.
- **Dependencies and story role:** M01, M10 and M13; identifies the mathematical foundation required before using collision distances.
- **Conceptual connection:** The squeezed thermal decomposition and integrability argument make the weighted comparison legitimate. The pure endpoint retains its separate argument from M14.
- **Sources:** Tsang Appendix B for state/measurement context; project-supplied [thermal decomposition](../science/collision-kernel.md#2-squeezed-thermal-decomposition), [inverse-quarter-root domain](../science/collision-kernel.md#3-domain-of-the-inverse-quarter-root) and [trace-class construction](../science/collision-kernel.md#4-weighted-gaussian-mixtures-are-trace-class).

### M16 — Exact collisions convert local states into a full-record bound

- **Central question:** How does the Gaussian calculation control an arbitrary joint measurement?
- **Understanding target:** Explain the chosen sandwiched collision weighting, its exact Gaussian integral, the trace-distance inequality and the product identity for independent photons.
- **Dependencies and story role:** M03, M10 and M15; joins the justified one-photon calculation to the complete quantum record.
- **Conceptual connection:** One plus the collision quantity multiplies under products, so $`\log(1+\chi^2_{1/2})`$ accumulates with the charged signal and calibration counts. Other quantum chi-square conventions cannot be substituted without proof.
- **Sources:** Tsang II for the universal-measurement question; [exact Gaussian identities](../science/collision-kernel.md#5-gaussian-integration), [collision tools and product identity](../science/quantum-converse.md#4-collision-tools-with-infinite-dimensional-justification).

### M17 — Balance the compensation against calibration

- **Central question:** Why does partial variance matching produce the harmonic count in the converse?
- **Understanding target:** Explain the choice $`\omega=N/(N+M)`$, the identity $`N(1-\omega)^2+M\omega^2=K`$, and the residual fourth-order signal cost.
- **Dependencies and story role:** M08, M13 and M16; identifies the competition between calibration information and shape information.
- **Conceptual connection:** Their joint collision exponent is bounded by terms of orders $`Kq^2/b`$ and $`Nq^4/b^2`$ on the admissible positive-noise hard pair. At $`M=0`$, the quadratic term vanishes.
- **Sources:** Tsang VII for moment context; [uniform variance-matching bounds](../science/collision-kernel.md#6-uniform-bounds-and-variance-matching), [balanced nuisance pair](../science/quantum-converse.md#5-an-admissible-nuisance-comparison).

### M18 — Make the quantum converse uniform

- **Central question:** How do the pure and nuisance branches yield one bound even when the noise bound shrinks?
- **Understanding target:** Explain why $`L=\max\{\sqrt N,K\}`$ and the admissibility cap give $`R_Q=N^{-1}+\min\{b,\sqrt{b/L}\}`$, with constants independent of $`N,M,b,u`$.
- **Dependencies and story role:** M12, M14 and M17; integrates the lower-bound half of the quantum theorem.
- **Conceptual connection:** The difficult point must belong to the separated alternative, including its local cutoff. The proof treats $`b=0`$ and $`M=0`$ explicitly rather than dividing by a vanishing quantity.
- **Sources:** Tsang VIII.J–K for worst-case detection context; [uniform phase lower bound](../science/quantum-converse.md#6-uniform-phase-lower-bound), [endpoints](../science/quantum-converse.md#7-endpoints-and-scope).

### M19 — Keep four outcomes and count every photon

- **Central question:** What finite apparatus can attain the quantum order?
- **Understanding target:** Describe HG0, HG1, HG2 and the orthogonal remainder, the fixed basis matched to the known pure amplitude, and the exact signal/calibration probabilities.
- **Dependencies and story role:** M05, M07 and M12; begins the constructive half of the narrative.
- **Conceptual connection:** The outcome probabilities arise by averaging the conditional HG law over jitter and source identity. The remainder is an observed category, so the construction does not gain apparent sensitivity through postselection.
- **Sources:** Tsang V and VII; [scope and apparatus](../science/finite-receiver.md#1-scope-and-claim), [exact probabilities](../science/finite-receiver.md#2-exact-outcome-probabilities).

### M20 — Remove the nuisance from the null mean

- **Central question:** What combination of three mode probabilities distinguishes separation from Gaussian jitter?
- **Understanding target:** Explain the exact invariant $`\theta=p_0p_2-\tfrac32p_1^2=-p_0^2q^2/(2+B)^4`$: its null value is zero for every allowed $`B`$, while it is negative at every nonzero $`q`$.
- **Dependencies and story role:** M06, M13 and M19; turns the shape distinction into an observable construction.
- **Conceptual connection:** The $`B^2`$ and $`Bq`$ terms cancel. The remaining scale is quadratic in $`q`$; cancellation of a nuisance-dependent mean does not eliminate statistical fluctuations.
- **Sources:** Tsang VII for the mode/moment connection; [exact invariant and uniform constants](../science/finite-receiver.md#2-exact-outcome-probabilities).

### M21 — Estimate the invariant without finite-sample bias

- **Central question:** Why does the count formula use $`n_1(n_1-1)`$ rather than $`n_1^2`$?
- **Understanding target:** Interpret the unbiased pair statistic and relate its full variance bound to the shape-test threshold $`N^{-1/2}+\sqrt b\,N^{-1/4}`$.
- **Dependencies and story role:** M03, M11 and M20; converts the exact probability identity into a finite-photon test.
- **Conceptual connection:** Pair counting removes the empirical-square bias. The error bound covers every $`q\ge h`$ in the alternative, including finite samples and the degenerate zero-jitter null.
- **Sources:** Tsang VIII.J and Appendix A for finite-sample statistical context; [unbiased statistic, variance and errors](../science/finite-receiver.md#3-a-shape-test-with-a-uniform-variance-bound).

### M22 — Calibration reveals a lower-order signal

- **Central question:** How can the HG0 event use a calibration source to reveal separation?
- **Understanding target:** Explain the difference between signal and calibration excitation frequencies, its mean proportional to $`q`$ on the bounded domain, and the threshold $`N^{-1}+\sqrt{b/K}`$.
- **Dependencies and story role:** M08, M11 and M19; supplies the attaining calibration branch.
- **Conceptual connection:** A matched calibration sample cancels common broadening in a difference statistic. Its variance still includes both samples; the branch is unavailable at $`M=0`$.
- **Sources:** Tsang V for mode-count statistics; [zero-mode calibration test](../science/finite-receiver.md#4-a-calibration-test-using-only-the-zero-mode-event).

### M23 — Use the supplied variance band directly

- **Central question:** When is a known noise bound already sufficient to resolve two sources?
- **Understanding target:** Explain the excitation threshold that exceeds every allowed null mean, giving order $`b+N^{-1}`$, and the exact no-jitter test based on any departure from HG0.
- **Dependencies and story role:** M07, M11 and M19; supplies the branch that protects the weak-noise corner.
- **Conceptual connection:** The apparatus need not estimate the true variance to exploit an upper bound. At $`b=0`$, the null never leaves HG0 and the miss probability is exactly $`e^{-Nq/4}`$.
- **Sources:** Tsang V and VIII.K for ideal mode detection; [known-bound test and noiseless endpoint](../science/finite-receiver.md#5-a-test-using-the-known-variance-upper-bound).

### M24 — Match the quantum converse with one fixed receiver

- **Central question:** How do three classical decisions on the same type of optical record attain the uniform frontier?
- **Understanding target:** Explain selection of the smallest certified threshold using only $`N,M,b`$, and why the resulting upper scale matches M18.
- **Dependencies and story role:** M18 and M21–M23; integrates the complete quantum result.
- **Conceptual connection:** Optical outcomes remain fixed while the classical branch depends on supplied resources. This proves order-optimal attainment without a nuisance-dependent basis, a preliminary variance estimate or a necessity claim about four outcomes.
- **Sources:** Tsang IV–V for measurement attainment; [branch combination](../science/finite-receiver.md#6-combining-the-branches), [uniform theorem](../science/model-and-results.md#3-uniform-resolution-theorem).

### M25 — Construct the direct-imaging comparison

- **Central question:** What do the corresponding position-data tests retain and lose?
- **Understanding target:** Explain the unbiased fourth-cumulant test, the calibrated second-moment test and the known-bound second-moment test, with thresholds of orders $`N^{-1/4}`$, $`K^{-1/2}`$ and $`b+N^{-1/2}`$ in $`q`$.
- **Dependencies and story role:** M04, M06, M08 and M11; builds an attainable classical comparison using the same physical resources.
- **Conceptual connection:** Position observations retain the nonzero optical variance even at zero jitter. Their shape statistic also has a mean quadratic in $`q`$, but its fluctuations differ from those of the mode statistic.
- **Sources:** Tsang III and VII.A–B; [three direct-imaging tests](../science/direct-imaging.md#2-three-attainable-tests).

### M26 — Match the direct-imaging lower bound

- **Central question:** Why can no more elaborate processing of position data beat the stated classical order?
- **Understanding target:** Combine the diffraction baseline and the matched-nuisance collision comparison to explain $`R_{\mathrm{DI}}=N^{-1/2}+\min\{b,L^{-1/2}\}`$.
- **Dependencies and story role:** M10, M13, M17 and M25; completes the matched measurement-class comparison.
- **Conceptual connection:** The classical collision exponent has terms of orders $`Kq^2`$ and $`Nq^4`$. The position-variance baseline removes the weak-jitter denominator responsible for the quantum moment advantage.
- **Sources:** Tsang III and VIII.J–K for classical limitations; [testing inequality](../science/direct-imaging.md#3-a-testing-inequality-with-a-strict-error-margin), [diffraction baseline](../science/direct-imaging.md#4-the-diffraction-baseline), [nuisance lower branch](../science/direct-imaging.md#6-the-nuisance-lower-branch-and-the-full-converse).

### M27 — Read the plateaus and changing relative advantage

- **Central question:** How can quantum advantage close and return as more signal photons arrive?
- **Understanding target:** At fixed small $`b`$ and $`M=0`$, locate the quantum crossovers near $`b^{-1}`$ and $`b^{-2}`$, the later direct-imaging plateau, and the closing-advantage window near $`N\asymp b^{-2}`$.
- **Dependencies and story role:** M24 and M26; translates the two frontiers into physical regimes.
- **Conceptual connection:** A plateau in matching orders is temporary. Extra photons can be ignored, so optimal absolute resolution cannot worsen when the budget increases; relative advantage and absolute performance are different comparisons.
- **Sources:** Tsang III–V as baseline context; [three quantum regimes](../science/interpretation.md#three-quantum-regimes), [signal-count plateaus](../science/interpretation.md#a-temporary-plateau-as-signal-photons-accumulate).

### M28 — Charge the calibration that changes a regime

- **Central question:** How much calibration is needed for a parametrically smaller resolution?
- **Understanding target:** Compare calibration with both shape information and the known variance band; distinguish crossover counts from strict improvements, finite $`M`$ from $`M\asymp N`$, and saturation when $`M\gg N`$.
- **Dependencies and story role:** M08, M22 and M27; connects the resource theorem to experimental budgeting.
- **Conceptual connection:** Useful parametric improvement requires the relevant $`K\gg\sqrt N`$ and $`K\gg b^{-1}`$ comparisons when the noiseless floor does not dominate. A finite calibration budget is not a permanent resolution floor because signal shape information continues improving.
- **Sources:** Tsang I and V for photon-resource context; [calibration regimes](../science/interpretation.md#how-much-calibration-is-useful), [closing-boundary example](../science/interpretation.md#a-scaling-example-at-the-closing-advantage-boundary).

### M29 — Separate the contribution, evidence and boundaries

- **Central question:** Which part is established by this project, and which ingredients or comparisons remain external?
- **Understanding target:** Credit inherited mode, moment, mixture and discrimination methods; identify the combined uniform frontier; distinguish analytical proof, deterministic finite checks, engineering assumptions and unresolved full-text comparisons.
- **Dependencies and story role:** M18, M24, M26 and M28; evaluates the complete scientific account before its final synthesis.
- **Conceptual connection:** Numerical agreement supports checked identities, not infinite-dimensional uniformity or priority. Known centroid, real Gaussian amplitude, independent jitter and matched calibration are consequential hypotheses.
- **Sources:** Tsang VIII.A for an adjacent model boundary; [attribution and scope](../science/model-and-results.md#5-attribution-and-scope), [related-work access limits](../references/related-work.md#7-access-limitations-and-the-scope-of-the-comparison), [verification scope](../verification/README.md#what-remains-analytical).

### M30 — Reconstruct the resolution frontier as one story

- **Central question:** Why do these assumptions, resources and measurements lead to these two resolution laws?
- **Understanding target:** Explain the complete path from width confounding through a universal hard-pair bound and finite receiver to the direct-imaging comparison, temporary plateau and calibration-dependent recovery of advantage.
- **Dependencies and story role:** M12, M18, M24 and M26–M29; integrates the narrative phase and the project as a whole.
- **Conceptual connection:** Keep $`q=s^2/(4u)`$ distinct from physical separation, take square roots when translating exponents, and state matching uniform orders with fixed-error and nonempty-alternative qualifications. The result is an operational frontier within the specified experiment.
- **Sources:** Tsang II–V, VII and VIII.J–K as the educational foundation; [complete theorem](../science/model-and-results.md#3-uniform-resolution-theorem), [physical interpretation](../science/interpretation.md), [scope](../science/model-and-results.md#5-attribution-and-scope).
