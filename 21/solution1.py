from typing import List
from state import read_input
from logic import get_shortest_keypress_sequence

test_codes = read_input("input1")
codes = read_input()

def solution1(codes: List[str]) -> int:
    sequences = [get_shortest_keypress_sequence(code) for code in codes]
    
    return sum(int(codes[i][:-1]) * len(sequences[i]) for i in range(len(codes)))

assert(solution1(test_codes) == 126384)
print(solution1(codes))
