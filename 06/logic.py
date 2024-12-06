from data_types import Map, State, Position
from typing import Set
import copy

def solution1(map: Map, state: State) -> int:
    seen_positions = positions_on_path(map, state)
        
    return len(seen_positions)

def solution2(map: Map, state: State) -> int:
    _, starting_position, _ = state

    # get all positions on guard's current path.
    seen_positions = positions_on_path(map, state)
    
    # for each position on the guard's current path, check if putting an obstacle there causes a loop.
    total_looping_obstacles = 0
    for position in seen_positions:
        if position == starting_position:
            continue
        new_map = copy.deepcopy(map)
        new_map[position[0]][position[1]] = "O"

        if does_loop(new_map, state):
            total_looping_obstacles += 1

    return total_looping_obstacles

def positions_on_path(map: Map, state: State) -> Set[Position]:
    on_map, position, _ = state
    seen_positions = set()
    seen_positions.add(position)

    while on_map:
        state = move_guard(map, state)
        on_map, position, _ = state
        seen_positions.add(position)

    return seen_positions

def move_guard(map: Map, state: State) -> State:
    _, position, direction = state

    new_position = (position[0] + direction.vec[0], position[1] + direction.vec[1])
    new_direction = direction.turn()

    if not is_on_map(map, new_position):
        return False, position, direction
    
    if map[new_position[0]][new_position[1]] == ".":
        return True, new_position, direction
    else:
        return True, position, new_direction

def is_on_map(map: Map, position: Position):
    r, c = position
    return 0 <= r < len(map) and 0 <= c < len(map[r])

def does_loop(map: Map, state: State) -> bool:
    on_map, _, _ = state
    seen_states = set()
    seen_states.add(state)

    while on_map:
        state = move_guard(map, state)

        if state in seen_states:
            return True
        
        seen_states.add(state)
        on_map, _, _ = state

    return False


