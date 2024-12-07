from data_types import Equation
from typing import List
from enum import Enum

class Operator(Enum):
    ADD = '+'
    MULTIPLY = '*'

    def apply(self, int1: int, int2: int) -> int:
        if self == Operator.ADD:
            return int1 + int2
        else:
            return int1 * int2

def solution1(equations: List[Equation]):
    total = 0
    for equation in equations:
        if is_possible(equation):
            result, _ = equation
            total += result
    return total

def is_possible(equation: Equation):
    expected_result, operands = equation
    
    queue = [[Operator.ADD for _ in range(len(operands) - 1)]]
    while queue:
        operators = queue.pop()
        result = compute_result(operands, operators)
        if result == expected_result:
            return True
        else:
            queue = queue + get_next_operators(operators)
    return False
        
def compute_result(operands: List[int], operators: List[Operator]) -> int:
    result = operands[0]
    for i in range(len(operators)):
        result = operators[i].apply(result, operands[i+1])
    return result

def get_next_operators(operators: List[Operator]) -> List[List[Operator]]:
    next_operators = []
    for i in range(len(operators)):
        if operators[i] == Operator.ADD:
            next_operators.append(
                [Operator.MULTIPLY if j == i else operators[j] for j in range(len(operators))]
            )
    return next_operators
            
