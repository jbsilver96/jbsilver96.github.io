"""MERGE proof study — frozen protocol (DESIGN.md).
Modes: evolve | randsearch | final.
DEV seeds 1000-1011 (fitness), PROBE seeds 3000-3019 (curve only),
HELD-OUT seeds 5000-5099 (final only). GA rng seeded and disclosed.
"""
import json
import math
import random
import sys
import time

from merge_engine import play_episode, ENGINE_VERSION
from players import INITIAL_W, SNAKE_W, greedy_policy, make_weight_policy, random_policy

RUN = "/home/hatch/workspace/think_tank/runs/autonomous_game_2026-10-23"
DEV = list(range(1000, 1012))
PROBE = list(range(3000, 3020))
HELDOUT = list(range(5000, 5100))
POP = 32
GENS = 20
TOTAL_CANDIDATES = POP * GENS  # 640
MUT_P = 0.25
MUT_SIGMA = 0.35


def mean_ci(xs):
    n = len(xs)
    m = sum(xs) / n
    if n < 2:
        return m, 0.0
    var = sum((x - m) ** 2 for x in xs) / (n - 1)
    return m, 1.96 * math.sqrt(var / n)


def fitness(weights, counter):
    pol = make_weight_policy(weights)
    scores = []
    for s in DEV:
        r = play_episode(s, pol)
        scores.append(r["score"])
        counter["steps"] += r["moves"]
        counter["episodes"] += 1
    return sum(scores) / len(scores)


def probe(weights, counter):
    pol = make_weight_policy(weights)
    scores = []
    for s in PROBE:
        r = play_episode(s, pol)
        scores.append(r["score"])
        counter["steps"] += r["moves"]
    return mean_ci(scores)


def mutate(rng, w):
    return [g + rng.gauss(0, MUT_SIGMA) if rng.random() < MUT_P else g for g in w]


def crossover(rng, a, b):
    return [x if rng.random() < 0.5 else y for x, y in zip(a, b)]


def run_evolve():
    rng = random.Random(20261024)
    fit_counter = {"steps": 0, "episodes": 0}
    probe_counter = {"steps": 0}
    curve = open(f"{RUN}/data/curve_evolution.jsonl", "w")
    flog = open(f"{RUN}/data/fitness_log_evolution.jsonl", "w")
    pop = [list(INITIAL_W)] + [mutate(rng, INITIAL_W) for _ in range(POP - 1)]
    candidates = 0
    champion = None
    t0 = time.time()
    for gen in range(GENS):
        scored = []
        for i, w in enumerate(pop):
            f = fitness(w, fit_counter)
            candidates += 1
            pid = f"evo-gen{gen}-idx{i}"
            scored.append((f, w, pid))
            flog.write(json.dumps({"policy_id": pid, "fitness": f}) + "\n")
        scored.sort(key=lambda t: -t[0])
        champ_f, champ_w, champ_id = scored[0]
        pm, pci = probe(champ_w, probe_counter)
        row = {
            "cumulative_candidates": candidates,
            "cumulative_env_steps": fit_counter["steps"],
            "probe_steps": probe_counter["steps"],
            "probe_mean": pm,
            "probe_ci95": pci,
            "champion_policy_id": champ_id,
            "champion_dev_fitness": champ_f,
        }
        curve.write(json.dumps(row) + "\n")
        curve.flush()
        print(f"[evo] gen {gen} champ {champ_id} dev {champ_f:.0f} probe {pm:.0f}±{pci:.0f} "
              f"cand {candidates} steps {fit_counter['steps']} t {time.time()-t0:.0f}s", flush=True)
        champion = (champ_w, champ_id, champ_f)
        if gen == GENS - 1:
            break
        parents = [w for _, w, _ in scored[:8]]
        elites = [list(w) for _, w, _ in scored[:2]]
        children = []
        while len(children) < POP - 2:
            a, b = rng.sample(parents, 2)
            children.append(mutate(rng, crossover(rng, a, b)))
        pop = elites + children
    json.dump({"policy_id": champion[1], "weights": champion[0], "dev_fitness": champion[2]},
              open(f"{RUN}/data/champion_evolution.json", "w"))
    print("[evo] DONE", champion[1], champion[2], "wall", time.time() - t0, flush=True)


def run_randsearch():
    rng = random.Random(20261024)
    fit_counter = {"steps": 0, "episodes": 0}
    probe_counter = {"steps": 0}
    curve = open(f"{RUN}/data/curve_random_search.jsonl", "w")
    flog = open(f"{RUN}/data/fitness_log_random_search.jsonl", "w")
    best = None  # (fitness, weights, policy_id)
    candidates = 0
    t0 = time.time()
    for block in range(GENS):
        for i in range(POP):
            w = list(INITIAL_W) if candidates == 0 else mutate(rng, INITIAL_W)
            f = fitness(w, fit_counter)
            candidates += 1
            pid = f"rs-{candidates}"
            flog.write(json.dumps({"policy_id": pid, "fitness": f}) + "\n")
            if best is None or f > best[0]:
                best = (f, w, pid)
        pm, pci = probe(best[1], probe_counter)
        row = {
            "cumulative_candidates": candidates,
            "cumulative_env_steps": fit_counter["steps"],
            "probe_steps": probe_counter["steps"],
            "probe_mean": pm,
            "probe_ci95": pci,
            "champion_policy_id": best[2],
            "champion_dev_fitness": best[0],
        }
        curve.write(json.dumps(row) + "\n")
        curve.flush()
        print(f"[rs] block {block} best {best[2]} dev {best[0]:.0f} probe {pm:.0f}±{pci:.0f} "
              f"cand {candidates} steps {fit_counter['steps']} t {time.time()-t0:.0f}s", flush=True)
    json.dump({"policy_id": best[2], "weights": best[1], "dev_fitness": best[0]},
              open(f"{RUN}/data/champion_random_search.json", "w"))
    print("[rs] DONE", best[2], best[0], "wall", time.time() - t0, flush=True)


def run_final():
    evo = json.load(open(f"{RUN}/data/champion_evolution.json"))
    rs = json.load(open(f"{RUN}/data/champion_random_search.json"))
    players = {
        "RANDOM": None,
        "GREEDY": greedy_policy,
        "FROZEN_INITIAL": make_weight_policy(INITIAL_W),
        "STRONG_FIXED_SOLVER": make_weight_policy(SNAKE_W),
        "RANDOM_SEARCH_CHAMPION": make_weight_policy(rs["weights"]),
        "EVOLUTION_CHAMPION": make_weight_policy(evo["weights"]),
    }
    out = open(f"{RUN}/data/heldout_episodes.jsonl", "w")
    summary = {"engine_version": ENGINE_VERSION, "heldout_seeds": [HELDOUT[0], HELDOUT[-1]], "players": {}}
    means = {}
    ses = {}
    for name, pol in players.items():
        scores, tiles = [], []
        steps = 0
        for s in HELDOUT:
            p = random_policy(random.Random(10_000_000 + s)) if name == "RANDOM" else pol
            r = play_episode(s, p)
            scores.append(r["score"])
            tiles.append(r["max_tile"])
            steps += r["moves"]
            out.write(json.dumps({"player": name, "seed": s, "score": r["score"],
                                  "max_tile": r["max_tile"], "moves": r["moves"]}) + "\n")
        m, ci = mean_ci(scores)
        means[name] = m
        ses[name] = ci / 1.96
        summary["players"][name] = {
            "mean": m, "ci95": ci, "env_steps": steps,
            "max_tile_median": sorted(tiles)[len(tiles) // 2],
            "games_at_2048": sum(1 for t in tiles if t >= 2048),
        }
        print(f"[final] {name}: {m:.0f} ± {ci:.0f}", flush=True)
    d = means["EVOLUTION_CHAMPION"] - means["RANDOM_SEARCH_CHAMPION"]
    dci = 1.96 * math.sqrt(ses["EVOLUTION_CHAMPION"] ** 2 + ses["RANDOM_SEARCH_CHAMPION"] ** 2)
    summary["evolution_minus_random_search"] = {"diff": d, "ci95": dci}
    success = (means["EVOLUTION_CHAMPION"] > means["RANDOM"]
               and means["EVOLUTION_CHAMPION"] > means["GREEDY"]
               and means["EVOLUTION_CHAMPION"] > means["FROZEN_INITIAL"])
    summary["success_criterion_met"] = success
    json.dump(summary, open(f"{RUN}/data/summary.json", "w"), indent=2)
    print("[final] evo - rs =", d, "±", dci, "| success:", success, flush=True)


if __name__ == "__main__":
    mode = sys.argv[1]
    {"evolve": run_evolve, "randsearch": run_randsearch, "final": run_final}[mode]()
