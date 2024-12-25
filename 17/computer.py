from typing import List

class Computer:
    def __init__(self, registers: List[int], program):
        self.a = registers[0]
        self.b = registers[1]
        self.c = registers[2]
        self.inst_ptr = 0
        self.program = program
        self.output = []
        self.instructions = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }

    def combo(self, operand):
        if operand in range(4):
            return operand
        elif operand == 4:
            return self.a
        elif operand == 5:
            return self.b
        elif operand == 6:
            return self.c
        else:
            assert False, "Combo operand 7 is reserved and will not appear in valid programs."

    def adv(self, operand):
        self.a = self.a // (2 ** self.combo(operand))

    def bxl(self, operand):
        self.b = self.b ^ operand

    def bst(self, operand):
        self.b = self.combo(operand) % 8

    def jnz(self, operand):
        if self.a == 0:
            return
        self.inst_ptr = operand - 2

    def bxc(self, operand):
        self.b = self.b ^ self.c

    def out(self, operand):
        self.output.append(
            self.combo(operand) % 8
        )

    def bdv(self, operand):
        self.b = self.a // (2 ** self.combo(operand))

    def cdv(self, operand):
        self.c = self.a // (2 ** self.combo(operand))
        

    def run(self):
        while self.inst_ptr in range(len(self.program)):
            opcode = self.program[self.inst_ptr]
            operand = self.program[self.inst_ptr + 1]
            self.instructions[opcode](operand)
            self.inst_ptr += 2
        return list(self.output)
