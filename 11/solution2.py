from state import read_input
from logic import solution1, solution2

assert solution1(read_input(), 25) == solution2(read_input(), 25)
print(solution2(read_input(), 75))
