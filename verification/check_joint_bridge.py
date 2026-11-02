#!/usr/bin/env python3
"""Check the normalization and finite consequences of the timing bridge.

The reference is refreshed only by --record. The checks cover the stationary
point-calibration experiment, close-doublet reduction, and the persistence of
physical jitter. They do not certify the arbitrary-schedule theorem.
"""
import argparse
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.optimize import brentq

EXPECTED = Path(__file__).resolve().parent/'expected'/'check_joint_bridge.json'


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def compare(actual, expected):
    if isinstance(actual, dict):
        require(isinstance(expected, dict) and actual.keys() == expected.keys(), 'reference keys')
        for key in actual: compare(actual[key], expected[key])
    elif isinstance(actual, list):
        require(isinstance(expected, list) and len(actual) == len(expected), 'reference length')
        for a, b in zip(actual, expected): compare(a, b)
    elif isinstance(actual, (int, float)):
        require(math.isclose(actual, expected, abs_tol=5e-12, rel_tol=2e-10), 'numeric reference')
    else:
        require(actual == expected, 'reference value')


def run_checks():
    nodes, weights = hermgauss(96)
    weights /= math.sqrt(math.pi)
    calibration, mappings = [], []
    for u in (.2, 1., 3.):
      for physical_variance in (0., 1e-5, .01, .3):
        x = math.sqrt(2*physical_variance)*nodes
        timing_x = x/math.sqrt(2*u)
        lambda_physical = x*x/(4*u)
        lambda_timing = timing_x*timing_x/2
        require(np.max(np.abs(lambda_physical-lambda_timing)) < 1e-12, 'HG coordinate mapping')
        w = physical_variance/(2*u)
        # Conditional Poisson moments, integrated independently in physical x.
        mean = float(weights@(2*lambda_physical))
        second = float(weights@(4*(lambda_physical**2+lambda_physical)))
        variance = second-mean*mean
        require(math.isclose(mean, w, abs_tol=1e-12, rel_tol=1e-12), 'stationary calibration mean')
        require(math.isclose(variance, 2*w+2*w*w, abs_tol=1e-12, rel_tol=1e-12), 'stationary calibration variance')
        calibration.append({'u': u, 'physical_jitter_variance': physical_variance,
                            'timing_jitter_variance': w, 'mean_2Q': mean, 'variance_2Q': variance})
      for s in (0., .01, .2, 1.):
        qt = s*s/(8*u)
        qc = s*s/(4*u)
        require(qc == 2*qt, 'separation normalization q_cal=2q_timing')
        require(math.isclose(2*math.sqrt(u*qc), 2*math.sqrt(2*u*qt), abs_tol=1e-14), 'physical separation mapping')
        mappings.append({'u': u, 'separation': s, 'q_calibration': qc, 'q_timing': qt})
    close_cases = []
    for N in (1000, 10000, 100000):
      n = N//2
      for b in (0., 1e-6, .001, .1):
        def info(q):
            return n*q*q/(b+1/N+q)+(n-1)*q*q/(b+1+q)
        r0 = brentq(lambda q: info(q)-1, 1e-16, 10, xtol=1e-15)
        S2 = n/(b+1/N)**2+(n-1)/(b+1)**2
        for M in (0, 10, N, 10*N):
            K = N*M/(N+M) if M else 0.
            L = max(math.sqrt(N), K)
            # Original Calibration theorem, converted to timing q units.
            calibration_scale_timing = (1/N+min(2*b, math.sqrt(2*b/L)))/2
            nuisance = 0. if not b else min(b, math.sqrt(b/M) if M else math.inf, S2**-.25)
            joint_scale = r0+nuisance
            ratio = joint_scale/calibration_scale_timing
            require(.2 < ratio < 12., 'close-doublet/calibration resolution-order reduction')
            close_cases.append({'N': N, 'M': M, 'b_timing': b,
                                'joint_scale': joint_scale, 'calibration_scale_in_timing_units': calibration_scale_timing})
    jitter = []
    for N in (1000, 10000, 100000):
      for w in (0., 1e-5, .001, .1):
        # Even exact knowledge of w leaves this probability under a single source.
        p0 = (1-(1+2*w)**-.5)/2
        slope = 1/(2*(1+2*w)**1.5)
        known_floor_proxy = 1/N+math.sqrt(w/N)
        require(p0 >= 0 and (p0 > 0 if w else p0 == 0), 'physical jitter background')
        jitter.append({'N': N, 'known_w': w, 'SWAP_null_probability': p0,
                       'SWAP_signal_slope_at_zero': slope, 'known_jitter_floor_proxy': known_floor_proxy})
    payload = {'schema_version': 1, 'normalization': mappings,
               'stationary_point_calibration': calibration, 'close_doublet_reduction': close_cases,
               'physical_jitter_with_perfect_calibration': jitter}
    return payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--record', action='store_true', help='refresh reference after independent checks pass')
    args = parser.parse_args()
    payload = run_checks()
    if args.record:
        EXPECTED.parent.mkdir(parents=True, exist_ok=True)
        EXPECTED.write_text(json.dumps(payload, indent=2, sort_keys=True)+'\n')
    else:
        require(EXPECTED.exists(), 'missing reference; --record intentionally creates it')
        compare(payload, json.loads(EXPECTED.read_text()))
    print(json.dumps({'status': 'recorded' if args.record else 'passed',
                      'normalization_cases': len(payload['normalization']),
                      'stationary_calibration_cases': len(payload['stationary_point_calibration']),
                      'close_doublet_cases': len(payload['close_doublet_reduction']),
                      'physical_jitter_cases': len(payload['physical_jitter_with_perfect_calibration']),
                      'meaning': 'finite bridge consistency checks; not a minimax proof'}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
