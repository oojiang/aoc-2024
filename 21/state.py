from typing import List

def read_input(filename: str = "input") -> List[str]:
    codes = []
    with open(filename, 'r') as file:
        for line in file:
            codes.append(line.strip())
    return codes
        
