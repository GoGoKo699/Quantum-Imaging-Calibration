#!/usr/bin/env python3
"""Check the Gaussian collision identity using a squeezed oscillator basis.

Default: calculate the checks, enforce analytic-comparison tolerances, and
compare with the committed expected/check_collision.json.  Use --record only
to replace that reference after reviewing a deliberate numerical change.

Dependencies: Python 3.11+ and NumPy.  No random samples, network, or SciPy.
"""

from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
import json
from pathlib import Path

import numpy as np


EXPECTED = Path(__file__).resolve().parent / "expected" / "check_collision.json"
KERNEL_RTOL = 2e-12
COLLISION_RTOL = 2e-9  # Includes a variance-matched divergence below 1e-15.
COLLISION_ATOL = 1e-25
ZERO_COLLISION_ATOL = 1e-18  # High-variance quadrature has a small absolute floor.


def close(actual: float, expected: float, *, rtol: float, atol: float, label: str) -> None:
    if not (np.isfinite(actual) and np.isfinite(expected)) or abs(actual - expected) > atol + rtol * abs(expected):
        raise AssertionError(
            f"{label}: actual={actual:.17g}, expected={expected:.17g}, "
            f"absolute error={abs(actual - expected):.3g}"
        )


def thermal_parameters(u: float, v: float) -> tuple[float, float]:
    if u <= 0 or v <= 0:
        raise ValueError("The collision reference requires u>0 and v>0.")
    t = np.sqrt(1 + v / u)
    # Algebraically (t-1)/(t+1), evaluated without small-v cancellation.
    r = (v / u) / (t + 1) ** 2
    return u * t, r


def weighted_coefficients(x: float, u: float, v: float, levels: int) -> np.ndarray:
    """<n_w|psi_x>/lambda_n(tau_v)^(1/4), from a three-term recurrence."""
    w, r = thermal_parameters(u, v)
    result = np.empty(levels)
    result[0] = (1 + r) ** 0.25 * np.exp(-x * x / (4 * (u + w)))
    if levels > 1:
        alpha = np.sqrt(w) * x / ((u + w) * r ** 0.25)
        result[1] = alpha * result[0]
        for n in range(2, levels):
            result[n] = (
                alpha / np.sqrt(n) * result[n - 1]
                - np.sqrt(r * (n - 1) / n) * result[n - 2]
            )
    return result


def kernel_formula(x: float, y: float, u: float, v: float) -> float:
    return float(np.sqrt(1 + v / u) * np.exp(
        -(x * x + y * y) / (2 * u) + np.sqrt((u + v) / v) * x * y / u
    ))


def weighted_state(
    u: float, v: float, a2: float, omega: float, *, signal: bool,
    levels: int = 80, nodes: int = 80,
) -> np.ndarray:
    """Integrate weighted rank-one states, without using the closed kernel."""
    variance = v - omega * a2
    if variance < -1e-14 * max(v, a2):
        raise ValueError("Alternative variance must be nonnegative.")
    variance = max(0.0, variance)
    means = (-np.sqrt(a2), np.sqrt(a2)) if signal else (0.0,)
    if variance == 0:
        positions, weights = np.array([0.0]), np.array([1.0])
    else:
        nodes_x, weights = np.polynomial.hermite.hermgauss(nodes)
        positions = np.sqrt(2 * variance) * nodes_x
        weights = weights / np.sqrt(np.pi)
    result = np.zeros((levels, levels))
    for mean in means:
        for x, weight in zip(positions + mean, weights):
            coeff = weighted_coefficients(float(x), u, v, levels)
            result += (weight / len(means)) * np.outer(coeff, coeff)
    return result


def reference_root(u: float, v: float, levels: int) -> np.ndarray:
    _, r = thermal_parameters(u, v)
    return np.diag(np.sqrt((1 - r) * r ** np.arange(levels)))


def collision_formula(u: float, v: float, a2: float, omega: float) -> tuple[float, float, float]:
    """70-digit scalar calculation avoids subtractive cancellation at z=0."""
    with localcontext() as ctx:
        ctx.prec = 70
        du, dv, da2, dw = (Decimal(str(x)) for x in (u, v, a2, omega))
        z = da2 / (dv * (du + dv)).sqrt()
        den = (1 - dw * dw * z * z).sqrt()
        signal = ((z / (1 + dw * z)).exp() + (-z / (1 - dw * z)).exp()) / (2 * den) - 1
        calibration = 1 / den - 1
        return float(signal), float(calibration), float(z)


def run_checks() -> dict:
    parameters = [(1.0, 1e-6), (1.0, .01), (1.0, .1),
                  (1.0, 1.0), (1.0, 10.0), (3.0, .2)]
    rows: list[dict] = []
    for u, v in parameters:
        for coordinate_id, (cx, cy) in enumerate([(0, 0), (.2, -.7), (.8, .5)]):
            x, y = cx * np.sqrt(v), cy * np.sqrt(v)
            actual = float(np.dot(weighted_coefficients(x, u, v, 200),
                                  weighted_coefficients(y, u, v, 200)) ** 2)
            exact = kernel_formula(x, y, u, v)
            label = f"kernel:u={u}:v={v}:coordinates={coordinate_id}"
            close(actual, exact, rtol=KERNEL_RTOL, atol=0, label=label)
            rows.append(dict(id=label, category="kernel", numerical=actual, formula=exact))

    cases = [(u, v, .2 * v, omega) for u, v in parameters for omega in (0., .3, 1.)]
    cases += [(1., .1, 0., 1.), (1., .1, .1, 1.)]  # Identical states and v1=0.
    for u, v, a2, omega in cases:
        levels, nodes = (160, 240) if v / u > 5 else (80, 80)
        baseline = reference_root(u, v, levels)
        signal_formula, cal_formula, z = collision_formula(u, v, a2, omega)
        for signal, exact in [(True, signal_formula), (False, cal_formula)]:
            weighted = weighted_state(u, v, a2, omega, signal=signal,
                                      levels=levels, nodes=nodes)
            actual = float(np.sum((weighted - baseline) ** 2))
            kind = "signal" if signal else "calibration"
            label = f"{kind}:u={u}:v={v}:a2={a2}:omega={omega}"
            absolute_tolerance = ZERO_COLLISION_ATOL if exact == 0 else COLLISION_ATOL
            close(actual, exact, rtol=COLLISION_RTOL, atol=absolute_tolerance, label=label)
            rows.append(dict(id=label, category=kind, numerical=actual, formula=exact, z=z))

    # Explicit small tensor matrices check the joint weighted difference.  This
    # uses tensor products of integrated matrices, not powers of the formula.
    for count_n, count_m in [(2, 0), (2, 1)]:
        u, v, a2, levels = 1., .01, .002, 12
        omega = count_n / (count_n + count_m)
        signal = weighted_state(u, v, a2, omega, signal=True, levels=levels)
        cal = weighted_state(u, v, a2, omega, signal=False, levels=levels)
        root = reference_root(u, v, levels)
        joint, baseline = np.ones((1, 1)), np.ones((1, 1))
        for factor in [signal] * count_n + [cal] * count_m:
            joint = np.kron(joint, factor)
            baseline = np.kron(baseline, root)
        actual = float(np.sum((joint - baseline) ** 2))
        fs, fc, _ = collision_formula(u, v, a2, omega)
        exact = float(np.expm1(count_n * np.log1p(fs) + count_m * np.log1p(fc)))
        label = f"tensor:N={count_n}:M={count_m}"
        close(actual, exact, rtol=COLLISION_RTOL, atol=COLLISION_ATOL, label=label)
        rows.append(dict(id=label, category="tensor", numerical=actual, formula=exact))

    # b=0 uses a pure overlap, never a singular inverse.  Direct quadrature of
    # the amplitude overlap checks the squared-fidelity convention.
    gh, weights = np.polynomial.hermite.hermgauss(80)
    for q in (.001, .1, 1.):
        overlap = float(np.dot(weights, np.exp(np.sqrt(q / 2) * gh - q / 4)) / np.sqrt(np.pi))
        actual, exact = overlap ** 2, float(np.exp(-q / 4))
        label = f"pure_fidelity:q={q}"
        close(actual, exact, rtol=KERNEL_RTOL, atol=0, label=label)
        rows.append(dict(id=label, category="pure_fidelity", numerical=actual, formula=exact))

    return {"schema": 1, "checks": rows}


def compare_reference(result: dict, reference: dict) -> None:
    if result["schema"] != reference.get("schema"):
        raise AssertionError("Expected-result schema differs.")
    actual_rows = {row["id"]: row for row in result["checks"]}
    expected_rows = {row["id"]: row for row in reference["checks"]}
    if actual_rows.keys() != expected_rows.keys():
        raise AssertionError("Expected-result check inventory differs; review before --record.")
    for label, row in actual_rows.items():
        expected = expected_rows[label]
        if row["category"] != expected["category"]:
            raise AssertionError(f"{label}: category differs.")
        for key in ("numerical", "formula"):
            absolute_tolerance = ZERO_COLLISION_ATOL if expected["formula"] == 0 else COLLISION_ATOL
            close(row[key], expected[key], rtol=COLLISION_RTOL,
                  atol=absolute_tolerance, label=f"reference:{label}:{key}")


def summary(result: dict, action: str) -> dict:
    counts: dict[str, int] = {}
    for row in result["checks"]:
        counts[row["category"]] = counts.get(row["category"], 0) + 1
    kernel = [row for row in result["checks"] if row["category"] == "kernel"]
    collision = [row for row in result["checks"] if row["category"] in ("signal", "calibration", "tensor")]
    return dict(
        status="PASS", action=action, checks=counts,
        max_kernel_relative_error=max(abs(r["numerical"] - r["formula"]) / r["formula"] for r in kernel),
        max_collision_absolute_error=max(abs(r["numerical"] - r["formula"]) for r in collision),
        max_nonzero_collision_relative_error=max(
            abs(r["numerical"] - r["formula"]) / r["formula"] for r in collision if r["formula"] > 0
        ),
        expected="expected/check_collision.json",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", action="store_true",
                        help="replace the committed expected results after analytic comparisons pass")
    args = parser.parse_args()
    result = run_checks()
    if args.record:
        EXPECTED.parent.mkdir(parents=True, exist_ok=True)
        EXPECTED.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        action = "recorded expected results"
    else:
        if not EXPECTED.is_file():
            raise FileNotFoundError(f"Missing committed reference: {EXPECTED}")
        compare_reference(result, json.loads(EXPECTED.read_text(encoding="utf-8")))
        action = "verified committed expected results"
    print(json.dumps(summary(result, action), indent=2))


if __name__ == "__main__":
    main()
