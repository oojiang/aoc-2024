from typing import List
from gates import Gate, Input, And, Or, Xor

def read_input(filename: str = "input"):
    branching = False
    with open(filename, 'r') as file:
        for line in file:
            if not line.strip():
                branching = True
            elif not branching:
                parsed = line.strip().split(': ')
                name = parsed[0]
                value = int(parsed[1])
                Input(name, value)
            else:
                parsed = line.strip().split(' ')
                left = parsed[0]
                gate_type = parsed[1]
                right = parsed[2]
                name = parsed[4]
                {
                    'AND': And,
                    'OR': Or,
                    'XOR': Xor,
                }[gate_type](name, left, right)
    return Gate.gates
