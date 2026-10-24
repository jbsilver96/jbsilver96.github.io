"""MERGE engine — canonical implementation, engine version merge-py-1.0.

Rules (frozen in DESIGN.md): 4x4 board, standard 2048 slide/merge (each tile
merges at most once per move, resolved from the leading edge), one spawn after
every board-changing move (cell uniform among empties; 2 with p=0.9 else 4),
all spawns from the episode's seeded PRNG. Replay identity = (engine version,
seed, action sequence).

Board representation: tuple of 4 row-integers; each row is 16 bits = 4 nibbles,
LOW nibble = leftmost cell. Cell index (row-major, 0 = top-left) of row r,
column c is r*4 + c; exponent e means tile value 2**e (0 = empty, cap 15).
"""
import random

ENGINE_VERSION = "merge-py-1.0"
UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3


def _slide_merge_left(row):
    """Slide+merge one 16-bit row toward the low-nibble (left) side.
    Returns (new_row, gain)."""
    cells = [row & 0xF, (row >> 4) & 0xF, (row >> 8) & 0xF, (row >> 12) & 0xF]
    tiles = [c for c in cells if c]
    out = []
    gain = 0
    i = 0
    while i < len(tiles):
        if i + 1 < len(tiles) and tiles[i] == tiles[i + 1]:
            merged = tiles[i] + 1
            out.append(merged)
            gain += 1 << merged
            i += 2
        else:
            out.append(tiles[i])
            i += 1
    while len(out) < 4:
        out.append(0)
    return out[0] | (out[1] << 4) | (out[2] << 8) | (out[3] << 12), gain


def _reverse_row(row):
    return ((row & 0xF) << 12) | ((row >> 4 & 0xF) << 8) | ((row >> 8 & 0xF) << 4) | (row >> 12 & 0xF)


LEFT_TABLE = {}
RIGHT_TABLE = {}
for _r in range(65536):
    _nl, _g = _slide_merge_left(_r)
    LEFT_TABLE[_r] = (_nl, _g)
    _rev = _reverse_row(_r)
    _nr, _g2 = _slide_merge_left(_rev)
    RIGHT_TABLE[_r] = (_reverse_row(_nr), _g2)


def exponents(board):
    """Board -> list of 16 exponents, row-major, 0 = top-left."""
    e = []
    for row in board:
        e += [row & 0xF, (row >> 4) & 0xF, (row >> 8) & 0xF, (row >> 12) & 0xF]
    return e


def _from_exponents(e):
    board = []
    for r in range(4):
        row = 0
        for c in range(4):
            row |= e[r * 4 + c] << (4 * c)
        board.append(row)
    return tuple(board)


def _transpose(board):
    e = exponents(board)
    t = [0] * 16
    for r in range(4):
        for c in range(4):
            t[c * 4 + r] = e[r * 4 + c]
    return _from_exponents(t)


def apply_move(board, move):
    """Apply a slide/merge (no spawn). Returns (new_board, gain, changed)."""
    gain = 0
    if move == LEFT:
        rows = []
        for row in board:
            nr, g = LEFT_TABLE[row]
            rows.append(nr)
            gain += g
        nb = tuple(rows)
    elif move == RIGHT:
        rows = []
        for row in board:
            nr, g = RIGHT_TABLE[row]
            rows.append(nr)
            gain += g
        nb = tuple(rows)
    elif move == UP:
        t = _transpose(board)
        rows = []
        for row in t:
            nr, g = LEFT_TABLE[row]
            rows.append(nr)
            gain += g
        nb = _transpose(tuple(rows))
    elif move == DOWN:
        t = _transpose(board)
        rows = []
        for row in t:
            nr, g = RIGHT_TABLE[row]
            rows.append(nr)
            gain += g
        nb = _transpose(tuple(rows))
    else:
        raise ValueError(move)
    return nb, gain, nb != board


def legal_moves(board):
    return [m for m in (UP, RIGHT, DOWN, LEFT) if apply_move(board, m)[2]]


def _spawn(board, rng):
    e = exponents(board)
    empties = [i for i, v in enumerate(e) if v == 0]
    if not empties:
        return board
    idx = rng.randrange(len(empties))
    val = 1 if rng.random() < 0.9 else 2  # exponent of 2 or 4
    e[empties[idx]] = val
    return _from_exponents(e)


def play_episode(seed, policy):
    """Play one episode. policy(board, legal, score, moves) -> move.
    Returns dict(seed, score, max_tile, moves, actions)."""
    rng = random.Random(seed)
    board = (0, 0, 0, 0)
    board = _spawn(board, rng)
    board = _spawn(board, rng)
    score = 0
    moves = 0
    actions = []
    while True:
        legal = legal_moves(board)
        if not legal:
            break
        mv = policy(board, legal, score, moves)
        if mv not in legal:
            raise ValueError(f"policy returned illegal move {mv}")
        board, gain, _ = apply_move(board, mv)
        score += gain
        moves += 1
        actions.append(mv)
        board = _spawn(board, rng)
    e = exponents(board)
    return {
        "seed": seed,
        "score": score,
        "max_tile": (1 << max(e)) if any(e) else 0,
        "moves": moves,
        "actions": actions,
    }


def replay(seed, actions):
    """Re-execute an episode from (seed, action sequence); determinism check."""
    rng = random.Random(seed)
    board = (0, 0, 0, 0)
    board = _spawn(board, rng)
    board = _spawn(board, rng)
    score = 0
    for mv in actions:
        board, gain, changed = apply_move(board, mv)
        assert changed, "recorded action was not board-changing"
        score += gain
        board = _spawn(board, rng)
    return score
