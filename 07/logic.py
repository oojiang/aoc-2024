from data_types import Equation
from typing import List
from enum import Enum

def solution1(equations: List[Equation]):
    total = 0
    for equation in equations:
        if is_possible(equation):
            result, _ = equation
            total += result
    return total

def solution2(equations: List[Equation]):
    total = 0
    for equation in equations:
        if is_possible(equation, with_concat = True):
            result, _ = equation
            total += result
    return total


def is_possible(equation: Equation, with_concat: bool = False):
    expected_result, operands = equation

    if expected_result <= 0:
        return False
     
    if len(operands) == 1:
        return expected_result == operands[0]

    reduced_operands = operands[:-1]

    add_result = expected_result - operands[-1]
    add_equation = (add_result, reduced_operands)
    if is_possible(add_equation, with_concat):
        return True
    
    if expected_result % operands[-1] == 0:
        mul_result = expected_result // operands[-1]
        mul_equation = (mul_result, reduced_operands)
        if is_possible(mul_equation, with_concat):
            return True

    if with_concat:
        last = operands[-1]
        last_len = len(str(last))
        if len(str(expected_result)) > last_len:
            if str(expected_result)[-last_len:] == str(last):
                concat_result = int(str(expected_result)[:-last_len])
                concat_equation = (concat_result, reduced_operands)
                if is_possible(concat_equation, with_concat):
                    return True
        
    return False
