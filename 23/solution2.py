from state import read_input
from logic import max_connected

test_connections = read_input("input1")
connections = read_input()

def solution2(connections):
    return ','.join(max_connected(connections))

assert(solution2(test_connections) == 'co,de,ka,ta')
print(solution2(connections))
