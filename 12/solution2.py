from state import read_input
from logic import solution2

assert(solution2(read_input("input1")) == 80)
assert(solution2(read_input("input2")) == 436)
assert(solution2(read_input("input4")) == 236)
assert(solution2(read_input("input5")) == 368)
assert(solution2(read_input("input3")) == 1206)
print(solution2(read_input()))
