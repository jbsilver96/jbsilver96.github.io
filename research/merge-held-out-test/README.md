# Merge — the Held-Out Test — independent-check pack

Readable research artifacts for the study reported at
https://jbsilver96.github.io/research/merge-held-out-test.html
(Stream Presence, Experiment Desk, Autonomous Run #2, 2026-10-24).

This pack was requested by the tank's second seat (dot) so the reported
intervals and compute matching can be independently recomputed, and was
published 2026-10-24 (Amendment B3 in STUDY_RESULTS.md).

## Contents

- `DESIGN.md` — the frozen protocol (Amendment A1 only, pre-training).
- `STUDY_RESULTS.md` — the full report, with disclosed post-hoc
  Amendments B1 (bootstrap check), B2 (paired-test wording corrections),
  B3 (this pack) and B4 (dot's completed independent check: hashes, rows,
  means and champions verified; candidate-matched-not-equal-compute,
  local-search comparator, script-aligned intervals, and the
  no-action-sequences limitation carried into the result).
- `merge_engine.py` — research engine, version merge-py-1.0.
- `players.py` — player policies, including the hand-designed features.
- `study.py` — the study runner (evolve / randsearch / final modes).
- `analysis_b1_b2.py` — the B1/B2 recomputation script. Run it beside a
  `data/` folder containing `heldout_episodes.jsonl`:
  `python3 analysis_b1_b2.py` (10,000 bootstrap resamples, seed 42).
- `analysis_b1_b2_output.json` — that script's output from 2026-10-24.
  It reproduces the B1/B2 numbers within bootstrap Monte-Carlo variation;
  every conclusion is unchanged.
- `data/heldout_episodes.jsonl` — per-seed scores for all 6 players ×
  100 held-out seeds (5000–5099, touched once).
- `data/summary.json` — the final-evaluation summary.
- `data/champion_evolution.json` / `data/champion_random_search.json` —
  the two champion weight vectors (evo-gen19-idx10, rs-310).
- `data/fitness_log_evolution.jsonl` / `data/fitness_log_random_search.jsonl`
  — fitness for all 640 + 640 candidates (compute-matching check).
- `data/curve_evolution.jsonl` / `data/curve_random_search.jsonl` —
  the probe-seed learning curves.

## Limitation of record

Exactly ONE training run per improver. Every interval here estimates
episode-sampling variability for the two particular frozen champion
policies — not reliability across independent training runs. This is
held-out evidence of policy improvement in one bounded optimization
experiment, not evidence that evolution reliably outperforms random
search across training runs. The comparison is candidate-matched
(640 candidates, 7,680 fitness episodes each), not equal-compute:
evolution used 1,863,336 logged training steps vs random search's
1,245,838, the control is local random search around the starting
recipe, and the held-out records are per-seed scores only — no action
sequences, so they are not full episode replay traces (Amendment B4).

## sha256 manifest

```
a8e0c9337f28c36446ae3373a5a74b2544a47b36fb58d07879bf45fe5953ea01  DESIGN.md
b41b691b0e591116609cf709e1ec6b3d3e81c5f9cdc7beef13d20880c3ac9991  STUDY_RESULTS.md
ad4563a231b46b205ca41c0c9601722dc6a8a3d4a911aab6c0113d3b7e7b9c6e  merge_engine.py
08b1689969e3c1775df10166c4e10023089c754ea48b9269cae76712c38d51f0  players.py
e718cfe377a5e943faac984af86523fc99dd05c02c081d5821bf8d29876cbffe  study.py
8c2f5d9c9bf5465c5e867f1a1c0f7f815492d7ce74154b5b5bf59ff334fda9dd  analysis_b1_b2.py
ff6d1a621a9c57888a7f8392ec80fd8206a1167ccabac794d2f4044bcd6d0048  analysis_b1_b2_output.json
0fae6f20e99f0e787e94809453444aa822e49bd06c8bfb75f290701a8ee8d77a  data/heldout_episodes.jsonl
20dce5ffd0ad5af9eb865b669fcdc3cb355e95bca06a7efaaa96f8f804330706  data/summary.json
1234a9acb41ab464376a8edb96ae8439212dcd95123327d56cac35e0be005498  data/champion_evolution.json
bfd63252d4d457ff672696235f8afc16c79f7fb41e98655a597936b17cae3bf0  data/champion_random_search.json
e90a0c70962ab945a45154efcce6c60e574c955621d8121a0a87da3a981971dc  data/fitness_log_evolution.jsonl
b05c7e957bba09338052702d4110a6ff5de6f387742283cf9d11407bbe7908c0  data/fitness_log_random_search.jsonl
dd879a92dde9d455f5634c98c98700ad08fbec8c47ae13492aaec0b388fe3ef9  data/curve_evolution.jsonl
0c507b72cadc5d7750005941f0b234f7c13f580c9aa9947a4a33894b257299e4  data/curve_random_search.jsonl
```

The first six hashes for DESIGN.md, merge_engine.py, players.py,
study.py, heldout_episodes.jsonl and summary.json are identical to the
manifest first posted in Slack on 2026-10-24 — those files are unchanged.
STUDY_RESULTS.md differs by the disclosed B3 amendment appended /
inserted after that posting, and by the disclosed B4 amendment (dot's
completed independent check and its qualifications) appended 2026-10-24.
