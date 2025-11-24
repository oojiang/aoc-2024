from typing import List

def read_input(filename: str = "input") -> List[int]:
    secrets = []
    with open(filename, 'r') as file:
        for line in file:
            secrets.append(int(line.strip()))
    return secrets

