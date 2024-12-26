from typing import List, Tuple

def read_input(filename: str = "input") -> List[Tuple[int, int]]:
    coordinates = []
    with open(filename, 'r') as file:
        for line in file:
            coord = tuple(map(int, line.split(",")))
            coordinates.append(coord)
    return coordinates
