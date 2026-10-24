#!/usr/bin/env python3
"""Independent-check analysis for Amendments B1/B2 — Merge, the Held-Out Test.

Recomputes, from data/heldout_episodes.jsonl only:
  - per-player mean and normal-approximation 95% CI (study.py mean_ci method)
  - per-player bootstrap 95% CI (B1)
  - paired per-seed bootstrap 95% CIs for EVOLUTION_CHAMPION minus each
    comparator, with seed-win counts (B2), plus the unpaired variant for
    evolution vs random search (B1)

Method: 10,000 bootstrap resamples, RNG seed 42 (random.Random), percentile
2.5 / 97.5 intervals. Paired resampling draws seed indices once and applies
the same indices to both players, preserving the per-seed pairing.
This script was written after the study (2026-10-24, presence run) to make
the B1/B2 numbers independently recomputable; it is not preregistration.
"""
import json
import math
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data" / "heldout_episodes.jsonl"
RESAMPLES = 10_000
BOOT_SEED = 42


def mean_ci(xs):
    n = len(xs)
    m = sum(xs) / n
    var = sum((x - m) ** 2 for x in xs) / (n - 1)
    return m, 1.96 * math.sqrt(var / n)


def percentile(sorted_xs, q):
    idx = min(len(sorted_xs) - 1, max(0, int(q * len(sorted_xs))))
    return sorted_xs[idx]


def bootstrap_mean_ci(xs, rng):
    n = len(xs)
    means = []
    for _ in range(RESAMPLES):
        means.append(sum(xs[rng.randrange(n)] for _ in range(n)) / n)
    means.sort()
    return percentile(means, 0.025), percentile(means, 0.975)


def bootstrap_paired_ci(a, b, rng):
    # a, b aligned by seed; returns CI for mean(a-b)
    n = len(a)
    diffs = []
    for _ in range(RESAMPLES):
        idx = [rng.randrange(n) for _ in range(n)]
        diffs.append(sum(a[i] - b[i] for i in idx) / n)
    diffs.sort()
    return percentile(diffs, 0.025), percentile(diffs, 0.975)


def bootstrap_unpaired_ci(a, b, rng):
    n = len(a)
    diffs = []
    for _ in range(RESAMPLES):
        ma = sum(a[rng.randrange(n)] for _ in range(n)) / n
        mb = sum(b[rng.randrange(n)] for _ in range(n)) / n
        diffs.append(ma - mb)
    diffs.sort()
    return percentile(diffs, 0.025), percentile(diffs, 0.975)


def main():
    by_player = {}
    for line in DATA.read_text().splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        by_player.setdefault(row["player"], {})[row["seed"]] = row["score"]
    players = {}
    for name, seed_scores in sorted(by_player.items()):
        seeds = sorted(seed_scores)
        xs = [seed_scores[s] for s in seeds]
        m, ci = mean_ci(xs)
        players[name] = {"n": len(xs), "seeds": [seeds[0], seeds[-1]],
                         "mean": m, "normal_ci95_halfwidth": ci, "scores_by_seed": seed_scores}
    out = {"source": "data/heldout_episodes.jsonl", "resamples": RESAMPLES, "bootstrap_seed": BOOT_SEED,
           "per_player": {}, "paired": {}}
    rng = random.Random(BOOT_SEED)
    for name, p in players.items():
        xs = [p["scores_by_seed"][s] for s in sorted(p["scores_by_seed"])]
        lo, hi = bootstrap_mean_ci(xs, rng)
        out["per_player"][name] = {"n": p["n"], "mean": round(p["mean"], 2),
                                   "normal_ci95": [round(p["mean"] - p["normal_ci95_halfwidth"], 1),
                                                   round(p["mean"] + p["normal_ci95_halfwidth"], 1)],
                                   "bootstrap_ci95": [round(lo, 1), round(hi, 1)]}
    evo = players["EVOLUTION_CHAMPION"]["scores_by_seed"]
    seeds = sorted(evo)
    evo_xs = [evo[s] for s in seeds]
    for comp in ["RANDOM_SEARCH_CHAMPION", "GREEDY", "RANDOM", "FROZEN_INITIAL"]:
        other = players[comp]["scores_by_seed"]
        other_xs = [other[s] for s in seeds]
        lo, hi = bootstrap_paired_ci(evo_xs, other_xs, rng)
        diffs = [a - b for a, b in zip(evo_xs, other_xs)]
        out["paired"][f"EVOLUTION_CHAMPION minus {comp}"] = {
            "mean_diff": round(sum(diffs) / len(diffs), 1),
            "paired_bootstrap_ci95": [round(lo, 1), round(hi, 1)],
            "seed_wins": sum(1 for d in diffs if d > 0), "n": len(diffs)}
    rs_xs = [players["RANDOM_SEARCH_CHAMPION"]["scores_by_seed"][s] for s in seeds]
    lo, hi = bootstrap_unpaired_ci(evo_xs, rs_xs, rng)
    out["paired"]["EVOLUTION_CHAMPION minus RANDOM_SEARCH_CHAMPION (unpaired bootstrap)"] = {
        "unpaired_bootstrap_ci95": [round(lo, 1), round(hi, 1)]}
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
