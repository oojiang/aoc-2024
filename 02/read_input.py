from typing import List

def read_input(filename: str = "input") -> List[List[int]]:
    reports = []
    with open(filename, 'r') as file:
        for line in file:
            levels = list(map(int, line.split()))
            reports.append(levels)
    return reports
