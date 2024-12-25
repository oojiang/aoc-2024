from computer import Computer
from state import read_input

registers, program = read_input()
comp = Computer(registers, program)
output = comp.run()
print(','.join(list(map(str, output))))
