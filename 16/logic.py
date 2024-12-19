from typing import List, Tuple, Dict
from data_types import Coor, Direction, State

MOVE_COST = 1
TURN_COST = 1000

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

    '''
    Sets the score if it is less than the current score.
    Returns whether or not the score was set.
    '''
    def set_score(self, state: State, score: float) -> bool:
        (r, c), direction = state
        current_score = self.get_score(state)
        if score < current_score:
            self.array[r][c][direction.index()] = score
            return True
        return False

'''
My strategy is to keep track of the smallest score you need to reach each square from the start.
'''
def solution1(maze: List[List[str]]) -> float:
    _, end = get_start_and_end(maze)
    scores = get_scores(maze)
    return min([scores.get_score((end, direction)) for direction in Direction])

def solution2(maze: List[List[str]]) -> int:
    scores = get_scores(maze)
    on_path = trace_path(maze, scores)
    count = 0
    for row in on_path:
        for tile in row:
            count += tile
    return count
    

def get_scores(maze: List[List[str]]) -> Scores:
    start, _ = get_start_and_end(maze)
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

    return scores

'''
Using scores, trace the paths in the maze and return an array marking which tiles are on the paths.
'''
def trace_path(maze: List[List[str]], scores: Scores) -> List[List[bool]]:
    start, end = get_start_and_end(maze)
    on_path = [[False for _ in row] for row in maze]

    queue = []

    end_states = [(end, direction) for direction in Direction]
    min_score = min([scores.get_score(state) for state in end_states])
    for state in end_states:
        if scores.get_score(state) == min_score:
            queue.append(state)
    
    while queue:
        state = queue.pop()
        (r, c), _ = state
        on_path[r][c] = True

        move_state = move_backwards(state)
        turn_cw_state = turn_cw(state)
        turn_ccw_state = turn_ccw(state)

        if scores.get_score(state) - scores.get_score(move_state) == MOVE_COST:
            queue.append(move_state)
        if scores.get_score(state) - scores.get_score(turn_cw_state) == TURN_COST:
            queue.append(turn_cw_state)
        if scores.get_score(state) - scores.get_score(turn_ccw_state) == TURN_COST:
            queue.append(turn_ccw_state)
        
    return on_path
        
def move(state: State) -> State:
    coor, direction = state
    return (direction.move(coor), direction)

def turn_cw(state: State) -> State:
    coor, direction = state
    return (coor, direction.turn_clockwise())

def turn_ccw(state: State) -> State:
    coor, direction = state
    return (coor, direction.turn_counterclockwise())

def move_backwards(state: State) -> State:
    coor, direction = state
    return (direction.turn_around().move(coor), direction)

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
