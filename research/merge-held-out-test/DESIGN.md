# DESIGN (FROZEN) — MERGE, seeded 2048 as an RSI testbed

Selected 2026-10-24 in Slack thread 1792814500.799549: Muse MERGE, dot MERGE, Arbiter VERDICT: Yes (ruling 20261024T041356Z; two earlier rulings truncated at the plug's 1,500-token output cap and are preserved as defective). Arbiter's name: ruled on separately in binary form against this spec (see §10). This document freezes the design BEFORE any study run. Amendments only below the freeze line, timestamped; frozen text is never edited.

## 1. Question
Does MERGE have a true, measurable skill curve? Concretely: can a programmatic improver (weight evolution), under a frozen per-move compute budget and a frozen candidate budget, produce a policy whose score on HELD-OUT seeds beats the frozen baselines — and does it beat a matched-budget random-search control over the same weight space? This run measures a learning/optimization curve, the substrate an RSI loop requires. It does not claim RSI.

## 2. The game (engine version `merge-py-1.0`, canonical)
- Board 4×4; cells hold exponents (0 = empty, k = 2^k, capped at 15).
- Start: empty board, then two spawns.
- Move (0=up, 1=right, 2=down, 3=left): slide all tiles; equal tiles merge once per move, resolved from the leading edge (standard 2048 rules). A move that changes nothing is illegal and is never offered to a policy (policies receive the legal-move mask).
- Spawn: after every legal move, exactly one tile: cell uniform among empties, value 2 with p=0.9 else 4 — always from the episode's seeded PRNG.
- Score: standard merge-sum (merging two 2^k tiles gains 2^(k+1)). Episode ends when no legal move exists. Recorded per episode: seed, score, max tile, moves, full action sequence.
- Replay identity = (engine version, seed, action sequence). PRNG: Python `random.Random(seed)` in the canonical engine. The browser page (`merge-js-1.0`) implements identical rules for human play; replay identity is claimed within an engine version, not across implementations.
- Policies observe ONLY the board (plus legal mask, score, move count). PRNG state and future spawns are never visible to a policy. Anti-exploit rule, no exceptions.

## 3. Policy class (the evolvable player)
Afterstate policy: for each legal move, apply the slide+merge deterministically (no spawn), evaluate the resulting board with a fixed linear feature function, play the argmax (ties → lowest move index). One forward evaluation per move; no search.
Features (fixed set): (i) 16 positional weights over tile exponents; (ii) empty-cell count; (iii) merge potential = sum over adjacent equal pairs of the pair's exponent; (iv) monotonicity = negative sum of exponent decreases along rows/columns in the two directions away from the max corner; (v) smoothness = negative sum of |exponent differences| over adjacent pairs; (vi) corner bonus = max exponent if the max tile sits in the designated corner cell (index 12, bottom-left), else 0; (vii) sum of exponents.
Weight vector: 22 numbers (16 positional + 6 global), stored as JSON artifacts.

## 4. Frozen players
- RANDOM: uniform over legal moves.
- GREEDY: move with the largest immediate merge gain; ties → most resulting empties, then lowest move index.
- FROZEN INITIAL (evolution's start, never tuned): positional weights = linear corner gradient toward cell 12 (16 at cell 12 descending by Manhattan distance to 1 at cell 3); global weights: empty=1.0, all others 0.
- STRONG FIXED SOLVER (hand-written, fixed here, never tuned on any study seed): afterstate policy with positional weights = the standard snake pattern over exponents, max weight 16 at the designated corner (cell 12, bottom-left), cells 0–15 row-major from top-left: [1,2,3,4, 8,7,6,5, 9,10,11,12, 16,15,14,13]; global weights: empty=270, merge-potential=55, monotonicity=40, smoothness=-12, corner=120, sum=8. These numbers are part of this freeze.
- EVOLUTION (the improver): (μ+λ) GA over the 22-weight space. Population 32; parents = top 8 by fitness (elitism carries top 2 unchanged); offspring by uniform crossover + Gaussian mutation (σ=0.35 per gene, 25% of genes mutated per child); 20 generations ⇒ ≤ 640 candidates evaluated (initial population counted). Fitness of a candidate = mean score over the DEV seed set, same set for every candidate (common random numbers).
- RANDOM-SEARCH CONTROL: 640 candidates sampled by the identical mutation operator applied to FROZEN INITIAL (same distribution family, matched count); best-on-DEV retained. Matched budget by construction.

## 5. Seed splits (disjoint, frozen)
- DEV (fitness + selection only): seeds 1000–1011 (12 episodes per candidate).
- PROBE (learning-curve checkpoints only; never used for selection): seeds 3000–3019 (20 episodes). The current champion is probe-evaluated after each generation.
- HELD-OUT (final evaluation only; touched once, at the end, by the frozen evaluator): seeds 5000–5099 (100 episodes per player). Players evaluated on held-out: RANDOM, GREEDY, FROZEN INITIAL, STRONG FIXED SOLVER, RANDOM-SEARCH champion, EVOLUTION champion.

## 6. Accounting (all counted and reported)
Candidates evaluated (both improvers, including failures), training environment steps (total moves played in fitness evaluations), probe steps, held-out steps, wall-clock per phase. Improvement-cost axis = cumulative candidates evaluated.

## 7. Endpoint and success criterion (predeclared)
Primary endpoint: HELD-OUT mean score per player with 95% CIs (normal approx on 100 episodes; bootstrap check in the report), and the learning curve: PROBE mean score vs cumulative candidates evaluated for evolution and random search.
SUCCESS (the skill-curve claim holds): EVOLUTION champion's held-out mean beats RANDOM, GREEDY, and FROZEN INITIAL.
REPORTED EITHER WAY: evolution vs random-search control on held-out (difference + CI); if evolution does not beat its matched control, the finding is stated as exactly that — the game is learnable, but at this budget evolution adds nothing over random search.
No best-run selection anywhere: the only champions are the predeclared best-on-DEV at the final generation / final sample.

## 8. RSI-readiness spec (how a future loop plugs in)
- The policy is a pure function of the board; a policy artifact = {engine_version, weights[22], policy_id}. The episode runner is a CLI: (seed, policy artifact) → one JSONL record {seed, actions[], score, max_tile, moves}.
- The learning-curve log format is frozen: one JSONL row per checkpoint {cumulative_candidates, cumulative_env_steps, probe_mean, probe_ci95, champion_policy_id}.
- Separation the future loop inherits: the PROPOSER (tonight: GA mutation/crossover; later: the RSI machinery) may change; the EVALUATOR, the seed splits, the per-move compute freeze, and the budgets live outside the proposer's reach. Held-out seeds are never visible during improvement.
- Anti-exploit rules carried forward: no PRNG visibility; no spawn peeking; no per-move search for entered policies; difficulty parameters (board size etc.) may be raised only inside a new frozen design, never mid-run.

## 9. Human face
A browser page (same rules, `merge-js-1.0`): arrow keys / WASD / swipe buttons, seed entry + display, score and max tile, new-game control. Publishes alongside the study write-up.

## 10. The name
Put to the Arbiter in its required binary form with this spec on the record. Muse's proposed name: **"Merge — the Long Climb"** — it measures long-horizon positional discipline under chance: the slow compounding of small good placements into large scores; an improvement loop on it proves its gains are real only if they survive seeds the improver never saw. The Arbiter's Yes/No rules on accuracy/non-overclaim; on a No, one revised proposal may be put.

— FROZEN 2026-10-24, before build and before any study run. Amendments below this line only, timestamped. —

## Amendment A1 — 2026-10-24, pre-build (definition sign correction, disclosed)
§3(v) defined the smoothness feature as the *negative* sum of adjacent |exponent differences|, while §4 gives the STRONG FIXED SOLVER a smoothness weight of −12; combined literally, that pairing would *reward* roughness — the opposite of the frozen intent. Correction, made before any code ran: the feature is the roughness sum itself (≥ 0), and the −12 weight penalizes it. No other definition, weight, seed, budget, or criterion changes. The monotonicity feature is likewise fixed concretely: per row and column, −min(total drops, total rises) along that line (≤ 0), so its +40 weight rewards monotone lines.
