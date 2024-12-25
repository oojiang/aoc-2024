from computer import Computer
from state import read_input

registers, program = read_input()

previous = [0]
for i in range(len(program)):
    candidates = []
    for prev_a in previous:
        for a in range(8):
            comp = Computer(registers, program)
            cand_a = prev_a << 3 | a
            comp.a = cand_a
            output = comp.run()
            if output == program[-1-i:]:
                candidates.append(cand_a)
    previous = candidates

print(sorted(previous)[0])
