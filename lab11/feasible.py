"""Part B: physics check. TODO 3."""
from __future__ import annotations

import math

from avsim.core import DEFAULTS

G = 9.81


def is_feasible(p: dict) -> bool:
    """TODO 3. False for scenarios no real road user could produce. Reject if ANY of:

    - the lane change needs more sideways grip than the road has: the cosine lane change of 3.5 m over
      p["cutDur"] seconds peaks at a_lat = (pi / cutDur)^2 * 3.5 / 2; reject if a_lat > mu * g;
    - the post-merge braking p["cutBrake"] exceeds mu * g;
    - the pedestrian runs: p["pedV"] > 2.5 m/s;
    - the cut-in speed p["cutV"] is not in (0, 22] m/s.
    mu is p["mu"]. A search that keeps infeasible scenarios reports failures that cannot happen.
    """
    mu = p.get("mu", DEFAULTS["mu"])
    cut_dur = p.get("cutDur", DEFAULTS["cutDur"])
    cut_brake = p.get("cutBrake", DEFAULTS["cutBrake"]) or 0.0
    ped_v = p.get("pedV", DEFAULTS["pedV"])
    cut_v = p.get("cutV", DEFAULTS["cutV"])
    grip = mu * G
    a_lat = (math.pi / cut_dur) ** 2 * 3.5 / 2
    if a_lat > grip:
        return False
    if cut_brake > grip:
        return False
    if ped_v > 2.5:
        return False
    if not 0.0 < cut_v <= 22.0:
        return False
    return True
