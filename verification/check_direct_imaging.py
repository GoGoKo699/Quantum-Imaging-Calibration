#!/usr/bin/env python3
"""Verify direct-imaging collision identities and unbiased moment statistics.

Default: run independent checks and compare with expected/check_direct_imaging.json.
Use --record to refresh that file after all independent checks pass.
The calculations are deterministic and do not use Monte Carlo.
"""
from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
import itertools
import json
import math
from pathlib import Path
from typing import Any

import numpy as np
from scipy.integrate import quad

EXPECTED = Path(__file__).resolve().parent / "expected" / "check_direct_imaging.json"


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


def collision(t: Decimal | str, w: Decimal | str) -> tuple[Decimal, Decimal]:
    """Return signal and calibration chi-square, using 80-digit arithmetic."""
    with localcontext() as ctx:
        ctx.prec = 80
        t, w = Decimal(t), Decimal(w)
        denominator = (1-w*w*t*t).sqrt()
        signal = ((t/(1+w*t)).exp() + (-t/(1-w*t)).exp()) / (2*denominator) - 1
        calibration = 1/denominator - 1
        return +signal, +calibration


def gaussian_density(x: float, mean: float, variance: float) -> float:
    return math.exp(-(x-mean)**2/(2*variance))/math.sqrt(2*math.pi*variance)


def collision_by_quadrature(s0: float, q: float, w: float,
                            *, calibration: bool) -> float:
    s1 = s0-w*q
    require(s1 > 0, "nonpositive alternative variance")
    a = 0.0 if calibration else math.sqrt(q)

    def integrand(z: float) -> float:
        y = math.sqrt(s0)*z
        reference = gaussian_density(y, 0.0, s0)
        alternative = 0.5*(gaussian_density(y, a, s1)
                           + gaussian_density(y, -a, s1))
        return ((alternative-reference)**2/reference)*math.sqrt(s0)

    value, _ = quad(integrand, -12.0, 12.0, epsabs=1e-13, epsrel=1e-11)
    return value


def even_moment(b: float, q: float, order: int) -> float:
    """Exact polynomial moment of sqrt(1+B) G + sqrt(q) S."""
    terms = []
    for k in range(order+1):
        normal_moment = math.factorial(2*k)/(2**k*math.factorial(k))
        terms.append(math.comb(2*order, 2*k)*normal_moment
                     *(1+b)**k*q**(order-k))
    return math.fsum(terms)


def moment_by_quadrature(b: float, q: float, order: int) -> float:
    # Even functions have the same average for either sign of sqrt(q).
    def integrand(z: float) -> float:
        y = math.sqrt(1+b)*z+math.sqrt(q)
        return y**(2*order)*math.exp(-z*z/2)/math.sqrt(2*math.pi)
    value, _ = quad(integrand, -12.0, 12.0, epsabs=1e-10, epsrel=2e-13)
    return value


def run_checks() -> tuple[dict[str, Any], dict[str, Any]]:
    collision_rows = []
    collision_errors = []
    for s0, q, w in ((1.0, 0.04, 0.0), (1.5, 0.04, 1.0),
                     (1.5, 0.25, 0.35), (2.0, 0.5, 0.8)):
        with localcontext() as ctx:
            ctx.prec = 80
            t = Decimal(str(q))/Decimal(str(s0))
            signal, calibration = collision(t, Decimal(str(w)))
        for name, exact, is_calibration in (
                ("signal", signal, False), ("calibration", calibration, True)):
            numerical = collision_by_quadrature(s0, q, w, calibration=is_calibration)
            close(numerical, float(exact), f"{name} collision quadrature")
            collision_errors.append(abs(numerical-float(exact)))
        collision_rows.append({"s0": s0, "q": q, "w": w,
                               "signal_chi2": float(signal),
                               "calibration_chi2": float(calibration)})

    endpoints = []
    with localcontext() as ctx:
        ctx.prec = 80
        for value in ("0.1", "0.03", "0.01", "0.003", "0.001", "0.00001"):
            t = Decimal(value)
            matched, _ = collision(t, "1")
            known, _ = collision(t, "0")
            endpoints.append({
                "t": value,
                "matched_chi2_over_t4": float(matched/t**4),
                "known_chi2_over_t2": float(known/t**2)})
        close(endpoints[-1]["matched_chi2_over_t4"], 1/6,
              "matched-variance coefficient", atol=2e-9)
        close(endpoints[-1]["known_chi2_over_t2"], 0.5,
              "known-variance coefficient", atol=2e-9)
        for w in ("0", "0.25", "0.5", "0.75", "1"):
            t = Decimal("0.00001")
            value, _ = collision(t, w)
            coefficient = (1-Decimal(w))**2/2
            close(float(value/t**2), float(coefficient),
                  "uniform quadratic coefficient", atol=2e-9)

    harmonic_rows = []
    for n, m in ((100, 0), (100, 1), (100, 10), (100, 100), (100, 10000)):
        w = n/(n+m)
        k = n*m/(n+m)
        quadratic = n*(1-w)**2+m*w*w
        close(quadratic, k, "harmonic count")
        harmonic_rows.append({"N": n, "M": m, "K": k, "quadratic_form": quadratic})

    # Independent Gaussian integration of kernel squares.
    nodes, weights = np.polynomial.hermite.hermgauss(12)
    normal_nodes = np.sqrt(2.0)*nodes
    normal_weights = weights/math.sqrt(math.pi)
    moment_rows = []
    moment_errors = []
    kernel_errors = []
    variance_errors = []
    for b, q in itertools.product((0.0, 0.1, 1.0), (0.0, 0.1, 1.0)):
        moments = [even_moment(b, q, order) for order in range(1, 5)]
        for order, exact in enumerate(moments, 1):
            numerical = moment_by_quadrature(b, q, order)
            close(numerical, exact, "Gaussian-mixture moment", atol=2e-9)
            moment_errors.append(abs(numerical-exact))
        m2, m4, m6, m8 = moments
        theta = m4-3*m2*m2
        close(theta, -2*q*q, "fourth cumulant")
        eh1sq = 0.25*m8-3*m2*m6+6*m2*m2*m4+0.75*m4*m4
        ehsq = 0.5*m8+9.5*m4*m4-6*m2*m6

        y = math.sqrt(1+b)*normal_nodes+math.sqrt(q)
        h1 = 0.5*(y**4+m4)-3*m2*y*y
        h = 0.5*(y[:, None]**4+y[None, :]**4)-3*y[:, None]**2*y[None, :]**2
        numerical_eh1sq = float(np.dot(normal_weights, h1*h1))
        numerical_ehsq = float(np.sum(normal_weights[:, None]
                                      *normal_weights[None, :]*h*h))
        close(numerical_eh1sq, eh1sq, "conditional kernel square", atol=2e-9)
        close(numerical_ehsq, ehsq, "full kernel square", atol=2e-9)
        kernel_errors.extend((abs(numerical_eh1sq-eh1sq), abs(numerical_ehsq-ehsq)))

        t = 1+b+q
        require(ehsq <= 138*t**4+1e-8, "kernel moment bound")
        variances = []
        for n in (2, 3, 7):
            exact_var = (4*(n-2)*(eh1sq-theta**2)
                         + 2*(ehsq-theta**2))/(n*(n-1))
            integrated_var = (4*(n-2)*(numerical_eh1sq-theta**2)
                              + 2*(numerical_ehsq-theta**2))/(n*(n-1))
            close(integrated_var, exact_var, "U-statistic variance", atol=2e-9)
            variance_errors.append(abs(integrated_var-exact_var))
            require(exact_var <= 552*t**4/n+1e-8, "uniform cumulant variance bound")
            if q == 0:
                null_var = 24*(n+2)*(1+b)**4/(n*(n-1))
                close(exact_var, null_var, "exact null variance")
            variances.append({"N": n, "variance": exact_var})
        moment_rows.append({"B": b, "q": q, "even_moments_2_4_6_8": moments,
                            "fourth_cumulant": theta, "variances": variances})

    branch_ratios = []
    for n in (2, 10, 100, 1_000_000):
        for m in (0, 1, 10, n, 10*n):
            k = n*m/(n+m)
            ell = max(math.sqrt(n), k)
            for b in (0.0, 1e-8, 1e-3, 0.1, 1.0):
                best = min(n**-0.25, k**-0.5 if m else math.inf, b+n**-0.5)
                rate = n**-0.5+min(b, ell**-0.5)
                require(best <= rate*(1+1e-13), "upper branch reduction")
                require(rate <= 2*best*(1+1e-13), "lower branch reduction")
                branch_ratios.append(best/rate)

    payload = {"schema_version": 1, "collision_integrals": collision_rows,
               "endpoint_coefficients": endpoints, "harmonic_count": harmonic_rows,
               "moment_statistics": moment_rows,
               "branch_reduction": {"grid_cases": len(branch_ratios),
                                    "minimum_ratio": min(branch_ratios),
                                    "maximum_ratio": max(branch_ratios)}}
    diagnostics = {
        "collision_integral_checks": 2*len(collision_rows),
        "maximum_collision_quadrature_error": max(collision_errors),
        "moment_parameter_cases": len(moment_rows),
        "maximum_even_moment_quadrature_error": max(moment_errors),
        "maximum_kernel_square_error": max(kernel_errors),
        "maximum_U_variance_error": max(variance_errors),
        "branch_grid_cases": len(branch_ratios),
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

