from typing import List
from logic import Scores
from data_types import Direction

def read_input(filename: str = "input") -> List[List[str]]:
    maze = []
    with open(filename, 'r') as file:
        for line in file:
            maze.append(list(line[:-1]))
    return maze

def print_maze(maze: List[List[str]]) -> None:
    for row in maze:
        for tile in row:
            print(tile, end='')
        print()

def print_scores(maze: List[List[str]], scores: Scores) -> None:
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == '#':
                print('#', end='\t')
            else:
                print(min([scores.get_score(((r,c), direction)) for direction in Direction]), end='\t')
        print()
