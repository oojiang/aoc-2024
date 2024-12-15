from typing import List, Tuple, Set, TypeAlias
from enum import Enum

Plot: TypeAlias = Tuple[int, int]

class Direction(Enum):
    UP      = (-1,  0)
    DOWN    = ( 1,  0)
    LEFT    = ( 0, -1)
    RIGHT   = ( 0,  1)

    def __init__(self, x, y):
        self.vec = (x, y)

def solution1(garden: List[List[str]]) -> int:
    return get_price(garden, get_areas(garden))

# Returns a matrix with the area of the region that a plot belongs to.
def get_areas(garden: List[List[str]]) -> List[List[int]]:
    regions = get_regions(garden)

    areas = [[len(region) for region in row] for row in regions]
    return areas

def get_regions(garden: List[List[str]]) -> List[List[Set[Plot]]]:
    region = [[set([(r,c)]) for c in range(len(garden[0]))] for r in range(len(garden))]

    for r in range(len(garden)):
        for c in range(len(garden[0])):
            for direction in (Direction.UP, Direction.LEFT):
                if not is_border(garden, r, c, direction):
                    adj_r = r + direction.vec[0]
                    adj_c = c + direction.vec[1]
                    if region[adj_r][adj_c] is not region[r][c]:
                        region[adj_r][adj_c].update(region[r][c])
                        for region_r, region_c in region[r][c]:
                            region[region_r][region_c] = region[adj_r][adj_c]

    return region
    

def get_price(garden: List[List[str]], area: List[List[int]]) -> int:
    price = 0
    for r in range(len(garden)):
        for c in range(len(garden[0])):
            for direction in Direction:
                if is_border(garden, r, c, direction):
                    price += area[r][c]
    return price

def is_border(garden, r, c, direction):
    adj_r = r + direction.vec[0]
    adj_c = c + direction.vec[1]
    if len(garden) > adj_r >= 0 and len(garden[0]) > adj_c >= 0:
        return garden[adj_r][adj_c] != garden[r][c]
    else:
        return True

def print_matrix(matrix):
    for row in matrix:
        for ele in row:
            print(ele, end='\t')
        print()

def print_garden_areas(garden, area):
    for r in range(len(garden)):
        for c in range(len(garden[0])):
            print(garden[r][c], area[r][c], end='\t')
        print()

