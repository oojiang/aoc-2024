from typing import List, Tuple, Set, Optional, TypeAlias
from enum import Enum
from itertools import product

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

def solution2(garden: List[List[str]]) -> int:
    areas = get_areas(garden)
    num_sides = get_num_sides(garden)
    regions = get_regions(garden)

    cost = 0
    for region in regions:
        r, c = next(iter(region))
        cost += areas[r][c] * num_sides[r][c]

    return cost

'''
Returns a matrix with the area of the region that each plot belongs to.
'''
def get_areas(garden: List[List[str]]) -> List[List[int]]:
    areas = [[1 for _ in row] for row in garden]
    visited = [[False for _ in row] for row in garden]

    for r in range(len(garden)):
        for c in range(len(garden[0])):
            if not visited[r][c]:
                region = get_region(garden, (r, c))
                for plot in region:
                    visited[plot[0]][plot[1]] = True
                    areas[plot[0]][plot[1]] = len(region)
    return areas

'''
Returns the set of plots in the region that a given plot is in.
'''
def get_region(garden: List[List[str]], plot: Plot) -> Set[Plot]:
    region = set()
    visited = [[False for _ in row] for row in garden]
    queue = []
    
    region.add(plot)
    visited[plot[0]][plot[1]] = True
    queue.append(plot)

    while queue:
        r, c = queue.pop()
        for direction in Direction:
            adj_r = r + direction.vec[0]
            adj_c = c + direction.vec[1]
            if len(garden) > adj_r >= 0 and len(garden[0]) > adj_c >= 0 \
                and not visited[adj_r][adj_c] \
                and garden[adj_r][adj_c] == garden[r][c]:
                visited[adj_r][adj_c] = True
                region.add((adj_r, adj_c))
                queue.append((adj_r, adj_c))

    return region

'''
Returns all regions in a garden.
A region is represented as a set of plots
'''
def get_regions(garden: List[List[str]]) -> List[Set[Plot]]:
    regions = []
    visited = [[False for _ in row] for row in garden]

    for r in range(len(garden)):
        for c in range(len(garden[0])):
            if not visited[r][c]:
                region = get_region(garden, (r, c))
                for plot in region:
                    visited[plot[0]][plot[1]] = True
                regions.append(region)

    return regions

'''
Returns a matrix with the number of sides of the region that each plot belongs to.
'''
def get_num_sides(garden: List[List[str]]) -> List[List[int]]:
    num_sides = [[0 for _ in row] for row in garden]
    regions = get_regions(garden)
    for region in regions:
        corners = get_corners_for_region(garden, region)
        for r, c in region:
            num_sides[r][c] = corners
        
    return num_sides

def get_corners_for_region(garden: List[List[str]], region: Set[Plot]) -> int:
    ex_r, ex_c = next(iter(region))
    label = garden[ex_r][ex_c]

    corners = 0
    for plot in region:
        r, c = plot
        if garden[r][c] == label:
            for vert_direction, horiz_direction in product([Direction.UP, Direction.DOWN], [Direction.LEFT, Direction.RIGHT]):
                if has_border(garden, (r, c), vert_direction) and has_border(garden, (r, c), horiz_direction):
                    corners += 1
                if not has_border(garden, (r, c), vert_direction) and not has_border(garden, (r, c), horiz_direction):
                    opp_r = r + vert_direction.vec[0] + horiz_direction.vec[0]
                    opp_c = c + vert_direction.vec[1] + horiz_direction.vec[1]
                    corners += (opp_r, opp_c) not in region
    return corners

def get_price(garden: List[List[str]], area: List[List[int]]) -> int:
    price = 0
    for r in range(len(garden)):
        for c in range(len(garden[0])):
            for direction in Direction:
                if has_border(garden, (r, c), direction):
                    price += area[r][c]
    return price

'''
Checks if a plot has a border in a particular direction
'''
def has_border(garden: List[List[str]], plot: Plot, direction: Direction, label: Optional[str] = None) -> bool:
    r, c = plot
    adj_r = r + direction.vec[0]
    adj_c = c + direction.vec[1]
    if len(garden) > adj_r >= 0 and len(garden[0]) > adj_c >= 0:
        return garden[adj_r][adj_c] != garden[r][c] and (label is None or garden[adj_r][adj_c] == label)
    else:
        return label is None
