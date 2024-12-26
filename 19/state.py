from typing import List, Tuple

def read_input(filename: str = "input") -> Tuple[List[str], List[str]]:
    desired = []
    with open(filename, 'r') as file:
        lines = iter(file.readlines())

        available = next(lines).strip().split(', ')

        next(lines)

        for line in lines:
            desired.append(line.strip())

    return available, desired
