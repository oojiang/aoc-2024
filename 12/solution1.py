from state import read_input
from logic import solution1

assert(solution1(read_input("input1")) == 140)
assert(solution1(read_input("input2")) == 772)
assert(solution1(read_input("input3")) == 1930)
print(solution1(read_input()))
