from typing import List, Tuple, TypeAlias
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

    def move_back(self, r: int, c: int) -> Tuple[int, int]:
        r_ = r - self.vec[0]
        c_ = c - self.vec[1]
        return r_, c_

CHEAT_TIME = 2
MAX_CHEAT_TIME = 20

def solution1(racetrack: List[List[str]], target_time_saved: int = 100) -> int:
    times = get_times_honest(racetrack)
    cheats = get_cheats(racetrack, times)
    return sum(map(lambda t: t >= target_time_saved, cheats))
        

def get_times_honest(racetrack: List[List[str]]) -> List[List[int]]:
    times = [[-1 for _ in row] for row in racetrack]
    start, end = find_start_end(racetrack)

    t = 0
    r, c = start
    times[r][c] = t

    while (r, c) != end:
        t += 1
        for direction in Direction:
            r_, c_ = direction.move(r, c)
            if len(racetrack) > r_ >= 0 and len(racetrack[0]) > c_ >= 0 \
                and racetrack[r_][c_] in ['.', 'E'] and times[r_][c_] == -1:
                r, c = r_, c_
                times[r][c] = t
                break
    return times

def get_cheats(racetrack: List[List[str]], times: List[List[int]], cheat_time: int = CHEAT_TIME) -> List[int]:
    _, end = find_start_end(racetrack)
    end_time = times[end[0]][end[1]]

    cheats = []
    for r in range(len(racetrack)):
        for c in range(len(racetrack[0])):
            if racetrack[r][c] == '#':
                for direction in Direction:
                    r_start, c_start = direction.move_back(r, c)
                    r_end, c_end = direction.move(r, c)
                    if len(racetrack) > r_start >= 0 and len(racetrack[0]) > c_start >= 0 \
                        and len(racetrack) > r_end >= 0 and len(racetrack[0]) > c_end >= 0 \
                        and times[r_start][c_start] >= 0 and times[r_end][c_end] >= 0 \
                        and times[r_start][c_start] < times[r_end][c_end]:
                        cheats.append(times[r_end][c_end] - times[r_start][c_start] - cheat_time)
    return cheats
    
def find_start_end(racetrack: List[List[str]]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    start = (-1, -1)
    end = (-1, -1)
    for r in range(len(racetrack)):
        for c in range(len(racetrack[0])):
            if racetrack[r][c] == 'S':
                start = (r, c)
            elif racetrack[r][c] == 'E':
                end = (r, c)
    return start, end

def solution2(racetrack: List[List[str]], target_time_saved: int = 100) -> int:
    path = get_path(racetrack)
    cheats = get_cheats2(racetrack, path)
    counts = {}
    return sum(map(lambda t: t >= target_time_saved, cheats))

def get_path(racetrack: List[List[str]]) -> List[Tuple[int, int]]:
    path = []
    seen = set()
    start, end = find_start_end(racetrack)

    r, c = start
    path.append((r,c))
    seen.add((r, c))

    while (r, c) != end:
        for direction in Direction:
            r_, c_ = direction.move(r, c)
            if len(racetrack) > r_ >= 0 and len(racetrack[0]) > c_ >= 0 \
                and racetrack[r_][c_] in ['.', 'E'] \
                and (r_, c_) not in seen:
                r, c = r_, c_
                path.append((r, c))
                seen.add((r, c))
                break
    return path

def get_cheats2(
    racetrack: List[List[str]], 
    path: List[Tuple[int, int]], 
    max_cheat_time: int = MAX_CHEAT_TIME
    ) -> List[int]:
    cheats = []

    for start in range(len(path)):
        for end in range(start + 1, len(path)):
            r_start, c_start = path[start]
            r_end, c_end = path[end]
            cheat_time = abs(r_end - r_start) + abs(c_end - c_start)
            time_saved = end - start - cheat_time
            if cheat_time <= max_cheat_time:
                cheats.append(time_saved)
    return cheats
