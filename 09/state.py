from data_types import FileId, BlockCount, File
from typing import List

def read_input(filename: str = "input") -> List[BlockCount]:
    with open(filename, 'r') as file:
        line = file.read()
    return list(map(int, line[:-1]))
