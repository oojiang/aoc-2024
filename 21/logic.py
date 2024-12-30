from typing import Dict, List, Tuple, TypeAlias
from enum import Enum

Coord: TypeAlias = Tuple[int, int]

class Keypress(Enum):
    UP          = (-1,  0,  "^")
    DOWN        = ( 1,  0,  "v")
    LEFT        = ( 0, -1,  "<")
    RIGHT       = ( 0,  1,  ">")
    ACTIVATE    = ( 0,  0,  "A")

    def __init__(self, r: int, c: int, symbol: str):
        self.vec = (r, c)
        self.symbol = symbol

    def move(self, coord: Coord) -> Coord:
        r, c = coord
        r_ = r + self.vec[0]
        c_ = c + self.vec[1]
        return r_, c_

KeypressCandidates = List[Keypress] | List['KeypressCandidates']
CodeCandidates = str | List['CodeCandidates']

class Keypad:
    def __init__(self, buttons: List[List[str]]):
        self.buttons = buttons
        self.locations : Dict[str, Coord] = {}
        self.start = (-1, -1)

        for r in range(len(buttons)):
            for c in range(len(buttons[0])):
                if buttons[r][c] != "":
                    self.locations[buttons[r][c]] = (r, c)
                if buttons[r][c] == 'A':
                    self.start = (r, c)
        assert self.start != (-1, -1)

    def button_at(self, coord: Coord) -> str:
        r, c = coord
        return self.buttons[r][c]

    def in_bounds(self, coord: Coord) -> bool:
        r, c = coord
        return len(self.buttons) > r >= 0 and len(self.buttons[0]) > c >= 0

    def can_move(self, start: Coord, keypress: Keypress) -> bool:
        end = keypress.move(start)
        return self.in_bounds(end) and self.button_at(end) != ""

    def move(self, start: Coord, keypress: Keypress) -> Coord:
        return keypress.move(start) 

numeric_keypad = Keypad([
    ['7','8','9'],
    ['4','5','6'],
    ['1','2','3'],
    [ '','0','A'],
])

directional_keypad = Keypad([
    [ '','^','A'],
    ['<','v','>'],
])

def get_shortest_keypress_sequence(numeric_code: str) -> str:
    # directional_code_0 (used by robot)
    key_press_candidates_0 = get_keypress_candidates(numeric_keypad, numeric_code)
    code_candidates_0 = keypress_to_code_candidates(key_press_candidates_0)

    # directional_code_1 (used by robot)
    key_press_candidates_1 = get_keypress_candidates(directional_keypad, code_candidates_0)
    code_candidates_1 = keypress_to_code_candidates(key_press_candidates_1)

    # directional_code_2 (used by me)
    key_press_candidates_2 = get_keypress_candidates(directional_keypad, code_candidates_1)
    code_candidates_2 = keypress_to_code_candidates(key_press_candidates_2)

    return get_shortest_code(code_candidates_2)

def get_shortest_code(code: CodeCandidates) -> str:
    if isinstance(code, str):
        return code
    elif isinstance(code[0], str):
        return sorted(code, key=len).pop(0) # type: ignore
    elif isinstance(code[0][0], str):
        return "".join(get_shortest_code(sub_code) for sub_code in code)
    else:
        return get_shortest_code([[get_shortest_code(code_00) for code_00 in code_0] for code_0 in code])

def keypress_to_code_candidates(keypress_candidates: KeypressCandidates) -> CodeCandidates:
    if isinstance(keypress_candidates[0], Keypress):
        return "".join(keypress.symbol for keypress in keypress_candidates) # type: ignore
    else:
        return [keypress_to_code_candidates(sub_candidate) for sub_candidate in keypress_candidates] # type: ignore

def get_keypress_candidates(keypad: Keypad, code: CodeCandidates) -> KeypressCandidates:
    if isinstance(code, str):
        sequence_segments = []

        current = keypad.start

        for c in code:
            target = keypad.locations[c]
            segment = get_keypress_candidates_for_next_button(keypad, current, target)
            sequence_segments.append(segment)
            current = target

        return sequence_segments
    else:
        return [
            get_keypress_candidates(keypad, sub_code) for sub_code in code
        ]

def get_keypress_candidates_for_next_button(keypad: Keypad, current: Coord, target: Coord) -> KeypressCandidates:
    sequences = []

    allowed_keypresses = []
    if current[0] > target[0]:
        allowed_keypresses.append(Keypress.UP)
    elif current[0] < target[0]:
        allowed_keypresses.append(Keypress.DOWN)
    if current[1] > target[1]:
        allowed_keypresses.append(Keypress.LEFT)
    elif current[1] < target[1]:
        allowed_keypresses.append(Keypress.RIGHT)

    queue = []
    queue.append((current, ()))
    
    while queue:
        current, path = queue.pop()

        if current == target:
            sequences.append(list(path + (Keypress.ACTIVATE,)))
        else:
            for keypress in allowed_keypresses:
                if keypad.can_move(current, keypress):
                    next_current = keypad.move(current, keypress)
                    queue.append((next_current, path + (keypress,)))
        
    return sequences
