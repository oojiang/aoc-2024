from typing import List

def read_input(filename: str = "input") -> List[int]:
    connections = []
    with open(filename, 'r') as file:
        for line in file:
            connections.append(line.strip().split('-'))
    return connections
