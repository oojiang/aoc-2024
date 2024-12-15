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
