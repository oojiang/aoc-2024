from state import read_input
from logic import find_triplets, filter_for_chief

test_connections = read_input("input1")
connections = read_input()

def solution1(connections):
    return len(filter_for_chief(find_triplets(connections)))

assert(solution1(test_connections) == 7)
print(solution1(connections))
