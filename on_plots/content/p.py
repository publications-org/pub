# ============================================================
# File: theorem2-7.py
# Description: Numerical evaluation and visualization of Theorem 2.7 from "On Glossary" by Amlal El Mahrouss.
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

# Theorem 2.7 — Glossary (Amlal El Mahrouss)
#
# For m = 7, log p ≠ log 1, and x ∈ ℝ:
#
#   Sum form:
#     7/log(p) + 363·log(7)/140  =  Σ_{k=1}^{7} [ ln x / k  +  k / ln x ]
#
#   Product form:
#     7/log(p) + log⁷(7)/5040   =  Π_{k=1}^{7} [ ln x / k  +  k / ln x ]
#
# The script evaluates the RHS numerically over x, plots both forms, and for
# a representative value of p locates the intersection point via bisection.

M = 7           # upper summation / product index stated by the theorem
FACTORIAL_M = 5040  # 7! = 5040


def term(x: np.ndarray, k: int) -> np.ndarray:
    lnx = np.log(x)
    return lnx / k + k / lnx


def rhs_sum(x: np.ndarray) -> np.ndarray:
    return sum(term(x, k) for k in range(1, M + 1))


def rhs_product(x: np.ndarray) -> np.ndarray:
    result = np.ones_like(x, dtype=float)
    for k in range(1, M + 1):
        result = result * term(x, k)
    return result


def lhs_sum(p: float) -> float:
    return 7.0 / np.log10(p) + 363.0 * np.log10(7) / 140.0


def lhs_product(p: float) -> float:
    return 7.0 / np.log10(p) + np.log10(7) ** M / FACTORIAL_M


def find_root(f_rhs, target: float, x_lo: float, x_hi: float):
    g = lambda x: f_rhs(np.array([x]))[0] - target
    try:
        return brentq(g, x_lo, x_hi)
    except ValueError:
        return None


# --- domain: x > 1 so that ln x > 0 and every term is positive ---
x = np.linspace(1.02, 12.0, 4000)

s_vals = rhs_sum(x)
p_vals = rhs_product(x)

# Representative left-hand-side values (p = 5)
P_DEMO = np.pi # PI is a common transcendental number. Might as well try np.e as well.
lhs_s = lhs_sum(P_DEMO)
lhs_p = lhs_product(P_DEMO)

root_s = find_root(rhs_sum, lhs_s, 1.02, 12.0)
root_p = find_root(rhs_product, lhs_p, 1.02, 12.0)

# --- figure ---
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle(
    "Theorem 2.7 — Glossary\n"
    r"$\sum_{k=1}^{7}\!\left(\frac{\ln x}{k}+\frac{k}{\ln x}\right)$  and  "
    r"$\prod_{k=1}^{7}\!\left(\frac{\ln x}{k}+\frac{k}{\ln x}\right)$",
    fontsize=13,
)

# ── left panel: sum form ─────────────────────────────────────────────────────
ax = axes[0]
ax.plot(x, s_vals, color="royalblue", linewidth=2, label=r"$S(x)=\sum_{k=1}^{7}(\frac{\ln x}{k}+\frac{k}{\ln x})$")
ax.axhline(lhs_s, color="tomato", linestyle="--", linewidth=1.4,
           label=rf"LHS  ($p={P_DEMO:.0f}$) $\approx{lhs_s:.4f}$")
if root_s is not None:
    ax.axvline(root_s, color="seagreen", linestyle=":", linewidth=1.4,
               label=rf"$x^*\approx{root_s:.4f}$")
    ax.scatter([root_s], [lhs_s], zorder=5, color="seagreen", s=60)

ax.set_title("Sum form", fontsize=11)
ax.set_xlabel("$x$")
ax.set_ylabel("Value")
ax.set_ylim(-2000, 6000)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.35)

# ── right panel: product form ────────────────────────────────────────────────
ax = axes[1]
ax.plot(x, p_vals, color="darkorange", linewidth=2, label=r"$P(x)=\prod_{k=1}^{7}(\frac{\ln x}{k}+\frac{k}{\ln x})$")
ax.axhline(lhs_p, color="tomato", linestyle="--", linewidth=1.4,
           label=rf"LHS  ($p={P_DEMO:.0f}$) $\approx{lhs_p:.4f}$")
if root_p is not None:
    ax.axvline(root_p, color="seagreen", linestyle=":", linewidth=1.4,
               label=rf"$x^*\approx{root_p:.4f}$")
    ax.scatter([root_p], [lhs_p], zorder=5, color="seagreen", s=60)

ax.set_title("Product form", fontsize=11)
ax.set_xlabel("$x$")
ax.set_ylabel("Value")
ax.set_ylim(-5000, 2000)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.35)

plt.tight_layout()

# --- console output ---
print("Theorem 2.7 — numerical evaluation")
print(f"  LHS sum  (p={P_DEMO}): {lhs_s:.6f}")
print(f"  LHS prod (p={P_DEMO}): {lhs_p:.6f}")
if root_s is not None:
    print(f"  Sum  form root x* = {root_s:.6f}   S(x*)={rhs_sum(np.array([root_s]))[0]:.6f}")
if root_p is not None:
    print(f"  Prod form root x* = {root_p:.6f}   P(x*)={rhs_product(np.array([root_p]))[0]:.6f}")

plt.savefig("theorem2-7.png", dpi=150, bbox_inches="tight")

print("Plot saved to theorem2-7.png")

