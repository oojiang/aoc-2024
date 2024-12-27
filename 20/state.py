from typing import List

def read_input(filename: str = "input") -> List[List[str]]:
    racetrack = []
    with open(filename, 'r') as file:
        for line in file:
            racetrack.append(list(line.strip()))
    return racetrack
