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

def print_robots(robots, rdim, cdim):
    photo = [['.' for _ in range(cdim)] for _ in range(rdim)]
    for robot in robots:
        (xpos, ypos), _ = robot
        if photo[ypos][xpos] == '.':
            photo[ypos][xpos] = 0
        photo[ypos][xpos] += 1

    for row in photo:
        for square in row:
            print(square, end='')
        print()
