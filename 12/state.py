from typing import List

def read_input(filename: str = "input") -> List[List[int]]:
    garden = []
    with open(filename, 'r') as file:
        for line in file:
            garden.append(list(line[:-1]))
    return garden
