from typing import List, Tuple
import re

PATTERN = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"

def read_input(filename: str = "input") -> List[Tuple[
    Tuple[int, int],
    Tuple[int, int]
]]:
    robots = []
    with open(filename, 'r') as file:
        for line in file:
            data = list(map(int, re.findall(PATTERN, line)[0]))
            robots.append((
                (data[0], data[1]),
                (data[2], data[3]),
            ))
    return robots

        
