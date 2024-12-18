from typing import Tuple, List
from data_types import Direction

WAREHOUSE = 'WAREHOUSE'
DIRECTIONS = 'DIRECTIONS'

STR_TO_DIRECTION = {
    "^": Direction.UP,
    "v": Direction.DOWN,
    "<": Direction.LEFT,
    ">": Direction.RIGHT,
}

def read_input(filename: str = "input") -> Tuple[List[List[str]], List[Direction]]:
    warehouse = []
    directions = []

    parser_state = WAREHOUSE
    with open(filename, 'r') as file:
        for line in file:
            if line == '\n':
                parser_state = DIRECTIONS
            elif parser_state == WAREHOUSE:
                warehouse.append(list(line[:-1]))
            else:
                directions += [STR_TO_DIRECTION[s] for s in list(line[:-1])]

    return warehouse, directions

EXPAND = {
    '#': list('##'),
    'O': list('[]'),
    '.': list('..'),
    '@': list('@.'),
}

def read_input2(filename: str = "input") -> Tuple[List[List[str]], List[Direction]]:
    warehouse = []
    directions = []

    parser_state = WAREHOUSE
    with open(filename, 'r') as file:
        for line in file:
            if line == '\n':
                parser_state = DIRECTIONS
            elif parser_state == WAREHOUSE:
                expanded_line = []
                for square in line[:-1]:
                    expanded_line += EXPAND[square]
                warehouse.append(expanded_line)
            else:
                directions += [STR_TO_DIRECTION[s] for s in list(line[:-1])]

    return warehouse, directions
