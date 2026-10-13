"""Part D: name the failure. TODO 8."""
from __future__ import annotations

from avsim import core


def label_mode(R: core.Rollout, k: int, event: dict, contact_type) -> str:
    """TODO 8. Name the kind of failure behind one ego collision. Return one of:

      'dart_out'   - the ego hit the crossing pedestrian P1
      'rear_ended' - something ran into the ego from behind (use contact_type(R, k, event) == 'rear')
      'bus_bypass' - the ego hit C2 while C2 was squeezing past the stopped bus: at contact C2 is at x < 112 m
                     and slower than 6 m/s
      'cut_in'     - the ego hit C2 in any other situation
      'other'      - anything else
    Check in that order. Positions and speeds at contact: R.F[k, event["f"], core.IX["C2"]] (x is column 0, v is 4).
    """
    raise NotImplementedError("TODO 8: label_mode")
