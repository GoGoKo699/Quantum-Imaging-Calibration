#!/usr/bin/env python3
"""Plot the theorem's representative scales, not exact minimax constants."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import tempfile

# A writable cache also makes the command usable in restricted environments.
os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "imaging-mpl"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def resolution_scales(n: np.ndarray, m: np.ndarray, b: float):
    """Return (R_Q,R_DI); n and m are positive signal/nonnegative calibration counts."""
    k = n * m / (n + m)
    ell = np.maximum(np.sqrt(n), k)
    return (1 / n + np.minimum(b, np.sqrt(b / ell)),
            1 / np.sqrt(n) + np.minimum(b, 1 / np.sqrt(ell)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--png", type=Path, help="Optional raster preview path")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    destination = root / "figures" / "resolution-regimes.svg"
    destination.parent.mkdir(parents=True, exist_ok=True)
    b = 1e-4
    n = np.logspace(1, 20, 700)
    rq, rdi = resolution_scales(n, np.zeros_like(n), b)
    calibrated, _ = resolution_scales(n, n, b)

    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 10,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.labelcolor": "#1c2638", "text.color": "#1c2638",
        "axes.edgecolor": "#94a3b8", "xtick.color": "#475569",
        "ytick.color": "#475569", "svg.hashsalt": "imaging-calibration-v1",
    })
    fig, (ax, advantage) = plt.subplots(1, 2, figsize=(12, 5.4),
                                       gridspec_kw={"width_ratios": [1.6, 1]})
    fig.patch.set_facecolor("#ffffff")
    quantum, direct, calibration = "#155e75", "#c05621", "#6d28d9"
    ax.axvspan(b**-1, b**-2, color=quantum, alpha=.09, lw=0)
    ax.axvspan(b**-2, b**-4, color=direct, alpha=.07, lw=0)
    ax.loglog(n, rdi, color=direct, lw=2.7, label="Direct imaging, M = 0")
    ax.loglog(n, rq, color=quantum, lw=2.7, label="Quantum, M = 0")
    ax.loglog(n, calibrated, color=calibration, lw=2, ls="--", label="Quantum, M = N")
    ax.set(xlim=(1e1, 1e20), ylim=(1e-12, 1), xlabel="Signal photons N",
           ylabel=r"Representative squared-separation scale R  ($q=s^2/(4u)$)")
    ax.set_title("Resolution improves across different regimes", loc="left", fontweight="bold", pad=15)
    ax.set_xticks([1e1, 1e4, 1e8, 1e12, 1e16, 1e20])
    ax.grid(which="major", color="#cbd5e1", alpha=.6, lw=.6)
    ax.text(1.6e4, 3e-2, "Quantum\nplateau", color=quantum, fontsize=9)
    ax.text(1e11, 3e-2, "Direct-imaging\nplateau", color=direct, fontsize=9)
    ax.legend(loc="lower left", frameon=False, fontsize=9)

    advantage.loglog(n, rdi / rq, color=quantum, lw=2.7)
    advantage.axvline(b**-2, color="#94a3b8", lw=1, ls=":")
    advantage.axhline(1, color="#94a3b8", lw=1, ls=":")
    advantage.set(xlim=(1e1, 1e20), ylim=(.8, 250), xlabel="Signal photons N",
                  ylabel=r"Scale ratio $R_{\rm DI}/R_Q$, with M = 0")
    advantage.set_title("Relative advantage closes and returns", loc="left", fontweight="bold", pad=15)
    advantage.set_xticks([1e1, 1e4, 1e8, 1e12, 1e16, 1e20])
    advantage.grid(which="major", color="#cbd5e1", alpha=.6, lw=.6)
    advantage.annotate("Same order near\n" + r"$N\sim b^{-2}$", xy=(1e8, 2),
                       xytext=(2e10, 5), fontsize=9,
                       arrowprops={"arrowstyle": "->", "color": "#475569"})
    fig.suptitle(r"Unknown independent Gaussian jitter: fixed bound $b=10^{-4}$",
                 x=.07, y=.99, ha="left", fontsize=15, fontweight="bold")
    fig.text(.07, .025,
             "Matching-order formulas; unknown multiplicative constants are omitted. "
             "These are not exact risk curves.\n"
             "Physical-separation ratios are the square roots of the displayed scale ratios.",
             fontsize=9, color="#475569")
    fig.subplots_adjust(left=.075, right=.985, bottom=.22, top=.84, wspace=.30)
    fig.savefig(destination, metadata={"Date": None,
        "Description": "Representative uniform minimax resolution scales, not exact risk or leading constants."})
    if args.png:
        args.png.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(args.png, dpi=160)
    plt.close(fig)
    print(destination)


if __name__ == "__main__":
    main()
