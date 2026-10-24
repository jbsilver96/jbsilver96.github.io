"""MERGE players — frozen definitions per DESIGN.md (engine merge-py-1.0).

Weight vector layout (22): [0..15] positional weights over exponents,
[16] empty, [17] merge-potential, [18] monotonicity, [19] roughness,
[20] corner, [21] sum-of-exponents.
Feature conventions (DESIGN.md §3 + Amendment A1):
  empty   = number of empty cells (>= 0)
  merge   = sum over adjacent equal nonzero pairs of the shared exponent (>= 0)
  mono    = sum over rows+cols of -min(drops, rises) along the line (<= 0)
  rough   = sum over adjacent pairs of |exponent difference| (>= 0)
  corner  = max exponent if the (first) max tile is at cell 12 else 0
  sumexp  = sum of exponents
"""
import random
from merge_engine import apply_move, exponents

PAIRS = []
for r in range(4):
    for c in range(4):
        i = r * 4 + c
        if c < 3:
            PAIRS.append((i, i + 1))
        if r < 3:
            PAIRS.append((i, i + 4))
LINES = []
for r in range(4):
    LINES.append([r * 4 + c for c in range(4)])
for c in range(4):
    LINES.append([r * 4 + c for r in range(4)])
CORNER_CELL = 12


def global_features(e):
    empty = sum(1 for v in e if v == 0)
    merge = 0
    rough = 0
    for a, b in PAIRS:
        if e[a] and e[a] == e[b]:
            merge += e[a]
        rough += abs(e[a] - e[b])
    mono = 0
    for line in LINES:
        drops = 0
        rises = 0
        for i in range(3):
            d = e[line[i]] - e[line[i + 1]]
            if d > 0:
                drops += d
            else:
                rises -= d
        mono -= min(drops, rises)
    mx = max(e)
    corner = mx if e[CORNER_CELL] == mx and mx > 0 else 0
    return [empty, merge, mono, rough, corner, sum(e)]


def evaluate(weights, board):
    e = exponents(board)
    v = 0.0
    for i in range(16):
        if e[i]:
            v += weights[i] * e[i]
    gf = global_features(e)
    for j in range(6):
        v += weights[16 + j] * gf[j]
    return v


def make_weight_policy(weights):
    w = list(weights)

    def policy(board, legal, score, moves):
        best_mv, best_v = None, None
        for mv in legal:  # legal is in fixed order; strict > keeps lowest index on ties
            nb, _, _ = apply_move(board, mv)
            v = evaluate(w, nb)
            if best_v is None or v > best_v:
                best_v, best_mv = v, mv
        return best_mv

    return policy


def random_policy(rng):
    def policy(board, legal, score, moves):
        return rng.choice(legal)

    return policy


def greedy_policy(board, legal, score, moves):
    best_mv, best_key = None, None
    for mv in legal:
        nb, gain, _ = apply_move(board, mv)
        empt = sum(1 for v in exponents(nb) if v == 0)
        key = (gain, empt, -mv)
        if best_key is None or key > best_key:
            best_key, best_mv = key, mv
    return best_mv


def _initial_positional():
    w = []
    for idx in range(16):
        r, c = divmod(idx, 4)
        d = abs(3 - r) + abs(0 - c)  # Manhattan distance to cell 12 = (3,0)
        w.append(16 - 2.5 * d)
    return w


INITIAL_W = _initial_positional() + [1.0, 0.0, 0.0, 0.0, 0.0, 0.0]
SNAKE_W = [1, 2, 3, 4, 8, 7, 6, 5, 9, 10, 11, 12, 16, 15, 14, 13] + [
    270.0, 55.0, 40.0, -12.0, 120.0, 8.0,
]
