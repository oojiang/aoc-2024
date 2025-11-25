from state import read_input
from gates import Gate

gates = read_input('input1')

def solution1(gates):
    zgates = {}
    for gate in gates:
        if gate[0] == 'z':
            zgates[int(gate[1:])] = gates[gate].compute()

    curr = 0
    result = ''
    while curr in zgates:
        result = str(zgates[curr]) + result
        curr += 1
    return int(result, 2)

assert(solution1(gates) == 4)

Gate.gates = {}
gates = read_input('input2')

assert(solution1(gates) == 2024)

Gate.gates = {}
gates = read_input('input')
print(solution1(gates))
