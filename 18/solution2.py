from state import read_input
from logic import solution2

assert(solution2(read_input("input1"), 7, 7) == (6, 1))
print(*solution2(read_input()), sep=',')