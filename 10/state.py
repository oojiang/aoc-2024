from typing import List

def read_input(filename: str = "input") -> List[List[int]]:
    topomap = []
    with open(filename, 'r') as file:
        for line in file:
            row = list(map(int, list(line[:-1])))
            topomap.append(row)
    return topomap
