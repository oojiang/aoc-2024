from typing import Tuple, List
from data_types import Rule, Update

def read_input(filename: str = "input") -> Tuple[List[Rule], List[Update]]:
    rules = []
    updates = []
    with open(filename, 'r') as file:
        part = 1
        for line in file:
            if part == 1:
                if line.strip() == "":
                    part = 2
                else:
                    rule = tuple(map(int, line.split("|")))
                    rules.append(rule)
            else:
                update = list(map(int, line.split(",")))
                updates.append(update)
    return rules, updates
