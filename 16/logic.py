from typing import List, Tuple, Dict
from data_types import Coor, Direction, State

MOVE_COST = 1
TURN_COST = 1000


'''
My strategy is to keep track of the smallest score you need to reach each square from the start.
'''
def solution1(maze: List[List[str]]) -> float:
    start, end = get_start_and_end(maze)
    start_state = (start, Direction.RIGHT)

    scores = Scores(maze)
    scores.set_score(start_state, 0)

    queue = []
    queue.append(start_state)

    while queue:
        state = queue.pop(0)

        move_state = move(state)
        (r, c), _ = move_state
        if maze[r][c] != '#':
            if scores.set_score(move_state, MOVE_COST + scores.get_score(state)):
                queue.append(move_state)

        turn_cw_state = turn_cw(state)
        if scores.set_score(turn_cw_state, TURN_COST + scores.get_score(state)):
            queue.append(turn_cw_state)

        turn_ccw_state = turn_ccw(state)
        if scores.set_score(turn_ccw_state, TURN_COST + scores.get_score(state)):
            queue.append(turn_ccw_state)

    return min([scores.get_score((end, direction)) for direction in Direction])
        
        
def move(state: State) -> State:
    coor, direction = state
    return (direction.move(coor), direction)

def turn_cw(state: State) -> State:
    coor, direction = state
    return (coor, direction.turn_clockwise())

def turn_ccw(state: State) -> State:
    coor, direction = state
    return (coor, direction.turn_counterclockwise())


def get_start_and_end(maze: List[List[str]]) -> Tuple[Coor, Coor]:
    start = (-1, -1)
    end = (-1, -1)
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)
    return start, end

'''
Wrapper over a 3D array with dimensions len(maze) x len(maze[0]) x len(Direction).
Its only purpose is to make the syntax for accessing the 3D array less hectic.
'''
class Scores:
    def __init__(self, maze: List[List[str]]):
        self.array = [[[float('inf') for _ in Direction] for _ in row] for row in maze]

    def get_score(self, state: State):
        (r, c), direction = state
        return self.array[r][c][direction.index()]

    def set_score(self, state: State, score: float) -> bool:
        (r, c), direction = state
        current_score = self.get_score(state)
        if score < current_score:
            self.array[r][c][direction.index()] = score
            return True
        return False
        
