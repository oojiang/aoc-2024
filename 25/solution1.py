from state import read_input
from logic import count_unique_pairs

locks, keys = read_input("input1")
assert count_unique_pairs(locks, keys) == 3, count_unique_pairs(locks, keys)

locks, keys = read_input()
print(count_unique_pairs(locks, keys))
