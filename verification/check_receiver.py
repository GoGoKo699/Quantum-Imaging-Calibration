#!/usr/bin/env python3
"""Verify the four-outcome HG receiver and its finite-sample statistics.

Default: run independent checks and compare with expected/check_receiver.json.
Use --record to refresh that file after the independent checks have passed.
No random sampling is used.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path
from typing import Any

from scipy.integrate import quad

EXPECTED = Path(__file__).resolve().parent / "expected" / "check_receiver.json"
NS = (2, 3, 7)
BS = (0.0, 1e-4, 0.1, 1.0, 3.0)
QS = (0.0, 1e-4, 0.1, 1.0)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def close(actual: float, expected: float, label: str,
          *, atol: float = 5e-12, rtol: float = 2e-10) -> None:
    require(math.isfinite(actual) and math.isfinite(expected),
            f"{label}: nonfinite value")
    require(math.isclose(actual, expected, abs_tol=atol, rel_tol=rtol),
            f"{label}: {actual!r} != {expected!r}")


def compare_json(actual: Any, expected: Any, path: str = "$") -> None:
    if isinstance(actual, dict):
        require(isinstance(expected, dict) and actual.keys() == expected.keys(),
                f"{path}: object keys differ")
        for key in actual:
            compare_json(actual[key], expected[key], f"{path}.{key}")
    elif isinstance(actual, list):
        require(isinstance(expected, list) and len(actual) == len(expected),
                f"{path}: list length differs")
        for index, (value, reference) in enumerate(zip(actual, expected)):
            compare_json(value, reference, f"{path}[{index}]")
    elif isinstance(actual, (int, float)) and not isinstance(actual, bool):
        require(isinstance(expected, (int, float)), f"{path}: expected a number")
        close(float(actual), float(expected), path)
    else:
        require(actual == expected, f"{path}: value differs")


def probabilities(b: float, q: float) -> list[float]:
    d = 2.0 + b
    p0 = (1.0 + b / 2.0) ** -0.5 * math.exp(-q / (2.0 * d))
    p1 = p0 * (b / (2.0 * d) + q / d**2)
    p2 = p0 * (3.0 * b**2 / (8.0 * d**2)
               + 3.0 * b * q / (2.0 * d**3)
               + q**2 / (2.0 * d**4))
    rest = 1.0 - p0 - p1 - p2
    require(rest >= -1e-14, "negative remainder probability")
    return [p0, p1, p2, max(0.0, rest)]


def probability_by_quadrature(b: float, q: float, mode: int) -> float:
    """Integrate the conditional Poisson probability against latent jitter."""
    if b == 0.0:
        return math.exp(-q / 4.0) * (q / 4.0)**mode / math.factorial(mode)
    a = math.sqrt(q)

    def integrand(z: float) -> float:
        lam = (a + math.sqrt(b) * z)**2 / 4.0
        return (math.exp(-z*z/2.0 - lam) * lam**mode
                / (math.sqrt(2.0*math.pi) * math.factorial(mode)))

    value, _ = quad(integrand, -12.0, 12.0, epsabs=1e-13, epsrel=1e-13)
    return value


def enumerate_counts(p: list[float], n: int) -> tuple[float, float, float]:
    """Independently enumerate the full four-category multinomial experiment."""
    probabilities_terms = []
    mean_terms = []
    second_terms = []
    for n0 in range(n + 1):
        for n1 in range(n - n0 + 1):
            for n2 in range(n - n0 - n1 + 1):
                counts = (n0, n1, n2, n - n0 - n1 - n2)
                coefficient = math.factorial(n) // math.prod(
                    math.factorial(k) for k in counts)
                probability = coefficient * math.prod(
                    pi**count for pi, count in zip(p, counts))
                statistic = (n0*n2 - 1.5*n1*(n1-1)) / (n*(n-1))
                probabilities_terms.append(probability)
                mean_terms.append(probability * statistic)
                second_terms.append(probability * statistic**2)
    mass = math.fsum(probabilities_terms)
    mean = math.fsum(mean_terms)
    variance = math.fsum(second_terms) - mean**2
    return mass, mean, variance


def branch_check() -> dict[str, Any]:
    """Check the exact algebraic reduction, including b=0 and M=0."""
    count = 0
    ratios = []
    for n in (2, 10, 100, 1_000_000):
        for m in (0, 1, 10, n, 10*n):
            k = n*m/(n+m)
            ell = max(math.sqrt(n), k)
            for b in (0.0, 1e-8, 1e-3, 0.1, 1.0):
                shape = n**-0.5 + math.sqrt(b)*n**-0.25
                calibrated = n**-1 + math.sqrt(b/k) if m else math.inf
                bound = n**-1 + b
                best = min(shape, calibrated, bound)
                rate = n**-1 + min(b, math.sqrt(b/ell))
                require(rate > 0 and math.isfinite(best), "invalid endpoint rate")
                require(best >= rate*(1-1e-13), "branch below combined rate")
                require(best <= 2*rate*(1+1e-13), "branch exceeds twice rate")
                ratios.append(best/rate)
                count += 1
    return {"grid_cases": count, "minimum_ratio": min(ratios),
            "maximum_ratio": max(ratios)}


def run_checks() -> tuple[dict[str, Any], dict[str, Any]]:
    records = []
    probability_errors = []
    invariant_errors = []
    mean_errors = []
    variance_errors = []
    variance_ratios = []
    for b, q in itertools.product(BS, QS):
        p = probabilities(b, q)
        p0, p1, p2, _ = p
        close(math.fsum(p), 1.0, "probability normalization")
        for mode in range(3):
            numerical = probability_by_quadrature(b, q, mode)
            close(numerical, p[mode], f"quadrature b={b},q={q},mode={mode}")
            probability_errors.append(abs(numerical-p[mode]))
        theta = -p0**2*q**2/(2.0+b)**4
        raw_invariant = p0*p2 - 1.5*p1**2
        close(raw_invariant, theta, f"invariant b={b},q={q}")
        invariant_errors.append(abs(raw_invariant-theta))

        eh1sq = 0.25*p0*p2**2 + 0.25*p0**2*p2 + 2.25*p1**3
        ehsq = 0.5*p0*p2 + 2.25*p1**2
        t = b+q
        require(p1 <= t/4.0 + 1e-14, "p1 elementary bound")
        require(p2 <= 3*t*t/32.0 + 1e-14, "p2 elementary bound")
        require(ehsq <= 3*t*t/16.0 + 1e-14, "kernel second-moment bound")

        sample_rows = []
        for n in NS:
            mass, mean, variance = enumerate_counts(p, n)
            predicted = (4*(n-2)*(eh1sq-theta**2)
                         + 2*(ehsq-theta**2))/(n*(n-1))
            close(mass, 1.0, "multinomial normalization")
            close(mean, theta, f"unbiased mean b={b},q={q},N={n}")
            close(variance, predicted, f"variance b={b},q={q},N={n}")
            require(variance <= 3*t*t/(4*n) + 1e-13,
                    "uniform U-statistic variance bound")
            if t:
                variance_ratios.append(variance*n/(t*t))
            else:
                close(variance, 0.0, "degenerate all-HG0 variance", atol=0, rtol=0)
            mean_errors.append(abs(mean-theta))
            variance_errors.append(abs(variance-predicted))
            sample_rows.append({"N": n, "mean": mean, "variance": variance})
        records.append({"B": b, "q": q, "probabilities": p,
                        "theta": theta, "multinomial": sample_rows})

    # Exact noiseless single-excitation test, with no calibration required.
    endpoint = []
    for n, q in ((2, 0.1), (100, 0.01), (1000, 0.001)):
        error = probabilities(0.0, q)[0]**n
        exact = math.exp(-n*q/4.0)
        close(error, exact, "noiseless type-II error")
        endpoint.append({"N": n, "q": q, "type_I": 0.0, "type_II": exact})

    payload = {"schema_version": 1, "cases": records,
               "noiseless_test": endpoint, "branch_reduction": branch_check()}
    diagnostics = {
        "parameter_cases": len(records),
        "multinomial_cases": len(records)*len(NS),
        "maximum_probability_quadrature_error": max(probability_errors),
        "maximum_invariant_error": max(invariant_errors),
        "maximum_mean_error": max(mean_errors),
        "maximum_variance_error": max(variance_errors),
        "maximum_variance_N_over_B_plus_q_squared": max(variance_ratios),
        "proved_variance_ratio_bound": 0.75,
        "branch_grid_cases": payload["branch_reduction"]["grid_cases"],
    }
    return payload, diagnostics


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", action="store_true",
                        help="refresh expected JSON after independent checks pass")
    args = parser.parse_args()
    payload, diagnostics = run_checks()
    if args.record:
        EXPECTED.parent.mkdir(parents=True, exist_ok=True)
        EXPECTED.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        status = "recorded"
    else:
        if not EXPECTED.exists():
            raise SystemExit(f"Missing expected file: {EXPECTED}. "
                             "Use --record only to intentionally create it.")
        compare_json(payload, json.loads(EXPECTED.read_text()))
        status = "passed"
    print(json.dumps({"status": status, **diagnostics}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

