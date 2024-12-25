from typing import List, Tuple
import re

REGISTER_REGEX = r'Register.*: (\d*)'
PROGRAM_REGEX = r'Program.*: (.*)'

def read_input(filename: str = "input") -> Tuple[List[int], List[int]]:
    registers = []
    program = []

    with open(filename, 'r') as file:
        file_str = file.read()
        registers = list(map(int, re.findall(REGISTER_REGEX, file_str)))

        program_str = re.search(PROGRAM_REGEX, file_str).group(1)
        matches = re.findall(r'\d+', program_str)
        program = list(map(int, matches))

    return registers, program
