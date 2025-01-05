from typing import List
from state import read_input
from logic2 import get_sequence_cost

test_codes = read_input("input1")
codes = read_input()

def solution1(codes: List[str]) -> int:
    score = 0
    for code in codes:
        score += int(code[:-1]) * get_sequence_cost(code, 'numeric', 3)
    return score

def solution2(codes: List[str]) -> int:
    score = 0
    for code in codes:
        score += int(code[:-1]) * get_sequence_cost(code, 'numeric', 26)
    return score

assert(solution1(test_codes) == 126384)
print(solution1(codes))
print(solution2(codes))
