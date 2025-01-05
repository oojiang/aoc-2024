from typing import Dict
from functools import lru_cache
from itertools import permutations, pairwise

numeric_keypad = {
    '7' : (0, 0),
    '8' : (0, 1),
    '9' : (0, 2),
    '4' : (1, 0),
    '5' : (1, 1),
    '6' : (1, 2),
    '1' : (2, 0),
    '2' : (2, 1),
    '3' : (2, 2),
    '0' : (3, 1),
    'A' : (3, 2),
}

directional_keypad = {
    '^': (0, 1),
    'A': (0, 2),
    '<': (1, 0),
    'v': (1, 1),
    '>': (1, 2),
}

keypads = {
    'numeric': numeric_keypad,
    'directional': directional_keypad,
}

direction = {
    '^': (-1,  0),
    '<': ( 0, -1),
    'v': ( 1,  0),
    '>': ( 0,  1),
}

@lru_cache(maxsize=None)
def get_cost(start: str, end: str, keypad_name: str = 'directional', depth: int = 0) -> int:
    keypad = keypads[keypad_name]

    allowed_keypresses = []
    vertical = keypad[end][0] - keypad[start][0]
    horizontal = keypad[end][1] - keypad[start][1]
    if vertical > 0:
        allowed_keypresses += ['v'] * vertical
    else:
        allowed_keypresses += ['^'] * abs(vertical)
    if horizontal > 0:
        allowed_keypresses += ['>'] * horizontal
    else:
        allowed_keypresses += ['<'] * abs(horizontal)

    candidate_sequences = filter(
        lambda sequence: is_legal(start, sequence, keypad),
        [''.join(seq) + 'A' for seq in permutations(allowed_keypresses)]
    )

    candidate_costs = map(
        lambda sequence: get_sequence_cost(sequence, 'directional', depth - 1),
        candidate_sequences
    )

    return min(candidate_costs)

def get_sequence_cost(sequence: str, keypad_name: str, depth: int = 0) -> int:
    if depth <= 0:
        return len(sequence)

    cost = 0
    current = 'A'
    for target in sequence:
        cost += get_cost(current, target, keypad_name, depth)
        current = target
    return cost

def is_legal(start: str, sequence: str, keypad: Dict) -> bool:
    if sequence[-1] != 'A':
        return False
    current = keypad[start]
    for keypress in sequence[:-1]:
        delta = direction[keypress]
        current = current[0] + delta[0], current[1] + delta[1]
        if current not in keypad.values():
            return False
    return True
