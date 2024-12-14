from typing import List

def read_input(filename: str = "input") -> List[int]:
    with open(filename, 'r') as file:
        return list(map(int, file.read().split()))
