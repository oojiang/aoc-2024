from typing import List

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
