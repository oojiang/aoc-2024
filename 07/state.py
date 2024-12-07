from data_types import Equation
from typing import List

def read_input(filename: str = "input") -> List[Equation]:
    equations = []
    with open(filename, 'r') as file:
        for line in file:
            tokens = line.split()
            result = int(tokens.pop(0)[:-1])
            operands = list(map(int, tokens))

            equation = (result, operands)
            equations.append(equation)
    return equations
