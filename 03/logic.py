import re

MUL_INST_REGEX = r"mul\((\d{1,3}),(\d{1,3})\)"

def solution1(program: str) -> int:
    mul_instructions = re.findall(MUL_INST_REGEX, program)
    mul_values = map(lambda t: int(t[0])*int(t[1]), mul_instructions)
    return sum(mul_values)

INST_REGEX = MUL_INST_REGEX + r"|(do\(\))|(don't\(\))"

def solution2(program: str) -> int:
    instructions = re.findall(INST_REGEX, program)

    total = 0
    mul_enabled = True
    for instr in instructions:
        if instr[2]:
            mul_enabled = True
        elif instr[3]:
            mul_enabled = False
        elif mul_enabled:
            total += int(instr[0]) * int(instr[1])
    return total
