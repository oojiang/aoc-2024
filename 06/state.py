from data_types import Map, State, Direction
from typing import Tuple
import copy

def read_input(filename: str = "input") -> Tuple[Map, State]:
    map = []
    guard = (-1, -1)
    r = 0
    with open(filename, 'r') as file:
        for line in file:
            row = list(line)
            row.pop(-1)

            if "^" in row:
                c = row.index("^")
                guard = (r, c)
                row[c] = "."

            map.append(row)
            r += 1

    assert(guard != (-1, -1))
    return map, (True, guard, Direction.UP)

def print_state(map: Map, state: State):
    on_map, position, direction = state
    printable_map = copy.deepcopy(map)
    printable_map[position[0]][position[1]] = direction.symbol()
    for row in printable_map:
        print(row)
    print()
