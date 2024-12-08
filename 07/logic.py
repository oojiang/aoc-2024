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
    if len(operands) == 1:
        return expected_result == operands[0]

    reduced_operands = operands[:-1]
    
    add_result = expected_result - operands[-1]
    add_equation = (add_result, reduced_operands)
    if is_possible(add_equation):
        return True
    
    if expected_result % operands[-1] == 0:
        mul_result = expected_result // operands[-1]
        mul_equation = (mul_result, reduced_operands)
        if is_possible(mul_equation):
            return True
            
def compute_result(operands: List[int], operators: List[Operator]) -> int:
    result = operands[0]
    for i in range(len(operators)):
        result = operators[i].apply(result, operands[i+1])
    return result
