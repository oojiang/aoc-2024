from typing import List, Tuple, Set, TypeAlias
from enum import Enum

Map: TypeAlias = List[List[int]]
Coor: TypeAlias = Tuple[int, int]
Trail: TypeAlias = List[Coor]

class Direction(Enum):
    UP      = (-1,  0)
    DOWN    = ( 1,  0)
    LEFT    = ( 0, -1)
    RIGHT   = ( 0,  1)

    def __init__(self, x, y):
        self.vec = (x, y)

SUMMIT = 9


def solution1(topomap: List[List[int]]) -> int:
    trailheads = get_trailheads(topomap)
    summits = get_accessible_summits(topomap)

    total_score = 0
    for r, c in trailheads:
        total_score += len(summits[r][c])
    return total_score

def solution2(topomap: List[List[int]]) -> int:
    trailheads = get_trailheads(topomap)
    num_trails = get_num_trails(topomap)

    total_score = 0
    for r, c in trailheads:
        total_score += num_trails[r][c]
    return total_score

def get_trailheads(topomap: List[List[int]]) -> List[Coor]:
    trailheads = []
    for r in range(len(topomap)):
        for c in range(len(topomap[0])):
            if topomap[r][c] == 0:
                trailheads.append((r,c))
    return trailheads

'''
Returns a 2D array of Sets of Coors.
Each element in the array represents the set of summits accessible from that coordinate.
'''
def get_accessible_summits(topomap: List[List[int]]) -> List[List[Set[Coor]]]:
    summits = [[set() for _ in range(len(topomap[0]))] for _ in range(len(topomap))]
    for r in range(len(topomap)):
        for c in range(len(topomap[0])):
            if topomap[r][c] == SUMMIT:
                summits[r][c].add((r, c))

    for i in reversed(range(SUMMIT + 1)):
        for r in range(len(topomap)):
            for c in range(len(topomap[0])):
                if topomap[r][c] == i:
                    for direction in Direction:
                        new_r = r + direction.vec[0]
                        new_c = c + direction.vec[1]
                        if len(topomap) > new_r >= 0 \
                            and len(topomap[0]) > new_c >= 0 \
                            and topomap[new_r][new_c] == i - 1:
                                summits[new_r][new_c].update(summits[r][c])
    return summits

def get_num_trails(topomap: List[List[int]]) -> List[List[int]]:
    num_trails = [[0 for _ in range(len(topomap[0]))] for _ in range(len(topomap))]
    for r in range(len(topomap)):
        for c in range(len(topomap[0])):
            if topomap[r][c] == SUMMIT:
                num_trails[r][c] = 1

    for i in reversed(range(SUMMIT + 1)):
        for r in range(len(topomap)):
            for c in range(len(topomap[0])):
                if topomap[r][c] == i:
                    for direction in Direction:
                        new_r = r + direction.vec[0]
                        new_c = c + direction.vec[1]
                        if len(topomap) > new_r >= 0 \
                            and len(topomap[0]) > new_c >= 0 \
                            and topomap[new_r][new_c] == i - 1:
                                num_trails[new_r][new_c] += num_trails[r][c]
    return num_trails
