from typing import Tuple, List
from data_types import Direction
import copy

def solution1(warehouse: List[List[str]], directions: List[Direction]) -> int:
    warehouse = copy.deepcopy(warehouse)

    r, c = find_robot(warehouse)

    for direction in directions:
        if move(warehouse, r, c, direction):
            r, c = direction.move(r, c)

    gps_coordinate_sum = 0
    for r in range(len(warehouse)):
        for c in range(len(warehouse[0])):
            if warehouse[r][c] == 'O':
                gps_coordinate_sum += gps_coordinate(r, c)

    return gps_coordinate_sum

'''
Modifies warehouse by moving the thing in (r, c) in the given direction.
Returns True if it was successfully moved. False otherwise.
'''
def move(warehouse: List[List[str]], r: int, c: int, direction: Direction) -> bool:
    if warehouse[r][c] == '.':
        return True
    elif warehouse[r][c] == '#':
        return False
    else: # '@' or 'O'
        r_, c_ = direction.move(r, c)
        if move(warehouse, r_, c_, direction):
            warehouse[r_][c_] = warehouse[r][c]
            warehouse[r][c] = '.'
            return True
        else:
            return False

def find_robot(warehouse: List[List[str]]) -> Tuple[int, int]:
    for r in range(len(warehouse)):
        for c in range(len(warehouse[0])):
            if warehouse[r][c] == '@':
                return r, c
    return -1, -1

def gps_coordinate(r: int, c: int) -> int:
    return 100 * r + c
