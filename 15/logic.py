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

def solution2(warehouse: List[List[str]], directions: List[Direction]) -> int:
    warehouse = copy.deepcopy(warehouse)

    r, c = find_robot(warehouse)

    i = 1
    for direction in directions:
        print(f'{i} / {len(directions)}', end='\r')
        i += 1
        success, warehouse = move2(warehouse, r, c, direction)
        if success:
            r, c = direction.move(r, c)
    print()

    gps_coordinate_sum = 0
    for r in range(len(warehouse)):
        for c in range(len(warehouse[0])):
            if warehouse[r][c] == '[':
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

OTHER_HALF = {
    '[': Direction.RIGHT,
    ']': Direction.LEFT
}

'''
Returns (1) whether the move was successful and (2) the resulting warehouse.
'''
def move2(warehouse: List[List[str]], r: int, c: int, direction: Direction) -> Tuple[bool, List[List[str]]]:
    warehouse = copy.deepcopy(warehouse)
    if direction in [Direction.LEFT, Direction.RIGHT]:
        success = move(warehouse, r, c, direction)
        return success, warehouse
    
    if warehouse[r][c] == '.':
        return True, warehouse
    elif warehouse[r][c] == '#':
        return False, warehouse
    else:
        r_, c_ = direction.move(r, c)
        success, warehouse_ = move2(warehouse, r_, c_, direction)
        if not success:
            return False, warehouse

        if warehouse[r][c] == '@':
            warehouse_[r_][c_] = warehouse[r][c]
            warehouse_[r][c] = '.'
            return True, warehouse_

        r2, c2 = OTHER_HALF[warehouse[r][c]].move(r, c)
        r2_, c2_ = direction.move(r2, c2)

        success, warehouse__ = move2(warehouse_, r2_, c2_, direction)
        if not success:
            return False, warehouse

        warehouse__[r_][c_] = warehouse[r][c]
        warehouse__[r2_][c2_] = warehouse[r2][c2]
        warehouse__[r2][c2] = '.'
        return True, warehouse__

def find_robot(warehouse: List[List[str]]) -> Tuple[int, int]:
    for r in range(len(warehouse)):
        for c in range(len(warehouse[0])):
            if warehouse[r][c] == '@':
                return r, c
    return -1, -1

def gps_coordinate(r: int, c: int) -> int:
    return 100 * r + c
