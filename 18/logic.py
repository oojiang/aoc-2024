from typing import List, Tuple
from enum import Enum

class Direction(Enum):
    UP      = (-1,  0)
    DOWN    = ( 1,  0)
    LEFT    = ( 0, -1)
    RIGHT   = ( 0,  1)

    def __init__(self, r: int, c: int) -> None:
        self.vec = (r, c)

    def move(self, r: int, c: int) -> Tuple[int, int]:
        r_ = r + self.vec[0]
        c_ = c + self.vec[1]
        return r_, c_

MEMORY_SIZE = 71
NUM_BYTES = 1024

def solution1(coordinates: List[Tuple[int, int]], nrows: int = MEMORY_SIZE, ncols: int = MEMORY_SIZE, nbytes: int = 1024) -> int:
    memory_space = get_memory_space(coordinates, nrows, ncols, nbytes)

    # for row in memory_space:
    #     for c in row:
    #         print(c, end='')
    #     print()

    seen = set()
    queue = []
    queue.append((0, 0, 0))
    seen.add((0,0))

    while queue:
        r, c, n = queue.pop(0)

        if r == nrows - 1 and c == ncols - 1:
            return n

        for direction in Direction:
            r_, c_ = direction.move(r, c)
            if (r_, c_) not in seen \
                and nrows > r_ >= 0 and ncols > c_ >= 0 \
                and memory_space[r_][c_] != '#':
                queue.append((r_, c_, n+1))
                seen.add((r_,c_))

    return -1 # No path exists

def get_memory_space(coordinates: List[Tuple[int, int]], nrows: int, ncols: int, nbytes: int) -> List[List[str]]:
    memory_space = []
    for _ in range(nrows):
        memory_space.append(['.' for _ in range(ncols)])
    
    for i in range(nbytes):
        c, r = coordinates[i]
        memory_space[r][c] = '#'

    return memory_space

def solution2(coordinates: List[Tuple[int, int]], nrows: int = MEMORY_SIZE, ncols: int = MEMORY_SIZE) -> Tuple[int, int]:
    lo = 0
    hi = len(coordinates) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        steps = solution1(coordinates, nrows, ncols, mid + 1)
        if steps == -1:
            hi = mid
        else:
            lo = mid + 1

    return coordinates[hi]
        
