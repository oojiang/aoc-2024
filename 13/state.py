from typing import List, Tuple

import re

PATTERN = r"[^\d]+(\d+)[^\d]+(\d+)"

def read_input(filename: str = "input") -> List[Tuple]:
    machines = []

    state = 1
    with open(filename, 'r') as file:
        lines = []
        for line in file:
            if state == 0:
                machines.append(lines_to_vecs(lines))
                lines = []
            else:
                lines.append(line)
            state = (state + 1) % 4
        if len(lines) == 3:
            machines.append(lines_to_vecs(lines))
            lines = []
        
    return machines

def lines_to_vecs(lines: List[str]) -> Tuple:
    vec_a = list(map(int, re.findall(PATTERN, lines[0])[0]))
    vec_b = list(map(int, re.findall(PATTERN, lines[1])[0]))
    prize = list(map(int, re.findall(PATTERN, lines[2])[0]))
    return vec_a, vec_b, prize

